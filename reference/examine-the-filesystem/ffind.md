<!-- generated-by: scripts/generate_pages.py -->
# ffind

**Kit:** REMnux · Kali Linux · SIFT Workstation  **Capability:** List files and directories, including deleted ones  **Version:** The Sleuth Kit ver 4.11.1
**Captured:** `cyberlab-aio` via `--help` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/ffind.help.txt)  **Docs:** <https://www.sleuthkit.org/sleuthkit>

## Purpose

Analyze disk images and recover files from them.

## Synopsis

```
ffind [-aduvV] [-f fstype] [-i imgtype] [-b dev_sector_size] [-o imgoffset] [-P pooltype] [-B pool_volume_block] image [images] inode
```

## Common invocations

_TODO: up to 8 task-titled invocations._

## Options

All 11 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-a` | — | Find all occurrences |  |
| `-d` | — | Find deleted entries ONLY |  |
| `-u` | — | Find undeleted entries ONLY |  |
| `-f` | fstype | Image file system type (use '-f list' for supported types) |  |
| `-i` | imgtype | The format of the image file (use '-i list' for supported types) |  |
| `-b` | dev_sector_size | The size (in bytes) of the device sectors |  |
| `-o` | imgoffset | The offset of the file system in the image (in sectors) |  |
| `-P` | pooltype | Pool container type (use '-p list' for supported types) |  |
| `-B` | pool_volume_block | Starting block (for pool volumes only) |  |
| `-v` | — | Verbose output to stderr |  |
| `-V` | — | Print version |  |

## Gotchas

_TODO: operational traps._

## See also

`fls`, `ils`, `tsk_recover`
