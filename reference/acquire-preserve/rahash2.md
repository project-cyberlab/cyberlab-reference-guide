<!-- generated-by: scripts/generate_pages.py -->
# rahash2

| | |
|---|---|
| **Kit** | REMnux |
| **Capability** | Verify evidence integrity with hashes |
| **Version** | rahash2 6.1.9 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-10 — [raw help output](../../capture/cyberlab-aio/help/rahash2.help.txt) |
| **Documentation** | <https://www.radare.org/n/radare2.html> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Examine binary files, including disassembling and debugging. Includes r2ai and decai plugins for LLM-powered analysis (API key or local Ollama required), plus the r2ghidra plugin for Ghidra decompilation via the pdg command.

## When you'd reach for this

An analyst reaches for rahash2 when they need to compute hash values for files or text strings, often using the -s option for strings or -a all to apply multiple algorithms simultaneously; they may run it after acquiring evidence to verify integrity or before submitting files for analysis, preferring it over similar tools for its ability to handle multiple algorithms in one command and its integration with radare for further forensic processing.

**Sources:** <https://book.rada.re/tools/rahash2/rahash_tool.html>

## Synopsis

```
rahash2 [-BehjkLqRrvX] [-b S] [-a A] [-c H] [-E A] [-s S] [-f O] [-t O] [file] ...
```

## Common invocations

```
# Verify file integrity by comparing CRC32 hash to expected value
rahash2 -qqa crc32 /bin/ls 63212007
# Encrypt string with rotation cipher and show output
rahash2 -S 12333 -E ror -s hello
# Compute and verify file hashes for integrity checks
rahash2 -L
# List loaded cryptographic plugins
rahash2 -L | grep ^c
# Calculate multiple hash values for a file
rahash2 -a all /bin/ls
```

## Options

All 23 options parsed from the captured help text; 3 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-a` | algo | comma separated list of algorithms (default is 'sha256') | An analyst would use the -a flag with the value 'all' when they need to compute multiple hash values for a file or string using all available algorithms known to rahash2. |
| `-b` | bsize | specify the size of the block (instead of full file) |  |
| `-B` | — | show per-block hash |  |
| `-c` | hash | compare with this hash | An analyst would use the -c flag when verifying if a file's computed hash matches a known hash to confirm its integrity or detect modifications. |
| `-e` | — | swap endian (use little endian) |  |
| `-E` | algo | encrypt. Use -S to set key and -I to set IV |  |
| `-D` | algo | decrypt. Use -S to set key and -I to set IV |  |
| `-f` | from | start hashing at given address |  |
| `-i` | num | repeat hash N iterations (f.ex: 3DES) |  |
| `-I` | iv | use give initialization vector (IV) (hexa or s:string) |  |
| `-j` | — | output in json |  |
| `-J` | — | new simplified json output (same as -jj) |  |
| `-S` | seed | use given seed (hexa or s:string) use ^ to prefix (key for -E) (- will slurp the key from stdin, the @ prefix points to a file | An analyst would use the -S flag when encrypting or decrypting data with a specific key or seed value, such as during symmetric encryption operations with plugins like AES-ECB or Blowfish. |
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
