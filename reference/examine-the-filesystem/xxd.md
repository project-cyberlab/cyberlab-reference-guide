<!-- generated-by: scripts/generate_pages.py -->
# xxd

| | |
|---|---|
| **Kit** | Base OS — present on every Linux image |
| **Capability** | Search raw data for a pattern; Decode, decrypt or transform encoded data; Inspect files by hand |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-10 — [raw help output](../../capture/cyberlab-aio/help/xxd.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Produce a hex dump, or reverse one back into binary with `-r`. The reverse direction is what distinguishes it from a viewer: edit the hex, convert it back, and you have carved or patched a file without a hex editor.

## Synopsis

```
xxd [options] [infile [outfile]]
or
xxd -r [-s [-]offset] [-c cols] [-ps] [infile [outfile]]
```

## Common invocations

```
# Recover original data from hex dump by reversing it
xxd -r
# Recover original data from hexdump
xxd -r -i
# Inspect binary files with hex dump
xxd file.bin
```

## Options

All 16 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-a` | — | toggle autoskip: A single '*' replaces nul-lines. Default off. |  |
| `-b` | — | binary digit dump (incompatible with -ps,-i,-r). Default hex. |  |
| `-C` | — | capitalize variable names in C include file style (-i). |  |
| `-c` | cols | format <cols> octets per line. Default 16 (-i: 12, -ps: 30). |  |
| `-E` | — | show characters in EBCDIC. Default ASCII. |  |
| `-e` | — | little-endian dump (incompatible with -ps,-i,-r). |  |
| `-g` | bytes | number of octets per group in normal output. Default 2 (-e: 4). |  |
| `-h` | — | print this summary. |  |
| `-i` | — | output in C include file style. |  |
| `-l` | len | stop after <len> octets. |  |
| `-n` | name | set the variable name used in C include output (-i). |  |
| `-o` | off | add <off> to the displayed file position. |  |
| `-r` | — | reverse operation: convert (or patch) hexdump into binary. |  |
| `-d` | — | show offset in decimal instead of hex. |  |
| `-u` | — | use upper case hex letters. |  |
| `-v` | — | show version: "xxd 2022-01-14 by Juergen Weigert et al.". |  |

## Gotchas

_TODO: operational traps._

## See also

[`rafind2`](../examine-the-filesystem/rafind2.md), [`strings`](../examine-the-filesystem/strings.md), `grep`, [`bulk_extractor`](../examine-the-filesystem/bulk_extractor.md), [`cyberchef`](../decode-deobfuscate/cyberchef.md), [`base64dump.py`](../malware-triage-static/base64dump.py.md), [`rax2`](../decode-deobfuscate/rax2.md), [`openssl`](../decode-deobfuscate/openssl.md)
