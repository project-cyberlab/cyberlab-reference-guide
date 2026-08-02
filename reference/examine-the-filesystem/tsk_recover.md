<!-- generated-by: scripts/generate_pages.py -->
# tsk_recover

| | |
|---|---|
| **Kit** | REMnux · Kali Linux · SIFT Workstation |
| **Capability** | List files and directories, including deleted ones; Recover deleted or lost files |
| **Version** | The Sleuth Kit ver 4.11.1 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-02 — [raw help output](../../capture/cyberlab-aio/help/tsk_recover.help.txt) |
| **Documentation** | <https://www.sleuthkit.org/sleuthkit> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Bulk-export files from an image to a directory.

## Synopsis

```
tsk_recover [-vVae] [-f fstype] [-i imgtype] [-b dev_sector_size] [-o sector_offset] [-P pooltype] [-B pool_volume_block] [-d dir_inum] image [image] output_dir
```

## Options

All 11 options parsed from the captured help text; 6 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-i` | imgtype | The format of the image file (use '-i list' for supported types) | Image format for non-raw evidence. |
| `-b` | dev_sector_size | The size (in bytes) of the device sectors |  |
| `-f` | fstype | The file system type (use '-f list' for supported types) | Force the filesystem type. |
| `-v` | — | verbose output to stderr |  |
| `-V` | — | Print version |  |
| `-a` | — | Recover allocated files only | Recover allocated (live) files only. |
| `-e` | — | Recover all files (allocated and unallocated) | Recover every file, allocated and deleted — the usual choice. |
| `-o` | sector_offset | sector offset for a volume to recover (recovers only that volume) | Partition offset in sectors, from `mmls`. |
| `-P` | pooltype | Pool container type (use '-P list' for supported types) |  |
| `-B` | pool_volume_block | Starting block (for pool volumes only) |  |
| `-d` | dir_inum | Directory inum to recover from (must also specify a specific partition using -o or there must not be a volume system) | Recover from a specified directory inode rather than the root. |

## Gotchas

- Default behaviour recovers only *deleted* files, which surprises people expecting a full export. Use `-e` for everything.
- This preserves paths and names, unlike carving. Prefer it whenever the filesystem metadata is intact, and carve only what it cannot reach.

## See also

[`fls`](../examine-the-filesystem/fls.md), [`ffind`](../examine-the-filesystem/ffind.md), [`ils`](../examine-the-filesystem/ils.md), [`icat`](../examine-the-filesystem/icat.md), [`photorec`](../examine-the-filesystem/photorec.md), [`testdisk`](../examine-the-filesystem/testdisk.md), [`blkls`](../examine-the-filesystem/blkls.md)
