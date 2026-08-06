<!-- generated-by: scripts/generate_pages.py -->
# rafind2

| | |
|---|---|
| **Kit** | REMnux · Kali Linux · SIFT Workstation |
| **Capability** | Search raw data for a pattern |
| **Version** | rafind2 6.1.9 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-06 — [raw help output](../../capture/cyberlab-aio/help/rafind2.help.txt) |
| **Documentation** | <https://www.radare.org/n/radare2.html> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Examine binary files, including disassembling and debugging. Includes r2ai and decai plugins for LLM-powered analysis (API key or local Ollama required), plus the r2ghidra plugin for Ghidra decompilation via the pdg command.

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
