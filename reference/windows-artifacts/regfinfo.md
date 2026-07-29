<!-- generated-by: scripts/generate_pages.py -->
# regfinfo

**Kit:** SIFT Workstation (libyal)  **Capability:** Parse registry hives
**Captured:** `cyberlab-aio` via `--help` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/regfinfo.help.txt)

## Purpose

Invalid argument: regfinfo

## Synopsis

```
regfinfo [ -B bodyfile ] [ -c codepage ] [ -hHvV ] source
```

## Common invocations

<!-- candidates mined from cyberlab; verify each flag against the options table below before treating as reviewed -->
```
# from cyberlab 04-registry-analysis
regfinfo -V
# from cyberlab 04-registry-analysis
regfinfo exercise/SYSTEM_sample.hive
# from cyberlab 04-registry-analysis
regfinfo /tmp/SYSTEM_recovered.hive
```

## Options

All 6 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-B` | — | output key and value hierarchy as a bodyfile |  |
| `-c` | — | codepage of ASCII strings, options: ascii, windows-874, windows-932, windows-936, windows-949, windows-950, windows-1250, windows-1251, windows-1252 (default), windows-1253, windows-1254, windows-1255 |  |
| `-h` | — | shows this help |  |
| `-H` | — | shows the key and value hierarchy |  |
| `-v` | — | verbose output to stderr |  |
| `-V` | — | print version |  |

## Gotchas

_TODO: operational traps._

## See also

`rip.pl`, `regripper`, `hivexsh`, `regfexport`, `regfmount`, `regipy-dump`, `regipy-parse-header`, `regipy-plugins-run`
