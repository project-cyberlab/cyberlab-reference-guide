<!-- generated-by: scripts/generate_pages.py -->
# rafind2

| | |
|---|---|
| **Kit** | REMnux · Kali Linux · SIFT Workstation |
| **Capability** | Search raw data for a pattern |
| **Version** | rafind2 6.1.9 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-10 — [raw help output](../../capture/cyberlab-aio/help/rafind2.help.txt) |
| **Documentation** | <https://www.radare.org/n/radare2.html> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Examine binary files, including disassembling and debugging. Includes r2ai and decai plugins for LLM-powered analysis (API key or local Ollama required), plus the r2ghidra plugin for Ghidra decompilation via the pdg command.

## When you'd reach for this

When an analyst needs to search for specific strings, hex patterns, or zero-terminated strings within a binary file, they use rafind2 to quickly locate offsets, then feed those results to radare2 for contextual analysis. They choose it over similar tools because it provides minimal, precise output that integrates seamlessly with radare2 commands for deeper inspection, and supports efficient workflows like counting results or displaying hex dumps.

**Sources:** <https://book.rada.re/tools/rafind2/intro.html>

## Synopsis

```
rafind2 [-mBXnzZhqv] [-a align] [-b sz] [-f/t from/to] [-[e|s|S] str] [-x hex] [-R str] [-I str] [-g] -|file|dir ..
```

## Options

_No option definitions could be parsed from this tool's help output. It may be subcommand-driven or have no flags; needs manual review._

## Gotchas

_TODO: operational traps._

## See also

[`strings`](../examine-the-filesystem/strings.md), `grep`, [`xxd`](../examine-the-filesystem/xxd.md), [`bulk_extractor`](../examine-the-filesystem/bulk_extractor.md)
