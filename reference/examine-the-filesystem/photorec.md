<!-- generated-by: scripts/generate_pages.py -->
# photorec

| | |
|---|---|
| **Kit** | SIFT Workstation |
| **Capability** | Recover deleted or lost files |
| **Version** | PhotoRec 7.1 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-08 — [raw help output](../../capture/cyberlab-aio/help/photorec.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Christophe GRENIER <grenier@cgsecurity.org>

## When you'd reach for this

An analyst reaches for PhotoRec when recovering files from disk images, Encase EWF images, or physical devices like hard disks and USB keys, after ensuring proper permissions and device selection; they may run it following the creation of a disk image or after selecting the target partition, preferring it over similar tools for its support of encrypted file systems, RAID, and direct carving from unallocated space without relying on file system metadata.

**Sources:** <https://www.cgsecurity.org/wiki/PhotoRec_Step_By_Step>

## Synopsis

```
photorec [/log] [/debug] [/d recup_dir] [file.dd|file.e01|device]
photorec /version
```

## Common invocations

```
# Recover files from raw disk image
photorec image.dd to carve a raw disk image
# Recover files from Encase EWF image
photorec image.E01 to recover files from an Encase EWF image
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
