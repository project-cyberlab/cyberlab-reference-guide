#!/usr/bin/env python3
"""Generate a GUI page skeleton from a captured control tree.

Same split as the CLI pipeline: everything mechanical comes from the capture,
and only judgement is written by hand. The control inventory, the enumerated
values of every combo box and the screenshot reference are derived from
capture/gui/<tool>/<tool>.tree.txt, so they cannot drift from the application
and cannot be invented.

Hand-written pages are never overwritten: a page without the generated marker
is left alone, exactly as generate_pages.py does.

usage: python scripts/generate_gui_pages.py
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAP = ROOT / "capture" / "gui"
REF = ROOT / "reference"
MARKER = "<!-- generated-by: scripts/generate_gui_pages.py -->"

# Which capability each GUI tool belongs under. Placement is a judgement call
# about what the tool is for, so it is written down here rather than guessed
# from the control tree.
CAPABILITY = {
    "dnSpy":              ("reverse-engineering",       ".NET assembly browser and debugger"),
    "VB-Decompiler":      ("reverse-engineering",       "Visual Basic decompiler"),
    "vbdec":              ("reverse-engineering",       "Visual Basic 5/6 decompiler"),
    "idr":                ("reverse-engineering",       "Delphi decompiler and form reconstructor"),
    "CFF-Explorer":       ("malware-triage-static",     "PE structure editor and viewer"),
    "PE-Detective":       ("malware-triage-static",     "PE packer and compiler signature scanner"),
    "Signature-Explorer": ("malware-triage-static",     "Browse and edit packer signature databases"),
    "PDFStreamDumper":    ("malware-triage-documents",  "Inspect and extract PDF object streams"),
    "OffVis":             ("malware-triage-documents",  "Visualise Office binary file structure"),
    "HashMyFiles":        ("acquire-preserve",          "Hash a set of files and compare the results"),
    "CryptoTester":       ("decode-deobfuscate",        "Try cryptographic operations against a sample"),
    "Regshot":            ("windows-artifacts",         "Diff the registry across a detonation"),
    "AccessEnum":         ("windows-artifacts",         "Enumerate filesystem and registry permissions"),
    "ADExplorer":         ("windows-artifacts",         "Browse and snapshot Active Directory"),
}

LEAF = ("Button", "Edit", "CheckBox", "ComboBox", "RadioButton", "List",
        "Tree", "Tab", "TabItem", "MenuItem", "Text", "Slider", "Document")


def parse(tree_text: str) -> dict:
    head = {}
    for line in tree_text.splitlines():
        m = re.match(r"^# (\w[\w ]*): (.*)$", line)
        if m:
            head[m.group(1).strip()] = m.group(2).strip()
    controls = []
    for line in tree_text.splitlines():
        if line.startswith("#"):
            continue
        m = re.match(r"^(\s*)(\w+)(?: \"([^\"]*)\")?(?: #(\S+))?(?: \[([^\]]*)\])?", line)
        if not m:
            continue
        indent, ctype, name, aid, key = m.groups()
        controls.append({"depth": len(indent) // 2, "type": ctype,
                         "name": name or "", "id": aid or "", "key": key or ""})
    # ListItems directly under a ComboBox are that control's permitted values.
    values: dict[str, list[str]] = {}
    current = None
    for c in controls:
        if c["type"] == "ComboBox":
            current = c["id"] or c["name"]
            values.setdefault(current, [])
        elif c["type"] == "ListItem" and current:
            values[current].append(c["name"])
        elif c["type"] not in ("List", "ListItem") and c["depth"] <= 1:
            current = None
    return {"head": head, "controls": controls,
            "values": {k: v for k, v in values.items() if v}}


def build(tool: str, data: dict, cap: str, blurb: str, has_png: bool) -> str:
    head = data["head"]
    window = head.get("window", "")
    version = ""
    vm = re.search(r"v?(\d+[\d.]*)", window)
    if vm:
        version = vm.group(0)

    L = [MARKER, f"# {tool} (GUI)", ""]
    L.append(f"**Capability:** {cap.replace('-', ' ')}  "
             f"**Window:** `{head.get('class','')}`  "
             f"**Version:** {version or '—'}")
    L.append(f"**Captured:** `{head.get('exe','')}` on {head.get('captured','')[:10]} — "
             f"control tree in "
             f"[`capture/gui/{tool}/{tool}.tree.txt`](../../capture/gui/{tool}/{tool}.tree.txt)")
    L += ["", "[← Capability index](../INDEX.md) · "
              "[Kit tool list](../../catalog/KIT-TOOLS.md)", ""]

    L += ["## Purpose", "", blurb + ".", ""]

    if has_png:
        L += ["## Window", "",
              f"![{tool} main window](../../capture/gui/{tool}/{tool}.png)", ""]

    leaves = [c for c in data["controls"] if c["type"] in LEAF and (c["name"] or c["id"])]
    if leaves:
        L += ["## Controls", "",
              f"All {len(data['controls'])} nodes come from the capture; "
              f"the {len(leaves)} interactive controls are listed here.", "",
              "| Control | Type | AutomationId | What it does |", "|---|---|---|---|"]
        seen = set()
        for c in leaves:
            label = (c["name"] or c["id"].split(".")[-1] or "").strip()
            # An unnamed control with no AutomationId has nothing to call it by.
            # Emitting `****` for it produces empty bold, which makes the bold
            # match run on into the next table row and reports the whole run as
            # an invented control.
            if not label or not label.strip("|`"):
                continue
            label = label.replace("|", "\\|")
            key = (label, c["type"])
            if key in seen:
                continue
            seen.add(key)
            aid = c["id"].split(".")[-1] if c["id"] else "—"
            L.append(f"| **{label}** | {c['type']} | `{aid}` | |")
        L.append("")

    if data["values"]:
        L += ["## Enumerated values", "",
              "Read from the control itself, so this is the set of choices in "
              "this build rather than what the documentation claims.", ""]
        for ctrl, vals in data["values"].items():
            L.append(f"**{ctrl.split('.')[-1]}**")
            L.append("")
            for v in vals:
                L.append(f"- {v}")
            L.append("")

    L += ["## Using it", "",
          "_TODO: numbered click-path, at most seven steps per task._", "",
          "## Gotchas", "",
          "_TODO: what surprises an analyst here._", ""]
    return "\n".join(L)


def main() -> int:
    if not CAP.exists():
        print("no capture/gui yet")
        return 0
    written = preserved = skipped = 0
    for d in sorted(CAP.iterdir()):
        if not d.is_dir() or d.name.startswith("_"):
            continue
        tool = d.name
        tree = d / f"{tool}.tree.txt"
        if not tree.exists():
            continue
        text = tree.read_text(encoding="utf-8", errors="replace")
        if "# ERROR" in text or "#--- nodes: 0" in text:
            skipped += 1
            continue
        if tool not in CAPABILITY:
            skipped += 1
            continue
        cap, blurb = CAPABILITY[tool]
        out = REF / cap / f"{tool}-gui.md"
        if out.exists() and MARKER not in out.read_text(encoding="utf-8", errors="replace"):
            preserved += 1
            continue
        data = parse(text)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(build(tool, data, cap, blurb, (d / f"{tool}.png").exists()),
                       encoding="utf-8")
        written += 1
    print(f"gui pages written={written} hand-written preserved={preserved} skipped={skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
