<!-- generated-by: scripts/generate_gui_pages.py -->
# vbdec (GUI)

| | |
|---|---|
| **Capability** | reverse engineering |
| **Window title** | vbdec |
| **Captured from** | `C:\Tools\vbdec\vbdec.exe` on 2026-08-02 — control tree in [`capture/gui/vbdec/vbdec.tree.txt`](../../capture/gui/vbdec/vbdec.tree.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Decompile VB5 and VB6 binaries, recovering forms, controls and event handlers. Those names usually survive compilation and describe what the program was written to do.

## When you'd reach for this

The command-line companion for the same Visual Basic targets as VB Decompiler. Reach for it when you are processing a set of samples rather than opening one, or scripting extraction into a pipeline; use the window when you are reading a single sample and want to navigate it.

The format caveat is identical: VB6 P-code reconstructs well, native-compiled VB6 much less so, and knowing which you have is the first question rather than an afterthought.

**Sources:** <https://www.vb-decompiler.org/products.htm>

## Controls

The parts of this window you will actually touch, read from the application's own accessibility tree rather than from a screenshot. The full node list is in [`capture/gui/vbdec/vbdec.tree.txt`](../../capture/gui/vbdec/vbdec.tree.txt).

The window exposes 1 further named controls: **Search Log**. The full tree, with every automation id, is in [the capture](../../capture/gui/vbdec/vbdec.tree.txt).

## Using it

1. Open the VB5/VB6 binary.
2. Work from the form and control names, which usually survive and describe the program's intent.

## Gotchas

- Scope is VB5 and VB6 only. VB.NET is a .NET assembly — use [dnSpy](../reverse-engineering/dnSpy-gui.md) for those.
