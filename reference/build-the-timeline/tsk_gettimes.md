<!-- generated-by: scripts/generate_pages.py -->
# tsk_gettimes

| | |
|---|---|
| **Kit** | REMnux · Kali Linux · SIFT Workstation |
| **Capability** | Build a filesystem MAC-time timeline |
| **Version** | The Sleuth Kit ver 4.11.1 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-10 — [raw help output](../../capture/cyberlab-aio/help/tsk_gettimes.help.txt) |
| **Documentation** | <https://www.sleuthkit.org/sleuthkit> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Analyze disk images and recover files from them.

## Synopsis

```
tsk_gettimes [-vVm] [-i imgtype] [-b dev_sector_size] [-z zone] [-s seconds] image [image]
```

## Common invocations

```
# Extract file timestamps from disk image
tsk_gettimes ./image.dd > body.txt
```

## Options

All 7 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-i` | imgtype | The format of the image file (use '-i list' for supported types) |  |
| `-b` | dev_sector_size | The size (in bytes) of the device sectors |  |
| `-m` | — | Calculate MD5 hash in output (slow) |  |
| `-v` | — | verbose output to stderr |  |
| `-V` | — | Print version |  |
| `-z` | — | Time zone of original machine (i.e. EST5EDT or GMT) (only useful with -l) |  |
| `-s` | seconds | Time skew of original machine (in seconds) (only useful with -l & -m) |  |

## Gotchas

_TODO: operational traps._

## See also

[`fls`](../examine-the-filesystem/fls.md), [`mactime`](../build-the-timeline/mactime.md)
