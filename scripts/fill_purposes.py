#!/usr/bin/env python3
"""Fill the Purpose column in the kit tool list from upstream package metadata.

REMnux and Security Onion arrived with a purpose for every tool, because their
upstream sources carry descriptions. Kali, FLARE-VM and SIFT arrived with the
column entirely empty -- 702 of 1006 tools -- because `kali-meta`'s
debian/control, FLARE's config.xml and sift-saltstack are bare package lists
with no description field at all.

The descriptions do exist; they are in the APT indices. This fills the column
from there rather than from memory, which keeps the catalogue's rule intact:
every entry derived from an upstream machine-readable source.

`catalog/_pkgdesc.json` is the harvested map (package -> short description),
built from the kali-rolling and Ubuntu focal indices.

Runs as a post-pass over the generated file for the same reason
link_kit_list.py does: build_kit_list.py rebuilds the catalogue from upstream
manifests, and regenerating it to add descriptions would risk changing the
binding scope as a side effect.

usage: python scripts/fill_purposes.py
"""
from __future__ import annotations
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KIT = ROOT / "catalog" / "KIT-TOOLS.md"
DESC = ROOT / "catalog" / "_pkgdesc.json"


def candidates(name: str):
    """Names a catalogue entry might be known by in a package index."""
    n = name.strip()
    yield n
    yield n.lower()
    yield n.lower().replace("_", "-")
    yield n.lower().replace(" ", "-")
    if n.lower().endswith(".py"):
        yield n[:-3].lower()
    if n.lower().startswith("python-"):
        yield n[7:].lower()
    # FLARE's packages are NuGet ids carrying a .vm suffix that the catalogue
    # does not use: the row says "010editor", the feed says "010editor.vm".
    yield n.lower() + ".vm"
    yield n.lower().replace(" ", "") + ".vm"


def main() -> int:
    if not KIT.exists() or not DESC.exists():
        print("kit list or description map missing", flush=True)
        return 1

    desc = json.loads(DESC.read_text(encoding="utf-8"))
    lines = KIT.read_text(encoding="utf-8").splitlines()

    filled = already = unmatched = 0
    for i, line in enumerate(lines):
        if not line.startswith("| ") or line.startswith("| Tool") or set(line) <= set("|- "):
            continue
        cells = line.split("|")
        if len(cells) < 5:
            continue

        purpose = cells[3].strip()
        if purpose and purpose != "—":
            already += 1
            continue

        # The tool cell may already be a link, so recover the display text.
        tool = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", cells[1]).strip()
        # Commands the row lists are also worth trying: the package is often
        # named after one of them.
        cmds = re.findall(r"`([^`]+)`", cells[2])

        hit = None
        for name in [tool, *cmds]:
            for cand in candidates(re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", name)):
                if cand in desc:
                    hit = desc[cand]
                    break
            if hit:
                break

        if not hit:
            unmatched += 1
            continue

        text = hit.strip().replace("|", "\\|")
        if len(text) > 118:
            text = text[:115].rstrip() + "..."
        # Upstream short descriptions are lower-case sentence fragments; make
        # them read like the hand-written REMnux ones.
        if text and text[0].islower():
            text = text[0].upper() + text[1:]
        if not text.endswith("."):
            text += "."
        cells[3] = f" {text} "
        lines[i] = "|".join(cells)
        filled += 1

    KIT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"purposes filled={filled} already_present={already} unmatched={unmatched}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
