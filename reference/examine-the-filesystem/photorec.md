<!-- generated-by: scripts/generate_pages.py -->
# photorec

| | |
|---|---|
| **Kit** | SIFT Workstation |
| **Capability** | Recover deleted or lost files |
| **Version** | PhotoRec 7.1 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-11 — [raw help output](../../capture/cyberlab-aio/help/photorec.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Christophe GRENIER <grenier@cgsecurity.org>

## When you'd reach for this

An analyst reaches for PhotoRec when recovering deleted files from damaged or unbootable disks, disk images, or encrypted partitions, often after using TestDisk to repair partition tables; they run it with parameters like `/log` for logging or specifying raw devices for speed, preferring it over similar tools for its robust support of fragmented file recovery and diverse image formats like .dd, .E01, and split files.

**Sources:** <https://docslib.org/doc/9154809/photorec-step-by-step> · <https://oneuptime.com/blog/post/2026-01-15-recover-deleted-files-testdisk-ubuntu/view> · <https://www.cgsecurity.org/wiki/PhotoRec_Step_By_Step>

## Synopsis

```
photorec [/log] [/debug] [/d recup_dir] [file.dd|file.e01|device]
photorec /version
```

## Common invocations

```
# Recover files from raw disk image
photorec image.dd to carve a raw disk image
```

## Options

All 2 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `/log` | — | create a photorec.log file |  |
| `/debug` | — | add debug information |  |

## Gotchas

_TODO: operational traps._

## See also

[`tsk_recover`](../examine-the-filesystem/tsk_recover.md), [`icat`](../examine-the-filesystem/icat.md), [`testdisk`](../examine-the-filesystem/testdisk.md), [`blkls`](../examine-the-filesystem/blkls.md)
