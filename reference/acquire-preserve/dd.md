<!-- generated-by: scripts/generate_pages.py -->
# dd

**Kit:** Base OS — present on every Linux image  **Capability:** Image a disk, volume or device  **Version:** dd (coreutils) 9.1
**Captured:** `cyberlab-aio` via `--help` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/dd.help.txt)

## Purpose

or:  dd OPTION

## Synopsis

```
dd [OPERAND]...
or:  dd OPTION
```

## Common invocations

<!-- candidates mined from cyberlab; verify each flag against the options table below before treating as reviewed -->
```
# from cyberlab 01-disk-forensics
dd if=/dev/zero of=exercise/sample.dd bs=1M count=10
# from cyberlab 51-linux-triage-workflow
dd if=/dev/zero of=triage_sample.raw bs=1M count=8
```

## Options

All 2 options parsed from the captured help text. The final column is the judgement layer and is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `--help` | — | display this help and exit | |
| `--version` | — | output version information and exit | |

## Gotchas

_TODO: operational traps._
