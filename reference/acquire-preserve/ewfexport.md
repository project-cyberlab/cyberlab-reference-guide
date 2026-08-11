<!-- generated-by: scripts/generate_pages.py -->
# ewfexport

| | |
|---|---|
| **Kit** | Kali Linux · SIFT Workstation |
| **Capability** | Inspect or mount a forensic image container |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-11 — [raw help output](../../capture/cyberlab-aio/help/ewfexport.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Convert an EWF/E01 image to raw, or to another EWF format, including extracting a subset of it.

## When you'd reach for this

An analyst reaches for ewfexport when they need to extract specific data from an EWF image, such as a partition or converting an E01 to another format, often after acquiring the image with ewfacquire; they may use it before further analysis to isolate relevant data, preferring it over other tools due to its flexibility in specifying byte ranges and output formats.

**Sources:** <https://bromiley.medium.com/tooling-thursday-libewf-ec27b4564c2a> · <https://forensics.wiki/libewf/>

## Synopsis

```
ewfexport [ -A codepage ] [ -b number_of_sectors ]
[ -B number_of_bytes ] [ -c compression_values ]
[ -d digest_type ] [ -f format ] [ -l log_filename ]
[ -o offset ] [ -p process_buffer_size ]
[ -S segment_file_size ] [ -t target ] [ -hqsuvVwx ] ewf_files
```

## Common invocations

```
# Convert EWF image to RAW or another EWF format
ewfexport image.E01
```

## Options

All 19 options parsed from the captured help text; 17 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-A` | — | codepage of header section, options: ascii (default), windows-874, windows-932, windows-936, windows-949, windows-950, windows-1250, windows-1251, windows-1252, windows-1253, windows-1254, windows-125 | Header codepage. |
| `-b` | — | specify the number of sectors to read at once (per chunk), options: 16, 32, 64 (default), 128, 256, 512, 1024, 2048, 4096, 8192, 16384 or 32768 (not used for raw and files formats) | Sectors per chunk. |
| `-B` | — | specify the number of bytes to export (default is all bytes) | Number of bytes to export — with `-o`, extracts one partition. |
| `-c` | — | specify the compression values as: level or method:level compression method options: deflate (default), bzip2 (bzip2 is only supported by EWF2 formats) compression level options: none (default), empty | Compression for an EWF target. |
| `-d` | — | calculate additional digest (hash) types besides md5, options: sha1, sha256 (not used for raw and files format) | Calculate an additional digest over the exported data. |
| `-f` | — | specify the output format to write to, options: raw (default), files (restricted to logical volume files), ewf, smart, encase1, encase2, encase3, encase4, encase5, encase6, encase7, encase7-v2, linen5 | Output format — `raw` for tools that cannot read EWF, or another EWF variant for compatibility. |
| `-h` | — | shows this help |  |
| `-l` | — | logs export errors and the digest (hash) to the log_filename | Log the export. |
| `-o` | — | specify the offset to start the export (default is 0) | Start offset, to export a region rather than the whole image. |
| `-p` | — | specify the process buffer size (default is the chunk size) | Process buffer size. |
| `-q` | — | quiet shows minimal status information | Minimal output. |
| `-s` | — | swap byte pairs of the media data (from AB to BA) (use this for big to little endian conversion and vice versa) | Swap byte pairs. |
| `-S` | — | specify the segment file size in bytes (default is 1.4 GiB) (minimum is 1.0 MiB, maximum is 7.9 EiB for raw, encase6 and encase7 format and 1.9 GiB for other formats) (not used for files format) | Segment size for the output. |
| `-t` | — | specify the target file to export to, use - for stdout (default is export) stdout is only supported for the raw format | Target name. `-` writes to stdout, which lets the image be piped straight into another tool without staging a full raw copy on disk. |
| `-u` | — | unattended mode (disables user interaction) | Unattended, for scripted conversion. |
| `-v` | — | verbose output to stderr | Verbose diagnostics to stderr. |
| `-V` | — | print version |  |
| `-w` | — | zero sectors on checksum error (mimic EnCase like behavior) | Zero sectors that cannot be read. |
| `-x` | — | use the chunk data instead of the buffered read and write functions. | Bypass the buffered read/write path. |

## Gotchas

- Exporting to raw discards the metadata and hashes that justified using E01. Keep the original: the raw copy is a working artefact, not the evidence.
- A raw export needs the full uncompressed size in free space. E01 compression routinely hides a 2 TB image inside 700 GB.

## See also

[`ewfinfo`](../acquire-preserve/ewfinfo.md), [`ewfmount`](../acquire-preserve/ewfmount.md), [`ewfverify`](../acquire-preserve/ewfverify.md), [`affinfo`](../acquire-preserve/affinfo.md), [`affcat`](../acquire-preserve/affcat.md), [`img_stat`](../acquire-preserve/img_stat.md), [`ntfs-3g`](../acquire-preserve/ntfs-3g.md), [`vshadowinfo`](../acquire-preserve/vshadowinfo.md)
