<!-- generated-by: scripts/generate_pages.py -->
# ffind

| | |
|---|---|
| **Kit** | REMnux · Kali Linux · SIFT Workstation |
| **Capability** | List files and directories, including deleted ones |
| **Version** | The Sleuth Kit ver 4.11.1 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-10 — [raw help output](../../capture/cyberlab-aio/help/ffind.help.txt) |
| **Documentation** | <https://www.sleuthkit.org/sleuthkit> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Find the file name that points at a given inode — the reverse of a directory lookup.

## When you'd reach for this

An analyst reaches for ffind when searching for files based on string content or file signatures within a disk image, often after creating an image with tools like dd, as it efficiently locates files without requiring prior knowledge of inode numbers, making it preferable to manual searches or tools like fls for metadata-based queries.

**Sources:** <https://github.com/sleuthkit/sleuthkit/wiki/Body-file> · <https://github.com/sleuthkit/sleuthkit/wiki/Timelines> · <https://hackernoon.com/getting-started-with-digital-forensics-using-the-sleuth-kit-c34a3wkg>

## Synopsis

```
ffind [-aduvV] [-f fstype] [-i imgtype] [-b dev_sector_size] [-o imgoffset] [-P pooltype] [-B pool_volume_block] image [images] inode
```

## Options

All 11 options parsed from the captured help text; 10 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-a` | — | Find all occurrences | Show every name for the inode. Hard-linked files have more than one, and stopping at the first hides that. |
| `-d` | — | Find deleted entries ONLY | Deleted names only. The direct answer to "what was this inode called before it was removed?" |
| `-u` | — | Find undeleted entries ONLY | Undeleted names only, when a recycled inode is returning stale hits. |
| `-f` | fstype | Image file system type (use '-f list' for supported types) | Force the filesystem type (`-f list` shows the options). |
| `-i` | imgtype | The format of the image file (use '-i list' for supported types) | Image format for non-raw evidence such as E01 or AFF. |
| `-b` | dev_sector_size | The size (in bytes) of the device sectors | Device sector size; required on 4Kn drives. |
| `-o` | imgoffset | The offset of the file system in the image (in sectors) | Offset, in sectors, from `mmls`. |
| `-P` | pooltype | Pool container type (use '-p list' for supported types) | Pool type, for APFS or LVM containers. |
| `-B` | pool_volume_block | Starting block (for pool volumes only) | Starting block within a pool volume. |
| `-v` | — | Verbose output to stderr | Verbose diagnostics to stderr. |
| `-V` | — | Print version |  |

## Gotchas

- Inodes are reused. A name returned for a deleted inode may belong to whatever claimed it next, not to the file you are chasing — corroborate with [`istat`](istat.md) timestamps before naming it in a report.
- This is the tool for the question [`icat`](icat.md) provokes: you carved data out by inode and now need to say what it was called.

## See also

[`fls`](../examine-the-filesystem/fls.md), [`ils`](../examine-the-filesystem/ils.md), [`tsk_recover`](../examine-the-filesystem/tsk_recover.md)
