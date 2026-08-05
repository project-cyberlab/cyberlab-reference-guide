#!/usr/bin/env python3
"""Real command lines for a tool, lifted from the retrieved corpus.

153 of 155 reference pages have no worked examples. fls.md has eight and was
written by hand as the exemplar; nothing else followed it. An options table
tells a reader what -r means and still leaves them unable to type the
command, which is the gap this closes.

The commands are EXTRACTED, never composed. A plausible invented command line
is the most dangerous thing this project could ship -- it looks authoritative,
it is quoted verbatim into a terminal, and the previous project shipped 44
modules of exactly that. So every line here appeared, character for character,
in a page someone wrote about the tool, and the citation records where.

What is generated is only the one-line explanation of why you would run it,
and that goes through the same gate as every other note.

    python scripts/invocations.py fls
    python scripts/invocations.py --audit
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import sources  # noqa: E402

# A shell prompt or list marker people put before a command.
LEAD = re.compile(r"^(?:\$|#|>|PS[^>]*>|\d+\.|[-*])\s+")

# Things that look like a command line but are not one to copy.
NOISE = re.compile(
    r"(sudo\s+)?(apt|apt-get|yum|dnf|pip|pip3|brew|choco|git)\s+(install|clone)"
    r"|^\s*(cd|ls|man|which|echo|export)\s"
    r"|https?://", re.I)


# Words that do not appear in a command line but are everywhere in a
# sentence. "icat extracts file contents by inode; useful when filenames are
# gone" begins with the tool name and is not a command, and a reference guide
# that prints it as one is telling the reader to type English at a shell.
PROSE = re.compile(r"(?<![\w-])(the|is|are|was|when|which|that|useful|used|"
                   r"parses|extracts|allows|this|for example|you can)"
                   r"(?![\w-])", re.I)

# A command line has to actually do something: carry a flag, name a file,
# take a path, or redirect. Without one of these it is a heading or a table
# cell that happens to start with the tool's name.
SUBSTANCE = re.compile(r"(?<![\w-])-{1,2}[A-Za-z]|[<>]|\|\s*\w+\s|/\S+"
                       r"|\S+\.[A-Za-z0-9]{2,4}(?:\s|$)|\{\{")


def candidate_lines(text: str, tool: str) -> list[str]:
    """Lines from this page that are invocations of the tool."""
    out = []
    for raw in text.splitlines():
        # Pages are fetched as HTML-derived text and quoting survives as
        # entities. A command copied with &quot; in it does not run.
        line = (raw.replace("&quot;", '"').replace("&#39;", "'")
                   .replace("&amp;", "&").replace("&lt;", "<")
                   .replace("&gt;", ">").replace("&#8212;", "--")
                   .replace("&nbsp;", " "))
        line = LEAD.sub("", line.strip())
        if not line or len(line) > 160:
            continue
        # Must START with the tool (optionally via python/perl or a path), so
        # prose that merely names it is excluded. "Using fls to list files" is
        # not a command, and treating it as one is how a reference guide ends
        # up telling someone to type an English sentence.
        if not re.match(r"^(?:python[23]?\s+|perl\s+|\./|/\S*/)?"
                        + re.escape(tool) + r"(?:\.py|\.pl|\.exe)?(?:\s|$)",
                        line):
            continue
        if NOISE.search(line):
            continue
        # A bare "fls" with no arguments teaches nothing.
        if len(line.split()) < 2:
            continue
        # Pages often append an explanation to the command with a dash or an
        # arrow. Keep the command, drop the gloss.
        line = re.split(r"\s+(?:→|—|–|<-|=>)\s+", line)[0].strip()

        # A shell prompt spliced into a heading: "tcpflow TCP flow recorder
        # root@kali:~# tcpflow -h". The prompt is the giveaway.
        if re.search(r"\S+@\S+:~?[^\s]*[#$]", line):
            continue
        # A table row: "tcpflow | Kali Linux Tools".
        if re.search(r"\|\s*[A-Z][a-z]+(\s+[A-Z][a-z]+)+\s*$", line):
            continue
        # A sentence: ends on a word and a full stop, and carries no flag.
        #
        # Counting three alphabetic words before the stop was not enough --
        # "tcpflow does not understand 802.11 headers." breaks the run with a
        # version number and slipped through. Real invocations end on a
        # filename, a value or an argument, and a line with no flag at all
        # that finishes with a word and a full stop is prose.
        if re.search(r"[A-Za-z]{3,}\.$", line) and not re.search(
                r"(?<![\w-])-{1,2}[A-Za-z]", line):
            continue

        if len(line.split()) < 2:
            continue
        rest = line.split(None, 1)[1]
        if PROSE.search(rest) or not SUBSTANCE.search(rest):
            continue
        out.append(line)
    return out


def invocations_for(tool: str, limit: int = 8) -> list[dict]:
    """Distinct real invocations, commonest shape first, each with a source."""
    seen: dict[str, dict] = {}
    for page in sources.corpus_for(tool):
        for line in candidate_lines(page.get("text") or "", tool):
            key = re.sub(r"\s+", " ", line)
            rec = seen.get(key)
            if rec:
                rec["count"] += 1
                continue
            seen[key] = {"command": key, "count": 1, "url": page.get("url", ""),
                         "flags": sorted(set(re.findall(r"(?<![\w-])(-{1,2}[A-Za-z][\w-]*)", key)))}
    ranked = sorted(seen.values(), key=lambda r: (-r["count"], len(r["command"])))
    return ranked[:limit]


def main() -> int:
    if "--audit" in sys.argv:
        from page_gaps import audit
        gaps = [r for r in audit() if not r["examples"] and not r["gui"]]
        print(f"{len(gaps)} CLI pages with no worked example")
        for r in gaps[:20]:
            print(f"  {r['page']}")
        return 0
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    tool = sys.argv[1]
    found = invocations_for(tool)
    print(f"{len(found)} real invocations for {tool}\n")
    for r in found:
        print(f"  {r['command']}")
        print(f"      seen {r['count']}x  flags={' '.join(r['flags']) or '-'}")
        print(f"      {r['url'][:88]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
