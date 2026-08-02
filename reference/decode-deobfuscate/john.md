<!-- generated-by: scripts/generate_pages.py -->
# john

**Kit:** Kali Linux  **Capability:** Crack passwords and hashes  **Version:** stat: version: No such file or directory
**Captured:** `cyberlab-aio` via `(no args)` on 2026-08-02  [raw](../../capture/cyberlab-aio/help/john.help.txt)

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

John the Ripper password cracker, version 1.9.0

## Synopsis

```
john [OPTIONS] [PASSWORD-FILES]
```

## Common invocations

<!-- candidates mined from cyberlab; verify each flag against the options table below before treating as reviewed -->
```
# from cyberlab 11-offensive-kali
john --list=build-info 2>&1 | head -n 1
# from cyberlab 11-offensive-kali
john --format=Raw-MD5 --wordlist=/usr/share/wordlists/rockyou.txt exercise/lab_hash.txt
# from cyberlab 11-offensive-kali
john --show --format=Raw-MD5 exercise/lab_hash.txt
# from cyberlab 40-password-cracking
john --version 2>&1 | head -n 1
# from cyberlab 40-password-cracking
john --list=formats | tr ',' '\n' | grep -i -m 5 md5
# from cyberlab 40-password-cracking
john --format=raw-md5 --wordlist=exercise/wordlist.txt exercise/hash.txt
# from cyberlab 40-password-cracking
john --format=raw-md5 --show exercise/hash.txt
```

## Options

All 21 options parsed from the captured help text. The final column is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `--single` | — | "single crack" mode |  |
| `--wordlist` | FILE | wordlist mode, read words from FILE or stdin |  |
| `--stdin` | — | wordlist mode, read words from FILE or stdin |  |
| `--rules` | — | enable word mangling rules for wordlist mode |  |
| `--incremental` | MODE (optional) | "incremental" mode [using section MODE] |  |
| `--external` | MODE | external mode or word filter |  |
| `--stdout` | LENGTH (optional) | just output candidate passwords [cut at LENGTH] |  |
| `--restore` | NAME (optional) | restore an interrupted session [called NAME] |  |
| `--session` | NAME | give a new session the NAME |  |
| `--status` | NAME (optional) | print status of a session [called NAME] |  |
| `--make-charset` | FILE | make a charset, FILE will be overwritten |  |
| `--show` | — | show cracked passwords |  |
| `--test` | TIME (optional) | run tests and benchmarks for TIME seconds each |  |
| `--users` | [-]LOGIN\|UID[,..] | [do not] load this (these) user(s) only |  |
| `--groups` | [-]GID[,..] | load users [not] of this (these) group(s) only |  |
| `--shells` | [-]SHELL[,..] | load users with[out] this (these) shell(s) only |  |
| `--salts` | [-]N | load salts with[out] at least N passwords only |  |
| `--save-memory` | LEVEL | enable memory saving, at LEVEL 1..3 |  |
| `--node` | MIN[-MAX] | this node's number range out of TOTAL count |  |
| `--fork` | N | fork N processes |  |
| `--format` | NAME | force hash type NAME: descrypt/bsdicrypt/md5crypt/ bcrypt/LM/AFS/tripcode/dummy/crypt |  |

## Gotchas

_TODO: operational traps._

## See also

[`hashcat`](../decode-deobfuscate/hashcat.md), [`hydra`](../decode-deobfuscate/hydra.md)
