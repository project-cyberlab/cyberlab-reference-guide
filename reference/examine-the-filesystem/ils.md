<!-- generated-by: scripts/generate_pages.py -->
# ils

**Kit:** REMnux · Kali Linux · SIFT Workstation  **Capability:** List files and directories, including deleted ones; Inspect metadata for one file or inode  **Version:** The Sleuth Kit ver 4.11.1
**Captured:** `cyberlab-aio` via `--help` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/ils.help.txt)  **Docs:** <https://www.sleuthkit.org/sleuthkit>

## Purpose

Analyze disk images and recover files from them.

## Synopsis

```
ils [-emOpvV] [-aAlLzZ] [-f fstype] [-i imgtype] [-b dev_sector_size] [-o imgoffset] [-P pooltype] [-B pool_volume_block] [-s seconds] image [images] [inum[-end]]
```

## Common invocations

_TODO: up to 8 task-titled invocations._

## Options

All 19 options parsed from the captured help text. The final column is the judgement layer and is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-e` | — | Display all inodes | |
| `-m` | — | Display output in the mactime format | |
| `-O` | — | Display inodes that are unallocated, but were sill open (UFS/ExtX only) | |
| `-p` | — | Display orphan inodes (unallocated with no file name) | |
| `-s` | seconds | Time skew of original machine (in seconds) | |
| `-a` | — | Allocated inodes | |
| `-A` | — | Unallocated inodes | |
| `-l` | — | Linked inodes | |
| `-L` | — | Unlinked inodes | |
| `-z` | — | Unused inodes | |
| `-Z` | — | Used inodes | |
| `-i` | imgtype | The format of the image file (use '-i list' for supported types) | |
| `-b` | dev_sector_size | The size (in bytes) of the device sectors | |
| `-f` | fstype | File system type (use '-f list' for supported types) | |
| `-o` | imgoffset | The offset of the file system in the image (in sectors) | |
| `-P` | pooltype | Pool container type (use '-p list' for supported types) | |
| `-B` | pool_volume_block | Starting block (for pool volumes only) | |
| `-v` | — | verbose output to stderr | |
| `-V` | — | Display version number | |

## Gotchas

_TODO: operational traps._

## See also

`fls`, `ffind`, `tsk_recover`, `istat`, `file`, `stat`
