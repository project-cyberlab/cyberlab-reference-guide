<!-- generated-by: scripts/generate_pages.py -->
# aeskeyfind

| | |
|---|---|
| **Kit** | REMnux · Kali Linux · SIFT Workstation |
| **Capability** | Recover encryption keys from memory |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-04 — [raw help output](../../capture/cyberlab-aio/help/aeskeyfind.help.txt) |
| **Documentation** | <https://citp.princeton.edu/our-work/memory/> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Find 128-bit and 256-bit AES keys in a memory image.

## When you'd reach for this

An analyst reaches for aeskeyfind when examining memory dumps or virtual machine snapshots to recover AES-128 keys, especially in cases where memory decay or corrupted key schedules may be present; they may pre-process dumps to filter irrelevant data and post-process results by validating discovered keys against known encryption usage, preferring it over similar tools due to its ability to handle reversed key schedules, InvMixColumn pre-applied entries, and entropy-based filtering of non-key blocks.

**Sources:** <https://github.com/SalpSec/aeskeyfind> · <https://github.com/makomk/aeskeyfind> · <https://github.com/project-cyberlab/cyberlab-reference-guide/blob/main/reference/memory-forensics/aeskeyfind.md>

## Synopsis

```
aeskeyfind [OPTION]... MEMORY-IMAGE
```

## Options

All 3 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-v` | — | verbose output -- prints the extended keys and the constraints on the rows of the key schedule |  |
| `-q` | — | don't display a progress bar |  |
| `-h` | — | displays this help message |  |

## Gotchas

_TODO: operational traps._

## See also

[`rsakeyfind`](../memory-forensics/rsakeyfind.md), [`bulk_extractor`](../examine-the-filesystem/bulk_extractor.md)
