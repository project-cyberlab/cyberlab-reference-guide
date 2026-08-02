#!/usr/bin/env python3
"""Generate a GUI page skeleton from a captured control tree.

Same split as the CLI pipeline: everything mechanical comes from the capture,
and only judgement is written by hand. The control inventory, the enumerated
values of every combo box and the screenshot reference are derived from
capture/gui/<tool>/<tool>.tree.txt, so they cannot drift from the application
and cannot be invented.

Hand-written pages are never overwritten: a page without the generated marker
is left alone, exactly as generate_pages.py does.

usage: python scripts/generate_gui_pages.py
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAP = ROOT / "capture" / "gui"
REF = ROOT / "reference"
MARKER = "<!-- generated-by: scripts/generate_gui_pages.py -->"

# Which capability each GUI tool belongs under. Placement is a judgement call
# about what the tool is for, so it is written down here rather than guessed
# from the control tree.
# Purpose is two or three sentences: what the tool is for, what an analyst gets
# out of it, and where it sits relative to the alternatives. Not a product
# blurb and not a paragraph -- enough that someone who has never opened it
# knows whether it is the right thing to reach for.
CAPABILITY = {
    "dnSpy": ("reverse-engineering",
              "Decompile, browse and debug .NET assemblies. It reconstructs "
              "readable C# from IL, so a managed sample is usually faster to "
              "understand here than in a disassembler, and it can attach a "
              "debugger to the running assembly when static reading stalls"),
    "VB-Decompiler": ("reverse-engineering",
                      "Recover source-level structure from Visual Basic "
                      "executables. P-code binaries decompile close to the "
                      "original; native-compiled ones yield disassembly with "
                      "the VB runtime calls identified"),
    "vbdec": ("reverse-engineering",
              "Decompile VB5 and VB6 binaries, recovering forms, controls and "
              "event handlers. Those names usually survive compilation and "
              "describe what the program was written to do"),
    "idr": ("reverse-engineering",
            "Reconstruct Delphi programs: identify the runtime library, "
            "recover form definitions and name the event handlers. Delphi "
            "binaries are mostly runtime code, so separating the author's few "
            "hundred lines from the library's tens of thousands is the "
            "difference between a tractable job and an intractable one"),
    "CFF-Explorer": ("malware-triage-static",
                     "Inspect and edit every structure in a PE file — headers, "
                     "sections, imports, exports, resources — with a built-in "
                     "hex editor. The import table and the gap between virtual "
                     "and raw section sizes are the two fastest reads on what "
                     "a binary can do and whether it is packed"),
    "PE-Detective": ("malware-triage-static",
                     "Scan a PE, or a directory of them, against a signature "
                     "database to name the compiler, linker or packer that "
                     "produced it. Answers \"what built this?\" before you "
                     "commit to unpacking"),
    "Signature-Explorer": ("malware-triage-static",
                           "Browse, edit and add to the packer signature "
                           "database that PE Detective and CFF Explorer read. "
                           "This is how a sample nothing recognises becomes a "
                           "signature that catches the next one"),
    "PDFStreamDumper": ("malware-triage-documents",
                        "Enumerate the objects and streams inside a PDF and "
                        "decode them, applying the filters so JavaScript, "
                        "embedded files and launch actions are readable rather "
                        "than compressed noise"),
    "OffVis": ("malware-triage-documents",
               "Visualise the record structure of legacy binary Office files "
               "beside their raw bytes. Exploits in these formats work by "
               "malforming records, so seeing the parsed structure disagree "
               "with the bytes is the detection"),
    "HashMyFiles": ("acquire-preserve",
                    "Hash a set of files — MD5, SHA-1, SHA-256 and CRC32 — and "
                    "show them in one sortable list. Sorting by hash collapses "
                    "duplicates across directories instantly, which is what "
                    "makes it a triage tool rather than a hashing utility"),
    "CryptoTester": ("decode-deobfuscate",
                     "Try cryptographic and encoding operations against a "
                     "sample interactively: XOR, block ciphers, hashes and "
                     "conversions, with entropy and pattern views to judge "
                     "whether a result is plausible plaintext. Built for the "
                     "guess-and-check work of recovering a malware "
                     "configuration blob"),
    "Regshot": ("windows-artifacts",
                "Take a registry and filesystem snapshot before and after "
                "detonating a sample, then diff them. The delta is the "
                "persistence and configuration the sample wrote"),
    "AccessEnum": ("windows-artifacts",
                   "Enumerate the effective permissions across a directory "
                   "tree or registry branch and show them in one list. Sorting "
                   "by permission surfaces the outlier — the world-writable "
                   "path that does not belong"),
    "ADExplorer": ("windows-artifacts",
                   "Browse Active Directory as a live tree and take offline "
                   "snapshots of it. A snapshot can be diffed later, which "
                   "turns \"what changed in the directory?\" into a question "
                   "with an answer"),
}

# Older Win32 dialogs expose no real control types: every button, checkbox and
# field comes back as a generic Pane, and only its name distinguishes it. PE
# Detective's Browse, Scan, Recursive and Deep Scan are all Panes. Excluding
# them left those pages with an empty control table while the evidence sat in
# the capture, so a *named* Pane counts. An unnamed one is a layout container
# and still does not.
LEAF = ("Button", "Edit", "CheckBox", "ComboBox", "RadioButton", "List",
        "Tree", "Tab", "TabItem", "MenuItem", "Text", "Slider", "Document",
        "Pane", "Group", "Hyperlink", "SplitButton", "ToolBar")


# The judgement layer for GUI pages, kept here for the same reason
# enrichment.py exists: the control inventory is captured, and everything a
# capture cannot tell you is written down separately where a reviewer can see
# exactly which claims are human.
#
# Steps name controls verbatim as the tree records them, so the linter can
# check them. Seven steps maximum per the Microsoft procedure convention.
GUI_NOTES = {
    "PE-Detective": {
        "steps": [
            "Press **Browse** and choose the binary.",
            "Tick **Deep Scan** — the default pass only checks the entry point, "
            "and packers that relocate it are missed without this.",
            "Choose **All Matches** rather than **Best Match** when triaging; "
            "a single best match hides the disagreement that tells you a "
            "signature is shaky.",
            "Press **Scan**.",
            "For a corpus, tick **Directory Scan** and **Recursive** instead of "
            "selecting one file.",
        ],
        "gotchas": [
            "It reports signature matches, not facts. A packer name is a "
            "hypothesis; a custom or modified packer matches nothing at all, so "
            "silence never means clean.",
            "**Best Match** is the default and is the wrong setting for triage. "
            "Two signatures disagreeing is information.",
            "It shares a signature format with Signature Explorer, so an "
            "unrecognised sample can be turned into a new signature there.",
        ],
    },
    "CFF-Explorer": {
        "steps": [
            "Drag the binary onto the window, or use the file menu.",
            "Work through the **Tree** on the left: headers, sections, imports, "
            "resources.",
            "Read the import table first — what a binary asks the OS for is the "
            "fastest read on what it can do.",
            "Compare section virtual size against raw size; a large gap is the "
            "classic packed-binary signal.",
            "Use the hex editor for a targeted look rather than a general "
            "browse.",
        ],
        "gotchas": [
            "It is an *editor*, not just a viewer. It will happily write to "
            "the file you opened, so work on a copy — never the evidence.",
            "It reports the headers as they are written. Malware edits headers "
            "freely, so a field saying DLL means the field says DLL.",
            "The UI is an old Win32 dialog and exposes almost nothing to "
            "automation: the whole window comes back as four unnamed panes, "
            "which is why this page has a small control table and a screenshot "
            "doing the work.",
        ],
    },
    "Signature-Explorer": {
        "steps": [
            "Open the signature database from the **Signatures** pane.",
            "Use **Check that the signature doesn't already exist** before "
            "adding anything — duplicates are the usual way a database rots.",
            "Fill **Name:**, **Entry Point:** and, where the pattern is not at "
            "the entry point, **Entire Portable Executable:**.",
            "Record why the signature exists in **Comments:** — a pattern with "
            "no rationale cannot be reviewed later.",
            "Press **Add**, then **Save Changes**.",
        ],
        "gotchas": [
            "This edits the database that PE Detective and CFF Explorer read. A "
            "bad signature here produces confident wrong answers in both.",
            "Entry-point signatures miss anything that relocates the entry "
            "point, which is exactly what many packers do. Prefer a whole-file "
            "pattern when the sample allows it.",
            "**Save Changes** is a separate action. Adding a signature and "
            "closing the window loses it.",
        ],
    },
    "HashMyFiles": {
        "steps": [
            "Drag files, or a folder, onto the window.",
            "Read the count in the status pane to confirm everything you "
            "expected was taken — it is the only feedback that files were "
            "missed.",
            "Sort by hash to group identical files; duplicates across "
            "directories collapse immediately.",
            "Copy the hashes out for the report, or save them as the record of "
            "what was collected.",
        ],
        "gotchas": [
            "Hashing here is for triage and deduplication. It is not "
            "acquisition — an image's hash of record comes from the acquisition "
            "tool that made it.",
            "It follows what you dropped and nothing more. A folder dropped "
            "without recursion silently hashes only the top level.",
        ],
    },
    "PDFStreamDumper": {
        "steps": [
            "Open the PDF. Objects load into the list on the left.",
            "Look for streams with `/JavaScript`, `/OpenAction`, `/Launch` or "
            "`/EmbeddedFile` first — those are where behaviour hides.",
            "Select a stream to see its decoded content; the tool applies the "
            "filters so you do not have to.",
            "Extract an embedded file rather than executing anything.",
        ],
        "gotchas": [
            "A PDF that parses cleanly here can still be malicious, and one that "
            "fails to parse is often *more* interesting — malformed structure "
            "is used deliberately to defeat parsers.",
            "It decodes streams for you, which means it also decodes hostile "
            "content. Run it on the analysis VM with no network path, not on a "
            "workstation.",
            "Object numbers are not stable across a rewrite of the same "
            "document, so cite content, not object numbers, in a report.",
        ],
    },
    "OffVis": {
        "steps": [
            "Open the legacy Office binary — `.doc`, `.xls`, `.ppt`.",
            "Read the parsed structure against the raw bytes shown alongside it.",
            "Compare what the record headers claim against what is actually "
            "present; the mismatch is the exploit.",
        ],
        "gotchas": [
            "It only understands the *binary* formats. OOXML files — `.docx`, "
            "`.xlsx` — are ZIP archives and this tool cannot read them; unzip "
            "and use `oledump.py` on the extracted `vbaProject.bin`.",
            "It is a structure visualiser, not a detector. It shows you the "
            "record layout so you can see the malformation; it does not tell "
            "you one is present.",
            "The tool is old and unmaintained. Treat a crash as information "
            "about the file rather than a reason to stop.",
        ],
    },
    "dnSpy": {
        "steps": [
            "**Open** the .NET assembly.",
            "Read the decompiled C# rather than the IL first — .NET decompiles "
            "cleanly enough that the source is usually the fastest route.",
            "Use **Search Assemblies** for the strings and API names that "
            "matter, instead of browsing the namespace tree.",
            "Set a breakpoint and start debugging when static reading stalls — "
            "this is a debugger as well as a decompiler, which is the reason to "
            "choose it.",
            "**Export to Project...** when the assembly is worth reading as a "
            "whole in an editor.",
        ],
        "gotchas": [
            "Obfuscated assemblies decompile into something that looks like "
            "code and is not. Names are meaningless after obfuscation; the "
            "control flow may be too. De-obfuscate first with `de4dot`.",
            "Debugging runs the sample. Do it only on the isolated VM, with no "
            "network path out.",
            "It edits and recompiles assemblies. That is useful and it is also "
            "how evidence gets modified by accident — work on a copy.",
        ],
    },
    "CryptoTester": {
        "steps": [
            "Paste or load the ciphertext.",
            "Try the obvious first: single-byte XOR and the common block ciphers "
            "cover most malware configuration blobs.",
            "Use the entropy and pattern views to judge whether the result is "
            "plausible plaintext before believing a key.",
            "Record the key and mode that worked; a decryption nobody can "
            "reproduce is not a finding.",
        ],
        "gotchas": [
            "It is an experiment bench, not an oracle. It tells you a "
            "transformation produced output, not that the output is correct.",
            "Plausible-looking plaintext from a short sample is often "
            "coincidence. Confirm against a second sample before concluding.",
        ],
    },
    "AccessEnum": {
        "steps": [
            "Accept the licence on first run; until that is done the tool never "
            "reaches its main window.",
            "Choose the directory or registry key to enumerate.",
            "Run the scan, then sort by the permissions column rather than by "
            "path — the outliers are the finding, and they do not cluster by "
            "location.",
            "Save the results as the before-state when you are about to change "
            "anything.",
        ],
        "gotchas": [
            "It reports what the ACLs say, not what is reachable. Group "
            "membership, inheritance and share permissions all sit on top of "
            "this.",
            "The capture behind this page is the licence dialog, not the tool: "
            "a first run shows the EULA and nothing else. Sysinternals "
            "binaries need `-accepteula` before they can be driven "
            "automatically, so the control table here documents that dialog "
            "rather than the main window.",
        ],
    },
    "VB-Decompiler": {
        "steps": [
            "Open the Visual Basic executable.",
            "Check whether it is p-code or native — the tool tells you, and it "
            "decides how much you get back.",
            "Read the form definitions: VB malware often carries its logic in "
            "event handlers rather than in a main routine.",
        ],
        "gotchas": [
            "P-code decompiles close to source. Native-compiled VB gives you "
            "disassembly with VB runtime calls, which is a different and much "
            "slower job.",
            "The Lite edition omits much of the analysis. Check which build you "
            "are on before concluding a feature is missing.",
        ],
    },
    "vbdec": {
        "steps": [
            "Open the VB5/VB6 binary.",
            "Work from the form and control names, which usually survive and "
            "describe the program's intent.",
        ],
        "gotchas": [
            "Scope is VB5 and VB6 only. VB.NET is a .NET assembly — use "
            "[dnSpy](../reverse-engineering/dnSpy-gui.md) for those.",
        ],
    },
    "idr": {
        "steps": [
            "Open the Delphi executable.",
            "Let it match the runtime library first; without that, most of the "
            "disassembly is Delphi's own code rather than the author's.",
            "Read the reconstructed forms and event handlers, which is where "
            "Delphi programs keep their logic.",
        ],
        "gotchas": [
            "Delphi binaries are mostly runtime. Library signature matching is "
            "what separates the few hundred lines that matter from the tens of "
            "thousands that do not.",
            "The knowledge base is version-specific. A mismatch against the "
            "Delphi version used to build the sample leaves the runtime "
            "unidentified and the output far less useful.",
        ],
    },
}


def parse(tree_text: str) -> dict:
    head = {}
    for line in tree_text.splitlines():
        m = re.match(r"^# (\w[\w ]*): (.*)$", line)
        if m:
            head[m.group(1).strip()] = m.group(2).strip()
    controls = []
    for line in tree_text.splitlines():
        if line.startswith("#"):
            continue
        m = re.match(r"^(\s*)(\w+)(?: \"([^\"]*)\")?(?: #(\S+))?(?: \[([^\]]*)\])?", line)
        if not m:
            continue
        indent, ctype, name, aid, key = m.groups()
        controls.append({"depth": len(indent) // 2, "type": ctype,
                         "name": name or "", "id": aid or "", "key": key or ""})
    # ListItems directly under a ComboBox are that control's permitted values.
    values: dict[str, list[str]] = {}
    current = None
    for c in controls:
        if c["type"] == "ComboBox":
            current = c["id"] or c["name"]
            values.setdefault(current, [])
        elif c["type"] == "ListItem" and current:
            values[current].append(c["name"])
        elif c["type"] not in ("List", "ListItem") and c["depth"] <= 1:
            current = None
    return {"head": head, "controls": controls,
            "values": {k: v for k, v in values.items() if v}}


def build(tool: str, data: dict, cap: str, blurb: str, has_png: bool) -> str:
    head = data["head"]
    window = head.get("window", "")
    version = ""
    vm = re.search(r"v?(\d+[\d.]*)", window)
    if vm:
        version = vm.group(0)

    L = [MARKER, f"# {tool} (GUI)", ""]
    L.append(f"**Capability:** {cap.replace('-', ' ')}  "
             f"**Window:** `{head.get('class','')}`  "
             f"**Version:** {version or '—'}")
    L.append(f"**Captured:** `{head.get('exe','')}` on {head.get('captured','')[:10]} — "
             f"control tree in "
             f"[`capture/gui/{tool}/{tool}.tree.txt`](../../capture/gui/{tool}/{tool}.tree.txt)")
    L += ["", "[← Capability index](../INDEX.md) · "
              "[Kit tool list](../../catalog/KIT-TOOLS.md)", ""]

    L += ["## Purpose", "", blurb + ".", ""]

    if has_png:
        L += ["## Window", "",
              f"![{tool} main window](../../capture/gui/{tool}/{tool}.png)", ""]

    leaves = [c for c in data["controls"]
              if c["type"] in LEAF
              and (c["name"] if c["type"] in ("Pane", "Group") else (c["name"] or c["id"]))]
    if leaves:
        # Structure follows the Wireshark User's Guide, which documents a window
        # as prose plus a short list of its major parts rather than an
        # inventory of every control. A 179-row table of every button in dnSpy
        # is not a reference, it is a data dump, and the AutomationId column was
        # worse: `toolButtonElapsedTime` is how the linter ties a claim to the
        # capture, and it means nothing to an analyst. Both are in
        # capture/gui/<tool>/<tool>.tree.txt, which is where evidence belongs.
        notes = GUI_NOTES.get(tool, {}).get("controls", {})

        # Curated controls first, in the order they were written. These are the
        # ones someone actually reaches for.
        curated = [c for c in leaves
                   if (c["name"] or "").strip() in notes]
        rest = [c for c in leaves
                if (c["name"] or "").strip() not in notes]

        L += ["## Controls", ""]
        if curated:
            L += ["| Control | Type | What it does |", "|---|---|---|"]
            seen = set()
            for c in curated:
                label = (c["name"] or "").strip().replace("|", "\\|")
                key = (label, c["type"])
                if key in seen:
                    continue
                seen.add(key)
                L.append(f"| **{label}** | {c['type']} | "
                         f"{notes[label].replace('|', chr(92) + '|')} |")
            L.append("")

        named_rest = []
        seen_r = set()
        for c in rest:
            label = (c["name"] or c["id"].split(".")[-1] or "").strip()
            if not label or not label.strip("|`") or label in seen_r:
                continue
            seen_r.add(label)
            named_rest.append(label.replace("|", "\\|"))
        if named_rest:
            shown = ", ".join(f"**{n}**" for n in named_rest[:40])
            more = ("" if len(named_rest) <= 40
                    else f", and {len(named_rest) - 40} more")
            L += [f"The window exposes {len(named_rest)} further named controls: "
                  f"{shown}{more}. The full tree, with every automation id, is in "
                  f"[the capture](../../capture/gui/{tool}/{tool}.tree.txt).", ""]

    if data["values"]:
        L += ["## Enumerated values", "",
              "Read from the control itself, so this is the set of choices in "
              "this build rather than what the documentation claims.", ""]
        for ctrl, vals in data["values"].items():
            L.append(f"**{ctrl.split('.')[-1]}**")
            L.append("")
            for v in vals:
                L.append(f"- {v}")
            L.append("")

    note = GUI_NOTES.get(tool, {})
    if note.get("steps"):
        L += ["## Using it", ""]
        L += [f"{i}. {s}" for i, s in enumerate(note["steps"], 1)]
        L.append("")
    else:
        L += ["## Using it", "",
              "_TODO: numbered click-path, at most seven steps per task._", ""]

    if note.get("gotchas"):
        L += ["## Gotchas", ""]
        L += [f"- {g}" for g in note["gotchas"]]
        L.append("")
    else:
        L += ["## Gotchas", "",
              "_TODO: what surprises an analyst here._", ""]
    return "\n".join(L)


def main() -> int:
    if not CAP.exists():
        print("no capture/gui yet")
        return 0
    written = preserved = skipped = 0
    for d in sorted(CAP.iterdir()):
        if not d.is_dir() or d.name.startswith("_"):
            continue
        tool = d.name
        tree = d / f"{tool}.tree.txt"
        if not tree.exists():
            continue
        text = tree.read_text(encoding="utf-8", errors="replace")
        if "# ERROR" in text or "#--- nodes: 0" in text:
            skipped += 1
            continue
        if tool not in CAPABILITY:
            skipped += 1
            continue
        cap, blurb = CAPABILITY[tool]
        out = REF / cap / f"{tool}-gui.md"
        if out.exists() and MARKER not in out.read_text(encoding="utf-8", errors="replace"):
            preserved += 1
            continue
        data = parse(text)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(build(tool, data, cap, blurb, (d / f"{tool}.png").exists()),
                       encoding="utf-8")
        written += 1
    print(f"gui pages written={written} hand-written preserved={preserved} skipped={skipped}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
