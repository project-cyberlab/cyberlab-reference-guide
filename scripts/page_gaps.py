#!/usr/bin/env python3
"""What each reference page is still missing, counted the same way every time.

Three things a reader needs that the option table cannot give them: where to
go next (contextual links to neighbouring tools), what a real invocation looks
like (worked examples with a line saying why), and for GUI tools a picture of
the window with the fields that matter called out.

Counted here rather than by eye, and rather than ad hoc at the prompt. An
earlier hand-written version of this reported 153 of 155 pages as having no
worked examples, which was shell quoting mangling the pattern -- fls.md has
eight. Acting on that number would have meant rewriting pages that were
already fine.

    python scripts/page_gaps.py            # summary
    python scripts/page_gaps.py --list     # every page with what it lacks
"""
from __future__ import annotations
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REF = ROOT / "reference"

# Links present on every page by construction. They are navigation, not a
# cross-reference, and counting them made every page look well linked.
NAV = ("Capability index", "Kit tool list")

CMD = re.compile(r"^\s*#[^#]", re.M)


def audit() -> list[dict]:
    rows = []
    for p in sorted(REF.rglob("*.md")):
        name = p.stem
        if name == "INDEX":
            continue
        t = p.read_text(encoding="utf-8", errors="replace")
        links = [m.group(1) for m in re.finditer(r"\[([^\]]+)\]\([^)]+\.md\)", t)
                 if not any(n in m.group(1) for n in NAV)]
        sec = re.search(r"## Common invocations\n(.*?)(\n## |\Z)", t, re.S)
        rows.append({
            "page": name,
            "path": str(p.relative_to(ROOT)),
            "links": len(links),
            "examples": len(CMD.findall(sec.group(1))) if sec else 0,
            "images": len(re.findall(r"!\[", t)),
            "gui": name.endswith("-gui"),
        })
    return rows


def main() -> int:
    rows = audit()
    gui = [r for r in rows if r["gui"]]
    cli = [r for r in rows if not r["gui"]]

    def pct(n, d):
        return f"{n:3d}/{d:<3d} ({100 * n / d:.0f}%)" if d else "n/a"

    print(f"reference pages: {len(rows)}  ({len(cli)} CLI, {len(gui)} GUI)\n")
    print("  no contextual link   :",
          pct(sum(1 for r in rows if not r["links"]), len(rows)))
    print("  no worked example    :",
          pct(sum(1 for r in rows if not r["examples"]), len(rows)))
    print("  thin (1-2 examples)  :",
          pct(sum(1 for r in rows if 0 < r["examples"] < 3), len(rows)))
    print("  GUI page, no image   :",
          pct(sum(1 for r in gui if not r["images"]), len(gui)))

    worst = [r for r in rows if not r["examples"] or not r["links"]]
    print(f"\npages missing links or examples: {len(worst)}")
    if "--list" in sys.argv:
        for r in sorted(worst, key=lambda r: (r["examples"], r["links"])):
            lack = []
            if not r["links"]:
                lack.append("no links")
            if not r["examples"]:
                lack.append("no examples")
            if r["gui"] and not r["images"]:
                lack.append("no screenshot")
            print(f"  {r['page']:24s} {', '.join(lack)}")
    else:
        for r in sorted(worst, key=lambda r: (r["examples"], r["links"]))[:15]:
            print(f"  {r['page']:24s} links={r['links']} examples={r['examples']}"
                  f"{' images=0' if r['gui'] and not r['images'] else ''}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
