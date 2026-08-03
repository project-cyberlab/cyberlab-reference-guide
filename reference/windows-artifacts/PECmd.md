<!-- generated-by: scripts/generate_pages.py -->
# PECmd

| | |
|---|---|
| **Kit** | FLARE-VM / SIFT (Eric Zimmerman tools) |
| **Capability** | Parse execution and persistence artifacts |
| **Version** | 2026.5.0 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-03 — [raw help output](../../capture/cyberlab-aio/help/PECmd.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Parse Windows Prefetch files into evidence of what executed, when, how often, and which files each run touched.

## Synopsis

```
PECmd [options]
```

## Options

All 20 options parsed from the captured help text; 14 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-f` | f | File to process. Either this or -d is required | A single .pf file, when chasing one binary. |
| `-d` | d | Directory to recursively process. Either this or -f is required | Recurse a directory — the normal mode, since Prefetch is only meaningful as a set. Point it at `C:\Windows\Prefetch`. |
| `-k` | k | Comma separated list of keywords to highlight in output. By default, 'temp' and 'tmp' are highlighted. Any additional keywords will be added to these | Highlight extra keywords in the output. `temp` and `tmp` are highlighted by default; add the names you are hunting. |
| `-o` | o | When specified, save prefetch file bytes to the given path. Useful to look at decompressed Win10 files | Save the decompressed Prefetch bytes. Win10+ Prefetch is MAM-compressed, so this is how you get something another tool or a hex editor can read. |
| `-q` | — | Do not dump full details about each file processed. Speeds up processing when using --json or --csv | Suppress the per-file detail. Worth it on a large directory when the CSV is the real output. |
| `--csv` | csv | Directory to save CSV formatted results to. Be sure to include the full path in double quotes | Write CSV to a directory. This is the output that matters: Prefetch is a timeline source, and Timeline Explorer or a spreadsheet is where the pattern shows up. |
| `--csvf` | csvf | File name to save CSV formatted results to. When present, overrides default name | Override the generated CSV filename. |
| `--json` | json | Directory to save JSON formatted results to. Be sure to include the full path in double quotes | JSON output, when the results feed another tool. |
| `--jsonf` | jsonf | File name to save JSON formatted results to. When present, overrides default name | Override the generated JSON filename. |
| `--html` | html | Directory to save xhtml formatted results to. Be sure to include the full path in double quotes | XHTML report, for handing to someone who will not open a CSV. |
| `--dt` | dt | The custom date/time format to use when displaying time stamps. See https://goo.gl/CNVq0k for options [default: yyyy-MM-dd HH:mm:ss] | Custom timestamp format for the output. |
| `--mp` | — | When true, display higher precision for timestamps | Higher-precision timestamps, when ordering events within the same second matters. |
| `--vss` | — | Process all Volume Shadow Copies that exist on drive specified by -f or -d | Also parse every Volume Shadow Copy on the drive. Prefetch rolls over at 1024 entries on Win10+, so shadow copies are often the only place an older execution still exists. |
| `--dedupe` | — | Deduplicate -f or -d & VSCs based on SHA-1. First file found wins | Drop duplicates by SHA-1 across the source and the shadow copies. Effectively mandatory with `--vss`, which otherwise returns the same file many times over. |
| `--debug` | — | Show debug information during processing |  |
| `--trace` | — | Show trace information during processing |  |
| `-?` | — | Show help and usage information |  |
| `-h` | — | Show help and usage information |  |
| `--help` | — | Show help and usage information |  |
| `--version` | — | Show version information |  |

## Gotchas

- Prefetch proves a program **ran**; it does not prove who ran it or what it did. Pair it with event logs or [`AmcacheParser`](AmcacheParser.md) before attributing anything.
- Absence is not evidence of absence. Prefetch can be disabled, is commonly off on SSD-era server builds, and rolls over — a missing entry means nothing on its own.
- The last-run timestamps are the eight most recent executions only. Older runs are gone from the file even though the run count keeps counting them.

## See also

[`AppCompatCacheParser`](../windows-artifacts/AppCompatCacheParser.md), [`MFTECmd`](../windows-artifacts/MFTECmd.md), [`AmcacheParser`](../windows-artifacts/AmcacheParser.md)
