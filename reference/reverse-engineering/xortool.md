<!-- generated-by: scripts/generate_pages.py -->
# xortool

| | |
|---|---|
| **Kit** | REMnux |
| **Capability** | Analyse shellcode; Break simple obfuscation |
| **Version** | 1.1.0 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-07 — [raw help output](../../capture/cyberlab-aio/help/xortool.help.txt) |
| **Documentation** | <https://github.com/hellman/xortool> |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Recover the key length and key of an XOR-encrypted file by frequency analysis.

## When you'd reach for this

An analyst reaches for xortool when dealing with XOR-encrypted data, particularly when the key length is unknown or longer than default limits, and runs it after initial attempts to guess the key fail, using flags like -m, -l, or -c to refine results; they choose it over similar tools because it automates key-length analysis, filters plaintexts by character sets (e.g., Base64), and handles multi-byte keys with adjustable parameters.

**Sources:** <https://github.com/hellman/xortool> · <https://github.com/hellman/xortool/blob/master/README.md> · <https://www.doyler.net/security-not-included/basic-xortool-usage>

## Synopsis

```
xortool [-x] [-m MAX-LEN] [-f] [-t CHARSET] [FILE]
xortool [-x] [-l LEN] [-c CHAR | -b | -o] [-f] [-t CHARSET] [-p PLAIN] [-r PERCENT] [FILE]
xortool [-x] [-m MAX-LEN| -l LEN] [-c CHAR | -b | -o] [-f] [-t CHARSET] [-p PLAIN] [-r PERCENT] [FILE]
xortool [-h | --help]
xortool --version
```

## Options

All 20 options parsed from the captured help text; 9 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-x` | — | input is hex-encoded str | An analyst would use the -x flag when processing a hex-encoded file, such as when decrypting data that has been represented in hexadecimal format. |
| `--hex` | — | input is hex-encoded str | An analyst would use the -x flag when processing a hex-encoded file, such as when decrypting data that has been represented in hexadecimal format. |
| `-l` | LEN | length of the key | Fix the key length when you already know it. |
| `--key-length` | LEN | length of the key | Fix the key length when you already know it. |
| `-m` | MAX-LEN | maximum key length to probe [default: 65] | Maximum key length to consider. |
| `--max-keylen` | MAX-LEN | maximum key length to probe [default: 65] | Maximum key length to consider. |
| `-c` | CHAR | most frequent char (one char or hex code) | Give the most frequent character of the plaintext — usually `20` (space) for text, `00` for binaries. This is the flag that makes or breaks the attack. |
| `--char` | CHAR | most frequent char (one char or hex code) | An analyst would use the --char flag when they have prior knowledge or suspicion about the most frequent character in the plaintext, aiding xortool in accurately guessing the XOR key. |
| `-b` | — | brute force all possible most frequent chars | Brute-force the most frequent character rather than guessing. |
| `--brute-chars` | — | brute force all possible most frequent chars | Brute-force the most frequent character rather than guessing. |
| `-o` | — | same as -b but will only check printable chars | An analyst would use the -o flag when brute-forcing possible keys by checking only printable characters to guess the most frequent byte in XOR-encrypted data. |
| `--brute-printable` | — | same as -b but will only check printable chars | An analyst would use the -o flag when brute-forcing possible keys by checking only printable characters to guess the most frequent byte in XOR-encrypted data. |
| `-f` | — | filter outputs based on the charset |  |
| `--filter-output` | — | filter outputs based on the charset |  |
| `-p` | PLAIN | use known plaintext for decoding | An analyst would use the -p flag when they have a known plaintext segment to aid in decrypting XOR-encrypted data, as demonstrated in examples where it's paired with encrypted files and brute-force options. |
| `--known-plaintext` | PLAIN | use known plaintext for decoding | An analyst would use the -p flag when they have a known plaintext segment to aid in decrypting XOR-encrypted data, as demonstrated in examples where it's paired with encrypted files and brute-force options. |
| `-r` | PERCENT | threshold validity percentage [default: 95] | An analyst would use the -r flag when adjusting the threshold validity percentage for determining the likelihood of correct key guesses during XOR analysis. |
| `--threshold` | PERCENT | threshold validity percentage [default: 95] | An analyst would use the -r flag when adjusting the threshold validity percentage for determining the likelihood of correct key guesses during XOR analysis. |
| `-h` | — | show this help |  |
| `--help` | — | show this help |  |

## Gotchas

- Output lands in an `xortool_out/` directory, not stdout. People routinely think it did nothing.
- `-c 00` is right far more often than the default for packed binaries, because null padding dominates.

## See also

[`rasm2`](../reverse-engineering/rasm2.md), [`floss`](../malware-triage-static/floss.md), [`xlmdeobfuscator`](../malware-triage-documents/xlmdeobfuscator.md)
