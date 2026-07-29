<!-- generated-by: scripts/generate_pages.py -->
# volatility3

**Kit:** SIFT Workstation (Volatility 3)  **Capability:** Analyse a memory image
**Captured:** `cyberlab-aio` via `--help` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/volatility3.help.txt)

## Purpose

An open-source memory forensics framework

## Synopsis

```
volatility3 [-h] [-c CONFIG] [--parallelism [{processes,threads,off}]]
[-e EXTEND] [-p PLUGIN_DIRS] [-s SYMBOL_DIRS] [-v] [-l LOG]
[-o OUTPUT_DIR] [-q] [-f FILE] [--write-config]
[--save-config SAVE_CONFIG] [--clear-cache]
[--cache-path CACHE_PATH] [--offline | -u URL]
[--filters FILTERS] [--hide-columns [HIDE_COLUMNS ...]]
```

## Common invocations

_TODO: up to 8 task-titled invocations._

## Options

All 35 options parsed from the captured help text. The final column is the judgement layer and is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-h` | — | Show this help message and exit, for specific plugin options use 'volatility3 <pluginname> --help' | |
| `--help` | — | Show this help message and exit, for specific plugin options use 'volatility3 <pluginname> --help' | |
| `-c` | CONFIG | Load the configuration from a json file | |
| `--config` | CONFIG | Load the configuration from a json file | |
| `--parallelism` | processes | Enables parallelism (defaults to off if no argument given) | |
| `-e` | EXTEND | Extend the configuration with a new (or changed) setting | |
| `--extend` | EXTEND | Extend the configuration with a new (or changed) setting | |
| `-p` | PLUGIN_DIRS | Semi-colon separated list of paths to find plugins | |
| `--plugin-dirs` | PLUGIN_DIRS | Semi-colon separated list of paths to find plugins | |
| `-s` | SYMBOL_DIRS | Semi-colon separated list of paths to find symbols | |
| `--symbol-dirs` | SYMBOL_DIRS | Semi-colon separated list of paths to find symbols | |
| `-v` | — | Increase output verbosity | |
| `--verbosity` | — | Increase output verbosity | |
| `-l` | LOG | Log output to a file as well as the console | |
| `--log` | LOG | Log output to a file as well as the console | |
| `-o` | OUTPUT_DIR | Directory in which to output any generated files | |
| `--output-dir` | OUTPUT_DIR | Directory in which to output any generated files | |
| `-q` | — | Remove progress feedback | |
| `--quiet` | — | Remove progress feedback | |
| `-f` | FILE | Shorthand for --single-location=file:// if single- location is not defined | |
| `--file` | FILE | Shorthand for --single-location=file:// if single- location is not defined | |
| `--write-config` | — | Write configuration JSON file out to config.json | |
| `--save-config` | SAVE_CONFIG | Save configuration JSON file to a file | |
| `--clear-cache` | — | Clears out all short-term cached items | |
| `--cache-path` | CACHE_PATH | Change the default path (/root/.cache/volatility3) used to store the cache | |
| `--offline` | — | Do not search online for additional JSON files | |
| `-u` | URL | Search online for ISF json files | |
| `--remote-isf-url` | URL | Search online for ISF json files | |
| `--filters` | FILTERS | List of filters to apply to the output (in the form of [+-]columname,pattern[!]) | |
| `--hide-columns` | HIDE_COLUMNS ... | Case-insensitive space separated list of prefixes to determine which columns to hide in the output if provided | |
| `-r` | RENDERER | Determines how to render the output (quick, none, csv, pretty, json, jsonl, arrow, parquet) | |
| `--renderer` | RENDERER | Determines how to render the output (quick, none, csv, pretty, json, jsonl, arrow, parquet) | |
| `--single-location` | SINGLE_LOCATION | Specifies a base location on which to stack | |
| `--stackers` | STACKERS ... | List of stackers | |
| `--single-swap-locations` | SINGLE_SWAP_LOCATIONS ... | Specifies a list of swap layer URIs for use with single-location | |

## Gotchas

_TODO: operational traps._

## See also

`vol`, `volshell`
