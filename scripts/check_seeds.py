#!/usr/bin/env python3
"""Check that seeded pages actually mention the tool they were seeded for.

Seeds are added by hand, from a search, when the loop's own search is
throttled. That is useful and it is also easy to get wrong in a way that
leaves no trace: a search for "registry forensics tools" returns excellent
pages about the subject, none of which contain the word regfexport. The
seeds look right, the pages fetch, and the tool still finds nothing --
because passages are located by the tool's name appearing in the text.

Four pages were seeded for regfexport this way. All four fetched. All four
mentioned it zero times.

Nothing in the pipeline complains about that, because a seed that yields no
passages is indistinguishable from a tool nobody has written about, and this
project is not allowed to conclude the second. So the check has to be
explicit.

    python scripts/check_seeds.py            # report
    python scripts/check_seeds.py --prune    # drop seeds that never match
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import sources  # noqa: E402

ROOT = HERE.parent
SEEDFILE = ROOT / "catalog" / "seed-urls.json"


def mentions(text: str, tool: str) -> int:
    return len(re.findall(r"(?<![\w./-])" + re.escape(tool) + r"(?![\w-])",
                          text, re.I))


def main() -> int:
    prune = "--prune" in sys.argv
    seeds = json.loads(SEEDFILE.read_text(encoding="utf-8"))
    bad: dict[str, list[str]] = {}
    silent: list[str] = []

    for tool, urls in sorted(seeds.items()):
        if tool.startswith("_"):
            continue
        keep, drop = [], []
        for url in urls:
            text = sources.fetch_text(url)
            n = mentions(text, tool) if text else 0
            (keep if n else drop).append(url)
            status = "ok" if n else ("EMPTY" if not text else "NO MENTION")
            if not n:
                print(f"  {status:10s} {tool:22s} {url[:64]}")
        if drop:
            bad[tool] = drop
        if not keep:
            silent.append(tool)
        if prune and keep:
            seeds[tool] = keep

    print(f"\n{len(bad)} tools have seeds that never mention them; "
          f"{len(silent)} have NO usable seed at all")
    if silent:
        print("no usable seed: " + ", ".join(silent))
        print("\nThese are not tools without sources. They are tools whose\n"
              "seeds were chosen by topic rather than by name, and they need\n"
              "a search for the binary itself -- 'regfexport example' rather\n"
              "than 'registry forensics tools'.")
    if prune:
        SEEDFILE.write_text(json.dumps(seeds, indent=2), encoding="utf-8")
        print("pruned seeds that never matched")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
