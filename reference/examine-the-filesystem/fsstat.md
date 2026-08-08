<!-- generated-by: scripts/generate_pages.py -->
# fsstat

| | |
|---|---|
| **Kit** | REMnux · Kali Linux · SIFT Workstation |
| **Capability** | See the partition and volume layout |
| **Version** | The Sleuth Kit ver 4.11.1 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-08 — [raw help output](../../capture/cyberlab-aio/help/fsstat.help.txt) |
| **Documentation** | <https://www.sleuthkit.org/sleuthkit> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Report a filesystem's layout and parameters: type, block size, inode range, and the geometry every other TSK tool needs.

## Synopsis

```
fsstat [-tvV] [-f fstype] [-i imgtype] [-b dev_sector_size] [-o imgoffset] image
```

## Options

All 10 options parsed from the captured help text; 9 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-t` | — | display type only | Print only the filesystem type. The scriptable form when all you need is a yes/no on what this volume is. |
| `-i` | imgtype | The format of the image file (use '-i list' for supported types) | Set the image format for non-raw evidence such as E01 or AFF. |
| `-b` | dev_sector_size | The size (in bytes) of the device sectors | Device sector size. Needed on 4Kn drives, where the 512-byte default silently computes every offset wrong. |
| `-f` | fstype | File system type (use '-f list' for supported types) | Force the filesystem type when detection is wrong or the superblock is damaged (`-f list` shows the options). |
| `-o` | imgoffset | The offset of the file system in the image (in sectors) | Offset, in **sectors**, of the filesystem inside the image. Take it from `mmls`; this is the flag that ties the two tools together. |
| `-P` | pooltype | Pool container type (use '-P list' for supported types) | Pool type, for APFS or LVM containers that hold the volume. |
| `-B` | pool_volume_block | Starting block (for pool volumes only) | Starting block within a pool volume. |
| `-v` | — | verbose output to stderr | Verbose diagnostics to stderr, useful when detection fails. |
| `-V` | — | Print version |  |
| `-k` | password | Decryption password for encrypted volumes | Password for an encrypted volume. |

## Gotchas

- Run this first. Block size and inode range from `fsstat` are what make [`blkls`](blkls.md), [`icat`](icat.md) and [`ils`](ils.md) output interpretable — starting anywhere else means guessing at the numbers they print.
- If it reports the wrong type or refuses the volume, the `-o` offset is wrong far more often than the image is corrupt.

## See also

[`mmls`](../examine-the-filesystem/mmls.md), [`img_stat`](../acquire-preserve/img_stat.md), [`testdisk`](../examine-the-filesystem/testdisk.md)
