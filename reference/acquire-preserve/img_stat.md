<!-- generated-by: scripts/generate_pages.py -->
# img_stat

| | |
|---|---|
| **Kit** | REMnux · Kali Linux · SIFT Workstation |
| **Capability** | Inspect or mount a forensic image container; See the partition and volume layout |
| **Version** | The Sleuth Kit ver 4.11.1 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-08 — [raw help output](../../capture/cyberlab-aio/help/img_stat.help.txt) |
| **Documentation** | <https://www.sleuthkit.org/sleuthkit> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Analyze disk images and recover files from them.

## Synopsis

```
img_stat [-tvV] [-i imgtype] [-b dev_sector_size] image
```

## Options

All 5 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-t` | — | display type only |  |
| `-i` | imgtype | The format of the image file (use '-i list' for list of supported types) |  |
| `-b` | dev_sector_size | The size (in bytes) of the device sectors |  |
| `-v` | — | verbose output to stderr |  |
| `-V` | — | Print version |  |

## Gotchas

_TODO: operational traps._

## See also

[`ewfinfo`](../acquire-preserve/ewfinfo.md), [`ewfmount`](../acquire-preserve/ewfmount.md), [`ewfverify`](../acquire-preserve/ewfverify.md), [`ewfexport`](../acquire-preserve/ewfexport.md), [`affinfo`](../acquire-preserve/affinfo.md), [`affcat`](../acquire-preserve/affcat.md), [`ntfs-3g`](../acquire-preserve/ntfs-3g.md), [`vshadowinfo`](../acquire-preserve/vshadowinfo.md)
