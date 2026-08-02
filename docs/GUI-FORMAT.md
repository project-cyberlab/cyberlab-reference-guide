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
- **Show the tool doing something.** An empty main window documents the layout
  and nothing else. Launch the tool against a sample so the panes hold real
  output — a detected packer, a parsed header, a computed hash. The sample must
  be benign; nothing in this pipeline hands live malware to a tool
  automatically, and a clean binary exercises the same interface.

### Where screenshots may come from

Ours first, always. A capture from the kit's own build needs no vetting: the
version is known, the theme and OS are ours, there is no watermark, no licence
question and no third party's private data in the frame. One reboot captures
the whole FLARE toolset, which is cheaper than assessing a single borrowed
image.

A screenshot from a reputable external source is acceptable **only** for a tool
we cannot run ourselves — a GUI on a VM with no desktop session, or a web
console — and only after it passes every one of these:

1. the version shown matches the version in the kit, or the difference is stated
2. the source is the vendor, the project's own documentation, or its repository
3. the licence permits reuse, and the source is cited in `capture/SOURCES.md`
4. no watermark, no third-party branding, no personal or customer data
5. the controls visible in it match the control tree we captured, where we have one
6. it illustrates the task the surrounding text describes, not a different one

Item 5 is checked by reading the image, not by glancing at it. Run it through
the 7B vision model on rick's 4090 and have it enumerate what is actually on
screen — window title, version string, every visible control and label — then
diff that against the control tree. Repeat the pass until it is stable; a
single look is how a wrong-version screenshot gets through. If the model
cannot resolve the detail well enough to enumerate controls, the image is not
good enough to publish.

An external screenshot is illustration, never evidence: it can never satisfy
item 6 of §1, because only a tree dump from the running application can.

Two capture paths exist, and they have different reach:

| Path | Reach | Status |
|---|---|---|
| Hypervisor framebuffer (`qm monitor screendump`) | whole screen, no guest cooperation | working — used to diagnose the VM 101 boot failure |
| In-guest per-window capture + UIA dump | single window, plus the control tree | **working**, see below |

### Getting into the interactive session

GUI automation must run in the interactive desktop session. Anything driven from
outside lands in session 0, which has no window station, so `Start-Process`
returns a process with no window and the tree comes back empty:

```
session 0  services  Disconnected   <- SSH and the guest agent land here
session 1  flare     Active         <- the desktop, explorer running
```

What did not work, recorded so it is not retried:

- `schtasks /IT`, both with `/RP` and with `/NP`, returned
  `SCHED_S_TASK_HAS_NOT_RUN` (267011).
- `PsExec -i 1` failed with *"Error creating key file... The handle is
  invalid"*. PsExec needs valid console handles and the guest-agent channel
  supplies none; redirecting from `NUL` did not satisfy it either.

What works: a script in the **All Users Startup folder**, executed by autologon
after a reboot. It runs as the console user in session 1 with a real desktop.

> Check `DefaultPassword` before rebooting for this. On VM 101 `AutoAdminLogon`
> was `1` but `DefaultPassword` was absent, so autologon would not have fired and
> the machine would have stopped at the logon screen — with SSH password auth
> already broken, that would have stranded it. Set the account password and the
> autologon credentials, snapshot, *then* reboot.

### Walking the tree

`FindAll(TreeScope::Descendants)` on the top-level window is not enough. For
applications whose content is virtualised — modern XAML, Qt, Java — it returns
almost nothing; Notepad reports two Panes and no menu at all. Recurse with
`TreeWalker.ControlViewWalker` instead, and expand `MenuItem`/`Menu` nodes
through `ExpandCollapsePattern` on the way past, because a collapsed menu
reports only its own label.

Worked example, captured from the kit's own build:
[`capture/gui/die/die.tree.txt`](../capture/gui/die/die.tree.txt) — Detect It
Easy v3.10, 41 controls carrying stable AutomationIds, with the screenshot
beside it.

The reason this satisfies §2 is visible in that file:

```
ComboBox "Scan" #GuiMainWindow.centralwidget.widgetFormats.groupBoxScanEngine.comboBoxScanEngine
  List
    ListItem "Automatic"
    ListItem "Detect It Easy (DiE)"
    ListItem "Nauz File Detector (NFD)"
    ListItem "Yara rules"
```

Those four ListItems are the permitted values of a GUI control, enumerated from
the running binary. They are the direct analogue of a CLI flag's accepted
arguments, and they can be linted exactly the same way.

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
