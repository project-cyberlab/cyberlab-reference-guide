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
