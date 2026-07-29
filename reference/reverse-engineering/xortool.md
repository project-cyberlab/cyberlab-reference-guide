<!-- generated-by: scripts/generate_pages.py -->
# xortool

**Kit:** REMnux  **Capability:** Analyse shellcode; Break simple obfuscation  **Version:** 1.1.0
**Captured:** `cyberlab-aio` via `--help` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/xortool.help.txt)  **Docs:** <https://github.com/hellman/xortool>

## Purpose

Analyze XOR-encoded data.

## Synopsis

```
xortool [-x] [-m MAX-LEN] [-f] [-t CHARSET] [FILE]
xortool [-x] [-l LEN] [-c CHAR | -b | -o] [-f] [-t CHARSET] [-p PLAIN] [-r PERCENT] [FILE]
xortool [-x] [-m MAX-LEN| -l LEN] [-c CHAR | -b | -o] [-f] [-t CHARSET] [-p PLAIN] [-r PERCENT] [FILE]
xortool [-h | --help]
xortool --version
```

## Common invocations

<!-- candidates mined from cyberlab; verify each flag against the options table below before treating as reviewed -->
```
# from cyberlab 09-deobfuscation
xortool --version
# from cyberlab 09-deobfuscation
xortool -c 20 exercise/encoded_payload.bin
```

## Options

All 8 options parsed from the captured help text. The final column is the judgement layer and is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-l` | LEN | length of the key | |
| `--key-length` | LEN | length of the key | |
| `-m` | MAX-LEN | maximum key length to probe [default: 65] | |
| `--max-keylen` | MAX-LEN | maximum key length to probe [default: 65] | |
| `-c` | CHAR | most frequent char (one char or hex code) | |
| `--char` | CHAR | most frequent char (one char or hex code) | |
| `-r` | PERCENT | threshold validity percentage [default: 95] | |
| `--threshold` | PERCENT | threshold validity percentage [default: 95] | |

## Gotchas

_TODO: operational traps._

## See also

`rasm2`, `floss`, `xlmdeobfuscator`
