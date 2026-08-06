<!-- generated-by: scripts/generate_pages.py -->
# blkls

| | |
|---|---|
| **Kit** | REMnux · Kali Linux · SIFT Workstation |
| **Capability** | Recover deleted or lost files |
| **Version** | The Sleuth Kit ver 4.11.1 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-06 — [raw help output](../../capture/cyberlab-aio/help/blkls.help.txt) |
| **Documentation** | <https://www.sleuthkit.org/sleuthkit> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Extract filesystem blocks — by default the unallocated ones, which is the input a carver wants.

## Synopsis

```
blkls [-aAelvV] [-f fstype] [-i imgtype] [-b dev_sector_size] [-o imgoffset] [-P pooltype] [-B pool_volume_block] image [images] [start-stop]
```

## Options

All 13 options parsed from the captured help text; 12 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-e` | — | every block (including file system metadata blocks) | Every block, including filesystem metadata. |
| `-l` | — | print details in time machine list format | List block details rather than emitting their contents. |
| `-a` | — | Display allocated blocks | Allocated blocks only — the inverse, when isolating live data. |
| `-A` | — | Display unallocated blocks | Unallocated blocks. The default and the usual intent: pipe this into `foremost` or `scalpel` so the carver reads only free space instead of the whole image. |
| `-f` | fstype | File system type (use '-f list' for supported types) | Force the filesystem type (`-f list` shows the options). |
| `-i` | imgtype | The format of the image file (use '-i list' for supported types) | Image format for non-raw evidence such as E01 or AFF. |
| `-b` | dev_sector_size | The size (in bytes) of the device sectors | Device sector size; required on 4Kn drives. |
| `-o` | imgoffset | The offset of the file system in the image (in sectors) | Offset, in sectors, from `mmls`. |
| `-P` | pooltype | Pool container type (use '-P list' for supported types) | Pool type, for APFS or LVM containers. |
| `-B` | pool_volume_block | Starting block (for pool volumes only) | Starting block within a pool volume. |
| `-s` | — | print slack space only (other flags are ignored | Slack space only: the tail of the last block of each file, where fragments of previous contents survive. A distinct hunt from carving free space, and it ignores the other flags. |
| `-v` | — | verbose to stderr | Verbose diagnostics to stderr. |
| `-V` | — | print version |  |

## Gotchas

- Output goes to stdout and is the size of the free space — redirect it to a file on a volume that can hold it, not into a pager.
- Block offsets in the extracted stream do **not** match offsets in the original image, because only unallocated blocks were written. Use `-l` if you need to map a hit back to its real location.

## See also

[`tsk_recover`](../examine-the-filesystem/tsk_recover.md), [`icat`](../examine-the-filesystem/icat.md), [`photorec`](../examine-the-filesystem/photorec.md), [`testdisk`](../examine-the-filesystem/testdisk.md)
