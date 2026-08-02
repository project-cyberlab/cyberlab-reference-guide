# How every open feedback item enters the research loop

The challenge that produced this document: *is the research loop truly fixing,
methodically, all of the issues with the document — and if not, find a way to
implement that into the loop using the local models, the free API keys and
Claude.*

The honest answer was no. The loop as designed addressed 7 of the 12 remaining
items and I had been treating the other 5 as a separate mechanical project.
That was wrong. Each of them has a **research question at its core**; I had
been seeing only the mechanical step that follows the answer.

This maps all 12 into one queue.

## The reframe

A task belongs in the loop if the hard part is *finding something out*. The
mechanical step afterwards — running a capture, drawing a box on an image,
writing a table cell — is the easy half and always was.

| Item | I called it | It actually is |
|---|---|---|
| 10 / 31 | capture engineering | *which of 899 catalogue entries is a real, runnable tool, and what is its entry point* |
| 24 | screenshot engineering | *what input makes this GUI show something worth looking at* |
| 39 | image engineering | *which controls on this window deserve explaining* |
| 11 | a generator tweak | *does this tool have a command line at all* |

## The queue

Work is drawn from `docs/REVIEW-FEEDBACK.md`. Each item declares what evidence
closes it and what the mechanical follow-through is.

### Content items — already in scope

**18 "when you would use it", 17 purposes, 16 invocations, 19 gotchas,
20 sources.** Retrieve passages showing the tool or flag in use, compress to
one grounded sentence, gate, audit, cite. Covered by the existing design.

**40 fields populated from whatever fills them.** Structural: the gate refuses
any text not grounded in a retrieved passage, so a field can only be filled by
evidence. This one is closed by construction rather than by effort.

### Coverage items — 899 tools with no capture

The blocker is not capture capacity. It is that we do not know what to run.

Measured: of 899 uncaptured catalogue entries, **722 already carry binary
names** and only need capture executed. The remaining **177 have no binary
name recorded** — and several plainly are the binary (`rtfdump.py`,
`emldump.py`, `msgconvert`), which is precisely the kind of thing a search
resolves in one hit.

**Research question per tool:** is this real and still maintained, what is its
executable entry point, is it CLI or GUI, and which kit actually ships it.

**Sources:** the project's own repository and README, the REMnux and Kali
package pages, the distribution package index.

**Gate:** a resolved binary name is only accepted if the tool's own
documentation shows it being invoked. A guessed executable name is the same
failure as a guessed flag.

**Mechanical follow-through:** feed resolved names to the existing capture
probe. Closes item 10 (nothing to link to) and item 31 (present in the
catalogue but absent from the guide).

### Item 11 — tools with no command line

Currently an em dash, which reads as missing data rather than as a fact.

**Research question:** does this tool have a CLI at all? A GUI-only tool is
not a gap in the guide, it is a property of the tool, and saying so plainly is
more useful than a blank.

Falls out of the same pass as items 10 and 31 — the same sources answer it.

### Item 24 — screenshots devoid of context

The 12 removed screenshots were empty windows. The one that works, `die`,
works because it was captured **with `notepad.exe` loaded** — it shows format,
architecture, compiler and the signature chain rather than an empty frame.

**Research question per GUI tool:** what input makes this tool display
something worth looking at, and what does a walkthrough show it displaying?

This is answerable from the same walkthroughs that answer the flag questions —
they are full of screenshots and descriptions of what the tool shows.

**Mechanical follow-through:** capture with `PrintWindow` after loading that
input. The blank-render refusal already added means an empty window cannot
ship even if the input fails to load.

### Item 39 — annotated callouts

Wanted, and flagged as a later step.

**Research question:** which controls on this window actually matter to a
junior analyst? A window has dozens; a callout on each teaches nothing.

**Mechanical follow-through:** the accessibility tree already records a
bounding rectangle for every control, so once the loop decides *which*
controls matter, the arrows can be drawn at exact coordinates. No manual image
editing.

### Item 32 — serve a junior analyst

Not a task. It is the audit criterion applied to every other item, and the
question the final pass asks.

## Which tier does what

Same split as the measured research: diversity comes from sources, not from
asking several models the same question.

| Tier | Role |
|---|---|
| Local models, 3090 + 4090 | Bulk drafting and extraction — one grounded sentence per passage; resolving binary names from fetched pages. Measured adequate at 9-14B, ~11s each, free |
| Free API models | Search a *different* way and improve a draft. Their value is different queries surfacing different pages, not a bigger parameter count |
| Claude | Final pass/fail on nuance, intent, and whether it serves a junior analyst — and the judgement calls: which controls deserve a callout, which of two conflicting sources wins |

## Parallelism

The two workloads do not contend. Retrieval is network-bound and runs
continuously; capture is VM-bound and runs in batches. Both GPUs are free —
rick's 4090 was released by unloading the screen-vision model, and l3e7's 3090
is idle.

## What "done" means

Not "every cell is full". Done is when a pass produces nothing that beats what
is already there, and the miss log has stopped shrinking — with every miss
recorded as a question still open rather than a blank asserting no answer
exists.
