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
import html
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


# A shell prompt, anywhere in a line: "$ ", "# ", "PS C:\>" or the full
# "[user@localhost /workdir]$ " form.
# Note the prompt characters: $ and #, and PS...> for PowerShell -- but NOT
# a bare ">". A lone > is a redirect far more often than a prompt, and
# including it split "mactime -b body.txt -d > timeline.csv" at the redirect
# and returned the command twice.
PROMPT = re.compile(r"(?:\[[^\]\n]{1,60}\]\s*)?(?:[a-z0-9_.-]+@[\w.-]+"
                    r"(?::[^\s$#]*)?)?\s*(?:[$#]|PS[^>\n]{0,40}>)\s+")

# An invocation that only asks the tool to describe itself. Real, and it
# teaches a reader nothing they cannot get by running the tool, so it is not
# worth a row -- and the captioner will confidently invent a purpose for it
# ("Identify signatures causing false positives" for `sigtool --help`).
#
# -v is included and lowercase deliberately. It is version on readelf and
# verbose on most other tools, and the pattern does not have to know which:
# a bare `tool -v` with nothing to act on teaches nothing either way. The
# trailing $ is what makes that safe -- `readelf -h /bin/ls` names a file
# and survives, while `readelf -v` alone does not. Captioned "Display notes
# from binary file", which is neither of the things -v does.
SELF = re.compile(r"^\S+\s+(?:-h|-v|-\?|-V|--help|--version|--usage)\s*$")

# Where a command stops when a page has run it together with its output.
# The output of the tools this guide covers is overwhelmingly of a shape
# arguments never take: a comma-and-colon record, a table rule, a second
# prompt, or the tool announcing itself again.
END = re.compile(r"\s{2,}|\S+,\d[\d.]*--|\|{2,}|[-=]{4,}"
                 r"|\[[^\]\n]{1,60}\]\s*[$#]")


def split_prompts(line: str, tool: str) -> list[str]:
    """Commands buried mid-line after a shell prompt.

    Pages converted from HTML routinely arrive with a whole session on one
    line: "[user@localhost /workdir]$ ssdeep -l config.h INSTALL ...". Only
    looking at the start of a line found nothing on those pages, which is
    why ssdeep, dd, md5sum, sha256sum and rahash2 all came back with zero
    invocations while their documentation was full of them.
    """
    out = []
    for seg in PROMPT.split(line):
        if not seg:
            continue
        seg = seg.strip()
        if not re.match(re.escape(tool) + r"(?:\.\w+)?\s", seg):
            continue
        # Cut at the first thing that reads as output rather than argument.
        out.append(END.split(seg)[0].strip())
    return out


# A usage synopsis, which names the tool and lists what it accepts and is
# not a command anyone runs:
#   foremost [-v|-V|-h|-T|-Q|-q|-a|-w-d] [-t <type>] [-s <blocks>]
#   clamscan [options] [file/directory/-]
SYNOPSIS = re.compile(r"\[[^\]]*\|[^\]]*\]|\[opt(?:ion)?s?\]|\[file/|\.{3}\]"
                      # Deliberately NOT matching a bare <placeholder>. A
                      # synopsis is given away by its bracketed options, and
                      # `ewfmount image.E01 <folder>` is a real command that
                      # names one argument generically -- the same thing this
                      # guide does with {{path/to/image.dd}}.
                      r"|\[-\w\|"
                      # A man page's optional-suffix notation: -h[elp],
                      # -s[eek]. Real in a manual, not runnable.
                      r"|-\w\[[a-z]+\]", re.I)

# A man page's placeholder operands, which read as arguments but are not:
#   xxd -s +seek        xxd -s seek ,
PLACEHOLDER = re.compile(r"(?<![\w-])[+]?(?:seek|offset|len|infile|outfile|"
                         r"cols|groupsize|file|dir|path|name|addr|size)"
                         r"\s*,?\s*$", re.I)

# A page title that happens to lead with the tool name:
#   olevba · decalage2/oletools Wiki · GitHub
#
# Middot only. Including " | " here caught `icat -o 2048 "$EVIDENCE" 12345 |
# md5sum` -- a shell pipe, not a title separator. Pipe-separated headings are
# already handled by the table-row rule below, which requires capitalised
# words after the bar.
TITLE = re.compile(r"\s·\s")


def _expand(flag: str) -> set[str]:
    """A flag token as the set of options it actually uses.

    Two forms the captured help text never lists literally:
    clustered short flags, where `-Fk` is `-F` and `-k`, and long flags
    carrying a value, where `--find="x"` is `--find`. Comparing the raw token
    dropped `tcpflow -a -o outdir -Fk -r packets.pcap` and `ngrep -tD ns3`,
    both of which are real.
    """
    flag = flag.split("=")[0]
    if flag.startswith("--") or len(flag) <= 2:
        return {flag}
    return {flag} | {"-" + c for c in flag[1:]}


def candidate_lines(text: str, tool: str,
                    real_flags: set[str] | None = None) -> list[str]:
    """Lines from this page that are invocations of the tool.

    real_flags, when given, is the set of options captured from the actual
    binary's help output. A command using anything else is dropped however
    real the page it came from looked -- `clamscan --memory` was extracted
    from a live page and clamscan has no --memory. Extraction guarantees
    somebody wrote the line down; it guarantees nothing about whether it
    runs, and this guide gets pasted into terminals.
    """
    out = []
    lines = []
    for ln in text.splitlines():
        lines.append(ln)
        # A line carrying a shell prompt can hold one or several commands;
        # pull each out and judge it on its own like any other candidate.
        #
        # No length condition. The first version required the line to be over
        # 120 characters, on the assumption that this only happened when a
        # whole session had been collapsed onto one line. The ssdeep page
        # puts "[user@localhost /workdir]$ ssdeep -l config.h INSTALL
        # m4/libtool.m4" on a line of 69, so the guard blocked exactly the
        # case it was written for and the extractor still reported zero.
        if PROMPT.search(ln):
            lines.extend(split_prompts(html.unescape(ln), tool))
    for raw in lines:
        # Pages are fetched as HTML-derived text and quoting survives as
        # entities. A command copied with &quot; in it does not run.
        #
        # html.unescape rather than a hand-written table: the table handled
        # &quot; and &lt; and missed the hex form, so `ewfmount image.E01
        # &#x3C;folder>` was extracted with the entity still in it.
        line = html.unescape(raw).replace("\xa0", " ")
        # Markup that survived the text extraction, dragging the tail of a
        # copy-to-clipboard button along with the command.
        line = re.split(r'"\s+(?:title|class|aria-\w+|data-\w+)=', line)[0]
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

        # The tool's own OUTPUT, which begins with its name and therefore
        # looks exactly like an invocation.
        #
        #   dc3dd 7.2.646 started at 2018-12-01 13:37:20 -0500
        #   affcat version 3.7.22
        #
        # Both were extracted and then captioned with confident nonsense --
        # "Create forensic image of log file and verify integrity" for a
        # startup banner. That is the precise failure this project exists to
        # prevent: an authoritative-looking line a reader pastes into a
        # terminal. Caught by reading the generated output, not by any check.
        if re.match(re.escape(tool) + r"\s+(?:v(?:ersion)?\s*)?\d+[\d.]*\b",
                    line, re.I):
            continue
        if re.search(r"\b(?:started at|version)\s+\d", line, re.I):
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
        # The tool's name repeated by a split that ran the heading into the
        # command: "evtxexport evtxexport -p c/ ...". Running it would try to
        # open the tool's own name as a file.
        line = re.sub(r"^(" + re.escape(tool) + r")\s+\1(?=\s)", r"\1", line)

        # Prose glued onto the end of a command by the text extraction:
        #   rasm2 -a x86 -b 32 'mov eax, 33' Disassemble opcode:
        # The colon after a capitalised word is the giveaway -- it is the
        # heading of the next example, not part of this one.
        line = re.sub(r"\s+[A-Z][a-z]+(?:\s+\w+){0,3}\s*:\s*$", "", line)
        # A man page's own section headings, run into the command by the text
        # extraction: "rasm2 -d 90 See Also radare2(1) Authors pancake
        # <pancake@nopcode.org> Referenced By ...". Everything from the
        # heading onward belongs to the page, not to the command.
        line = re.split(r"\s+(?:See Also|Referenced By|Authors?|Copyright|"
                        r"Reporting Bugs|Description|Synopsis|Options|"
                        r"Examples?|Colophon|This page is part of)\b",
                        line)[0].strip()
        # A shebang is never part of a command line. It appears because the
        # extraction ran a heading and the script beneath it into the command
        # above: `ffind -o 2048 "$EVIDENCE" 12345 Scripting a Complete
        # Analysis #!/bin/bash`.
        line = re.split(r"\s+#!", line)[0].strip()
        # ...and the heading itself, which is the giveaway pattern of two
        # capitalised words with at most a couple of small words between.
        # Command arguments are paths, values and flags, not title case.
        line = re.split(r"\s+[A-Z][a-z]+(?:\s+[a-z]{1,4})*\s+[A-Z][a-z]+",
                        line)[0].strip()
        # ...and shell noise the same extraction dragged along:
        #   rahash2 -S 12333 -E ror -s hello && echo Cell{
        line = re.split(r"\s+&&\s+echo\s", line)[0].strip()

        # The trims above can cut a line back to the bare tool name, which
        # the earlier length check has already passed. Re-check here rather
        # than let split() raise on a one-token line.
        if len(line.split()) < 2:
            continue

        # "msodde : to detect and extract DDE/DDEAUTO links from MS Office
        # documents, RTF and CSV" -- a tool listing, where the colon
        # separates the name from its description. A colon straight after
        # the tool name is never an argument.
        if re.match(re.escape(tool) + r"(?:\.\w+)?\s*:", line):
            continue

        if SELF.match(line) or SYNOPSIS.search(line) or TITLE.search(line):
            continue
        if PLACEHOLDER.search(line):
            continue
        # Two or more bracketed groups is a synopsis listing what the tool
        # accepts: `xortool [-x] [-m MAX-LEN] [-f] [-t CHARSET] [FILE]`.
        #
        # The all-placeholder rule misses this one because the groups split
        # across whitespace -- "[-m" and "MAX-LEN]" are separate tokens and
        # neither is a bracketed word. Counting the groups sees it whole. A
        # real invocation carries at most one bracketed optional argument.
        if len(re.findall(r"\[[^\]\n]{0,40}\]", line)) >= 2:
            continue
        # A trailing shell comment, which cheat sheets use to caption their
        # own examples: `hashcat -m 100 hashes.txt wordlist.txt #SHA1`. The
        # caption is generated separately, so the comment is noise here --
        # and it would be pasted into a terminal along with the command.
        #
        # Any whitespace-preceded # starts a shell comment. The first draft
        # required a non-space or a capital after it and so kept
        # `EvtxECmd.exe --sync # update 700+ community maps first`. Nothing
        # is lost by being general: a # inside an argument, as in
        # Project#1542292355.pdf, has no space before it.
        line = re.split(r"\s+#", line)[0].strip()
        # Every operand a placeholder means this is a synopsis, whatever
        # bracket style it uses: `olemeta <file>`, `hydra [ options ]
        # <target> <service>`.
        #
        # Note the difference from `ewfmount image.E01 <folder>`, which is
        # kept: that names a real file and generalises ONE argument, the way
        # this guide does with {{path/to/image.dd}}. What marks a synopsis is
        # that nothing in it is concrete.
        operands = [w for w in line.split()[1:] if not w.startswith("-")]
        # The lone-bracket alternatives matter: a spaced synopsis like
        # "hydra [ options ] <target>" tokenises to [ , options , ] and
        # none of those is a bracketed word on its own.
        if operands and all(re.fullmatch(r"[<\[].*[>\]]|\||options?|[\[\]<>]",
                                         w, re.I) for w in operands):
            continue
        # An unbalanced brace or bracket means the line was cut out of
        # something larger and is not a command on its own.
        if line.count("{") != line.count("}") or line.count("[") != line.count("]"):
            continue
        # A prose parenthetical standing in for arguments -- "mergecap -F
        # (different options)" is a sentence about the flag, not a command.
        if re.search(r"\((?:[a-z]+\s+){1,4}[a-z]+\)", line):
            continue
        # In a shell pipe the right-hand side is another command, so it
        # starts with a lowercase program name. A title reads
        # "md5sum Linux Command (10 Examples) | phoenixNAP KB", where what
        # follows the bar is a proper noun and the line is a page heading.
        if " | " in line:
            after = line.split(" | ", 1)[1].lstrip()
            # Testing only that the first token was lowercase was not enough:
            # "md5sum Linux Command (10 Examples) | phoenixNAP KB" begins its
            # right-hand side with a lowercase letter. The giveaway is the
            # capitalised word after it -- a program's arguments are rarely
            # proper nouns, and a page title is made of them.
            if (not re.match(r"[a-z][\w.-]*(?:\s|$)", after)
                    or any(w[:1].isupper() for w in after.split())):
                continue
        # An operand with nothing after it: `dd if=/dev/`, `dd if=/dev/zero
        # of=/dev/`. These came out of pages where the device name was markup
        # that the text extraction dropped, and they were captioned
        # "Securely erase drive data" and "Wipe drive data with zeros". Half
        # a dd wipe command under a confident destructive caption is the
        # worst thing this guide could print, so an operand must have a
        # value and the value must not end at a path separator.
        if (re.search(r"\b\w+=\s*(?:$|\s)", line)
                # A bare /dev/ with no device after it, anywhere in the line
                # -- `dd if=img.dd of=/dev/ conv=notrunc` slipped through a
                # rule that only looked at the end of the line.
                or re.search(r"=/dev/(?=\s|$)", line)
                or re.search(r"=\S*/\s*$", line)):
            continue
        # Spacing mangled by the same extraction: `dd if = /dev /sda2`.
        if re.search(r"\b\w+\s+=\s|\s=\s+\S", line):
            continue
        # A line continuation means the command is cut off here. Publishing
        # half of it is worse than publishing none: it looks complete.
        #
        # The space before the backslash matters. Testing for a trailing
        # backslash alone dropped `clamscan.exe --recursive C:\`, where the
        # backslash is a Windows drive root and the command is whole.
        if re.search(r"\s\\$", line.rstrip() + ""):
            continue
        # Every flag the command uses must exist on the real binary.
        if real_flags:
            # Only the part before a pipe: "icat -o 2048 img 12 | md5sum"
            # runs a second program whose flags are not this tool's.
            head = line.split("|")[0]
            used = re.findall(r"(?<![\w-])(-{1,2}[A-Za-z][\w-]*)", head)
            if any(not (_expand(f) & real_flags) for f in used):
                continue
        # Smart quotes come from prose-formatted pages and do not run in a
        # shell: tshark -R “!arp && !bootp” was extracted verbatim.
        if re.search(r"[‘’“”]", line):
            continue
        rest = line.split(None, 1)[1]
        if PROSE.search(rest) or not SUBSTANCE.search(rest):
            continue
        if line not in out:          # a line and its prompt-split twin
            out.append(line)
    return out


def invocations_for(tool: str, limit: int = 8,
                    real_flags: set[str] | None = None) -> list[dict]:
    """Distinct real invocations, commonest shape first, each with a source."""
    seen: dict[str, dict] = {}
    for page in sources.corpus_for(tool):
        for line in candidate_lines(page.get("text") or "", tool, real_flags):
            key = re.sub(r"\s+", " ", line)
            rec = seen.get(key)
            if rec:
                rec["count"] += 1
                continue
            seen[key] = {"command": key, "count": 1, "url": page.get("url", ""),
                         "flags": sorted(set(re.findall(r"(?<![\w-])(-{1,2}[A-Za-z][\w-]*)", key)))}
    ranked = sorted(seen.values(), key=lambda r: (-r["count"], len(r["command"])))

    # One row per command SHAPE, not per command.
    #
    # `file` returned six invocations -- file app.py, file run.sh, file
    # data.zip, file /bin/bash, file photo.jpg, file image.png -- every one
    # of them real, every one captioned "identify file type", and together
    # they teach exactly what the first one teaches. Six rows of padding on
    # a page whose whole value is being short.
    #
    # Shape is the tool plus the set of flags it uses plus how many operands
    # follow. Different flags mean a different lesson and survive; different
    # filenames do not.
    out, shapes = [], set()
    for rec in ranked:
        parts = rec["command"].split()
        flags = frozenset(f.split("=")[0] for f in parts[1:] if f.startswith("-"))
        operands = sum(1 for p in parts[1:] if not p.startswith("-"))
        shape = (flags, min(operands, 3))
        if shape in shapes:
            continue
        shapes.add(shape)
        out.append(rec)
        if len(out) >= limit:
            break
    return out


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
