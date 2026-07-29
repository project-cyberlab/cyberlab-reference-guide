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
# An argument attached to the flag: =VAL  <VAL>  [VAL]  VAL
ARG = r"(?:[=\s](?:<[^>]{1,40}>|\[[^\]]{1,40}\]|\{[^}]{1,40}\}|[A-Za-z][A-Za-z0-9_.-]{0,30}))"

# Whole-line option definition: leading space, flag(s), optional arg, then
# either two+ spaces before the description or end of line.
# Two shapes are common and both must match:
#   "  -o, --output FILE    write here"   (comma-separated, 2+ space gap)
#   "\t-d: Display deleted entries only"  (colon separator, single space) -- TSK
OPT_LINE = re.compile(
    rf"^(?P<indent>\s*)(?P<flags>{FLAG}(?:{ARG})?(?:\s*,\s*{FLAG}(?:{ARG})?)*)"
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
    for part in re.split(r"\s*,\s*", blob.strip()):
        part = part.strip()
        if not part:
            continue
        m = re.match(rf"^({FLAG})(?:[=\s]+(.+))?$", part)
        if not m:
            continue
        flag, arg = m.group(1), (m.group(2) or "").strip()
        arg = arg.strip("<>[]{}").strip()
        if arg.lower() in ("", "n/a"):
            arg = ""
        out.append((flag, arg))
    if not out:
        return []
    # An argument written once after a group applies to the group's last flag;
    # propagate it so `-o, --output FILE` records FILE for both.
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
        if len(s) < 12 or len(s) > 200:
            continue
        if s.lower().startswith(cmd.lower()) and len(s.split()) < 4:
            continue
        return s
    return ""
