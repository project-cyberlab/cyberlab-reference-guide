<!-- generated-by: scripts/generate_pages.py -->
# esedbexport

| | |
|---|---|
| **Kit** | SIFT Workstation (libyal) |
| **Capability** | Parse ESE / SRUM / Amcache databases |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-07 — [raw help output](../../capture/cyberlab-aio/help/esedbexport.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Use esedbexport to export items stored in an Extensible Storage Engine (ESE)

## When you'd reach for this

When analyzing EDB files from applications like Active Directory, an analyst uses esedbexport after mounting the file via Docker, as shown in the example command, to extract structured data from the database. They might run it after obtaining the EDB file through imaging or extraction tools, and choose it because it is specifically designed for ESE databases, as indicated by the documentation's mention of its use in Windows Mail, Exchange, and Active Directory.

**Sources:** <https://github.com/4k4xs4pH1r3/libesedb-utils/blob/master/libesedb.md> · <https://github.com/security-dockerfiles/esedbexport>

## Synopsis

```
esedbexport [ -c codepage ] [ -l logfile ] [ -m mode ] [ -t target ]
[ -T table_name ] [ -hvV ] source
```

## Options

All 8 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-c` | — | codepage of ASCII strings, options: ascii, windows-874, windows-932, windows-936, windows-1250, windows-1251, windows-1252 (default), windows-1253, windows-1254 windows-1255, windows-1256, windows-125 |  |
| `-h` | — | shows this help |  |
| `-l` | — | logs information about the exported items |  |
| `-m` | — | export mode, option: all, tables (default) 'all' exports all the tables or a single specified table with indexes, 'tables' exports all the tables or a single specified table |  |
| `-t` | — | specify the basename of the target directory to export to (default is the source filename) esedbexport will add the suffix .export to the basename |  |
| `-T` | — | exports only a specific table |  |
| `-v` | — | verbose output to stderr |  |
| `-V` | — | print version |  |

## Gotchas

_TODO: operational traps._

## See also

[`esedbinfo`](../windows-artifacts/esedbinfo.md), [`SrumECmd`](../windows-artifacts/SrumECmd.md), [`AmcacheParser`](../windows-artifacts/AmcacheParser.md)
