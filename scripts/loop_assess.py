#!/usr/bin/env python3
"""Grade the loop's own run and propose the next improvement to itself.

A loop that only produces output cannot tell you whether it is getting better.
Every failure so far here was found by a human reading the results -- the
paraphrases, the inverted workflows, the search queries that excluded the term
they were searching for. That does not scale, and it means the loop's real
error rate is whatever the last manual review happened to catch.

So a pass ends by assessing itself. Two stages, deliberately in this order:

  1. MECHANICAL diagnostics over the run's own records. Counts, causes, which
     tools produced nothing and why, where evidence was thin. These are facts
     about the run and cannot be argued with.

  2. A MODEL reads those diagnostics and proposes the single highest-value
     change. Advisory only -- it never edits anything.

The mechanical half comes first because a model handed raw output will
critique the writing. The diagnostics point at the machinery instead, which is
where the fixable problems live: a tool with no seed URLs, an anchor phrase
returning nothing, a rejection reason firing on half the corpus.

Nothing here changes code. It produces a report for a human to act on --
because a loop that rewrites its own gate can loosen the gate, and a gate that
loosens itself is how the previous project shipped 44 modules of fabrications.

    python scripts/loop_assess.py
"""
from __future__ import annotations
import json
import re
import sys
import urllib.request
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

ROOT = HERE.parent
FILES = {"kept": ROOT / "research_output.json",
         "review": ROOT / "research_review.json",
         "miss": ROOT / "research_misses.json"}
REPORT = ROOT / "research_assessment.md"


# Proposals already tested against the recorded verdicts and disproven.
#
# The assessor has recommended a minimum passage-score threshold at least
# twice, and the record refutes it both times: a score>=5 rule would discard
# 34 of 81 accepted notes -- 42% -- to remove 62% of the rejects. scalpel,
# binwalk, evtxinfo, aeskeyfind, hivexsh, dc3dd and foremost all scored 0-2
# and are all correct.
#
# Without this the assessor cannot learn, because it sees one round's
# diagnostics and never the history of what those diagnostics led to. It will
# keep proposing the same plausible fix forever, and each time it costs a
# round to re-disprove.
DISPROVEN = """- A minimum passage-score threshold (4.7, 5.0, or any value). Passage score
  measures RETRIEVAL quality, not correctness. Tested twice: a score>=5 cut
  would discard 42% of accepted notes, including scalpel, binwalk, evtxinfo
  and foremost, all of which are correct.
- Excluding output-file flags (-o, --output, --csv). Measured: they are
  accepted at 62%, every other flag at 63%. Indistinguishable.
- Relaxing the grounding threshold below 45%. The problem there was never the
  threshold; the measurement was counting plurals as ungrounded, and stemming
  fixed it.
"""

ASSESSOR = ("l3e7-3090", "http://192.168.1.253:11434", "qwen3:30b-a3b-instruct-2507-q4_K_M")

PROMPT = """You are reviewing the performance of an automated research \
pipeline that writes guidance for a forensic tool reference guide.

Its job: for each tool, find real documentation and walkthroughs showing the \
tool in use, and turn them into one grounded, cited note saying WHEN a junior \
analyst would reach for it. Notes that are ungrounded, that merely restate the \
tool's own help text, or that state a workflow order the sources do not \
support are rejected.

Some changes have already been tried and DISPROVEN against the recorded review decisions. Do not propose these again:

{rejected}

Here are the measured diagnostics from the last run:

{diagnostics}

Identify the SINGLE change to the pipeline that would most improve the next \
run, and say concretely what to change. Focus on the machinery -- retrieval \
queries, source seeding, prompts, thresholds -- not on rewriting individual \
notes.

Answer in under 120 words. Be specific about what to change and why the \
diagnostics point at it."""


def ask(prompt: str, timeout: int = 300) -> str:
    _n, base, model = ASSESSOR
    body = json.dumps({"model": model, "prompt": prompt, "stream": False,
                       "options": {"temperature": 0.2, "num_ctx": 8192}}).encode()
    req = urllib.request.Request(base + "/api/generate", data=body,
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            out = json.loads(r.read()).get("response", "")
    except Exception as e:
        return f"(assessor unreachable: {e})"
    return re.sub(r"<think>.*?</think>", "", out, flags=re.S).strip()


def load() -> dict[str, list[dict]]:
    out = {}
    for k, p in FILES.items():
        try:
            out[k] = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            out[k] = []
    return out


def diagnose(runs: dict[str, list[dict]]) -> tuple[str, dict]:
    """Facts about the run. No judgement, no model."""
    kept, review, miss = runs["kept"], runs["review"], runs["miss"]
    total = len(kept) + len(review) + len(miss)
    lines: list[str] = []
    stats: dict = {"total": total, "kept": len(kept),
                   "review": len(review), "miss": len(miss)}

    if not total:
        return "No records from the last run.", stats

    lines.append(f"attempted: {total}")
    lines.append(f"  kept        {len(kept):3d}  ({100*len(kept)/total:.0f}%)")
    lines.append(f"  needs review{len(review):3d}  ({100*len(review)/total:.0f}%)")
    lines.append(f"  missed      {len(miss):3d}  ({100*len(miss)/total:.0f}%)")

    # Why things failed. The dominant cause is the thing worth fixing.
    causes = Counter()
    for r in review + miss:
        why = r.get("why", "unknown")
        why = re.sub(r"\d+", "N", why)
        causes[why[:70]] += 1
    if causes:
        lines.append("\nreasons a note did not ship, most common first:")
        for why, n in causes.most_common(6):
            lines.append(f"  {n:3d}  {why}")

    # Evidence quality is the lever. A pass that fails mostly because the
    # corpus was thin needs better sources, not better prompts.
    thin = [r for r in review + miss if r.get("sources_tried", 0) <= 2]
    nosrc = [r for r in review + miss if r.get("sources_tried", 0) == 0]
    lines.append(f"\nevidence: {len(nosrc)} attempts found NO sources, "
                 f"{len(thin)} found 2 or fewer")
    stats["no_sources"] = len(nosrc)
    stats["thin_sources"] = len(thin)

    if nosrc:
        lines.append("  tools with no sources at all (search terms are wrong "
                     "or the tool needs seed URLs):")
        for r in nosrc[:8]:
            lines.append(f"    {r.get('tool')}{' ' + r['flag'] if r.get('flag') else ''}")

    scores = [r.get("top_score", 0) for r in kept + review if "top_score" in r]
    if scores:
        lines.append(f"\npassage quality: best-passage score averaged "
                     f"{sum(scores)/len(scores):.1f}; "
                     f"{sum(1 for s in scores if s <= 2)} runs had a top score of 2 or less "
                     f"(the retrieved text carried little scenario language)")

    # A gate that never fires is not protecting anything; one that always
    # fires is blocking the work. Both are visible here.
    if not miss and not review:
        lines.append("\nWARNING: nothing was rejected or queued. A gate that "
                     "never fires is not a gate -- an earlier run passed 28 of "
                     "28 notes and every one was a paraphrase.")
    if not kept and total:
        lines.append("\nWARNING: nothing survived. The gate may be too strict, "
                     "or the corpus too thin to support any claim.")

    return "\n".join(lines), stats


def main() -> int:
    runs = load()
    diagnostics, stats = diagnose(runs)
    print(diagnostics)

    print("\n--- asking the assessor what to change ---")
    suggestion = ask(PROMPT.format(diagnostics=diagnostics, rejected=DISPROVEN))
    print(suggestion)

    REPORT.write_text(
        "# Loop self-assessment\n\n"
        "Mechanical diagnostics from the last run, then a model's proposal for\n"
        "the next improvement. The proposal is advisory: nothing here edits the\n"
        "pipeline. A loop that can loosen its own gate will.\n\n"
        "## Diagnostics\n\n```\n" + diagnostics + "\n```\n\n"
        "## Proposed next change\n\n" + suggestion + "\n",
        encoding="utf-8")
    print(f"\nwrote {REPORT.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
