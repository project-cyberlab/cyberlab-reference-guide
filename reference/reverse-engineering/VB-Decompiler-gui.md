<!-- generated-by: scripts/generate_gui_pages.py -->
# VB-Decompiler (GUI)

**Capability:** reverse engineering  **Window:** `t0000000`  **Version:** v26.4
**Captured:** `C:\Tools\VB Decompiler\VB Decompiler.exe` on 2026-08-02 — control tree in [`capture/gui/VB-Decompiler/VB-Decompiler.tree.txt`](../../capture/gui/VB-Decompiler/VB-Decompiler.tree.txt)

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Visual Basic decompiler.

## Window

![VB-Decompiler main window](../../capture/gui/VB-Decompiler/VB-Decompiler.png)

## Controls

All 12 nodes come from the capture; the 5 interactive controls are listed here.

| Control | Type | AutomationId | What it does |
|---|---|---|---|
| **Decompile** | Pane | `131836` | |
| **...** | Pane | `655904` | |
| **Panel3** | Pane | `459348` | |
| **Decompiler** | Pane | `786932` | |
| **Panel2** | Pane | `393782` | |

## Using it

1. Open the Visual Basic executable.
2. Check whether it is p-code or native — the tool tells you, and it decides how much you get back.
3. Read the form definitions: VB malware often carries its logic in event handlers rather than in a main routine.

## Gotchas

- P-code decompiles close to source. Native-compiled VB gives you disassembly with VB runtime calls, which is a different and much slower job.
- The Lite edition omits much of the analysis. Check which build you are on before concluding a feature is missing.
