<!-- generated-by: scripts/generate_pages.py -->
# sha256sum

| | |
|---|---|
| **Kit** | Base OS — present on every Linux image |
| **Capability** | Verify evidence integrity with hashes |
| **Version** | sha256sum (GNU coreutils) 9.1 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-03 — [raw help output](../../capture/cyberlab-aio/help/sha256sum.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Print or check SHA256 (256-bit) checksums.

## Synopsis

```
sha256sum [OPTION]... [FILE]...
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

[`rahash2`](../acquire-preserve/rahash2.md), [`ssdeep`](../acquire-preserve/ssdeep.md), [`md5sum`](../acquire-preserve/md5sum.md), [`sigtool`](../acquire-preserve/sigtool.md)
