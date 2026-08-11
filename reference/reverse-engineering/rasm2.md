<!-- generated-by: scripts/generate_pages.py -->
# rasm2

| | |
|---|---|
| **Kit** | REMnux |
| **Capability** | Disassemble and explore a binary; Analyse shellcode |
| **Version** | rasm2 6.1.9 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-11 — [raw help output](../../capture/cyberlab-aio/help/rasm2.help.txt) |
| **Documentation** | <https://www.radare.org/n/radare2.html> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Examine binary files, including disassembling and debugging. Includes r2ai and decai plugins for LLM-powered analysis (API key or local Ollama required), plus the r2ghidra plugin for Ghidra decompilation via the pdg command.

## When you'd reach for this

An analyst reaches for rasm2 when they need to disassemble binary or hex data into human-readable assembly instructions, such as converting a hex value like '90' to 'nop' or analyzing bytecode. They may use it after obtaining a binary file or hex dump, often in conjunction with radare2 commands like `pd` or `pD` for deeper analysis. They choose it for its direct integration with radare2 and ability to handle both hexpair and binary inputs efficiently.

**Sources:** <https://book.rada.re/tools/rasm2/disassemble.html>

## Synopsis

```
rasm2 [-ACdDehHLBvw] [-a arch] [-b bits] [-s addr] [-S syntax]
[-f file] [-o file] [-F fil:ter] [-i skip] [-l len] 'code'|hex|0101b|-
```

## Common invocations

```
# Assemble x86 instruction into machine code bytes
rasm2 -a x86 -b 32 'mov eax, 33'
# Disassemble hex bytes into assembly instructions
rasm2 -d 90
# List available architecture plugins for disassembly
rasm2 -L
# Convert between assembly instructions and hex representations
rasm2 -a java 'nop'
# Disassemble hex bytes into assembly instructions
rasm2 -a x86 -b 32 -d '90'
```

## Options

All 25 options parsed from the captured help text; 5 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-a` | arch | set architecture to assemble/disassemble (see -L) | An analyst would use the -a flag when disassembling code for a specific architecture, such as x86 or Java, to ensure the correct instruction set is used. |
| `-A` | — | show Analysis information from given hexpairs |  |
| `-b` | bits | set cpu register size (8, 16, 32, 64) (RASM2_BITS) | An analyst would use the `-b` flag when specifying the bitness of the target architecture (e.g., 32 or 64) during disassembly to ensure accurate interpretation of machine code instructions. |
| `-B` | — | binary input/output (-l is mandatory for binary input) |  |
| `-c` | cpu | select specific CPU (depends on arch) |  |
| `-C` | — | output in C format |  |
| `-d` | — | disassemble from hexpair bytes (-D show hexpairs) | An analyst would use the `-d` flag when converting hexadecimal opcodes into human-readable assembly instructions to analyze binary data. |
| `-D` | — | disassemble from hexpair bytes (-D show hexpairs) | An analyst would use the `-D` flag when needing to disassemble hexpair bytes while also viewing the corresponding offset and opcode bytes for detailed analysis. |
| `-e` | — | use big endian instead of little endian |  |
| `-E` | — | display ESIL expression (same input as in -d) |  |
| `-f` | file | read data from file |  |
| `-F` | parser | specify which parse filter use (see -LL) |  |
| `-i` | len | ignore/skip N bytes of the input buffer | An analyst would use the -i flag when they need to skip a specific number of bytes in the input buffer to bypass irrelevant data, such as file headers or padding, while disassembling a binary file. |
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
