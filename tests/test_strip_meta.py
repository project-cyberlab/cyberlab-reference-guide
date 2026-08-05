"""strip_meta must cut passage-talk and leave forensic prose alone.

Every string here is a real note the loop produced. The two "must survive"
cases are the ones that caught the first draft of the pattern out: it matched
a bare "source", which in this domain means the evidence, not a citation.
"""
import os
import sys

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(R, 'scripts'))
import enrich_loop as e  # noqa: E402

LEAKS = [
    ("mactime",
     "An analyst reaches for mactime after gathering temporal data into a "
     "body file, giving a chronological view, which is critical for event "
     "reconstruction. The passages do not explicitly compare it to similar "
     "tools."),
    ("clamscan --remove",
     "An analyst would use the --remove flag when monitoring an "
     "upload/downloads directory, as the passages caution against its "
     "general use due to risks of accidental deletion."),
    ("yara",
     "An analyst reaches for YARA when they need to detect malware using "
     "complex string conditions, offsets, and metadata, as described in the "
     "passages."),
    ("evtxexport",
     "An analyst reaches for evtxexport when examining a Windows EVTX file. "
     "It is explicitly mentioned as a tool suited for processing EVTX files "
     "in the context of the walkthrough."),
    ("editcap",
     "An analyst reaches for editcap when splitting capture files. They use "
     "capinfos to check file details first, as the passages show editcap "
     "being used alongside capinfos."),
]

# "source" here means evidence, not citation. Both were false positives.
SURVIVE = [
    ("log2timeline.py --timezone",
     "When analyzing loose files or a triage collection, an analyst would use "
     "the --timezone flag to explicitly specify the source system's time "
     "zone."),
    ("dcfldd",
     "An analyst reaches for dcfldd when hashing on the fly. They may use it "
     "after preparing the source and destination media, and before verifying "
     "the image."),
]

ok = []


def check(name, cond):
    ok.append(cond)
    print(('PASS  ' if cond else 'FAIL  ') + name)


for label, note in LEAKS:
    out = e.strip_meta(note)
    check('%-26s leak removed' % label, not e.META.search(out))
    check('%-26s content survives' % label, len(out) > 40)

for label, note in SURVIVE:
    out = e.strip_meta(note)
    check('%-26s untouched' % label, out.strip() == note.strip())

# A note that is nothing but passage-talk collapses, and the gate's own
# length check then rejects it -- strip_meta must not fabricate a pass.
check('pure passage-talk collapses',
      len(e.strip_meta("The passages do not explicitly compare it.")) < 40)

print('\n%d/%d passed' % (sum(ok), len(ok)))
sys.exit(0 if all(ok) else 1)
