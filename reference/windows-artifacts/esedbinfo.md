<!-- generated-by: scripts/generate_pages.py -->
# esedbinfo

| | |
|---|---|
| **Kit** | SIFT Workstation (libyal) |
| **Capability** | Parse ESE / SRUM / Amcache databases |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-11 — [raw help output](../../capture/cyberlab-aio/help/esedbinfo.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Use esedbinfo to determine information about an Extensible Storage Engine (ESE)

## When you'd reach for this

An analyst reaches for esedbinfo when examining Extensible Storage Engine (ESE) Database Files (EDB) to retrieve metadata such as file format, page size, tables, columns, and indexes, as demonstrated by the example `esedbinfo Windows.edb`. They may run it after obtaining an EDB file from a system, such as one used by Exchange or Active Directory, to understand its structure before deeper analysis. The tool is chosen for its specific focus on ESE databases and its ability to provide detailed catalog information, as described in the documentation.

**Sources:** <https://github.com/4k4xs4pH1r3/libesedb-utils/blob/master/libesedb.md> · <https://manpages.debian.org/unstable/libesedb-utils/esedbinfo.1.en.html>

## Synopsis

```
esedbinfo [ -hvV ] source
```

## Options

All 3 options parsed from the captured help text; 1 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-h` | — | shows this help |  |
| `-v` | — | verbose output to stderr | An analyst would use the -v flag when needing detailed verbose output about an ESE Database File's structure and contents, such as page size, table counts, and column details. |
| `-V` | — | print version |  |

## Gotchas

_TODO: operational traps._

## See also

[`esedbexport`](../windows-artifacts/esedbexport.md), [`SrumECmd`](../windows-artifacts/SrumECmd.md), [`AmcacheParser`](../windows-artifacts/AmcacheParser.md)
