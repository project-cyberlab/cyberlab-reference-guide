<!-- generated-by: scripts/generate_pages.py -->
# volshell

| | |
|---|---|
| **Kit** | SIFT Workstation (Volatility 3) |
| **Capability** | Analyse a memory image |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-08 — [raw help output](../../capture/cyberlab-aio/help/volshell.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

An interactive Python shell over a memory image, with Volatility's object model loaded — for questions no plugin answers.

## When you'd reach for this

An analyst reaches for volshell when they need to interactively run plugins or execute custom scripts on a memory image, often after loading the image to extract or analyze specific data. They may use it to generate TreeGrid objects for structured data access or run snippets via rs for quick tasks, preferring it over writing full plugins due to its flexibility and direct framework access.

**Sources:** <https://github.com/volatilityfoundation/volatility3/blob/develop/doc/source/volshell.rst> · <https://volatility3.readthedocs.io/en/latest/volshell.html>

## Synopsis

```
volshell [-h] [-c CONFIG] [-e EXTEND] [-p PLUGIN_DIRS] [-s SYMBOL_DIRS]
[-v] [-o OUTPUT_DIR] [-q] [--log LOG] [-f FILE]
[--write-config] [--save-config SAVE_CONFIG] [--clear-cache]
[--cache-path CACHE_PATH] [--offline | -u URL] [-w | -l | -m]
[--single-location SINGLE_LOCATION]
[--stackers [STACKERS ...]]
```

## Options

All 38 options parsed from the captured help text; 21 reviewed with usage guidance.

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
| `-s` | SYMBOL_DIRS | Semi-colon separated list of paths to find symbols | Where to find symbol tables — the usual fix when a Linux or macOS image will not resolve. |
| `--symbol-dirs` | SYMBOL_DIRS | Semi-colon separated list of paths to find symbols | Where to find symbol tables. |
| `-v` | — | Increase output verbosity | More verbose output. |
| `--verbosity` | — | Increase output verbosity | More verbose output. |
| `-o` | OUTPUT_DIR | Directory in which to output any generated files | Directory for files written out of the shell. |
| `--output-dir` | OUTPUT_DIR | Directory in which to output any generated files | Directory for files written out of the shell. |
| `-q` | — | Remove progress feedback | Quiet. |
| `--quiet` | — | Remove progress feedback | Quiet. |
| `--log` | LOG | Log output to a file as well as the console |  |
| `-f` | FILE | Shorthand for --single-location=file:// if single- location is not defined | The memory image. |
| `--file` | FILE | Shorthand for --single-location=file:// if single- location is not defined | The memory image. |
| `--write-config` | — | Write configuration JSON file out to config.json |  |
| `--save-config` | SAVE_CONFIG | Save configuration JSON file to a file |  |
| `--clear-cache` | — | Clears out all short-term cached items | Drop cached items when results look stale. |
| `--cache-path` | CACHE_PATH | Change the default path (/root/.cache/volatility3) used to store the cache |  |
| `--offline` | — | Do not search online for additional JSON files | Never fetch symbols online. |
| `-u` | URL | Search online for ISF json files |  |
| `--remote-isf-url` | URL | Search online for ISF json files |  |
| `-w` | — | Run a Windows volshell | Treat the image as Windows. |
| `--windows` | — | Run a Windows volshell | Treat the image as Windows. |
| `-l` | — | Run a Linux volshell | Treat the image as Linux. |
| `--linux` | — | Run a Linux volshell | Treat the image as Linux. |
| `-m` | — | Run a Mac volshell | Treat the image as macOS. |
| `--mac` | — | Run a Mac volshell | Treat the image as macOS. |
| `--single-location` | SINGLE_LOCATION | Specifies a base location on which to stack |  |
| `--stackers` | STACKERS  | List of stackers |  |
| `--single-swap-locations` | SINGLE_SWAP_LOCATIONS  | Specifies a list of swap layer URIs for use with single-location |  |
| `--script` | SCRIPT | File to load and execute at start | Run a Python script against the image and drop into the shell afterwards — the repeatable form of an interactive session. |
| `--script-only` | — | Exit volshell after the script specified in --script completes | Run the script and exit. This is how an exploratory session becomes an automated one. |
| `--pid` | PID | Process ID | Enter with a process context already selected, so `cc()` is not the first thing you type. |

## Gotchas

- Reach for this when a plugin nearly answers the question but not quite. If a plugin exists, use the plugin — it is tested and this is not.
- Findings from an interactive session are not reproducible by default. Move anything that matters into `--script` so the result can be regenerated and reviewed.
- The same symbol requirement as [`volatility3`](volatility3.md) applies: without an ISF matching the exact kernel build, a Linux or macOS image will not resolve at all.

## See also

[`vol`](../memory-forensics/vol.md), [`volatility3`](../memory-forensics/volatility3.md)
