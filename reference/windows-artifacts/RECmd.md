<!-- generated-by: scripts/generate_pages.py -->
# RECmd

| | |
|---|---|
| **Kit** | FLARE-VM / SIFT (Eric Zimmerman tools) |
| **Capability** | Parse registry hives |
| **Version** | 2026.5.0 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-09 — [raw help output](../../capture/cyberlab-aio/help/RECmd.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Query and export Windows registry hives from the command line, using batch files of plugin definitions to pull known-interesting keys in one pass. The batch approach is the point: it turns 'check the usual persistence locations' into one reproducible command.

## When you'd reach for this

An analyst reaches for RECmd during incident triage after checking event logs, file system changes, and amcache data to investigate persistence mechanisms like Run keys, services, or tasks; they use it alongside tools like EvtxECmd and MFTECmd to build a timeline of suspicious activity, as RECmd specifically targets registry artifacts for persistence analysis.

**Sources:** <https://ridgelinecyber.com/resources/kape-ez-tools/> · <https://ridgelinecyber.com/training/modules/free/ir01-toolkit-setup/03-eztools/>

## Synopsis

```
RECmd [options]
```

## Options

All 33 options parsed from the captured help text; 4 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-f` | f | Hive to search. -f or -d is required | An analyst would use the -f flag when processing a single registry hive file against a specific rule file to extract forensic artifacts. |
| `-d` | d | Directory to look for hives (recursively). -f or -d is required | An analyst would use the -d flag with RECmd when batch-processing hives against a community ruleset to extract forensic values like RunOnce persistence or user activity from the registry. |
| `--kn` | kn | Display details for key name. Includes subkeys and values |  |
| `--vn` | vn | Value name. Only this value will be dumped |  |
| `--bn` | bn | Use settings from supplied file to find keys/values. See included sample file for examples |  |
| `--csv` | csv | Directory to save CSV formatted results to. Be sure to include the full path in double quotes | An analyst would use the --csv flag when batch-processing registry hives against the community ruleset to generate structured CSV output for forensic analysis of persistence mechanisms, user activity, and system configuration details. |
| `--csvf` | csvf | File name to save CSV formatted results to. When present, overrides default name | An analyst would use the --csvf flag when processing registry hives with RECmd to generate a CSV output file for further analysis or documentation during a forensic investigation. |
| `--saveTo` | saveTo | Saves --vn value data in binary form to file. Expects path to a FILE |  |
| `--json` | json | Directory to save JSON formatted results to. Be sure to include the full path in double quotes |  |
| `--jsonf` | jsonf | File name to save JSON formatted results to. When present, overrides default name |  |
| `--details` | — | Show more details when displaying results |  |
| `--base64` | base64 | Find Base64 encoded values with size >= Base64 (specified in bytes) |  |
| `--minSize` | minSize | Find values with data size >= MinSize (specified in bytes) |  |
| `--sa` | sa | Search for <string> in keys, values, data, and slack |  |
| `--sk` | sk | Search for <string> in value record's key names |  |
| `--sv` | sv | Search for <string> in value record's value names |  |
| `--sd` | sd | Search for <string> in value record's value data |  |
| `--ss` | ss | Search for <string> in value record's value slack |  |
| `--literal` | — | If true, --sd and --ss search value will not be interpreted as ASCII or Unicode byte strings |  |
| `--nd` | — | If true, do not show data when using --sd or --ss |  |
| `--regex` | — | If present, treat <string> in --sk, --sv, --sd, and --ss as a regular expression |  |
| `--dt` | dt | The custom date/time format to use when displaying time stamps. See https://goo.gl/CNVq0k for options [default: yyyy-MM-dd HH:mm:ss.fffffff] |  |
| `--nl` | — | When true, allow transaction log files to not exist for dirty hives |  |
| `--recover` | — | If true, recover deleted keys/values. Default is true |  |
| `--vss` | — | Process all Volume Shadow Copies that exist on drive specified by -f or -d |  |
| `--dedupe` | — | Deduplicate -f or -d & VSCs based on SHA-1. First file found wins |  |
| `--sync` | — | If true, the latest batch files from https://github.com/EricZimmerman/RECmd/tree/master/BatchExamples are downloaded and local files updated |  |
| `--debug` | — | Show debug information during processing |  |
| `--trace` | — | Show trace information during processing |  |
| `-?` | — | Show help and usage information |  |
| `-h` | — | Show help and usage information |  |
| `--help` | — | Show help and usage information |  |
| `--version` | — | Show version information |  |

## Gotchas

_TODO: operational traps._

## See also

[`rip.pl`](../windows-artifacts/rip.pl.md), [`regripper`](../windows-artifacts/regripper.md), [`hivexsh`](../windows-artifacts/hivexsh.md), [`regfexport`](../windows-artifacts/regfexport.md), [`regfinfo`](../windows-artifacts/regfinfo.md), [`regfmount`](../windows-artifacts/regfmount.md), [`regipy-dump`](../windows-artifacts/regipy-dump.md), [`regipy-parse-header`](../windows-artifacts/regipy-parse-header.md)
