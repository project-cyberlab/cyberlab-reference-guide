<!-- generated-by: scripts/generate_pages.py -->
# hashcat

| | |
|---|---|
| **Kit** | Kali Linux |
| **Capability** | Crack passwords and hashes |
| **Version** | v6.2.6 |
| **Captured from** | `cyberlab-aio` via `--help` on 2026-08-11 — [raw help output](../../capture/cyberlab-aio/help/hashcat.help.txt) |

[← Capability index](../INDEX.md) · [Kit tool list](../../catalog/KIT-TOOLS.md)

## Purpose

Recover passwords from hashes using GPU-accelerated guessing — dictionary, rule-mutated, mask and brute-force attacks across several hundred hash types. In DFIR it is usually pointed at credentials recovered from a host to establish what an attacker could have reused elsewhere.

## When you'd reach for this

An analyst reaches for hashcat when dealing with hashes like MD5, using wordlists such as rockyou.txt for brute-force or combination attacks, and runs it after identifying the hash type and preparing input files; they choose it over similar tools due to its GPU-accelerated cracking capabilities and support for advanced attack modes like mask attacks, as demonstrated in the examples.

**Sources:** <https://github.com/IPIRATEXAPTAIN/htb-academy/blob/main/CrackingPasswordsWithHashcat.md> · <https://hashcat.net/wiki/doku.php?id=frequently_asked_questions>

## Synopsis

```
hashcat [options]... hash|hashfile|hccapxfile [dictionary|mask|directory]...
```

## Common invocations

```
# Restore a paused hash cracking session using saved state
hashcat --restore --session=my_session
# Coordinate distributed cracking to avoid redundant attempts
hashcat --brain-server
# Crack SHA1 hashes using a wordlist to recover passwords
hashcat -m 100 hashes.txt wordlist.txt
# Display backend info for performance tuning
hashcat --backend-info
# Display available OpenCL devices for selection
hashcat -I
# Test hardware performance for cracking speed
hashcat -b
```

## Options

All 143 options parsed from the captured help text; 15 reviewed with usage guidance.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-m` | — | \| Num \| Hash-type, references below (otherwise autodetect) \| -m 1000 | An analyst would use the -m flag when specifying the hash type (e.g., MD5, SHA-256) to ensure Hashcat correctly interprets the hash format during cracking attempts. |
| `--hash-type` | — | \| Num \| Hash-type, references below (otherwise autodetect) \| -m 1000 | An analyst would use the -m flag when specifying the hash type (e.g., MD5, SHA-256) to ensure Hashcat correctly interprets the hash format during cracking attempts. |
| `-a` | — | \| Num \| Attack-mode, see references below \| -a 3 | An analyst would use the -a flag when performing a combination attack to generate password combinations from two separate wordlists. |
| `--attack-mode` | — | \| Num \| Attack-mode, see references below \| -a 3 | An analyst would use the -a flag when performing a combination attack to generate password combinations from two separate wordlists. |
| `-V` | — | \| \| Print version \| |  |
| `--version` | — | \| \| Print version \| |  |
| `-h` | — | \| \| Print help \| |  |
| `--help` | — | \| \| Print help \| |  |
| `--quiet` | — | \| \| Suppress output \| |  |
| `--hex-charset` | — | \| \| Assume charset is given in hex \| |  |
| `--hex-salt` | — | \| \| Assume salt is given in hex \| |  |
| `--hex-wordlist` | — | \| \| Assume words in wordlist are given in hex \| |  |
| `--force` | — | \| \| Ignore warnings \| |  |
| `--status` | — | \| \| Enable automatic update of the status screen \| |  |
| `--status-json` | — | \| \| Enable JSON format for status output \| |  |
| `--status-timer` | — | \| Num \| Sets seconds between status screen updates to X \| --status-timer=1 |  |
| `--stdin-timeout-abort` | — | \| Num \| Abort if there is no input from stdin for X seconds \| --stdin-timeout-abort=300 |  |
| `--machine-readable` | — | \| \| Display the status view in a machine-readable format \| |  |
| `--keep-guessing` | — | \| \| Keep guessing the hash after it has been cracked \| |  |
| `--self-test-disable` | — | \| \| Disable self-test functionality on startup \| |  |
| `--loopback` | — | \| \| Add new plains to induct directory \| |  |
| `--markov-hcstat2` | — | \| File \| Specify hcstat2 file to use \| --markov-hcstat2=my.hcstat2 |  |
| `--markov-disable` | — | \| \| Disables markov-chains, emulates classic brute-force \| |  |
| `--markov-classic` | — | \| \| Enables classic markov-chains, no per-position \| |  |
| `--markov-inverse` | — | \| \| Enables inverse markov-chains, no per-position \| |  |
| `-t` | — | \| Num \| Threshold X when to stop accepting new markov-chains \| -t 50 |  |
| `--markov-threshold` | — | \| Num \| Threshold X when to stop accepting new markov-chains \| -t 50 |  |
| `--runtime` | — | \| Num \| Abort session after X seconds of runtime \| --runtime=10 |  |
| `--session` | — | \| Str \| Define specific session name \| --session=mysession | An analyst would use the --session flag when resuming an interrupted hashcat session to continue cracking from the last checkpointed position. |
| `--restore` | — | \| \| Restore session from --session \| |  |
| `--restore-disable` | — | \| \| Do not write restore file \| |  |
| `--restore-file-path` | — | \| File \| Specific path to restore file \| --restore-file-path=x.restore |  |
| `-o` | — | \| File \| Define outfile for recovered hash \| -o outfile.txt | An analyst would use the -o flag when they need to specify the output file path for storing cracked hashes, such as in the example where 'cracked.txt' is used. |
| `--outfile` | — | \| File \| Define outfile for recovered hash \| -o outfile.txt | An analyst would use the -o flag when they need to specify the output file path for storing cracked hashes, such as in the example where 'cracked.txt' is used. |
| `--outfile-format` | — | \| Str \| Outfile format to use, separated with commas \| --outfile-format=1,3 | An analyst would use the --outfile-format flag when they need to specify a custom output format for cracked hashes, such as saving results in plain text instead of the default hash[:salt] format. |
| `--outfile-autohex-disable` | — | \| \| Disable the use of $HEX[] in output plains \| |  |
| `--outfile-check-timer` | — | \| Num \| Sets seconds between outfile checks to X \| --outfile-check-timer=30 |  |
| `-p` | — | \| Char \| Separator char for hashlists and outfile \| -p : |  |
| `--separator` | — | \| Char \| Separator char for hashlists and outfile \| -p : |  |
| `--stdout` | — | \| \| Do not crack a hash, instead print candidates only \| | An analyst would use the --stdout flag when generating custom wordlists by specifying mask patterns to create targeted combinations of characters for cracking hashes. |
| `--show` | — | \| \| Compare hashlist with potfile; show cracked hashes \| | An analyst would use the --show flag to display previously cracked hashes stored in the potfile when verifying results or avoiding redundant cracking efforts. |
| `--left` | — | \| \| Compare hashlist with potfile; show uncracked hashes \| |  |
| `--username` | — | \| \| Enable ignoring of usernames in hashfile \| |  |
| `--remove` | — | \| \| Enable removal of hashes once they are cracked \| |  |
| `--remove-timer` | — | \| Num \| Update input hash file each X seconds \| --remove-timer=30 |  |
| `--potfile-disable` | — | \| \| Do not write potfile \| |  |
| `--potfile-path` | — | \| File \| Specific path to potfile \| --potfile-path=my.pot |  |
| `--encoding-from` | — | \| Code \| Force internal wordlist encoding from X \| --encoding-from=iso-8859-15 |  |
| `--encoding-to` | — | \| Code \| Force internal wordlist encoding to X \| --encoding-to=utf-32le |  |
| `--debug-mode` | — | \| Num \| Defines the debug mode (hybrid only by using rules) \| --debug-mode=4 |  |
| `--debug-file` | — | \| File \| Output file for debugging rules \| --debug-file=good.log |  |
| `--induction-dir` | — | \| Dir \| Specify the induction directory to use for loopback \| --induction=inducts |  |
| `--outfile-check-dir` | — | \| Dir \| Specify the outfile directory to monitor for plains \| --outfile-check-dir=x |  |
| `--logfile-disable` | — | \| \| Disable the logfile \| |  |
| `--hccapx-message-pair` | — | \| Num \| Load only message pairs from hccapx matching X \| --hccapx-message-pair=2 |  |
| `--nonce-error-corrections` | — | \| Num \| The BF size range to replace AP's nonce last bytes \| --nonce-error-corrections=16 |  |
| `--keyboard-layout-mapping` | — | \| File \| Keyboard layout mapping table for special hash-modes \| --keyb=german.hckmap |  |
| `--truecrypt-keyfiles` | — | \| File \| Keyfiles to use, separated with commas \| --truecrypt-keyf=x.png |  |
| `--veracrypt-keyfiles` | — | \| File \| Keyfiles to use, separated with commas \| --veracrypt-keyf=x.txt |  |
| `--veracrypt-pim-start` | — | \| Num \| VeraCrypt personal iterations multiplier start \| --veracrypt-pim-start=450 |  |
| `--veracrypt-pim-stop` | — | \| Num \| VeraCrypt personal iterations multiplier stop \| --veracrypt-pim-stop=500 |  |
| `-b` | — | \| \| Run benchmark of selected hash-modes \| | An analyst would use the -b flag when benchmarking a hash mode to estimate raw speed on their hardware before initiating a cracking job. |
| `--benchmark` | — | \| \| Run benchmark of selected hash-modes \| | An analyst would use the -b flag when benchmarking a hash mode to estimate raw speed on their hardware before initiating a cracking job. |
| `--benchmark-all` | — | \| \| Run benchmark of all hash-modes (requires -b) \| |  |
| `--speed-only` | — | \| \| Return expected speed of the attack, then quit \| |  |
| `--progress-only` | — | \| \| Return ideal progress step size and time to process \| |  |
| `-c` | — | \| Num \| Sets size in MB to cache from the wordfile to X \| -c 32 |  |
| `--segment-size` | — | \| Num \| Sets size in MB to cache from the wordfile to X \| -c 32 |  |
| `--bitmap-min` | — | \| Num \| Sets minimum bits allowed for bitmaps to X \| --bitmap-min=24 |  |
| `--bitmap-max` | — | \| Num \| Sets maximum bits allowed for bitmaps to X \| --bitmap-max=24 |  |
| `--cpu-affinity` | — | \| Str \| Locks to CPU devices, separated with commas \| --cpu-affinity=1,2,3 |  |
| `--hook-threads` | — | \| Num \| Sets number of threads for a hook (per compute unit) \| --hook-threads=8 |  |
| `--hash-info` | — | \| \| Show information for each hash-mode \| |  |
| `--example-hashes` | — | \| \| Alias of --hash-info \| |  |
| `--backend-ignore-cuda` | — | \| \| Do not try to open CUDA interface on startup \| |  |
| `--backend-ignore-hip` | — | \| \| Do not try to open HIP interface on startup \| |  |
| `--backend-ignore-metal` | — | \| \| Do not try to open Metal interface on startup \| |  |
| `--backend-ignore-opencl` | — | \| \| Do not try to open OpenCL interface on startup \| |  |
| `-I` | — | \| \| Show system/evironment/backend API info \| -I or -II |  |
| `--backend-info` | — | \| \| Show system/evironment/backend API info \| -I or -II |  |
| `-d` | — | \| Str \| Backend devices to use, separated with commas \| -d 1 | An analyst would use the -d flag when specifying a particular GPU device in a multi-GPU setup where hashcat encounters mapping errors due to identical or similarly identified devices, requiring manual selection to bypass temperature or fan control issues. |
| `--backend-devices` | — | \| Str \| Backend devices to use, separated with commas \| -d 1 | An analyst would use the -d flag when specifying a particular GPU device in a multi-GPU setup where hashcat encounters mapping errors due to identical or similarly identified devices, requiring manual selection to bypass temperature or fan control issues. |
| `-D` | — | \| Str \| OpenCL device-types to use, separated with commas \| -D 1 | An analyst would use the -D flag when they need to specify whether to use the CPU, GPU, or both for hash cracking based on available hardware resources. |
| `--opencl-device-types` | — | \| Str \| OpenCL device-types to use, separated with commas \| -D 1 | An analyst would use the -D flag when they need to specify whether to use the CPU, GPU, or both for hash cracking based on available hardware resources. |
| `-O` | — | \| \| Enable optimized kernels (limits password length) \| |  |
| `--optimized-kernel-enable` | — | \| \| Enable optimized kernels (limits password length) \| |  |
| `-M` | — | \| \| Disable multiply kernel-accel with processor count \| |  |
| `--multiply-accel-disable` | — | \| \| Disable multiply kernel-accel with processor count \| |  |
| `-w` | — | \| Num \| Enable a specific workload profile, see pool below \| -w 3 | An analyst would use the -w flag when optimizing Hashcat performance on a dedicated cracking rig with a GPU not driving a display, specifically setting -w 4 for maximum workload intensity. |
| `--workload-profile` | — | \| Num \| Enable a specific workload profile, see pool below \| -w 3 | An analyst would use the -w flag when optimizing Hashcat performance on a dedicated cracking rig with a GPU not driving a display, specifically setting -w 4 for maximum workload intensity. |
| `-n` | — | \| Num \| Manual workload tuning, set outerloop step size to X \| -n 64 |  |
| `--kernel-accel` | — | \| Num \| Manual workload tuning, set outerloop step size to X \| -n 64 |  |
| `-u` | — | \| Num \| Manual workload tuning, set innerloop step size to X \| -u 256 |  |
| `--kernel-loops` | — | \| Num \| Manual workload tuning, set innerloop step size to X \| -u 256 |  |
| `-T` | — | \| Num \| Manual workload tuning, set thread count to X \| -T 64 |  |
| `--kernel-threads` | — | \| Num \| Manual workload tuning, set thread count to X \| -T 64 |  |
| `--backend-vector-width` | — | \| Num \| Manually override backend vector-width to X \| --backend-vector=4 |  |
| `--spin-damp` | — | \| Num \| Use CPU for device synchronization, in percent \| --spin-damp=10 |  |
| `--hwmon-disable` | — | \| \| Disable temperature and fanspeed reads and triggers \| |  |
| `--hwmon-temp-abort` | — | \| Num \| Abort if temperature reaches X degrees Celsius \| --hwmon-temp-abort=100 | An analyst would use the --hwmon-temp-abort flag when cracking hashes on a GPU to automatically abort the process if the GPU temperature reaches 90°C, preventing overheating. |
| `--scrypt-tmto` | — | \| Num \| Manually override TMTO value for scrypt to X \| --scrypt-tmto=3 |  |
| `-s` | — | \| Num \| Skip X words from the start \| -s 1000000 |  |
| `--skip` | — | \| Num \| Skip X words from the start \| -s 1000000 |  |
| `-l` | — | \| Num \| Limit X words from the start + skipped words \| -l 1000000 |  |
| `--limit` | — | \| Num \| Limit X words from the start + skipped words \| -l 1000000 |  |
| `--keyspace` | — | \| \| Show keyspace base:mod values and quit \| |  |
| `-j` | — | \| Rule \| Single rule applied to each word from left wordlist \| -j 'c' |  |
| `--rule-left` | — | \| Rule \| Single rule applied to each word from left wordlist \| -j 'c' |  |
| `-k` | — | \| Rule \| Single rule applied to each word from right wordlist \| -k '^-' |  |
| `--rule-right` | — | \| Rule \| Single rule applied to each word from right wordlist \| -k '^-' |  |
| `-r` | — | \| File \| Multiple rules applied to each word from wordlists \| -r rules/best64.rule | An analyst would use the -r flag when applying custom or built-in rule sets to a wordlist to generate password variations during cracking attacks, as demonstrated in the examples involving rules/best64.rule and modifying rules to append specific strings like years to passwords. |
| `--rules-file` | — | \| File \| Multiple rules applied to each word from wordlists \| -r rules/best64.rule | An analyst would use the -r flag when applying custom or built-in rule sets to a wordlist to generate password variations during cracking attacks, as demonstrated in the examples involving rules/best64.rule and modifying rules to append specific strings like years to passwords. |
| `-g` | — | \| Num \| Generate X random rules \| -g 10000 | An analyst would use the -g flag when encountering errors related to excessive rule usage, such as clEnqueueCopyBuffer() -30 or cuStreamSynchronize() 702, to reduce the number of rules and resolve the issue. |
| `--generate-rules` | — | \| Num \| Generate X random rules \| -g 10000 | An analyst would use the -g flag when encountering errors related to excessive rule usage, such as clEnqueueCopyBuffer() -30 or cuStreamSynchronize() 702, to reduce the number of rules and resolve the issue. |
| `--generate-rules-func-min` | — | \| Num \| Force min X functions per rule \| |  |
| `--generate-rules-func-max` | — | \| Num \| Force max X functions per rule \| |  |
| `--generate-rules-func-sel` | — | \| Str \| Pool of rule operators valid for random rule engine \| --generate-rules-func-sel=ioTlc |  |
| `--generate-rules-seed` | — | \| Num \| Force RNG seed set to X \| |  |
| `-1` | — | \| CS \| User-defined charset ?1 \| -1 ?l?d?u | An analyst would use the --custom-charset1 flag when defining a custom character set (e.g., ?l?d) to reference in a mask with ?1, such as in a hashcat mask file line like "?l?d,?l?l?l?l?1" to specify a combination of lowercase letters and digits for password cracking. |
| `--custom-charset1` | — | \| CS \| User-defined charset ?1 \| -1 ?l?d?u | An analyst would use the --custom-charset1 flag when defining a custom character set (e.g., ?l?d) to reference in a mask with ?1, such as in a hashcat mask file line like "?l?d,?l?l?l?l?1" to specify a combination of lowercase letters and digits for password cracking. |
| `-2` | — | \| CS \| User-defined charset ?2 \| -2 ?l?d?s |  |
| `--custom-charset2` | — | \| CS \| User-defined charset ?2 \| -2 ?l?d?s |  |
| `-3` | — | \| CS \| User-defined charset ?3 \| |  |
| `--custom-charset3` | — | \| CS \| User-defined charset ?3 \| |  |
| `-4` | — | \| CS \| User-defined charset ?4 \| |  |
| `--custom-charset4` | — | \| CS \| User-defined charset ?4 \| |  |
| `--identify` | — | \| \| Shows all supported algorithms for input hashes \| --identify my.hash |  |
| `-i` | — | \| \| Enable mask increment mode \| |  |
| `--increment` | — | \| \| Enable mask increment mode \| |  |
| `--increment-min` | — | \| Num \| Start mask incrementing at X \| --increment-min=4 |  |
| `--increment-max` | — | \| Num \| Stop mask incrementing at X \| --increment-max=8 |  |
| `-S` | — | \| \| Enable slower (but advanced) candidate generators \| |  |
| `--slow-candidates` | — | \| \| Enable slower (but advanced) candidate generators \| |  |
| `--brain-server` | — | \| \| Enable brain server \| |  |
| `--brain-server-timer` | — | \| Num \| Update the brain server dump each X seconds (min:60) \| --brain-server-timer=300 |  |
| `-z` | — | \| \| Enable brain client, activates -S \| |  |
| `--brain-client` | — | \| \| Enable brain client, activates -S \| |  |
| `--brain-client-features` | — | \| Num \| Define brain client features, see below \| --brain-client-features=3 |  |
| `--brain-host` | — | \| Str \| Brain server host (IP or domain) \| --brain-host=127.0.0.1 |  |
| `--brain-port` | — | \| Port \| Brain server port \| --brain-port=13743 |  |
| `--brain-password` | — | \| Str \| Brain server authentication password \| --brain-password=bZfhCvGUSjRq |  |
| `--brain-session` | — | \| Hex \| Overrides automatically calculated brain session \| --brain-session=0x2ae611db |  |
| `--brain-session-whitelist` | — | \| Hex \| Allow given sessions only, separated with commas \| --brain-session-whitelist=0x2ae611db |  |

## Gotchas

_TODO: operational traps._

## See also

[`john`](../decode-deobfuscate/john.md), [`hydra`](../decode-deobfuscate/hydra.md)
