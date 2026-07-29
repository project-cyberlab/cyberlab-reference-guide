<!-- generated-by: scripts/generate_pages.py -->
# blkls

**Kit:** REMnux · Kali Linux · SIFT Workstation  **Capability:** Recover deleted or lost files  **Version:** The Sleuth Kit ver 4.11.1
**Captured:** `cyberlab-aio` via `--help` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/blkls.help.txt)  **Docs:** <https://www.sleuthkit.org/sleuthkit>

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Analyze disk images and recover files from them.

## Synopsis

```
blkls [-aAelvV] [-f fstype] [-i imgtype] [-b dev_sector_size] [-o imgoffset] [-P pooltype] [-B pool_volume_block] image [images] [start-stop]
```

## Common invocations

_TODO: up to 8 task-titled invocations._

## Options

All 13 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-e` | — | every block (including file system metadata blocks) |  |
| `-l` | — | print details in time machine list format |  |
| `-a` | — | Display allocated blocks |  |
| `-A` | — | Display unallocated blocks |  |
| `-f` | fstype | File system type (use '-f list' for supported types) |  |
| `-i` | imgtype | The format of the image file (use '-i list' for supported types) |  |
| `-b` | dev_sector_size | The size (in bytes) of the device sectors |  |
| `-o` | imgoffset | The offset of the file system in the image (in sectors) |  |
| `-P` | pooltype | Pool container type (use '-P list' for supported types) |  |
| `-B` | pool_volume_block | Starting block (for pool volumes only) |  |
| `-s` | — | print slack space only (other flags are ignored |  |
| `-v` | — | verbose to stderr |  |
| `-V` | — | print version |  |

## Gotchas

_TODO: operational traps._

## See also

[`tsk_recover`](../examine-the-filesystem/tsk_recover.md), [`icat`](../examine-the-filesystem/icat.md), [`photorec`](../examine-the-filesystem/photorec.md), [`testdisk`](../examine-the-filesystem/testdisk.md)
