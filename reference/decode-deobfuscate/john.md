<!-- generated-by: scripts/generate_pages.py -->
# john

| | |
|---|---|
| **Kit** | Kali Linux |
| **Capability** | Crack passwords and hashes |
| **Captured from** | `cyberlab-aio` via `(no args)` on 2026-08-08 — [raw help output](../../capture/cyberlab-aio/help/john.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Copyright (c) 1996-2019 by Solar Designer

## When you'd reach for this

An analyst reaches for John when attempting to crack password hashes, often after preparing a larger wordlist and configuring the tool's settings, as it supports multiple modes like single crack, wordlist with rules, and incremental cracking for thoroughness. They may run `john --show` afterward to display cracked passwords, preferring John over similar tools due to its flexibility in using custom charsets, filters, and incremental modes tailored to specific password patterns.

**Sources:** <https://www.openwall.com/john/doc/EXAMPLES.shtml>

## Synopsis

```
john [OPTIONS] [PASSWORD-FILES]
```

## Options

All 21 options parsed from the captured help text; 11 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `--single` | — | "single crack" mode | An analyst would use the --single flag when auditing Linux system passwords to quickly identify weak passwords in hash files during the initial phase of a security assessment. |
| `--wordlist` | FILE | wordlist mode, read words from FILE or stdin | An analyst would use the --wordlist flag when attempting to crack password hashes by feeding John the Ripper a file of potential passwords, such as the rockyou.txt wordlist, to compare against the target hash file. |
| `--stdin` | — | wordlist mode, read words from FILE or stdin | An analyst would use the --wordlist flag when attempting to crack password hashes by feeding John the Ripper a file of potential passwords, such as the rockyou.txt wordlist, to compare against the target hash file. |
| `--rules` | — | enable word mangling rules for wordlist mode | An analyst would use the --rules flag when applying word mangling rules to a wordlist to generate variations of passwords for cracking, as demonstrated in examples like "john --wordlist=all.lst --rules mypasswd" and similar commands in the documentation. |
| `--incremental` | MODE (optional) | "incremental" mode [using section MODE] | An analyst would use the --incremental flag when the wordlist has been exhausted and the hash remains uncracked, particularly for short passwords (5-7 characters) where incremental brute-force is feasible. |
| `--external` | MODE | external mode or word filter |  |
| `--stdout` | LENGTH (optional) | just output candidate passwords [cut at LENGTH] |  |
| `--restore` | NAME (optional) | restore an interrupted session [called NAME] | An analyst would use the --restore flag when resuming an interrupted session to continue cracking passwords from where it left off. |
| `--session` | NAME | give a new session the NAME | An analyst would use the --session flag when running multiple parallel cracking sessions or resuming an interrupted session to avoid conflicts and ensure proper restoration from a saved session state. |
| `--status` | NAME (optional) | print status of a session [called NAME] |  |
| `--make-charset` | FILE | make a charset, FILE will be overwritten | An analyst would use the --make-charset flag when generating a custom character set file based on character frequencies from a password file containing many already cracked passwords or multiple password files from the same organization or country. |
| `--show` | — | show cracked passwords | An analyst would use the --show flag after successfully cracking passwords to display the cracked credentials in a human-readable format for review or documentation. |
| `--test` | TIME (optional) | run tests and benchmarks for TIME seconds each |  |
| `--users` | [-]LOGIN\|UID[,..] | [do not] load this (these) user(s) only | An analyst would use the --users flag when checking if cracked accounts correspond to specific UIDs, such as root (UID 0), or when isolating specific usernames like "root" in the output. |
| `--groups` | [-]GID[,..] | load users [not] of this (these) group(s) only |  |
| `--shells` | [-]SHELL[,..] | load users with[out] this (these) shell(s) only | An analyst would use the --shells flag when excluding accounts with disabled shells from the cracked password report. |
| `--salts` | [-]N | load salts with[out] at least N passwords only |  |
| `--save-memory` | LEVEL | enable memory saving, at LEVEL 1..3 |  |
| `--node` | MIN[-MAX] | this node's number range out of TOTAL count |  |
| `--fork` | N | fork N processes |  |
| `--format` | NAME | force hash type NAME: descrypt/bsdicrypt/md5crypt/ bcrypt/LM/AFS/tripcode/dummy/crypt | An analyst would use the --format flag when cracking hashes from specific sources like NTDS.dit or /etc/shadow, or when the hash type requires a specific format identifier such as NT or raw-md5 to ensure John the Ripper correctly interprets the hash structure. |

## Gotchas

_TODO: operational traps._

## See also

[`hashcat`](../decode-deobfuscate/hashcat.md), [`hydra`](../decode-deobfuscate/hydra.md)
