<!-- generated-by: scripts/generate_pages.py -->
# ils

| | |
|---|---|
| **Kit** | REMnux · Kali Linux · SIFT Workstation |
| **Capability** | List files and directories, including deleted ones; Inspect metadata for one file or inode |
| **Version** | The Sleuth Kit ver 4.11.1 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-10 — [raw help output](../../capture/cyberlab-aio/help/ils.help.txt) |
| **Documentation** | <https://www.sleuthkit.org/sleuthkit> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

List inode metadata, including inodes that no longer have a name pointing at them.

## Synopsis

```
ils [-emOpvV] [-aAlLzZ] [-f fstype] [-i imgtype] [-b dev_sector_size] [-o imgoffset] [-P pooltype] [-B pool_volume_block] [-s seconds] image [images] [inum[-end]]
```

## Options

All 19 options parsed from the captured help text; 18 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-e` | — | Display all inodes | Every inode, allocated or not. |
| `-m` | — | Display output in the mactime format | mactime format — the form `mactime` consumes to build a timeline. This is how deleted-file metadata reaches the timeline at all. |
| `-O` | — | Display inodes that are unallocated, but were sill open (UFS/ExtX only) | Unallocated inodes that were still open at the time of imaging (UFS/ExtX). The same trick, caught mid-deletion. |
| `-p` | — | Display orphan inodes (unallocated with no file name) | Orphan inodes — allocated content with no directory entry. Files that were unlinked while still open, and a standard hiding place worth checking explicitly. |
| `-s` | seconds | Time skew of original machine (in seconds) | Correct for a known clock skew on the source machine, in seconds, so times line up with other evidence. |
| `-a` | — | Allocated inodes | Allocated inodes only. |
| `-A` | — | Unallocated inodes | Unallocated inodes only — deleted file metadata that often survives after the name is gone. |
| `-l` | — | Linked inodes | Linked inodes (a name still points at them). |
| `-L` | — | Unlinked inodes | Unlinked inodes (nothing does). |
| `-z` | — | Unused inodes | Unused inodes. |
| `-Z` | — | Used inodes | Used inodes. |
| `-i` | imgtype | The format of the image file (use '-i list' for supported types) | Image format for non-raw evidence such as E01 or AFF. |
| `-b` | dev_sector_size | The size (in bytes) of the device sectors | Device sector size; required on 4Kn drives. |
| `-f` | fstype | File system type (use '-f list' for supported types) | Force the filesystem type (`-f list` shows the options). |
| `-o` | imgoffset | The offset of the file system in the image (in sectors) | Offset, in sectors, from `mmls`. |
| `-P` | pooltype | Pool container type (use '-p list' for supported types) | Pool type, for APFS or LVM containers. |
| `-B` | pool_volume_block | Starting block (for pool volumes only) | Starting block within a pool volume. |
| `-v` | — | verbose output to stderr | Verbose diagnostics to stderr. |
| `-V` | — | Display version number |  |

## Gotchas

- `ils` finds metadata with no name; [`ffind`](ffind.md) turns an inode back into a name; [`icat`](icat.md) extracts its content. Deleted-file work is usually all three in sequence.
- An inode surviving does not mean its data did. The blocks it points at may already be reallocated, so [`icat`](icat.md) can return another file's contents entirely.

## See also

[`fls`](../examine-the-filesystem/fls.md), [`ffind`](../examine-the-filesystem/ffind.md), [`tsk_recover`](../examine-the-filesystem/tsk_recover.md), [`istat`](../examine-the-filesystem/istat.md), [`file`](../examine-the-filesystem/file.md), `stat`
