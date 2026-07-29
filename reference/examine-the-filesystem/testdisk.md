<!-- generated-by: scripts/generate_pages.py -->
# testdisk

**Kit:** SIFT Workstation  **Capability:** See the partition and volume layout; Recover deleted or lost files  **Version:** TestDisk 7.1
**Captured:** `cyberlab-aio` via `--help` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/testdisk.help.txt)

## Purpose

TestDisk 7.1, Data Recovery Utility, July 2019

## Synopsis

```
testdisk [/log] [/debug] [file.dd|file.e01|device]
testdisk /list  [/log]   [file.dd|file.e01|device]
testdisk /version
```

## Common invocations

<!-- candidates mined from cyberlab; verify each flag against the options table below before treating as reviewed -->
```
# from cyberlab 01-disk-forensics
testdisk /version
```

## Options

All 3 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `/log` | — | create a testdisk.log file |  |
| `/debug` | — | add debug information |  |
| `/list` | — | display current partitions |  |

## Gotchas

_TODO: operational traps._

## See also

`mmls`, `fsstat`, `img_stat`, `tsk_recover`, `icat`, `photorec`, `blkls`
