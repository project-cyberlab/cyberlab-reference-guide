<!-- generated-by: scripts/generate_pages.py -->
# dd

| | |
|---|---|
| **Kit** | Base OS — present on every Linux image |
| **Capability** | Image a disk, volume or device |
| **Version** | dd (coreutils) 9.1 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-03 — [raw help output](../../capture/cyberlab-aio/help/dd.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Copy data block by block, without interpreting it. In forensics this is the plain-raw imaging tool: it will read a whole device including unallocated space, but it has no hashing, no error recovery and no metadata. Prefer [`dc3dd`](dc3dd.md), [`dcfldd`](dcfldd.md) or [`ewfacquire`](ewfacquire.md) for evidence; reach for `dd` when you need a byte range and nothing else.

## Synopsis

```
dd [OPERAND]...
or:  dd OPTION
```

## Options

All 2 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `--help` | — | display this help and exit |  |
| `--version` | — | output version information and exit |  |

## Gotchas

_TODO: operational traps._

## See also

[`dc3dd`](../acquire-preserve/dc3dd.md), [`dcfldd`](../acquire-preserve/dcfldd.md), [`ewfacquire`](../acquire-preserve/ewfacquire.md), [`affconvert`](../acquire-preserve/affconvert.md)
