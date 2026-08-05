#!/usr/bin/env python3
"""The numbers this loop is steered by, computed the same way every round.

These were being derived by hand at each check, and a hand-derived metric
drifts. The flag-targeting number is the one that caught it out: it asks what
fraction of flag attempts were aimed at flags that already had an answer, and
the obvious way to compute it is to look each flag up in ENRICHMENT.

That is wrong, and quietly. ENRICHMENT is mutated at import so published
answers merge into it, so two notes the loop itself had just published came
back as redundant targeting the following round -- a jump from 0% to 3% that
looked exactly like a regression and was in fact a success being counted as
waste. The fix is to measure against the hand-written block only, which is
what HAND_ANSWERED preserves.

The general form of that mistake is the one this project keeps meeting:
measuring the step before the thing rather than the thing. A watchdog counted
log lines instead of verdicts and called nine barren hours healthy.

    python scripts/loop_metrics.py
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
ROOT = HERE.parent

from enrichment import ENRICHMENT, HAND_ANSWERED  # noqa: E402

VERDICT = re.compile(r"(KEPT|MISS|REJECTED|REVIEW)\s+(\S+)(?:\s+(-{1,2}\S+))?")


def _load(name: str):
    try:
        return json.loads((ROOT / name).read_text(encoding="utf-8"))
    except Exception:
        return []


def main() -> int:
    log = (ROOT / "research_live.log")
    txt = log.read_text(encoding="utf-8", errors="replace") if log.exists() else ""
    rows = VERDICT.findall(txt)
    flags = [(t, f) for _v, t, f in rows if f]

    print(f"verdicts recorded      : {len(rows)}")
    print(f"flag attempts          : {len(flags)}")

    if flags:
        # Against the hand-written block ONLY. See the module docstring.
        dup = [(t, f) for t, f in flags if f in HAND_ANSWERED.get(t, ())]
        print(f"  already answered by hand: {len(dup)} "
              f"({100 * len(dup) / len(flags):.1f}%)  [target: near 0]")
        for t, f in dup[:5]:
            print(f"    {t} {f}")

    by = {}
    for v, _t, _f in rows:
        by[v] = by.get(v, 0) + 1
    print("  " + "  ".join(f"{k}={v}" for k, v in sorted(by.items())))

    out, dec = _load("research_output.json"), _load("research_decisions.json")
    if isinstance(dec, dict):
        pend = [r for r in out
                if (f"{r['tool']} {r['flag']}" if r.get("flag") else r["tool"])
                not in dec]
        print(f"unreviewed in publish queue: {len(pend)}")

    # Provenance. A published answer counts as covered, but the two are not
    # the same kind of thing and the split is worth watching.
    hand = sum(len(v) for v in HAND_ANSWERED.values())
    allw = sum(len(r.get("when") or {}) for r in ENRICHMENT.values())
    print(f"option answers         : {allw} total "
          f"({hand} hand-written, {allw - hand} researched)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
