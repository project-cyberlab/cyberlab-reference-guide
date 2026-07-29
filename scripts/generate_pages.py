#!/usr/bin/env python3
"""Generate one reference page per captured, capability-mapped tool.

Mechanical by design. Everything on a generated page is derived from the tool's
own captured help text or from the kit catalogue -- nothing is invented here.
The judgement layer ("when you would use it", gotchas) is added afterwards by a
human or model and is marked so it is obvious what has been reviewed.

Existing hand-written pages are NEVER overwritten: a page is skipped if it
lacks the generated-marker.
"""
from __future__ import annotations
import json
import re
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from taxonomy import TAXONOMY  # noqa: E402
from helpparse import parse_options, parse_synopsis, parse_purpose  # noqa: E402

ROOT = HERE.parent
CAP = ROOT / "capture"
REF = ROOT / "reference"
MARKER = "<!-- generated-by: scripts/generate_pages.py -->"

COV = json.loads((CAP / "coverage.json").read_text(encoding="utf-8"))
KIT = json.loads((ROOT / "catalog" / "kit-tools.json").read_text(encoding="utf-8"))
CANDS = {}
cf = CAP / "cyberlab-candidates.json"
if cf.exists():
    CANDS = json.loads(cf.read_text(encoding="utf-8"))["tools"]


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


from candidates import ALIASES  # noqa: E402

# binary -> the kit-catalogue names that ship it, so `vol` resolves to
# "Volatility Framework" and `fls` to "The Sleuth Kit (TSK)".
BIN_TO_PKG: dict[str, set[str]] = {}
for _pkg, _bins in ALIASES.items():
    for _b in _bins:
        BIN_TO_PKG.setdefault(_b.lower(), set()).add(_pkg.lower())


def _norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.lower())


def kit_homes(cmd: str) -> tuple[list[str], str, str]:
    """Which kit VMs carry this tool, its documented purpose, and doc URL."""
    vms, purpose, url = [], "", ""
    low = cmd.lower()
    pkgs = BIN_TO_PKG.get(low, set())
    for vm, cats in KIT["kit"].items():
        for _cat, entries in cats.items():
            for e in entries:
                tool = e["tool"]
                names = {tool.lower()} | {b.lower() for b in (e.get("binaries") or [])}
                norms = {_norm(tool)} | {_norm(b) for b in (e.get("binaries") or [])}
                # Match on: exact name, normalised name, or a known package
                # alias ("Volatility Framework" ships `vol`).
                hit = (low in names or _norm(low) in norms
                       or bool(pkgs & {p for p in names})
                       or bool({_norm(p) for p in pkgs} & norms))
                if hit:
                    if vm not in vms:
                        vms.append(vm)
                    purpose = purpose or (e.get("purpose") or "")
                    url = url or (e.get("url") or "")
    return vms, purpose, url


# Attribution the catalogue cannot resolve on its own.
#
# Three cases: (1) suites whose manifest entry names the LIBRARY not the
# binaries -- the kit tracker lists "libyal libraries" with a Notes field of
# library names, never `evtxexport`; (2) suites shipped as a bundle (Eric
# Zimmerman's tools, folded into SIFT/FLARE by the kit build); (3) base OS
# utilities that no manifest names because every Linux image has them -- an
# analyst still needs to know they are always available.
FALLBACK_KIT: dict[str, list[str]] = {}
for _b in ["evtxexport", "evtxinfo", "esedbexport", "esedbinfo", "regfexport",
           "regfinfo", "regfmount", "vshadowinfo", "bdeinfo", "pffexport",
           "pffinfo", "ewfinfo", "ewfmount"]:
    FALLBACK_KIT[_b] = ["SIFT Workstation (libyal)"]
for _b in ["EvtxECmd", "MFTECmd", "PECmd", "RECmd", "AmcacheParser",
           "SrumECmd", "AppCompatCacheParser"]:
    FALLBACK_KIT[_b] = ["FLARE-VM / SIFT (Eric Zimmerman tools)"]
for _b in ["vol", "volatility3", "volshell"]:
    FALLBACK_KIT[_b] = ["SIFT Workstation (Volatility 3)"]
for _b in ["regipy-dump", "regipy-diff", "regipy-parse-header",
           "regipy-plugins-run", "regipy-plugins-list",
           "regipy-process-transaction-logs"]:
    FALLBACK_KIT[_b] = ["SIFT Workstation (regipy)"]
for _b in ["chainsaw", "hayabusa"]:
    FALLBACK_KIT[_b] = ["SIFT / Security Onion (Sigma-based log hunting)"]
for _b in ["grep", "less", "md5sum", "sha256sum", "stat", "strings", "xxd",
           "dd", "openssl", "readelf", "objdump", "file", "unzip", "patch"]:
    FALLBACK_KIT[_b] = ["Base OS — present on every Linux image"]


def clean_version(v: str) -> str:
    """Keep a version only when it looks like one.

    Tools that log on startup (volatility prints an INFO plugin-path banner)
    otherwise smuggle a paragraph into the header.
    """
    v = (v or "").strip()
    if not v or re.search(r"\b(INFO|WARNING|ERROR|Traceback)\b", v):
        return ""
    if re.search(r"(invalid|unknown|unrecognized)\s+option", v, re.I):
        return ""
    m = re.search(r"([A-Za-z][A-Za-z0-9 ._-]{0,40}?\s*v?\d+\.\d+(?:\.\d+)?)", v)
    if m:
        return m.group(1).strip()
    return v[:60] if len(v) <= 60 else ""


def capability_of(cmd: str) -> list[tuple[str, str]]:
    return [(ph, cap) for ph, caps in TAXONOMY.items()
            for cap, cmds in caps if cmd in cmds]


def siblings(cmd: str) -> list[str]:
    out: list[str] = []
    for _ph, cap in capability_of(cmd):
        for ph2, caps in TAXONOMY.items():
            for c2, cmds in caps:
                if c2 == cap:
                    out += [x for x in cmds
                            if x != cmd and x in COV["documented"]]
    seen, uniq = set(), []
    for s in out:
        if s not in seen:
            seen.add(s)
            uniq.append(s)
    return uniq[:8]


def build_page(cmd: str, meta: dict) -> str:
    img = meta["image"]
    help_path = CAP / img / "help" / f"{cmd}.help.txt"
    if not help_path.exists():
        safe = re.sub(r"[^A-Za-z0-9._-]", "_", cmd)
        help_path = CAP / img / "help" / f"{safe}.help.txt"
    text = help_path.read_text(encoding="utf-8", errors="replace")

    opts = parse_options(text)
    syn = parse_synopsis(text)
    vms, kit_purpose, url = kit_homes(cmd)
    if not vms:
        vms = FALLBACK_KIT.get(cmd, [])
    purpose = kit_purpose or parse_purpose(text, cmd)
    caps = capability_of(cmd)
    version = clean_version(meta.get("version") or "")

    rel_root = "../.." if caps else ".."
    L: list[str] = [MARKER, f"# {cmd}", ""]

    bits = []
    if vms:
        bits.append(f"**Kit:** {' · '.join(vms)}")
    if caps:
        bits.append("**Capability:** " + "; ".join(c for _p, c in caps))
    if version:
        bits.append(f"**Version:** {version}")
    L.append("  ".join(bits))
    ln = [f"**Captured:** `{img}` via `{meta.get('via','')}` on {date.today().isoformat()}",
          f"[raw]({rel_root}/capture/{img}/help/{help_path.name})"]
    if url:
        ln.append(f"**Docs:** <{url}>")
    L += ["  ".join(ln), ""]

    L += ["## Purpose", "", purpose or "_TODO: one-line imperative purpose._", ""]

    if syn:
        L += ["## Synopsis", "", "```", syn, "```", ""]

    mined = CANDS.get(cmd, [])
    L += ["## Common invocations", ""]
    if mined:
        L += ["<!-- candidates mined from cyberlab; verify each flag against the "
              "options table below before treating as reviewed -->", "```"]
        for m in mined[:8]:
            L.append(f"# from cyberlab {m['module']}")
            L.append(m["cmd"])
        L += ["```", ""]
    else:
        L += ["_TODO: up to 8 task-titled invocations._", ""]

    L += ["## Options", ""]
    if opts:
        L += [f"All {len(opts)} options parsed from the captured help text. "
              "The final column is the judgement layer and is filled in by review.",
              "", "| Flag | Argument | What it does | When you would use it |",
              "|---|---|---|---|"]
        for o in opts:
            d = re.sub(r"\s+", " ", o["desc"]).replace("|", "\\|").strip() or "—"
            a = (o["arg"] or "—").replace("|", "\\|")
            L.append(f"| `{o['flag']}` | {a} | {d[:200]} | |")
        L.append("")
    else:
        L += ["_No option definitions could be parsed from this tool's help "
              "output. It may be subcommand-driven or have no flags; needs "
              "manual review._", ""]

    L += ["## Gotchas", "", "_TODO: operational traps._", ""]

    sib = siblings(cmd)
    if sib:
        L += ["## See also", "", ", ".join(f"`{s}`" for s in sib), ""]
    return "\n".join(L)


def main() -> None:
    written = skipped = preserved = 0
    for cmd, meta in sorted(COV["documented"].items()):
        caps = capability_of(cmd)
        if not caps:
            skipped += 1
            continue
        folder = slug(caps[0][0])
        path = REF / folder / f"{cmd}.md"
        if path.exists() and MARKER not in path.read_text(encoding="utf-8", errors="replace"):
            preserved += 1
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        try:
            path.write_text(build_page(cmd, meta), encoding="utf-8")
            written += 1
        except Exception as e:                       # one bad tool must not stop the run
            print(f"  WARN {cmd}: {e}", file=sys.stderr)
    print(f"pages written={written} hand-written preserved={preserved} "
          f"skipped (no capability)={skipped}")


if __name__ == "__main__":
    main()



