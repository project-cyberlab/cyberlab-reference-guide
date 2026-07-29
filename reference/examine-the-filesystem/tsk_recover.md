<!-- generated-by: scripts/generate_pages.py -->
# tsk_recover

**Kit:** REMnux · Kali Linux · SIFT Workstation  **Capability:** List files and directories, including deleted ones; Recover deleted or lost files  **Version:** The Sleuth Kit ver 4.11.1
**Captured:** `cyberlab-aio` via `--help` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/tsk_recover.help.txt)  **Docs:** <https://www.sleuthkit.org/sleuthkit>

## Purpose

Analyze disk images and recover files from them.

## Synopsis

```
tsk_recover [-vVae] [-f fstype] [-i imgtype] [-b dev_sector_size] [-o sector_offset] [-P pooltype] [-B pool_volume_block] [-d dir_inum] image [image] output_dir
```

## Common invocations

_TODO: up to 8 task-titled invocations._

## Options

All 11 options parsed from the captured help text. The final column is the judgement layer and is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-i` | imgtype | The format of the image file (use '-i list' for supported types) | |
| `-b` | dev_sector_size | The size (in bytes) of the device sectors | |
| `-f` | fstype | The file system type (use '-f list' for supported types) | |
| `-v` | — | verbose output to stderr | |
| `-V` | — | Print version | |
| `-a` | — | Recover allocated files only | |
| `-e` | — | Recover all files (allocated and unallocated) | |
| `-o` | sector_offset | sector offset for a volume to recover (recovers only that volume) | |
| `-P` | pooltype | Pool container type (use '-P list' for supported types) | |
| `-B` | pool_volume_block | Starting block (for pool volumes only) | |
| `-d` | dir_inum | Directory inum to recover from (must also specify a specific partition using -o or there must not be a volume system) | |

## Gotchas

_TODO: operational traps._

## See also

`fls`, `ffind`, `ils`, `icat`, `photorec`, `testdisk`, `blkls`
