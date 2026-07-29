<!-- generated-by: scripts/generate_pages.py -->
# regfmount

**Kit:** SIFT Workstation (libyal)  **Capability:** Parse registry hives
**Captured:** `cyberlab-aio` via `--help` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/regfmount.help.txt)

## Purpose

Invalid argument: regfmount

## Synopsis

```
regfmount [ -c codepage ] [ -X extended_options ] [ -hvV ] file
mount_point
```

## Common invocations

_TODO: up to 8 task-titled invocations._

## Options

All 5 options parsed from the captured help text. The final column is the judgement layer and is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-c` | — | codepage of ASCII strings, options: ascii, windows-874, windows-932, windows-936, windows-949, windows-950, windows-1250, windows-1251, windows-1252 (default), windows-1253, windows-1254, windows-1255 | |
| `-h` | — | shows this help | |
| `-v` | — | verbose output to stderr, while regfmount will remain running in the foreground | |
| `-V` | — | print version | |
| `-X` | — | extended options to pass to sub system | |

## Gotchas

_TODO: operational traps._

## See also

`rip.pl`, `regripper`, `hivexsh`, `regfexport`, `regfinfo`, `regipy-dump`, `regipy-parse-header`, `regipy-plugins-run`
