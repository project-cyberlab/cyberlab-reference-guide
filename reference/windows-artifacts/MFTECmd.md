<!-- generated-by: scripts/generate_pages.py -->
# MFTECmd

**Kit:** FLARE-VM / SIFT (Eric Zimmerman tools)  **Capability:** Parse execution and persistence artifacts  **Version:** 2026.5.0+4fd94a6bd12237e8501baff5fc9e5b1b01c53862
**Captured:** `cyberlab-aio` via `--help` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/MFTECmd.help.txt)

## Purpose

Description:

## Synopsis

```
MFTECmd [options]
```

## Common invocations

_TODO: up to 8 task-titled invocations._

## Options

All 32 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-f` | f | File to process ($MFT \| $J \| $Boot \| $SDS \| $I30). Required |  |
| `-m` | m | $MFT file to use when -f points to a $J file (Use this to resolve parent path in $J CSV output) |  |
| `--csv` | csv | Directory to save CSV formatted results to. Be sure to include the full path in double quotes. This or --json required unless --de or --body is specified |  |
| `--csvf` | csvf | File name to save CSV formatted results to. When present, overrides default name |  |
| `--json` | json | Directory to save JSON formatted results to. Be sure to include the full path in double quotes. This or --csv required unless --de or --body is specified |  |
| `--jsonf` | jsonf | File name to save JSON formatted results to. When present, overrides default name |  |
| `--body` | body | Directory to save bodyfile formatted results to. --bdl is also required when using this option |  |
| `--bodyf` | bodyf | File name to save body formatted results to. When present, overrides default name |  |
| `--bdl` | bdl | Drive letter (C, D, etc.) to use with bodyfile. Only the drive letter itself should be provided |  |
| `--blf` | — | When true, use LF vs CRLF for newlines |  |
| `--dd` | dd | Directory to save exported $MFT FILE record. --do is also required when using this option |  |
| `--do` | do | Offset of the $MFT FILE record to dump as decimal or hex. Ex: 5120 or 0x1400 Use --de or --debug to see offsets |  |
| `--de` | de | Dump full details for $MFT entry/sequence #. Format is 'Entry' or 'Entry-Seq' as decimal or hex. Example: 5, 624-5 or 0x270-0x5. |  |
| `--dr` | — | When true, dump $MFT resident files to dir specified by --csv or --json, in 'Resident' subdirectory. Files will be named '<EntryNumber>-<SequenceNumber>-<AttributeNumber>_<FileName>.bin' |  |
| `--fls` | — | When true, displays contents of directory from $MFT specified by --de. Ignored when --de points to a file |  |
| `--ds` | ds | Dump full details for Security Id from $SDS as decimal or hex. Example: 624 or 0x270 |  |
| `--dt` | dt | The custom date/time format to use when displaying time stamps. See https://goo.gl/CNVq0k for options [default: yyyy-MM-dd HH:mm:ss.fffffff] |  |
| `--sn` | — | Include DOS file name types in $MFT output |  |
| `--fl` | — | Generate condensed file listing of parsed $MFT contents. Requires --csv |  |
| `--at` | — | When true, include all timestamps from 0x30 attribute vs only when they differ from 0x10 in the $MFT |  |
| `--rs` | — | When true, recover slack space from FILE records when processing $MFT files. This option has no effect for $I30 files |  |
| `--vss` | — | Process all Volume Shadow Copies that exist on drive specified by -f |  |
| `--dedupe` | — | Deduplicate -f & VSCs based on SHA-1. First file found wins |  |
| `--ir` | — | Include resident data in JSON/CSV output |  |
| `--re` | re | Comma-separated list of extensions to include for resident data (e.g., '.txt,.ps1,.bat'). If omitted, includes all |  |
| `--rm` | rm | Maximum size in bytes for resident data to include (max: 1024000) [default: 1024] |  |
| `--debug` | — | Show debug information during processing |  |
| `--trace` | — | Show trace information during processing |  |
| `-?` | — | Show help and usage information |  |
| `-h` | — | Show help and usage information |  |
| `--help` | — | Show help and usage information |  |
| `--version` | — | Show version information |  |

## Gotchas

_TODO: operational traps._

## See also

`PECmd`, `AppCompatCacheParser`, `AmcacheParser`
