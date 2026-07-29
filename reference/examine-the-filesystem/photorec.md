<!-- generated-by: scripts/generate_pages.py -->
# photorec

**Kit:** SIFT Workstation  **Capability:** Recover deleted or lost files  **Version:** PhotoRec 7.1
**Captured:** `cyberlab-aio` via `--help` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/photorec.help.txt)

## Purpose

PhotoRec 7.1, Data Recovery Utility, July 2019

## Synopsis

```
photorec [/log] [/debug] [/d recup_dir] [file.dd|file.e01|device]
photorec /version
```

## Common invocations

<!-- candidates mined from cyberlab; verify each flag against the options table below before treating as reviewed -->
```
# from cyberlab 01-disk-forensics
photorec /version
# from cyberlab 01-disk-forensics
photorec /log /d /tmp/carved /cmd exercise/sample.dd partition_none,options,mode_ext2,fileopt,everything,enable,search
```

## Options

All 2 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `/log` | — | create a photorec.log file |  |
| `/debug` | — | add debug information |  |

## Gotchas

_TODO: operational traps._

## See also

`tsk_recover`, `icat`, `testdisk`, `blkls`
