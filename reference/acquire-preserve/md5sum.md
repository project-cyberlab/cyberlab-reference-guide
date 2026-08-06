<!-- generated-by: scripts/generate_pages.py -->
# md5sum

| | |
|---|---|
| **Kit** | Base OS — present on every Linux image |
| **Capability** | Verify evidence integrity with hashes |
| **Version** | md5sum (GNU coreutils) 9.1 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-06 — [raw help output](../../capture/cyberlab-aio/help/md5sum.help.txt) |

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

All 17 options parsed from the captured help text; 5 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-b` | — | read in binary mode |  |
| `--binary` | — | read in binary mode |  |
| `-c` | — | read checksums from the FILEs and check them | An analyst would use the --check flag when verifying if files have changed by comparing their current state to stored hash values, such as after modifying a file or during automated integrity checks. |
| `--check` | — | read checksums from the FILEs and check them | An analyst would use the --check flag when verifying if files have changed by comparing their current state to stored hash values, such as after modifying a file or during automated integrity checks. |
| `--tag` | — | create a BSD-style checksum | An analyst would use the --tag flag when they need to display the MD5 hash in BSD-style format, as demonstrated in the examples where it formats the output as "MD5 (filename) = hashvalue". |
| `-t` | — | read in text mode (default) |  |
| `--text` | — | read in text mode (default) |  |
| `-z` | — | end each output line with NUL, not newline, and disable file name escaping |  |
| `--zero` | — | end each output line with NUL, not newline, and disable file name escaping |  |
| `--ignore-missing` | — | don't fail or report status for missing files | An analyst would use the --ignore-missing flag when verifying checksums of files that may be intentionally absent, to avoid warnings about missing files and focus on verification failures. |
| `--quiet` | — | don't print OK for each successfully verified file | An analyst would use the --quiet flag when checking multiple files to display only the modified files, filtering out unchanged ones during verification. |
| `--status` | — | don't output anything, status code shows success | An analyst would use the --status flag when running md5sum in a script to check file integrity and need the command to return a status code (0 for no changes, 1 for mismatches) without producing any output. |
| `--strict` | — | exit non-zero for improperly formatted checksum lines |  |
| `-w` | — | warn about improperly formatted checksum lines |  |
| `--warn` | — | warn about improperly formatted checksum lines |  |
| `--help` | — | display this help and exit |  |
| `--version` | — | output version information and exit |  |

## Gotchas

_TODO: operational traps._

## See also

[`rahash2`](../acquire-preserve/rahash2.md), [`ssdeep`](../acquire-preserve/ssdeep.md), [`sha256sum`](../acquire-preserve/sha256sum.md), [`sigtool`](../acquire-preserve/sigtool.md)
