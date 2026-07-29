<!-- generated-by: scripts/generate_pages.py -->
# fsstat

**Kit:** REMnux · Kali Linux · SIFT Workstation  **Capability:** See the partition and volume layout  **Version:** The Sleuth Kit ver 4.11.1
**Captured:** `cyberlab-aio` via `--help` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/fsstat.help.txt)  **Docs:** <https://www.sleuthkit.org/sleuthkit>

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Analyze disk images and recover files from them.

## Synopsis

```
fsstat [-tvV] [-f fstype] [-i imgtype] [-b dev_sector_size] [-o imgoffset] image
```

## Common invocations

<!-- candidates mined from cyberlab; verify each flag against the options table below before treating as reviewed -->
```
# from cyberlab 01-disk-forensics
fsstat -V
# from cyberlab 01-disk-forensics
fsstat -o 2048 exercise/sample.dd
# from cyberlab 01-disk-forensics
fsstat -o 0 exercise/sample.dd | grep -Ei "file system type|sector size|cluster size"
# from cyberlab 22-sleuthkit-mastery
fsstat -o 2048 exercise/practice.dd
# from cyberlab 51-linux-triage-workflow
fsstat -o 2048 disk.raw
```

## Options

All 10 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-t` | — | display type only |  |
| `-i` | imgtype | The format of the image file (use '-i list' for supported types) |  |
| `-b` | dev_sector_size | The size (in bytes) of the device sectors |  |
| `-f` | fstype | File system type (use '-f list' for supported types) |  |
| `-o` | imgoffset | The offset of the file system in the image (in sectors) |  |
| `-P` | pooltype | Pool container type (use '-P list' for supported types) |  |
| `-B` | pool_volume_block | Starting block (for pool volumes only) |  |
| `-v` | — | verbose output to stderr |  |
| `-V` | — | Print version |  |
| `-k` | password | Decryption password for encrypted volumes |  |

## Gotchas

_TODO: operational traps._

## See also

[`mmls`](../examine-the-filesystem/mmls.md), [`img_stat`](../acquire-preserve/img_stat.md), [`testdisk`](../examine-the-filesystem/testdisk.md)
