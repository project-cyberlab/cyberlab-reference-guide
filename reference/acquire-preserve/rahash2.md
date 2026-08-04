<!-- generated-by: scripts/generate_pages.py -->
# rahash2

| | |
|---|---|
| **Kit** | REMnux |
| **Capability** | Verify evidence integrity with hashes |
| **Version** | rahash2 6.1.9 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-04 — [raw help output](../../capture/cyberlab-aio/help/rahash2.help.txt) |
| **Documentation** | <https://www.radare.org/n/radare2.html> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Examine binary files, including disassembling and debugging. Includes r2ai and decai plugins for LLM-powered analysis (API key or local Ollama required), plus the r2ghidra plugin for Ghidra decompilation via the pdg command.

## When you'd reach for this

An analyst reaches for rahash2 when examining filesystems to identify modified sections of large files, as it hashes each block individually, allowing comparison against known hashes to pinpoint changes. They may run it after obtaining a file from disk imaging or before performing deeper analysis to verify data integrity. They choose it over other hash tools because its block-based approach enables targeted modification detection without processing the entire file at once.

**Sources:** <https://gist.github.com/52617365/95baed8b731c3effdad04b1d6ccf4831> · <https://www.sentinelone.com/labs/automating-string-decryption-and-other-reverse-engineering-tasks-in-radare2-with-r2pipe/>

## Synopsis

```
rahash2 [-BehjkLqRrvX] [-b S] [-a A] [-c H] [-E A] [-s S] [-f O] [-t O] [file] ...
```

## Options

All 23 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-a` | algo | comma separated list of algorithms (default is 'sha256') |  |
| `-b` | bsize | specify the size of the block (instead of full file) |  |
| `-B` | — | show per-block hash |  |
| `-c` | hash | compare with this hash |  |
| `-e` | — | swap endian (use little endian) |  |
| `-E` | algo | encrypt. Use -S to set key and -I to set IV |  |
| `-D` | algo | decrypt. Use -S to set key and -I to set IV |  |
| `-f` | from | start hashing at given address |  |
| `-i` | num | repeat hash N iterations (f.ex: 3DES) |  |
| `-I` | iv | use give initialization vector (IV) (hexa or s:string) |  |
| `-j` | — | output in json |  |
| `-J` | — | new simplified json output (same as -jj) |  |
| `-S` | seed | use given seed (hexa or s:string) use ^ to prefix (key for -E) (- will slurp the key from stdin, the @ prefix points to a file |  |
| `-k` | — | show hash using the openssh's randomkey algorithm |  |
| `-q` | — | run in quiet mode (-qq to show only the hash) |  |
| `-L` | — | list muta plugins (combines with -q, used by -a, -E and -D) |  |
| `-r` | — | output radare commands |  |
| `-R` | — | output radare2 sdb commands (k file.<algo>=...) |  |
| `-s` | string | hash this string instead of files |  |
| `-t` | — | stop hashing at given address |  |
| `-x` | hexstr | hash this hexpair string instead of files |  |
| `-X` | — | output in hexpairs instead of binary/plain |  |
| `-v` | — | show version information |  |

## Gotchas

_TODO: operational traps._

## See also

[`ssdeep`](../acquire-preserve/ssdeep.md), [`sha256sum`](../acquire-preserve/sha256sum.md), [`md5sum`](../acquire-preserve/md5sum.md), [`sigtool`](../acquire-preserve/sigtool.md)
