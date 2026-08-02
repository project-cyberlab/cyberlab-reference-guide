# Research: search backend, local models, and triangulation

Measured rather than assumed. Everything below was tested on this fleet
against the real task on 2026-08-02.

## Local models: retrieval dominates, model size does not

Six candidate models were given the same real retrieved passage — the Sleuth
Kit wiki paragraph explaining `fls -s` — and asked for one grounded sentence
saying when an analyst would reach for that flag.

| Model | Host | Time | Result |
|---|---|---|---|
| gemma2:9b | l3e7 3090 | 10.8s | correct |
| qwen3:14b | l3e7 3090 | 10.9s | correct |
| qwen3:14b | rick 4090 | 11.6s | correct |
| qwen3:30b-a3b-instruct | l3e7 3090 | 14.9s | correct |
| mistral-small3.2:24b | l3e7 3090 | 19.4s | correct |
| qwen3:32b | l3e7 3090 | 22.8s | correct |
| qwen2.5:14b-instruct | both | 7-10s | **INSUFFICIENT** (false negative) |

Every model that answered produced substantially the same correct sentence.
The 32B took twice as long as the 9B and was no better.

**Conclusion: when the retrieved passage contains the answer, the model is
doing near-trivial work — compressing one paragraph.** The intelligence in
this pipeline lives in finding the right paragraph, not in processing it.
Spend the budget on more and better sources, not larger models.

Practical consequences:

- **Draft with a small fast model.** gemma2:9b or qwen3:14b, ~11s per note.
  Both GPUs in parallel gives roughly 10 notes/minute.
- **Avoid qwen2.5:14b-instruct for this task.** It returned INSUFFICIENT on a
  passage that plainly contained the answer. A false negative is expensive
  here: it looks exactly like "no source exists", which is the conclusion this
  whole design forbids.
- **Model disagreement is a useful signal.** Where models converge, the
  passage was clear. Where they diverge, the passage probably did not contain
  the answer and the miss log should get a row.

## Search backend: SearxNG is the right workhorse

Self-hosted SearxNG on rick, port 8888.

Measured over 8 realistic tool queries: **8/8 returned results, 4 seconds
total, ~0.5s per query.** No API key, no quota, no per-query cost.

Earlier zero-result runs were not the engine failing. They were two bugs in
how queries were built:

1. **A leading hyphen is the NOT operator on every search engine.** `fls -s
   sleuthkit` searches for fls and sleuthkit while *excluding* "s". Flag
   queries were suppressing the exact pages that held the answer.
2. **Quoted phrases return nothing** for these niche strings.

Both are fixed by searching per tool rather than per flag, and mining flags
out of the resulting corpus locally.

### Should we add a second backend?

Not for reliability — SearxNG is reliable. The argument is **diversity**, and
it matters specifically because of triangulation.

SearxNG is a metasearch engine: it aggregates other engines, most of which are
Google- or Bing-derived. So three "independent" searchers querying SearxNG are
not independent at all — they see one index through one lens, and agreement
between them means much less than it appears.

[Brave](https://brave.com/search/api/) runs its **own** index rather than
reselling Google's, which is what makes it worth adding: it is a genuinely
different view of the web, so corroboration across the two means something.
[Tavily](https://tavily.com/) is agent-native (relevance scores, extracted
content) with a free tier of ~1,000 credits/month.

A full corpus pass over ~147 tools at 4 queries each is ~600 queries. That
fits a free tier for corroboration duty, if not for bulk work.

**Recommendation:** SearxNG carries the bulk — unlimited and free. Add one
independent index for corroboration on published claims only. Neither key is
required to start; the pipeline works today on SearxNG alone.

## What this means for triangulation

The user's design is that local models, free-API models and Claude all search,
and cross-validate each other into solid information. Two corrections fall out
of the measurements:

**Diversity has to come from the sources, not the models.** Three models
reading the same passage will agree — as they did here, all six of them — and
that agreement is not evidence, it is an echo. Genuine triangulation means
different *searchers* finding different *pages*, then comparing what those
pages claim.

**So the tiers should split by role, not repeat the same job:**

| Tier | Job | Why |
|---|---|---|
| Local models (3090 + 4090) | Draft one grounded sentence per passage; high volume, free | Measured adequate at 9-14B; bigger buys nothing |
| Free API models | Search a *different* way, and improve a draft that a local model produced | Different query phrasing surfaces different pages — that is where real diversity enters |
| Claude | Final pass/fail on nuance, intent and whether it serves a junior analyst | The judgement the smaller models cannot make, and the user's stated role for it |

**Corroboration rule:** a claim published to the guide should be traceable to
a passage on a real page. Where two independent sources agree, confidence is
high. Where they conflict, the tool's own documentation wins, and the conflict
is worth recording — a walkthrough contradicting the man page is either out of
date or wrong, and either way it is a signal about that source's reliability.


---

# Deep research: how to verify generated claims

Prompted by a direct challenge - had the research actually been done, across
the board, on doing this properly. It had not, beyond the prior loops and the
local measurements above. This is that research, and it changed the design.

## The finding that matters: confirmation bias in verifiers

**MARCH - Multi-Agent Reinforced Self-Check** (arXiv 2603.24579).

When a verifier sees the evidence **and** the draft together, it endorses
errors through *internal coherence* rather than grounding. The paper names
this confirmation bias and measures it.

Their fix is **deliberate information asymmetry**:

| Role | Sees | Job |
|---|---|---|
| Solver | question + documents | writes the draft |
| Proposer | the draft | decomposes it into atomic, separately checkable questions |
| Checker | **documents only, never the draft** | re-answers those questions independently |

Disagreement between what the draft claims and what the Checker derives is the
hallucination signal. They call it *blind scrutiny*.

Measured: an 8B model went from 55.2% to 75.2% average accuracy on
RAGTruth/FaithBench, matching far larger proprietary models. On HotpotQA it
reached 71.2%, above GPT-4o at 64.0%.

**This matches the local benchmark exactly.** Six models here produced the
same answer regardless of size, because architecture - not parameter count -
is what determines quality on this job.

**Our gate had precisely the bias described.** It saw the note and the evidence
together, which is why it approved two inverted workflows.

## Verify at the point of creation, not later

**Delayed Verification Destabilizes Multi-Agent LLM Belief** (arXiv 2606.27409).

Verification meant to suppress hallucination can destabilise a system when
delayed: correction that is too strong or too delayed turns consensus into
oscillation, below a threshold that shrinks as delay grows.

The reassuring part for this design: **factual tasks with absorbing boundaries
- truth as a fixed constraint - remain stable regardless of delay.** A
retrieved passage is exactly such a constraint. This pipeline sits in the
stable regime by construction, because every claim is anchored to a fetched
document rather than to another agent's belief.

Design rule taken from it: verify each claim where it is created; never let an
unverified claim flow downstream and become an input.

## What was implemented, and how it was calibrated

`scripts/blind_check.py`. Proposer (qwen3:14b, l3e7) decomposes a note into
neutral questions - prompted to ask "Which runs first, X or Y?" rather than
"Does X run before Y?", so the question does not leak the answer. Checker
(gemma3:27b, rick) answers from the passages alone. Different host **and**
different model family, because two qwen models share training data and
therefore share blind spots.

**Tested by deliberate inversion** on strong evidence - a true note about
`fls -m` feeding `mactime`, and the same note with the order reversed:

- FALSE note -> **rejected**. The decisive check: "Which runs first, mactime
  or fls -m?" - claim said mactime, sources said fls. Exactly the failure that
  passed every mechanical check.
- TRUE note -> initially also rejected, which exposed a flaw worth recording.

**Ask about contradiction, not agreement.** The first judge prompt asked "do
these agree?" and marked "building a timeline" against "collecting temporal
data from file systems" as disagreement - the same fact at two granularities.
Likewise "produces the body file" against "a line for each file", which is
one output described two ways. A judge hunting agreement rejects correct work.
Only genuine conflict counts; different wording, different detail level, or
extra detail on one side are all compatible.

**Zero tolerance is wrong for a noisy judge.** MARCH's Zero-Tolerance Reward
assumes the judge is right. Measured here it is not. So the thresholds are
calibrated to observed reliability:

| Signal | Verdict | Why |
|---|---|---|
| Ordering contradiction | **reject** | "Which runs first" has one answer; the judge got it right in both directions, and it is the error that actually misleads a junior analyst |
| Two or more contradictions | **reject** | Independent conflicts are unlikely to both be judge noise |
| Exactly one contradiction | **review** | Judge is not reliable enough alone to bin otherwise-good work |
| Sources answered nothing | **review** | Evidence too thin to rule either way |

Discarding correct notes is not a safe default. It is how a loop quietly stops
making progress while appearing rigorous.
