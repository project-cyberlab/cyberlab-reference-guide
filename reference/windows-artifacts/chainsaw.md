<!-- generated-by: scripts/generate_pages.py -->
# chainsaw

**Kit:** SIFT / Security Onion (Sigma-based log hunting)  **Capability:** Parse Windows event logs  **Version:** chainsaw 2.16.0
**Captured:** `cyberlab-aio` via `--help` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/chainsaw.help.txt)

## Purpose

Rapidly work with Forensic Artefacts

## Synopsis

```
chainsaw [OPTIONS] <COMMAND>
```

## Common invocations

<!-- candidates mined from cyberlab; verify each flag against the options table below before treating as reviewed -->
```
# from cyberlab 58-eventlog-hunting
chainsaw hunt Security_sample.evtx -s sigma/ --mapping mapping.yml
```

## Options

All 6 options parsed from the captured help text. The final column is the judgement layer and is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `--no-banner` | — | Hide Chainsaw's banner | |
| `--num-threads` | NUM_THREADS | Limit the thread number (default: num of CPUs) | |
| `-h` | — | Print help | |
| `--help` | — | Print help | |
| `-V` | — | Print version | |
| `--version` | — | Print version | |

## Gotchas

_TODO: operational traps._

## See also

`evtxexport`, `evtxinfo`, `EvtxECmd`, `hayabusa`
