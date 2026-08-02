<!-- generated-by: scripts/generate_pages.py -->
# mmls

**Kit:** REMnux · Kali Linux · SIFT Workstation  **Capability:** See the partition and volume layout  **Version:** The Sleuth Kit ver 4.11.1
**Captured:** `cyberlab-aio` via `--help` on 2026-08-02  [raw](../../capture/cyberlab-aio/help/mmls.help.txt)  **Docs:** <https://www.sleuthkit.org/sleuthkit>

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Display the partition layout of a disk image, including unallocated gaps.

## Options

All 12 options parsed from the captured help text; 9 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-t` | vstype | The type of volume system (use '-t list' for list of supported types) | Force the volume-system type when auto-detection guesses wrong (`-t list` shows the options). |
| `-i` | imgtype | The format of the image file (use '-i list' for list supported types) | Set the image format for non-raw evidence such as E01 or AFF. |
| `-b` | dev_sector_size | The size (in bytes) of the device sectors | Set the device sector size; required on 4Kn drives where the 512-byte default is wrong. |
| `-o` | imgoffset | Offset to the start of the volume that contains the partition system (in sectors) | Read a volume system nested at an offset — rare, but needed for nested containers. |
| `-B` | — | print the rounded length in bytes | Print volume sizes in bytes rather than sectors, when reporting. |
| `-r` | — | recurse and look for other partition tables in partitions (DOS Only) | Recurse into nested volume systems (e.g. an extended partition). |
| `-v` | — | verbose output | Verbose diagnostics to stderr when an image will not parse. |
| `-V` | — | print the version |  |
| `-a` | — | Show allocated volumes | Show allocated volumes only, when the gap entries are noise. |
| `-A` | — | Show unallocated volumes | Show unallocated space only — where a hidden or deleted partition would show up. |
| `-m` | — | Show metadata volumes |  |
| `-M` | — | Hide metadata volumes |  |

## Gotchas

- The **Start** column is in sectors. That value is what every other TSK tool wants for `-o`. Multiplying by the sector size here is the single most common mistake in a TSK workflow.
- If `mmls` reports no partition table, the image may be a single volume rather than a whole disk — try [`fsstat`](fsstat.md) on it directly at offset 0 before assuming the image is corrupt.

## See also

[`fsstat`](../examine-the-filesystem/fsstat.md), [`img_stat`](../acquire-preserve/img_stat.md), [`testdisk`](../examine-the-filesystem/testdisk.md)
