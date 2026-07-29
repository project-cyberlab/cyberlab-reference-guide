#!/usr/bin/env python3
"""Build the authoritative KIT TOOL LIST: VM -> category -> tools.

Every entry comes from an upstream machine-readable manifest, never from memory.
This is the binding scope for the quick-reference guide: if a tool is not in
this list, it is not in the kit, and the guide must not document it.

Sources (all pinned in SOURCES below):
  Security Onion  <- the kit tracker CSV (already enumerates its sub-tools)
  REMnux          <- REMnux/docs discover-the-tools/*.md (categorised upstream)
  Kali            <- kali-meta debian/control (kali-tools-* = upstream taxonomy)
  FLARE-VM        <- mandiant/flare-vm config.xml (137 packages)
  SIFT            <- teamdfir/sift-saltstack packages

Outputs:
  catalog/kit-tools.json  machine-readable (drives the guide + the linter)
  catalog/KIT-TOOLS.md    human-readable, VM -> category -> tools
"""
from __future__ import annotations
import json
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog"
CACHE = ROOT / ".cache"
CACHE.mkdir(exist_ok=True)

GH_RAW = "https://raw.githubusercontent.com"

SOURCES = {
    "remnux_docs": f"{GH_RAW}/REMnux/docs/master/discover-the-tools",
    "kali_control": "https://gitlab.com/kalilinux/packages/kali-meta/-/raw/kali/master/debian/control",
    "flare_config": f"{GH_RAW}/mandiant/flare-vm/main/config.xml",
}

REMNUX_PAGES = [
    "analyze+documents/email+messages.md", "analyze+documents/general.md",
    "analyze+documents/microsoft+office.md", "analyze+documents/pdf.md",
    "dynamically+reverse-engineer+code/elf+files.md",
    "dynamically+reverse-engineer+code/general.md",
    "dynamically+reverse-engineer+code/scripts.md",
    "dynamically+reverse-engineer+code/shellcode.md",
    "examine+static+properties/.net.md", "examine+static+properties/deobfuscation.md",
    "examine+static+properties/elf+files.md", "examine+static+properties/general.md",
    "examine+static+properties/go.md", "examine+static+properties/pe+files.md",
    "explore+network+interactions/connecting.md",
    "explore+network+interactions/monitoring.md",
    "explore+network+interactions/services.md",
    "gather+and+analyze+data.md", "general+utilities.md",
    "investigate+system+interactions.md", "perform+memory+forensics.md",
    "statically+analyze+code/.net.md", "statically+analyze+code/android.md",
    "statically+analyze+code/general.md", "statically+analyze+code/java.md",
    "statically+analyze+code/pe-files.md", "statically+analyze+code/python.md",
    "statically+analyze+code/scripts.md", "statically+analyze+code/unpacking.md",
    "use+artificial+intelligence.md", "view+or+edit+files.md",
]

# Kali is scope-explosive (kali-linux-everything = thousands). Restrict to the
# category metapackages that match this kit's mission; wireless/bluetooth/RFID/
# SDR/hardware are excluded because the tracker records no radio hardware.
KALI_GROUPS = [
    "kali-tools-information-gathering", "kali-tools-vulnerability",
    "kali-tools-web", "kali-tools-database", "kali-tools-passwords",
    "kali-tools-reverse-engineering", "kali-tools-exploitation",
    "kali-tools-sniffing-spoofing", "kali-tools-post-exploitation",
    "kali-tools-forensics", "kali-tools-crypto-stego", "kali-tools-fuzzing",
]

# SIFT's salt package list mixes analyst tools with OS plumbing. These are
# infrastructure, not things an analyst invokes during an investigation.
SIFT_PLUMBING = re.compile(
    r"^(apt|apache2|at|ca-certificates|cifs|curl|dkms|dpkg|g\+\+|gcc|git|gnupg|"
    r"htop|libc|libssl|linux-|make|nfs|ntp|openssh|openvpn|python3?-?(dev|pip|"
    r"setuptools|wheel)?$|samba|ssh|sudo|tmux|tzdata|unzip|vim|wget|xrdp|zip|"
    r"software-properties|build-essential|dbus|dconf|desktop|fonts?-|gvfs|"
    r"lib[a-z0-9]+|net-tools|policykit|ubuntu-|x11|xfce|xorg)",
    re.I,
)


def fetch(url: str) -> str:
    key = CACHE / (re.sub(r"[^A-Za-z0-9]+", "_", url)[-120:] + ".txt")
    if key.exists():
        return key.read_text(encoding="utf-8", errors="replace")
    req = urllib.request.Request(url, headers={"User-Agent": "kit-list-builder"})
    with urllib.request.urlopen(req, timeout=30) as r:
        text = r.read().decode("utf-8", errors="replace")
    key.write_text(text, encoding="utf-8")
    return text


def parse_remnux() -> dict:
    """REMnux docs: '## Tool' + description + '**Notes**: binary1, binary2'."""
    cats: dict[str, list] = {}
    for page in REMNUX_PAGES:
        try:
            body = fetch(f"{SOURCES['remnux_docs']}/{page}")
        except Exception as e:                      # a missing page must not kill the build
            print(f"  WARN remnux {page}: {e}", file=sys.stderr)
            continue
        parts = page[:-3].split("/")
        category = parts[0].replace("+", " ").title()
        sub = parts[1].replace("+", " ").title() if len(parts) > 1 else "General"
        entries = []
        for block in re.split(r"^## ", body, flags=re.M)[1:]:
            lines = block.strip().splitlines()
            if not lines:
                continue
            name = lines[0].strip()
            desc = ""
            for ln in lines[1:]:
                s = ln.strip()
                if s and not s.startswith("**"):
                    desc = s
                    break
            m = re.search(r"\*\*Notes\*\*:\s*(.+)", block)
            binaries = []
            if m:
                # Notes is free prose in many pages and a comma-separated binary
                # list in others. Accept a token only if it LOOKS like a command
                # name; that keeps sentences ("use 7zz instead of 7z.") out of
                # the command column. Markdown line continuations ('\') and
                # trailing punctuation are stripped first.
                cand = m.group(1).rstrip("\\").strip()
                if len(cand) < 120 and "`" not in cand:
                    for tok in cand.split(","):
                        tok = tok.strip().rstrip("\\").strip(" .")
                        if re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._+-]{1,40}", tok):
                            binaries.append(tok)
            site = re.search(r"\*\*Website\*\*:\s*\[([^\]]+)\]", block)
            entries.append({
                "tool": name,
                "purpose": desc,
                "binaries": binaries,
                "url": site.group(1) if site else "",
            })
        if entries:
            cats.setdefault(f"{category} / {sub}", []).extend(entries)
    return cats


def parse_kali() -> dict:
    """kali-meta debian/control: one stanza per metapackage, Depends = tools."""
    body = fetch(SOURCES["kali_control"])
    out: dict[str, list] = {}
    for stanza in body.split("\n\n"):
        m = re.search(r"^Package:\s*(\S+)", stanza, re.M)
        if not m or m.group(1) not in KALI_GROUPS:
            continue
        # The Depends block is interrupted by '# comment' lines at column 0
        # (e.g. "# Packages"), so we cannot stop at the first non-indented line.
        # Take everything after Depends: to the end of the stanza, then drop
        # comments and stop only at a genuine RFC822 field header.
        dep = re.search(r"^Depends:(.*)\Z", stanza, re.M | re.S)
        if not dep:
            continue
        body_lines = []
        for ln in dep.group(1).splitlines():
            if ln.startswith("#"):
                continue                      # kali-meta section comment
            if re.match(r"^[A-Za-z][A-Za-z0-9-]*:", ln):
                break                         # next field (Description:, ...)
            body_lines.append(ln)
        pkgs = []
        for tok in " ".join(body_lines).split(","):
            tok = tok.strip()
            # strip architecture qualifiers: "binwalk3 [amd64 arm64]"
            tok = re.sub(r"\[.*?\]", "", tok).strip()
            tok = re.sub(r"[|].*", "", tok).strip()
            tok = tok.split()[0] if tok else ""
            if tok and not tok.startswith("$") and not tok.startswith("kali-"):
                pkgs.append(tok)
        label = m.group(1).replace("kali-tools-", "").replace("-", " ").title()
        out[label] = [{"tool": p, "purpose": "", "binaries": [p], "url": ""}
                      for p in sorted(set(pkgs))]
    return out


def parse_flare() -> dict:
    body = fetch(SOURCES["flare_config"])
    names = sorted({n[:-3] if n.endswith(".vm") else n
                    for n in re.findall(r'<package name="([^"]+)"', body)})
    return {"All Packages (choco)": [
        {"tool": n, "purpose": "", "binaries": [n], "url": ""} for n in names]}


def parse_sift(pkg_names: list[str]) -> dict:
    tools = [p for p in sorted(set(pkg_names)) if not SIFT_PLUMBING.match(p)]
    dropped = [p for p in sorted(set(pkg_names)) if SIFT_PLUMBING.match(p)]
    print(f"  SIFT: kept {len(tools)} analyst tools, set aside {len(dropped)} plumbing pkgs")
    return {"Forensic Packages": [
        {"tool": t, "purpose": "", "binaries": [t], "url": ""} for t in tools]}


def parse_security_onion(csv_text: str) -> dict:
    out: dict[str, list] = {}
    for line in csv_text.splitlines()[1:]:
        cols = [c.strip() for c in line.split(",")]
        if len(cols) < 6 or cols[0] != "Security Onion":
            continue
        out.setdefault(cols[1], []).append({
            "tool": cols[2], "purpose": cols[5],
            "binaries": [], "url": cols[6] if len(cols) > 6 else "",
        })
    return out


def main() -> int:
    kit: dict[str, dict] = {}

    print("REMnux...")
    kit["REMnux"] = parse_remnux()
    print("Kali...")
    kit["Kali Linux"] = parse_kali()
    print("FLARE-VM...")
    kit["FLARE-VM"] = parse_flare()

    sift_file = CATALOG / "_sift_packages.txt"
    if sift_file.exists():
        print("SIFT...")
        kit["SIFT Workstation"] = parse_sift(sift_file.read_text().split())

    so_file = CATALOG / "Cyber_Tools_Lab_Tracker.csv"
    if so_file.exists():
        print("Security Onion...")
        kit["Security Onion"] = parse_security_onion(
            so_file.read_text(encoding="utf-8", errors="replace"))

    CATALOG.mkdir(exist_ok=True)
    (CATALOG / "kit-tools.json").write_text(
        json.dumps({"sources": SOURCES, "kit": kit}, indent=2), encoding="utf-8")

    # ---- human-readable list: VM -> category -> tools --------------------
    md = ["# Kit Tool List", "",
          "The binding scope for the quick-reference guide. A tool absent from this",
          "list is **not in the kit** and must not be documented in the guide.", "",
          "Every entry is derived from an upstream machine-readable manifest; none",
          "is written from memory. Sources are listed at the end.", ""]
    total = 0
    md.append("## Contents\n")
    for vm in kit:
        n = sum(len(v) for v in kit[vm].values())
        total += n
        md.append(f"- [{vm}](#{vm.lower().replace(' ', '-')}) — {n} tools, "
                  f"{len(kit[vm])} categories")
    md.append(f"\n**Total: {total} tools across {len(kit)} platforms.**\n")

    for vm, cats in kit.items():
        md.append(f"\n## {vm}\n")
        for cat, entries in sorted(cats.items()):
            md.append(f"### {cat}\n")
            md.append("| Tool | Command(s) | Purpose |")
            md.append("|---|---|---|")
            for e in sorted(entries, key=lambda x: x["tool"].lower()):
                cmds = ", ".join(f"`{b}`" for b in e["binaries"]) or "—"
                purpose = (e["purpose"] or "").replace("|", "\\|")[:120]
                md.append(f"| {e['tool']} | {cmds} | {purpose} |")
            md.append("")

    md.append("\n## Sources\n")
    for k, v in SOURCES.items():
        md.append(f"- `{k}` — {v}")
    (CATALOG / "KIT-TOOLS.md").write_text("\n".join(md), encoding="utf-8")

    print(f"\nWrote catalog/kit-tools.json and catalog/KIT-TOOLS.md")
    for vm, cats in kit.items():
        print(f"  {vm:20s} {sum(len(v) for v in cats.values()):4d} tools "
              f"in {len(cats)} categories")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
