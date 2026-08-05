"""When to reach for each GUI tool, written by hand after research.

Kept separate from generate_gui_pages.py for the same reason enrichment.py is
separate: everything in that file is derived from a capture and cannot be
invented, and everything in this one is a judgement a human made. A reviewer
should be able to see the boundary at a glance.

These answer a question the research loop structurally cannot. The loop
retrieves passages about one tool and compresses them, so it can say what a
tool does. It cannot say why you would open this window rather than the one
beside it, because that comparison exists in no single passage. For the
decompilers it is the entire decision: dnSpy, VB Decompiler and IDR do not
compete on quality, they handle different compilation formats, and choosing
by reputation instead of by format wastes an afternoon before you notice.

Every entry cites what it was written from.
"""
from __future__ import annotations

SCENARIOS: dict[str, dict] = {

    "dnSpy": {
        "scenario": (
            "Reach for dnSpy when the sample is **managed .NET** — a PE "
            "carrying a CLR header, which `die` or CFF Explorer reports in "
            "seconds. It decompiles IL back to near-original C#, so a .NET "
            "dropper often reads almost like the developer's source rather "
            "than like disassembly.\n\n"
            "What makes it beat a static decompiler on live malware is the "
            "built-in debugger. You can attach to a running process, set "
            "breakpoints and step through code that only exists after "
            "unpacking, and you can edit an assembly and save it back — which "
            "is how an anti-debug check or a licence test gets neutered so "
            "the next stage will run.\n\n"
            "It is the wrong tool for unmanaged native code. No CLR header "
            "means nothing here applies, and you want a native disassembler "
            "instead."
        ),
        "sources": [
            "https://dnspy.org/",
            "https://www.cybereason.com/blog/research/.net-malware-dropper",
        ],
    },

    "VB-Decompiler": {
        "scenario": (
            "Reach for VB Decompiler when the sample is **Visual Basic 6** or "
            "**VB.NET / C#**. VB6 is the case that catches people out, "
            "because it compiles two different ways and what comes back "
            "depends entirely on which: P-code recovers a large share of the "
            "original logic, while native-compiled VB6 leaves you much closer "
            "to ordinary disassembly. Establish which you have before "
            "judging the tool.\n\n"
            "Expect a partial reconstruction rather than compilable source. "
            "The vendor quotes roughly 85% logic restoration for P-code and "
            "around 95% for .NET. That is enough to read intent, which is "
            "usually the question, and not enough to rebuild the program.\n\n"
            "For .NET specifically, dnSpy is the better first stop because of "
            "its debugger. VB Decompiler earns its place on the VB6 samples "
            "dnSpy cannot open at all."
        ),
        "sources": [
            "https://www.vb-decompiler.org/products.htm",
            "https://www.vb-decompiler.org/faq.htm",
        ],
    },

    "vbdec": {
        "scenario": (
            "The command-line companion for the same Visual Basic targets as "
            "VB Decompiler. Reach for it when you are processing a set of "
            "samples rather than opening one, or scripting extraction into a "
            "pipeline; use the window when you are reading a single sample "
            "and want to navigate it.\n\n"
            "The format caveat is identical: VB6 P-code reconstructs well, "
            "native-compiled VB6 much less so, and knowing which you have is "
            "the first question rather than an afterthought."
        ),
        "sources": ["https://www.vb-decompiler.org/products.htm"],
    },

    "idr": {
        "scenario": (
            "Reach for IDR when the sample is **Delphi**. Delphi binaries are "
            "large and mostly runtime library, so a general disassembler "
            "buries the author's few thousand lines inside hundreds of "
            "thousands of lines of framework code. IDR knows the runtime "
            "library and can tell the two apart, which is the difference "
            "between a tractable job and an intractable one.\n\n"
            "The form viewer is the reason to open it rather than a generic "
            "tool. Delphi stores its visual forms inside the binary together "
            "with the event handlers wired to each control, so you can go "
            "from *the button labelled Install* straight to the routine that "
            "runs when it is clicked. On a Delphi dropper that is often the "
            "shortest path to the payload."
        ),
        "sources": [
            "https://gitbook.seguranca-informatica.pt/tools-1/decompilers",
        ],
    },
}


# The rest, split into a second file only to keep each readable.
from gui_scenarios_more import SCENARIOS as _MORE  # noqa: E402
SCENARIOS.update(_MORE)
