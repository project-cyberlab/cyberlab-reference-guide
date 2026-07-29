<!-- generated-by: scripts/generate_pages.py -->
# istat

**Kit:** REMnux · Kali Linux · SIFT Workstation  **Capability:** Inspect metadata for one file or inode  **Version:** The Sleuth Kit ver 4.11.1
**Captured:** `cyberlab-aio` via `--help` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/istat.help.txt)  **Docs:** <https://www.sleuthkit.org/sleuthkit>

## Purpose

Analyze disk images and recover files from them.

## Synopsis

```
istat [-N num] [-f fstype] [-i imgtype] [-b dev_sector_size] [-o imgoffset] [-P pooltype] [-B pool_volume_block] [-z zone] [-s seconds] [-rvV] image inum
```

## Common invocations

<!-- candidates mined from cyberlab; verify each flag against the options table below before treating as reviewed -->
```
# from cyberlab 22-sleuthkit-mastery
istat -o 2048 exercise/practice.dd 4
```

## Options

All 14 options parsed from the captured help text. The final column is the judgement layer and is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-N` | num | force the display of NUM address of block pointers | |
| `-r` | — | display run list instead of list of block addresses | |
| `-z` | zone | time zone of original machine (i.e. EST5EDT or GMT) | |
| `-s` | seconds | Time skew of original machine (in seconds) | |
| `-i` | imgtype | The format of the image file (use '-i list' for supported types) | |
| `-b` | dev_sector_size | The size (in bytes) of the device sectors | |
| `-f` | fstype | File system type (use '-f list' for supported types) | |
| `-o` | imgoffset | The offset of the file system in the image (in sectors) | |
| `-P` | pooltype | Pool container type (use '-p list' for supported types) | |
| `-B` | pool_volume_block | Starting block (for pool volumes only) | |
| `-S` | snap_id | Snapshot ID (for APFS only) | |
| `-v` | — | verbose output to stderr | |
| `-V` | — | print version | |
| `-k` | password | Decryption password for encrypted volumes | |

## Gotchas

_TODO: operational traps._

## See also

`ils`, `file`, `stat`
