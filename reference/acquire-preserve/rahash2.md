<!-- generated-by: scripts/generate_pages.py -->
# rahash2

**Kit:** REMnux  **Capability:** Verify evidence integrity with hashes  **Version:** rahash2 6.1.9
**Captured:** `cyberlab-aio` via `--help` on 2026-08-02  [raw](../../capture/cyberlab-aio/help/rahash2.help.txt)  **Docs:** <https://www.radare.org/n/radare2.html>

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Examine binary files, including disassembling and debugging. Includes r2ai and decai plugins for LLM-powered analysis (API key or local Ollama required), plus the r2ghidra plugin for Ghidra decompilation via the pdg command.

## Synopsis

```
rahash2 [-BehjkLqRrvX] [-b S] [-a A] [-c H] [-E A] [-s S] [-f O] [-t O] [file] ...
```

## Common invocations

_TODO: up to 8 task-titled invocations._

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
| `-t` | to | stop hashing at given address |  |
| `-x` | hexstr | hash this hexpair string instead of files |  |
| `-X` | — | output in hexpairs instead of binary/plain |  |
| `-v` | — | show version information |  |

## Gotchas

_TODO: operational traps._

## See also

[`ssdeep`](../acquire-preserve/ssdeep.md), [`sha256sum`](../acquire-preserve/sha256sum.md), [`md5sum`](../acquire-preserve/md5sum.md), [`sigtool`](../acquire-preserve/sigtool.md)
