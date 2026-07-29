# Implementation Plan

Goal: a field quick-reference covering the kit's tools, capability-indexed, with
every command's options completely listed and explained, verified against real
binaries.

Status legend: ✅ done · ▶ next · ○ pending

---

## Phase 0 — Foundations ✅

- ✅ **Scope fixed.** `catalog/kit-tools.json` + `KIT-TOOLS.md`: 1,006 tools,
  5 platforms, 54 categories, each from an upstream machine-readable manifest.
- ✅ **Format designed** from six reference works — `docs/FORMAT.md`.
- ✅ **Verification proven.** `cyberlab-aio:v1` on rick has `fls`, `clamscan`,
  `binwalk`, `yara`, `vol`, `tshark`, `exiftool`, `log2timeline.py`.
- ✅ **Worked example** — `reference/filesystem-analysis/fls.md`, 22 options
  from a real capture.

## Phase 1 — Capability taxonomy ▶

The primary index. Draft ~40–60 capabilities phrased as **problems**, not tool
names, e.g. *"Recover deleted files from an image"*, *"Find what persisted on a
host"*, *"Decode an obfuscated payload"*, *"Prove lateral movement"*.

- Seed from the categories already carried by upstream: REMnux's 11 capability
  categories, Kali's 12 `kali-tools-*` groups, Security Onion's 9, and SANS
  investigative-task ordering.
- Map every one of the 1,006 kit tools to ≥1 capability. Tools that map to none
  are reported, not silently dropped — an unmapped tool is either a taxonomy gap
  or genuinely out of scope, and both need a decision.
- **Deliverable:** `reference/INDEX.md` — capability → tools → page links.

**Open question for review:** should the capability taxonomy follow an existing
public framework (NIST/DFIR phases, MITRE ATT&CK tactics) for familiarity, or a
kit-native one tuned to what we actually carry? Recommendation: kit-native
primary, with ATT&CK IDs as secondary tags where they genuinely apply — forcing
forensic tools into attacker tactics distorts both.

## Phase 1b — Mine cyberlab as a source ▶

The cyberlab training lab already contains a large body of commands and prior
exhaustive research. It is **read-only input** here — cyberlab is on hold and
receives no changes.

- `scripts/mine_cyberlab.py`: extract every fenced command block from the 61
  modules, plus `docs/CURRICULUM_ROADMAP.md`, `docs/TEST_REPORT.md` and
  `docs/CONTENT_QUALITY_AUDIT.md`, and the `catalog/` research.
- Produce `capture/cyberlab-candidates.json`: tool → observed invocations,
  with the module each came from.
- These become **candidate invocations** for the "Common invocations" section —
  real workflows someone already thought through, which is exactly the part that
  is expensive to invent.

**Mine the cleaned branch, not `main`.** The content-quality audit found
fabricated CLI flags in ~44 of 61 modules, concentrated in the generated
"enrichment tail". Branch `audit/content-quality-p0-p1` (PR #1) already removed
that tail — ~11,000 lines — so it is the higher-signal source. Modules 57
(acquisition) and 58 (eventlog) were rated the cleanest and are worth reading
first.

**Candidates are never trusted.** Every mined invocation still has to pass the
Phase 3 linter against a real capture. Mining saves the *thinking*, not the
*verification* — a mined command with an invented flag must fail exactly as
loudly as one written from scratch.

## Phase 2 — Capture pipeline ○

`scripts/capture_help.py`: for each in-scope tool, run `--help`/`-h`/`man` in
the right container, store raw output under `capture/<tool>.help.txt`.

- Containers: `cyberlab-aio:v1` and `dfir-aio:v4` on rick (Docker active, 830 GB free).
- **Always timeout-guard** — `vol` once pinned 99% CPU indefinitely on a
  synthetic image. Hard per-tool timeout, failure recorded not retried blindly.
- Emit a coverage report: which kit tools are covered by a container, which need
  a booted VM (Kali, FLARE-VM Windows guests), which are GUI-only and have no
  CLI surface to document.

**Reality check:** the 1,006-tool list includes GUI-only tools (Autopsy,
Wireshark GUI, PE-bear) and appliance services (Elasticsearch, Kibana) with no
meaningful command surface. Expect the genuinely CLI-documentable set to be
substantially smaller. Phase 2's report turns that from a guess into a number
before any page is written.

## Phase 3 — Page generation + linter ○

- Generate a page skeleton per tool from its capture: header, synopsis, complete
  options table. Mechanical, deterministic — no model invention.
- Human/model adds only the *judgement* columns: purpose, "when you'd use it",
  invocations, gotchas.
- `scripts/lint.py` gates the build:
  - every documented flag exists in the capture;
  - every captured flag appears in the page (**completeness**, the hard requirement);
  - every tool is in `kit-tools.json`;
  - format rules hold (imperative mood, ≤8 examples, placeholder syntax).

## Phase 4 — Print render ○

Markdown → PDF for field carry. Build artifact only, never hand-edited.
Per-capability booklets rather than one 1,000-page brick.

## Phase 5 — Prioritised content ○

Do not attempt all tools at once. Order by field value:

1. Core forensics: TSK suite, Volatility, Plaso, RegRipper, bulk_extractor
2. Network: Zeek, Suricata, tshark, tcpdump
3. Malware triage: YARA, ClamAV, capa, FLOSS, Detect-It-Easy
4. Live response / hunting: Velociraptor, osquery, Hayabusa, Chainsaw
5. Offensive-side as needed for exercises

---

## Risks

| Risk | Mitigation |
|---|---|
| Fabricated flags (killed the predecessor project) | Capture-or-it-does-not-ship, enforced by linter |
| Scale — 1,006 tools is a lot of pages | Phase 2 coverage report right-sizes it; Phase 5 prioritises |
| Kit VMs powered down (`kali`, `range-linux-web`, `redinfra01`) | Containers cover most Linux tooling; boot VMs only for the remainder |
| Version drift between capture and deployed kit | Version + capture date in every page header |
| GUI-only tools with no CLI | Identify in Phase 2; document workflow, not flags |
