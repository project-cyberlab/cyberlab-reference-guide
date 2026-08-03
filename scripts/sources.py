#!/usr/bin/env python3
"""Find where a tool or flag is actually USED, and keep the surrounding prose.

Reference documentation defines a flag. It almost never says when an analyst
would reach for it, because that is not what reference documentation is for.
A walkthrough is different: it uses the flag inside a scenario, and the prose
around the command says why.

So the query here is not "what does fls -s do". It is "find fls -s being used
and read the paragraph around it". Proven on fls before this module was
written: `--help` says -s "adjusts times", while a walkthrough says it exists
for when you are correlating a host against other servers whose clocks
disagree. The second is the thing a junior analyst needs, and no amount of
reasoning over --help produces it.

Search is a self-hosted SearxNG on rick. It metasearches, needs no API key,
and gives the local models, the free API models and me the same interface --
which is what makes cross-validation between them possible at all.

Nothing here writes to a page. It returns evidence with a URL attached, and
the caller decides.
"""
from __future__ import annotations
import json
import re
import threading
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "capture" / "source-cache"

# rick over the tailnet; the LAN address is not routable from this host.
SEARX = "http://100.112.76.79:8888"

UA = "Mozilla/5.0 (compatible; cyberlab-reference-guide/1.0)"

# Reputation, not a hard allowlist. A hard allowlist cannot find a university
# lab exercise nobody thought to list in advance, and those turned out to be
# the best flag-level source there is. So rank instead: trusted publishers
# float up, known-bad content sinks, everything else is usable but has to
# survive corroboration.
TRUSTED = (
    "attack.mitre.org", "sans.org", "sleuthkit.org", "github.com",
    "docs.remnux.org", "ericzimmerman.github.io", "thedfirreport.com",
    "redcanary.com", "learn.microsoft.com", "nmap.org", "wireshark.org",
    "volatilityfoundation.org", "blog.didierstevens.com", "didierstevens.com",
    "manpages.debian.org", "man7.org", "readthedocs.io", "kali.org",
    "malware-traffic-analysis.net", "unit42.paloaltonetworks.com",
    "mandiant.com", "nist.gov", "cisa.gov", "forensicswiki.xyz",
    ".edu", ".ac.uk",
)

# Content farms and answer-scrapers: confidently wrong, and they plagiarise
# each other so corroboration between them means nothing.
DENY = (
    "w3schools", "geeksforgeeks", "tutorialspoint", "javatpoint",
    "chegg.com", "coursehero", "scribd", "quizlet", "studocu",
    "linuxhint", "codegrepper", "stackoverflow.com/jobs",
)


# A search for a two-letter flag matches the whole internet. '"fls -s"
# example' returned a float-switch datasheet. The tool's subject area has to
# go into the query or the results are noise, and the anchor that works is
# the one a practitioner would actually type -- the suite name and the task,
# not the word "forensics" bolted on.
ANCHORS = {
    "fls": "sleuthkit timeline body file",
    "mactime": "sleuthkit timeline",
    "icat": "sleuthkit file recovery",
    "mmls": "sleuthkit partition layout",
    "fsstat": "sleuthkit filesystem",
    "tsk_recover": "sleuthkit export files",
    "pdfid": "malicious PDF triage Didier Stevens",
    "pdf-parser": "malicious PDF analysis Didier Stevens",
    "pdf-parser.py": "malicious PDF analysis Didier Stevens",
    "olevba": "malicious macro Office document oletools",
    "oleid": "malicious Office document oletools",
    "oleobj": "embedded object Office document oletools",
    "rtfobj": "malicious RTF oletools",
    "mraptor": "macro triage oletools",
    "vol": "volatility memory forensics",
    "volatility3": "volatility memory forensics",
    "nmap": "network scanning NSE",
    "nping": "packet crafting network probe",
    "tshark": "packet capture analysis wireshark",
    "capinfos": "packet capture wireshark",
    "editcap": "packet capture wireshark",
    "mergecap": "packet capture wireshark",
    "binwalk": "firmware extraction embedded file carving",
    "bulk_extractor": "bulk extractor forensic feature extraction",
    "foremost": "file carving recovery",
    "photorec": "file carving recovery testdisk",
    "testdisk": "partition recovery repair",
    "hashcat": "password cracking hash",
    "john": "password cracking hash john the ripper",
    "log2timeline.py": "plaso super timeline",
    "psort.py": "plaso super timeline",
    "frida": "dynamic instrumentation reverse engineering",
    "frida-trace": "dynamic instrumentation reverse engineering",
    "radare2": "reverse engineering disassembly",
    "r2": "reverse engineering disassembly",
    "yara": "yara rule malware detection",
    "clamscan": "clamav malware scanning",
    "exiftool": "metadata extraction forensics",
    "chainsaw": "windows event log hunting sigma",
    "hayabusa": "windows event log hunting sigma",
    "evtxexport": "windows event log forensics",
    "dc3dd": "forensic imaging acquisition",
    "dcfldd": "forensic imaging acquisition",
    "ewfacquire": "forensic imaging E01 acquisition",
    "diec": "Detect It Easy packer identification",
    "upx": "executable packing unpacking",
    "strings": "malware triage strings",
    "ssdeep": "fuzzy hashing similarity malware",
}


def _deadline(fn, timeout: float, default):
    """Run fn with a hard wall-clock bound.

    urllib's own timeout does not fire on a socket that keeps trickling
    bytes. The cyberlab loop lost 18 minutes to exactly that, and its
    subprocess timeout was an hour. A daemon thread returns regardless.
    """
    box = [default]

    def run():
        try:
            box[0] = fn()
        except Exception:
            pass

    t = threading.Thread(target=run, daemon=True)
    t.start()
    t.join(timeout)
    return box[0]


def _get(url: str, timeout: float = 15) -> str:
    def go():
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read(2_000_000).decode("utf-8", "replace")
    return _deadline(go, timeout + 5, "")


def trust(url: str) -> int:
    """3 = trusted publisher, 0 = usable, -1 = refuse."""
    u = url.lower()
    if any(d in u for d in DENY):
        return -1
    return 3 if any(t in u for t in TRUSTED) else 0


# Minimum seconds between searches.
#
# SearxNG is a metasearch front end: it has no index of its own and forwards
# to consumer engines that police automated traffic. A pass firing roughly 400
# queries suspended all four -- brave and google cse "too many requests",
# startpage a CAPTCHA with an hour-long suspension, duckduckgo timing out --
# and every tool searched afterwards was recorded as having no sources.
#
# That is the worst failure mode this project has, because it does not look
# like a failure. It looks like an answered question with the answer "nothing
# exists", which is the one conclusion the guide is forbidden to draw.
#
# Pacing keeps a long pass inside what the upstreams tolerate. The durable fix
# is an index that expects programmatic use -- see docs/LOOP-RESEARCH.md.
SEARCH_INTERVAL = 1.5
_last_search = [0.0]


def _pace() -> None:
    gap = time.time() - _last_search[0]
    if gap < SEARCH_INTERVAL:
        time.sleep(SEARCH_INTERVAL - gap)
    _last_search[0] = time.time()


def _search_once(query: str) -> list | None:
    q = urllib.parse.urlencode({"q": query, "format": "json"})
    raw = _get(f"{SEARX}/search?{q}", timeout=30)
    if not raw:
        return None
    try:
        return json.loads(raw).get("results", [])
    except json.JSONDecodeError:
        return None


def search(query: str, limit: int = 10) -> list[dict]:
    """Metasearch, best-trusted first, junk dropped.

    Retries an empty result, because empty usually means the upstream engines
    are rate-limited rather than that nothing exists. A whole pass once
    recorded 39 tools as having no sources at all; the cause was Wikipedia
    answering "Too many request (suspended_time=180)" and DuckDuckGo timing
    out, not an absent internet. A loop that turns throttling into "no answer
    exists" manufactures exactly the false conclusion this project is built
    to avoid, and it does it silently and at scale.
    """
    _pace()
    results = _search_once(query)
    if not results:
        # One retry only. Suspensions here are measured in minutes to an hour,
        # so hammering the retry neither recovers the engine nor helps -- it is
        # what exhausted them in the first place.
        time.sleep(6)
        results = _search_once(query)
    if not results:
        return []
    out = []
    for r in results:
        url = r.get("url", "")
        t = trust(url)
        if t < 0:
            continue
        out.append({"url": url, "title": r.get("title", ""),
                    "snippet": r.get("content", ""), "trust": t})
    out.sort(key=lambda r: -r["trust"])
    return out[:limit]


_TAG = re.compile(r"<(script|style)[^>]*>.*?</\1>", re.S | re.I)
_ANY = re.compile(r"<[^>]+>")


def fetch_text(url: str, max_chars: int = 40000) -> str:
    """Page text, cached on disk. Cache is keyed by URL, never expires here --
    a walkthrough from 2014 is as true today as it was then."""
    CACHE.mkdir(parents=True, exist_ok=True)
    key = re.sub(r"[^A-Za-z0-9]+", "_", url)[:120]
    p = CACHE / f"{key}.txt"
    if p.exists():
        return p.read_text(encoding="utf-8", errors="replace")[:max_chars]
    html = _get(url)
    if not html:
        return ""
    text = _ANY.sub(" ", _TAG.sub(" ", html))
    text = re.sub(r"&nbsp;?", " ", text)
    text = re.sub(r"&amp;", "&", text)
    text = re.sub(r"&lt;", "<", text)
    text = re.sub(r"&gt;", ">", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n\n", text)
    # Never cache a failed fetch. forensicswiki.xyz is dead and returns a
    # 12-character body; caching that meant the URL could never be retried,
    # and four tools were permanently starved of sources by one dead host
    # while the diagnostics reported it as "search terms are wrong". An empty
    # result is a transient condition until proven otherwise.
    if len(text.strip()) >= 500:
        p.write_text(text, encoding="utf-8")
    return text[:max_chars]


# Language that signals a scenario rather than a definition. A synopsis line
# reads "[-s seconds]"; a scenario reads "so that the system is consistent
# with other servers". These weights are what tell them apart.
_SCENARIO_CUES = (
    (r"\bso that\b", 3), (r"\bin order to\b", 3), (r"\bbecause\b", 3),
    (r"\bwhen you\b", 3), (r"\bif you\b", 3), (r"\bwhen the\b", 2),
    (r"\bthis (?:is )?(?:useful|matters|lets|allows)\b", 3),
    (r"\btaken into consideration\b", 2), (r"\bconsider\b", 2),
    (r"\byou (?:can|should|want|need|would)\b", 2),
    (r"\bthe (?:first|next|final) step\b", 2), (r"\bstep \d\b", 2),
    (r"\bthen (?:run|use)\b", 2), (r"\bafter (?:running|you)\b", 2),
    (r"\bbefore (?:running|you)\b", 2), (r"\brequires? the\b", 2),
    (r"\binstead of\b", 2), (r"\brather than\b", 2), (r"\bunlike\b", 2),
    (r"\bnote:?\b", 1), (r"\bcaution\b", 2), (r"\bwarning\b", 2),
)
# Reference-manual furniture: present in every man page, carries no scenario.
_BOILERPLATE = (
    (r"\bsynopsis\b", -4), (r"\btable of contents\b", -4),
    (r"\bcopyright\b", -3), (r"\bsee also\b", -2),
    (r"\bmanual page\b", -3), (r"\bAUTHOR\b", -2),
)


def score_passage(chunk: str) -> int:
    """How likely this text explains WHEN to use something, not what it is."""
    s = 0
    for pat, w in _SCENARIO_CUES:
        if re.search(pat, chunk, re.I):
            s += w
    for pat, w in _BOILERPLATE:
        if re.search(pat, chunk, re.I):
            s += w
    return s


def passages_using(text: str, token: str, window: int = 700,
                   limit: int = 6, near: str | None = None) -> list[tuple[int, str]]:
    """The prose around each place `token` is used, best-scoring first.

    This is the whole point of the module. The flag's own definition is
    worthless to us; the sentences someone wrote around an actual invocation
    are where the scenario lives.

    Ordering matters more than it looks. Taking matches in document order put
    the man-page synopsis line first for `fls -s` and pushed out the sentence
    that actually explained it -- "so that the system is consistent with other
    servers", which is the whole answer. Score, then take the best.
    """
    scored, seen = [], set()
    # A bare flag matches far too much. Searching for "-s" alone landed on a
    # stray hyphen in an article about NTFS alternate data streams that never
    # mentions fls at all. The flag only counts as evidence when the tool it
    # belongs to is nearby -- that is what makes it an invocation rather than
    # a coincidence.
    pat = re.escape(token) + r"(?![\w-])"
    # Require the flag to be preceded by the tool name within a short reach,
    # which is what a real command line looks like: "fls -o 63 -f openbsd -m".
    for m in re.finditer(pat, text):
        lo = max(0, m.start() - window)
        hi = min(len(text), m.end() + window)
        if near:
            # Look both ways. A command line puts the tool first
            # ("fls -o 63 -m / -r image.dd"), but prose often puts it after
            # ("Using the '-s' argument to 'fls'") -- and that second form is
            # exactly the sentence that carries the scenario, so a
            # backwards-only check throws away the best evidence.
            ctx = text[max(0, m.start() - 200):m.end() + 200]
            if not re.search(r"(?<![\w-])" + re.escape(near) + r"(?![\w-])",
                             ctx, re.I):
                continue
        chunk = " ".join(text[lo:hi].split())
        k = chunk[:120]
        if k in seen:
            continue
        seen.add(k)
        scored.append((score_passage(chunk), chunk))
    scored.sort(key=lambda p: -p[0])
    return scored[:limit]


# Pages that are certainly worth reading for a tool, regardless of what any
# search engine decides to return today. Search is a discovery mechanism, not
# a reliable one: the Sleuth Kit's own Timelines wiki page is THE source for
# what `fls -s` is for, and it came back on one query and not the next. Seeds
# make the canonical sources deterministic; search adds what we did not think
# to list.
SEEDS: dict[str, tuple[str, ...]] = {}


def _seed_suite(tools: str, urls: tuple[str, ...]) -> None:
    for t in tools.split():
        SEEDS[t] = urls


_seed_suite(
    "fls mactime icat ils istat mmls fsstat blkls blkcat ffind ifind "
    "tsk_recover tsk_gettimes img_stat srch_strings",
    ("https://github.com/sleuthkit/sleuthkit/wiki/Timelines",
     "https://github.com/sleuthkit/sleuthkit/wiki/Body-file",
     "https://wiki.sleuthkit.org/index.php?title=FS_Analysis"),
)
_seed_suite(
    "pdfid pdfid.py pdf-parser pdf-parser.py",
    ("https://blog.didierstevens.com/programs/pdf-tools/",
     "https://blog.didierstevens.com/2008/10/30/pdfid/"),
)
_seed_suite(
    "olevba oleid oleobj rtfobj mraptor msodde olemeta oletimes oledir "
    "olemap olebrowse pyxswf",
    ("https://github.com/decalage2/oletools/wiki",
     "https://github.com/decalage2/oletools/wiki/olevba",
     "https://github.com/decalage2/oletools/wiki/oleid"),
)
_seed_suite(
    "vol volatility3 volshell",
    ("https://volatility3.readthedocs.io/en/latest/basics.html",),
)
_seed_suite(
    "nmap nping ncat",
    ("https://nmap.org/book/man-briefoptions.html",
     "https://nmap.org/book/nse-usage.html"),
)
_seed_suite(
    "tshark capinfos editcap mergecap dumpcap",
    ("https://www.wireshark.org/docs/wsug_html_chunked/AppToolstshark.html",),
)
_seed_suite(
    "photorec testdisk fidentify",
    ("https://www.cgsecurity.org/wiki/PhotoRec_Step_By_Step",
     "https://www.cgsecurity.org/wiki/TestDisk_Step_By_Step",
     "https://www.cgsecurity.org/wiki/PhotoRec"),
)
_seed_suite(
    "binwalk",
    ("https://github.com/ReFirmLabs/binwalk/wiki/Usage",),
)
_seed_suite(
    "foremost scalpel",
    ("http://foremost.sourceforge.net/",
     "https://www.kali.org/tools/foremost/",
     "https://www.kali.org/tools/scalpel/"),
)
_seed_suite(
    "bulk_extractor",
    ("https://github.com/simsong/bulk_extractor/wiki",),
)
_seed_suite(
    "exiftool",
    ("https://exiftool.org/examples.html",),
)
_seed_suite(
    "hashcat",
    ("https://hashcat.net/wiki/doku.php?id=hashcat",
     "https://hashcat.net/wiki/doku.php?id=frequently_asked_questions"),
)
_seed_suite(
    "john",
    ("https://www.openwall.com/john/doc/EXAMPLES.shtml",),
)
_seed_suite(
    "yara",
    ("https://yara.readthedocs.io/en/stable/writingrules.html",),
)
_seed_suite(
    "chainsaw hayabusa",
    ("https://github.com/WithSecureLabs/chainsaw",
     "https://github.com/Yamato-Security/hayabusa"),
)
_seed_suite(
    "dd dc3dd dcfldd ewfacquire guymager ewfinfo ewfmount",
    ("https://github.com/libyal/libewf/wiki/Tools",
     "https://www.kali.org/tools/dc3dd/",
     "https://www.kali.org/tools/dcfldd/",
     "https://www.kali.org/tools/guymager/"),
)
_seed_suite(
    "radare2 r2",
    ("https://book.rada.re/basic_commands/intro.html",),
)
_seed_suite(
    "frida frida-trace",
    ("https://frida.re/docs/frida-trace/",),
)
_seed_suite(
    "diec die",
    ("https://github.com/horsicq/Detect-It-Easy",),
)
_seed_suite(
    "upx",
    ("https://github.com/upx/upx/blob/devel/README.md",),
)
_seed_suite(
    "ssdeep",
    ("https://ssdeep-project.github.io/ssdeep/usage.html",),
)
_seed_suite(
    "log2timeline.py psort.py pinfo.py",
    ("https://plaso.readthedocs.io/en/latest/sources/user/Using-log2timeline.html",),
)


def corpus_for(tool: str, max_pages: int = 10) -> list[dict]:
    """Pages worth mining for this tool: canonical seeds, then search.

    Built once per tool and cached on disk, so every one of a tool's flags is
    mined from the same corpus instead of running a fresh search per flag.
    """
    anchor = ANCHORS.get(tool, "forensics DFIR analysis")
    pages: list[dict] = []
    seen: set[str] = set()

    for url in SEEDS.get(tool, ()):
        if url in seen:
            continue
        seen.add(url)
        text = fetch_text(url)
        if text:
            pages.append({"url": url, "title": "(canonical)",
                          "trust": 3, "text": text})

    def harvest(queries, cap: int) -> None:
        for q in queries:
            for hit in search(q, limit=8):
                if len(pages) >= cap:
                    return
                if hit["url"] in seen:
                    continue
                seen.add(hit["url"])
                text = fetch_text(hit["url"])
                if text:
                    pages.append({"url": hit["url"], "title": hit["title"],
                                  "trust": hit["trust"], "text": text})

    # Wave one is deliberately capped below max_pages. Filling the whole
    # budget here meant the quality check below never ran and the second wave
    # never fired -- the corpus was full of reference pages before anything
    # asked whether they were any good.
    harvest((f'{tool} {anchor} walkthrough example',
             f'{tool} {anchor} when to use analyst workflow',
             f'{tool} {anchor} tutorial step by step',
             f'{tool} {anchor} cheat sheet command'),
            cap=max(3, max_pages - 4))

    # Second wave, only when the first found nothing scenario-bearing.
    #
    # Imaging tools showed the problem: dd, dc3dd and foremost all retrieved
    # fine and every passage scored 0-2, because the pages that rank for a
    # tool's name are reference pages -- a Kali tool page states what a flag
    # does and never says when you would reach for it. The fix is not more
    # pages, it is differently-shaped ones, so this wave asks for the genres
    # that narrate an investigation rather than describe a program.
    best = 0
    for pg in pages:
        for sc, _ in passages_using(pg["text"], tool, limit=3):
            best = max(best, sc)
    if best >= 4:
        return pages

    harvest((f'{tool} case study investigation writeup',
             f'how to use {tool} real world example {anchor}',
             f'{tool} lab exercise forensics course',
             f'using {tool} incident response'),
            cap=max_pages)
    return pages


def evidence_for(tool: str, flag: str | None = None,
                 max_pages: int = 10) -> list[dict]:
    """Cited passages showing this tool or flag in use.

    Returns [{url, title, trust, score, passage}], best scenario-bearing text
    first. Never returns a passage without the URL it came from: an uncited
    claim cannot be checked, and uncheckable claims are how the previous loop
    shipped invented flags.
    """
    token = flag if flag else tool
    found: list[dict] = []
    for page in corpus_for(tool, max_pages=max_pages):
        for sc, passage in passages_using(page["text"], token,
                                          near=tool if flag else None):
            found.append({"url": page["url"], "title": page["title"],
                          "trust": page["trust"], "score": sc,
                          "passage": passage})
    # Scenario-bearing text first, then publisher trust. A high-trust synopsis
    # line is still a synopsis line and teaches nothing.
    found.sort(key=lambda f: (-f["score"], -f["trust"]))
    return found


if __name__ == "__main__":
    import sys
    tool = sys.argv[1] if len(sys.argv) > 1 else "fls"
    flag = sys.argv[2] if len(sys.argv) > 2 else None
    ev = evidence_for(tool, flag)
    print(f"{len(ev)} passages from {len({e['url'] for e in ev})} sources\n")
    for e in ev[:6]:
        print(f"[score {e['score']} trust {e['trust']}] {e['url']}")
        print(f"  {e['passage'][:280]}\n")
