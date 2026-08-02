<!-- generated-by: scripts/generate_pages.py -->
# xortool

| | |
|---|---|
| **Kit** | REMnux |
| **Capability** | Analyse shellcode; Break simple obfuscation |
| **Version** | 1.1.0 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-02 — [raw help output](../../capture/cyberlab-aio/help/xortool.help.txt) |
| **Documentation** | <https://github.com/hellman/xortool> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Recover the key length and key of an XOR-encrypted file by frequency analysis.

## Synopsis

```
xortool [-x] [-m MAX-LEN] [-f] [-t CHARSET] [FILE]
xortool [-x] [-l LEN] [-c CHAR | -b | -o] [-f] [-t CHARSET] [-p PLAIN] [-r PERCENT] [FILE]
xortool [-x] [-m MAX-LEN| -l LEN] [-c CHAR | -b | -o] [-f] [-t CHARSET] [-p PLAIN] [-r PERCENT] [FILE]
xortool [-h | --help]
xortool --version
```

## Options

All 20 options parsed from the captured help text; 4 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-x` | — | input is hex-encoded str |  |
| `--hex` | — | input is hex-encoded str |  |
| `-l` | LEN | length of the key | Fix the key length when you already know it. |
| `--key-length` | LEN | length of the key | Fix the key length when you already know it. |
| `-m` | MAX-LEN | maximum key length to probe [default: 65] | Maximum key length to consider. |
| `--max-keylen` | MAX-LEN | maximum key length to probe [default: 65] | Maximum key length to consider. |
| `-c` | CHAR | most frequent char (one char or hex code) | Give the most frequent character of the plaintext — usually `20` (space) for text, `00` for binaries. This is the flag that makes or breaks the attack. |
| `--char` | CHAR | most frequent char (one char or hex code) | Give the most frequent character of the plaintext — usually `20` (space) for text, `00` for binaries. This is the flag that makes or breaks the attack. |
| `-b` | — | brute force all possible most frequent chars | Brute-force the most frequent character rather than guessing. |
| `--brute-chars` | — | brute force all possible most frequent chars | Brute-force the most frequent character rather than guessing. |
| `-o` | — | same as -b but will only check printable chars |  |
| `--brute-printable` | — | same as -b but will only check printable chars |  |
| `-f` | — | filter outputs based on the charset |  |
| `--filter-output` | — | filter outputs based on the charset |  |
| `-p` | PLAIN | use known plaintext for decoding |  |
| `--known-plaintext` | PLAIN | use known plaintext for decoding |  |
| `-r` | PERCENT | threshold validity percentage [default: 95] |  |
| `--threshold` | PERCENT | threshold validity percentage [default: 95] |  |
| `-h` | — | show this help |  |
| `--help` | — | show this help |  |

## Gotchas

- Output lands in an `xortool_out/` directory, not stdout. People routinely think it did nothing.
- `-c 00` is right far more often than the default for packed binaries, because null padding dominates.

## See also

[`rasm2`](../reverse-engineering/rasm2.md), [`floss`](../malware-triage-static/floss.md), [`xlmdeobfuscator`](../malware-triage-documents/xlmdeobfuscator.md)
