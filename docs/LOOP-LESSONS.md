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

## Proximity is not ownership

`passages_using` requires the tool's name within ±200 characters of the flag,
which is what separates a real invocation from a stray hyphen. It does not ask
whether the tool *owns* the option being described, and on sibling tools those
come apart. scalpel is a fork of foremost and names foremost in its own man
page, so a scalpel option block passes the proximity test on a foremost query.
The loop duly reported that `foremost -b` carves files whose footers are
missing — scalpel's `-b`; foremost's sets the block size — and that `foremost
-s` skips bytes, where scalpel skips bytes and foremost skips blocks.

`misattributed()` cannot catch this. It looks for another tool's name in the
note, and this failure works by *dropping* the attribution and keeping the
semantics. There is nothing in the note to find.

So `option_owner()` checks the evidence rather than the claim: for each place
the flag appears, find the nearest preceding synopsis and ask whose it is.
Replayed over all 154 recorded flag records it fires ten times and reproduces
both misattributions that had been caught by hand — `mactime -m` and `ils -m`,
each lifted from an `fls` synopsis.

Two outcomes, because the faults differ. A flag the tool does not have is a
fabrication and is rejected. A flag it does have, documented here from someone
else's synopsis, may well be right and cannot be settled from this evidence —
that goes to review. `mmls -o` is the case that forced the distinction.

## Do not read your own output back as evidence

`rax2` shipped citing exactly one source: this guide's own `rax2.md`. Search
had indexed the repository, so the loop was retrieving pages it had written
earlier and treating them as corroboration. A claim then supports itself one
generation later, and the citation makes it look sourced.

The whole design rests on retrieval from outside. Nothing external is learned
by reading your own output. `project-cyberlab` is now in `DENY`.

The recurring shape, again: every stage has a plausible near-miss that produces
no error. Seeded-but-unmatched, reviewed-but-unpublished, committed-but-not-
running, answered-but-duplicate, and now cited-but-self-cited. Each looks
exactly like success from the step before it.

## The two columns want different sources

A tool page has two things a reader needs, and they do not come from the
same kind of page.

The **when** column wants a walkthrough: someone narrating an investigation,
saying what they reached for and why and what came before it. The **worked
examples** want a man page, a tldr entry or a "ten practical examples"
article: something that prints command lines.

Neither genre supplies the other, and the seeding routine had been treating
"has sources" as one question. Measured on three tools:

    readelf       man pages only     19 passages,  0 usable commands
    readelf       + cheat sheets     38 passages,  8 usable commands
    strings       walkthroughs only  36 passages,  0 usable commands
    strings       + command examples 42 passages,  8 usable commands

readelf is the clearest case: nineteen passages of real evidence and not one
command, because a man page prints `readelf [opts] <elf>` and that is
notation, not an invocation. The extractor is right to reject it, and no
amount of further man-page seeding would have helped.

So seed for the gap you have. A tool with a note and no examples needs
command pages; a tool with examples and no note needs somebody's write-up.

## A page that fetches to nothing still costs a slot

The corpus is capped, so a page returning fifteen characters does not merely
add nothing -- it displaces a page that would have added something. strings
fell from 36 passages and 2 usable commands to 24 and 0 between two runs,
and the whole difference was a facebook.com result taking one of the ten
slots.

The cache already refused to store anything under 500 characters. The corpus
now refuses to count it, and the social platforms are in DENY, because a
search for a tool name reaches them and what comes back is a login wall.
