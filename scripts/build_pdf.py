#!/usr/bin/env python3
"""Render the guide to a single print-ready PDF.

Markdown is the source of truth; this is a build artifact and is never edited
by hand, so the two cannot drift.

Pipeline: markdown -> one self-contained HTML (print CSS + generated contents)
-> PDF via headless Edge/Chrome. No network, no LaTeX.
"""
from __future__ import annotations
import base64
import html
import re
import shutil
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
    # The capability index is the primary entry point, so it comes before the
    # rationale -- in the field you want the lookup, not the design notes.
    ("Capability Index", ROOT / "reference" / "INDEX.md"),
    # docs/FORMAT.md and docs/PLAN.md are deliberately NOT here. The roadmap,
    # the phase list and the risk table are about building the guide, not about
    # using it, and in a field reference they are pages an analyst pays for and
    # never reads. They stay in the repository, where that context belongs.
    # The kit index: VM -> category -> tool. Long, but it is the "what do I
    # have?" half of the guide and has to be carryable in the field too.
    ("Kit Tool List", ROOT / "catalog" / "KIT-TOOLS.md"),
]

# Where the repo lives publicly. Links that point at files which are *not*
# reproduced inside the PDF (raw captures, scripts) are rewritten to here, so a
# downloaded PDF never references the author's local disk.
REPO_URL = "https://github.com/project-cyberlab/cyberlab-reference-guide/blob/main"


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


# Repo-relative paths that ARE reproduced as sections in the PDF, and the
# in-document anchor each one becomes. Keep in step with SECTIONS above.
INLINED = {
    "README.md": "overview",
    "reference/INDEX.md": "capability-index",
    "catalog/KIT-TOOLS.md": "kit-tool-list",
}


def rewrite_href(href: str, src: Path) -> str:
    """Map a link written for the repo onto something valid inside the PDF.

    Markdown pages cross-reference each other with relative paths
    (``../INDEX.md``). Rendered to HTML and printed from a ``file://`` URL those
    resolve against the author's filesystem, so the shipped PDF would point at
    directories that exist only on one machine. Every repo-relative link
    therefore becomes either an internal anchor (if that file is inlined as a
    PDF section) or an absolute GitHub URL (if it is not).
    """
    if not href or href.startswith(("http://", "https://", "mailto:", "#")):
        return href

    path_part, _, frag = href.partition("#")
    if not path_part:                      # pure "#anchor"
        return href

    # Resolve relative to the page that wrote the link, then make it repo-relative.
    try:
        target = (src.parent / path_part).resolve()
        rel = target.relative_to(ROOT).as_posix()
    except (ValueError, OSError):
        return href                        # escapes the repo: leave it alone

    if rel in INLINED:
        return "#" + INLINED[rel]

    # Another tool page -> its section anchor in the Tool Reference.
    if rel.startswith("reference/") and rel.endswith(".md"):
        return "#tool-" + slug(Path(rel).stem)

    # Everything else (raw captures, scripts) is evidence that lives in the
    # repo but not in the PDF: send the reader to the public copy.
    return f"{REPO_URL}/{rel}" + (f"#{frag}" if frag else "")


def strip_placeholders(md_text: str) -> str:
    """Drop unwritten sections rather than printing scaffolding at a reader.

    Pages carry `_TODO: ..._` markers where curation has not happened yet. They
    are the right thing in the source -- the linter counts them, so the debt is
    visible and cannot be forgotten -- but printing "TODO: operational traps"
    in a field guide tells the reader nothing except that the page is
    unfinished. A shorter honest page is better than a padded one.

    Only the placeholder and its now-empty heading are removed; a section with
    real content is untouched.
    """
    lines = md_text.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if re.match(r"^#{2,3} ", line):
            # Look ahead: does this section contain anything but a placeholder?
            j = i + 1
            body: list[str] = []
            while j < len(lines) and not re.match(r"^#{2,3} ", lines[j]):
                body.append(lines[j])
                j += 1
            meaningful = [b for b in body
                          if b.strip() and not re.match(r"^_TODO:.*_$", b.strip())]
            has_placeholder = any(re.match(r"^_TODO:.*_$", b.strip()) for b in body)
            # Drop the heading only when a placeholder is the ONLY thing under
            # it. A heading whose body is empty because a subsection follows is
            # a real heading -- removing it deletes the anchor every link to
            # that section depends on, which is how the capability index's
            # phase links were silently broken.
            if not meaningful and has_placeholder:
                i = j                      # drop heading and placeholder together
                continue
            out.append(line)
            out.extend(b for b in body if not re.match(r"^_TODO:.*_$", b.strip()))
            i = j
            continue
        out.append(line)
        i += 1
    return "\n".join(out)


def fix_links(html_fragment: str, src: Path) -> str:
    return re.sub(
        r'href="([^"]*)"',
        lambda m: f'href="{html.escape(rewrite_href(html.unescape(m.group(1)), src), quote=True)}"',
        html_fragment,
    )


def embed_images(html_fragment: str, src: Path) -> str:
    """Inline screenshots as data URIs.

    Image paths are written relative to the markdown file, but the HTML is
    rendered from build/, so they resolve a level too high and every screenshot
    comes out broken. Embedding sidesteps the path problem entirely and makes
    the PDF self-contained, which matters because it is downloaded on its own,
    away from the repository the images live in.
    """
    def repl(m: re.Match) -> str:
        raw = html.unescape(m.group(1))
        if raw.startswith(("http://", "https://", "data:")):
            return m.group(0)
        img = (src.parent / raw).resolve()
        if not img.exists() or img.suffix.lower() not in (".png", ".jpg", ".jpeg", ".gif"):
            return m.group(0)
        mime = "image/png" if img.suffix.lower() == ".png" else "image/jpeg"
        b64 = base64.b64encode(img.read_bytes()).decode("ascii")
        return f'src="data:{mime};base64,{b64}"'

    return re.sub(r'src="([^"]*)"', repl, html_fragment)


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
/* Long lines must WRAP, never scroll. `overflow-x: auto` gives a scrollbar on
   a web page and gives nothing at all on paper or in a PDF viewer: the text
   past the right edge is simply clipped and unreachable. Wrapping is the only
   way the content survives. */
pre { background: #f7f9fb; border: 1px solid #dde5ed; border-left: 3px solid #1f6feb;
      border-radius: 4px; padding: .6em .8em;
      white-space: pre-wrap; word-wrap: break-word; overflow-wrap: anywhere;
      page-break-inside: avoid; }
pre code { background: none; border: none; padding: 0; font-size: 8.8pt;
           white-space: pre-wrap; overflow-wrap: anywhere; }
code { overflow-wrap: anywhere; }
table { border-collapse: collapse; width: 100%; margin: .6em 0; font-size: 9pt;
        page-break-inside: auto; table-layout: fixed; }
td, th { overflow-wrap: anywhere; word-break: normal; }
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
/* Page numbers in the contents and index. A leader dot rule would need
   CSS GCPM which Chrome lacks, so the number is right-aligned in its own
   column instead -- same job, renders everywhere. */
.toc li { display: flex; align-items: baseline; gap: .4em; }
.toc li > a:first-child { flex: 0 1 auto; }
.toc .pg { margin-left: auto; color: #7a8794; font-variant-numeric: tabular-nums;
           font-size: 9pt; white-space: nowrap; }
.toc ul ul .pg { font-size: 8.5pt; }
.idx { column-count: 3; column-gap: 1.4em; font-size: 9pt; }
.idx div { break-inside: avoid; display: flex; gap: .35em; }
.idx .pg { margin-left: auto; color: #7a8794; font-variant-numeric: tabular-nums; }
.idx a { color: #14181d; }
.idx .grp { column-span: all; font-weight: 700; color: #0b2545; margin: .7em 0 .25em;
            border-bottom: 1px solid #d6dde5; }
"""


CAPABILITY_TITLES = {
    "acquire-preserve": "Acquire & preserve",
    "examine-the-filesystem": "Examine the filesystem",
    "build-the-timeline": "Build the timeline",
    "windows-artifacts": "Windows artifacts",
    "memory-forensics": "Memory forensics",
    "network-analysis": "Network analysis",
    "malware-triage-static": "Malware triage — static",
    "malware-triage-documents": "Malware triage — documents",
    "reverse-engineering": "Reverse engineering",
    "decode-deobfuscate": "Decode & deobfuscate",
    "report-support": "Report & support",
}


def dest_pages(pdf_path: Path) -> dict[str, int]:
    """anchor -> 1-based page number, read back from the rendered PDF.

    Page numbers cannot be known before rendering, so the build renders once to
    learn them and again to print them. Chrome writes a ``/Dests`` table for our
    anchor ids, which makes the mapping exact rather than estimated.
    """
    try:
        from pypdf import PdfReader
    except ImportError:
        return {}
    reader = PdfReader(str(pdf_path))
    page_of = {p.indirect_reference.idnum: i + 1
               for i, p in enumerate(reader.pages)
               if p.indirect_reference is not None}
    dests = reader.trailer["/Root"].get("/Dests")
    dests = dests.get_object() if dests is not None else {}
    out: dict[str, int] = {}
    for name, d in dests.items():
        d = d.get_object()
        arr = d.get("/D", d) if isinstance(d, dict) else d
        try:
            pg = page_of.get(arr[0].idnum)
        except (AttributeError, IndexError, TypeError):
            continue
        if pg:
            out[str(name).lstrip("/")] = pg
    return out


def build_tool_index(tool_pages: list[Path], pages: dict[str, int]) -> str:
    """Alphabetical back-of-book index: every tool, its capability, its page."""
    rows = sorted(tool_pages, key=lambda p: p.stem.lower())
    out = ['<div class="section" id="tool-index"><h1>Alphabetical Tool Index</h1>',
           '<p>Every tool in the guide, A&ndash;Z, with the page its entry starts on.</p>',
           '<div class="idx">']
    letter = ""
    for p in rows:
        first = p.stem[0].upper()
        if not first.isalpha():
            first = "#"
        if first != letter:
            letter = first
            out.append(f'<div class="grp">{html.escape(letter)}</div>')
        anchor = "tool-" + slug(p.stem)
        pg = pages.get(anchor)
        cap = CAPABILITY_TITLES.get(p.parent.name, p.parent.name.replace("-", " "))
        out.append(
            f'<div><a href="#{anchor}"><code>{html.escape(p.stem)}</code></a>'
            f'<span style="color:#7a8794"> {html.escape(cap)}</span>'
            f'<span class="pg">{pg if pg else "&mdash;"}</span></div>')
    out.append("</div></div>")
    return "".join(out)


def add_outline(pdf_path: Path, tool_pages: list[Path]) -> int:
    """Give the PDF a real bookmark tree.

    Headless Chrome renders anchors and named destinations but emits no
    document outline, so a 370-page guide opens with an empty bookmark pane and
    the only way to reach a tool is scrolling. Chrome *does* write a ``/Dests``
    table mapping our anchor ids to pages, so the outline can be reconstructed
    exactly rather than estimated: front matter at the top level, then a
    chapter per capability with its tools nested underneath.
    """
    try:
        from pypdf import PdfReader, PdfWriter
        from pypdf.generic import ArrayObject, NameObject, NullObject
    except ImportError:
        print("  pypdf not installed - outline skipped", file=sys.stderr)
        return 0

    reader = PdfReader(str(pdf_path))
    writer = PdfWriter()
    writer.append_pages_from_reader(reader)

    # page object id -> page index, so a named destination resolves to a page
    page_of = {p.indirect_reference.idnum: i
               for i, p in enumerate(reader.pages)
               if p.indirect_reference is not None}

    dests = reader.trailer["/Root"].get("/Dests")
    dests = dests.get_object() if dests is not None else {}

    def page_for(anchor: str) -> int | None:
        d = dests.get("/" + anchor) or dests.get(anchor)
        if d is None:
            return None
        d = d.get_object()
        arr = d.get("/D", d) if isinstance(d, dict) else d
        try:
            return page_of.get(arr[0].idnum)
        except (AttributeError, IndexError, TypeError):
            return None

    added = 0

    def bookmark(title: str, anchor: str, parent=None):
        nonlocal added
        pg = page_for(anchor)
        if pg is None:
            return None
        added += 1
        return writer.add_outline_item(title, pg, parent=parent)

    for title, _ in SECTIONS:
        bookmark(title, slug(title))

    ref_root = bookmark("Tool Reference", "reference")
    by_cap: dict[str, list[Path]] = {}
    for p in tool_pages:
        by_cap.setdefault(p.parent.name, []).append(p)

    for cap, pages in sorted(
            by_cap.items(),
            key=lambda kv: min((page_for("tool-" + slug(p.stem)) or 10**6)
                               for p in kv[1])):
        title = CAPABILITY_TITLES.get(cap, cap.replace("-", " ").capitalize())
        first = min((page_for("tool-" + slug(p.stem)) or 10**6) for p in pages)
        if first == 10**6:
            continue
        added += 1
        cap_node = writer.add_outline_item(
            f"{title}  ({len(pages)})", first, parent=ref_root)
        for p in sorted(pages, key=lambda q: page_for("tool-" + slug(q.stem)) or 0):
            bookmark(p.stem, "tool-" + slug(p.stem), parent=cap_node)

    # Rewrite link annotations to point at an explicit page destination rather
    # than a named one. Chrome and Edge's built-in PDF viewers resolve named
    # destinations poorly -- links simply do not jump -- while Adobe handles
    # them fine. Most people read this in a browser, so the links have to work
    # there.
    fixed = 0
    for page in writer.pages:
        for annot in (page.get("/Annots") or []):
            try:
                obj = annot.get_object()
            except Exception:
                continue
            if obj.get("/Subtype") != "/Link":
                continue
            dest = obj.get("/Dest")
            if dest is None or not isinstance(dest, (str, bytes)):
                continue
            name = str(dest).lstrip("/")
            target = dests.get("/" + name) or dests.get(name)
            if target is None:
                continue
            target = target.get_object()
            arr = target.get("/D", target) if isinstance(target, dict) else target
            try:
                pg = page_of.get(arr[0].idnum)
            except (AttributeError, IndexError, TypeError):
                continue
            if pg is None:
                continue
            obj[NameObject("/Dest")] = ArrayObject(
                [writer.pages[pg].indirect_reference,
                 NameObject("/XYZ"), NullObject(), NullObject(), NullObject()])
            fixed += 1
    if fixed:
        print(f"resolved {fixed} link destinations to explicit pages")

    writer.page_mode = "/UseOutlines"          # open with the bookmark pane showing
    with open(pdf_path, "wb") as fh:
        writer.write(fh)
    return added


def find_browser() -> str | None:
    for b in BROWSERS:
        if Path(b).exists():
            return b
    return None


def convert(md_text: str) -> str:
    return markdown.markdown(
        md_text, extensions=["tables", "fenced_code", "toc", "sane_lists"])


def render_html(tool_pages: list[Path], pages: dict[str, int]) -> str:
    """Build the whole document. `pages` is empty on the first pass and holds
    anchor->page on the second, which is when the contents gets its numbers."""

    def pg(anchor: str) -> str:
        n = pages.get(anchor)
        return f'<span class="pg">{n}</span>' if n else ""

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
        anchor = slug(title)
        toc.append(f'<li><a href="#{anchor}">{html.escape(title)}</a>{pg(anchor)}</li>')
        body.append(f'<div class="section" id="{anchor}">'
                    f'{embed_images(fix_links(convert(strip_placeholders(path.read_text(encoding="utf-8"))), path), path)}</div>')

    if tool_pages:
        toc.append(f'<li><a href="#reference">Tool Reference</a>{pg("reference")}<ul>')
        body.append('<div class="section" id="reference"><h1>Tool Reference</h1>'
                    '<p>One page per tool. Every option below was read off the '
                    'real binary and is checked by the linter.</p></div>')
        # Group the contents by capability so it reads as chapters, not a
        # 135-entry flat list.
        by_cap: dict[str, list[Path]] = {}
        for p in tool_pages:
            by_cap.setdefault(p.parent.name, []).append(p)
        for cap in sorted(by_cap, key=lambda c: CAPABILITY_TITLES.get(c, c)):
            title = CAPABILITY_TITLES.get(cap, cap.replace("-", " ").capitalize())
            group = sorted(by_cap[cap], key=lambda q: q.stem.lower())
            toc.append(f'<li><strong>{html.escape(title)}</strong> '
                       f'<span style="color:#7a8794">({len(group)})</span></li><ul>')
            for p in group:
                anchor = "tool-" + slug(p.stem)
                toc.append(f'<li><a href="#{anchor}">{html.escape(p.stem)}</a>'
                           f'{pg(anchor)}</li>')
                body.append(f'<div class="section" id="{anchor}">'
                            f'{embed_images(fix_links(convert(strip_placeholders(p.read_text(encoding="utf-8"))), p), p)}</div>')
            toc.append("</ul>")
        toc.append("</ul></li>")
        toc.append(f'<li><a href="#tool-index">Alphabetical Tool Index</a>'
                   f'{pg("tool-index")}</li>')
        body.append(build_tool_index(tool_pages, pages))

    parts.append('<div class="toc"><h1>Contents</h1><ul>'
                 + "".join(toc) + "</ul></div>")
    parts.extend(body)

    return (f"<!doctype html><html><head><meta charset='utf-8'>"
            f"<title>CyberLab Reference Guide</title>"
            f"<style>{CSS}</style></head><body>"
            f"{''.join(parts)}</body></html>")


def main() -> int:
    tool_pages = sorted(p for p in (ROOT / "reference").rglob("*.md")
                        if p.name != "INDEX.md")
    html_path = BUILD / "cyberlab-reference-guide.html"
    pdf_path = BUILD / "cyberlab-reference-guide.pdf"

    browser = find_browser()

    def render(pages: dict[str, int]) -> bool:
        doc = render_html(tool_pages, pages)
        html_path.write_text(doc, encoding="utf-8")
        if not browser:
            return False
        subprocess.run(
            [browser, "--headless", "--disable-gpu", "--no-sandbox",
             "--no-pdf-header-footer", f"--print-to-pdf={pdf_path}",
             html_path.as_uri()],
            check=False, timeout=300,
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return pdf_path.exists()

    if not browser:
        render({})
        print("No Edge/Chrome found — HTML written, PDF skipped.", file=sys.stderr)
        return 1

    # Pass 1 exists only to discover where everything landed.
    if not render({}):
        print("PDF was not produced.", file=sys.stderr)
        return 1
    pages = dest_pages(pdf_path)
    print(f"pass 1: {len(pages)} anchors located")

    # Pass 2 prints those page numbers into the contents and the index.
    if not render(pages):
        print("PDF was not produced on pass 2.", file=sys.stderr)
        return 1
    print(f"wrote {pdf_path.relative_to(ROOT)} "
          f"({pdf_path.stat().st_size:,} bytes)")

    n = add_outline(pdf_path, tool_pages)
    print(f"added {n} PDF bookmarks")

    # build/ is gitignored, so a PDF left only there never reaches anyone who
    # clones or downloads the repo. Publish the finished artifact to the repo
    # root, which is the copy people actually open.
    published = ROOT / "CyberLab-Reference-Guide.pdf"
    shutil.copyfile(pdf_path, published)
    print(f"published {published.name} ({published.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
