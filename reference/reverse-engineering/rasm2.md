<!-- generated-by: scripts/generate_pages.py -->
# rasm2

| | |
|---|---|
| **Kit** | REMnux |
| **Capability** | Disassemble and explore a binary; Analyse shellcode |
| **Version** | rasm2 6.1.9 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-05 — [raw help output](../../capture/cyberlab-aio/help/rasm2.help.txt) |
| **Documentation** | <https://www.radare.org/n/radare2.html> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Examine binary files, including disassembling and debugging. Includes r2ai and decai plugins for LLM-powered analysis (API key or local Ollama required), plus the r2ghidra plugin for Ghidra decompilation via the pdg command.

## Synopsis

```
rasm2 [-ACdDehHLBvw] [-a arch] [-b bits] [-s addr] [-S syntax]
[-f file] [-o file] [-F fil:ter] [-i skip] [-l len] 'code'|hex|0101b|-
```

## Options

All 25 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-a` | arch | set architecture to assemble/disassemble (see -L) |  |
| `-A` | — | show Analysis information from given hexpairs |  |
| `-b` | bits | set cpu register size (8, 16, 32, 64) (RASM2_BITS) |  |
| `-B` | — | binary input/output (-l is mandatory for binary input) |  |
| `-c` | cpu | select specific CPU (depends on arch) |  |
| `-C` | — | output in C format |  |
| `-d` | — | disassemble from hexpair bytes (-D show hexpairs) |  |
| `-D` | — | disassemble from hexpair bytes (-D show hexpairs) |  |
| `-e` | — | use big endian instead of little endian |  |
| `-E` | — | display ESIL expression (same input as in -d) |  |
| `-f` | file | read data from file |  |
| `-F` | parser | specify which parse filter use (see -LL) |  |
| `-i` | len | ignore/skip N bytes of the input buffer |  |
| `-j` | — | output in json format |  |
| `-k` | kernel | select operating system (linux, windows, darwin, android, ios, ..) |  |
| `-l` | len | input/Output length |  |
| `-N` | — | same as r2 -N (or R2_NOPLUGINS) (not load any plugin) |  |
| `-o` | file | output file name (rasm2 -Bf a.asm -o a) |  |
| `-p` | — | run SPP over input for assembly |  |
| `-q` | — | quiet mode |  |
| `-r` | — | output in radare commands |  |
| `-S` | syntax | select syntax (intel, att) |  |
| `-v` | — | show version information |  |
| `-x` | — | use hex dwords instead of hex pairs when assembling. |  |
| `-w` | — | what's this instruction for? describe opcode |  |

## Gotchas

_TODO: operational traps._

## See also

[`r2`](../reverse-engineering/r2.md), [`rabin2`](../malware-triage-static/rabin2.md), [`objdump`](../malware-triage-static/objdump.md), [`vivbin`](../reverse-engineering/vivbin.md), [`vdbbin`](../reverse-engineering/vdbbin.md), [`xortool`](../reverse-engineering/xortool.md)
