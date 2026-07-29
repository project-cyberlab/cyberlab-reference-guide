<!-- generated-by: scripts/generate_pages.py -->
# mmls

**Kit:** REMnux · Kali Linux · SIFT Workstation  **Capability:** See the partition and volume layout  **Version:** The Sleuth Kit ver 4.11.1
**Captured:** `cyberlab-aio` via `--help` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/mmls.help.txt)  **Docs:** <https://www.sleuthkit.org/sleuthkit>

## Purpose

Analyze disk images and recover files from them.

## Common invocations

<!-- candidates mined from cyberlab; verify each flag against the options table below before treating as reviewed -->
```
# from cyberlab 01-disk-forensics
mmls -V
# from cyberlab 01-disk-forensics
mmls exercise/sample.dd
# from cyberlab 22-sleuthkit-mastery
mmls exercise/practice.dd
# from cyberlab 51-linux-triage-workflow
mmls disk.raw
# from cyberlab 57-forensic-acquisition
sudo mmls /mnt/ewf/ewf1
```

## Options

All 12 options parsed from the captured help text. The final column is the judgement layer and is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-t` | vstype | The type of volume system (use '-t list' for list of supported types) | |
| `-i` | imgtype | The format of the image file (use '-i list' for list supported types) | |
| `-b` | dev_sector_size | The size (in bytes) of the device sectors | |
| `-o` | imgoffset | Offset to the start of the volume that contains the partition system (in sectors) | |
| `-B` | — | print the rounded length in bytes | |
| `-r` | — | recurse and look for other partition tables in partitions (DOS Only) | |
| `-v` | — | verbose output | |
| `-V` | — | print the version | |
| `-a` | — | Show allocated volumes | |
| `-A` | — | Show unallocated volumes | |
| `-m` | — | Show metadata volumes | |
| `-M` | — | Hide metadata volumes | |

## Gotchas

_TODO: operational traps._

## See also

`fsstat`, `img_stat`, `testdisk`
