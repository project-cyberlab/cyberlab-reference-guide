# Review feedback

Every issue raised while reading the built PDF, with what was done about it.
Kept because a verbal list evaporates and because several of these were
regressions I introduced and would otherwise reintroduce.

Status: **done** · **partial** · **open**

---

## Navigation and structure

| # | Issue | Status | Notes |
|---|---|---|---|
| 1 | Phase entries are blue but not clickable | **done** | Not a styling bug. `strip_placeholders` deleted any heading whose body looked empty, and `## Acquire & preserve` is followed immediately by `###` subheadings — so the heading and its anchor were removed. Every phase link dangled. |
| 2 | Kit Tool List contents links do not work | **done** | Same cause. 11/11 anchors present, 0 dangling. |
| 3 | Links do not jump in a browser | **done** | Named destinations; Adobe resolves them, Chrome/Edge/Firefox largely do not. All 1,700+ are explicit page destinations now. |
| 4 | Links pointed at directories on the author's disk | **done** | Relative paths rendered from a `file://` URL. Repo-internal links became anchors; evidence links became GitHub URLs. |
| 5 | Implementation plan / roadmap takes up space | **done** | Removed from the PDF; still in the repo. |
| 6 | Risks section not needed | **done** | Lived in `docs/PLAN.md`, removed with it. |
| 7 | Content clipped, cannot scroll right | **done** | `overflow-x: auto` gives a scrollbar on a web page and nothing on paper — text past the edge was unreachable. Long lines wrap now. |
| 8 | Alphabetical tool index | liked | Kept. |

## The kit tool list

| # | Issue | Status | Notes |
|---|---|---|---|
| 9 | Purpose column empty on Kali | **done** | And on FLARE and SIFT — 702 of 1006 rows. Their upstream manifests carry no description field. Harvested from the APT indices and the vm-packages NuGet feed: Kali 0→95.8%, FLARE 0→98.5%, SIFT 0→90.7%. |
| 10 | Tools do not link to their pages | **partial** | 177 links added. Only 86 of 911 catalogue names have a capture at all, so most have no page to link to yet. |
| 11 | Tools with no command should be identified | open | Currently an em dash; should say explicitly that the tool has no CLI. |
| 12 | Validation pass over tool / command / purpose | **done** | `scripts/audit.py`. |

## Content quality

| # | Issue | Status | Notes |
|---|---|---|---|
| 13 | Invalid-argument text appearing in fields | **done** | `fls: invalid option -- '-'` and `Invalid argument: bdeinfo` reached Purpose lines. Page-level audit findings 18 → 0. Captures keep the stderr as evidence; it no longer reaches a page. |
| 14 | Version numbers should be short | **done** | Was emitting 40-char git hashes, `/data/version is not a valid directory!`, `------> --version <------`. |
| 15 | Auto-populating from cyberlab | **done** | cyberlab reached ~25% before the project pivoted and its own audit found fabricated flags in ~44 of 61 modules. Nothing auto-publishes from it. Mined data stays in `capture/` as a research lead. |
| 16 | Common invocations give no functional value | **partial** | Hand-written and task-labelled now, so each says *why*. Done for `mmls`; the rest to follow. |
| 17 | Purposes too thin to tell you what a tool does | **partial** | 87 pages had a Purpose under 70 chars, many of them scraped banners (`hashcat (v6.2.6) starting in help mode`). Down to 60; parser now rejects banners, labels and synopses. |
| 18 | "When you would use it" column empty | **partial** | 837 of 3166 rows (26%). The largest remaining gap. |
| 19 | Gotchas are good, want more elaboration | open | |
| 20 | Sources / research should keep expanding | open | |

## GUI pages

| # | Issue | Status | Notes |
|---|---|---|---|
| 21 | No GUI tools in the document | **done** | 13 captured, 13 pages. |
| 22 | Screenshots broken | **done** | Image paths were relative to the markdown but rendered from `build/`. Embedded as data URIs; the PDF is self-contained. |
| 23 | **Screenshot captured the taskbar and a news headline** | **done** | The operator's personal content, published. Cause: capturing a *screen region*, which grabs the desktop by construction. Image removed; capture must render the window itself. |
| 24 | Screenshots are functionally devoid of context | **partial** | `die` re-captured against a real PE now shows format, architecture, compiler and the signature chain. The other 12 regressed behind modal dialogs and still show empty windows. |
| 25 | AutomationId column not wanted | **done** | Linter plumbing, not analyst information. |
| 26 | Control table is ugly / a data dump | **done** | Restructured on the Wireshark User's Guide model: prose plus the major parts, not 179 rows. |
| 27 | `Window: WindowsForms10.Window.8.app.0.378734a` means nothing | **done** | Replaced with the window title. Blank `Version: —` now omitted. |
| 28 | Designer defaults listed as controls | **done** | `menuStrip1`, `statusStrip1` filtered. |
| 29 | Vendor screenshots acceptable if audited | **done** | Policy rewritten: the test is which image teaches more. External images need six checks including a 7B vision-model read diffed against the control tree. |

## Scope

| # | Issue | Status | Notes |
|---|---|---|---|
| 30 | Basic OS commands do not belong | **done** | `less`, `pager`, `sensible-pager`, `grep`, `stat`, `curl`, `wget` removed. Conservative: `file`, `strings`, `xxd`, `dd`, `md5sum`, `ssdeep`, `unzip`, `7za` are generic Unix but genuinely part of triage. |
| 31 | If it cannot be in the guide, remove it | open | 825 catalogue entries have no capture. They are real analyst tools the platforms ship; we capture from containers, not the VMs. REMnux now probed directly — 217 captured. |
| 32 | Guide must serve a **junior analyst** | **partial** | Written into `docs/FORMAT.md` as the governing test. A page must say when to reach for the tool, what to type first and why, and what comes before and after it. |

---

## The loop

Raised: build a research loop, as other projects here have, using local models
and spare API keys to keep it token-light.

`scripts/research_loop.py` does this. Evidence in, draft out, validate hard:
it prompts a local model with **only** a tool's captured help, then rejects any
note that mentions a flag absent from that capture, restates the help, hedges,
or runs long. Survivors land in `enrichment_draft.py`, which the build does not
read — quarantine, not output.

That constraint is the whole design. An unvalidated model writing command
guidance is the cyberlab failure reproduced at machine speed.
