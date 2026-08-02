# Documenting GUI tools

The guide's rule for CLI tools is *capture-or-it-does-not-ship*: every documented
flag must appear in a real `--help` capture, enforced by `scripts/lint.py`. That
rule is why this project exists — the predecessor shipped fabricated flags in ~44
of 61 modules.

GUI tools have no `--help`. This document defines the equivalent evidence chain,
so a GUI page carries the same guarantee rather than a weaker one.

---

## 1. What a GUI page must contain

The CLI page answers *tool → command → every option*. The GUI page answers
**tool → task → every control that task touches**, plus a complete control
inventory so nothing is silently omitted.

| # | Item | Required | Evidence source | Notes |
|---|---|---|---|---|
| 1 | Tool name, version, kit membership | yes | installed build | Version must come from the running app, not the vendor page. |
| 2 | Launch method | yes | live | Binary path, Start-menu entry, or `.desktop` file. Include the CLI entry point when one exists. |
| 3 | Purpose (one sentence) | yes | vendor docs | What problem it solves. |
| 4 | Window/pane map | yes | UIA / AT-SPI | The top-level regions and what each is for. Autopsy's Tree / Result / Content viewers are the model. |
| 5 | **Menu tree** | yes | UIA / AT-SPI | Every menu and submenu item, verbatim. This is the direct analogue of the options table. |
| 6 | **Control inventory** | yes | UIA / AT-SPI | Every dialog, checkbox, field and button reachable from the documented tasks. Completeness lives here. |
| 7 | Task procedures | yes | vendor docs + live | Numbered click-paths. See §4. |
| 8 | Screenshots | per task | live capture | See §5. |
| 9 | Gotchas | if known | live | Traps found while driving it. |
| 10 | Citations | yes | vendor docs | Liveness-checked by `scripts/validate_sources.py`. |

Items 5 and 6 are what make the page *complete* rather than merely helpful. A
control present in the capture but absent from the page is the GUI equivalent of
`W-MISSING` and must be reported the same way.

---

## 2. Two evidence sources, and why both are mandatory

Neither source alone reproduces the CLI guarantee. This was measured, not assumed.

**Vendor documentation** — gives procedures, semantics and the *why*. It is
mineable and citable. But it is organised by feature, not by control: the Autopsy
user guide documents each ingest module on its own page and never enumerates the
`Tools → Options` dialog exhaustively. Mining it alone reproduces the failure this
project exists to prevent, because the gaps are invisible.

**Accessibility tree** — gives the exhaustive control inventory. UI Automation on
Windows and AT-SPI on Linux enumerate every menu, submenu, button, checkbox and
field as machine-readable text. **This is to a GUI what `--help` is to a CLI**:
reproducible, diffable, and lintable.

> Rule: prose and meaning may come from the vendor. The *list of controls* must
> come from the application. A control named in a page but absent from the tree
> dump is treated exactly like an invented flag.

---

## 3. Deciding what is a GUI tool

Not by name, and not from the package manifest. The catalogue is built from
upstream package lists, so it contains entries that are not binaries at all
(`X11`, `accept-all-ips`, and literally `absent`), plus duplicates (`7-zip` and
`7zip`). Any GUI count derived from it is fiction.

Classify from the installed binary:

- **Windows** — the PE optional header's `Subsystem` field: `2` = GUI, `3` = console.
  Exact, and it needs no execution. Measured across 400 installed FLARE
  executables: 16 GUI, 384 console, 0 unreadable.
- **Linux** — presence of a `.desktop` entry, or linkage against GTK/Qt.

A tool can be both (Wireshark ships `tshark`). When a CLI entry point exists it is
documented as a CLI page and cross-linked; the GUI page covers only what the CLI
cannot do.

---

## 4. Task procedures

Follow the Microsoft Writing Style Guide conventions already standard for this
kind of reference:

- One task per procedure. If it exceeds **seven steps** it is more than one task —
  split it.
- Steps are imperative and start with the action: "Select **File → Add Data Source**."
- UI element names are **bold** and verbatim, matching the accessibility tree
  exactly. One approved term per object, used everywhere.
- State the outcome, so the reader can tell the step worked.

---

## 5. Screenshots

Screenshots illustrate; they never carry a completeness claim on their own — an
image cannot be linted the way a tree dump can. Every screenshot must therefore
be paired with the control inventory it depicts.

Requirements:

- One screenshot per task step that changes what is on screen, at most.
- Captured from **the kit's own build**, not the vendor's marketing image, so the
  version in the caption matches the version in the header.
- Stored under `capture/gui/<tool>/` alongside the tree dump that backs it.
- Caption names the window and the control being exercised.

Two capture paths exist, and they have different reach:

| Path | Reach | Status |
|---|---|---|
| Hypervisor framebuffer (`qm monitor screendump`) | whole screen, no guest cooperation | **working** — used to diagnose the VM 101 boot failure |
| In-guest per-window capture + UIA dump | single window, plus the control tree | **blocked**, see below |

**Known blocker.** GUI automation must run in the interactive desktop session.
On VM 101 the SSH service lands in session 0, which has no window station, so
`Start-Process notepad` yields *no window found*:

```
session 0  services  Disconnected   <- SSH lands here
session 1  flare     Active         <- the desktop, explorer running
```

Two `schtasks /IT` variants returned `SCHED_S_TASK_HAS_NOT_RUN` (267011). The
probe script itself stages correctly, so this is solely an execution-context
problem. Untried: `PsExec -i 1`, a Startup-folder script run at autologon, or
driving the framebuffer with `qm monitor sendkey`. Until it is resolved, GUI pages
can carry vendor-sourced procedures and full-screen captures, but **not** the
control inventory — and a page without item 6 is incomplete and must say so.

---

## 6. Lint rules to add

Mirroring the CLI rules, so the same gate applies:

| Code | Meaning |
|---|---|
| `E-GUI-NOCAPTURE` | GUI page with no accessibility-tree dump in `capture/gui/` |
| `W-GUI-MISSING` | control in the tree dump absent from the page |
| `W-GUI-INVENTED` | control named in the page absent from the tree dump |
| `W-GUI-NOSHOT` | task procedure with no screenshot |
| `W-GUI-STEPS` | procedure longer than seven steps |

---

## 7. Order of work

1. Rebuild the catalogue from installed binaries rather than package manifests.
2. Run the subsystem classifier across all five kit VMs → the real GUI list and a
   real count.
3. Resolve session-1 execution → tree dumps and per-window screenshots.
4. Mine vendor documentation for the classified GUI tools, with citations.
5. Only then fix the page template, driven by what the captures actually contain.

Steps 1–2 are unblocked today. Step 3 gates items 5, 6 and 8.
