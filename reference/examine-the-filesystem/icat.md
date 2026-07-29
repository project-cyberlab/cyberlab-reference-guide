<!-- generated-by: scripts/generate_pages.py -->
# icat

**Kit:** REMnux · Kali Linux · SIFT Workstation  **Capability:** Recover deleted or lost files  **Version:** The Sleuth Kit ver 4.11.1
**Captured:** `cyberlab-aio` via `--help` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/icat.help.txt)  **Docs:** <https://www.sleuthkit.org/sleuthkit>

## Purpose

Analyze disk images and recover files from them.

## Synopsis

```
icat [-hrRsvV] [-f fstype] [-i imgtype] [-b dev_sector_size] [-o imgoffset] image [images] inum[-typ[-id]]
```

## Common invocations

<!-- candidates mined from cyberlab; verify each flag against the options table below before treating as reviewed -->
```
# from cyberlab 01-disk-forensics
icat -o 2048 exercise/sample.dd 5 > /tmp/recovered_file.bin
# from cyberlab 01-disk-forensics
icat -o 0 exercise/sample.dd 5 > /tmp/recovered.txt
# from cyberlab 22-sleuthkit-mastery
icat -o 2048 exercise/practice.dd 4 | head
# from cyberlab 22-sleuthkit-mastery
icat -o 2048 exercise/practice.dd 6
# from cyberlab 51-linux-triage-workflow
icat -o 2048 disk.raw 5 > recovered_file.bin
# from cyberlab 51-linux-triage-workflow
icat exercise/triage_sample.raw $(fls -p exercise/triage_sample.raw | awk '/eicar.com/{gsub(/:/,"",$2);print $2}') > exercise/extract/eicar.com
```

## Options

All 14 options parsed from the captured help text. The final column is the judgement layer and is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-h` | — | Do not display holes in sparse files | |
| `-r` | — | Recover deleted file | |
| `-R` | — | Recover deleted file and suppress recovery errors | |
| `-s` | — | Display slack space at end of file | |
| `-i` | imgtype | The format of the image file (use '-i list' for supported types) | |
| `-b` | dev_sector_size | The size (in bytes) of the device sectors | |
| `-f` | fstype | File system type (use '-f list' for supported types) | |
| `-o` | imgoffset | The offset of the file system in the image (in sectors) | |
| `-P` | pooltype | Pool container type (use '-P list' for supported types) | |
| `-B` | pool_volume_block | Starting block (for pool volumes only) | |
| `-S` | snap_id | Snapshot ID (for APFS only) | |
| `-v` | — | verbose to stderr | |
| `-V` | — | Print version | |
| `-k` | password | Decryption password for encrypted volumes | |

## Gotchas

_TODO: operational traps._

## See also

`tsk_recover`, `photorec`, `testdisk`, `blkls`
