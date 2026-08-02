#!/usr/bin/env python3
"""Run the build in the only order that is correct.

There is an ordering dependency that is easy to trip over by hand:

    enrichment.py  ->  generate_pages.py  ->  build_pdf.py

Editing curation and jumping straight to the PDF publishes pages that do not
contain the edit. It fails silently -- no error, no warning, just a PDF missing
the work. That happened once, so the sequence lives in code rather than in
anyone's memory.

usage: python scripts/build_all.py [--no-pdf]
"""
from __future__ import annotations
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def run(script: str) -> str:
    print(f"--- {script}")
    r = subprocess.run([sys.executable, str(ROOT / "scripts" / script)],
                       capture_output=True, text=True)
    out = (r.stdout or "") + (r.stderr or "")
    for line in out.strip().splitlines()[-4:]:
        print(f"    {line}")
    if r.returncode != 0:
        print(f"    FAILED (exit {r.returncode})", file=sys.stderr)
        raise SystemExit(r.returncode)
    return out


def reviewed_rows() -> tuple[int, int]:
    """How much of the options tables carry usage guidance."""
    row = re.compile(r"^\|\s*`[^`]+`\s*\|")
    total = reviewed = 0
    for page in (ROOT / "reference").rglob("*.md"):
        if page.name == "INDEX.md":
            continue
        for line in page.read_text(encoding="utf-8", errors="replace").splitlines():
            if not row.match(line):
                continue
            total += 1
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 4 and cells[-1]:
                reviewed += 1
    return reviewed, total


def main() -> int:
    run("generate_pages.py")
    run("build_index.py")
    lint = run("lint.py")

    errors = 0
    m = re.search(r"ERRORS=(\d+)", lint)
    if m:
        errors = int(m.group(1))

    if "--no-pdf" not in sys.argv:
        run("build_pdf.py")

    rev, tot = reviewed_rows()
    print()
    print(f"  option rows with guidance : {rev}/{tot} ({100*rev/max(tot,1):.1f}%)")
    print(f"  lint errors               : {errors}")
    if errors:
        print("  build is NOT publishable while errors stand", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
