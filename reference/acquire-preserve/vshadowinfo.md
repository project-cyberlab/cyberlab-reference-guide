<!-- generated-by: scripts/generate_pages.py -->
# vshadowinfo

| | |
|---|---|
| **Kit** | SIFT Workstation (libyal) |
| **Capability** | Inspect or mount a forensic image container |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-05 — [raw help output](../../capture/cyberlab-aio/help/vshadowinfo.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Use vshadowinfo to determine information about a Windows NT Volume Shadow

## Synopsis

```
vshadowinfo [ -o offset ] [ -ahvV ] source
```

## Options

All 5 options parsed from the captured help text; 2 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-a` | — | shows allocation information | An analyst would use the -a flag when examining allocation information related to a Volume Shadow Snapshot (VSS) volume. |
| `-h` | — | shows this help |  |
| `-o` | — | specify the volume offset in bytes | An analyst would use the -o flag when needing to specify a non-default volume offset in bytes to access a particular section of a VSS volume that isn't starting at the beginning of the source file or device. |
| `-v` | — | verbose output to stderr |  |
| `-V` | — | print version |  |

## Gotchas

_TODO: operational traps._

## See also

[`ewfinfo`](../acquire-preserve/ewfinfo.md), [`ewfmount`](../acquire-preserve/ewfmount.md), [`ewfverify`](../acquire-preserve/ewfverify.md), [`ewfexport`](../acquire-preserve/ewfexport.md), [`affinfo`](../acquire-preserve/affinfo.md), [`affcat`](../acquire-preserve/affcat.md), [`img_stat`](../acquire-preserve/img_stat.md), [`ntfs-3g`](../acquire-preserve/ntfs-3g.md)
