<!-- generated-by: scripts/generate_pages.py -->
# istat

| | |
|---|---|
| **Kit** | REMnux · Kali Linux · SIFT Workstation |
| **Capability** | Inspect metadata for one file or inode |
| **Version** | The Sleuth Kit ver 4.11.1 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-09 — [raw help output](../../capture/cyberlab-aio/help/istat.help.txt) |
| **Documentation** | <https://www.sleuthkit.org/sleuthkit> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Show the full metadata for one inode: times, size, and the blocks it occupies.

## Synopsis

```
istat [-N num] [-f fstype] [-i imgtype] [-b dev_sector_size] [-o imgoffset] [-P pooltype] [-B pool_volume_block] [-z zone] [-s seconds] [-rvV] image inum
```

## Options

All 14 options parsed from the captured help text; 5 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-N` | num | force the display of NUM address of block pointers | Limit how many block addresses are printed for a large file. |
| `-r` | — | display run list instead of list of block addresses | Include recovery information for a deleted inode. |
| `-z` | zone | time zone of original machine (i.e. EST5EDT or GMT) | Set the time zone for the displayed timestamps. |
| `-s` | seconds | Time skew of original machine (in seconds) | Apply a clock skew in seconds for a known-bad system clock. |
| `-i` | imgtype | The format of the image file (use '-i list' for supported types) |  |
| `-b` | dev_sector_size | The size (in bytes) of the device sectors |  |
| `-f` | fstype | File system type (use '-f list' for supported types) |  |
| `-o` | imgoffset | The offset of the file system in the image (in sectors) | Partition offset in sectors, from `mmls`. |
| `-P` | pooltype | Pool container type (use '-p list' for supported types) |  |
| `-B` | pool_volume_block | Starting block (for pool volumes only) |  |
| `-S` | snap_id | Snapshot ID (for APFS only) |  |
| `-v` | — | verbose output to stderr |  |
| `-V` | — | print version |  |
| `-k` | password | Decryption password for encrypted volumes |  |

## Gotchas

- The block list is what lets you prove whether a deleted file is still recoverable — cross-check it before promising a recovery.

## See also

[`ils`](../examine-the-filesystem/ils.md), [`file`](../examine-the-filesystem/file.md), `stat`
