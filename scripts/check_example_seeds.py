#!/usr/bin/env python3
"""Does a seed page actually PRINT commands, or only name the tool?

check_seeds asks whether a page mentions the binary. That is the right
question for the WHEN column, where a walkthrough naming the tool in prose
is exactly what is wanted, and it is not enough for worked examples.

The TSK Tool Overview wiki names sorter, tsk_loaddb, blkstat, mmcat and
tsk_comparedir, so check_seeds verified 4/4 for several of them -- and all
five yielded zero invocations, because the page describes each tool and
invokes none. Naming is necessary and not sufficient.

This asks the stronger question by running the real extractor over the
page: would any command survive? Use it before seeding for the examples
gap, so a batch is not spent on pages that cannot produce one.

    python scripts/check_example_seeds.py sorter blkstat mmcat
    python scripts/check_example_seeds.py --all      # audit every seed
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
ROOT = HERE.parent

import sources          # noqa: E402
import invocations      # noqa: E402
import check_seeds      # noqa: E402
import enrich_loop      # noqa: E402


def audit(tool: str) -> list[tuple[str, int, int]]:
    """(url, mentions, extractable commands) for each of the tool's seeds."""
    seeds = json.loads((ROOT / "catalog" / "seed-urls.json")
                       .read_text(encoding="utf-8"))
    rf = enrich_loop.capture_flags(tool)
    out = []
    for url in seeds.get(tool, ()):
        text = sources.fetch_text(url) or ""
        out.append((url,
                    check_seeds.mentions(text, tool),
                    len(invocations.candidate_lines(text, tool, rf))))
    return out


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--all" in sys.argv:
        seeds = json.loads((ROOT / "catalog" / "seed-urls.json")
                           .read_text(encoding="utf-8"))
        args = sorted(k for k in seeds if not k.startswith("_"))
    if not args:
        print(__doc__)
        return 1

    for tool in args:
        rows = audit(tool)
        cmds = sum(c for _u, _m, c in rows)
        named = sum(1 for _u, m, _c in rows if m)
        print(f"{tool:22s} {named}/{len(rows)} name it, "
              f"{cmds} extractable commands")
        for url, m, c in rows:
            if m and not c:
                print(f"    names but never invokes: {url[:72]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
