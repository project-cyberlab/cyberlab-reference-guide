<!-- generated-by: scripts/generate_pages.py -->
# vivbin

| | |
|---|---|
| **Kit** | REMnux |
| **Capability** | Disassemble and explore a binary |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-02 — [raw help output](../../capture/cyberlab-aio/help/vivbin.help.txt) |
| **Documentation** | <https://github.com/vivisect/vivisect> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Statically examine and emulate binary files.

## Synopsis

```
vivbin [options] <workspace|binaries...>
```

## Options

All 34 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-h` | — | show this help message and exit |  |
| `--help` | — | show this help message and exit |  |
| `-M` | MODNAME | run the file listed as an analysis module in non-gui mode and exit |  |
| `--module` | MODNAME | run the file listed as an analysis module in non-gui mode and exit |  |
| `-A` | — | Do *not* do an initial auto-analysis pass |  |
| `--skip-analysis` | — | Do *not* do an initial auto-analysis pass |  |
| `-B` | — | Do *not* start the gui, just load, analyze and save |  |
| `--bulk` | — | Do *not* start the gui, just load, analyze and save |  |
| `-C` | — | Output vivisect performace profiling (cProfile) info |  |
| `--cprofile` | — | Output vivisect performace profiling (cProfile) info |  |
| `-E` | ENTRYPOINTS | Add Entry Point for bulk analysis (can have multiple "-E <addr>" args |  |
| `--entrypoint` | ENTRYPOINTS | Add Entry Point for bulk analysis (can have multiple "-E <addr>" args |  |
| `-O` | OPTION | <secname>.<optname>=<optval> (optval must be json syntax) |  |
| `--option` | OPTION | <secname>.<optname>=<optval> (optval must be json syntax) |  |
| `-p` | PARSEMOD | Manually specify the parser module (pe/elf/blob/...) |  |
| `--parser` | PARSEMOD | Manually specify the parser module (pe/elf/blob/...) |  |
| `-s` | STORAGE_NAME | Specify a storage module by name |  |
| `--storage` | STORAGE_NAME | Specify a storage module by name |  |
| `-S` | — | Run Vivisect Server. Last argument should be the VivWorkspaces directory. |  |
| `--server` | — | Run Vivisect Server. Last argument should be the VivWorkspaces directory. |  |
| `-P` | SERVER_PORT | Port to run Vivisect Server on (only meaningful with --server) |  |
| `--port` | SERVER_PORT | Port to run Vivisect Server on (only meaningful with --server) |  |
| `-v` | — | Enable verbose mode (multiples matter: -vvvv) |  |
| `--verbose` | — | Enable verbose mode (multiples matter: -vvvv) |  |
| `-V` | VERSION | Add file version (if available) to save file name |  |
| `--version` | VERSION | Add file version (if available) to save file name |  |
| `-c` | CONFIG | Path to a directory to use for config data |  |
| `--config` | CONFIG | Path to a directory to use for config data |  |
| `-a` | — | Autosave configuration data |  |
| `--autosave` | — | Autosave configuration data |  |
| `-o` | OUTFILE | Name of VivWorkspace file to create (useful for loading multiple binaries into one workspace) |  |
| `--outfile` | OUTFILE | Name of VivWorkspace file to create (useful for loading multiple binaries into one workspace) |  |
| `-m` | — | List Architectures and their version/maturity |  |
| `--archmaturity` | — | List Architectures and their version/maturity |  |

## Gotchas

_TODO: operational traps._

## See also

[`r2`](../reverse-engineering/r2.md), [`rabin2`](../malware-triage-static/rabin2.md), [`rasm2`](../reverse-engineering/rasm2.md), [`objdump`](../malware-triage-static/objdump.md), [`vdbbin`](../reverse-engineering/vdbbin.md)
