#!/usr/bin/env python3
"""The capability taxonomy — the guide's primary index.

Capabilities are phrased as PROBLEMS ("recover deleted files"), not tool names,
because that is the state you are in when you open this guide in the field: you
know what you need to achieve, not which binary achieves it.

Phase grouping follows NIST SP 800-86 (collect -> examine -> analyse -> report)
with the SANS FOR508 working order layered on top. Within a phase, capabilities
are ordered the way an investigation actually runs.

Mapping is explicit, not guessed: each capability lists the commands that serve
it. A captured tool that matches no capability is REPORTED, never silently
dropped — an unmapped tool is either a taxonomy gap or out of scope, and both
need a human decision.
"""
from __future__ import annotations

# phase -> [(capability, [commands...])]
TAXONOMY: dict[str, list[tuple[str, list[str]]]] = {

    "Acquire & preserve": [
        ("Image a disk, volume or device",
         ["dc3dd", "dcfldd", "dd", "ewfacquire", "guymager", "affconvert"]),
        ("Verify evidence integrity with hashes",
         ["hashdeep", "md5deep", "sha256deep", "rahash2", "ssdeep", "sha256sum",
          "md5sum", "sigtool"]),
        ("Inspect or mount a forensic image container",
         ["ewfinfo", "ewfmount", "ewfverify", "ewfexport", "affinfo", "affcat",
          "img_stat", "ntfs-3g", "vshadowinfo", "bdeinfo"]),
        ("Capture live network traffic",
         ["dumpcap", "tcpdump", "tshark"]),
    ],

    "Examine the filesystem": [
        ("See the partition and volume layout",
         ["mmls", "fsstat", "img_stat", "testdisk"]),
        ("List files and directories, including deleted ones",
         ["fls", "ffind", "ils", "tsk_recover"]),
        ("Recover deleted or lost files",
         ["tsk_recover", "icat", "photorec", "testdisk", "ext4magic",
          "extundelete", "ext3grep", "blkls"]),
        ("Carve files out of unstructured data",
         ["foremost", "scalpel", "binwalk", "bulk_extractor", "tcpxtract",
          "magicrescue"]),
        ("Inspect metadata for one file or inode",
         ["istat", "ils", "exiftool", "file", "trid", "magika", "stat"]),
        ("Search raw data for a pattern",
         ["lightgrep", "rafind2", "strings", "grep", "xxd", "bulk_extractor"]),
    ],

    "Build the timeline": [
        ("Build a super-timeline from many artifact sources",
         ["log2timeline.py", "psort.py", "psteal.py", "pinfo.py"]),
        ("Build a filesystem MAC-time timeline",
         ["fls", "mactime", "tsk_gettimes"]),
    ],

    "Windows artifacts": [
        ("Parse registry hives",
         ["rip.pl", "regripper", "hivexsh", "hivexget", "hivexml", "regfexport",
          "regfinfo", "regfmount", "regipy-dump", "regipy-parse-header",
          "regipy-plugins-run", "regipy-diff", "RECmd"]),
        ("Parse Windows event logs",
         ["evtxexport", "evtxinfo", "EvtxECmd", "chainsaw", "hayabusa",
          "evtx_dump"]),
        ("Parse ESE / SRUM / Amcache databases",
         ["esedbexport", "esedbinfo", "SrumECmd", "AmcacheParser"]),
        ("Parse execution and persistence artifacts",
         ["PECmd", "AppCompatCacheParser", "MFTECmd", "analyzeMFT", "AmcacheParser"]),
        ("Parse mail stores",
         ["pffexport", "pffinfo", "readpst"]),
    ],

    "Memory forensics": [
        ("Analyse a memory image",
         ["vol", "vol.py", "volatility3", "volshell", "rekall"]),
        ("Recover encryption keys from memory",
         ["aeskeyfind", "rsakeyfind", "bulk_extractor"]),
    ],

    "Network analysis": [
        ("Read and filter packet captures",
         ["tshark", "capinfos", "ngrep", "tcpflow"]),
        ("Split, merge or repair capture files",
         ["editcap", "mergecap", "reordercap"]),
        ("Extract files and payloads from traffic",
         ["tcpxtract", "tcpflow", "foremost"]),
        ("Detect intrusions in traffic",
         ["suricata", "suricatasc", "zeek", "zeek-cut", "rita"]),
        ("Probe or scan hosts and services",
         ["nmap", "nping", "ncat", "arp-scan", "netdiscover"]),
        ("Simulate network services for detonation",
         ["inetsim", "fakedns", "fakenet"]),
    ],

    "Malware triage — static": [
        ("Identify what a file actually is",
         ["file", "trid", "die", "diec", "magika", "exiftool"]),
        ("Scan with signatures for known-bad",
         ["yara", "yarac", "clamscan", "clamdscan", "freshclam", "sigtool"]),
        ("Identify capabilities in a binary",
         ["capa", "floss"]),
        ("Extract strings, including obfuscated ones",
         ["floss", "strings", "base64dump.py", "numbers-to-string.py"]),
        ("Inspect PE / ELF structure",
         ["rabin2", "readelf", "readelf.py", "objdump", "pescan", "pecheck.py",
          "peframe"]),
        ("Detect and reverse packing",
         ["upx", "die", "diec", "binwalk", "7za", "unzip"]),
        ("Compare or cluster samples",
         ["ssdeep", "radiff2", "bytehist"]),
    ],

    "Malware triage — documents": [
        ("Analyse Office documents and macros",
         ["olevba", "oleid", "oledump.py", "olemeta", "oletimes", "olemap",
          "oledir", "olebrowse", "olefile", "oleobj", "mraptor", "msodde",
          "pcodedmp", "pyxswf", "xlmdeobfuscator", "runxlrd2.py", "vipermonkey"]),
        ("Analyse RTF documents and embedded objects",
         ["rtfobj", "rtfdump.py", "oleobj"]),
        ("Analyse PDFs",
         ["pdfid", "pdfid.py", "pdf-parser", "pdf-parser.py", "peepdf", "qpdf"]),
        ("Analyse other container formats",
         ["7za", "unzip", "msoffcrypto-tool", "onenoteanalyzer"]),
    ],

    "Reverse engineering": [
        ("Disassemble and explore a binary",
         ["r2", "rizin", "rabin2", "rasm2", "objdump", "vivbin", "vdbbin",
          "ghidra", "cutter"]),
        ("Diff two binaries",
         ["radiff2", "bindiff"]),
        ("Emulate or instrument execution",
         ["frida", "frida-trace", "frida-ps", "frida-discover", "frida-kill",
          "frida-ls-devices", "speakeasy", "qiling", "scdbg", "unicorn"]),
        ("Analyse shellcode",
         ["scdbg", "rasm2", "xortool", "shellcode2exe"]),
    ],

    "Decode & deobfuscate": [
        ("Decode, decrypt or transform encoded data",
         ["cyberchef", "base64dump.py", "rax2", "xxd", "openssl",
          "numbers-to-string.py"]),
        ("Break simple obfuscation",
         ["xortool", "floss", "xlmdeobfuscator", "de4dot"]),
        ("Crack passwords and hashes",
         ["hashcat", "john", "hydra", "unshadow", "zip2john", "rar2john",
          "fcrackzip", "hashid"]),
        ("Find hidden data",
         ["steghide", "stegosuite", "binwalk", "ssdeep"]),
    ],

    "Report & support": [
        ("Fetch and verify external references",
         ["curl", "wget"]),
        ("Inspect files by hand",
         ["xxd", "ezhexviewer", "hexdump", "less"]),
    ],
}

# Commands deliberately excluded from the index: build/runtime plumbing that a
# container happens to ship. Present in the kit, not part of an investigation.
NOT_A_CAPABILITY = {
    "perl", "python3", "python", "pkg-config", "patch", "dotnet", "gcc", "g++",
    "make", "cmake", "pip", "pip3", "npm", "node", "ruby", "gem", "java",
    "sudo", "set", "bash", "sh", "dash", "env",
}


def capability_of(cmd: str) -> list[tuple[str, str]]:
    """Return [(phase, capability)] that this command serves."""
    hits = []
    for phase, caps in TAXONOMY.items():
        for cap, cmds in caps:
            if cmd in cmds:
                hits.append((phase, cap))
    return hits


def all_mapped_commands() -> set[str]:
    return {c for caps in TAXONOMY.values() for _, cmds in caps for c in cmds}
