<!-- generated-by: scripts/generate_pages.py -->
# strings

**Kit:** Base OS — present on every Linux image  **Capability:** Search raw data for a pattern; Extract strings, including obfuscated ones  **Version:** GNU strings (GNU Binutils for Debian) 2.40
**Captured:** `cyberlab-aio` via `--help` on 2026-08-01  [raw](../../capture/cyberlab-aio/help/strings.help.txt)

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Print sequences of printable characters found in a binary file.

## Synopsis

```
strings [option(s)] [file(s)]
```

## Common invocations

_TODO: up to 8 task-titled invocations._

## Options

All 14 options parsed from the captured help text; 3 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-d` | — | Only scan the data sections in the file |  |
| `--data` | — | Only scan the data sections in the file |  |
| `-f` | — | Print the name of the file before each string |  |
| `--print-file-name` | — | Print the name of the file before each string |  |
| `-n` | number | Locate & print any sequence of at least <number> | Minimum length. Default 4 is noisy; 8–10 cuts most false hits. |
| `--bytes` | number | displayable characters. (The default is 4). |  |
| `-t` | o,d,x | Print the location of the string in base 8, 10 or 16 |  |
| `--radix` | o,d,x | Print the location of the string in base 8, 10 or 16 |  |
| `-o` | — | An alias for --radix=o | Print the byte offset of each string — lets you seek back to it. |
| `-T` | — | Specify the binary file format |  |
| `--target` | BFDNAME | Specify the binary file format |  |
| `-U` | d\|s\|i\|x\|e\|h | Specify how to treat UTF-8 encoded unicode characters | Control how unicode is handled; needed for UTF-16 Windows strings. |
| `-h` | — | Display this information |  |
| `--help` | — | Display this information |  |

## Gotchas

- GNU `strings` reads only initialised, loaded sections by default. Use `-a` to scan the whole file — malware routinely hides outside them.
- It finds ASCII by default and will miss UTF-16LE strings that Windows binaries are full of. When a PE looks empty, that is usually why — reach for [`floss`](../malware-triage-static/floss.md) instead.

## See also

[`rafind2`](../examine-the-filesystem/rafind2.md), [`grep`](../examine-the-filesystem/grep.md), [`xxd`](../examine-the-filesystem/xxd.md), [`floss`](../malware-triage-static/floss.md), [`base64dump.py`](../malware-triage-static/base64dump.py.md), [`numbers-to-string.py`](../malware-triage-static/numbers-to-string.py.md)
