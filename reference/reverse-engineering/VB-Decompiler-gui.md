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

## When you'd reach for this

Reach for VB Decompiler when the sample is **Visual Basic 6** or **VB.NET / C#**. VB6 is the case that catches people out, because it compiles two different ways and what comes back depends entirely on which: P-code recovers a large share of the original logic, while native-compiled VB6 leaves you much closer to ordinary disassembly. Establish which you have before judging the tool.

Expect a partial reconstruction rather than compilable source. The vendor quotes roughly 85% logic restoration for P-code and around 95% for .NET. That is enough to read intent, which is usually the question, and not enough to rebuild the program.

For .NET specifically, dnSpy is the better first stop because of its debugger. VB Decompiler earns its place on the VB6 samples dnSpy cannot open at all.

**Sources:** <https://www.vb-decompiler.org/products.htm> · <https://www.vb-decompiler.org/faq.htm>

## Controls

The parts of this window you will actually touch, read from the application's own accessibility tree rather than from a screenshot. The full node list is in [`capture/gui/VB-Decompiler/VB-Decompiler.tree.txt`](../../capture/gui/VB-Decompiler/VB-Decompiler.tree.txt).

The window exposes 3 further named controls: **Decompile**, **...**, **Decompiler**. The full tree, with every automation id, is in [the capture](../../capture/gui/VB-Decompiler/VB-Decompiler.tree.txt).

## Using it

1. Open the Visual Basic executable.
2. Check whether it is p-code or native — the tool tells you, and it decides how much you get back.
3. Read the form definitions: VB malware often carries its logic in event handlers rather than in a main routine.

## Gotchas

- P-code decompiles close to source. Native-compiled VB gives you disassembly with VB runtime calls, which is a different and much slower job.
- The Lite edition omits much of the analysis. Check which build you are on before concluding a feature is missing.
