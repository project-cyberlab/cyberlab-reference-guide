<!-- generated-by: scripts/generate_pages.py -->
# strings

**Kit:** Base OS — present on every Linux image  **Capability:** Search raw data for a pattern; Extract strings, including obfuscated ones  **Version:** GNU strings (GNU Binutils for Debian) 2.40
**Captured:** `cyberlab-aio` via `--help` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/strings.help.txt)

## Purpose

Display printable strings in [file(s)] (stdin by default)

## Synopsis

```
strings [option(s)] [file(s)]
```

## Common invocations

_TODO: up to 8 task-titled invocations._

## Options

All 4 options parsed from the captured help text. The final column is the judgement layer and is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-n` | number | Locate & print any sequence of at least <number> | |
| `--bytes` | number | displayable characters. (The default is 4). | |
| `-o` | — | An alias for --radix=o | |
| `-U` | d\|s\|i\|x\|e\|h | Specify how to treat UTF-8 encoded unicode characters | |

## Gotchas

_TODO: operational traps._

## See also

`rafind2`, `grep`, `xxd`, `floss`, `base64dump.py`, `numbers-to-string.py`
