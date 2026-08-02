#!/usr/bin/env python3
"""Link the kit tool list to the pages that document it.

KIT-TOOLS.md answers "what do I have?" and the reference pages answer "how do
I use it?", and until now nothing joined them: 1,006 catalogued tools, not one
link, including for the tools that do have a page.

This runs as a post-processing pass over the generated file rather than inside
build_kit_list.py, because that script rebuilds the catalogue from upstream
manifests. Regenerating it to add hyperlinks would risk changing the binding
scope as a side effect of a formatting change.

Idempotent: it skips rows that already carry a link, so it can run on every
build.

usage: python scripts/link_kit_list.py
"""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KIT = ROOT / "catalog" / "KIT-TOOLS.md"
REF = ROOT / "reference"


def page_index() -> dict[str, str]:
    """command/tool name -> path relative to catalog/."""
    out: dict[str, str] = {}
    for p in REF.rglob("*.md"):
        if p.name == "INDEX.md":
            continue
        rel = "../" + p.relative_to(ROOT).as_posix()
        out[p.stem.lower()] = rel
        # A GUI page is reachable under the base tool name too, so a catalogue
        # row for a tool with only a GUI still finds it.
        if p.stem.endswith("-gui"):
            out.setdefault(p.stem[:-4].lower(), rel)
    return out


def main() -> int:
    if not KIT.exists():
        print("KIT-TOOLS.md not found", flush=True)
        return 1
    pages = page_index()
    text = KIT.read_text(encoding="utf-8")
    lines = text.splitlines()

    linked_tools = 0
    linked_cmds = 0

    def unlink_missing(cell: str) -> str:
        """Strip links whose target page no longer exists.

        Pages come and go -- a tool ruled out of scope loses its page -- and
        because this pass skips rows that already carry a link, a stale one
        would survive forever and render as a dead anchor in the PDF.
        """
        def repl(m: re.Match) -> str:
            label, target = m.group(1), m.group(2)
            if target.startswith(("http://", "https://", "#")):
                return m.group(0)
            if (KIT.parent / target).resolve().exists():
                return m.group(0)
            return label
        return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", repl, cell)

    for i, line in enumerate(lines):
        if not line.startswith("| ") or line.startswith("| Tool") or set(line) <= set("|- "):
            continue
        cells = line.split("|")
        if len(cells) < 5:
            continue

        cells[1] = " " + unlink_missing(cells[1].strip()) + " "
        cells[2] = " " + unlink_missing(cells[2].strip()) + " "
        line = "|".join(cells)
        lines[i] = line

        tool = cells[1].strip()
        cmds = cells[2].strip()

        # Tool name -> its page, when one exists and it is not already a link.
        if tool and not tool.startswith("["):
            hit = pages.get(tool.lower()) or pages.get(tool.lower().replace(" ", "-"))
            if hit:
                cells[1] = f" [{tool}]({hit}) "
                linked_tools += 1

        # Each backticked command -> its own page.
        if "`" in cmds and "](" not in cmds:
            def repl(m: re.Match) -> str:
                nonlocal linked_cmds
                name = m.group(1)
                hit = pages.get(name.lower())
                if not hit:
                    return m.group(0)
                linked_cmds += 1
                return f"[`{name}`]({hit})"
            cells[2] = " " + re.sub(r"`([^`]+)`", repl, cmds) + " "

        lines[i] = "|".join(cells)

    KIT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"kit list linked: {linked_tools} tool names, {linked_cmds} commands")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
