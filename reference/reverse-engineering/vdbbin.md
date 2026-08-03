<!-- generated-by: scripts/generate_pages.py -->
# vdbbin

| | |
|---|---|
| **Kit** | REMnux |
| **Capability** | Disassemble and explore a binary |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-03 — [raw help output](../../capture/cyberlab-aio/help/vdbbin.help.txt) |
| **Documentation** | <https://github.com/vivisect/vivisect> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Statically examine and emulate binary files.

## Synopsis

```
vdbbin [options] [platformopt=foo, ...]
```

## Options

All 27 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-h` | — | show this help message and exit |  |
| `--help` | — | show this help message and exit |  |
| `-c` | COMMAND | Debug a fired command |  |
| `--cmd` | COMMAND | Debug a fired command |  |
| `-p` | PROCESS | Attach to process by name or pid |  |
| `--process` | PROCESS | Attach to process by name or pid |  |
| `-Q` | — | Run the QT gui |  |
| `--qt` | — | Run the QT gui |  |
| `-R` | REMOTEHOST | Attach to remote VDB server |  |
| `--remote` | REMOTEHOST | Attach to remote VDB server |  |
| `-r` | — | Do not stop on attach |  |
| `--run` | — | Do not stop on attach |  |
| `-s` | SNAPSHOT | Load a vtrace snapshot file |  |
| `--snapshot` | SNAPSHOT | Load a vtrace snapshot file |  |
| `-S` | — | — |  |
| `--server` | — | — |  |
| `-v` | — | — |  |
| `--verbose` | — | — |  |
| `-t` | TARGET | Activate special vdb target ( -t ? for list ) |  |
| `--target` | TARGET | Activate special vdb target ( -t ? for list ) |  |
| `--android` | — | Debug Android with ADB! |  |
| `-e` | EVENTID | Used for Windows JIT |  |
| `--eventid` | EVENTID | Used for Windows JIT |  |
| `-w` | WAITFOR | Wait for process with name |  |
| `--waitfor` | WAITFOR | Wait for process with name |  |
| `--LI` | — | Breakpoint on Library initialization |  |
| `--LL` | — | Breakpoint on Library load time |  |

## Gotchas

_TODO: operational traps._

## See also

[`r2`](../reverse-engineering/r2.md), [`rabin2`](../malware-triage-static/rabin2.md), [`rasm2`](../reverse-engineering/rasm2.md), [`objdump`](../malware-triage-static/objdump.md), [`vivbin`](../reverse-engineering/vivbin.md)
