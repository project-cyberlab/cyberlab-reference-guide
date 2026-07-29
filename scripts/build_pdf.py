#!/usr/bin/env python3
"""Render the guide to a single print-ready PDF.

Markdown is the source of truth; this is a build artifact and is never edited
by hand, so the two cannot drift.

Pipeline: markdown -> one self-contained HTML (print CSS + generated contents)
-> PDF via headless Edge/Chrome. No network, no LaTeX.
"""
from __future__ import annotations
import html
import re
import subprocess
import sys
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "build"
BUILD.mkdir(exist_ok=True)

BROWSERS = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
]

# Order matters: this is the reading order of the printed booklet.
SECTIONS = [
    ("Overview", ROOT / "README.md"),
    ("The Format", ROOT / "docs" / "FORMAT.md"),
    ("Roadmap", ROOT / "docs" / "PLAN.md"),
    # The kit index: VM -> category -> tool. Long, but it is the "what do I
    # have?" half of the guide and has to be carryable in the field too.
    ("Kit Tool List", ROOT / "catalog" / "KIT-TOOLS.md"),
]

CSS = """
@page { size: Letter; margin: 16mm 14mm 16mm 14mm;
        @bottom-center { content: counter(page); } }
* { box-sizing: border-box; }
body { font: 10.5pt/1.45 "Segoe UI", system-ui, sans-serif; color: #14181d;
       margin: 0; }
h1 { font-size: 20pt; margin: 0 0 .3em; padding-bottom: .2em;
     border-bottom: 2.5px solid #1f6feb; color: #0b2545; }
h2 { font-size: 14pt; margin: 1.4em 0 .35em; color: #0b2545;
     border-bottom: 1px solid #d6dde5; padding-bottom: .15em; }
h3 { font-size: 11.5pt; margin: 1.1em 0 .3em; color: #1f3b57; }
p, li { orphans: 3; widows: 3; }
code { font: 9.2pt/1.35 "Cascadia Mono", Consolas, monospace;
       background: #f2f5f8; padding: .1em .32em; border-radius: 3px;
       border: 1px solid #e2e8ef; }
pre { background: #f7f9fb; border: 1px solid #dde5ed; border-left: 3px solid #1f6feb;
      border-radius: 4px; padding: .6em .8em; overflow-x: auto;
      page-break-inside: avoid; }
pre code { background: none; border: none; padding: 0; font-size: 8.8pt; }
table { border-collapse: collapse; width: 100%; margin: .6em 0; font-size: 9pt;
        page-break-inside: auto; }
th { background: #0b2545; color: #fff; text-align: left; padding: .38em .5em;
     font-weight: 600; }
td { border: 1px solid #dde5ed; padding: .32em .5em; vertical-align: top; }
tr:nth-child(even) td { background: #f7f9fb; }
tr { page-break-inside: avoid; }
blockquote { margin: .7em 0; padding: .5em .9em; background: #fff8e6;
             border-left: 3px solid #e3a008; }
a { color: #1f6feb; text-decoration: none; }
.section { page-break-before: always; }
.section:first-of-type { page-break-before: avoid; }
.cover { text-align: center; padding-top: 26vh; page-break-after: always; }
.cover h1 { font-size: 30pt; border: none; }
.cover .sub { color: #4a5b6e; font-size: 12pt; margin-top: .4em; }
.cover .meta { color: #7a8794; font-size: 9.5pt; margin-top: 2.5em; }
.toc { page-break-after: always; }
.toc a { color: #14181d; }
.toc ul { list-style: none; padding-left: 1em; }
"""


def find_browser() -> str | None:
    for b in BROWSERS:
        if Path(b).exists():
            return b
    return None


def convert(md_text: str) -> str:
    return markdown.markdown(
        md_text, extensions=["tables", "fenced_code", "toc", "sane_lists"])


def main() -> int:
    # Tool pages, grouped by their capability directory.
    tool_pages = sorted((ROOT / "reference").rglob("*.md"))

    parts: list[str] = []
    toc: list[str] = []

    parts.append(
        '<div class="cover"><h1>CyberLab Reference Guide</h1>'
        '<div class="sub">Field quick-reference for the kit<br>'
        'capability &rarr; tool &rarr; command &rarr; every option explained</div>'
        '<div class="meta">Generated from the repository. '
        'Markdown is the source of truth.<br>'
        'github.com/project-cyberlab/cyberlab-reference-guide</div></div>')

    body: list[str] = []
    for title, path in SECTIONS:
        if not path.exists():
            print(f"  skip (missing): {path.name}", file=sys.stderr)
            continue
        anchor = re.sub(r"[^a-z0-9]+", "-", title.lower())
        toc.append(f'<li><a href="#{anchor}">{html.escape(title)}</a></li>')
        body.append(f'<div class="section" id="{anchor}">'
                    f'{convert(path.read_text(encoding="utf-8"))}</div>')

    if tool_pages:
        toc.append('<li><a href="#reference">Tool Reference</a><ul>')
        body.append('<div class="section" id="reference"><h1>Tool Reference</h1>'
                    '<p>One page per tool. Every option below was read off the '
                    'real binary and is checked by the linter.</p></div>')
        for p in tool_pages:
            name = p.stem
            anchor = "tool-" + re.sub(r"[^a-z0-9]+", "-", name.lower())
            cat = p.parent.name.replace("-", " ")
            toc.append(f'<li><a href="#{anchor}">{html.escape(name)} '
                       f'<em>({html.escape(cat)})</em></a></li>')
            body.append(f'<div class="section" id="{anchor}">'
                        f'{convert(p.read_text(encoding="utf-8"))}</div>')
        toc.append("</ul></li>")

    parts.append('<div class="toc"><h1>Contents</h1><ul>'
                 + "".join(toc) + "</ul></div>")
    parts.extend(body)

    html_doc = (f"<!doctype html><html><head><meta charset='utf-8'>"
                f"<title>CyberLab Reference Guide</title>"
                f"<style>{CSS}</style></head><body>"
                f"{''.join(parts)}</body></html>")

    html_path = BUILD / "cyberlab-reference-guide.html"
    html_path.write_text(html_doc, encoding="utf-8")
    print(f"wrote {html_path.relative_to(ROOT)} ({len(html_doc):,} bytes)")

    browser = find_browser()
    if not browser:
        print("No Edge/Chrome found — HTML written, PDF skipped.", file=sys.stderr)
        return 1

    pdf_path = BUILD / "cyberlab-reference-guide.pdf"
    cmd = [browser, "--headless", "--disable-gpu", "--no-sandbox",
           "--no-pdf-header-footer", f"--print-to-pdf={pdf_path}",
           html_path.as_uri()]
    subprocess.run(cmd, check=False, timeout=180,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if pdf_path.exists():
        print(f"wrote {pdf_path.relative_to(ROOT)} "
              f"({pdf_path.stat().st_size:,} bytes)")
        return 0
    print("PDF was not produced.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
