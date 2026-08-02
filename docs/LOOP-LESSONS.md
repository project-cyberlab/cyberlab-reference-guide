# What the earlier research loops learned

The cyberlab training lab ran an autonomous enrichment loop for months across
61 modules. It produced a great deal, and then a content-quality audit found
that a large part of what it produced was fabricated. Those findings are
recorded here because this guide is about to attempt the same thing, and
because the failure was not carelessness — it was an architecture that could
not fail any other way.

Sources: `cyberlab-v2-hybrid-enrichment`, `cyberlab-audit-roadmap`,
`cyberlab-tool-gap-closure`, `cyberlab-training-lab-loop` (project memory).

---

## The finding that matters most

The audit of 61 modules found **~44 of them shipping fabricated CLI flags** —
`yara --module`, `yara --extern`, `clamscan --yaravars`, invented PE-bear,
`scdbg` and x64dbg switches, Volatility 2 commands inside a Volatility 3
module. Alongside that: wrong ATT&CK technique names throughout, blocks
pasted two and three times, and one YARA rule repeated across eight modules.

The enrichment tail was 9,645 of 23,998 lines — **40% of the lab** — and
essentially every defect lived in it. The remediation was to delete all of it:
~11,000 lines removed, and `cyberlab_enrich_gen` **permanently disabled**
because it fabricates.

The named root cause was **generate-and-append-without-execution**.

This is the single most important thing for this guide, because a reference
that invents a flag is worse than no reference: an analyst types it, it fails,
and the guide has cost them time and trust. The reason this guide gates
everything on captured `--help` output is precisely this failure.

## What replaced it

> **Architecture shift: retrieval-first + mechanical insertion (deterministic,
> hang-safe) instead of LLM generation (fragile + fabricating).**

Real Sigma and YARA rules pulled verbatim from SigmaHQ and Neo23x0 with
attribution and source URL, real MITRE data from the live technique pages,
real case studies from documented intrusions. Inserted by code, not written by
a model. Result: 54 of 61 modules got real rules, all 61 passed, cost $0.

**The tooling already exists and is hardened.** On rick:
`~/work/night_loop/adapters/cyberlab_retrieval.py` — stdlib only, allowlisted
domains (attack.mitre.org, SANS, docs.remnux.org, ericzimmerman.github.io,
thedfirreport.com, Red Canary, Microsoft Learn, the YARA/Volatility/Sigma/
Suricata/Plaso docs, NIST, CISA), 30-day disk cache, and every network call
deadline-guarded. Functions: `fetch_text`, `verify_url`, `mitre_technique`,
`real_sigma_rule`, `real_yara_rule`.

Reuse it. Do not write another one.

## Lessons that apply directly to this guide's loop

**1. The gate is the only ground truth. The model never self-certifies.**
Stated as loop doctrine, and it held up.

**2. Weak models fail at whole-document work and succeed at one bounded
section.** Research (STORM, Skeleton-of-Thought, DeCRIM) plus prototyping
proved it. The fix was to shard into ~200-word cited sections, validate each,
and assemble *mechanically* so the structure is guaranteed by code.

*Implicates this guide:* `research_loop.py` asks for all 54 flags of a tool in
one call. That is the whole-document shape that does not work.

**3. Absolute quality scoring saturates; forced ranking works.** Scoring each
dimension 0–2 maxed out through leniency and verbosity bias. Replacing it with
a forced, no-ties ranking across dimensions was the fix.

*Implicates this guide:* validation here is a set of binary rules. It cannot
say "this note is weaker than that one", which is the judgement actually
needed.

**4. Verify every cited URL.** Hallucinated citations pass every other check.
`verify_url` on each new URL, with a control check first so a network outage
never causes a false rejection.

**5. Keep injected grounding small — 400 characters, not 2,500.** Injecting
2,500 characters of retrieved context stalled provider SSE streams; append
went from 34s to over 200s and hung the loop. It was reverted.

**6. Deadline-guard every network call.** A urllib timeout does not fire on a
trickling read. One stalled fetch blocked the whole loop for 18 minutes. The
fix is a daemon thread with a join timeout, returning a default regardless.

**7. Measure value-delta, not growth.** A raw "+15% words" bar was unfair and
gameable. Replaced with net-new authoritative sources, net-new techniques, new
substantive subsections.

**8. Gate against bloat explicitly.** Shingle overlap of added text against the
original (>0.55 rejects), filler-phrase density, and a size ceiling. Saturated
modules then return nothing instead of padding — convergence, not failure.

**9. Do not ask for JSON output.** It inflates token use by ~40%.

*Implicates this guide:* `research_loop.py` requests strict JSON.

**10. Fence-aware parsing is required.** A `#` inside a fenced code block is
not a heading. This broke section parsing on 12 of 38 modules before it was
fixed.

*Implicates this guide:* the `SECTION-UNEXPLAINED` check in `audit.py` scans
for headings without excluding code fences.

**11. "Completion-over-skill is a documented failure mode."** Recorded
verbatim in the backlog. Filling a field because the field exists is the
defect, not the cure — which is the same objection raised against this guide's
empty columns.

## Operational traps worth not rediscovering

- Retry caps that silently permanently skip an item (`MAX_ATTEMPTS=2` wrote to
  a skip-list; a transient failure excluded a module forever and the loop then
  reported "all modules already enriched").
- Never `pkill` a running adapter — it counts as a crash and trips the
  crash-loop breaker into a handback. Let the subprocess timeout self-heal.
- An evaluation function that writes its candidate to the real file path will
  pollute the source. Copy to a temp path for dry evaluation.
- Do not let a subagent create files in a directory holding load-bearing
  modules of the same name — one overwrote the contract validator and broke
  the gate.
- Free strong models rate-limit under sustained load, and contract-following
  strength — not key count — is the bottleneck. More keys did not help.

## Standing rules from the other loops

These are not cyberlab-specific. They are recorded as standing user direction
across the REM and Emergence loops and they govern this work too.

**Research before implementing, not after.** Recorded as a standing rule after
a run of failures traced to building on guesses: "research-backed specs go
40/40 first-attempt; guess-based work burned whole evenings." Prefer
source-verified claims — read the tool's own source or documentation — over
tutorials and recollection.

**Every research finding gets logged, every time.** A hard rule: no finding
stays only in chat. It goes into the durable record, because chat is
ephemeral. This document exists for that reason.

**Read the record before acting — this is the half that gets skipped.** The
logging rule has a corollary added after a wasted night: "we logged but never
read first." Check what is already known before starting. This whole
investigation happened because a loop was built here without first reading the
loop that had already failed the same way.

**Research ahead of need.** The aim is that when a hard decision comes up, the
answer is already recorded, rather than being researched under pressure.
Retrieval is cheap — network fetches and small embeds, not GPU time — so it
can run continuously.

**A null result on one lever is not convergence.** Recorded twice, after the
same mistake was made twice: a plateau on one approach means pivot to the next
untried lever, not stop. But paired with its correction — "an idle GPU beats a
redundant run" — repeating settled work is not progress either. Progress means
new knowledge.

## What this means for this guide

The current `research_loop.py` is an LLM-generation loop. That is the
architecture that fabricated flags across 44 modules and was disabled. It
survives here only because its validator refuses any flag absent from the
capture — which blocks fabrication but, as the first real run showed, leaves
paraphrase as the only thing the model can produce.

The correction is the same one cyberlab arrived at: **retrieve first, insert
mechanically, and use the model for judgement rather than for content.** For a
"when would you use this flag" note, the sources are the tool's own
documentation, its author's writing, and published analyst workflows — fetched
through the existing allowlisted retrieval module, liveness-checked, cited on
the page, and cached.
