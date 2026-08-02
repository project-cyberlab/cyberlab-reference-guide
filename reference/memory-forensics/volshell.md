<!-- generated-by: scripts/generate_pages.py -->
# volshell

**Kit:** SIFT Workstation (Volatility 3)  **Capability:** Analyse a memory image
**Captured:** `cyberlab-aio` via `--help` on 2026-08-02  [raw](../../capture/cyberlab-aio/help/volshell.help.txt)

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Volshell (Volatility 3 Framework) 2.28.0

## Synopsis

```
volshell [-h] [-c CONFIG] [-e EXTEND] [-p PLUGIN_DIRS] [-s SYMBOL_DIRS]
[-v] [-o OUTPUT_DIR] [-q] [--log LOG] [-f FILE]
[--write-config] [--save-config SAVE_CONFIG] [--clear-cache]
[--cache-path CACHE_PATH] [--offline | -u URL] [-w | -l | -m]
[--single-location SINGLE_LOCATION]
[--stackers [STACKERS ...]]
```

## Common invocations

_TODO: up to 8 task-titled invocations._

## Options

All 38 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-h` | — | show this help message and exit |  |
| `--help` | — | show this help message and exit |  |
| `-c` | CONFIG | Load the configuration from a json file |  |
| `--config` | CONFIG | Load the configuration from a json file |  |
| `-e` | EXTEND | Extend the configuration with a new (or changed) setting |  |
| `--extend` | EXTEND | Extend the configuration with a new (or changed) setting |  |
| `-p` | PLUGIN_DIRS | Semi-colon separated list of paths to find plugins |  |
| `--plugin-dirs` | PLUGIN_DIRS | Semi-colon separated list of paths to find plugins |  |
| `-s` | SYMBOL_DIRS | Semi-colon separated list of paths to find symbols |  |
| `--symbol-dirs` | SYMBOL_DIRS | Semi-colon separated list of paths to find symbols |  |
| `-v` | — | Increase output verbosity |  |
| `--verbosity` | — | Increase output verbosity |  |
| `-o` | OUTPUT_DIR | Directory in which to output any generated files |  |
| `--output-dir` | OUTPUT_DIR | Directory in which to output any generated files |  |
| `-q` | — | Remove progress feedback |  |
| `--quiet` | — | Remove progress feedback |  |
| `--log` | LOG | Log output to a file as well as the console |  |
| `-f` | FILE | Shorthand for --single-location=file:// if single- location is not defined |  |
| `--file` | FILE | Shorthand for --single-location=file:// if single- location is not defined |  |
| `--write-config` | — | Write configuration JSON file out to config.json |  |
| `--save-config` | SAVE_CONFIG | Save configuration JSON file to a file |  |
| `--clear-cache` | — | Clears out all short-term cached items |  |
| `--cache-path` | CACHE_PATH | Change the default path (/root/.cache/volatility3) used to store the cache |  |
| `--offline` | — | Do not search online for additional JSON files |  |
| `-u` | URL | Search online for ISF json files |  |
| `--remote-isf-url` | URL | Search online for ISF json files |  |
| `-w` | — | Run a Windows volshell |  |
| `--windows` | — | Run a Windows volshell |  |
| `-l` | — | Run a Linux volshell |  |
| `--linux` | — | Run a Linux volshell |  |
| `-m` | — | Run a Mac volshell |  |
| `--mac` | — | Run a Mac volshell |  |
| `--single-location` | SINGLE_LOCATION | Specifies a base location on which to stack |  |
| `--stackers` | STACKERS ... | List of stackers |  |
| `--single-swap-locations` | SINGLE_SWAP_LOCATIONS ... | Specifies a list of swap layer URIs for use with single-location |  |
| `--script` | SCRIPT | File to load and execute at start |  |
| `--script-only` | — | Exit volshell after the script specified in --script completes |  |
| `--pid` | PID | Process ID |  |

## Gotchas

_TODO: operational traps._

## See also

[`vol`](../memory-forensics/vol.md), [`volatility3`](../memory-forensics/volatility3.md)
