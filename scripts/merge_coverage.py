#!/usr/bin/env python3
"""Merge per-container probe results into one coverage report.

Answers the question that right-sizes the whole project: of the kit's tools,
how many can we actually document from a real binary today, and what is left.
"""
from __future__ import annotations
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAP = ROOT / "capture"
IMAGES = ["cyberlab-aio", "dfir-aio"]


def load(img: str) -> dict[str, dict]:
    f = CAP / img / "coverage.tsv"
    if not f.exists():
        return {}
    out = {}
    with f.open(encoding="utf-8", errors="replace") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            out[row["command"]] = row
    return out


def main() -> None:
    per = {img: load(img) for img in IMAGES}
    cands = sorted({c for d in per.values() for c in d})

    documented: dict[str, dict] = {}   # has real help text
    present_no_help: list[str] = []
    absent: list[str] = []

    for c in cands:
        best = None
        for img in IMAGES:
            row = per[img].get(c)
            if not row or row["status"] != "present":
                continue
            b = int(row.get("bytes") or 0)
            if b > 0 and (best is None or b > best[1]):
                best = (img, b, row)
        if best:
            img, b, row = best
            documented[c] = {"image": img, "bytes": b,
                             "via": row.get("help_flag", ""),
                             "version": (row.get("version") or "").strip()}
        elif any(per[i].get(c, {}).get("status") == "present" for i in IMAGES):
            present_no_help.append(c)
        else:
            absent.append(c)

    (CAP / "coverage.json").write_text(
        json.dumps({"documented": documented,
                    "present_no_help": present_no_help,
                    "absent": absent}, indent=2), encoding="utf-8")

    md = ["# Capture Coverage", "",
          "What can be documented **from a real binary** today, and what cannot.",
          "A tool without a capture cannot get a page — see "
          "[docs/FORMAT.md](../docs/FORMAT.md#5-verification-why-the-options-can-be-trusted).",
          "",
          f"- **{len(documented)} tools captured** with real help text — ready to document",
          f"- **{len(present_no_help)} present but no usable help** — GUI-only, or help "
          f"needs arguments; document workflow rather than flags",
          f"- **{len(absent)} not in either container** — need a booted VM "
          f"(Kali, FLARE-VM Windows guest) or are GUI/appliance-only",
          f"- probed against `cyberlab-aio:v1` and `dfir-aio:v4` on rick", "",
          "## Captured — ready to document", "",
          "| Command | Image | Via | Version | Help bytes |",
          "|---|---|---|---|---|"]
    for c, d in sorted(documented.items()):
        ver = (d["version"] or "")[:48].replace("|", "\\|")
        md.append(f"| `{c}` | {d['image']} | `{d['via']}` | {ver} | {d['bytes']:,} |")

    md += ["", "## Present, but no usable help text", "",
           "These exist in a container but print nothing useful for `--help`. Most are "
           "GUI apps or need arguments first. They get workflow pages, not flag tables.",
           "", ", ".join(f"`{c}`" for c in present_no_help) or "_none_", ""]

    md += ["## Not available in a container", "",
           f"{len(absent)} candidates were absent. This includes Windows-only "
           "(FLARE-VM), GUI-only, appliance services, and names that were never real "
           "commands (package names that do not map to a binary).", "",
           "<details><summary>Full list</summary>", "",
           ", ".join(f"`{c}`" for c in absent), "", "</details>"]

    (CAP / "COVERAGE.md").write_text("\n".join(md), encoding="utf-8")
    print(f"documented={len(documented)}  present_no_help={len(present_no_help)}  "
          f"absent={len(absent)}")


if __name__ == "__main__":
    main()
