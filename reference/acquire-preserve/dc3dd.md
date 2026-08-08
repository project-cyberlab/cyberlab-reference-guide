<!-- generated-by: scripts/generate_pages.py -->
# dc3dd

| | |
|---|---|
| **Kit** | Kali Linux · SIFT Workstation |
| **Capability** | Image a disk, volume or device |
| **Version** | dc3dd (dc3dd) 7.2.646 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-08 — [raw help output](../../capture/cyberlab-aio/help/dc3dd.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

dc3dd [OPTION 1] [OPTION 2] ... [OPTION N]

## When you'd reach for this

An analyst reaches for dc3dd when imaging a disk with inline hash verification required, such as during forensic acquisition of a test device or system they own, ensuring the image matches the source through SHA-256 hashing logged in the acquisition file. They may run it after confirming authorization and before handing the image to another analyst, preferring it over similar tools for its detailed logging of hash, byte count, and completion status, which is critical for chain of custody and integrity verification.

**Sources:** <https://github.com/plaintext-security/plaintext-labs/blob/main/forensics/02-acquisition-imaging/lab.md> · <https://www.kali.org/tools/dc3dd/>

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
