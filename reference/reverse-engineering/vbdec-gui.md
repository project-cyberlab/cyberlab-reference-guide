<!-- generated-by: scripts/generate_gui_pages.py -->
# vbdec (GUI)

**Capability:** reverse engineering  **Window:** `ThunderRT6FormDC`  **Version:** —
**Captured:** `C:\Tools\vbdec\vbdec.exe` on 2026-08-02 — control tree in [`capture/gui/vbdec/vbdec.tree.txt`](../../capture/gui/vbdec/vbdec.tree.txt)

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Visual Basic 5/6 decompiler.

## Window

![vbdec main window](../../capture/gui/vbdec/vbdec.png)

## Controls

All 8 nodes come from the capture; the 1 interactive controls are listed here.

| Control | Type | AutomationId | What it does |
|---|---|---|---|
| **Search Log** | Pane | `10` | |

## Using it

1. Open the VB5/VB6 binary.
2. Work from the form and control names, which usually survive and describe the program's intent.

## Gotchas

- Scope is VB5 and VB6 only. VB.NET is a .NET assembly — use [dnSpy](../reverse-engineering/dnSpy-gui.md) for those.
