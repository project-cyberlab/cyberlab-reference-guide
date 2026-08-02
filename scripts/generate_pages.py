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
import os
import re
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from taxonomy import TAXONOMY  # noqa: E402
from helpparse import parse_options, parse_synopsis, parse_purpose  # noqa: E402
from enrichment import ENRICHMENT  # noqa: E402

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


# Base-system utilities that are present on every Linux install and are not
# what any of these platforms is known for. An analyst reference documents the
# analyst tooling; nobody reaches for this guide to learn `less`.
#
# Deliberately conservative. Tools that are generic Unix but genuinely part of
# a forensic workflow stay: file, strings, xxd, dd, md5sum, sha256sum, ssdeep,
# unzip and 7za all earn their place in triage.
OUT_OF_SCOPE = {
    "less", "pager", "sensible-pager",   # also the only captures carrying
                                         # man-style overstrike garbage
    "grep", "stat", "curl", "wget",
}


# Tools that ship both a command line and a window. The names rarely match --
# the GUI is `die`, the command is `diec` -- so a reader landing on one page
# has no way to know the other exists. Both pages say so explicitly, and both
# titles carry (CLI) or (GUI), because "diec" and "die-gui" side by side in an
# index tell you nothing about which one opens a window.
GUI_COUNTERPART = {
    "diec": "die",
    "die": "die",
}

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
    # More ways a tool answers --version with something that is not a version:
    # "/data/version is not a valid directory!", "------> --version <------",
    # "/usr/bin/cpan version 1.64 calling Getopt::Std::getopts (...)".
    if re.search(r"(not a valid|calling Getopt|no such file|command not found)", v, re.I):
        return ""
    if v.startswith(("-", "/", "=")) or set(v.strip()) <= set("-<> "):
        return ""

    # A build hash is not useful in a field guide:
    # "2026.5.0+76dc8354aa98ce1e1c6f942abcfb09f583f411d" -> "2026.5.0".
    v = re.sub(r"\+[0-9a-f]{7,}\b", "", v)
    # "(Git v4.0.17 packaged as 4.0.17-0+deb12u3)" adds nothing either.
    v = re.sub(r"\s*\((Git|git)[^)]*\)", "", v)

    m = re.search(r"([A-Za-z][A-Za-z0-9 ._-]{0,40}?\s*v?\d+\.\d+(?:\.\d+)?)", v)
    if m:
        out = m.group(1).strip()
        # Trailing prose after the number ("ccrypt 1.11. Secure encryption...")
        # is a description, not part of the version.
        return out[:45]
    return v[:45] if len(v) <= 45 else ""


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


def page_path_of(tool: str) -> Path | None:
    """Where a tool's page lives, or None if it has none."""
    for ph, caps in TAXONOMY.items():
        for _cap, cmds in caps:
            if tool in cmds:
                cand = REF / slug(ph) / f"{tool}.md"
                if cand.exists():
                    return cand
    return None


def link_inline_mentions(text: str, cmd: str, page: Path) -> str:
    """Turn `othertool` in prose into a link to that tool's page.

    Readers navigate by following links inside the sentence they are already
    reading, far more than by going back to an index, so a tool named mid-page
    should be reachable from there. Only inline code spans are linked: several
    tools are also ordinary English words (`file`, `stat`, `strings`, `less`),
    and linking those on sight would turn the prose into a minefield. A code
    span is an explicit statement that the author meant the command.
    """
    parts = re.split(r"(```.*?```)", text, flags=re.S)      # never touch fenced code
    for idx, part in enumerate(parts):
        if part.startswith("```"):
            continue
        out_lines = []
        for line in part.splitlines(keepends=True):
            # Tables carry captured flag text; leave them alone.
            if line.lstrip().startswith("|"):
                out_lines.append(line)
                continue

            def repl(m: re.Match) -> str:
                tool = m.group(1).strip()
                if tool == cmd:
                    return m.group(0)
                target = page_path_of(tool)
                if target is None:
                    return m.group(0)
                rel = os.path.relpath(target, page.parent).replace(os.sep, "/")
                return f"[`{tool}`]({rel})"

            # Skip spans already inside a markdown link.
            if re.search(r"\]\([^)]*\)", line):
                out_lines.append(line)
                continue
            out_lines.append(re.sub(r"`([^`\n]{2,40})`", repl, line))
        parts[idx] = "".join(out_lines)
    return "".join(parts)


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
    enr = ENRICHMENT.get(cmd, {})
    when: dict[str, str] = enr.get("when", {})
    # Curated purpose wins over the catalogue blurb, which wins over whatever
    # the help text volunteers.
    purpose = enr.get("purpose") or kit_purpose or parse_purpose(text, cmd)
    caps = capability_of(cmd)
    version = clean_version(meta.get("version") or "")

    rel_root = "../.." if caps else ".."
    title = f"{cmd} (CLI)" if cmd in GUI_COUNTERPART else cmd
    L: list[str] = [MARKER, f"# {title}", ""]

    # A two-column table, not a run of bold labels on one line. Joined with
    # spaces these fields render as "...pdfid.py 0.2.10 Captured: cyberlab-aio"
    # -- the reader cannot tell where one field ends and the next begins, and
    # a bare value like `diec` after "CLI counterpart:" reads as a stray token.
    rows: list[tuple[str, str]] = []
    if vms:
        rows.append(("Kit", " · ".join(vms)))
    if caps:
        rows.append(("Capability", "; ".join(c for _p, c in caps)))
    if version:
        rows.append(("Version", version))
    # Say plainly when a tool has both a window and a command line. `die`,
    # `die-gui` and `diec` are three pages for one product, and without this
    # the reader has to work out which is which from the filename.
    gui = GUI_COUNTERPART.get(cmd)
    if gui:
        gui_page = next((p for p in REF.rglob(f"{gui}-gui.md")), None)
        if gui_page:
            rel = gui_page.relative_to(REF).as_posix()
            depth = "" if not caps else "../"
            rows.append(("Graphical version",
                         f"The same tool has a window-based version, "
                         f"[{gui} (GUI)]({depth}{rel}), which is the better "
                         f"choice when you are exploring one sample rather "
                         f"than scripting"))
    rows.append(("Captured from",
                 f"`{img}` via `{meta.get('via','')}` on {date.today().isoformat()} "
                 f"— [raw help output]({rel_root}/capture/{img}/help/{help_path.name})"))
    if url:
        rows.append(("Documentation", f"<{url}>"))
    L += ["| | |", "|---|---|"]
    L += [f"| **{k}** | {v} |" for k, v in rows]
    L.append("")

    # Navigation back to the two entry points: you should never be stranded on
    # a tool page without a route back to "what else does this job?".
    L += [f"[← Capability index](../INDEX.md) · [Kit tool list]({rel_root}/catalog/KIT-TOOLS.md)",
          ""]

    L += ["## Purpose", "", purpose or "_TODO: one-line imperative purpose._", ""]

    # "When you'd reach for this" -- the tool-level scenario.
    #
    # This is the section the whole research loop exists to fill, and it is a
    # section rather than a table cell because the useful answer will not fit
    # in one: what situation brings you here, what runs before and after, and
    # why this tool rather than the one beside it. A junior analyst choosing
    # between pdfid and pdf-parser, or photorec and testdisk, needs the
    # difference spelled out, not two similar definitions.
    #
    # Sources are printed with it. A claim a reader cannot check is a claim
    # they have to take on trust, and this guide has already published
    # confidently-wrong text once.
    ent = ENRICHMENT.get(cmd, {})
    scenario = ent.get("scenario", "")
    if scenario:
        L += ["## When you'd reach for this", "", scenario, ""]
        srcs = ent.get("sources") or []
        if srcs:
            L.append("**Sources:** " + " · ".join(f"<{u}>" for u in srcs[:3]))
            L.append("")

    if syn:
        L += ["## Synopsis", "", "```", syn, "```", ""]

    # Invocations mined from cyberlab are NOT published.
    #
    # cyberlab was an idea that reached roughly a quarter finished before the
    # work pivoted, and its own content audit found fabricated CLI flags in ~44
    # of 61 modules. Seeding a guide that exists to prevent fabrication from a
    # source known to contain it is the wrong trade at any volume. The linter
    # catches an invented *flag*, but a mined command can be wrong in ways it
    # cannot see: right flags, wrong order, wrong context, wrong tool for the
    # job. An empty section is honest; a plausible wrong command is not.
    #
    # The mined data stays in capture/cyberlab-candidates.json as a research
    # lead for whoever writes these by hand.
    invocations = ENRICHMENT.get(cmd, {}).get("invocations") or []
    if invocations:
        L += ["## Common invocations", "", "```"]
        for inv in invocations[:8]:
            L.append(f"# {inv['task']}")
            L.append(inv["cmd"])
        L += ["```", ""]

    L += ["## Options", ""]
    if opts:
        n_when = sum(1 for o in opts if o["flag"] in when)
        note = (f"All {len(opts)} options parsed from the captured help text"
                + (f"; {n_when} reviewed with usage guidance." if n_when
                   else ". The final column is filled in by review."))
        L += [note, "",
              "| Flag | Argument | What it does | When you would use it |",
              "|---|---|---|---|"]
        # Many tools list a short and a long spelling of the same option as
        # separate rows ("-c" and "--count"), carrying the identical captured
        # description. Curating one and leaving the other blank means half the
        # table is empty for no reason -- whichever spelling the reader looks
        # up decides whether they get an answer. An identical description is
        # the tool's own statement that these are one option, so the guidance
        # is mirrored across them.
        by_desc: dict[str, str] = {}
        for o in opts:
            key = re.sub(r"\s+", " ", o["desc"]).strip().lower()
            g = when.get(o["flag"], "")
            if key and g and key not in by_desc:
                by_desc[key] = g

        for o in opts:
            d = re.sub(r"\s+", " ", o["desc"]).replace("|", "\\|").strip() or "—"
            a = (o["arg"] or "—").replace("|", "\\|")
            w = when.get(o["flag"], "")
            if not w:
                w = by_desc.get(re.sub(r"\s+", " ", o["desc"]).strip().lower(), "")
            w = w.replace("|", "\\|")
            L.append(f"| `{o['flag']}` | {a} | {d[:200]} | {w} |")
        L.append("")
    else:
        L += ["_No option definitions could be parsed from this tool's help "
              "output. It may be subcommand-driven or have no flags; needs "
              "manual review._", ""]

    gotchas = enr.get("gotchas") or []
    L += ["## Gotchas", ""]
    if gotchas:
        L += [f"- {g}" for g in gotchas] + [""]
    else:
        L += ["_TODO: operational traps._", ""]

    sib = siblings(cmd)
    if sib:
        # Link siblings, so a dead end reroutes instead of stalling mid-task.
        links = []
        for s in sib:
            sp = None
            for ph, caps2 in TAXONOMY.items():
                for c2, cmds2 in caps2:
                    if s in cmds2:
                        cand = REF / slug(ph) / f"{s}.md"
                        if cand.exists():
                            sp = cand
                            break
                if sp:
                    break
            if sp:
                rp = ("../" + sp.relative_to(REF).as_posix())
                links.append(f"[`{s}`]({rp})")
            else:
                links.append(f"`{s}`")
        L += ["## See also", "", ", ".join(links), ""]
    return "\n".join(L)


def main() -> None:
    written = skipped = preserved = 0
    for cmd, meta in sorted(COV["documented"].items()):
        if cmd in OUT_OF_SCOPE:
            skipped += 1
            continue
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
            page = build_page(cmd, meta)
            page = link_inline_mentions(page, cmd, path)
            path.write_text(page, encoding="utf-8")
            written += 1
        except Exception as e:                       # one bad tool must not stop the run
            print(f"  WARN {cmd}: {e}", file=sys.stderr)
    print(f"pages written={written} hand-written preserved={preserved} "
          f"skipped (no capability)={skipped}")


if __name__ == "__main__":
    main()



