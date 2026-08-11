"""A flag whose twin is already answered is not worth researching again.

generate_pages mirrors guidance across a short and long spelling that share
an identical captured description, so answering -c fills the --check row
too. rank_flags could not see that, and spent 7% of the flag budget -- 49 of
706 recorded attempts -- on options that already had an answer.

The pairs come from the help declaring both spellings on one line, which is
the tool's own statement that they are one option.
"""
import os
import sys

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(R, 'scripts'))
import enrich_loop as e  # noqa: E402

ok = []


def check(name, cond):
    ok.append(bool(cond))
    print(('PASS  ' if cond else 'FAIL  ') + name)


# Real pairings from the captured help of tools in this guide.
check('sha256sum -c -> --check', e._twin('sha256sum', '-c') == '--check')
check('sha256sum --check -> -c', e._twin('sha256sum', '--check') == '-c')
check('dumpcap -D -> --list-interfaces',
      e._twin('dumpcap', '-D') == '--list-interfaces')
check('dumpcap --interface -> -i', e._twin('dumpcap', '--interface') == '-i')

# An option with only one spelling has no twin, and must not invent one.
check('no twin invented for a lone flag',
      e._twin('sha256sum', '--ignore-missing') is None)
check('unknown tool yields nothing', e._twin('nosuchtool', '-c') is None)

# The exclusion itself: a flag whose twin is answered drops out of ranking.
# rank_flags reads ENRICHMENT, so this checks the pairing feeds it correctly
# rather than re-testing the corpus ranking.
from enrichment import ENRICHMENT  # noqa: E402
answered = set((ENRICHMENT.get('sha256sum') or {}).get('when', {}))
check('sha256sum --check is answered in the guide', '--check' in answered)
expanded = answered | {t for f in answered if (t := e._twin('sha256sum', f))}
check('-c excluded because --check is answered', '-c' in expanded)

print('\n%d/%d passed' % (sum(ok), len(ok)))
sys.exit(0 if all(ok) else 1)
