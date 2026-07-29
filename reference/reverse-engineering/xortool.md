<!-- generated-by: scripts/generate_pages.py -->
# xortool

**Kit:** REMnux  **Capability:** Analyse shellcode; Break simple obfuscation  **Version:** 1.1.0
**Captured:** `cyberlab-aio` via `--help` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/xortool.help.txt)  **Docs:** <https://github.com/hellman/xortool>

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

## Common invocations

<!-- candidates mined from cyberlab; verify each flag against the options table below before treating as reviewed -->
```
# from cyberlab 09-deobfuscation
xortool --version
# from cyberlab 09-deobfuscation
xortool -c 20 exercise/encoded_payload.bin
```

## Options

All 8 options parsed from the captured help text; 3 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-l` | LEN | length of the key | Fix the key length when you already know it. |
| `--key-length` | LEN | length of the key |  |
| `-m` | MAX-LEN | maximum key length to probe [default: 65] | Maximum key length to consider. |
| `--max-keylen` | MAX-LEN | maximum key length to probe [default: 65] |  |
| `-c` | CHAR | most frequent char (one char or hex code) | Give the most frequent character of the plaintext — usually `20` (space) for text, `00` for binaries. This is the flag that makes or breaks the attack. |
| `--char` | CHAR | most frequent char (one char or hex code) |  |
| `-r` | PERCENT | threshold validity percentage [default: 95] |  |
| `--threshold` | PERCENT | threshold validity percentage [default: 95] |  |

## Gotchas

- Output lands in an `xortool_out/` directory, not stdout. People routinely think it did nothing.
- `-c 00` is right far more often than the default for packed binaries, because null padding dominates.

## See also

[`rasm2`](../reverse-engineering/rasm2.md), [`floss`](../malware-triage-static/floss.md), [`xlmdeobfuscator`](../malware-triage-documents/xlmdeobfuscator.md)
