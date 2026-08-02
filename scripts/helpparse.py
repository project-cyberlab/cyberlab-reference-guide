#!/usr/bin/env python3
"""Parse captured --help text into a structured option list.

Deliberately conservative. A flag is only emitted when the line really looks
like an option definition, because a false option is exactly the failure this
project exists to prevent. When in doubt, drop it -- the linter will surface
the shortfall as missing coverage rather than let an invention through.
"""
from __future__ import annotations
import re

# A flag token: -v  --verbose  --long-opt  -X  /F (windows-style)
FLAG = r"(?:--[A-Za-z0-9][A-Za-z0-9_-]*|-[A-Za-z0-9?#@]|/[A-Za-z0-9?]+)"
# A simple value token, used for the space-separated form (-o FILE). Kept tight:
# after a space, anything looser starts eating description words.
VAL = r"(?:<[^>]{1,40}>|\[[^\]]{1,40}\]|\{[^}]{1,40}\}|[A-Za-z][A-Za-z0-9_.-]{0,30})"
# An argument attached to the flag. Real help text is messier than "=VAL":
#   --incremental[=MODE]     optional value, the bracket comes *before* the '='
#   --groups=[-]GID[,..]     bracketed and punctuated value after '='
#   --node=MIN[-MAX]/TOTAL   slashes and dashes inside the value
# An '=' makes the binding unambiguous, so everything up to whitespace can be
# taken; after a bare space we stay conservative and only accept VAL.
# "-E<fieldsoption>=<value>" binds its argument with no separator at all.
ATTACHED = r"(?:<[^>]{1,40}>(?:=<[^>]{1,40}>)?)"
# A trailing "..." (repeatable option) must not defeat the gap match:
#   "-a <autostop cond.> ..., --autostop <autostop cond.> ..."
# "={VAL}" must be tried before "=\S+": a bracketed value may contain spaces
# ("--script=<Lua scripts>"), and the non-space form would stop at "=<Lua".
ARG = rf"(?:\[=[^\]]{{0,40}}\]|{ATTACHED}|={VAL}|=\S{{1,40}}|\s{VAL})(?:\s*\.\.\.)?"
# Aliases are also written slash-joined, sometimes with the "--" left off the
# later members: "--scan-delay/--max-scan-delay", "--min-rtt-timeout/max-rtt-timeout".
# The suffix is matched so the line parses at all; _split_flags then keeps only
# the members that carry their own prefix, because expanding "max-rtt-timeout"
# into "--max-rtt-timeout" would be an inference, and inferred flags are exactly
# what this parser exists to prevent.
ALT = r"(?:/[A-Za-z0-9][A-Za-z0-9_-]*)*"

# Whole-line option definition: leading space, flag(s), optional arg, then
# either two+ spaces before the description or end of line.
# Two shapes are common and both must match:
#   "  -o, --output FILE    write here"   (comma-separated, 2+ space gap)
#   "\t-d: Display deleted entries only"  (colon separator, single space) -- TSK
#   "--wordlist=FILE --stdin    wordlist mode"  (space-separated, no comma)
# The space-separated alternative is restricted to *long* flags: a short flag
# after a single space is far more likely to be prose ("-1 to disable") than a
# second option, and inventing an option is the one failure that matters here.
LONG = r"--[A-Za-z0-9][A-Za-z0-9_-]*"
OPT_LINE = re.compile(
    rf"^(?P<indent>\s*)(?P<flags>{FLAG}{ALT}(?:{ARG})?"
    rf"(?:\s*[,;]\s*{FLAG}{ALT}(?:{ARG})?|\s+{LONG}{ALT}(?:{ARG})?)*)"
    rf"(?P<gap>\s*:\s+|\s{{2,}}|\s*$)(?P<desc>.*)$"
)

# A description that actually begins with an alias flag, e.g. clamscan's
# "    --help                -h             Show this help". The alias must be
# followed by a real gap, otherwise "-1 to disable" would be misread.
ALIAS_PREFIX = re.compile(rf"^(?P<alias>{FLAG})(?:\s{{2,}})(?P<rest>\S.*)$")

SECTION_STOP = re.compile(
    r"^\s*(examples?|usage|synopsis|description|notes?|see also|author|report|"
    r"copyright|environment|files|exit status|commands?|subcommands?)\s*:?\s*$", re.I)


def _split_flags(blob: str) -> list[tuple[str, str]]:
    """'-o, --output FILE' -> [('-o',''), ('--output','FILE')] (arg on last)."""
    out: list[tuple[str, str]] = []
    # Split on commas *or* whitespace that precedes another flag, so
    # "--wordlist=FILE --stdin" yields both options rather than being dropped.
    # The separator must be followed by a flag: a comma inside a value, as in
    # "--groups=[-]GID[,..]", is part of the value and must not split it.
    for part in re.split(rf"\s*[,;]\s*(?={FLAG})|\s+(?={FLAG})|/(?=-)", blob.strip()):
        part = part.strip().rstrip(".").strip()
        if not part:
            continue
        # Drop a bare slash-suffix ("max-rtt-timeout"): it names a real option
        # but only by implication, and implied flags are not evidence. Guard the
        # leading slash first -- "/F" is itself a flag, and splitting it here
        # would delete every Windows-style option.
        if not part.startswith("/"):
            part = part.split("/")[0]
        m = re.match(rf"^({FLAG})(?:(\[=[^\]]*\])|({ATTACHED})|[=\s]+(.+))?$", part)
        if not m:
            continue
        flag = m.group(1)
        # "--incremental[=MODE]" -> the value is MODE and it is optional.
        arg = (m.group(2) or m.group(3) or m.group(4) or "").strip()
        if arg.startswith("[=") and arg.endswith("]"):
            arg = arg[2:-1].strip() + " (optional)" if arg[2:-1].strip() else ""
        arg = arg.strip("<>{}").strip()
        if arg.startswith("[") and arg.endswith("]") and "[" not in arg[1:-1]:
            arg = arg[1:-1].strip()
        # An argument is a placeholder name, not a sentence fragment. These all
        # shipped: "autostop cond." and "ringbuffer opt." carried the trailing
        # period of an abbreviation, "[!]list" kept an unbalanced bracket, and
        # rahash2 -t recorded the word "to" from its description.
        arg = arg.rstrip(".,;:")
        if arg.count("[") != arg.count("]"):
            arg = arg.replace("[", "").replace("]", "")
        if arg.lower() in ("the", "a", "an", "of", "to", "and", "or", "is",
                           "for", "with", "in", "on"):
            arg = ""
        if arg.lower() in ("", "n/a"):
            arg = ""
        out.append((flag, arg))
    if not out:
        return []
    # An argument written once after a comma-separated group applies to the
    # whole group, so `-o, --output FILE` records FILE for both -- they are
    # aliases for one option. Space-separated flags are *different* options
    # ("--wordlist=FILE --stdin"), so the argument must not be propagated or
    # --stdin acquires an argument it does not take.
    if "," in blob:
        arg = next((a for _, a in reversed(out) if a), "")
        if arg:
            out = [(f, arg) for f, _ in out]
    return out


def parse_options(help_text: str) -> list[dict]:
    """Return [{flag, arg, desc}] found in the help text, order preserved."""
    lines = help_text.splitlines()
    found: dict[str, dict] = {}
    order: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("#"):          # our capture header
            i += 1
            continue
        m = OPT_LINE.match(line)
        if not m:
            i += 1
            continue
        flags = _split_flags(m.group("flags"))
        if not flags:
            i += 1
            continue
        desc = (m.group("desc") or "").strip()
        base_indent = len(m.group("indent"))

        # Pull an alias flag out of the description into the flag group.
        am = ALIAS_PREFIX.match(desc)
        if am:
            extra = _split_flags(am.group("alias"))
            if extra:
                flags = flags + extra
                desc = am.group("rest").strip()

        # Continuation: more-indented, non-option lines belong to this option.
        j = i + 1
        while j < len(lines):
            nxt = lines[j]
            if not nxt.strip():
                break
            if SECTION_STOP.match(nxt):
                break
            nxt_indent = len(nxt) - len(nxt.lstrip())
            if nxt_indent <= base_indent:
                break
            if OPT_LINE.match(nxt) and re.match(rf"^\s*{FLAG}", nxt):
                break
            desc = (desc + " " + nxt.strip()).strip()
            j += 1
        i = j if j > i + 1 else i + 1

        for flag, arg in flags:
            if flag in found:
                if not found[flag]["desc"] and desc:
                    found[flag]["desc"] = desc
                continue
            found[flag] = {"flag": flag, "arg": arg, "desc": desc}
            order.append(flag)

    return [found[f] for f in order]


def parse_synopsis(help_text: str) -> str:
    """Pull the usage/synopsis line(s) verbatim."""
    lines = help_text.splitlines()
    out: list[str] = []
    for idx, line in enumerate(lines):
        if re.match(r"^\s*(usage|Usage|USAGE|SYNOPSIS)\b", line):
            first = re.sub(r"^\s*(usage|Usage|USAGE|SYNOPSIS)\s*:?\s*", "", line).strip()
            if first:
                out.append(first)
            for nxt in lines[idx + 1:]:
                if not nxt.strip():
                    break
                if OPT_LINE.match(nxt) and re.match(rf"^\s*{FLAG}", nxt):
                    break
                if len(nxt) - len(nxt.lstrip()) < 2 and out:
                    break
                out.append(nxt.strip())
                if len(out) >= 6:
                    break
            break
    return "\n".join(out).strip()


def parse_purpose(help_text: str, cmd: str) -> str:
    """Best-effort one-line description from the help body."""
    for line in help_text.splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        if re.match(r"^(usage|Usage|USAGE|SYNOPSIS)\b", s):
            continue
        if OPT_LINE.match(line) and re.match(rf"^\s*{FLAG}", line):
            continue
        # Synopsis continuation lines ("[-e EXTEND] [-p PLUGIN_DIRS]") are not a
        # description, nor are runtime banners the tool prints before its help.
        if s.startswith(("[", "-", "/", "|", "{")):
            continue
        if re.match(r"^(Running as user|INFO\b|WARNING\b|Volatility \d)", s):
            continue
        # Tools that have no --help emit an error first; that is not a purpose.
        # e.g. "fls: invalid option -- '-'", "Missing image name".
        if re.match(r"^\S+:\s*(invalid|unknown|illegal|unrecognized)\s+option", s, re.I):
            continue
        if re.match(r"^(Missing|Error|error|Cannot|Unknown option)\b", s):
            continue
        # A tool that rejects --help announces the rejection, and the shapes it
        # uses are many. "Invalid argument: bdeinfo" reached the Purpose line of
        # four pages because the pattern above only matches "<cmd>: invalid
        # option". Anything that reads as a complaint is not a description.
        if re.match(r"^(invalid|unrecognized|unknown|illegal|unsupported)\b", s, re.I):
            continue
        if re.search(r"\b(invalid|unrecognized) (argument|option|parameter|value)\b", s, re.I):
            continue
        if re.search(r"(no such file|failed to open|not a valid|permission denied|"
                     r"command not found|try '.*--help')", s, re.I):
            continue
        # "usage: fls [-adDFlhpruvV] ..." is a synopsis, not a purpose.
        if re.match(rf"^{re.escape(cmd)}\b.*\[-", s):
            continue
        # A banner is not a purpose. These all reached the Purpose line of a
        # published page: "hashcat (v6.2.6) starting in help mode",
        # "Nping 0.7.93 ( https://nmap.org/nping )", "Rip v.3.0 - CLI RegRipper
        # tool", "Hayabusa v3.9.0 - Showa Day Release".
        if re.match(rf"^{re.escape(cmd)}\b[^.]*\bv?\d+\.\d+", s, re.I):
            continue
        if re.search(r"\bstarting in \w+ mode\b", s, re.I):
            continue
        if re.match(r"^\S+\s+v?\.?\d+\.\d+(\.\d+)?\s*[-(]", s):
            continue
        # A bare field label such as "Description:" or "Standard commands",
        # and continuation fragments such as "(may be repeated)" or
        # "or:  dd OPTION", are structure from the help text, not prose.
        if re.match(r"^[A-Z][a-z]+( [a-z]+)?:?\s*$", s):
            continue
        if s.startswith(("(", "or:", "See ", "Please")):
            continue
        # A URL on its own line is a homepage, not a description.
        if re.match(r"^\(?https?://", s):
            continue
        if len(s) < 12 or len(s) > 200:
            continue
        if s.lower().startswith(cmd.lower()) and len(s.split()) < 4:
            continue
        return s
    return ""
