<!-- generated-by: scripts/generate_gui_pages.py -->
# VB-Decompiler (GUI)

| | |
|---|---|
| **Capability** | reverse engineering |
| **Window title** | VB Decompiler Lite v26.4 |
| **Version** | v26.4 |
| **Captured from** | `C:\Tools\VB Decompiler\VB Decompiler.exe` on 2026-08-02 — control tree in [`capture/gui/VB-Decompiler/VB-Decompiler.tree.txt`](../../capture/gui/VB-Decompiler/VB-Decompiler.tree.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Recover source-level structure from Visual Basic executables. P-code binaries decompile close to the original; native-compiled ones yield disassembly with the VB runtime calls identified.

## Controls

The window exposes 3 further named controls: **Decompile**, **...**, **Decompiler**. The full tree, with every automation id, is in [the capture](../../capture/gui/VB-Decompiler/VB-Decompiler.tree.txt).

## Using it

1. Open the Visual Basic executable.
2. Check whether it is p-code or native — the tool tells you, and it decides how much you get back.
3. Read the form definitions: VB malware often carries its logic in event handlers rather than in a main routine.

## Gotchas

- P-code decompiles close to source. Native-compiled VB gives you disassembly with VB runtime calls, which is a different and much slower job.
- The Lite edition omits much of the analysis. Check which build you are on before concluding a feature is missing.
