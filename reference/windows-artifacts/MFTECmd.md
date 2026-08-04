<!-- generated-by: scripts/generate_pages.py -->
# MFTECmd

| | |
|---|---|
| **Kit** | FLARE-VM / SIFT (Eric Zimmerman tools) |
| **Capability** | Parse execution and persistence artifacts |
| **Version** | 2026.5.0 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-04 — [raw help output](../../capture/cyberlab-aio/help/MFTECmd.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Parse NTFS metadata files — $MFT, $J, $Boot, $SDS, $I30 — into CSV or bodyfile, including entries for deleted files.

## Synopsis

```
MFTECmd [options]
```

## Options

All 32 options parsed from the captured help text; 26 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-f` | f | File to process ($MFT \| $J \| $Boot \| $SDS \| $I30). Required | The metadata file to parse. Required, and the file type is detected from its contents rather than its name. |
| `-m` | m | $MFT file to use when -f points to a $J file (Use this to resolve parent path in $J CSV output) | Supply the $MFT alongside a $J. Without it the journal shows file names with no path, because the parent directory only exists in the $MFT. |
| `--csv` | csv | Directory to save CSV formatted results to. Be sure to include the full path in double quotes. This or --json required unless --de or --body is specified | Write CSV to a directory. The normal output. |
| `--csvf` | csvf | File name to save CSV formatted results to. When present, overrides default name | Override the generated CSV filename. |
| `--json` | json | Directory to save JSON formatted results to. Be sure to include the full path in double quotes. This or --csv required unless --de or --body is specified | JSON output, for a pipeline. |
| `--jsonf` | jsonf | File name to save JSON formatted results to. When present, overrides default name | Override the generated JSON filename. |
| `--body` | body | Directory to save bodyfile formatted results to. --bdl is also required when using this option | Bodyfile output, which is what `mactime` consumes — the bridge from NTFS metadata into a classic timeline. |
| `--bodyf` | bodyf | File name to save body formatted results to. When present, overrides default name | Override the generated bodyfile name. |
| `--bdl` | bdl | Drive letter (C, D, etc.) to use with bodyfile. Only the drive letter itself should be provided | Drive letter to record in the bodyfile. Required with `--body`, because a bodyfile path is meaningless without the volume it came from. |
| `--blf` | — | When true, use LF vs CRLF for newlines | Use LF rather than CRLF, when the output is going to a Unix toolchain. |
| `--dd` | dd | Directory to save exported $MFT FILE record. --do is also required when using this option | Directory to write an exported FILE record to. |
| `--do` | do | Offset of the $MFT FILE record to dump as decimal or hex. Ex: 5120 or 0x1400 Use --de or --debug to see offsets | Offset of the FILE record to dump, decimal or hex. |
| `--de` | de | Dump full details for $MFT entry/sequence #. Format is 'Entry' or 'Entry-Seq' as decimal or hex. Example: 5, 624-5 or 0x270-0x5. | Dump full detail for one entry, as `Entry` or `Entry-Seq`. The flag for interrogating a single suspicious file. |
| `--dr` | — | When true, dump $MFT resident files to dir specified by --csv or --json, in 'Resident' subdirectory. Files will be named '<EntryNumber>-<SequenceNumber>-<AttributeNumber>_<FileName>.bin' | Dump resident files out of the $MFT. Small files live entirely inside their MFT record, so this recovers content with no data runs to follow. |
| `--fls` | — | When true, displays contents of directory from $MFT specified by --de. Ignored when --de points to a file | List a directory's contents from the $MFT, for the entry given by `--de`. |
| `--ds` | ds | Dump full details for Security Id from $SDS as decimal or hex. Example: 624 or 0x270 | Dump a security descriptor from $SDS by Id — how you get from a file to the ACL that was on it. |
| `--dt` | dt | The custom date/time format to use when displaying time stamps. See https://goo.gl/CNVq0k for options [default: yyyy-MM-dd HH:mm:ss.fffffff] | Custom timestamp format for the output. |
| `--sn` | — | Include DOS file name types in $MFT output | Include DOS 8.3 short names. |
| `--fl` | — | Generate condensed file listing of parsed $MFT contents. Requires --csv | Condensed file listing instead of the full attribute dump. |
| `--at` | — | When true, include all timestamps from 0x30 attribute vs only when they differ from 0x10 in the $MFT | Include all $STANDARD_INFORMATION timestamps rather than only those that differ from $FILE_NAME. Differences between the two attribute sets are the classic timestomping signal, so include them when that is the question. |
| `--rs` | — | When true, recover slack space from FILE records when processing $MFT files. This option has no effect for $I30 files | Recover slack space from FILE records. Old entries survive in the unused tail of a record, so this reaches deleted metadata that a straight parse skips. |
| `--vss` | — | Process all Volume Shadow Copies that exist on drive specified by -f | Also parse every Volume Shadow Copy, which is where an older $MFT still holds entries the live one has reused. |
| `--dedupe` | — | Deduplicate -f & VSCs based on SHA-1. First file found wins | Drop duplicates by SHA-1 across the source and shadow copies. Use it whenever `--vss` is on. |
| `--ir` | — | Include resident data in JSON/CSV output | Include resident data inline in the output rather than as separate files. |
| `--re` | re | Comma-separated list of extensions to include for resident data (e.g., '.txt,.ps1,.bat'). If omitted, includes all | Restrict resident extraction to these extensions. |
| `--rm` | rm | Maximum size in bytes for resident data to include (max: 1024000) [default: 1024] | Cap the size of resident data included. |
| `--debug` | — | Show debug information during processing |  |
| `--trace` | — | Show trace information during processing |  |
| `-?` | — | Show help and usage information |  |
| `-h` | — | Show help and usage information |  |
| `--help` | — | Show help and usage information |  |
| `--version` | — | Show version information |  |

## Gotchas

- $MFT entries are reused. A deleted file's record is overwritten by the next file that needs it, so an entry describing a deleted file may already belong to something else — check the sequence number before asserting the two are the same file.
- $STANDARD_INFORMATION timestamps are trivially forged; $FILE_NAME timestamps are not, because they update only through the kernel. `--at` is what lets you compare them, and a mismatch is the strongest cheap indicator of timestomping.
- Parsing a live volume's $MFT copied with a normal file copy will fail — it is locked. Extract it with a forensic tool or from a shadow copy.

## See also

[`PECmd`](../windows-artifacts/PECmd.md), [`AppCompatCacheParser`](../windows-artifacts/AppCompatCacheParser.md), [`AmcacheParser`](../windows-artifacts/AmcacheParser.md)
