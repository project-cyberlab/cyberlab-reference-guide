<!-- generated-by: scripts/generate_pages.py -->
# dc3dd

| | |
|---|---|
| **Kit** | Kali Linux · SIFT Workstation |
| **Capability** | Image a disk, volume or device |
| **Version** | dc3dd (dc3dd) 7.2.646 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-07 — [raw help output](../../capture/cyberlab-aio/help/dc3dd.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

dc3dd [OPTION 1] [OPTION 2] ... [OPTION N]

## When you'd reach for this

An analyst reaches for dc3dd when encountering unreadable sectors during disk imaging, using cnt=, iskip=, and oskip= parameters before running it to handle errors, and prefers it for its robust error recovery features and ability to report progress upon interruption.

**Sources:** <https://www.kali.org/tools/dc3dd/>

## Synopsis

```
------
```

## Common invocations

```
# Verify data integrity during forensic imaging
dc3dd if=/var/log/messages of=/tmp/dc3dd hash=sha512
```

## Options

All 3 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `--help` | — | display this help and exit |  |
| `--version` | — | output version information and exit |  |
| `--flags` | — | display compile-time flags and exit |  |

## Gotchas

_TODO: operational traps._

## See also

[`dcfldd`](../acquire-preserve/dcfldd.md), [`dd`](../acquire-preserve/dd.md), [`ewfacquire`](../acquire-preserve/ewfacquire.md), [`affconvert`](../acquire-preserve/affconvert.md)
