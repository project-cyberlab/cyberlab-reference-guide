<!-- generated-by: scripts/generate_pages.py -->
# volatility3

| | |
|---|---|
| **Kit** | SIFT Workstation (Volatility 3) |
| **Capability** | Analyse a memory image |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-09 — [raw help output](../../capture/cyberlab-aio/help/volatility3.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Analyse a memory image. These are the framework-wide options; each plugin adds its own, shown by `volatility3 <plugin> --help`.

## Synopsis

```
volatility3 [-h] [-c CONFIG] [--parallelism [{processes,threads,off}]]
[-e EXTEND] [-p PLUGIN_DIRS] [-s SYMBOL_DIRS] [-v] [-l LOG]
[-o OUTPUT_DIR] [-q] [-f FILE] [--write-config]
[--save-config SAVE_CONFIG] [--clear-cache]
[--cache-path CACHE_PATH] [--offline | -u URL]
[--filters FILTERS] [--hide-columns [HIDE_COLUMNS ...]]
```

## Options

All 35 options parsed from the captured help text; 33 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-h` | — | Show this help message and exit, for specific plugin options use 'volatility3 <pluginname> --help' |  |
| `--help` | — | Show this help message and exit, for specific plugin options use 'volatility3 <pluginname> --help' |  |
| `-c` | CONFIG | Load the configuration from a json file | Load options from a JSON config. |
| `--config` | CONFIG | Load the configuration from a json file | Load options from a JSON config. |
| `--parallelism` | {processes,threads,off} | Enables parallelism (defaults to off if no argument given) | Enable process or thread parallelism. Off by default, and worth turning on for a long scan. |
| `-e` | EXTEND | Extend the configuration with a new (or changed) setting | Override a single configuration setting. |
| `--extend` | EXTEND | Extend the configuration with a new (or changed) setting | Override a single configuration setting. |
| `-p` | PLUGIN_DIRS | Semi-colon separated list of paths to find plugins | Additional plugin directories, for plugins outside the tree. |
| `--plugin-dirs` | PLUGIN_DIRS | Semi-colon separated list of paths to find plugins | Additional plugin directories. |
| `-s` | SYMBOL_DIRS | Semi-colon separated list of paths to find symbols | Where to find symbol tables. The usual fix when a Linux or macOS image will not resolve: the ISF for that exact kernel has to be reachable. |
| `--symbol-dirs` | SYMBOL_DIRS | Semi-colon separated list of paths to find symbols | Where to find symbol tables — the usual fix when a Linux or macOS image will not resolve. |
| `-v` | — | Increase output verbosity | More verbose output; repeat for more. |
| `--verbosity` | — | Increase output verbosity | More verbose output; repeat for more. |
| `-l` | LOG | Log output to a file as well as the console | Also write output to a log file. |
| `--log` | LOG | Log output to a file as well as the console | Also write output to a log file. |
| `-o` | OUTPUT_DIR | Directory in which to output any generated files | Directory for files the plugin writes — dumped processes, extracted DLLs. Required before any `--dump` plugin option does anything useful. |
| `--output-dir` | OUTPUT_DIR | Directory in which to output any generated files | Directory for files the plugin writes. Required before any `--dump` plugin option is useful. |
| `-q` | — | Remove progress feedback | Suppress progress feedback, for scripted runs. |
| `--quiet` | — | Remove progress feedback | Suppress progress feedback, for scripted runs. |
| `-f` | FILE | Shorthand for --single-location=file:// if single- location is not defined | The memory image. Almost every invocation starts here. |
| `--file` | FILE | Shorthand for --single-location=file:// if single- location is not defined | The memory image. Almost every invocation starts here. |
| `--write-config` | — | Write configuration JSON file out to config.json | Write the resolved configuration to config.json — useful for making a complex run reproducible. |
| `--save-config` | SAVE_CONFIG | Save configuration JSON file to a file | Write the resolved configuration to a named file. |
| `--clear-cache` | — | Clears out all short-term cached items | Drop cached items. First thing to try when results look stale or an image was replaced in place. |
| `--cache-path` | CACHE_PATH | Change the default path (/root/.cache/volatility3) used to store the cache | Move the cache somewhere with room; it grows. |
| `--offline` | — | Do not search online for additional JSON files | Never fetch symbols online. Use it on an analysis host that must not touch the network, and expect failures unless the ISFs are already local. |
| `-u` | URL | Search online for ISF json files | Point at an alternative ISF repository. |
| `--remote-isf-url` | URL | Search online for ISF json files | Point at an alternative ISF repository. |
| `--filters` | FILTERS | List of filters to apply to the output (in the form of [+-]columname,pattern[!]) | Filter rows as `[+-]column,pattern`, so a plugin that returns thousands of rows can be narrowed without a second pass. |
| `--hide-columns` | HIDE_COLUMNS  | Case-insensitive space separated list of prefixes to determine which columns to hide in the output if provided | Drop columns from the output to keep a wide table readable. |
| `-r` | RENDERER | Determines how to render the output (quick, none, csv, pretty, json, jsonl, arrow, parquet) | Output renderer. `csv` or `jsonl` when the result feeds another tool; `pretty` is for reading, not for parsing. |
| `--renderer` | RENDERER | Determines how to render the output (quick, none, csv, pretty, json, jsonl, arrow, parquet) | Output renderer. `csv` or `jsonl` when the result feeds another tool; `pretty` is for reading. |
| `--single-location` | SINGLE_LOCATION | Specifies a base location on which to stack | The image URI, when it is not a plain local file (`-f` is shorthand for this). |
| `--stackers` | STACKERS  | List of stackers | Control the layer stackers used to interpret the image. |
| `--single-swap-locations` | SINGLE_SWAP_LOCATIONS  | Specifies a list of swap layer URIs for use with single-location | Supply swap files alongside the image, so paged-out memory can be resolved. |

## Gotchas

- Symbols are the usual failure, not the image. Windows profiles are generated automatically, but Linux and macOS need an ISF matching the exact kernel build — same version is not enough.
- Volatility 3 dropped the Volatility 2 profile system entirely, so `--profile` from older notes and blog posts does not exist here.
- It has pinned CPU indefinitely on a malformed image before. Run long analyses under a timeout rather than assuming progress.

## See also

[`vol`](../memory-forensics/vol.md), [`volshell`](../memory-forensics/volshell.md)
