# Research loop design — sourced guidance for every tool and every flag

**Status:** draft for review. No code written against this yet.

## The goal

Every tool in this guide gets a real scenario saying when an analyst would
reach for it, and every flag gets a note saying when they would use that flag.
Both grounded in a real source and cited. Nothing invented.

## The premise this design is built on

> Every tool we use has scenarios in which we would use them. If I have a
> wrench, it's a specific size or shape — there's a time and a place where you
> would use that tool, and where you'd use a screwdriver instead.
>
> Just because you can't find it doesn't mean there's not a good answer for
> it. It just means you weren't able to find it, and we need to keep searching
> and refining that answer.

This is a hard constraint on the design, not a sentiment. It means:

- **A failed search is a gap in the work, never a fact about the world.** The
  loop may never record "no guidance exists" for anything. The only honest
  states are *researched* and *not yet researched*.
- **There is no category of flag that does not deserve a note.** `-v` looked
  like an exception until examined: a malformed PDF is itself an evasion
  technique, so "when a document fails to parse and you need to see where it
  broke, because the breakage may be the point" is a real analytical scenario.
  Every apparent exception so far has dissolved under a closer look.
- **Answers are provisional and get refined.** A thin answer is still a work
  item. Passes revisit, they do not just fill.

## Why the current attempt failed

`scripts/research_loop.py` asked a local model for guidance with the tool's
captured `--help` as its only input. Its first real run produced, for
`pdf-parser -o` (help text: *"id(s) of indirect object(s) to select"*), the
note *"When you need to focus on specific indirect objects by their IDs."*

That is the description with "When you need to" prepended. It is not a
tuning problem. **"When would an analyst reach for this" is not a fact present
in `--help`**, so paraphrase is the only thing the model can return.

The clearest illustration is `nmap --script`. That is not one flag, it is a
doorway to hundreds of NSE scripts, each with its own purpose — `default` for
a safe first sweep, `smb-vuln-*` when checking a specific exposure, `exploit`
when you are deliberately touching the target and had better have
authorisation. All of it documented at length in the nmap book and the NSE
docs. None of it in `--help`. The answer was findable; the loop was reading
the one source guaranteed not to contain it.

## What counts as a good answer

The bar, stated plainly: the note must give **a scenario in which this would
be useful**. Not a definition, not an abstraction, not the description with
"when you need to" prepended — a situation the reader could recognise
themselves being in.

Concretely, a note passes only if it says at least one of:

- **the trigger** — what you just saw that makes you reach for this
  (*"a non-zero `/JS` count from `pdfid`"*)
- **the position** — what runs before or after it
  (*"output feeds `mactime` when you are building a timeline"*)
- **the choice** — why this and not the neighbouring tool or flag
  (*"unlike `dd`, it hashes as it reads, so the acquisition is verifiable"*)
- **the consequence** — what changes if you use it or skip it
  (*"without it a zero count is indistinguishable from not having checked"*)

A note that states none of these is a restatement, and restatement is the
defect this whole exercise exists to remove. This is enforced in the gate as a
structural check, not left to taste.

Worked example of the bar, on a flag that looks like it has no scenario —
`pdf-parser -v`:

> **Fails:** "When you want verbose output." (definition)
>
> **Passes:** "When a document fails to parse — malformed structure is itself
> an evasion technique, so where it breaks is evidence." (trigger +
> consequence)

## Architecture

Retrieval-first, mechanical insertion, models restricted to judgement. This is
the correction cyberlab arrived at after its enrichment loop shipped
fabricated CLI flags in ~44 of 61 modules (see `docs/LOOP-LESSONS.md`).

```
  per-tool source ladder
          |
     retrieve passages  (cyberlab_retrieval.py: allowlist, cache, deadlines)
          |
     model compresses passage -> one sentence   [local LLM / free API]
          |
     GATE   mechanical, no model
          |
     AUDIT  forced-ranking judge: worth it for a junior analyst?
          |
     publish with citation      OR      miss log -> next pass
```

### 1. The source ladder is per-tool, not generic

A tool's best source is usually specific to it. The loop keeps and grows a
`SOURCES` map from tool to its authoritative documentation, and walks the
ladder cheapest-and-most-authoritative first:

| Tier | Source | Notes |
|---|---|---|
| 0 | The capture we already hold | `--help`; also mine its cross-references |
| 1 | Man page | Stripped from the container base; available at manpages.debian.org. Richer than `--help` — `fls -m` states its output feeds `mactime`, which is itself a "when" |
| 2 | The tool's own documentation | REMnux docs, project README/wiki, the author's writing — Didier Stevens for the pdf tools, Eric Zimmerman for the EZ tools, the nmap book and NSE docs for nmap |
| 3 | Workflow sources | SANS cheat sheets and posters, published DFIR write-ups |

Tier 2 is where most real answers live, and it is the tier the previous
attempt skipped entirely.

Retrieval goes through rick's existing
`~/work/night_loop/adapters/cyberlab_retrieval.py` — stdlib only, domain
allowlist, 30-day disk cache (104 entries already warm), every network call
deadline-guarded. Verified present 2026-08-02. Do not write another one; its
allowlist gains the tool-documentation domains this guide needs.

### 2. Where the local models and free API keys fit

They do the high-volume cheap work and never supply a fact:

- **Compress** a retrieved passage into one sentence. The sentence must stay
  word-grounded in that passage or it is rejected.
- **Rank** candidate sentences against each other.

Grounding injected into a prompt is capped at 400 characters. Cyberlab
injected 2,500 and stalled provider SSE streams — append went from 34s to over
200s and hung the loop; it was reverted.

Work is sharded to one flag or one small group per call. Weak models fail
whole-document work and succeed at one bounded piece; asking for all 54 flags
of a tool in a single call is the shape that does not work.

No JSON output — it inflates tokens ~40%.

### 3. Gate — mechanical, no model

Binary, cheap, and not foolable by fluent prose. A candidate is rejected if it:

- cites no source, or cites a URL that fails a liveness check
- is not word-grounded in the passage it came from
- names any flag absent from the tool's capture
- paraphrases the flag's own description (content-word overlap)
- duplicates guidance already present elsewhere in the guide

### 4. Audit — the junior-analyst pass

The question is the one you asked for: *is this worth putting in the document,
and worth it for the junior analyst?*

**Forced ranking, never absolute scoring.** Cyberlab found 0–2 scoring
saturates through leniency and verbosity bias; reframing as a forced no-ties
ranking was the fix. The audit ranks candidates against each other and against
the existing text, and keeps the best only if it beats what is already there.

### 5. Miss log

A miss writes a row recording the tool, the flag, which tiers were tried, and
which queries ran. It is a work item, not a verdict. Next pass retries it
against a wider ladder. **Nothing in the guide ever states or implies that no
guidance exists.**

### 6. Passes refine

Each pass targets the weakest not-yet-covered aspect of a tool rather than
re-doing the same work, so successive passes add each tool's next most-needed
improvement instead of repeating. Convergence is when passes stop producing
anything that beats what is there — not when every cell is non-empty.

## Priority order

Not "most empty cells" — that put `hashcat` (143 blanks) first, which is a
tool a junior analyst rarely has to choose between neighbours for.

Priority is **confusable neighbours**, because that is where a junior analyst
makes the wrong call:

- `pdfid` / `pdf-parser` — the ten-second count vs what you open when it is non-zero
- `photorec` / `testdisk` — carve data out when the filesystem is gone vs repair it so it mounts
- `dd` / `dc3dd` / `dcfldd` — no hashing and bad error handling vs built for evidence
- `oleid` / `olevba` / `mraptor` / the other ten oletools — which to run, in what order
- `die` / `diec` — the window for one sample vs the command line for scripting

## Scale

124 pages carry option tables, 3,166 option rows, ~147 mapped tools. Tool-level
scenarios are ~147 units of work. Flag-level notes are 3,166, worked in
priority order across passes.

## What changes on the page

- **New section, "When you'd reach for this"**, under Purpose: a few sentences
  with citations saying what situation brings you here, what you run before
  it, and what you do with the output. This is the differential — why this
  tool and not the one beside it. A table cell cannot hold it.
- **The "When you would use it" column stays** and gets filled. It is not
  restructured away.
- Sources cited on the page, so a reader can check the claim.

## Success criteria

- Every tool page has a sourced "When you'd reach for this" section.
- Every published note carries a live citation.
- Zero flags named in guidance that are absent from the capture.
- The miss log shrinks pass over pass.
- No page states that guidance does not exist.

## Open questions for review

1. Priority order — is "confusable neighbours first" the right call over
   "worst pages first"?
2. Whether tool-documentation domains should be added to the shared cyberlab
   retrieval allowlist, or kept in a separate allowlist owned by this repo.
