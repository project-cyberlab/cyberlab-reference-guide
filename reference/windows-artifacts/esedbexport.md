<!-- generated-by: scripts/generate_pages.py -->
# esedbexport

**Kit:** SIFT Workstation (libyal)  **Capability:** Parse ESE / SRUM / Amcache databases
**Captured:** `cyberlab-aio` via `--help` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/esedbexport.help.txt)

## Purpose

Invalid argument: esedbexport

## Synopsis

```
esedbexport [ -c codepage ] [ -l logfile ] [ -m mode ] [ -t target ]
[ -T table_name ] [ -hvV ] source
```

## Common invocations

<!-- candidates mined from cyberlab; verify each flag against the options table below before treating as reviewed -->
```
# from cyberlab 06-windows-artifact-libs
esedbexport -V
# from cyberlab 06-windows-artifact-libs
esedbexport -t /tmp/edb_out exercise/Current.edb
```

## Options

All 8 options parsed from the captured help text. The final column is the judgement layer and is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-c` | — | codepage of ASCII strings, options: ascii, windows-874, windows-932, windows-936, windows-1250, windows-1251, windows-1252 (default), windows-1253, windows-1254 windows-1255, windows-1256, windows-125 | |
| `-h` | — | shows this help | |
| `-l` | — | logs information about the exported items | |
| `-m` | — | export mode, option: all, tables (default) 'all' exports all the tables or a single specified table with indexes, 'tables' exports all the tables or a single specified table | |
| `-t` | — | specify the basename of the target directory to export to (default is the source filename) esedbexport will add the suffix .export to the basename | |
| `-T` | — | exports only a specific table | |
| `-v` | — | verbose output to stderr | |
| `-V` | — | print version | |

## Gotchas

_TODO: operational traps._

## See also

`esedbinfo`, `SrumECmd`, `AmcacheParser`
