"""A flag note must be about its own flag.

nping -c came back describing --icmp from end to end. It named the right
tool, cited a real page and read fluently, so misattributed() -- which looks
for other TOOLS -- saw nothing wrong. A reader would have taken the sentence
as the meaning of -c.

The cases that must SURVIVE are the point of the test. Cross-referencing a
sibling flag is normal and useful writing, and a long spelling of the same
option is not a different option.
"""
import os
import sys

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(R, 'scripts'))
import enrich_loop as e  # noqa: E402

CAUGHT = [
    ('-c', 'An analyst would use the --icmp flag with nping when testing '
           'ICMP connectivity by sending a number of packets.', '--icmp'),
    ('-b', 'Use -o to write the carved files to a chosen directory.', '-o'),
]

SURVIVES = [
    # names its own flag
    ('-c', 'Use -c when verifying files against a stored checksum list.'),
    # cross-reference, but names its own flag too
    ('-c', 'Use -c together with -a all to check every algorithm at once.'),
    # long spelling of the same option
    ('-c', 'The --check form is used when verifying a checksum file.'),
    # no flag named at all: nothing to contradict
    ('-r', 'Use it when the directory must be walked to its full depth.'),
]

ok = []


def check(name, cond):
    ok.append(bool(cond))
    print(('PASS  ' if cond else 'FAIL  ') + name)


for flag, note, want in CAUGHT:
    got = e.wrong_flag(note, flag)
    check('catch %-6s -> %-8s' % (flag, want), got == want)

for flag, note in SURVIVES:
    check('keep  %-6s %s' % (flag, note[:44]), e.wrong_flag(note, flag) is None)

# No flag subject at all (a tool-level note) must never trip it.
check('tool-level note untouched', e.wrong_flag('Reach for it after fls -m.',
                                                None) is None)

print('\n%d/%d passed' % (sum(ok), len(ok)))
sys.exit(0 if all(ok) else 1)
