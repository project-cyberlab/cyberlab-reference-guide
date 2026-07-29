#!/usr/bin/env python3
"""Generate reference/INDEX.md — the capability index.

capability -> tools -> (page, if written yet). Also produces the honest
counter-report: captured tools that map to no capability, and capabilities
with no captured tool behind them. Both are gaps that need a decision; neither
is allowed to hide.
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from taxonomy import TAXONOMY, NOT_A_CAPABILITY, all_mapped_commands  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
COV = json.loads((ROOT / "capture" / "coverage.json").read_text(encoding="utf-8"))
DOCUMENTED: dict[str, dict] = COV["documented"]


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def page_for(cmd: str) -> Path | None:
    hits = list((ROOT / "reference").rglob(f"{cmd}.md"))
    return hits[0] if hits else None


def main() -> None:
    md = [
        "# Capability Index", "",
        "**Start here when you have a problem.** Find what you need to *do*; it "
        "points you at the tool and its page.", "",
        "Phases follow [NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final) "
        "(collect → examine → analyse → report), ordered the way an investigation "
        "actually runs.", "",
        "Legend: **bold** = captured from a real binary, page can be written · "
        "plain = in the kit but not captured yet (needs a booted VM or has no CLI).",
        "",
    ]

    used: set[str] = set()
    empty_caps: list[str] = []
    total_caps = 0

    # Contents
    md.append("## Phases\n")
    for phase in TAXONOMY:
        md.append(f"- [{phase}](#{slug(phase)})")
    md.append("")

    for phase, caps in TAXONOMY.items():
        md.append(f"\n## {phase}\n")
        for cap, cmds in caps:
            total_caps += 1
            have = [c for c in cmds if c in DOCUMENTED]
            miss = [c for c in cmds if c not in DOCUMENTED]
            used.update(have)
            if not have:
                empty_caps.append(f"{phase} / {cap}")
            parts = []
            for c in have:
                p = page_for(c)
                if p:
                    rel = p.relative_to(ROOT / "reference").as_posix()
                    parts.append(f"[**{c}**]({rel})")
                else:
                    parts.append(f"**{c}**")
            parts += [c for c in miss]
            md.append(f"### {cap}\n")
            md.append(", ".join(f"`{p}`" if not p.startswith(("[", "**")) else p
                                for p in parts) or "_no tools mapped_")
            md.append("")

    # ---- the honest counter-report -------------------------------------
    # Scope matters here. _candidates.txt was derived FROM catalog/kit-tools.json,
    # so a captured command in that file is a named kit tool. Everything else was
    # discovered by walking the container's PATH: it ships in a kit image, but the
    # kit manifests never named it, so most of it is plumbing (ls, gcc, dpkg).
    cand_file = ROOT / "capture" / "_candidates.txt"
    kit_named = set(cand_file.read_text(encoding="utf-8").split()) if cand_file.exists() else set()

    unmapped_all = [c for c in DOCUMENTED
                    if c not in all_mapped_commands() and c not in NOT_A_CAPABILITY]
    unmapped_in_kit = sorted(c for c in unmapped_all if c in kit_named)
    unmapped_other = sorted(c for c in unmapped_all if c not in kit_named)
    unmapped = unmapped_in_kit  # the list that actually needs a decision

    md += ["\n---\n", "## Coverage of this index\n",
           f"- **{total_caps} capabilities** across {len(TAXONOMY)} phases",
           f"- **{len(used)} captured tools** are reachable through a capability",
           f"- **{len(unmapped)} named kit tools map to no capability** (below)",
           f"- **{len(empty_caps)} capabilities have no captured tool** behind them yet",
           ""]

    if empty_caps:
        md += ["### Capabilities with nothing captured yet\n",
               "These are real needs the kit may cover with GUI or Windows-only "
               "tools that a Linux container cannot capture.\n"]
        md += [f"- {e}" for e in empty_caps]
        md.append("")

    md += ["### Named kit tools not yet mapped to a capability\n",
           "These are named in the kit manifests, captured from a real binary, and "
           "reach no capability in this index. Each is a taxonomy gap to close or an "
           "explicit out-of-scope decision. Listed rather than silently dropped, "
           "because a missing capability is otherwise invisible.\n",
           ", ".join(f"`{c}`" for c in unmapped) or "_none_", "",
           "### Container-provided commands (not named in the kit manifests)\n",
           "Discovered by walking the container's `PATH`. They ship in a kit image "
           "but no kit manifest names them, so the great majority is OS plumbing "
           "rather than investigative tooling. Kept for completeness only.\n",
           "<details><summary>"
           f"{len(unmapped_other)} container-provided commands</summary>\n",
           ", ".join(f"`{c}`" for c in unmapped_other), "\n</details>"]

    (ROOT / "reference").mkdir(exist_ok=True)
    (ROOT / "reference" / "INDEX.md").write_text("\n".join(md), encoding="utf-8")

    print(f"capabilities={total_caps} mapped_tools={len(used)} "
          f"unmapped={len(unmapped)} empty_caps={len(empty_caps)}")


if __name__ == "__main__":
    main()
