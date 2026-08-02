<!-- generated-by: scripts/generate_pages.py -->
# testdisk

**Kit:** SIFT Workstation  **Capability:** See the partition and volume layout; Recover deleted or lost files  **Version:** TestDisk 7.1
**Captured:** `cyberlab-aio` via `--help` on 2026-08-01  [raw](../../capture/cyberlab-aio/help/testdisk.help.txt)

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

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

[`mmls`](../examine-the-filesystem/mmls.md), [`fsstat`](../examine-the-filesystem/fsstat.md), [`img_stat`](../acquire-preserve/img_stat.md), [`tsk_recover`](../examine-the-filesystem/tsk_recover.md), [`icat`](../examine-the-filesystem/icat.md), [`photorec`](../examine-the-filesystem/photorec.md), [`blkls`](../examine-the-filesystem/blkls.md)
