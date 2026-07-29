#!/usr/bin/env python3
"""Mine the cyberlab training lab for candidate command invocations.

cyberlab is READ-ONLY input. It is on hold and this script never writes to it.

What we take: real invocations someone already thought through, which is the
expensive part of writing "Common invocations". What we explicitly do NOT take:
authority. The content-quality audit found fabricated CLI flags across ~44 of
61 modules, so every mined invocation is a CANDIDATE that must still survive
the linter against a real capture.
"""
from __future__ import annotations
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MINED = ROOT / ".mined"
sys.path.insert(0, str(Path(__file__).resolve().parent))
from taxonomy import all_mapped_commands  # noqa: E402

TOOLS = all_mapped_commands()
COV = json.loads((ROOT / "capture" / "coverage.json").read_text(encoding="utf-8"))
DOCUMENTED = set(COV["documented"])

FENCE = re.compile(r"```[a-zA-Z0-9]*\n(.*?)```", re.S)
PROMPT = re.compile(r"^\s*(?:\$|#|PS[^>]*>)\s*")
CONT = re.compile(r"\\\s*$")


def clean(line: str) -> str:
    line = PROMPT.sub("", line.rstrip())
    return line.strip()


def first_token(cmd: str) -> str:
    # Strip env-var prefixes: FOO=bar tool ...
    parts = cmd.split()
    i = 0
    while i < len(parts) and re.fullmatch(r"[A-Z_][A-Z0-9_]*=.*", parts[i]):
        i += 1
    if i >= len(parts):
        return ""
    tok = parts[i]
    if tok in ("sudo", "time", "timeout", "nohup"):
        # take the next real token
        for t in parts[i + 1:]:
            if not t.startswith("-") and not re.fullmatch(r"\d+[smh]?", t):
                return Path(t).name
        return ""
    return Path(tok).name


def main() -> None:
    if not MINED.exists():
        print("no .mined/ — pull cyberlab first", file=sys.stderr)
        return

    per_tool: dict[str, list[dict]] = defaultdict(list)
    seen: set[tuple[str, str]] = set()
    n_files = n_blocks = n_cmds = 0

    for readme in sorted(MINED.rglob("README.md")):
        module = readme.parent.name
        if not re.match(r"^\d{2}-", module):
            continue
        n_files += 1
        text = readme.read_text(encoding="utf-8", errors="replace")
        for block in FENCE.findall(text):
            n_blocks += 1
            # join backslash continuations
            joined, buf = [], ""
            for raw in block.splitlines():
                line = clean(raw)
                if not line or line.startswith("#"):
                    continue
                if CONT.search(line):
                    buf += CONT.sub(" ", line)
                    continue
                joined.append((buf + line).strip())
                buf = ""
            if buf:
                joined.append(buf.strip())

            for cmd in joined:
                tool = first_token(cmd)
                if not tool or tool not in TOOLS:
                    continue
                # collapse whitespace so near-duplicates dedupe
                norm = re.sub(r"\s+", " ", cmd)
                key = (tool, norm)
                if key in seen:
                    continue
                seen.add(key)
                n_cmds += 1
                per_tool[tool].append({"cmd": norm, "module": module})

    out = {
        "note": "CANDIDATES ONLY — mined from cyberlab, never authoritative. "
                "Every flag must still be verified against capture/.",
        "source": "cyberlab-training-lab @ audit/content-quality-p0-p1",
        "tools": {k: v for k, v in sorted(per_tool.items())},
    }
    (ROOT / "capture" / "cyberlab-candidates.json").write_text(
        json.dumps(out, indent=2), encoding="utf-8")

    have_capture = [t for t in per_tool if t in DOCUMENTED]
    print(f"modules={n_files} blocks={n_blocks} invocations={n_cmds} "
          f"tools={len(per_tool)} (of which {len(have_capture)} also have a capture)")
    top = sorted(per_tool.items(), key=lambda kv: -len(kv[1]))[:15]
    for t, v in top:
        print(f"  {t:22s} {len(v):3d} invocations")


if __name__ == "__main__":
    main()
