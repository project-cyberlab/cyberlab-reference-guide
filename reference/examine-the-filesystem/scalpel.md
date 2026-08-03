<!-- generated-by: scripts/generate_pages.py -->
# scalpel

| | |
|---|---|
| **Kit** | REMnux · Kali Linux · SIFT Workstation |
| **Capability** | Carve files out of unstructured data |
| **Version** | Scalpel version 1.60 |
| **Captured from** | `cyberlab-aio` via `-h` on 2026-08-03 — [raw help output](../../capture/cyberlab-aio/help/scalpel.help.txt) |
| **Documentation** | <https://github.com/sleuthkit/scalpel> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Carve contents out of binary files, such as partitions.

## Synopsis

```
scalpel [-b] [-c <config file>] [-d] [-h|V] [-i <file>]
[-m blocksize] [-n] [-o <outputdir>] [-O num] [-q clustersize]
[-r] [-s num] [-t <blockmap file>] [-u] [-v]
<imgfile> [<imgfile>] ...
```

## Options

All 17 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-b` | — | Carve files even if defined footers aren't discovered within maximum carve size for file type [foremost 0.69 compat mode]. |  |
| `-c` | — | Choose configuration file. |  |
| `-d` | — | Generate header/footer database; will bypass certain optimizations and discover all footers, so performance suffers. Doesn't affect the set of files carved. **EXPERIMENTAL** |  |
| `-h` | — | Print this help message and exit. |  |
| `-i` | — | Read names of disk images from specified file. |  |
| `-m` | — | Generate/update carve coverage blockmap file. The first 32bit unsigned int in the file identifies the block size. Thereafter each 32bit unsigned int entry in the blockmap file corresponds to one block |  |
| `-n` | — | Don't add extensions to extracted files. |  |
| `-o` | — | Set output directory for carved files. |  |
| `-O` | — | Don't organize carved files by type. Default is to organize carved files into subdirectories. |  |
| `-p` | — | Perform image file preview; audit log indicates which files would have been carved, but no files are actually carved. |  |
| `-q` | — | Carve only when header is cluster-aligned. |  |
| `-r` | — | Find only first of overlapping headers/footers [foremost 0.69 compat mode]. |  |
| `-s` | — | Skip n bytes in each disk image before carving. |  |
| `-t` | — | Set directory for coverage blockmap. **EXPERIMENTAL** |  |
| `-u` | — | Use carve coverage blockmap when carving. Carve only sections of the image whose entries in the blockmap are 0. These areas are treated as contiguous regions. **EXPERIMENTAL** |  |
| `-V` | — | Print copyright information and exit. |  |
| `-v` | — | Verbose mode. |  |

## Gotchas

_TODO: operational traps._

## See also

[`foremost`](../examine-the-filesystem/foremost.md), [`binwalk`](../examine-the-filesystem/binwalk.md), [`bulk_extractor`](../examine-the-filesystem/bulk_extractor.md), [`tcpxtract`](../examine-the-filesystem/tcpxtract.md)
