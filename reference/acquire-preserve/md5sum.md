<!-- generated-by: scripts/generate_pages.py -->
# md5sum

| | |
|---|---|
| **Kit** | Base OS — present on every Linux image |
| **Capability** | Verify evidence integrity with hashes |
| **Version** | md5sum (GNU coreutils) 9.1 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-05 — [raw help output](../../capture/cyberlab-aio/help/md5sum.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Compute or verify MD5 checksums. Still everywhere in DFIR for matching files against hash sets, but MD5 is broken for collisions — use it to say two files are the same, never to prove a file is what it claims.

## Synopsis

```
md5sum [OPTION]... [FILE]...
```

## Common invocations

```
# Generate MD5 checksum to verify file integrity
md5sum ravi.pdf
# Verify file integrity using hash
md5sum file1.txt
# Verify files match stored checksums
md5sum -c files.md5
# Verify file integrity by comparing MD5 checksum with expected value
md5sum -b [filename]
# Generate MD5 checksum for file integrity verification
md5sum -t [filename]
# Verify multiple files' integrity with stored hashes
md5sum --check hashes
```

## Options

All 17 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-b` | — | read in binary mode |  |
| `--binary` | — | read in binary mode |  |
| `-c` | — | read checksums from the FILEs and check them |  |
| `--check` | — | read checksums from the FILEs and check them |  |
| `--tag` | — | create a BSD-style checksum |  |
| `-t` | — | read in text mode (default) |  |
| `--text` | — | read in text mode (default) |  |
| `-z` | — | end each output line with NUL, not newline, and disable file name escaping |  |
| `--zero` | — | end each output line with NUL, not newline, and disable file name escaping |  |
| `--ignore-missing` | — | don't fail or report status for missing files |  |
| `--quiet` | — | don't print OK for each successfully verified file |  |
| `--status` | — | don't output anything, status code shows success |  |
| `--strict` | — | exit non-zero for improperly formatted checksum lines |  |
| `-w` | — | warn about improperly formatted checksum lines |  |
| `--warn` | — | warn about improperly formatted checksum lines |  |
| `--help` | — | display this help and exit |  |
| `--version` | — | output version information and exit |  |

## Gotchas

_TODO: operational traps._

## See also

[`rahash2`](../acquire-preserve/rahash2.md), [`ssdeep`](../acquire-preserve/ssdeep.md), [`sha256sum`](../acquire-preserve/sha256sum.md), [`sigtool`](../acquire-preserve/sigtool.md)
