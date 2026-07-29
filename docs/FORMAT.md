# The Format

How every page in this guide is built, and why. Derived from studying the
reference works that already do this well, then fixing what they each get wrong
for our use case: **a field guide you open mid-mission when you need a
capability and do not remember the tool.**

---

## 1. What the research said

| Source | What it does well | What it does not give us |
|---|---|---|
| [tldr-pages style guide](https://github.com/tldr-pages/tldr/blob/main/contributing-guides/style-guide.md) | Curated examples (≤8), imperative mood, `{{placeholder}}` syntax, machine-linted | Deliberately **incomplete** — omits most options by design. No capability index. |
| [POSIX Utility Conventions ch.12](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap12.html) + [man-pages(7)](https://www.man7.org/linux/man-pages/man7/man-pages.7.html) | Unambiguous synopsis grammar: `[]` optional, `\|` exclusive, `...` repeatable | Reference-shaped, not task-shaped. You must already know the tool's name. |
| [SANS DFIR cheat sheets](https://www.sans.org/posters/sans-dfir-cheatsheet-booklet) | Organised by **investigative task** — the right primary axis | Print-first, not greppable, not exhaustive on flags |
| [Jai Minton DFIR cheatsheet](https://www.jaiminton.com/cheatsheet/DFIR/) | 200+ scannable anchors; artifact paths and ATT&CK IDs as headings | *"Most entries lack detailed flag documentation… assumes operator familiarity"* |
| [navi / cheat.sh](https://github.com/JoverZhang/navi-cheats) | Machine-parseable, taggable, directly executable entries | No explanation layer at all |
| [Progressive disclosure](https://ixdf.org/literature/topics/progressive-disclosure) (Nielsen, 1995) | Layer information: essentials first, depth on demand | — |

**The gap we fill:** every existing DFIR quick-reference assumes you already
know the tool and its flags. None of them explains the options. That is exactly
the layer this guide exists to provide, and it is why "completely listed out"
is a hard requirement rather than a stretch goal.

---

## 2. Two entry points, one dataset

You arrive at this guide in one of two states:

1. **"I have a problem."** — *I need to recover deleted files from this image.*
   → **Capability Index**: capability → tool → command → options.
   This is the primary path and the reason the guide exists.
2. **"What do I have?"** — *Is there anything in the kit for Go binaries?*
   → **Kit Index**: VM → category → tool.
   This is `catalog/KIT-TOOLS.md`, generated from upstream manifests.

Both views are projections of the same JSON, so they can never disagree.

---

## 3. Scope is binding

A tool may appear in this guide **only** if it is in `catalog/kit-tools.json`,
which is generated from the kit's own VM manifests. If it is not in the kit, it
does not get a page — no matter how good the tool is.

Every command entry is tagged with the **VM(s) that carry it**, so in the field
you instantly know whether you can actually run it on the box in front of you.

---

## 4. The page format

Every tool page has these sections, in this order. Sections are layered by
progressive disclosure: a reader in a hurry stops after §3; a reader who needs
precision continues to §4.

### Header
```
# <tool>
**Kit:** REMnux · SIFT   **Category:** Filesystem analysis   **Version:** 4.11.1
**Docs:** <upstream URL>   **Verified:** 2026-07-29 from `cyberlab-aio:v1`
```
The version and the verification date are not decoration — they are the claim
that the options below were read off the real binary on a known date.

### 1. Purpose — one line, imperative
> List files and directory names in a disk image, including deleted entries.

### 2. Synopsis — POSIX notation, verbatim from the tool
```
fls [-adDFlhpruvV] [-f fstype] [-i imgtype] [-b dev_sector_size] [-m dir/]
    [-o imgoffset] [-z ZONE] [-s seconds] image [images] [inode]
```

### 3. Common invocations — ≤8, task-titled, copy-paste ready
Each example is titled by **the task it accomplishes**, not by the flag it uses,
because the reader is searching by intent. Placeholders use tldr syntax so they
are visually obvious and machine-checkable:

```
# List deleted files in a partition, recursively, with full paths
fls -rpd -o {{2048}} {{path/to/image.dd}}
```

### 4. Options — COMPLETE, one row per flag
Every flag the binary accepts. Not the useful ones — **all** of them.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-d` | — | Display deleted entries only | Narrowing a recovery hunt to what was removed |

The fourth column is the one that makes this a guide rather than a man page
dump. It answers *why would I reach for this*, which is what you actually need
under time pressure.

### 5. Gotchas
Real operational traps, each one earned. Examples already known on this project:
timeout-guard `vol`, `binwalk`, `clamscan` and `radare2` in any harness — a
synthetic memory image once pinned `vol` at 99% CPU indefinitely.

### 6. See also
Sibling tools for the same capability, so a dead end reroutes instead of stalling.

---

## 5. Verification: why the options can be trusted

The predecessor project shipped **fabricated CLI flags in roughly 44 of its 61
modules** — invented options for `yara`, `clamscan`, PE-bear, `scdbg` and
others — because content was generated from a language model rather than read
off the tools. That failure is the reason this guide exists in its current form.

So the rule here is mechanical, not aspirational:

1. Run the tool's `--help` / `-h` / man page **inside the kit container or VM**.
2. Store the raw output under `capture/<tool>.help.txt`, committed.
3. Generate/check the options table **against that capture**.
4. `scripts/lint.py` fails the build if a documented flag is absent from the
   capture, or if a captured flag is missing from the page.

A flag that cannot be produced from a real binary cannot ship. This is the same
discipline `tldr-lint` applies to formatting, applied instead to truth.

**Worked proof.** The captured `fls` usage line advertises `[-adDFlhpruvV]`, but
the body of the same output documents `-P`, `-B`, `-S` and `-k` as well. Anyone
transcribing the synopsis — or working from memory — silently loses four real
options. Only a capture catches that.

---

## 6. Sources and citation validation

Two different claims need two different kinds of evidence, and they must not be
confused:

- **What a flag *is*** → the binary. Captured, committed, linter-enforced (§5).
  No online source overrides a real `--help`.
- **What a tool is *for*, and how practitioners actually use it** → authoritative
  upstream documentation and reputable DFIR publishers.

Acceptable sources for the second kind, in preference order: the project's own
docs/repo (sleuthkit.org, volatilityfoundation.org, docs.remnux.org,
ericzimmerman.github.io, Microsoft Learn), then recognised practitioner sources
(SANS, thedfirreport.com, Red Canary, Mandiant/Unit42), then MITRE ATT&CK for
technique mapping.

**Every cited URL is liveness-checked before it ships.** The predecessor project
shipped hallucinated citations that looked plausible and 404'd; it already has a
hardened, allowlisted, deadline-guarded fetcher (`cyberlab_retrieval.py`, with
`verify_url`) built precisely for this, and this guide reuses that discipline.
A dead or unreachable citation fails the build rather than degrading quietly.

Version skew is a real hazard: upstream docs describe the *current* release,
while the kit runs pinned versions (TSK 4.11.1 in the container vs 4.15.0 in the
tracker, for example). Where docs and capture disagree, **the capture wins** and
the discrepancy is worth a line in Gotchas.

## 7. Output

- **Markdown** is the source of truth: greppable, diffable, reviewable, renders on GitHub.
- **PDF/print render** is generated from the markdown for field use. It is a
  build artifact, never hand-edited, so the two can never drift.
