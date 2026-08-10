<!-- generated-by: scripts/generate_pages.py -->
# testdisk

| | |
|---|---|
| **Kit** | SIFT Workstation |
| **Capability** | See the partition and volume layout; Recover deleted or lost files |
| **Version** | TestDisk 7.1 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-10 — [raw help output](../../capture/cyberlab-aio/help/testdisk.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Christophe GRENIER <grenier@cgsecurity.org>

## When you'd reach for this

An analyst reaches for TestDisk when recovering lost partitions or repairing filesystems on physical devices, running it with administrative or root privileges after ensuring access rights; they choose it over similar tools because it specifically handles partition recovery and filesystem repair, unlike PhotoRec, which focuses on file recovery from unallocated space.

**Sources:** <https://www.cgsecurity.org/wiki/PhotoRec> · <https://www.cgsecurity.org/wiki/TestDisk_Step_By_Step>

## Synopsis

```
testdisk [/log] [/debug] [file.dd|file.e01|device]
testdisk /list  [/log]   [file.dd|file.e01|device]
testdisk /version
```

## Common invocations

```
# Recover partitions and repair filesystems from disk images
testdisk image.dd to work on a raw disk image
```

## Options

All 3 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `/log` | — | create a testdisk.log file |  |
| `/debug` | — | add debug information |  |
| `/list` | — | display current partitions |  |

## Gotchas

_TODO: operational traps._

## See also

[`mmls`](../examine-the-filesystem/mmls.md), [`fsstat`](../examine-the-filesystem/fsstat.md), [`img_stat`](../acquire-preserve/img_stat.md), [`tsk_recover`](../examine-the-filesystem/tsk_recover.md), [`icat`](../examine-the-filesystem/icat.md), [`photorec`](../examine-the-filesystem/photorec.md), [`blkls`](../examine-the-filesystem/blkls.md)
