#!/usr/bin/env python3
"""Emit the candidate command names to probe inside the kit containers.

Sources every name from catalog/kit-tools.json so the probe can never drift
from the binding scope: binaries named by REMnux, plus package/tool names
(normalised) for the platforms whose manifests only give package names.
"""
from __future__ import annotations
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KIT = json.loads((ROOT / "catalog" / "kit-tools.json").read_text(encoding="utf-8"))

# Package names that are demonstrably not commands.
SKIP = re.compile(
    r"^(lib|python3?-|ruby-|perl-|golang-|fonts?-|.*-doc$|.*-dev$|.*-data$|"
    r".*-common$|.*-tools?$|.*-scripts$|.*-plugins?$)", re.I)

# Package -> real binary, where they differ and it matters.
ALIASES = {
    "sleuthkit": ["fls", "mmls", "icat", "istat", "fsstat", "blkls", "img_stat",
                  "tsk_recover", "tsk_gettimes", "mactime", "ffind", "ils"],
    "afflib-tools": ["affinfo", "affconvert", "affcat"],
    "ewf-tools": ["ewfinfo", "ewfacquire", "ewfexport", "ewfverify", "ewfmount"],
    "libhivex-bin": ["hivexget", "hivexsh", "hivexregedit"],
    "python3-volatility3": ["vol"],
    "volatility3": ["vol"],
    "volatility": ["vol.py", "vol"],
    "plaso": ["log2timeline.py", "psort.py", "pinfo.py", "psteal.py"],
    "python3-plaso": ["log2timeline.py", "psort.py", "pinfo.py"],
    "wireshark": ["tshark", "capinfos", "editcap", "mergecap", "dumpcap", "reordercap"],
    "tshark": ["tshark"],
    "clamav": ["clamscan", "freshclam", "sigtool", "clamdscan"],
    "yara": ["yara", "yarac"],
    "bulk-extractor": ["bulk_extractor"],
    "exiftool": ["exiftool"],
    "libimage-exiftool-perl": ["exiftool"],
    "regripper": ["rip.pl", "rip"],
    "hashdeep": ["hashdeep", "md5deep", "sha256deep"],
    "john": ["john", "unshadow", "zip2john", "rar2john"],
    "hashcat": ["hashcat"],
    "nmap": ["nmap", "ncat", "nping"],
    "binutils": ["objdump", "readelf", "strings", "nm", "strip"],
    "radare2": ["r2", "rabin2", "rax2", "radiff2", "rafind2"],
    "rizin": ["rizin", "rz-bin", "rz-find"],
    "foremost": ["foremost"],
    "scalpel": ["scalpel"],
    "testdisk": ["testdisk", "photorec"],
    "chainsaw": ["chainsaw"],
    "hayabusa": ["hayabusa"],
    "velociraptor": ["velociraptor"],
    "zeek": ["zeek", "zeek-cut"],
    "suricata": ["suricata", "suricatasc"],
    "tcpdump": ["tcpdump"],
    "sqlite3": ["sqlite3"],
    "dc3dd": ["dc3dd"],
    "dcfldd": ["dcfldd"],
    "guymager": ["guymager"],
    "binwalk": ["binwalk"],
    "oletools": ["olevba", "oleid", "oledump.py", "rtfobj", "msodde"],
    "pdfid": ["pdfid.py", "pdfid"],
    "pdf-parser": ["pdf-parser.py", "pdf-parser"],
    "capa": ["capa"],
    "flare-floss": ["floss"],
    "floss": ["floss"],
    "die": ["diec", "die"],
    "detect-it-easy": ["diec"],
    "upx-ucl": ["upx"],
    "upx": ["upx"],
    "steghide": ["steghide"],
    "ssdeep": ["ssdeep"],
    "trid": ["trid"],
    "magika": ["magika"],
}


def normalise(name: str) -> list[str]:
    n = name.strip()
    if not n:
        return []
    low = n.lower()
    if low in ALIASES:
        return ALIASES[low]
    # Drop display-name decoration: "The Sleuth Kit (TSK)" -> "the sleuth kit"
    low = re.sub(r"\(.*?\)", "", low).strip()
    if low in ALIASES:
        return ALIASES[low]
    if SKIP.match(low):
        return []
    # A plausible command name: single token, no spaces.
    tok = low.replace(" ", "-")
    if re.fullmatch(r"[a-z0-9][a-z0-9._+-]{1,40}", tok):
        return [tok]
    return []


def main() -> None:
    cands: set[str] = set()
    for vm, cats in KIT["kit"].items():
        for cat, entries in cats.items():
            for e in entries:
                for b in e.get("binaries") or []:
                    cands.update(normalise(b))
                cands.update(normalise(e["tool"]))
    out = ROOT / "capture" / "_candidates.txt"
    out.parent.mkdir(exist_ok=True)
    out.write_text("\n".join(sorted(cands)) + "\n", encoding="utf-8")
    print(f"{len(cands)} candidate commands -> {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
