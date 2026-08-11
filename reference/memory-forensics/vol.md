<!-- generated-by: scripts/generate_pages.py -->
# vol

| | |
|---|---|
| **Kit** | SIFT Workstation (Volatility 3) |
| **Capability** | Analyse a memory image |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-11 — [raw help output](../../capture/cyberlab-aio/help/vol.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Extract and analyse artifacts from a memory image using Volatility 3 plugins.

## When you'd reach for this

An analyst reaches for vol when examining memory dumps to detect malicious activity, such as unusual processes or command-line arguments; they may first run plugins like `windows.pslist` or `windows.pstree` to establish context before using `windows.cmdline` or `windows.handles` for deeper analysis, as the tool's use of symbol tables ensures accurate parsing of memory structures over guesswork.

**Sources:** <https://hivesecurity.gitlab.io/blog/memory-forensics-volatility-attack-detect/> · <https://www.dfirhive.com/post/windows-memory-and-process-analysis-volatility3-walkthrough>

## Synopsis

```
vol [-h] [-c CONFIG] [--parallelism [{processes,threads,off}]]
[-e EXTEND] [-p PLUGIN_DIRS] [-s SYMBOL_DIRS] [-v] [-l LOG]
[-o OUTPUT_DIR] [-q] [-f FILE] [--write-config]
[--save-config SAVE_CONFIG] [--clear-cache]
[--cache-path CACHE_PATH] [--offline | -u URL] [--filters FILTERS]
[--hide-columns [HIDE_COLUMNS ...]] [-r RENDERER]
```

## Options

All 35 options parsed from the captured help text; 9 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-h` | — | Show this help message and exit, for specific plugin options use 'vol <pluginname> --help' |  |
| `--help` | — | Show this help message and exit, for specific plugin options use 'vol <pluginname> --help' |  |
| `-c` | CONFIG | Load the configuration from a json file | Load saved configuration from a JSON file. |
| `--config` | CONFIG | Load the configuration from a json file | Load saved configuration from a JSON file. |
| `--parallelism` | {processes,threads,off} | Enables parallelism (defaults to off if no argument given) |  |
| `-e` | EXTEND | Extend the configuration with a new (or changed) setting |  |
| `--extend` | EXTEND | Extend the configuration with a new (or changed) setting |  |
| `-p` | PLUGIN_DIRS | Semi-colon separated list of paths to find plugins | Add a directory of custom plugins. |
| `--plugin-dirs` | PLUGIN_DIRS | Semi-colon separated list of paths to find plugins | Add a directory of custom plugins. |
| `-s` | SYMBOL_DIRS | Semi-colon separated list of paths to find symbols | Point at a local symbol-table directory — the fix for an air-gapped host that cannot download symbols. |
| `--symbol-dirs` | SYMBOL_DIRS | Semi-colon separated list of paths to find symbols | Point at a local symbol-table directory — the fix for an air-gapped host that cannot download symbols. |
| `-v` | — | Increase output verbosity | Increase verbosity while diagnosing a symbol-table failure. |
| `--verbosity` | — | Increase output verbosity | Increase verbosity while diagnosing a symbol-table failure. |
| `-l` | LOG | Log output to a file as well as the console |  |
| `--log` | LOG | Log output to a file as well as the console |  |
| `-o` | OUTPUT_DIR | Directory in which to output any generated files | Directory for files the plugin dumps (processes, DLLs, files). |
| `--output-dir` | OUTPUT_DIR | Directory in which to output any generated files | Directory for files the plugin dumps (processes, DLLs, files). |
| `-q` | — | Remove progress feedback | Quiet — suppress the progress and INFO banner when scripting. |
| `--quiet` | — | Remove progress feedback | Quiet — suppress the progress and INFO banner when scripting. |
| `-f` | FILE | Shorthand for --single-location=file:// if single- location is not defined | The memory image to analyse — required for almost every plugin. |
| `--file` | FILE | Shorthand for --single-location=file:// if single- location is not defined | The memory image to analyse — required for almost every plugin. |
| `--write-config` | — | Write configuration JSON file out to config.json |  |
| `--save-config` | SAVE_CONFIG | Save configuration JSON file to a file |  |
| `--clear-cache` | — | Clears out all short-term cached items |  |
| `--cache-path` | CACHE_PATH | Change the default path (/root/.cache/volatility3) used to store the cache |  |
| `--offline` | — | Do not search online for additional JSON files | Never attempt a network fetch for symbols. Use this on evidence networks so a scan cannot stall on a download. |
| `-u` | URL | Search online for ISF json files |  |
| `--remote-isf-url` | URL | Search online for ISF json files |  |
| `--filters` | FILTERS | List of filters to apply to the output (in the form of [+-]columname,pattern[!]) |  |
| `--hide-columns` | HIDE_COLUMNS  | Case-insensitive space separated list of prefixes to determine which columns to hide in the output if provided |  |
| `-r` | RENDERER | Determines how to render the output (quick, none, csv, pretty, json, jsonl, arrow, parquet) | Choose the renderer: `csv`/`json` when feeding another tool. |
| `--renderer` | RENDERER | Determines how to render the output (quick, none, csv, pretty, json, jsonl, arrow, parquet) | Choose the renderer: `csv`/`json` when feeding another tool. |
| `--single-location` | SINGLE_LOCATION | Specifies a base location on which to stack |  |
| `--stackers` | STACKERS  | List of stackers |  |
| `--single-swap-locations` | SINGLE_SWAP_LOCATIONS  | Specifies a list of swap layer URIs for use with single-location |  |

## Gotchas

- **Timeout-guard `vol` in any harness.** On a synthetic or truncated memory image it has pinned a core at 99% indefinitely on this project. Never run it unbounded in an automated pass.
- Volatility 3 takes plugin names, not v2 syntax: `windows.pslist`, not `--profile=... pslist`. Most 'plugin not found' errors are pasted v2 commands.
- The first run against an unfamiliar image downloads symbol tables. On an isolated network that hangs — pre-stage symbols and use `--offline`.

## See also

[`volatility3`](../memory-forensics/volatility3.md), [`volshell`](../memory-forensics/volshell.md)
