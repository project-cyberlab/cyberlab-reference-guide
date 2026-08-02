# GUI Tool Inventory

The list of kit tools that have a graphical interface, and therefore need a GUI
page rather than a CLI page. See [docs/GUI-FORMAT.md](../docs/GUI-FORMAT.md) for
what a GUI page must contain.

**Generated from installed binaries on the running kit VMs — not from the package
manifests.** The manifests cannot answer this question: they list package names,
so the 1,006-entry catalogue contains entries that are not binaries at all
(`X11`, `accept-all-ips`, and literally `absent`) alongside duplicates
(`7-zip` / `7zip`). Any GUI count derived from them would be fiction.

---

## Method

| Platform | Test | Why it is exact |
|---|---|---|
| Windows | PE optional header `Subsystem`: `2` = GUI, `3` = console | Recorded in the binary itself; needs no execution |
| Linux | A `.desktop` entry with `Terminal=false` | How the desktop itself decides to show a launcher |

Entries are then intersected with `catalog/KIT-TOOLS.md`, because a tool outside
the binding scope must not be documented — the desktop-shell applications
(GNOME Settings panels, IBus, Nautilus) are stripped by that intersection.

---

## Status

| VM | Access | Classified | GUI tools found |
|---|---|---|---|
| REMnux (142) | guest agent | yes | **17** (see below) |
| FLARE-VM (101) | SSH + agent | partial — install running | 16 GUI of 400 exes scanned |
| SIFT Workstation (143) | SSH + agent | yes | **0** — 2 entries, both snap plumbing |
| Kali (146) | SSH + agent | yes | 94 entries, **2** in the catalogue |
| Security Onion (170) | SSH | yes | **0** — headless by design |

Access was established by regenerating the cloud-init drive (142/146), which
changes the instance-id and forces cloud-init to re-run, and by offline key
injection into the LVM root for 170 (which has no cloud-init drive). A ZFS
snapshot `vmdata/vm-170-disk-0@pre-agent-inject` was taken first.

> The host's `/root/.ssh/id_rsa` and `id_rsa.pub` are **a mismatched pair** —
> `identity_sign: private key contents do not match public`. Every earlier
> "Permission denied" was a client-side signing failure, not an authorisation
> one. Lab access now uses `/root/.ssh/id_ed25519_lab`.

---

## The kit VMs do not contain the kit

This is the finding that matters most, and it undercuts the coverage numbers.

Spot-check of catalogued tools against what is actually installed:

**SIFT Workstation (143)** — 597 packages, and **every** core tool is absent:

```
fls  mmls  icat  log2timeline.py  psort.py  vol  volatility3
bulk_extractor  foremost  regripper  evtx_dump  plaso      -> all ABSENT
```

It is a bare Ubuntu 20.04.6 install; the SIFT tooling was never laid down. This
matches the known-broken SIFT installer (`repo.saltproject.io` decommissioned).

**Kali (146)** — a `kali-cloud` image (`6.19.14+kali-cloud-amd64`) carrying only
`kali-linux-core`, not the full metapackages the catalogue is derived from:

| Present | Absent |
|---|---|
| nmap, msfconsole, burpsuite, sqlmap, hydra, john, aircrack-ng, wireshark, responder | ghidra, maltego, zenmap, ettercap, beef-xss, bloodhound |

**Security Onion (170)** — 0 desktop entries, 0 X/GUI packages,
`multi-user.target`, 4 listeners on 80/443, 182 `so-*` commands. Headless by
design: its interface is the web console, so it needs the DOM treatment, not
UIA/AT-SPI. The 182 `so-*` commands are ordinary CLI tools and are capturable
today — none are currently in the guide.

### What this means

The 945 captured tools came from the **containers** (`cyberlab-aio`, `dfir-aio`),
not from these VMs. The "791 absent" tools are therefore not absent because a VM
was powered down — they are absent because **the VMs do not have those tools
installed**. Booting them changes nothing on its own.

Before further capture work:

1. Install the SIFT toolset on 143, or retire the VM and document SIFT from the
   container that actually carries the tools.
2. Decide whether Kali is in scope at the catalogue's 403 tools or at what
   `kali-linux-core` actually provides. Documenting 403 from a manifest while the
   VM carries a fraction of them would be documenting tools nobody can run.
3. Capture the 182 `so-*` commands — unblocked today.

---

## REMnux — classified

82 non-terminal `.desktop` entries were found; 65 were desktop-shell noise. The
17 that intersect the kit catalogue:

| Tool | Command | Notes |
|---|---|---|
| Ghidra | `/opt/ghidra/ghidraRun` | Large menu surface; the priority page |
| Cutter | `cutter` | Radare2 GUI; `r2` CLI already documented |
| Wireshark | `wireshark` | `tshark` CLI page exists — cross-link, do not duplicate |
| NetworkMiner | `networkminer` | GUI-only in practice |
| edb | `edb` | Debugger |
| wxHexEditor | `wxHexEditor` | Hex editor |
| CyberChef | `cyberchef` | Browser-based; see caveat below |
| SciTE | `SciTE` | Editor |
| Visual Studio Code | `/usr/share/code/code` | Editor; two entries (app + URL handler) |
| Detect It Easy | `die` | Has a `diec` CLI — cross-link |
| BinNavi | `binnavi` | Matched by name, not by the intersection |
| Document Viewer | `evince` | Borderline: general-purpose viewer |
| Feh | `feh` | Borderline: image viewer |
| Galculator | `galculator` | Borderline: calculator |
| Files | `nautilus` | Borderline: file manager |
| Wine | `wine` | Loader, not an analysis tool |
| IBus Preferences | `ibus-setup` | Almost certainly a false match |

**The last five need a scope decision.** They matched the catalogue but are not
DFIR tools in any meaningful sense. Options: tighten the intersection to the
tool's own catalogue row rather than a name match, or mark them out of scope
explicitly. Recording them rather than silently dropping them, per the same rule
the catalogue already uses for unmapped tools.

**Also note:** `Detect It Easy` and `BinNavi` did not match cleanly on command
name, which means the catalogue and the installed binaries disagree on naming.
That is a catalogue-quality finding in its own right.

### Tools with both a GUI and a CLI

Wireshark/`tshark`, Detect It Easy/`diec`, Cutter/`r2`. These get a CLI page as
today, and the GUI page covers only what the CLI cannot do. Duplicating option
tables across both would guarantee they drift.

### CyberChef

Runs in a browser, so it has no accessibility tree of its own in the desktop
sense — its controls live in the page DOM. It needs the web-app treatment
(DOM-derived control inventory), not the UIA/AT-SPI treatment. Security Onion's
console has the same shape.

---

## Next

1. Install `qemu-guest-agent` on VMs 143, 146, 170 → classify the remaining three.
2. Re-run the PE classifier on FLARE-VM once its 137-package install finishes.
3. Resolve interactive-session execution (see GUI-FORMAT §5) → tree dumps and
   per-window screenshots.
4. Decide the borderline scope cases above.
