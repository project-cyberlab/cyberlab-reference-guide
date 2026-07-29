<!-- generated-by: scripts/generate_pages.py -->
# stat

**Kit:** Base OS — present on every Linux image  **Capability:** Inspect metadata for one file or inode  **Version:** stat (GNU coreutils) 9.1
**Captured:** `cyberlab-aio` via `--help` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/stat.help.txt)

## Purpose

Display file or file system status.

## Synopsis

```
stat [OPTION]... FILE...
```

## Common invocations

_TODO: up to 8 task-titled invocations._

## Options

All 11 options parsed from the captured help text. The final column is the judgement layer and is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-L` | — | follow links | |
| `--dereference` | — | follow links | |
| `-f` | — | display file system status instead of file status | |
| `--file-system` | — | display file system status instead of file status | |
| `--cached` | MODE | specify how to use cached attributes; useful on remote file systems. See MODE below | |
| `-c` | — | --format=FORMAT use the specified FORMAT instead of the default; output a newline after each use of FORMAT | |
| `--printf` | FORMAT | like --format, but interpret backslash escapes, and do not output a mandatory trailing newline; if you want a newline, include \n in FORMAT | |
| `-t` | — | print the information in terse form | |
| `--terse` | — | print the information in terse form | |
| `--help` | — | display this help and exit | |
| `--version` | — | output version information and exit | |

## Gotchas

_TODO: operational traps._

## See also

`istat`, `ils`, `file`
