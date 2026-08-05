#!/usr/bin/env python3
"""The judgement layer, kept separate from generated content.

Generated pages carry facts read off the binary. This file carries the things a
binary cannot tell you: why you would reach for a flag, and what will bite you.

Kept apart from generate_pages.py deliberately -- regenerating pages from fresh
captures must never destroy curation, and a reviewer must be able to see, in
one place, exactly which claims are human judgement rather than captured fact.

`when` keys only ANNOTATE flags that already exist in a page's options table.
They cannot introduce a flag, so this file cannot reintroduce the fabrication
problem it exists to avoid.
"""
from __future__ import annotations

ENRICHMENT: dict[str, dict] = {

    # Invocations are written by hand, one task per entry. Every flag used in
    # them exists in that tool's capture, because the linter checks flags found
    # in fenced blocks against the captured help and fails the build on one
    # that does not. The task line matters as much as the command: a bare
    # command is something to copy, a labelled one is something to learn.

    # --- Purposes -----------------------------------------------------------
    # Written because the parsed ones were unusable. parse_purpose takes the
    # first plausible line of the help text, and for these tools that line was
    # a banner, a field label or a synopsis: "Description:", "or:  dd OPTION",
    # "hashcat (v6.2.6) starting in help mode". Each of these says what the
    # tool is for to someone who has not met it.

    "AppCompatCacheParser": {
        "purpose": "Parse the Application Compatibility Cache (Shimcache) out "
                   "of the SYSTEM registry hive. Windows records an executable "
                   "here when the shim engine examines it, which happens for "
                   "programs that were run and for some that were merely "
                   "present — so it is evidence of existence and interest, not "
                   "proof of execution.",
    },
    "RECmd": {
        "purpose": "Query and export Windows registry hives from the command "
                   "line, using batch files of plugin definitions to pull "
                   "known-interesting keys in one pass. The batch approach is "
                   "the point: it turns 'check the usual persistence "
                   "locations' into one reproducible command.",
    },
    "SrumECmd": {
        "purpose": "Parse the System Resource Usage Monitor database, which "
                   "Windows keeps for roughly 30 days. It records bytes sent "
                   "and received per application per user — the artifact that "
                   "answers 'how much data left this host, and which process "
                   "sent it?' long after the network logs have rolled.",
    },
    "dd": {
        "purpose": "Copy data block by block, without interpreting it. In "
                   "forensics this is the plain-raw imaging tool: it will read "
                   "a whole device including unallocated space, but it has no "
                   "hashing, no error recovery and no metadata. Prefer "
                   "`dc3dd`, `dcfldd` or `ewfacquire` for evidence; reach for "
                   "`dd` when you need a byte range and nothing else.",
    },
    "xxd": {
        "purpose": "Produce a hex dump, or reverse one back into binary with "
                   "`-r`. The reverse direction is what distinguishes it from "
                   "a viewer: edit the hex, convert it back, and you have "
                   "carved or patched a file without a hex editor.",
    },
    "hashcat": {
        "purpose": "Recover passwords from hashes using GPU-accelerated "
                   "guessing — dictionary, rule-mutated, mask and brute-force "
                   "attacks across several hundred hash types. In DFIR it is "
                   "usually pointed at credentials recovered from a host to "
                   "establish what an attacker could have reused elsewhere.",
    },
    "nping": {
        "purpose": "Craft and send arbitrary network packets, and report what "
                   "comes back. Unlike `ping` it will build TCP, UDP, ICMP or "
                   "raw ARP probes with chosen flags and payloads, which makes "
                   "it the tool for asking a firewall or an IDS a precise "
                   "question about what it permits.",
    },
    "regripper": {
        "purpose": "Run plugins against a Windows registry hive and print what "
                   "each finds. The plugins encode where the interesting keys "
                   "live and how to interpret them, so it answers 'what is in "
                   "this hive that matters?' without you memorising key paths.",
    },
    "rip.pl": {
        "purpose": "The command-line entry point to RegRipper — run one plugin "
                   "or a whole profile against a registry hive. Scriptable in "
                   "a way the GUI is not, which is what makes it the form used "
                   "in a pipeline.",
    },
    "hayabusa": {
        "purpose": "Scan Windows event logs against a bundled Sigma rule set "
                   "and produce a ranked timeline of what looks like attacker "
                   "activity. It is built for speed over a whole log directory, "
                   "so it is the first pass that tells you which hosts and "
                   "which hours deserve a closer look.",
    },
    "tcpflow": {
        "purpose": "Reassemble TCP streams from a capture and write each "
                   "conversation to its own file. Where a packet tool shows "
                   "you frames, this gives you the bytes each side actually "
                   "sent, in order — which is what you need to read a protocol "
                   "or recover a transferred file.",
    },
    "tcpxtract": {
        "purpose": "Carve files out of network traffic by signature, without "
                   "understanding the protocol that carried them. Useful when "
                   "a transfer is not something a dissector recognises and you "
                   "only need the payload.",
    },
    "sigtool": {
        "purpose": "Inspect and build ClamAV signature databases: unpack a "
                   ".cvd, list its signatures, or generate a new one from a "
                   "sample. The bridge between 'ClamAV detects this' and "
                   "'here is exactly which signature fired and why'.",
    },
    "freshclam": {
        "purpose": "Update ClamAV's signature databases. Worth knowing in an "
                   "air-gapped lab, where it will fail silently and leave "
                   "`clamscan` quietly scanning with signatures that are "
                   "months old.",
    },
    "pcodedmp": {
        "purpose": "Disassemble the VBA p-code stored alongside macro source "
                   "in an Office document. The two can disagree: an attacker "
                   "can leave innocuous source in place while the p-code that "
                   "actually executes does something else, and this is how you "
                   "see the difference.",
    },
    "pdf-parser.py": {
        "purpose": "Walk a PDF's object graph and show what each object "
                   "contains, decoding streams on request. Where `pdfid` "
                   "counts suspicious keywords, this resolves references and "
                   "shows the actual content — the step from 'this PDF "
                   "contains JavaScript' to 'here is the JavaScript'.",
    },
    "pdf-parser": {
        "purpose": "Walk a PDF's object graph and show what each object "
                   "contains, decoding streams on request. Where `pdfid` "
                   "counts suspicious keywords, this resolves references and "
                   "shows the actual content — the step from 'this PDF "
                   "contains JavaScript' to 'here is the JavaScript'.",
    },
    "affinfo": {
        "purpose": "Print the metadata of an AFF forensic container: acquisition "
                   "details, hashes and segment layout. The AFF equivalent of "
                   "`ewfinfo`, and the fastest way to see what an .aff file "
                   "claims about its own provenance.",
    },
    "affcat": {
        "purpose": "Stream the raw contents of an AFF container to stdout, so "
                   "tools that cannot read AFF can be fed the image through a "
                   "pipe rather than a full conversion to raw.",
    },
    "affconvert": {
        "purpose": "Convert between AFF and raw images in either direction. The "
                   "usual reason is a tool that only reads one of them; keep "
                   "the original, because converting to raw discards the "
                   "metadata and hashes AFF was carrying.",
    },
    "md5sum": {
        "purpose": "Compute or verify MD5 checksums. Still everywhere in DFIR "
                   "for matching files against hash sets, but MD5 is broken "
                   "for collisions — use it to say two files are the same, "
                   "never to prove a file is what it claims.",
    },
    "openssl": {
        "purpose": "The general-purpose crypto toolkit: inspect certificates, "
                   "compute digests, encrypt and decrypt, and speak TLS to a "
                   "service. In analysis it is most often used to read a "
                   "certificate a sample presented, or to decrypt a blob once "
                   "the key is known.",
    },
    "regipy-dump": {
        "purpose": "Dump a registry hive to JSON with regipy, so the contents "
                   "can be searched, diffed or fed into other tooling rather "
                   "than read key by key.",
    },
    "regipy-plugins-run": {
        "purpose": "Run regipy's plugins over a hive and emit structured "
                   "results. The Python counterpart to RegRipper, and the "
                   "easier one to embed in a pipeline because the output is "
                   "JSON rather than formatted text.",
    },
    "regipy-diff": {
        "purpose": "Diff two registry hives and report what changed between "
                   "them. The artifact-level version of a before-and-after "
                   "detonation: snapshot, run the sample, snapshot again, and "
                   "read the delta.",
    },
    "regipy-parse-header": {
        "purpose": "Print a hive's header — sequence numbers, timestamp and "
                   "whether it was cleanly unmounted. A dirty hive means "
                   "transaction logs still hold recent changes, so this is the "
                   "check that tells you whether you are reading the whole "
                   "story.",
    },
    "hydra": {
        "purpose": "Test credentials against a network service across many "
                   "protocols. In an authorised engagement it answers whether "
                   "a recovered password works elsewhere; it is loud, it locks "
                   "accounts, and it belongs nowhere near production without "
                   "written permission.",
    },

    "mmls": {
        "purpose": "Display the partition layout of a disk image, including "
                   "unallocated gaps.",
        "invocations": [
            {"task": "First look at an unknown disk image",
             "cmd": "mmls {{image.dd}}"},
            {"task": "The offset you need for every other TSK tool is the "
                     "Start column, in sectors",
             "cmd": "mmls {{image.dd}}   # then: fls -o {{2048}} {{image.dd}}"},
            {"task": "Force the volume-system type when detection guesses wrong",
             "cmd": "mmls -t dos {{image.dd}}"},
            {"task": "Read an E01 rather than a raw image",
             "cmd": "mmls -i ewf {{image.E01}}"},
            {"task": "4Kn drive, where the 512-byte default computes every "
                     "offset wrong",
             "cmd": "mmls -b 4096 {{image.dd}}"},
            {"task": "Show only the gaps, where a hidden partition would sit",
             "cmd": "mmls -A {{image.dd}}"},
        ],
        "when": {
            "-t": "Force the volume-system type when auto-detection guesses wrong "
                  "(`-t list` shows the options).",
            "-i": "Set the image format for non-raw evidence such as E01 or AFF.",
            "-o": "Read a volume system nested at an offset — rare, but needed for "
                  "nested containers.",
            "-b": "Set the device sector size; required on 4Kn drives where the "
                  "512-byte default is wrong.",
            "-a": "Show allocated volumes only, when the gap entries are noise.",
            "-A": "Show unallocated space only — where a hidden or deleted "
                  "partition would show up.",
            "-r": "Recurse into nested volume systems (e.g. an extended partition).",
            "-B": "Print volume sizes in bytes rather than sectors, when reporting.",
            "-v": "Verbose diagnostics to stderr when an image will not parse.",
        },
        "gotchas": [
            "The **Start** column is in sectors. That value is what every other "
            "TSK tool wants for `-o`. Multiplying by the sector size here is the "
            "single most common mistake in a TSK workflow.",
            "If `mmls` reports no partition table, the image may be a single "
            "volume rather than a whole disk — try `fsstat` on it directly at "
            "offset 0 before assuming the image is corrupt.",
        ],
    },

    "icat": {
        "purpose": "Extract the contents of a file by inode, including deleted files.",
        "when": {
            "-r": "Attempt recovery of a deleted file — the reason you usually "
                  "reach for icat.",
            "-R": "Recover with slack space included, when you want everything the "
                  "blocks still hold.",
            "-s": "Include slack space in the output.",
            "-h": "Skip holes in sparse files so the output is not padded with zeroes.",
            "-o": "Partition offset in sectors, from `mmls`.",
            "-f": "Force the filesystem type when detection is wrong.",
            "-i": "Image format for non-raw evidence.",
            "-k": "Supply a decryption password for an encrypted volume.",
        },
        "gotchas": [
            "Always redirect to a file (`icat ... > out.bin`). Binary content "
            "dumped to a terminal will corrupt your session.",
            "A deleted inode listed by `fls -d` may return nothing or garbage: the "
            "metadata survived but the blocks were reallocated. Empty output is "
            "evidence, not a tool failure.",
        ],
    },

    "istat": {
        "purpose": "Show the full metadata for one inode: times, size, and the "
                   "blocks it occupies.",
        "when": {
            "-z": "Set the time zone for the displayed timestamps.",
            "-s": "Apply a clock skew in seconds for a known-bad system clock.",
            "-N": "Limit how many block addresses are printed for a large file.",
            "-o": "Partition offset in sectors, from `mmls`.",
            "-r": "Include recovery information for a deleted inode.",
        },
        "gotchas": [
            "The block list is what lets you prove whether a deleted file is still "
            "recoverable — cross-check it before promising a recovery.",
        ],
    },

    "mactime": {
        "purpose": "Turn a TSK body file into a human-readable chronological timeline.",
        "when": {
            "-b": "Read the body file produced by `fls -m` — the normal input.",
            "-d": "Emit CSV rather than the default text, for spreadsheets or "
                  "further tooling.",
            "-z": "Time zone of the evidence machine. Getting this wrong shifts "
                  "the whole timeline.",
            "-y": "Print dates ISO-style (year first), which sorts correctly.",
            "-m": "Print month numerically instead of by name.",
            "-g": "Map group IDs to names using a supplied group file.",
            "-p": "Map user IDs to names using a supplied passwd file.",
            "-h": "Produce HTML output for a report.",
        },
        "gotchas": [
            "`mactime` reports in the time zone you give it, not the one embedded "
            "in the evidence. An unstated `-z` silently produces a plausible, "
            "wrong timeline — state it explicitly every run.",
            "A date range is passed as a trailing argument "
            "(`mactime -b body.txt 2026-01-01..2026-02-01`), not as a flag.",
        ],
    },

    "yara": {
        "purpose": "Scan files, directories or live processes against YARA rules.",
        "when": {
            "-r": "Recurse into directories — the usual mode when triaging a tree.",
            "-s": "Print the matching strings and their offsets. Essential for "
                  "verifying a hit is real rather than trusting the rule name.",
            "-f": "Fast matching mode; faster but can miss some overlapping matches.",
            "-c": "Print only the count of matches per file, for a quick sweep.",
            "-n": "Print files that do NOT match — useful for finding the odd one out.",
            "-w": "Suppress warnings, which are noisy on large third-party rulesets.",
            "-m": "Print rule metadata, which usually carries author and reference.",
            "-t": "Scan only rules carrying a given tag.",
            "-d": "Define an external variable a rule expects, e.g. `-d filename=x`.",
            "-C": "Load a pre-compiled ruleset (from `yarac`) instead of source.",
            "-p": "Use N threads to speed up a large scan.",
            "-i": "Scan only the rule with the given identifier.",
        },
        "gotchas": [
            "A rule that references an external variable fails to compile unless "
            "you supply it with `-d`. This is the most common 'the rule is broken' "
            "false alarm.",
            "Scanning a live process needs a PID rather than a path, and root.",
            "Compile large rulesets once with `yarac` and scan with `-C`; "
            "recompiling thousands of rules per scan dominates runtime.",
        ],
    },

    "clamscan": {
        "purpose": "Scan files and directories with the ClamAV signature engine.",
        "when": {
            "-r": "Recurse into subdirectories.",
            "-i": "Print infected files only — the flag that makes output usable.",
            "--bell": "Audible alert on detection; useful during a long live scan.",
            "--move": "Quarantine detections into a directory. Never point this at "
                      "evidence you must preserve.",
            "--copy": "Copy rather than move detections, preserving the original.",
            "--exclude": "Skip paths matching a regex — noisy or irrelevant trees.",
            "--include": "Restrict the scan to paths matching a regex.",
            "--log": "Write results to a log file for the case record.",
            "--file-list": "Scan exactly the paths listed in a file.",
            "--tempdir": "Redirect temp extraction; important when scanning large "
                         "archives on a small root filesystem.",
            "--quiet": "Only report errors, for scripted runs.",
            "--no-summary": "Suppress the trailing summary block when parsing output.",
        },
        "gotchas": [
            "Without `-i` the output lists every clean file too, which buries the "
            "hits in a large tree.",
            "`--move` and `--remove` MUTATE evidence. On an investigation, scan a "
            "copy or use `--copy` — a quarantine action on original evidence is "
            "not defensible.",
            "Signatures must be current for the result to mean anything; a stale "
            "database yields a comfortable and worthless clean result.",
        ],
    },

    "floss": {
        "purpose": "Extract strings from a binary, including obfuscated strings that "
                   "`strings` cannot see.",
        "when": {
            "-n": "Minimum string length; raise it to cut noise on large binaries.",
            "-j": "Emit JSON, for feeding results into other tooling.",
            "-q": "Quiet mode — just the strings, for piping.",
            "-v": "Verbose progress; FLOSS emulation can be slow and silent otherwise.",
            "--color": "Control colour output when redirecting to a file.",
        },
        "gotchas": [
            "FLOSS emulates code to recover decoded strings, so it is far slower "
            "than `strings` and can take minutes on a large sample. Budget for it.",
            "It is built for Windows PE files. Pointing it at an ELF or a script "
            "gives you little more than plain `strings` would.",
        ],
    },

    "foremost": {
        "purpose": "Carve files out of an image or raw data by header and footer "
                   "signatures.",
        "when": {
            "-t": "Restrict carving to given types (`jpg`, `pdf`, `all`). Narrowing "
                  "this is the difference between a usable result and 40,000 files.",
            "-i": "Input file or device to carve from.",
            "-o": "Output directory — must be empty or foremost refuses to run.",
            "-c": "Use a custom configuration file to add signatures.",
            "-a": "Write all headers found, even without a valid footer.",
            "-w": "Write the audit file only, carving nothing — a cheap dry run.",
            "-q": "Quick mode: scan only sector boundaries. Much faster, misses "
                  "embedded files.",
            "-v": "Verbose output.",
        },
        "gotchas": [
            "Carving recovers content but **not filenames or timestamps** — those "
            "live in filesystem metadata that carving bypasses. Use `tsk_recover` "
            "when the filesystem is intact and carve only what it cannot reach.",
            "The output directory must be empty; foremost aborts otherwise. This "
            "trips scripted reruns constantly.",
        ],
    },

    "binwalk": {
        "purpose": "Find and extract embedded files and filesystems inside a binary "
                   "blob or firmware image.",
        "when": {
            "-e": "Extract what is found, rather than only listing it.",
            "-M": "Recurse into extracted files (matryoshka) — for nested firmware.",
            "-d": "Limit recursion depth; unbounded `-M` can explode.",
            "-C": "Choose the output directory for extractions.",
            "-y": "Only report signatures matching this string.",
            "-x": "Exclude signatures matching this string, to cut false hits.",
            "-A": "Scan for executable opcodes to identify architecture.",
            "-E": "Entropy analysis — the fast way to spot encryption or compression.",
        },
        "gotchas": [
            "**Always timeout-guard binwalk in a harness.** Signature scanning on a "
            "large or synthetic image can run effectively forever; this project has "
            "been bitten by exactly that.",
            "`-e -M` on an unknown blob can produce an enormous directory tree. Set "
            "`-d` and carve into a scratch filesystem, not your case directory.",
            "A signature hit is a guess based on magic bytes. Confirm with `file` "
            "or entropy before reporting an embedded filesystem as fact.",
        ],
    },

    "olevba": {
        "purpose": "Extract and analyse VBA macros from Office documents.",
        "when": {
            "-a": "Show only the analysis results, skipping the macro source.",
            "-c": "Show only the macro source code.",
            "-t": "Triage mode — one compact line per file, ideal for a batch.",
            "-d": "Show the deobfuscated macro source.",
            "--decode": "Display all the decoded strings the analyser recovered.",
            "--reveal": "Substitute deobfuscated values back into the source, which "
                        "is the most readable view of a hostile macro.",
            "-p": "Supply a password for an encrypted document.",
            "-z": "Read documents from inside a zip archive.",
            "--show-pcode": "Disassemble the stored p-code — catches macros where "
                            "the VBA source and compiled p-code disagree.",
            "-l": "Set log level when diagnosing a parse failure.",
        },
        "gotchas": [
            "**VBA source and p-code can differ.** Malware abuses this so the "
            "readable source looks benign while the p-code executes. If a document "
            "is suspicious but the source is clean, check `--show-pcode`.",
            "Run this on a copy, in an isolated VM. Nothing here executes the "
            "macro, but the sample itself is still live malware.",
        ],
    },

    "vol": {
        "purpose": "Extract and analyse artifacts from a memory image using "
                   "Volatility 3 plugins.",
        "when": {
            "-f": "The memory image to analyse — required for almost every plugin.",
            "-o": "Directory for files the plugin dumps (processes, DLLs, files).",
            "-r": "Choose the renderer: `csv`/`json` when feeding another tool.",
            "-q": "Quiet — suppress the progress and INFO banner when scripting.",
            "-v": "Increase verbosity while diagnosing a symbol-table failure.",
            "-s": "Point at a local symbol-table directory — the fix for an "
                  "air-gapped host that cannot download symbols.",
            "-p": "Add a directory of custom plugins.",
            "--offline": "Never attempt a network fetch for symbols. Use this on "
                         "evidence networks so a scan cannot stall on a download.",
            "-c": "Load saved configuration from a JSON file.",
        },
        "gotchas": [
            "**Timeout-guard `vol` in any harness.** On a synthetic or truncated "
            "memory image it has pinned a core at 99% indefinitely on this project. "
            "Never run it unbounded in an automated pass.",
            "Volatility 3 takes plugin names, not v2 syntax: `windows.pslist`, not "
            "`--profile=... pslist`. Most 'plugin not found' errors are pasted v2 "
            "commands.",
            "The first run against an unfamiliar image downloads symbol tables. On "
            "an isolated network that hangs — pre-stage symbols and use `--offline`.",
        ],
    },

    "tshark": {
        "purpose": "Read, filter and dissect network captures from the command line.",
        "when": {
            "-r": "Read from a capture file — the normal forensic mode.",
            "-i": "Capture live from an interface instead of reading a file.",
            "-Y": "Apply a *display* filter (Wireshark syntax) after dissection.",
            "-f": "Apply a *capture* filter (BPF syntax) before packets are stored.",
            "-T": "Choose output format; `-T fields` gives parseable columns.",
            "-e": "With `-T fields`, name each field to print. Repeatable.",
            "-c": "Stop after N packets — a fast way to sample a huge capture.",
            "-q": "Suppress per-packet output, for use with `-z` statistics.",
            "-z": "Run a statistics tap (conversations, endpoints, protocol tree).",
            "-n": "Disable name resolution. Also stops DNS lookups leaking from an "
                  "evidence host — use it by default on an investigation.",
            "-w": "Write the (filtered) packets to a new capture file.",
            "-x": "Hex and ASCII dump of packet contents.",
            "-2": "Two-pass analysis, so fields needing later context resolve.",
        },
        "gotchas": [
            "**`-f` and `-Y` are different languages.** `-f` is BPF and applies at "
            "capture time; `-Y` is the Wireshark display filter and applies to a "
            "file. Passing display syntax to `-f` fails, sometimes silently.",
            "Name resolution is on by default and will emit DNS queries from the "
            "analysis host. Use `-n` when touching evidence.",
            "`-T fields` prints nothing useful without at least one `-e`.",
        ],
    },

    "capa": {
        "purpose": "Identify the capabilities of a binary by matching rules against "
                   "its disassembly, mapped to MITRE ATT&CK.",
        "when": {
            "-v": "Verbose: show which rules matched and where.",
            "-j": "JSON output, for feeding a triage pipeline.",
            "-r": "Use an alternate rules directory.",
            "-s": "Point at the library-identification signatures.",
            "-t": "Only run rules carrying a given tag.",
            "--os": "Force the target OS when auto-detection is wrong.",
            "-q": "Quiet output for scripted use.",
            "--restrict-to-functions": "Analyse only the named functions — useful "
                                       "on a large binary you have already triaged.",
        },
        "gotchas": [
            "capa reports *capabilities*, not verdicts. 'Can encrypt data' describes "
            "a backup tool as readily as ransomware — it narrows where to look.",
            "Packed samples yield almost nothing useful. Unpack first, or capa will "
            "just describe the packer stub.",
        ],
    },

    "strings": {
        "purpose": "Print sequences of printable characters found in a binary file.",
        "when": {
            "-n": "Minimum length. Default 4 is noisy; 8–10 cuts most false hits.",
            "-o": "Print the byte offset of each string — lets you seek back to it.",
            "-U": "Control how unicode is handled; needed for UTF-16 Windows strings.",
        },
        "gotchas": [
            "GNU `strings` reads only initialised, loaded sections by default. Use "
            "`-a` to scan the whole file — malware routinely hides outside them.",
            "It finds ASCII by default and will miss UTF-16LE strings that Windows "
            "binaries are full of. When a PE looks empty, that is usually why — "
            "reach for `floss` instead.",
        ],
    },

    "tsk_recover": {
        "purpose": "Bulk-export files from an image to a directory.",
        "when": {
            "-a": "Recover allocated (live) files only.",
            "-e": "Recover every file, allocated and deleted — the usual choice.",
            "-d": "Recover from a specified directory inode rather than the root.",
            "-o": "Partition offset in sectors, from `mmls`.",
            "-f": "Force the filesystem type.",
            "-i": "Image format for non-raw evidence.",
        },
        "gotchas": [
            "Default behaviour recovers only *deleted* files, which surprises people "
            "expecting a full export. Use `-e` for everything.",
            "This preserves paths and names, unlike carving. Prefer it whenever the "
            "filesystem metadata is intact, and carve only what it cannot reach.",
        ],
    },

    "log2timeline.py": {
        "purpose": "Extract timestamped events from evidence into a Plaso storage "
                   "file, the first half of a super-timeline.",
        "when": {
            "--parsers": "Restrict to specific parsers. A targeted run is minutes "
                         "instead of hours.",
            "--storage_file": "Where the .plaso output goes.",
            "-f": "Use a file filter to limit what gets processed.",
            "--hashers": "Compute hashes during extraction, saving a second pass.",
            "--workers": "Number of worker processes; tune to the host's cores.",
            "--status_view": "Change progress display; `none` for clean logs.",
            "--vss_stores": "Also process Volume Shadow Copies — often where the "
                            "pre-attack state survives.",
            "-z": "Time zone of the source machine.",
        },
        "gotchas": [
            "This produces a .plaso database, **not** a timeline you can read. "
            "`psort.py` is the second half; running only this looks like nothing "
            "happened.",
            "A full run on a disk image can take hours and tens of GB. Scope with "
            "`--parsers` unless you genuinely need everything.",
        ],
    },

    "psort.py": {
        "purpose": "Filter, sort and output the events in a Plaso storage file.",
        "when": {
            "-o": "Output format — `l2tcsv`, `dynamic`, `json`, or a timeline tool.",
            "-w": "Write output to a file rather than stdout.",
            "-q": "Quiet, for scripted runs.",
            "--analysis": "Run analysis plugins (tagging, sessionizing) over events.",
        },
        "gotchas": [
            "The date filter is a positional argument, not a flag. Filtering to the "
            "incident window is what makes a multi-million-event timeline usable.",
            "Output ordering follows the storage file, so always sort or filter "
            "explicitly rather than assuming chronology.",
        ],
    },

    "upx": {
        "purpose": "Pack and unpack executables with the UPX compressor.",
        "when": {
            "-d": "Decompress — the only flag you normally want in analysis.",
            "-t": "Test the file's integrity without writing anything.",
            "-l": "List compression info about the file.",
            "-k": "Keep a backup of the original file.",
            "-f": "Force the operation on a file UPX considers questionable.",
            "-q": "Quiet output.",
        },
        "gotchas": [
            "**Work on a copy.** `upx -d` rewrites the file in place, mutating your "
            "sample and invalidating its hash.",
            "Malware routinely uses a modified UPX header so stock `upx -d` refuses. "
            "Failure to unpack is itself an indicator, not a dead end.",
        ],
    },

    "xortool": {
        "purpose": "Recover the key length and key of an XOR-encrypted file by "
                   "frequency analysis.",
        "when": {
            "-l": "Fix the key length when you already know it.",
            "-c": "Give the most frequent character of the plaintext — usually `20` "
                  "(space) for text, `00` for binaries. This is the flag that makes "
                  "or breaks the attack.",
            "-m": "Maximum key length to consider.",
            "-b": "Brute-force the most frequent character rather than guessing.",
        },
        "gotchas": [
            "Output lands in an `xortool_out/` directory, not stdout. People "
            "routinely think it did nothing.",
            "`-c 00` is right far more often than the default for packed binaries, "
            "because null padding dominates.",
        ],
    },

    "pdfid": {
        "purpose": "Count the PDF tags that make a document *do* something, "
                   "and print the tally. A PDF is a set of objects, and a "
                   "handful of tag names are the ones that can execute or "
                   "fetch: `/JavaScript` and `/JS` carry script, `/OpenAction` "
                   "and `/AA` run something when the file opens or on an "
                   "event, `/Launch` starts an external program, "
                   "`/EmbeddedFile` carries another file inside this one, and "
                   "`/URI` reaches the network. A normal invoice has none of "
                   "them. Output is one line per tag with a count, so the "
                   "judgement is simply: are any non-zero, and does this "
                   "document have any business containing them? It parses "
                   "nothing and decodes nothing -- it is the ten-second look "
                   "that tells you whether to spend an hour with pdf-parser.",
        "when": {
            "-s": "Scan a directory of PDFs rather than a single file.",
            "-a": "Display all keyword counts, including zero entries.",
            "-e": "Include extra keywords beyond the default set.",
            "-d": "Disarm the PDF — neutralise /JS and /JavaScript. Produces a "
                  "safe-to-open copy; never overwrite the original.",
            "-n": "Hide zero-count keywords to shorten the output.",
            "-c": "CSV output for batch triage.",
            "-m": "Only report files scoring above a minimum, for a large sweep.",
        },
        "gotchas": [
            "`pdfid` **counts keywords; it does not parse**. A high `/JS` count is a "
            "reason to look, not proof of malice — and a crafted PDF can hide "
            "content from it. Follow up with `pdf-parser`.",
            "`/OpenAction` plus `/JS` is the classic auto-execute pair worth "
            "prioritising in triage.",
        ],
    },

    # --- Acquisition -------------------------------------------------------
    # The E01 workflow: acquire, inspect, verify, convert. This is the first
    # step of every investigation and was the least documented part of the
    # guide until the tools existed in the kit to capture from.

    "ewfacquire": {
        "purpose": "Acquire a disk, volume or device into an EWF/E01 evidence "
                   "container, with the case metadata and hashes stored inside "
                   "the image itself.",
        "when": {
            "-t": "Set the output name, without extension — ewfacquire appends "
                  "`.E01`, `.E02`… itself. The one flag you always pass.",
            "-2": "Write a second copy in the same pass. Two independent copies "
                  "for the cost of one read, which matters when the source is "
                  "failing and may not survive a second acquisition.",
            "-c": "Trade size against time. `best` on a slow USB source is often "
                  "faster overall than `none`, because the bottleneck is the "
                  "read, not the CPU.",
            "-d": "Add sha1 or sha256 alongside the default md5. Worth doing "
                  "once, at acquisition: md5 alone is increasingly challenged, "
                  "and rehashing later means reading the whole image again.",
            "-C": "Case number, stored in the image header.",
            "-D": "Description, stored in the image header.",
            "-e": "Examiner name, stored in the image header.",
            "-E": "Evidence number, stored in the image header.",
            "-N": "Free-text notes, stored in the image header. These five "
                  "metadata flags are the reason to choose E01 over a raw `dd` "
                  "image: the container describes its own provenance.",
            "-f": "Choose the EWF variant. `encase6` is the safe default for "
                  "interoperability; pick the format the tool that will read it "
                  "expects, not the newest one available.",
            "-S": "Segment size. The 1.4 GiB default suits FAT32 and optical "
                  "media; raise it on a modern filesystem to avoid hundreds of "
                  "fragments.",
            "-b": "Sectors per chunk. Larger chunks read faster but lose more "
                  "data to each unreadable sector.",
            "-g": "Error granularity — how much data around a bad sector is "
                  "discarded. Lower values preserve more of a failing disk at "
                  "the cost of speed.",
            "-r": "Read retries before giving up on a sector. Raise it for a "
                  "dying drive; lower it when retries are heating a drive that "
                  "may not survive the acquisition.",
            "-w": "Zero unreadable sectors instead of aborting, the way EnCase "
                  "does. Keeps offsets aligned so the filesystem still parses.",
            "-R": "Resume an interrupted acquisition at a safe point, instead of "
                  "restarting a multi-hour read.",
            "-u": "Unattended — suppresses the interactive prompts. Required "
                  "for any scripted or headless acquisition.",
            "-q": "Minimal status output, for logs.",
            "-l": "Write the acquisition log, including errors and hashes, to a "
                  "file. This is the record you cite later; do not skip it.",
            "-o": "Start at an offset rather than sector 0.",
            "-B": "Acquire a fixed number of bytes rather than the whole device — "
                  "with `-o`, the way to image one region.",
            "-m": "Record the media type (fixed, removable, optical, memory) in "
                  "the header.",
            "-M": "Record whether this is a physical device or a logical volume.",
            "-P": "Override bytes-per-sector. Needed on 4Kn drives where the "
                  "512-byte assumption is wrong.",
            "-p": "Process buffer size — a throughput tuning knob.",
            "-T": "Supply a CUE file when imaging optical media, so the track "
                  "layout is preserved.",
            "-s": "Swap byte pairs for a big-endian source. Rare, and wrong "
                  "unless you know the source endianness differs.",
            "-A": "Header codepage, for non-ASCII metadata.",
            "-x": "Bypass the buffered read/write path.",
            "-v": "Verbose diagnostics to stderr — worth capturing alongside "
                  "`-l` when a source is throwing read errors.",
        },
        "gotchas": [
            "The case metadata flags default to literal placeholder strings — "
            "`case_number`, `examiner_name`, `evidence_number`. Omit them and the "
            "image ships with those placeholders recorded as fact, which is worse "
            "than an empty field because it looks filled in.",
            "`-t` takes the name **without** an extension. Passing `image.E01` "
            "produces `image.E01.E01`.",
            "Acquisition is not verification. `ewfacquire` records hashes; proving "
            "the image still matches them later is `ewfverify`.",
        ],
    },

    "ewfinfo": {
        "purpose": "Show the metadata, hashes and acquisition details recorded "
                   "inside an EWF/E01 image.",
        "when": {
            "-i": "Acquisition details only — who imaged it, when, with what.",
            "-m": "Media details only — geometry, sector size, media type.",
            "-e": "Read errors recorded at acquisition. Check this before "
                  "trusting a clean-looking image: unreadable sectors are noted "
                  "here, not in the filesystem.",
            "-f": "Emit DFXML instead of text, when the output feeds a tool "
                  "rather than a person.",
            "-d": "Date format. `iso8601` is the unambiguous choice for a report.",
            "-A": "Header codepage, for images with non-ASCII metadata.",
            "-v": "Verbose diagnostics to stderr.",
        },
        "gotchas": [
            "This reads the header only. It reports the hash that was recorded at "
            "acquisition; it does not recompute it, so it cannot tell you the "
            "image is still intact. Use `ewfverify` for that.",
        ],
    },

    "ewfverify": {
        "purpose": "Recompute an EWF/E01 image's hashes and check them against "
                   "the values stored at acquisition.",
        "when": {
            "-d": "Also verify an additional digest such as sha256, when one was "
                  "recorded at acquisition.",
            "-l": "Write the verification result to a log file — the artefact "
                  "worth keeping with the case, not just terminal output.",
            "-q": "Minimal output, for scripted checks.",
            "-f": "Output format.",
            "-p": "Process buffer size.",
            "-A": "Header codepage.",
            "-v": "Verbose diagnostics to stderr.",
            "-w": "Wipe sectors that could not be read.",
            "-x": "Bypass the buffered read/write path.",
        },
        "gotchas": [
            "This reads every byte, so it takes as long as the acquisition did. "
            "Budget for that rather than discovering it mid-deadline.",
            "A pass proves the image matches what was recorded **at acquisition**. "
            "It says nothing about whether the acquisition captured the device "
            "correctly — a disk failing mid-image produces a verifiable image of "
            "incomplete data.",
        ],
    },

    "ewfexport": {
        "purpose": "Convert an EWF/E01 image to raw, or to another EWF format, "
                   "including extracting a subset of it.",
        "when": {
            "-t": "Target name. `-` writes to stdout, which lets the image be "
                  "piped straight into another tool without staging a full raw "
                  "copy on disk.",
            "-f": "Output format — `raw` for tools that cannot read EWF, or "
                  "another EWF variant for compatibility.",
            "-o": "Start offset, to export a region rather than the whole image.",
            "-B": "Number of bytes to export — with `-o`, extracts one partition.",
            "-S": "Segment size for the output.",
            "-c": "Compression for an EWF target.",
            "-d": "Calculate an additional digest over the exported data.",
            "-u": "Unattended, for scripted conversion.",
            "-q": "Minimal output.",
            "-l": "Log the export.",
            "-s": "Swap byte pairs.",
            "-b": "Sectors per chunk.",
            "-p": "Process buffer size.",
            "-A": "Header codepage.",
            "-v": "Verbose diagnostics to stderr.",
            "-w": "Zero sectors that cannot be read.",
            "-x": "Bypass the buffered read/write path.",
        },
        "gotchas": [
            "Exporting to raw discards the metadata and hashes that justified "
            "using E01. Keep the original: the raw copy is a working artefact, "
            "not the evidence.",
            "A raw export needs the full uncompressed size in free space. E01 "
            "compression routinely hides a 2 TB image inside 700 GB.",
        ],
    },

    # --- The Sleuth Kit, remainder -----------------------------------------
    # fls, icat, istat and mmls are already curated. These four complete the
    # set. Every TSK tool shares -f/-i/-b/-o/-P/-B/-v/-V, so the shared flags
    # are explained the same way on each page rather than differently, which
    # is what a reader flipping between them needs.

    "fsstat": {
        "purpose": "Report a filesystem's layout and parameters: type, block "
                   "size, inode range, and the geometry every other TSK tool "
                   "needs.",
        "when": {
            "-t": "Print only the filesystem type. The scriptable form when all "
                  "you need is a yes/no on what this volume is.",
            "-f": "Force the filesystem type when detection is wrong or the "
                  "superblock is damaged (`-f list` shows the options).",
            "-o": "Offset, in **sectors**, of the filesystem inside the image. "
                  "Take it from `mmls`; this is the flag that ties the two "
                  "tools together.",
            "-i": "Set the image format for non-raw evidence such as E01 or AFF.",
            "-b": "Device sector size. Needed on 4Kn drives, where the 512-byte "
                  "default silently computes every offset wrong.",
            "-P": "Pool type, for APFS or LVM containers that hold the volume.",
            "-B": "Starting block within a pool volume.",
            "-k": "Password for an encrypted volume.",
            "-v": "Verbose diagnostics to stderr, useful when detection fails.",
        },
        "gotchas": [
            "Run this first. Block size and inode range from `fsstat` are what "
            "make `blkls`, `icat` and `ils` output interpretable — starting "
            "anywhere else means guessing at the numbers they print.",
            "If it reports the wrong type or refuses the volume, the `-o` offset "
            "is wrong far more often than the image is corrupt.",
        ],
    },

    "ffind": {
        "purpose": "Find the file name that points at a given inode — the "
                   "reverse of a directory lookup.",
        "when": {
            "-a": "Show every name for the inode. Hard-linked files have more "
                  "than one, and stopping at the first hides that.",
            "-d": "Deleted names only. The direct answer to \"what was this "
                  "inode called before it was removed?\"",
            "-u": "Undeleted names only, when a recycled inode is returning "
                  "stale hits.",
            "-f": "Force the filesystem type (`-f list` shows the options).",
            "-o": "Offset, in sectors, from `mmls`.",
            "-i": "Image format for non-raw evidence such as E01 or AFF.",
            "-b": "Device sector size; required on 4Kn drives.",
            "-P": "Pool type, for APFS or LVM containers.",
            "-B": "Starting block within a pool volume.",
            "-v": "Verbose diagnostics to stderr.",
        },
        "gotchas": [
            "Inodes are reused. A name returned for a deleted inode may belong "
            "to whatever claimed it next, not to the file you are chasing — "
            "corroborate with `istat` timestamps before naming it in a report.",
            "This is the tool for the question `icat` provokes: you carved data "
            "out by inode and now need to say what it was called.",
        ],
    },

    "blkls": {
        "purpose": "Extract filesystem blocks — by default the unallocated "
                   "ones, which is the input a carver wants.",
        "when": {
            "-A": "Unallocated blocks. The default and the usual intent: pipe "
                  "this into `foremost` or `scalpel` so the carver reads only "
                  "free space instead of the whole image.",
            "-a": "Allocated blocks only — the inverse, when isolating live data.",
            "-e": "Every block, including filesystem metadata.",
            "-s": "Slack space only: the tail of the last block of each file, "
                  "where fragments of previous contents survive. A distinct "
                  "hunt from carving free space, and it ignores the other flags.",
            "-l": "List block details rather than emitting their contents.",
            "-f": "Force the filesystem type (`-f list` shows the options).",
            "-o": "Offset, in sectors, from `mmls`.",
            "-i": "Image format for non-raw evidence such as E01 or AFF.",
            "-b": "Device sector size; required on 4Kn drives.",
            "-P": "Pool type, for APFS or LVM containers.",
            "-B": "Starting block within a pool volume.",
            "-v": "Verbose diagnostics to stderr.",
        },
        "gotchas": [
            "Output goes to stdout and is the size of the free space — redirect "
            "it to a file on a volume that can hold it, not into a pager.",
            "Block offsets in the extracted stream do **not** match offsets in "
            "the original image, because only unallocated blocks were written. "
            "Use `-l` if you need to map a hit back to its real location.",
        ],
    },

    "ils": {
        "purpose": "List inode metadata, including inodes that no longer have a "
                   "name pointing at them.",
        "when": {
            "-p": "Orphan inodes — allocated content with no directory entry. "
                  "Files that were unlinked while still open, and a standard "
                  "hiding place worth checking explicitly.",
            "-O": "Unallocated inodes that were still open at the time of "
                  "imaging (UFS/ExtX). The same trick, caught mid-deletion.",
            "-e": "Every inode, allocated or not.",
            "-a": "Allocated inodes only.",
            "-A": "Unallocated inodes only — deleted file metadata that often "
                  "survives after the name is gone.",
            "-l": "Linked inodes (a name still points at them).",
            "-L": "Unlinked inodes (nothing does).",
            "-z": "Unused inodes.",
            "-Z": "Used inodes.",
            "-m": "mactime format — the form `mactime` consumes to build a "
                  "timeline. This is how deleted-file metadata reaches the "
                  "timeline at all.",
            "-s": "Correct for a known clock skew on the source machine, in "
                  "seconds, so times line up with other evidence.",
            "-f": "Force the filesystem type (`-f list` shows the options).",
            "-o": "Offset, in sectors, from `mmls`.",
            "-i": "Image format for non-raw evidence such as E01 or AFF.",
            "-b": "Device sector size; required on 4Kn drives.",
            "-P": "Pool type, for APFS or LVM containers.",
            "-B": "Starting block within a pool volume.",
            "-v": "Verbose diagnostics to stderr.",
        },
        "gotchas": [
            "`ils` finds metadata with no name; `ffind` turns an inode back into "
            "a name; `icat` extracts its content. Deleted-file work is usually "
            "all three in sequence.",
            "An inode surviving does not mean its data did. The blocks it points "
            "at may already be reallocated, so `icat` can return another file's "
            "contents entirely.",
        ],
    },

    # --- Windows artifacts, Eric Zimmerman's tools -------------------------
    # These share a house style: -f or -d for input, --csv/--json/--html for
    # output, --vss, --dedupe, --dt. Explaining the shared flags identically on
    # each page is deliberate; a reader moving between them should not have to
    # re-read the same idea in different words.

    "PECmd": {
        "purpose": "Parse Windows Prefetch files into evidence of what executed, "
                   "when, how often, and which files each run touched.",
        "when": {
            "-d": "Recurse a directory — the normal mode, since Prefetch is only "
                  "meaningful as a set. Point it at `C:\\Windows\\Prefetch`.",
            "-f": "A single .pf file, when chasing one binary.",
            "--csv": "Write CSV to a directory. This is the output that matters: "
                     "Prefetch is a timeline source, and Timeline Explorer or a "
                     "spreadsheet is where the pattern shows up.",
            "--csvf": "Override the generated CSV filename.",
            "--json": "JSON output, when the results feed another tool.",
            "--jsonf": "Override the generated JSON filename.",
            "--html": "XHTML report, for handing to someone who will not open a CSV.",
            "-k": "Highlight extra keywords in the output. `temp` and `tmp` are "
                  "highlighted by default; add the names you are hunting.",
            "-o": "Save the decompressed Prefetch bytes. Win10+ Prefetch is "
                  "MAM-compressed, so this is how you get something another tool "
                  "or a hex editor can read.",
            "-q": "Suppress the per-file detail. Worth it on a large directory "
                  "when the CSV is the real output.",
            "--vss": "Also parse every Volume Shadow Copy on the drive. Prefetch "
                     "rolls over at 1024 entries on Win10+, so shadow copies are "
                     "often the only place an older execution still exists.",
            "--dedupe": "Drop duplicates by SHA-1 across the source and the shadow "
                        "copies. Effectively mandatory with `--vss`, which "
                        "otherwise returns the same file many times over.",
            "--dt": "Custom timestamp format for the output.",
            "--mp": "Higher-precision timestamps, when ordering events within the "
                    "same second matters.",
        },
        "gotchas": [
            "Prefetch proves a program **ran**; it does not prove who ran it or "
            "what it did. Pair it with event logs or `AmcacheParser` before "
            "attributing anything.",
            "Absence is not evidence of absence. Prefetch can be disabled, is "
            "commonly off on SSD-era server builds, and rolls over — a missing "
            "entry means nothing on its own.",
            "The last-run timestamps are the eight most recent executions only. "
            "Older runs are gone from the file even though the run count keeps "
            "counting them.",
        ],
    },

    "EvtxECmd": {
        "purpose": "Parse Windows event logs into a normalised, filterable CSV, "
                   "mapping the useful fields out of the XML payload.",
        "when": {
            "-d": "Recurse a directory of .evtx files — the usual mode when "
                  "working from a collected `winevt\\Logs`.",
            "-f": "A single log, when you already know which one matters.",
            "--csv": "Write CSV to a directory. The normal output, and the form "
                     "the rest of a timeline workflow expects.",
            "--csvf": "Override the generated CSV filename.",
            "--json": "JSON output, for feeding another tool.",
            "--jsonf": "Override the generated JSON filename.",
            "--xml": "XML output.",
            "--xmlf": "Override the generated XML filename.",
            "--inc": "Process only these Event IDs. The fastest way to cut a "
                     "multi-gigabyte log down to the question being asked — "
                     "ranges are allowed (`4624,4625,5410-5500`).",
            "--exc": "Process everything except these Event IDs. `--inc` wins if "
                     "both are given.",
            "--sd": "Drop events older than this date (UTC).",
            "--ed": "Drop events newer than this date (UTC). With `--sd`, scopes "
                    "the parse to the incident window instead of all history.",
            "--maps": "Where the event maps live. The maps are what turn raw XML "
                      "into named columns; without the right ones, useful fields "
                      "stay buried in the payload.",
            "--sync": "Pull the latest maps from upstream. Worth doing before a "
                      "big parse — map coverage improves continuously.",
            "--vss": "Also parse every Volume Shadow Copy on the drive, which is "
                     "where cleared or rotated logs may survive.",
            "--dedupe": "Drop duplicates by SHA-1 across the source and shadow "
                        "copies. Use it whenever `--vss` is on.",
            "--tdt": "Seconds of tolerance for time-discrepancy detection — flags "
                     "records whose timestamps disagree, a clock-tampering signal.",
            "--fj": "Export all available data in JSON rather than the mapped "
                    "subset.",
            "--met": "Show per-log metrics about what was processed.",
            "--dt": "Custom timestamp format for the output.",
        },
        "gotchas": [
            "Without a map for an Event ID, the interesting values stay inside "
            "the XML payload rather than becoming columns. If an expected field "
            "is missing, the map is usually the reason, not the log.",
            "A cleared log is itself the finding: Security 1102 and System 104 "
            "record the clearing. Include them explicitly when hunting "
            "anti-forensics.",
            "Event log timestamps are recorded in UTC but `--sd`/`--ed` are only "
            "as good as your assumption about the host's clock. Corroborate "
            "before building a timeline on them.",
        ],
    },

    "AmcacheParser": {
        "purpose": "Parse Amcache.hve — the record of programs present on a "
                   "host, with SHA-1 hashes, including binaries that have since "
                   "been deleted.",
        "when": {
            "-f": "The Amcache.hve to parse.",
            "-i": "Include file entries associated with Programs entries. More "
                  "complete, and noisier.",
            "-b": "Whitelist of SHA-1 hashes to include.",
            "-w": "Blacklist of SHA-1 hashes to exclude. Blacklisting overrides "
                  "whitelisting, so a hash in both is dropped — the safe default "
                  "when suppressing known-good noise.",
            "--csv": "Write CSV to a directory. The usual output.",
            "--csvf": "Override the generated CSV filename.",
            "--nl": "Ignore transaction logs for a dirty hive. Leave this off "
                    "unless you know why you want it: skipping the logs means "
                    "parsing a hive that is missing its most recent changes.",
            "--dt": "Custom timestamp format for the output.",
            "--mp": "Higher-precision timestamps.",
        },
        "gotchas": [
            "Amcache records that a binary was **present**, not that it ran. It "
            "is evidence of existence; Prefetch and event logs are evidence of "
            "execution. Conflating the two is the standard error with this "
            "artifact.",
            "It carries SHA-1 for entries, which makes it the fastest way to tie "
            "a deleted binary to threat intelligence long after the file is gone.",
            "The hive is usually dirty when collected from a live host. Let the "
            "transaction logs replay — the entries only in the logs are the most "
            "recent, which is normally the part you care about.",
        ],
    },

    # --- Memory and bulk data ----------------------------------------------
    # volatility3 and bulk_extractor both list short and long forms as separate
    # rows, so both spellings are annotated. Saying "see -x" on the long form
    # would leave whichever one the reader looked up first unexplained.

    "volatility3": {
        "purpose": "Analyse a memory image. These are the framework-wide "
                   "options; each plugin adds its own, shown by "
                   "`volatility3 <plugin> --help`.",
        "when": {
            "-f": "The memory image. Almost every invocation starts here.",
            "--file": "The memory image. Almost every invocation starts here.",
            "-r": "Output renderer. `csv` or `jsonl` when the result feeds "
                  "another tool; `pretty` is for reading, not for parsing.",
            "--renderer": "Output renderer. `csv` or `jsonl` when the result "
                          "feeds another tool; `pretty` is for reading.",
            "-o": "Directory for files the plugin writes — dumped processes, "
                  "extracted DLLs. Required before any `--dump` plugin option "
                  "does anything useful.",
            "--output-dir": "Directory for files the plugin writes. Required "
                            "before any `--dump` plugin option is useful.",
            "-s": "Where to find symbol tables. The usual fix when a Linux or "
                  "macOS image will not resolve: the ISF for that exact kernel "
                  "has to be reachable.",
            "--symbol-dirs": "Where to find symbol tables — the usual fix when a "
                             "Linux or macOS image will not resolve.",
            "--offline": "Never fetch symbols online. Use it on an analysis host "
                         "that must not touch the network, and expect failures "
                         "unless the ISFs are already local.",
            "-u": "Point at an alternative ISF repository.",
            "--remote-isf-url": "Point at an alternative ISF repository.",
            "--clear-cache": "Drop cached items. First thing to try when results "
                             "look stale or an image was replaced in place.",
            "--cache-path": "Move the cache somewhere with room; it grows.",
            "--parallelism": "Enable process or thread parallelism. Off by "
                             "default, and worth turning on for a long scan.",
            "--filters": "Filter rows as `[+-]column,pattern`, so a plugin that "
                         "returns thousands of rows can be narrowed without a "
                         "second pass.",
            "--hide-columns": "Drop columns from the output to keep a wide table "
                              "readable.",
            "-p": "Additional plugin directories, for plugins outside the tree.",
            "--plugin-dirs": "Additional plugin directories.",
            "-l": "Also write output to a log file.",
            "--log": "Also write output to a log file.",
            "-q": "Suppress progress feedback, for scripted runs.",
            "--quiet": "Suppress progress feedback, for scripted runs.",
            "-v": "More verbose output; repeat for more.",
            "--verbosity": "More verbose output; repeat for more.",
            "-c": "Load options from a JSON config.",
            "--config": "Load options from a JSON config.",
            "-e": "Override a single configuration setting.",
            "--extend": "Override a single configuration setting.",
            "--write-config": "Write the resolved configuration to config.json — "
                              "useful for making a complex run reproducible.",
            "--save-config": "Write the resolved configuration to a named file.",
            "--single-location": "The image URI, when it is not a plain local "
                                 "file (`-f` is shorthand for this).",
            "--single-swap-locations": "Supply swap files alongside the image, so "
                                       "paged-out memory can be resolved.",
            "--stackers": "Control the layer stackers used to interpret the image.",
        },
        "gotchas": [
            "Symbols are the usual failure, not the image. Windows profiles are "
            "generated automatically, but Linux and macOS need an ISF matching "
            "the exact kernel build — same version is not enough.",
            "Volatility 3 dropped the Volatility 2 profile system entirely, so "
            "`--profile` from older notes and blog posts does not exist here.",
            "It has pinned CPU indefinitely on a malformed image before. Run long "
            "analyses under a timeout rather than assuming progress.",
        ],
    },

    "bulk_extractor": {
        "purpose": "Scan an image for features — email addresses, URLs, credit "
                   "card numbers, EXIF, keys — without parsing the filesystem "
                   "at all, so deleted and unallocated content is included.",
        "when": {
            "-o": "Output directory. Required, and it must not already exist "
                  "unless you also pass `-Z`.",
            "--outdir": "Output directory. Required.",
            "-E": "Run exactly one scanner and disable the rest. The fastest way "
                  "to answer a single question instead of a full sweep.",
            "--enable_exclusive": "Run exactly one scanner and disable the rest.",
            "-e": "Enable a scanner that is off by default, repeatable.",
            "--enable": "Enable a scanner that is off by default, repeatable.",
            "-x": "Disable a scanner, repeatable. Turning off the noisy ones is "
                  "usually a bigger speed win than adding threads.",
            "--disable": "Disable a scanner, repeatable.",
            "-f": "Search for a regex pattern, repeatable.",
            "--find": "Search for a regex pattern, repeatable.",
            "-F": "Read search patterns from a file — the practical form when "
                  "hunting a list of indicators.",
            "--find_file": "Read search patterns from a file.",
            "--find-case-sensitive": "Make `-f`/`-F` case-sensitive; they are not "
                                     "by default.",
            "-w": "Stop list: features to suppress. This is how you cut the "
                  "known-good noise that otherwise buries the findings.",
            "--stop_list": "Stop list of features to suppress.",
            "-r": "Alert list: features to flag prominently — the inverse of a "
                  "stop list, for known-bad indicators.",
            "--alert_list": "Alert list of features to flag prominently.",
            "-j": "Thread count. Defaults to the core count; lower it when the "
                  "scan is competing with other work.",
            "--threads": "Thread count.",
            "-J": "Single-threaded. Slow, but the first thing to try when a scan "
                  "crashes or results look non-deterministic.",
            "--no_threads": "Single-threaded — use when debugging a crash.",
            "-s": "Random sampling as `frac[:passes]`. Scans a fraction of a huge "
                  "image to judge whether a full run is worth the hours.",
            "--sampling": "Random sampling as `frac[:passes]`.",
            "-Y": "Restrict the scan to a byte range, when `mmls` already told "
                  "you which region matters.",
            "--scan": "Restrict the scan to a `<start>[-end]` byte range.",
            "-R": "Treat the input as a directory and recurse it, rather than as "
                  "a disk image.",
            "--recurse": "Treat the input as a directory and recurse it.",
            "-C": "Bytes of context stored around each hit. Raise it when a bare "
                  "match is not enough to judge relevance.",
            "--context_window": "Bytes of context stored around each hit.",
            "-M": "Maximum recursion depth into nested containers. Lower it if a "
                  "zip bomb or deeply nested archive stalls the scan.",
            "--max_depth": "Maximum recursion depth into nested containers.",
            "-Z": "Wipe the output directory first. Convenient for reruns and "
                  "destructive by definition — never point it at a directory "
                  "holding results you still need.",
            "--zap": "Wipe the output directory first — destructive.",
            "-q": "Suppress status and performance output.",
            "--quit": "Suppress status and performance output.",
            "-H": "Report what each scanner does. Worth reading once; the scanner "
                  "set is the tool.",
            "--info_scanners": "Report what each scanner does.",
            "-S": "Set a scanner option as `name=value`, repeatable.",
            "--set": "Set a scanner option as `name=value`, repeatable.",
            "-P": "Additional directories to load scanner plugins from.",
            "--scanner_dir": "Additional directories to load scanner plugins from.",
            "-A": "Add an offset to reported feature locations — use it when "
                  "scanning a carved fragment so offsets still refer to the "
                  "original image.",
            "--offset_add": "Add an offset to reported feature locations.",
            "-b": "Prepend a banner file to every feature file, e.g. a case "
                  "header.",
            "--banner_file": "Prepend a banner file to every feature file.",
            "-G": "Page size read per pass.",
            "--pagesize": "Page size read per pass.",
            "-g": "Margin carried between pages, so a feature spanning a page "
                  "boundary is still found.",
            "--marginsize": "Margin carried between pages, so features spanning a "
                            "page boundary are still found.",
            "-z": "Start at a given page number, to resume a long scan.",
            "--page_start": "Start at a given page number.",
            "-p": "Print the value at a path, with optional length and hex or raw "
                  "output — inspection rather than scanning.",
            "--path": "Print the value at a path, for inspection rather than "
                      "scanning.",
            "--log-level": "Diagnostic log level.",
            "--log-file": "Diagnostic log file; defaults inside the output "
                          "directory.",
            "-d": "Debug-level diagnostic logging.",
            "--max_minute_wait": "How long to wait for all data to be read before "
                                 "giving up — raise it for slow or failing media.",
            "--max_bad_alloc_errors": "Allocation failures tolerated before "
                                      "aborting.",
        },
        "gotchas": [
            "It ignores the filesystem completely. That is the point — it finds "
            "content in unallocated space and slack that a filesystem-aware tool "
            "cannot reach — but it also means a hit carries no filename and no "
            "timestamp. Map the offset back with `ffind`/`istat` before naming "
            "a file in a report.",
            "Feature files are raw pattern matches, not verified findings. The "
            "credit-card scanner in particular flags anything passing a Luhn "
            "check, which includes plenty of ordinary numbers.",
            "Output is large and the scan is long. Sample with `-s` on a "
            "multi-terabyte image before committing to a full pass.",
        ],
    },

    # --- Packet capture handling -------------------------------------------

    "editcap": {
        "purpose": "Cut, split, deduplicate and convert capture files — the "
                   "tool that makes an unmanageable pcap workable before "
                   "analysis starts.",
        "when": {
            "-A": "Keep only packets at or after this timestamp.",
            "-B": "Keep only packets before this timestamp. With `-A`, this is "
                  "how a multi-gigabyte capture becomes the incident window.",
            "-c": "Split into files of N packets each. The standard fix for a "
                  "capture too large for Wireshark to open.",
            "-i": "Split into files covering N seconds each — the same fix, when "
                  "time is the natural unit.",
            "-d": "Drop duplicate packets using the default 5-packet window. "
                  "Captures taken from a SPAN port routinely see each packet "
                  "twice, which distorts every count downstream.",
            "-D": "Drop duplicates with an explicit window, when `-d`'s default "
                  "is too narrow.",
            "-w": "Drop duplicates within a time window rather than a packet "
                  "count.",
            "--novlan": "Ignore VLAN tags when comparing for duplicates, so the "
                        "same frame seen on two VLANs collapses to one.",
            "-r": "Invert the selection: keep the specified packets instead of "
                  "deleting them. Easy to forget, and it reverses the meaning of "
                  "the whole command.",
            "-s": "Truncate each packet to N bytes. Strips payload while keeping "
                  "headers — the usual way to share a capture without its "
                  "contents.",
            "-L": "Adjust the recorded frame length to match after truncating, so "
                  "the file is not self-inconsistent.",
            "-t": "Shift every timestamp by a relative amount. This is how a "
                  "capture from a host with a skewed clock is aligned to the "
                  "rest of the timeline.",
            "-F": "Output file format; pcapng by default. An empty `-F` lists "
                  "the choices.",
            "-T": "Output encapsulation type, when the link type must change.",
            "--discard-all-secrets": "Strip embedded decryption secrets before "
                                     "handing the file to someone else.",
            "--capture-comment": "Attach a comment to the file — a place to "
                                 "record provenance that travels with the "
                                 "capture.",
            "--discard-capture-comment": "Remove existing comments on output.",
            "-I": "Ignore N leading bytes when comparing for duplicates.",
            "-o": "With `-E`, skip bytes before introducing errors.",
            "--seed": "With `-E`, fix the random seed so a corrupted-capture test "
                      "is reproducible.",
            "-V": "Verbose; with the duplicate options it reports what was "
                  "removed rather than silently dropping packets.",
        },
        "gotchas": [
            "`-r` inverts the selection. Without it the named packets are "
            "**deleted**, which is the opposite of what most people intend the "
            "first time.",
            "Deduplication is a heuristic over a window, not a proof. A genuine "
            "retransmission looks like a duplicate, and dropping it destroys the "
            "evidence that a retransmission occurred.",
            "Splitting renumbers packets per output file. Frame numbers cited "
            "from a split file do not refer to the original capture.",
        ],
    },

    "ngrep": {
        "purpose": "Grep packet payloads, live or from a capture, with BPF "
                   "filtering — pattern matching on the wire.",
        "when": {
            "-I": "Read from a pcap file instead of an interface. The safe mode: "
                  "no capture privileges and no risk of touching live traffic.",
            "-O": "Write matched packets to a pcap, turning a search into a "
                  "smaller capture that Wireshark can open.",
            "-i": "Case-insensitive match — usually what you want for protocol "
                  "keywords and hostnames.",
            "-w": "Match the pattern as a whole word, to stop a short string "
                  "matching inside longer ones.",
            "-X": "Treat the pattern as hexadecimal, for matching binary "
                  "signatures rather than text.",
            "-x": "Print payloads as a hexdump — necessary when the protocol is "
                  "not text.",
            "-v": "Invert the match, to see everything that is *not* the known "
                  "traffic.",
            "-t": "Print a timestamp on every match.",
            "-T": "Print the delta since the previous match; twice for delta from "
                  "the first. Useful for spotting beaconing intervals.",
            "-n": "Stop after N packets.",
            "-A": "Also print N packets following each match, for the response to "
                  "the request that matched.",
            "-d": "Choose the capture interface rather than the pcap default.",
            "-p": "Do not enter promiscuous mode — capture only traffic addressed "
                  "to this host.",
            "-s": "Set the BPF capture length.",
            "-S": "Limit how much of a matched packet is shown.",
            "-W": "Output format: `byline` is far more readable for text "
                  "protocols than the default.",
            "-F": "Read the BPF filter from a file, when it is too long to be "
                  "comfortable on a command line.",
            "-M": "Single-line matching instead of multi-line.",
            "-D": "Replay a pcap at its recorded timing rather than as fast as "
                  "possible.",
            "-e": "Show empty packets, which are otherwise hidden.",
            "-q": "Suppress the reception hash marks.",
            "-l": "Line-buffer stdout, so output appears when piped.",
            "-c": "Force the column width.",
            "-P": "Set the character shown for non-printable bytes.",
            "-N": "Show sub-protocol numbers.",
            "-R": "Skip privilege revocation.",
            "-K": "Send packets to kill matched connections. This **writes to the "
                  "network** — it is not an analysis option, and it does not "
                  "belong anywhere near evidence handling.",
        },
        "gotchas": [
            "It matches within individual packets. A string split across TCP "
            "segments will not be found — reassembly is `tshark`'s job, not "
            "this one's.",
            "`-K` is the one flag here that changes the world instead of "
            "observing it. Everything else reads; that one transmits.",
            "Matching payload on a live interface needs capture privileges, and "
            "on a busy link `ngrep` drops packets silently. Capture first, "
            "search the file afterwards, when the answer has to be complete.",
        ],
    },

    "MFTECmd": {
        "purpose": "Parse NTFS metadata files — $MFT, $J, $Boot, $SDS, $I30 — "
                   "into CSV or bodyfile, including entries for deleted files.",
        "when": {
            "-f": "The metadata file to parse. Required, and the file type is "
                  "detected from its contents rather than its name.",
            "-m": "Supply the $MFT alongside a $J. Without it the journal shows "
                  "file names with no path, because the parent directory only "
                  "exists in the $MFT.",
            "--csv": "Write CSV to a directory. The normal output.",
            "--csvf": "Override the generated CSV filename.",
            "--json": "JSON output, for a pipeline.",
            "--jsonf": "Override the generated JSON filename.",
            "--body": "Bodyfile output, which is what `mactime` consumes — the "
                      "bridge from NTFS metadata into a classic timeline.",
            "--bodyf": "Override the generated bodyfile name.",
            "--bdl": "Drive letter to record in the bodyfile. Required with "
                     "`--body`, because a bodyfile path is meaningless without "
                     "the volume it came from.",
            "--blf": "Use LF rather than CRLF, when the output is going to a "
                     "Unix toolchain.",
            "--de": "Dump full detail for one entry, as `Entry` or `Entry-Seq`. "
                    "The flag for interrogating a single suspicious file.",
            "--fls": "List a directory's contents from the $MFT, for the entry "
                     "given by `--de`.",
            "--dd": "Directory to write an exported FILE record to.",
            "--do": "Offset of the FILE record to dump, decimal or hex.",
            "--ds": "Dump a security descriptor from $SDS by Id — how you get "
                    "from a file to the ACL that was on it.",
            "--dr": "Dump resident files out of the $MFT. Small files live "
                    "entirely inside their MFT record, so this recovers content "
                    "with no data runs to follow.",
            "--ir": "Include resident data inline in the output rather than as "
                    "separate files.",
            "--re": "Restrict resident extraction to these extensions.",
            "--rm": "Cap the size of resident data included.",
            "--rs": "Recover slack space from FILE records. Old entries survive "
                    "in the unused tail of a record, so this reaches deleted "
                    "metadata that a straight parse skips.",
            "--at": "Include all $STANDARD_INFORMATION timestamps rather than "
                    "only those that differ from $FILE_NAME. Differences between "
                    "the two attribute sets are the classic timestomping signal, "
                    "so include them when that is the question.",
            "--sn": "Include DOS 8.3 short names.",
            "--fl": "Condensed file listing instead of the full attribute dump.",
            "--vss": "Also parse every Volume Shadow Copy, which is where an "
                     "older $MFT still holds entries the live one has reused.",
            "--dedupe": "Drop duplicates by SHA-1 across the source and shadow "
                        "copies. Use it whenever `--vss` is on.",
            "--dt": "Custom timestamp format for the output.",
        },
        "gotchas": [
            "$MFT entries are reused. A deleted file's record is overwritten by "
            "the next file that needs it, so an entry describing a deleted file "
            "may already belong to something else — check the sequence number "
            "before asserting the two are the same file.",
            "$STANDARD_INFORMATION timestamps are trivially forged; $FILE_NAME "
            "timestamps are not, because they update only through the kernel. "
            "`--at` is what lets you compare them, and a mismatch is the "
            "strongest cheap indicator of timestomping.",
            "Parsing a live volume's $MFT copied with a normal file copy will "
            "fail — it is locked. Extract it with a forensic tool or from a "
            "shadow copy.",
        ],
    },

    "tshark": {
        "purpose": "Wireshark's command line: capture, filter, dissect and "
                   "export packet data, including fields for a timeline.",
        "when": {
            "-r": "Read a capture file. The safe default — analysis needs no "
                  "privileges and cannot disturb the wire.",
            "-i": "Capture live from an interface instead. Needs capture rights, "
                  "and on a busy link a live dissect will drop packets.",
            "-f": "**Capture** filter, in BPF syntax. Applied before packets are "
                  "written, so what it drops is gone forever.",
            "-Y": "**Display** filter, in Wireshark syntax. Applied after "
                  "capture, so nothing is lost and it can be changed later. "
                  "Confusing these two is the classic tshark mistake.",
            "-R": "Read filter, which needs `-2`. Prefer `-Y` unless you know "
                  "why you want this one.",
            "-2": "Two-pass analysis, so fields that depend on later packets — "
                  "reassembly, response times, stream indexes — are populated.",
            "-T": "Output format. `fields` with `-e` is how you get CSV for a "
                  "timeline; `json` and `ek` feed other tools.",
            "-e": "Which field to print, repeatable. Only meaningful with "
                  "`-T fields`, and the ordering is the column ordering.",
            "-c": "Stop after N packets — the fast way to sample a huge file "
                  "before committing to a full pass.",
            "-a": "Autostop condition for a live capture: duration, filesize or "
                  "file count.",
            "-b": "Ring buffer: roll to a new file on time or size, so a long "
                  "capture cannot fill the disk.",
            "-w": "Write packets out rather than dissecting them, which is much "
                  "faster when you only want a filtered subset.",
            "-D": "List interfaces and exit — how you find the right `-i` value.",
            "-L": "List the link-layer types an interface supports.",
            "-s": "Snapshot length; truncates each packet as it is captured.",
            "-p": "Do not enter promiscuous mode.",
            "-I": "Monitor mode, for capturing 802.11 management frames.",
            "-B": "Kernel buffer size. Raise it when a fast link is dropping "
                  "packets at capture time.",
            "-y": "Force the link-layer type.",
            "-M": "Reset dissector state every N packets, to bound memory on a "
                  "very long capture.",
        },
        "gotchas": [
            "Capture filters (`-f`) and display filters (`-Y`) use **different "
            "syntaxes** and apply at different times. `-f` discards packets "
            "permanently; `-Y` only hides them. Reaching for the wrong one is "
            "the most common way to destroy evidence with this tool.",
            "Dissecting live on a busy link drops packets silently. Capture to a "
            "file first, analyse afterwards, whenever completeness matters.",
            "`-T fields` prints nothing useful without `-e`. It is not an error, "
            "just empty output, which reads like the filter matched nothing.",
        ],
    },

    "chainsaw": {
        "purpose": "Hunt through Windows event logs with Sigma rules and "
                   "built-in detection logic, at speed.",
        "when": {
            "--num-threads": "Cap the thread count. Defaults to every core, "
                             "which is usually right on a dedicated analysis "
                             "box and rude on a shared one.",
            "--no-banner": "Suppress the banner, for clean output in a report or "
                           "a pipeline.",
        },
        "gotchas": [
            "The interesting options live on the subcommands — `hunt`, `search`, "
            "`dump` — not at the top level captured here. Run "
            "`chainsaw hunt --help` for the ones that matter.",
            "Rules are not bundled with the binary. Without a Sigma rule set and "
            "the mapping file, `hunt` runs and finds nothing, which looks "
            "identical to a clean host.",
        ],
    },

    "diec": {
        "purpose": "Identify a file's format, compiler, linker and packer from "
                   "the command line — the scriptable half of Detect It Easy.",
        "when": {
            "-r": "Recurse a directory. This is the flag that makes `diec` the "
                  "right tool for a corpus, where the GUI handles one sample.",
            "-d": "Deep scan: look past the entry point for signatures a quick "
                  "pass misses. Slower, and worth it on anything suspicious.",
            "-u": "Heuristic scan, for packers with no exact signature. Raises "
                  "false positives, so treat a heuristic-only hit as a lead.",
            "-g": "Aggressive scan — the most thorough and the noisiest.",
            "-a": "Scan every type rather than stopping at the detected format.",
            "-e": "Show entropy. High entropy with no packer signature is the "
                  "interesting case: something is compressed or encrypted and "
                  "nothing recognises it.",
            "-i": "Show file info — size, format, architecture.",
            "-S": "Ask for one specific piece of info, e.g. `-S Hash#MD5`. The "
                  "form to use when scripting rather than reading.",
            "-U": "Hide unknown results, to cut noise across a large scan.",
            "-b": "Verbose output, including which signature matched.",
            "-l": "Profile signature performance — for tuning a slow scan, not "
                  "for analysis.",
            "-j": "JSON output, for a pipeline.",
        },
        "gotchas": [
            "`diec` and the GUI share a signature set, so they agree by "
            "construction. Use this for corpora and reports; use "
            "[the GUI](die-gui.md) when you need to browse *why* something "
            "matched.",
            "A packer name is a signature match, not proof. Custom and modified "
            "packers match nothing, so silence is not the same as clean.",
            "Deep and aggressive scans cost real time on a large directory. "
            "Sample before committing to a full corpus run.",
        ],
    },

    "dumpcap": {
        "purpose": "Capture packets to a file. It does nothing else — which is "
                   "the point.",
        "when": {
            "-i": "Interface to capture from. `-D` lists what is available.",
            "-w": "Output file. Without it, dumpcap writes to a temporary file "
                  "and tells you where, which is rarely what you meant.",
            "-f": "Capture filter in BPF syntax. Applied before writing, so "
                  "anything it excludes is gone permanently.",
            "-b": "Ring buffer: roll to a new file on duration, filesize or "
                  "count. The difference between a capture that runs overnight "
                  "and one that fills the disk at 3am.",
            "-a": "Autostop condition — duration, filesize or files.",
            "-c": "Stop after N packets.",
            "-s": "Snapshot length: truncate each packet. Headers only, when "
                  "payload must not be recorded.",
            "-B": "Kernel buffer size in MiB. Raise it first when a fast link "
                  "reports drops; the default is small for modern traffic.",
            "-p": "Do not enter promiscuous mode — only traffic for this host.",
            "-I": "Monitor mode, for 802.11 management and control frames.",
            "-D": "List interfaces and exit.",
            "-L": "List link-layer types for the chosen interface.",
            "-S": "Print per-interface packet statistics once a second, for "
                  "confirming traffic is arriving before committing to a "
                  "long capture.",
            "-d": "Print the compiled BPF for a filter, to check it means what "
                  "you think before capturing hours of the wrong thing.",
            "-M": "Machine-readable output for `-D`, `-L` and `-S`.",
            "-y": "Force the link-layer type.",
            "-n": "pcapng output (the default).",
            "-P": "Legacy pcap output, for a tool that cannot read pcapng.",
            "-q": "Quiet — no packet-count updates.",
        },
        "gotchas": [
            "This is deliberately minimal: it captures and it does not dissect. "
            "That is why it is the right thing to run as the privileged process "
            "and why `tshark` shells out to it — the analysis code never needs "
            "the capture privilege.",
            "Filtering here is destructive. A capture filter that was slightly "
            "wrong cannot be widened afterwards; capture broadly and filter at "
            "analysis time whenever the disk allows it.",
            "Drops are reported at the end, not during. Check the count before "
            "treating a capture as complete — a busy link with the default "
            "buffer loses packets silently.",
        ],
    },

    "oledump.py": {
        "purpose": "List and extract the streams inside an OLE2 file — the "
                   "container behind legacy Office documents and many malicious "
                   "attachments.",
        "when": {
            "-s": "Select a stream by number, or `a` for all. Everything else "
                  "operates on the selection, so this usually comes first.",
            "-d": "Dump the selected stream raw, for carving an embedded "
                  "payload out to a file.",
            "-x": "Hex dump, when the stream is binary and you need to see "
                  "structure.",
            "-a": "ASCII dump, for a quick look at mostly-text content.",
            "-A": "ASCII dump with run-length encoding, which collapses long "
                  "runs of padding that otherwise bury the content.",
            "-S": "Strings dump — the fastest way to see whether a stream holds "
                  "anything readable.",
            "-v": "Decompress VBA. Macro streams are stored compressed, so "
                  "without this the source looks like binary noise. This is the "
                  "flag the tool exists for.",
            "--vbadecompresscorrupt": "Decompress as far as possible and show "
                                      "it, for a deliberately corrupted macro "
                                      "stream that defeats a clean decompress.",
            "--vbadecompressskipattributes": "Skip the attribute preamble and "
                                             "show only the macro body.",
            "-r": "Treat the input as a raw stream rather than an OLE file, for "
                  "a stream already carved out elsewhere.",
            "-T": "Head and tail only, to glance at a large stream.",
            "-t": "Apply a translation such as `utf16` when the stream is "
                  "wide-character text.",
            "-m": "Print the full manual, which documents the plugin and "
                  "selection syntax this summary cannot cover.",
        },
        "gotchas": [
            "The stream letters in the listing are the finding: `M` marks a "
            "macro stream and `O` an embedded object. A document with neither "
            "is not carrying either, whatever else it contains.",
            "OOXML files — .docx, .xlsx — are ZIP archives, not OLE2. Unzip "
            "first and run this against the extracted `vbaProject.bin`.",
            "Reading a decompressed macro is not analysing it. `olevba` adds "
            "the keyword and IOC pass; this tool gets you the bytes.",
        ],
    },

    "file": {
        "purpose": "Identify a file's type from its contents rather than its "
                   "name, using magic signatures.",
        "when": {
            "-i": "Print a MIME type instead of prose. The form to use when the "
                  "output feeds a script rather than a person.",
            "--mime-type": "MIME type only, without the encoding.",
            "--mime-encoding": "Character encoding only.",
            "-b": "Omit the filename, leaving just the type — for pipelines and "
                  "for-loops.",
            "-z": "Look inside compressed files and report what they contain "
                  "rather than reporting a compressed stream.",
            "-Z": "Same, without reporting the compression itself.",
            "-k": "Keep going after the first match and print every rule that "
                  "fired. Files crafted to defeat identification often match "
                  "more than one signature, and the disagreement is the finding.",
            "-f": "Read the list of files to test from a file, for a corpus.",
            "-L": "Follow symlinks and report the target.",
            "-h": "Do not follow symlinks — report the link itself.",
            "-m": "Use an alternative magic database.",
            "-C": "Compile a magic file to its indexed form.",
            "-s": "Read block and character devices too. Needed to type a raw "
                  "disk, which `file` otherwise refuses.",
            "-r": "Print raw bytes rather than escaping unprintables.",
            "-p": "Preserve the access time on the files examined — the flag "
                  "that stops a triage sweep from rewriting timestamps across "
                  "the evidence.",
            "-e": "Exclude a test type, when one is misfiring on a corpus.",
            "-0": "Print a NUL after the filename, for safe piping into `xargs -0`.",
            "-N": "Do not pad filenames to align the output.",
            "-P": "Tune a parser limit, e.g. `bytes` or `indir`.",
            "-S": "Disable the sandbox. Only when seccomp blocks a legitimate "
                  "test, and never on untrusted input if avoidable.",
        },
        "gotchas": [
            "Magic reads the first few hundred bytes. Prepend a valid header to "
            "anything and `file` will report the header — it is a fast triage "
            "signal, not an authority on content.",
            "`-p` preserves atime. Without it, typing a directory tree updates "
            "access times across the evidence, which is the kind of avoidable "
            "contamination that gets noticed later.",
            "An 'ASCII text' verdict on something you expected to be binary "
            "usually means it is base64 or hex, not that it is harmless.",
        ],
    },

    "rabin2": {
        "purpose": "Report the structure of a binary — headers, sections, "
                   "imports, exports, strings, symbols — for any format radare2 "
                   "understands.",
        "when": {
            "-I": "The header summary: format, architecture, bits, endianness, "
                  "stripped, and whether NX, PIE and canaries are on. The usual "
                  "first command on an unknown binary.",
            "-i": "Imports. What a binary asks the OS for is the fastest read on "
                  "what it can do.",
            "-E": "Exports — the entry points a DLL offers.",
            "-s": "Symbols, when the binary is not stripped.",
            "-S": "Sections with their sizes and permissions. A section that is "
                  "both writable and executable is worth a second look.",
            "-z": "Strings from the data sections.",
            "-zz": "Strings from the whole file, including sections a normal "
                   "pass skips.",
            "-l": "Linked libraries.",
            "-e": "Entrypoint address.",
            "-c": "Class information, for Objective-C, Java and .NET binaries.",
            "-R": "Relocations.",
            "-H": "Headers in full detail.",
            "-j": "JSON output, for a pipeline.",
            "-q": "Quiet, minimal formatting — easier to parse in a shell.",
            "-k": "Query a specific field rather than printing everything.",
            "-O": "Patch the binary. Read-only work never needs this, and using "
                  "it on evidence modifies it.",
            "-a": "Force the architecture when detection is wrong.",
            "-b": "Force the bit width, 32 or 64.",
            "-A": "List all sub-binaries in a fat/universal file.",
            "-x": "Extract the sub-binaries of a fat file.",
            "-v": "Version.",
        },
        "gotchas": [
            "This is the static, scriptable half of radare2. Nothing here "
            "executes the binary, which makes it safe to run over a corpus of "
            "samples — unlike opening them in a debugger.",
            "The security flags in `-I` describe the *binary*, not the running "
            "process. NX and ASLR also depend on the loader and the OS.",
            "`-z` misses strings outside the data sections, which is where "
            "packed and obfuscated samples hide theirs. Try `-zz` before "
            "concluding a sample has none.",
        ],
    },

    "volshell": {
        "purpose": "An interactive Python shell over a memory image, with "
                   "Volatility's object model loaded — for questions no plugin "
                   "answers.",
        "when": {
            "-f": "The memory image.",
            "--file": "The memory image.",
            "-w": "Treat the image as Windows.",
            "--windows": "Treat the image as Windows.",
            "-l": "Treat the image as Linux.",
            "--linux": "Treat the image as Linux.",
            "-m": "Treat the image as macOS.",
            "--mac": "Treat the image as macOS.",
            "--pid": "Enter with a process context already selected, so `cc()` "
                     "is not the first thing you type.",
            "--script": "Run a Python script against the image and drop into "
                        "the shell afterwards — the repeatable form of an "
                        "interactive session.",
            "--script-only": "Run the script and exit. This is how an "
                             "exploratory session becomes an automated one.",
            "-s": "Where to find symbol tables — the usual fix when a Linux or "
                  "macOS image will not resolve.",
            "--symbol-dirs": "Where to find symbol tables.",
            "-o": "Directory for files written out of the shell.",
            "--output-dir": "Directory for files written out of the shell.",
            "--offline": "Never fetch symbols online.",
            "--clear-cache": "Drop cached items when results look stale.",
            "-q": "Quiet.",
            "--quiet": "Quiet.",
            "-v": "More verbose output.",
            "--verbosity": "More verbose output.",
        },
        "gotchas": [
            "Reach for this when a plugin nearly answers the question but not "
            "quite. If a plugin exists, use the plugin — it is tested and this "
            "is not.",
            "Findings from an interactive session are not reproducible by "
            "default. Move anything that matters into `--script` so the result "
            "can be regenerated and reviewed.",
            "The same symbol requirement as `volatility3` applies: without an "
            "ISF matching the exact kernel build, a Linux or macOS image will "
            "not resolve at all.",
        ],
    },

    "objdump": {
        "purpose": "Disassemble and dump the contents of an object file or "
                   "executable — sections, symbols, relocations and code.",
        "when": {
            "-d": "Disassemble the executable sections. The common case.",
            "-D": "Disassemble everything, including data. Use it when code has "
                  "been hidden in a section not marked executable.",
            "-x": "All headers at once — the fastest orientation on an unknown "
                  "object.",
            "-f": "The file header alone: format, architecture, entry point.",
            "-p": "Format-specific private headers. On a PE this is where the "
                  "import table and data directories live.",
            "-h": "Section headers with sizes, addresses and flags.",
            "-t": "The symbol table, when the binary is not stripped.",
            "-T": "Dynamic symbols — what a shared object exports and imports.",
            "-r": "Relocations.",
            "-R": "Dynamic relocations, which reveal the PLT/GOT layout.",
            "-s": "Full contents of each section as a hex dump.",
            "-j": "Restrict the operation to one section, so a `-s` or `-d` on a "
                  "large binary stays readable.",
            "-S": "Interleave source with disassembly. Only useful when debug "
                  "info survived, which for malware it has not.",
            "-l": "Annotate with file and line numbers from debug info.",
            "-C": "Demangle C++ symbols into something readable.",
            "-b": "Force the file format when detection fails.",
            "-m": "Force the architecture, needed for raw shellcode with no "
                  "container to describe it.",
            "-M": "Pass a disassembler option, e.g. `intel` for Intel syntax "
                  "instead of AT&T.",
            "-g": "Debug information, if present.",
            "-w": "Wide output that does not truncate long symbol names.",
            "-z": "Do not collapse blocks of zero bytes, when the padding "
                  "itself matters.",
        },
        "gotchas": [
            "Disassembly starts where the section says code starts. Packed and "
            "self-modifying binaries decrypt themselves at runtime, so a static "
            "pass shows the unpacking stub and nothing about the payload.",
            "Default output is AT&T syntax. Most Windows malware documentation "
            "is Intel, so `-M intel` avoids constant mental translation.",
            "`-d` skips sections not marked executable, which is precisely where "
            "code gets hidden. `-D` is slower and sees them.",
        ],
    },

    "readelf": {
        "purpose": "Display the structure of an ELF file — headers, sections, "
                   "segments, symbols, notes and dynamic linkage.",
        "when": {
            "-h": "The ELF header: type, architecture, entry point. First thing "
                  "to run on an unknown Linux binary.",
            "-S": "Section headers.",
            "-l": "Program headers, which describe what the loader maps. A "
                  "section table can be stripped or faked; the program headers "
                  "must be right or the binary will not run.",
            "-d": "The dynamic section — needed libraries, RPATH, and the init "
                  "and fini arrays that run before and after `main`.",
            "-s": "The symbol table.",
            "--dyn-syms": "Dynamic symbols only — what the binary imports and "
                          "exports at runtime.",
            "-n": "Notes, including the build ID that ties a stripped binary to "
                  "its debug symbols.",
            "-r": "Relocations.",
            "-u": "Unwind information.",
            "-x": "Hex dump of a named section.",
            "-p": "String dump of a named section — the targeted alternative to "
                  "running `strings` over the whole file.",
            "-a": "Everything. Verbose, and the right first move when you do "
                  "not yet know what you are looking for.",
            "-C": "Demangle C++ symbols.",
            "-D": "Use the dynamic symbol table rather than the static one.",
            "-W": "Wide output that does not truncate.",
            "-t": "Section details in full.",
            "-e": "Header summary: file, section and program headers together.",
        },
        "gotchas": [
            "The section header table is optional at runtime. Malware strips or "
            "corrupts it to break tools, and the binary still runs — when "
            "sections look wrong, read `-l` instead, because the loader must be "
            "able to.",
            "`DT_INIT` and `DT_INIT_ARRAY` in `-d` run before `main`. Code "
            "placed there executes even if `main` looks harmless.",
            "An `RPATH` or `RUNPATH` pointing somewhere writable is a hijack "
            "waiting to happen, and it shows up here.",
        ],
    },

    "nmap": {
        "purpose": "Discover hosts, ports and services, and fingerprint what is "
                   "listening.",
        "when": {
            "-sS": "SYN scan — the default when running privileged. Fast, and it "
                   "does not complete the handshake.",
            "-sT": "Full TCP connect, when you lack the privileges for `-sS`.",
            "-sU": "UDP scan. Slow and unreliable by nature, but DNS, SNMP and "
                   "DHCP live there and a TCP-only sweep never sees them.",
            "-sn": "Host discovery only, no port scan — mapping what exists "
                   "before deciding what to probe.",
            "-Pn": "Skip discovery and treat every host as up. The flag for "
                   "networks that drop ping, and the reason a scan that "
                   "'found nothing' sometimes finds plenty.",
            "-p": "Which ports. `-p-` is all 65535 and takes far longer than "
                  "people expect.",
            "-F": "Fast scan of the top 100 ports.",
            "--top-ports": "Scan the N most common ports — the usual "
                           "time/coverage compromise.",
            "-sV": "Probe for service and version. This talks to the service "
                   "properly, so it is louder and slower than a port scan.",
            "--version-intensity": "How hard `-sV` tries, 0 to 9.",
            "--version-light": "Intensity 2 — much faster, misses more.",
            "--version-all": "Intensity 9.",
            "-O": "OS fingerprint from the TCP/IP stack. A guess with a "
                  "confidence, not a fact.",
            "--osscan-guess": "Report near matches rather than staying silent.",
            "-A": "Aggressive: version, OS, scripts and traceroute together. "
                  "Convenient and unmistakably noisy.",
            "-T": "Timing template 0-5. `-T4` is the usual choice on a LAN; "
                  "`-T0` and `-T1` exist for evading rate-based detection and "
                  "take hours.",
            "--script": "Run NSE scripts. The category matters — `vuln` and "
                        "`exploit` scripts actively test, and `exploit` can "
                        "change the target.",
            "--script-args": "Arguments for those scripts.",
            "--script-help": "Explain what a script does before running it, "
                             "which is worth doing for anything outside `safe`.",
            "-oA": "Write all three output formats at once. Do this always — "
                   "rerunning a scan to get a different format wastes time and "
                   "produces different results.",
            "-oN": "Normal output to a file.",
            "-oX": "XML output, for tooling.",
            "-oG": "Greppable output.",
            "--open": "Show only open ports, cutting the closed-port noise.",
            "-v": "Verbose; repeat for more.",
            "-n": "No reverse DNS, which is often the single biggest speed-up.",
            "-e": "Choose the interface to scan from.",
            "-S": "Spoof the source address.",
            "-D": "Decoy scan.",
            "-6": "Scan IPv6. Hosts frequently expose more on v6 than v4 "
                  "because the firewall rules were never mirrored.",
            "--exclude": "Skip these hosts. The safety flag: use it for anything "
                         "fragile before starting a range scan.",
            "--excludefile": "Skip the hosts listed in a file.",
            "--max-retries": "Cap retransmissions on a lossy link.",
            "--host-timeout": "Give up on a host after this long, so one dead "
                              "host cannot stall a range.",
            "--traceroute": "Trace the path to each host.",
        },
        "gotchas": [
            "Scanning is not passive. `-sV` and NSE talk to services properly, "
            "`--script exploit` may change the target, and everything here is "
            "recorded by anything watching. Have authorisation before running "
            "it, and use `--exclude` for hosts that must not be touched.",
            "`-p-` on a /24 is a very different job from the default scan. "
            "Scope the ports before scoping the hosts.",
            "A closed port and a filtered port are different findings. "
            "'Filtered' means something dropped the probe, which is information "
            "about the network rather than about the host.",
        ],
    },
}


# Who answered what, captured before the researched blocks below merge into
# ENRICHMENT and make the two indistinguishable.
#
# The merge is deliberate -- a published answer is an answer, and rank_flags
# is right to skip a flag that already has one. But after it runs, nothing
# can tell a human judgement from a machine-generated one, and that broke the
# metric this loop is steered by: the fraction of flag attempts aimed at
# already-answered flags. Two notes were accepted and published, the next
# round measured against the merged dict, and the loop's own successes came
# back as redundant targeting. A phantom regression from 0% to 3% that would
# have been chased as a real one.
#
# Provenance is worth keeping for its own sake anyway. These two kinds of
# answer carry different weight, and once merged that distinction is gone.
HAND_ANSWERED: dict[str, frozenset] = {
    _c: frozenset((_r.get("when") or {})) for _c, _r in ENRICHMENT.items()
}
HAND_SCENARIOS: frozenset = frozenset(
    _c for _c, _r in ENRICHMENT.items() if _r.get("scenario"))


# Extracted worked commands, merged in above publish.py's boundary so the
# block survives regeneration. setdefault, so a hand-written invocations list
# always wins over an extracted one -- same rule as every other field here.
try:
    from invocations_data import INVOCATIONS as _INV
    for _c, _rows in _INV.items():
        ENRICHMENT.setdefault(_c, {}).setdefault("invocations", _rows)
except Exception:
    pass


# --- BEGIN researched scenarios (scripts/publish.py) ---
#
# Generated by scripts/publish.py from research the loop verified:
# retrieved from real documentation and walkthroughs, checked
# against the sources blind to the draft, and cited. Do not edit
# by hand -- rerun publish.py. Anything hand-written belongs in
# ENRICHMENT above, which always wins over this block.
RESEARCHED: dict[str, dict] = {
    'AmcacheParser': {
        'scenario': 'An analyst reaches for AmcacheParser after manually examining the AmCache hive with Registry Explorer or when needing structured CSV output for timeline analysis, as it automates extraction of AmCache data into a CSV file, which is more efficient than manual methods or RegRipper’s plugin-based reports. They may run it following the extraction of the Amcache.hve file and before analyzing results in Timeline Explorer, prioritizing its automation and compatibility with further analysis tools.',
        'sources': ['https://www.mennovanveenendaal.com/posts/The-Windows-AmCache-and-ShimCache-Artifacts/'],
    },
    'AppCompatCacheParser': {
        'scenario': "An analyst reaches for AppCompatCacheParser when examining ShimCache for historical execution evidence, often after checking UserAssist or before parsing AmCache, as it converts the registry's AppCompatCache into a readable CSV, providing file names, sizes, and timestamps that manual analysis cannot easily extract. They may prefer it over AmCacheParser when focusing on ShimCache-specific data rather than AmCache's more detailed but differently structured entries.",
        'sources': ['https://hackers-arise.com/digital-forensics-registry-analysis-for-beginners-part-3-evidence-of-execution/', 'https://hivesecurity.gitlab.io/blog/dfir-incident-response-complete-guide-2026/', 'https://nullsec.us/windows-10-11-appcompatcache-deep-dive/'],
    },
    'EvtxECmd': {
        'scenario': 'An analyst reaches for EvtxECmd during the "PARSE" phase of the DFIR workflow to convert event logs into standardized CSV, XML, or JSON formats, often after collecting logs with KAPE and before analyzing them in Timeline Explorer, as it supports custom maps, locked file handling, and produces structured output essential for correlation and triage.',
        'sources': ['https://ericzimmerman.github.io/', 'https://ridgelinecyber.com/resources/kape-ez-tools/'],
    },
    'JLECmd': {
        'scenario': 'An analyst reaches for JLECmd when parsing individual Jump Lists or extracting shell item data from .automaticDestinations-ms files, often after obtaining the files through forensic imaging or before analyzing the extracted .lnk files with other tools like LNK Tool. They may choose JLECmd over JumpList Explorer (JLE) when command-line processing is required, though JLE is preferred for its graphical interface.',
        'sources': ['https://www.cyberengage.org/post/jump-list-analysis-tool-jlecmd-exe'],
    },
    'PECmd': {
        'scenario': 'An analyst reaches for PECmd when processing Windows Prefetch files to extract execution details, often running it after collecting .pf files from a system or before exporting data for further analysis; they may use it over similar tools due to its structured output options like JSON or CSV, and its specific focus on Windows Prefetch parsing.',
        'sources': ['https://github.com/EricZimmerman/PECmd'],
    },
    'RBCmd': {
        'scenario': 'An analyst reaches for RBCmd when examining deleted files in the Recycle Bin to extract metadata like deletion time, original path, and file size from $I and $R files, often after manually identifying these files or directories; they may run it following initial file recovery attempts or alongside tools that recover $R files, preferring it for its ability to parse and output structured data (e.g., CSV) directly from $I files, which contain critical forensic information not easily accessible through other means.',
        'sources': ['https://medium.com/@jenito/recycle-bin-forensics-inside-the-digital-trash-can-dc6d1f479af8', 'https://www.cyberengage.org/post/recycle-bin-i-analyses-tool-i_parse_v1-1'],
    },
    'RecentFileCacheParser': {
        'scenario': 'An analyst reaches for RecentFileCacheParser when parsing a RecentFileCache.bcf file to extract recently accessed file paths, often after acquiring a forensic image or during artifact collection; they may run it before exporting data to CSV or JSON for structured analysis, preferring it over similar tools due to its specialized focus on .bcf files and clear export formatting options.',
        'sources': ['https://github.com/EricZimmerman/RecentFileCacheParser', 'https://github.com/wodzen/agent-forensics-skills/blob/main/skills/recentfilecacheparser/SKILL.md'],
    },
    'SBECmd': {
        'scenario': 'An analyst reaches for SBECmd when processing mounted forensic images to extract ShellBags data from NTUSER.DAT and UsrClass.dat files, often running it after mounting the image and before manual analysis or generating reports, as it automates parsing and outputs structured CSV files, making it preferable for large-scale investigations over manual tools.',
        'sources': ['https://cyber5w.com/blog/windows-shell-items-analysis', 'https://www.cyberengage.org/post/shell-bags-analysis-tool-sbecmd-exe-or-shellbagsexplorer-gui-version-very-important-artifact'],
    },
    'SrumECmd': {
        'scenario': 'An analyst reaches for SrumECmd during incident response after checking logs, processes, file changes, and persistence mechanisms to analyze data egress volume per application by processing SRUDB.dat and SOFTWARE hive data, as it specifically addresses network and application-based data movement insights not covered by other tools in the triage sequence.',
        'sources': ['https://ericzimmerman.github.io/', 'https://ridgelinecyber.com/resources/kape-ez-tools/', 'https://ridgelinecyber.com/training/modules/free/ir01-toolkit-setup/03-eztools/'],
    },
    'SumECmd': {
        'scenario': 'An analyst reaches for SumECmd after repairing corrupted UAL database files with Esentutl.exe /p to parse the Windows User Access Log (UAL) and generate CSV files correlating role access timestamps, GUIDs, and role names, as it specifically handles UAL logs that retain historical authentication data longer than typical event logs. They may use it alongside EDR telemetry and Security event logs to investigate suspicious activity, such as anomalous logins or appliance connections, due to its focus on UAL artifacts.',
        'sources': ['https://cloud.google.com/blog/topics/threat-intelligence/brickstorm-espionage-campaign', 'https://github.com/AndrewRathbun/Awesome-KAPE', 'https://github.com/S-RM/wiskess_rust'],
    },
    'WxTCmd': {
        'scenario': 'An analyst reaches for WxTCmd when examining Windows 10 timeline data to determine execution times or user activity, running it with the -f option on an ActivitiesCache.db file before opening the resulting CSV in EZviewer; they choose it over tools like JLECmd because WxTCmd specifically processes timeline files for execution details, whereas JLECmd handles Jump Lists for recent file access.',
        'sources': ['https://github.com/AndrewRathbun/Awesome-KAPE', 'https://github.com/AndrewRathbun/Awesome-KAPE/blob/main/README.md', 'https://github.com/Digital-Forensics-Discord-Server/ArtifactParsers'],
    },
    'XORSearch': {
        'scenario': 'An analyst reaches for XORSearch when searching for XOR, ROL, ROT, or SHIFT encoded strings in a binary file, particularly when suspecting malware obfuscation like hidden URLs; they may run it after extracting a suspicious file or before deeper analysis to decode potential hidden data, choosing it over similar tools due to its support for multiple encoding types and specific options like dictionary attacks for 32-bit keys.',
        'sources': ['https://blog.didierstevens.com/programs/xorsearch/'],
    },
    'aeskeyfind': {
        'scenario': 'An analyst reaches for aeskeyfind when examining memory dumps or virtual machine snapshots to recover AES-128 keys, especially in cases where memory decay or corrupted key schedules may be present; they may pre-process dumps to filter irrelevant data and post-process results by validating discovered keys against known encryption usage, preferring it over similar tools due to its ability to handle reversed key schedules, InvMixColumn pre-applied entries, and entropy-based filtering of non-key blocks.',
        'sources': ['https://github.com/SalpSec/aeskeyfind', 'https://github.com/makomk/aeskeyfind', 'https://www.siberoloji.com/aeskeyfind-kali-linux-advanced-memory-forensics-aes-key-recovery/'],
    },
    'affinfo': {
        'scenario': 'An analyst reaches for affinfo when examining an AFF file to validate its integrity or extract metadata, often after acquiring the file or before decrypting it with a passphrase; they choose it for its specific capabilities to verify hashes, list segments, and identify file structures, which are critical for forensic analysis.',
        'sources': ['https://www.kali.org/tools/afflib/'],
    },
    'base64dump.py': {
        'scenario': 'An analyst reaches for base64dump.py when encountering malformed base64 or hexadecimal strings that require length adjustment or specific decoding, such as after initial detection using regular expressions. They may run it with options like -p (e.g., L4 or custom lambdas) to preprocess strings before decoding or -P to postprocess decoded data, as it allows handling of non-standard encodings and integrates built-in functions for tasks like UTF16-to-ASCII conversion, which other tools may not natively support.',
        'sources': ['https://github.com/DidierStevens/DidierStevensSuite/blob/master/base64dump.py'],
    },
    'binwalk': {
        'scenario': 'An analyst reaches for binwalk when examining firmware images to identify embedded files, compressed data, or cryptographic keys, often after obtaining a firmware dump from a device; they may run it before deeper analysis to map contents or after extracting files for further inspection, preferring it for its entropy analysis and custom signature capabilities over tools lacking these specific features.',
        'sources': ['https://github.com/ReFirmLabs/binwalk/wiki/Usage', 'https://www.hardbreak.wiki/hardware-hacking/basics/tools/software-tools/binwalk'],
    },
    'capa': {
        'scenario': 'An analyst reaches for capa after submitting a sample to CAPE for dynamic analysis, running it against the generated JSON report to extract capabilities, particularly when dealing with packed or obfuscated binaries where static analysis may fail. They may use it following unpacking or sandbox execution to bypass obfuscation limitations, preferring it over standalone static analysis tools due to its integration with dynamic reports and support for IDA Pro/Ghidra for enhanced feature extraction.',
        'sources': ['https://github.com/mandiant/capa', 'https://github.com/xuguowong/capa-SAST'],
    },
    'cyberchef': {
        'scenario': 'When an analyst needs to decrypt, decode, or transform data, they reach for CyberChef due to its versatile interface and client-side processing, which ensures no data is transmitted to third-party servers, making it preferable over tools that may not handle sensitive information as securely.',
        'sources': ['https://github.com/martinmathurine/Cryptography-Decryption-CyberChef-Lab', 'https://www.it-connect.tech/cyberchef-a-web-application-for-decrypting-decoding-and-transforming-data/'],
    },
    'dc3dd': {
        'scenario': 'An analyst reaches for dc3dd when encountering unreadable sectors during disk imaging, using cnt=, iskip=, and oskip= parameters before running it to handle errors, and prefers it for its robust error recovery features and ability to report progress upon interruption.',
        'sources': ['https://www.kali.org/tools/dc3dd/'],
    },
    'dcfldd': {
        'scenario': 'An analyst uses dcfldd when creating a verified forensic copy of a disk drive for investigation, ensuring write protection is enabled before imaging and verifying the image with hashing tools afterward, as it provides enhanced forensic features like progress tracking and error handling compared to standard dd or dc3dd.',
        'sources': ['https://dohost.us/index.php/2025/11/01/creating-a-forensic-image-of-the-disk-drive-dd-dc3dd-dcfldd/', 'https://github.com/mukul975/Anthropic-Cybersecurity-Skills/blob/main/skills/acquiring-disk-image-with-dd-and-dcfldd/SKILL.md'],
    },
    'evtxexport': {
        'scenario': 'An analyst reaches for evtxexport when exporting event records from an XML Event Log (.evtx) file, often after mounting a volume or image to access logs, as it supports exporting full event messages requiring SYSTEM and SOFTWARE registry files; they may use it after mounting a QEMU VM image and before analyzing event data in text or XML format, preferring it over similar tools for its ability to handle multi-language resources and full message exports.',
        'sources': ['https://github.com/libyal/libevtx/wiki/Tools'],
    },
    'evtxinfo': {
        'scenario': "An analyst reaches for evtxinfo after extracting EVTX files from memory dumps using tools like volatility's dumpfiles, running it to inspect file headers and chunk metadata before using evtxdump to parse event data, as it provides structural insights without full log parsing.",
        'sources': ['https://manpages.debian.org/unstable/libevtx-utils/evtxexport.1.en.html', 'https://www.rocheston.com/fire/', 'https://www.tophertimzen.com/resources/cs407/slides/week04_02-EventLogs.html'],
    },
    'ewfexport': {
        'scenario': 'An analyst reaches for ewfexport when they need to extract specific data from an EWF image, such as a partition or converting an E01 to another format, often after acquiring the image with ewfacquire; they may use it before further analysis to isolate relevant data, preferring it over other tools due to its flexibility in specifying byte ranges and output formats.',
        'sources': ['https://bromiley.medium.com/tooling-thursday-libewf-ec27b4564c2a', 'https://forensics.wiki/libewf/'],
    },
    'floss': {
        'scenario': 'An analyst reaches for FLOSS when examining an executable file containing obfuscated strings, as it automatically emulates decoding routines and extracts human-readable strings from memory differences; they may run it after initial static analysis to uncover hidden data, preferring it over manual emulation or other tools due to its automated comparison of memory states before and after decoding.',
        'sources': ['https://cloud.google.com/blog/topics/threat-intelligence/automatically-extracting-obfuscated-strings'],
    },
    'fls': {
        'scenario': "An analyst reaches for fls when gathering temporal data from file systems to create a timeline, running it with the '-m' flag and '-r' to recursively collect all files across each partition in a disk image; they may adjust time skew with '-s' to align with other systems, preferring fls over older tools like 'grave-robber' because it streamlines the process by eliminating the need for 'ils' and integrates directly with mactime for timeline generation.",
        'sources': ['https://github.com/sleuthkit/sleuthkit/wiki/Timelines'],
    },
    'foremost': {
        'scenario': 'An analyst reaches for foremost when recovering lost files from disk images or drives, using command line switches to specify built-in file types or configuration files for headers and footers; they may run it after creating an image with tools like dd, and choose it over similar tools due to its reliability and speed from using internal data structures of file formats.',
        'sources': ['http://foremost.sourceforge.net/', 'https://www.kali.org/tools/foremost/'],
    },
    'frida': {
        'scenario': 'An analyst reaches for Frida when bypassing root detection in Android apps, setting up the Frida server via adb push and running frida-ls-devices to confirm device connections before hooking into methods like onCreate(); they prefer it over similar tools because newer versions avoid bugs that prevent hooking early lifecycle functions, ensuring reliable interception of critical app behaviors.',
        'sources': ['https://bananamafia.dev/post/r2frida-1/', 'https://github.com/dweinstein/awesome-frida'],
    },
    'frida-trace': {
        'scenario': "An analyst reaches for frida-trace when tracing and modifying application behavior dynamically, such as during reverse engineering or security testing, often after copying frida-server to a remote device and before interacting with the target app's methods. They may choose it over similar tools because it allows real-time modification of method outputs and provides detailed tracing capabilities, as demonstrated by altering return values or inspecting method parameters during execution.",
        'sources': ['https://frida.re/docs/frida-trace/', 'https://www.vaadata.com/en/blog/frida-the-tool-dedicated-to-mobile-application-security/'],
    },
    'hashcat': {
        'scenario': 'An analyst reaches for hashcat when dealing with hashes like MD5, using wordlists such as rockyou.txt for brute-force or combination attacks, and runs it after identifying the hash type and preparing input files; they choose it over similar tools due to its GPU-accelerated cracking capabilities and support for advanced attack modes like mask attacks, as demonstrated in the examples.',
        'sources': ['https://github.com/IPIRATEXAPTAIN/htb-academy/blob/main/CrackingPasswordsWithHashcat.md', 'https://hashcat.net/wiki/doku.php?id=frequently_asked_questions'],
    },
    'hayabusa': {
        'scenario': 'An analyst reaches for Hayabusa when generating fast forensics timelines from Windows event logs, either after collecting logs for offline analysis or during live-response investigations; they may run it before importing data into tools like Elastic Stack or Timesketch, as it consolidates events into structured formats and leverages Sigma rules for detection, offering speed and compatibility with enterprise-scale analysis platforms.',
        'sources': ['https://github.com/Yamato-Security/hayabusa'],
    },
    'hivexsh': {
        'scenario': 'An analyst reaches for hivexsh when examining pagefile.sys to extract and analyze carved registry hive fragments, often after initial string or artifact extraction, to process regf and hbin blocks for registry keys, command-line patterns, or credential indicators; they may use it in conjunction with RegRipper or Registry Explorer for deeper analysis, as it specifically handles registry data recovery from pagefile.sys fragments.',
        'sources': ['https://www.pagefilesysparser.com/en'],
    },
    'hydra': {
        'scenario': 'When testing system security to identify weak or default credentials, an analyst uses Hydra after creating custom username/password lists, running it via command line for protocols like SSH, preferring it over similar tools for its cross-platform support and ability to validate security measures effectively.',
        'sources': ['https://github.com/evarol/HYDRA', 'https://www.linkedin.com/pulse/unleashing-hydra-password-cracking-penetration-testing-tirthan-kiyada-oxzlf'],
    },
    'inetsim': {
        'scenario': 'An analyst reaches for inetsim when setting up a simulated internet environment for malware analysis, running it before detonating a sample to intercept network traffic and avoid exposing real services. They configure it alongside tools like Wireshark and Fiddler, preferring it for its ability to mimic network responses and capture traffic without requiring actual internet connectivity.',
        'sources': ['https://github.com/gl0bal01/intel-codex/blob/main/Security/Analysis/sop-malware-analysis.md', 'https://seanthegeek.net/posts/beginning-malware-analysis/'],
    },
    'mactime': {
        'scenario': 'An analyst reaches for mactime after gathering temporal data from file systems, logs, and other sources into a body file using tools like fls, to sort and merge the data into a single timeline. They would run it after collecting and consolidating all temporal data, as it is specifically designed to handle the body file format and create a chronological view, which is critical for event reconstruction.',
        'sources': ['https://github.com/sleuthkit/sleuthkit/wiki/Timelines'],
    },
    'mergecap': {
        'scenario': 'An analyst reaches for mergecap when merging multiple pcap files captured sequentially into a single file, often running it after capturing or before analysis to consolidate data; they choose it over append mode to maintain correct timestamps and avoid misordering packets, as demonstrated in the documentation.',
        'sources': ['https://osqa-ask.wireshark.org/questions/31113/wireshark-merging-pcap-files/', 'https://osqa-ask.wireshark.org/questions/39951/how-to-simultaneously-filter-and-merge-several-pcap-files/', 'https://wiki.wireshark.org/Tools'],
    },
    'ngrep': {
        'scenario': 'An analyst reaches for ngrep when searching for specific patterns in network traffic, such as detecting "login" in Telnet sessions, using switches like -w, -i, and -t for precise matching and timestamps; they may run it alongside tcpdump to analyze captured packets, preferring it over tcpdump for its grep-style filtering and intuitive regular expression handling.',
        'sources': ['https://www.admin-magazine.com/Articles/Network-Grep'],
    },
    'nping': {
        'scenario': 'An analyst reaches for nping when they need to send custom network packets for testing or forensic analysis, such as probing specific ports or crafting ICMP requests, often after identifying a target range or before verifying network behavior. They may choose it over similar tools due to its detailed target specification options, support for CIDR and octet ranges, and flexibility in packet crafting, as demonstrated in the examples and documentation.',
        'sources': ['https://nmap.org/book/nping-man.html'],
    },
    'numbers-to-string.py': {
        'scenario': 'An analyst reaches for numbers-to-string.py when processing files containing numeric sequences that need conversion to readable strings, such as ASCII or custom-encoded data; they may run it after extracting numbers from a file or before analyzing the resulting text, and they choose it over similar tools due to its support for custom translation tables, statistical analysis, and binary output handling as described in the documentation.',
        'sources': ['https://github.com/DidierStevens/DidierStevensSuite/blob/master/numbers-to-string.py'],
    },
    'objdump': {
        'scenario': 'An analyst reaches for objdump when examining raw binary files like BIOS dumps or ELF binaries to inspect assembly code, section headers, or memory layouts, often after capturing memory or firmware data; they may use it alongside tools like ndisasm or Ghidra for deeper analysis, preferring objdump for its integration with ELF metadata and ability to display low-level code structures.',
        'sources': ['https://can-ozkan.medium.com/learning-elf-the-foundation-of-linux-binary-analysis-c4f1f8df83e4', 'https://github.com/gl0bal01/intel-codex/blob/main/Security/Analysis/sop-malware-analysis.md', 'https://hacktricks.wiki/en/binary-exploitation/basic-stack-binary-exploitation-methodology/elf-tricks.html'],
    },
    'olebrowse': {
        'scenario': 'An analyst reaches for olebrowse when they need to interactively explore the structure of an OLE file, such as viewing or extracting individual data streams from MS Office documents, as it provides a simple GUI interface for this purpose. They may use it alongside tools like oledir or olemap for structural analysis, but prefer olebrowse for its visual inspection capabilities over command-line alternatives.',
        'sources': ['https://github.com/decalage2/oletools/wiki', 'https://github.com/decalage2/oletools/wiki/olevba'],
    },
    'oledump.py': {
        'scenario': 'An analyst reaches for oledump.py when examining OLE files (e.g., .xls) for embedded VBA macros or obfuscated content, often after extracting a file from a password-protected zip (using the password "infected") to avoid manual extraction. They may run it with options like -m to list streams, -v to decompress macros, or plugins like plugin_http_heuristics.py to extract URLs, preferring it over similar tools due to its ability to analyze zipped files in-place and integrate with YARA for rule-based scanning.',
        'sources': ['https://blog.didierstevens.com/programs/oledump-py/'],
    },
    'pdfid': {
        'scenario': 'An analyst reaches for pdfid when triaging PDF documents to quickly identify potential threats, such as those containing JavaScript or obfuscation, before conducting deeper analysis with a parser; they may run it initially to screen files for suspicious content, preferring it over more complex parsers due to its simplicity and reduced risk of exploitation.',
        'sources': ['https://blog.didierstevens.com/programs/pdf-tools/'],
    },
    'pdfid.py': {
        'scenario': 'An analyst reaches for pdfid.py when triaging PDF documents to quickly identify potential threats like embedded JavaScript or suspicious actions, running it before deeper analysis with a full parser due to its simplicity and effectiveness in scanning for keywords without complex parsing.',
        'sources': ['https://blog.didierstevens.com/programs/pdf-tools/'],
    },
    'photorec': {
        'scenario': 'An analyst reaches for PhotoRec when recovering files from disk images, Encase EWF images, or physical devices like hard disks and USB keys, after ensuring proper permissions and device selection; they may run it following the creation of a disk image or after selecting the target partition, preferring it over similar tools for its support of encrypted file systems, RAID, and direct carving from unallocated space without relying on file system metadata.',
        'sources': ['https://www.cgsecurity.org/wiki/PhotoRec_Step_By_Step'],
    },
    'rabin2': {
        'scenario': 'An analyst reaches for rabin2 when examining binary files to extract structured information about ELF/PE/MZ/CLASS files, often after extracting them from disk images or PCAPs, as it provides detailed insights into binary structure and security features (e.g., `rabin2 -I` for security checks or `rabin2 -z` for strings) that may be more straightforward or comprehensive than alternatives like `readelf` or `checksec`.',
        'sources': ['https://gist.github.com/52617365/95baed8b731c3effdad04b1d6ccf4831', 'https://github.com/Adamkadaban/CTFs'],
    },
    'radare2': {
        'scenario': "An analyst reaches for radare2 when analyzing a binary to understand its structure, find exploits, or debug code, often running `radare2 <binary file>` to start, followed by `aaa` to analyze the binary's executable sections and calls. They may choose it for its detailed disassembly and navigation capabilities, as highlighted by the emphasis on commands like `aaa` and `afl` for exploring code flow and functions.",
        'sources': ['https://kindawingingit.medium.com/radare2-an-introduction-d6762dceeac5'],
    },
    'rahash2': {
        'scenario': 'An analyst reaches for rahash2 when examining filesystems to identify modified sections of large files, as it hashes each block individually, allowing comparison against known hashes to pinpoint changes. They may run it after obtaining a file from disk imaging or before performing deeper analysis to verify data integrity. They choose it over other hash tools because its block-based approach enables targeted modification detection without processing the entire file at once.',
        'sources': ['https://gist.github.com/52617365/95baed8b731c3effdad04b1d6ccf4831', 'https://www.sentinelone.com/labs/automating-string-decryption-and-other-reverse-engineering-tasks-in-radare2-with-r2pipe/'],
    },
    'readelf': {
        'scenario': "An analyst reaches for readelf when examining stripped binaries or analyzing ELF headers to identify architecture, sections, or security features like CET; they may run it after using strings or before deeper disassembly to understand the binary's structure and protections, preferring it over similar tools for its precise ELF-specific insights into headers, sections, and dynamic symbols.",
        'sources': ['https://hacktricks.wiki/en/binary-exploitation/basic-stack-binary-exploitation-methodology/elf-tricks.html', 'https://intezer.com/blog/elf-malware-analysis-101-initial-analysis/', 'https://w00tsec.blogspot.com/2015/02/firmware-forensics-diffs-timelines-elfs.html'],
    },
    'regripper': {
        'scenario': 'An analyst reaches for RegRipper when examining registry hive files to quickly extract and decode data using pre-canned plugins, often after extracting the hive from a forensic image or system; they may run it alongside manual registry analysis to validate findings, as it automates complex data extraction tasks like decoding ROT-13 or translating binary values, which would be time-consuming manually.',
        'sources': ['https://www.sans.org/blog/regripper-ripping-registries-with-ease'],
    },
    'reordercap': {
        'scenario': 'An analyst uses reordercap when packets in a capture file are out of chronological order, running it after capturing or extracting the file to reorder packets by timestamp; they avoid using the same input and output file to prevent malformation, and prefer it over manual sorting or other tools because it automatically detects file formats and compression.',
        'sources': ['https://manpages.debian.org/testing/wireshark-common/reordercap.1.en.html', 'https://tshark.dev/edit/reordercap/'],
    },
    'scalpel': {
        'scenario': 'When an analyst needs to recover files from a disk image or raw device without relying on filesystem structure, they use Scalpel after imaging the drive, as it is filesystem-independent and can extract files from multiple formats. They may choose it over similar tools like Foremost because it is a faster, rewritten version designed for both digital forensics and file recovery.',
        'sources': ['https://www.kali.org/tools/scalpel/'],
    },
    'ssdeep': {
        'scenario': 'An analyst reaches for ssdeep when comparing files for similarity rather than exact matches, running commands like -r to generate fuzzy hashes and -x or -k to compare signatures, as it is a mainstream tool used by NIST and can detect partial overlaps between files.',
        'sources': ['https://dfir.science/2017/07/How-To-Fuzzy-Hashing-with-SSDEEP-(similarity-matching).html', 'https://ssdeep-project.github.io/ssdeep/usage.html'],
    },
    'tcpflow': {
        'scenario': 'An analyst reaches for tcpflow after capturing network traffic with tools like tcpdump, when they need to reconstruct and analyze TCP data streams in files for easier forensic examination; they may run tcpflow on stored pcap files to extract and organize data, preferring it over Wireshark for its ability to save reconstructed flows into conventional files, simplifying further analysis with standard tools.',
        'sources': ['https://forensics.wiki/tcpflow/', 'https://www.systutorials.com/docs/linux/man/1-tcpflow/'],
    },
    'tcpxtract': {
        'scenario': 'When an analyst needs to extract files from network traffic, they use tcpxtract on pcap capture files or live traffic, as it supports 26 file formats and allows custom configurations via its config file. They may run it after capturing traffic with tools that generate pcap files, preferring it over similar tools due to its flexibility in adding new formats and reliance on file signatures for accurate extraction.',
        'sources': ['https://www.freshports.org/net/tcpxtract/'],
    },
    'testdisk': {
        'scenario': 'An analyst reaches for TestDisk when recovering lost partitions or repairing filesystems on physical devices, running it with administrative or root privileges after ensuring access rights; they choose it over similar tools because it specifically handles partition recovery and filesystem repair, unlike PhotoRec, which focuses on file recovery from unallocated space.',
        'sources': ['https://www.cgsecurity.org/wiki/PhotoRec', 'https://www.cgsecurity.org/wiki/TestDisk_Step_By_Step'],
    },
    'upx': {
        'scenario': 'An analyst reaches for UPX when encountering a sample with .UPX0/.UPX1 sections, running `upx -d` to quickly unpack it before analyzing the decrypted code, as it is straightforward and automated compared to manual unpacking or tools like Unipacker that require emulation for more complex packers.',
        'sources': ['https://inventivehq.com/blog/malware-unpacking-guide'],
    },
    'vol': {
        'scenario': "An analyst reaches for vol when examining memory dumps to detect malicious activity, such as unusual processes or command-line arguments; they may first run plugins like `windows.pslist` or `windows.pstree` to establish context before using `windows.cmdline` or `windows.handles` for deeper analysis, as the tool's use of symbol tables ensures accurate parsing of memory structures over guesswork.",
        'sources': ['https://hivesecurity.gitlab.io/blog/memory-forensics-volatility-attack-detect/', 'https://www.dfirhive.com/post/windows-memory-and-process-analysis-volatility3-walkthrough'],
    },
    'volshell': {
        'scenario': 'An analyst reaches for volshell when they need to interactively run plugins or execute custom scripts on a memory image, often after loading the image to extract or analyze specific data. They may use it to generate TreeGrid objects for structured data access or run snippets via rs for quick tasks, preferring it over writing full plugins due to its flexibility and direct framework access.',
        'sources': ['https://github.com/volatilityfoundation/volatility3/blob/develop/doc/source/volshell.rst', 'https://volatility3.readthedocs.io/en/latest/volshell.html'],
    },
    'xortool': {
        'scenario': 'An analyst reaches for xortool when dealing with XOR-encrypted data, particularly when the key length is unknown or longer than default limits, and runs it after initial attempts to guess the key fail, using flags like -m, -l, or -c to refine results; they choose it over similar tools because it automates key-length analysis, filters plaintexts by character sets (e.g., Base64), and handles multi-byte keys with adjustable parameters.',
        'sources': ['https://github.com/hellman/xortool', 'https://github.com/hellman/xortool/blob/master/README.md', 'https://www.doyler.net/security-not-included/basic-xortool-usage'],
    },
    'yara': {
        'scenario': 'An analyst reaches for YARA when they need to detect specific malware or file patterns using Boolean conditions and tags, running it after collecting files from an incident or system, as it allows efficient filtering and organization of rules through metadata and tags.',
        'sources': ['https://www.eccouncil.org/cybersecurity-exchange/ethical-hacking/mastering-yara-rules-a-complete-guide-with-use-cases-syntax-and-real-world-examples/', 'https://www.picussecurity.com/resource/glossary/what-is-a-yara-rule', 'https://yara.readthedocs.io/en/stable/writingrules.html'],
    },
}

RESEARCHED_FLAGS: dict[str, dict] = {
    'MFTECmd': {
        '--csvf': 'An analyst would use the --csvf flag when specifying a custom filename for the CSV output file generated by MFTECmd during the analysis of an $MFT file.',
        '-f': 'An analyst would use the -f flag when specifying the path to the Master File Table ($MFT) file, such as when processing a mounted disk image or a local NTFS drive to extract file system metadata.',
    },
    'PECmd': {
        '--csv': 'An analyst would use the --csv flag when processing an entire prefetch directory to generate a structured CSV report for detailed analysis of execution timestamps and file activity.',
        '-f': 'An analyst would use the -f flag when examining a specific prefetch file to extract detailed execution information, such as timestamps and context about a suspicious executable like Mimikatz.',
        '-k': 'An analyst would use the -k flag when performing one-off analysis to quickly highlight and identify known-bad folders or files by searching for specific keywords in the output.',
    },
    'RECmd': {
        '--csv': 'An analyst would use the --csv flag when batch-processing registry hives against the community ruleset to generate structured CSV output for forensic analysis of persistence mechanisms, user activity, and system configuration details.',
        '--csvf': 'An analyst would use the --csvf flag when processing registry hives with RECmd to generate a CSV output file for further analysis or documentation during a forensic investigation.',
        '-d': 'An analyst would use the -d flag with RECmd when batch-processing hives against a community ruleset to extract forensic values like RunOnce persistence or user activity from the registry.',
        '-f': 'An analyst would use the -f flag when processing a single registry hive file against a specific rule file to extract forensic artifacts.',
    },
    'SrumECmd': {
        '-f': 'An analyst would use the -f flag with SrumECmd when extracting per-app network usage data from the SRUDB.dat file to investigate network activity over the last 30-60 days.',
    },
    'WxTCmd': {
        '--csv': 'An analyst would use the --csv flag with WxTCmd when parsing the Windows 10 Timeline database to export the results into a CSV file for structured analysis of application execution times and user activity.',
        '-f': 'An analyst would use the -f flag with WxTCmd when processing the Windows 10 Timeline database file (ActivitiesCache.db) to extract and save application usage data as a CSV for forensic analysis.',
    },
    'aeskeyfind': {
        '-t': 'An analyst would use the -t flag when examining a memory image with potential bit errors due to memory decay, allowing the tool to tolerate a specified number of discrepancies in candidate key schedules to improve the chances of recovering valid AES keys.',
        '-v': 'An analyst would use the -v flag when examining memory images to obtain detailed verbose output, including extended keys and constraints on the rows of the key schedule, to aid in forensic analysis.',
    },
    'binwalk': {
        '-E': 'An analyst would use the -E flag when analyzing entropy to detect encrypted or compressed sections within a firmware image.',
        '-e': 'An analyst would use the -e flag when automatically extracting embedded files and file systems from a firmware image during firmware reverse engineering or investigation.',
    },
    'bulk_extractor': {
        '-R': 'An analyst would use the -R flag when needing to recursively scan and extract buried evidence from compressed files like ZIP, GZIP, or PDF archives.',
        '-o': 'An analyst would use the -o flag when they need to specify a custom output directory to save the extracted artifacts generated by bulk_extractor.',
    },
    'capinfos': {
        '-T': 'An analyst would use the -T flag when generating a table-style report to organize and export capture file information in a structured format, such as for importing into spreadsheet applications or further analysis.',
        '-n': 'An analyst would use the -n flag when examining a capture file to determine the number of resolved IPv4 and IPv6 addresses present.',
    },
    'chainsaw': {
        '--json': 'An analyst would use the --json flag when they need to output search or analysis results in a structured, machine-readable JSON format for further processing or integration with other tools.',
        '--mapping': 'An analyst would use the --mapping flag when applying third-party detection rules to event logs, as the mapping file specifies which log fields to use for rule matching.',
        '-i': 'An analyst would use the -i flag when searching for a string in event logs where the case of the letters in the pattern may vary, such as when looking for "mimikatz" in logs where it might appear as "MIMIKATZ" or "mimikatz".',
        '-s': 'An analyst would use the -s flag when incorporating Sigma rules into the hunting process to apply third-party detection logic during log analysis.',
        '-t': 'An analyst would use the -t flag when searching for specific event log entries by defining precise tau expressions, such as identifying events by their System EventID in EVTX files.',
    },
    'clamscan': {
        '--exclude-dir': 'An analyst would use the --exclude-dir flag when scanning a system to skip over directories like /proc, /sys, and /dev that contain non-file system data and are not relevant to virus scanning.',
        '--infected': 'An analyst would use the --infected flag when scanning directories or files to quickly identify and isolate only the infected items without displaying clean files, as demonstrated in the examples of showing infected files during recursive scans or automated upload checks.',
        '--max-filesize': 'An analyst would use the --max-filesize flag when scanning directories containing large files to skip scanning files exceeding a specified size, such as 100MB, to avoid unnecessary processing.',
        '--recursive': 'An analyst would use the --recursive flag when scanning a directory and needing to include all subdirectories to ensure every file is checked.',
    },
    'dumpcap': {
        '-w': 'An analyst would use the -w flag when capturing network traffic to disk for later analysis, particularly when managing large volumes of data through ring buffers, size-based file rotation, or time-based segmentation to ensure efficient storage and focused investigation.',
    },
    'evtxexport': {
        '-S': 'An analyst would use the -S flag when exporting event logs from a mounted volume and needing to include the SOFTWARE registry file to resolve software-specific information referenced in the event data.',
        '-f': 'An analyst would use the -f flag when exporting event records from an EVTX file in a specific format, such as XML, to ensure the data is structured for analysis or integration with other tools.',
        '-p': 'An analyst would use the -p flag when specifying the path to a mounted file system or volume containing Windows event logs and registry files for extraction.',
        '-r': 'An analyst would use the -r flag when specifying the directory containing the SYSTEM and SOFTWARE registry files to properly parse event log data from a mounted Windows volume.',
        '-s': 'An analyst would use the -s flag when specifying the path to the SYSTEM registry file to export event log data that requires registry information for proper interpretation.',
    },
    'fls': {
        '-d': 'An analyst would use the -d flag with fls when examining a disk image to identify and list deleted files by their inode numbers for potential recovery.',
        '-f': 'An analyst would use the -f flag when specifying the file system type for non-Windows partitions, such as OpenBSD, to ensure fls correctly interprets the directory structure and file metadata.',
        '-m': "An analyst would use the '-m' flag with 'fls' when gathering allocated file data from each partition of a disk image to create a timeline, as described in the TSK documentation.",
        '-o': 'An analyst would use the -o flag when specifying the starting sector offset of a partition in a disk image to process that specific partition with fls.',
        '-p': 'An analyst would use the -p flag with fls when generating timelines to list files with full paths.',
        '-r': "An analyst would use the '-r' flag with 'fls' when recursively gathering all files from a file system to create a comprehensive timeline of file system activity, as required for processing each partition in a disk image.",
        '-s': "An analyst would use the '-s' flag with 'fls' when adjusting the system's time skew to align timestamps in the body file with those of other servers.",
    },
    'foremost': {
        '-i': 'An analyst would use the `-i` flag when processing a disk image file, such as one generated by `dd`, to specify the input file for forensic carving.',
        '-t': 'An analyst would use the -t flag when specifying particular file types to recover from a disk image during a forensic investigation.',
    },
    'frida': {
        '-N': 'When an analyst needs to inject a script into a specific Android application to modify its behavior, such as bypassing validation or decrypting a flag, they would use the -N flag to target the application by name.',
        '-U': 'When an analyst needs to attach Frida to a target application running on a connected Android device via USB to intercept logs, decrypt data, or hook methods during dynamic instrumentation.',
        '-f': 'An analyst would use the -f flag when needing to inject a script at the start of a target process to bypass security mechanisms like SSL pinning or anti-root protection as the application launches.',
        '-l': "An analyst would use the -l flag when injecting a JavaScript script to modify an application's behavior, such as decrypting obfuscated strings or bypassing security mechanisms like SSL pinning.",
    },
    'fsstat': {
        '-o': "An analyst would use the -o flag with fsstat when examining the file system's data structures, such as the $MFT in NTFS, after determining the correct offset from the partition layout using mmls.",
    },
    'hashcat': {
        '--show': 'An analyst would use the --show flag to display previously cracked hashes stored in the potfile when verifying results or avoiding redundant cracking efforts.',
        '-a': 'An analyst would use the -a flag when performing a combination attack to generate password combinations from two separate wordlists.',
        '-m': 'An analyst would use the -m flag when specifying the hash type (e.g., MD5, SHA-256) to ensure Hashcat correctly interprets the hash format during cracking attempts.',
        '-r': 'An analyst would use the -r flag when applying custom or built-in rule sets to a wordlist to generate password variations during cracking attacks, as demonstrated in the examples involving rules/best64.rule and modifying rules to append specific strings like years to passwords.',
        '-w': 'An analyst would use the -w flag when optimizing Hashcat performance on a dedicated cracking rig with a GPU not driving a display, specifically setting -w 4 for maximum workload intensity.',
    },
    'istat': {
        '-o': "An analyst would use the -o flag with istat when examining metadata of a specific inode to retrieve detailed information about a file's properties and timestamps from a disk image or partition.",
    },
    'john': {
        '--format': 'An analyst would use the --format flag when cracking hashes from specific sources like NTDS.dit or /etc/shadow, or when the hash type requires a specific format identifier such as NT or raw-md5 to ensure John the Ripper correctly interprets the hash structure.',
        '--incremental': 'An analyst would use the --incremental flag when the wordlist has been exhausted and the hash remains uncracked, particularly for short passwords (5-7 characters) where incremental brute-force is feasible.',
        '--rules': 'An analyst would use the --rules flag when applying word mangling rules to a wordlist to generate variations of passwords for cracking, as demonstrated in examples like "john --wordlist=all.lst --rules mypasswd" and similar commands in the documentation.',
        '--show': 'An analyst would use the --show flag after successfully cracking passwords to display the cracked credentials in a human-readable format for review or documentation.',
        '--wordlist': 'An analyst would use the --wordlist flag when attempting to crack password hashes by feeding John the Ripper a file of potential passwords, such as the rockyou.txt wordlist, to compare against the target hash file.',
    },
    'log2timeline.py': {
        '--file-filter': 'An analyst would use the --file-filter flag when processing a full disk image directly to specify individual files or paths for analysis, avoiding the need to create a separate triage collection.',
        '--logfile': 'An analyst would use the --logfile flag when they need to redirect all log messages from log2timeline.py to a file for detailed debugging or record-keeping during processing.',
        '--partitions': 'An analyst would use the --partitions flag when processing a disk image with multiple partitions and needing to specify a particular partition number to avoid interactive prompts during the analysis.',
        '--storage-file': 'An analyst would use the --storage-file flag when processing a storage media image to specify the output file where the extracted timeline events will be stored.',
        '--timezone': "When analyzing loose files, a triage collection, or when the system's time zone cannot be auto-detected, an analyst would use the --timezone flag to explicitly specify the source system's time zone.",
    },
    'mactime': {
        '-b': 'An analyst would use the -b flag when processing a body file to generate a timeline of file activity based on timestamps extracted from the file system.',
        '-i': 'An analyst would use the -i flag when creating an index summary file to import into a spreadsheet for graphing suspicious behavior, such as when analyzing file activity hits per day or hour.',
        '-z': 'An analyst would use the -z flag when the time zone of the data in the body file differs from their local time zone to ensure accurate timestamp interpretation in the timeline.',
    },
    'mergecap': {
        '-F': 'An analyst would use the -F flag when they need to specify a particular output format for the merged capture file, such as when the default pcapng format is not suitable or when compatibility with specific tools requires a different format.',
        '-w': 'An analyst would use the -w flag with mergecap when they need to aggregate and consolidate multiple packet capture files into a single output file for further analysis or sharing with a colleague.',
    },
    'mmls': {
        '-o': "An analyst would use the -o flag when analyzing an embedded filesystem by specifying its sector offset, obtained from mmls output, to correctly reference files within a partition that isn't the primary boot volume.",
    },
    'mraptor': {
        '--zip': 'When an analyst needs to scan a file contained within a password-protected ZIP archive, such as "malicious_file.xls" with the password "infected".',
        '-r': 'An analyst would use the -r flag when scanning multiple files across subdirectories to check for suspicious macro behaviors recursively.',
    },
    'olevba': {
        '--decode': 'An analyst would use the --decode flag when examining a document to reveal obfuscated strings by displaying them in decoded form.',
        '--reveal': "An analyst would use the --reveal flag when examining a file to deobfuscate and display the macro source code's VBA strings in a readable format.",
        '-d': 'An analyst would use the -d flag when performing a detailed analysis of a single file to display all details of the VBA macro examination.',
        '-r': 'An analyst would use the -r flag when scanning a directory structure to recursively process all .doc and .xls files in subfolders.',
        '-z': 'An analyst would use the -z flag when scanning encrypted documents stored in a Zip archive that require a password to access their contents.',
    },
    'regipy-diff': {
        '-o': 'An analyst would use the -o flag when comparing registry hives to save the resulting differences to a CSV file for further analysis or documentation.',
    },
    'regipy-dump': {
        '-t': 'An analyst would use the -t flag when they need to output a timeline of the registry hive data instead of a JSON file.',
    },
    'regripper': {
        '-f': 'An analyst would use the -f flag when specifying the type of registry hive file being parsed, such as system, sam, or ntuser, to ensure RegRipper applies the correct plugin configurations during analysis.',
        '-l': 'An analyst would use the -l flag when they need to list all available plugins to determine which ones to apply during registry analysis.',
        '-p': 'An analyst would use the -p flag when they need to execute a specific plugin module on a registry hive file, such as extracting user-assist data from an NTUSER.DAT file.',
    },
    'reordercap': {
        '-n': 'An analyst would use the -n flag when verifying if a pcap file is already in chronological order to avoid unnecessary processing and output file creation.',
    },
    'sigtool': {
        '--hex-dump': "An analyst would use the --hex-dump flag when needing to generate a hexadecimal representation of a file's contents for detailed forensic examination or signature creation.",
    },
    'ssdeep': {
        '-b': 'An analyst would use the -b flag when processing multiple files from different directories to generate fuzzy hashes based only on filenames, ignoring directory paths.',
        '-d': 'An analyst would use the -d flag when comparing multiple files across directories to identify similar or duplicate documents, such as eliminating redundant Microsoft Word files in folders like Incoming, Outgoing, and Trash.',
        '-m': 'An analyst would use the -m flag when comparing files against a precomputed fuzzy hash signature or database to identify matches, such as verifying if a file corresponds to a known hash stored in a file like sig.txt or fuzzy.db.',
        '-s': 'An analyst would use the -s flag when creating a database of fuzzy hashes for later comparison to detect similarities between files, even if they have been slightly modified.',
    },
    'tcpflow': {
        '-C': 'An analyst would use the -C flag when they need to view flow data in the console without the display of source/destination headers.',
        '-o': 'An analyst would use the -o flag when they need to specify a particular directory to store the transcript files generated by tcpflow during packet analysis.',
        '-r': 'An analyst would use the -r flag when processing a pcap file to automatically decode and save TCP flows, such as extracting HTTP responses or reconstructing data from network captures.',
    },
    'tcpxtract': {
        '-o': 'An analyst would use the -o flag when performing a live capture from a network interface to specify the output directory for extracted files.',
    },
    'tshark': {
        '-q': 'An analyst would use the -q flag when running tshark with the -z option to generate specific statistics, as shown in examples like "tshark -q -z io,stat,5,ip.addr==255.255.255.255" and "tshark -q -z conv.',
    },
    'upx': {
        '-d': 'An analyst would use the `-d` flag with UPX when encountering a malware sample packed with UPX to automatically unpack it into its original executable form.',
        '-o': 'An analyst would use the -o flag when unpacking a UPX-packed sample to specify the output file name for the unpacked executable, as demonstrated in the example command.',
    },
    'xlmdeobfuscator': {
        '--no-indent': 'An analyst would use the --no-indent flag when they need to extract deobfuscated macros from an Excel document without any formatting indentation to simplify analysis or processing.',
        '--output-formula-format': 'An analyst would use the --output-formula-format flag when they need to deobfuscate macros in Excel documents and want the output to display only the integer-formula representation without any indentation or additional formatting.',
        '-x': 'An analyst would use the -x flag when they need to extract macros from Excel documents without performing any deobfuscation.',
    },
    'xortool': {
        '-p': "An analyst would use the -p flag when they have a known plaintext segment to aid in decrypting XOR-encrypted data, as demonstrated in examples where it's paired with encrypted files and brute-force options.",
        '-t': 'When analyzing a Base64-encoded XORed message to filter plaintexts to only those containing valid Base64 characters.',
        '-x': 'An analyst would use the -x flag when processing a hex-encoded file, such as when decrypting data that has been represented in hexadecimal format.',
    },
    'yara': {
        '-v': 'An analyst would use the -v flag when validating the syntax of a YARA rule to ensure it is correctly formatted before testing it against files.',
    },
}

for _cmd, _fl in RESEARCHED_FLAGS.items():
    _w = ENRICHMENT.setdefault(_cmd, {}).setdefault('when', {})
    for _f, _n in _fl.items():
        _w.setdefault(_f, _n)

# Hand-written entries win: a human who wrote a scenario has
# judged it, and a research pass must never overwrite that.
for _cmd, _rec in RESEARCHED.items():
    _e = ENRICHMENT.setdefault(_cmd, {})
    _e.setdefault('scenario', _rec['scenario'])
    _e.setdefault('sources', _rec['sources'])
# --- END researched scenarios ---
