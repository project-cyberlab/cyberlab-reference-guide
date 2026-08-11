"""A tool stops being retried only until it is seeded.

The rotation is fair, and that is the problem: a tool with no corpus misses
every round and its attempt count rises with everyone else's, so it is picked
again forever. vdbbin, vivbin, xxd and yarac reached 196 attempts each without
producing a single note, and 23 such tools were taking 19% of every attempt.

The skip must never harden into "this tool has no sources". These tests pin
the escape hatch: seed it and it comes straight back.
"""
import hashlib
import json
import os
import sys
import tempfile
from pathlib import Path

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(R, 'scripts'))
import enrich_loop as e  # noqa: E402

tmp = Path(tempfile.mkdtemp())
e.BARREN = tmp / 'barren.json'
e.LIVE_LOG = tmp / 'live.log'
SEEDFILE = tmp / 'seed-urls.json'

ok = []


def check(name, cond):
    ok.append(cond)
    print(('PASS  ' if cond else 'FAIL  ') + name)


def write_seeds(d):
    SEEDFILE.write_text(json.dumps(d), encoding='utf-8')
    e.seed_counts = lambda: {k: len(v) for k, v in
                             json.loads(SEEDFILE.read_text(encoding='utf-8'))
                             .items()}
    e.seed_fp = lambda t: hashlib.sha1(
        chr(10).join(sorted(
            json.loads(SEEDFILE.read_text(encoding='utf-8')).get(t, [])
        )).encode()).hexdigest()[:12]


# A log where vdbbin only ever missed, and fls sometimes kept.
lines = []
for _ in range(10):
    lines.append('00:00:00  MISS     vdbbin                       no passages')
for _ in range(9):
    lines.append('00:00:00  MISS     fls                          no passages')
lines.append('00:00:00  KEPT     fls                          a real note')
# Missed only a few times: not enough evidence to call it barren.
for _ in range(3):
    lines.append('00:00:00  MISS     rare                         no passages')
e.LIVE_LOG.write_text('\n'.join(lines), encoding='utf-8')

write_seeds({})
found = e.refresh_barren()
check('a tool that only ever missed is recorded', 'vdbbin' in found)
check('a tool that ever produced a note is not', 'fls' not in found)
check('too few attempts is not enough', 'rare' not in found)
check('recorded with its seed count',
      (found.get('vdbbin') or {}).get('seeds') == 0)
check('skipped while unseeded', 'vdbbin' in e.still_barren())

# The escape hatch: seeding it makes it eligible again, with no other action.
write_seeds({'vdbbin': ['https://example.com/vdbbin-usage']})
check('seeding makes it eligible again', 'vdbbin' not in e.still_barren())

# And if it is seeded, misses again, and is re-recorded at the higher count,
# it stays skipped until seeded FURTHER -- not permanently.
# Refreshing must NOT re-trap it. The log still holds every miss from
# before the seeds existed, so recomputing over all history would mark it
# barren again at the new seed count and it could never earn a KEPT,
# because it would never be selected. Seeding has to actually buy a run.
e.refresh_barren()
check('seeding is not undone by the next refresh',
      'vdbbin' not in e.still_barren())

# Once it HAS had its fresh run and still only missed, it is set aside
# again -- at the higher seed count, so more seeds free it once more.
extra = ['00:00:00  MISS     vdbbin                       no passages'] * 10
e.LIVE_LOG.write_text('\n'.join(lines + extra), encoding='utf-8')
e.refresh_barren()
check('re-recorded after a fresh run that also missed',
      'vdbbin' in e.still_barren())
write_seeds({'vdbbin': ['https://example.com/a', 'https://example.com/b']})
check('more seeds frees it once more', 'vdbbin' not in e.still_barren())

# SWAPPING a seed frees it too, though the count is unchanged.
#
# The rule used to compare counts, so replacing a seed that yielded nothing
# with one that might left the tool set aside -- and that is precisely the
# intervention most worth retrying for. It also drifted: unrelated attempts
# accumulated until an attempt-count comparison re-trapped rasm2 and rahash2
# while they held 29 and 30 passages between them.
# The first refresh after a reseed REBASES the counter and leaves the tool
# eligible; it does not set it aside. Setting aside needs real attempts
# after that point and a later refresh. Getting this sequence wrong is what
# the drift bug looked like from the outside.
e.refresh_barren()
check('a reseed rebases rather than setting aside',
      'vdbbin' not in e.still_barren())
e.LIVE_LOG.write_text(chr(10).join(lines + extra * 3), encoding='utf-8')
e.refresh_barren()
check('set aside again after a fresh run on the new seeds',
      'vdbbin' in e.still_barren())
write_seeds({'vdbbin': ['https://example.com/a', 'https://example.com/OTHER']})
check('swapping a seed frees it, though the count is unchanged',
      'vdbbin' not in e.still_barren())

print('\n%d/%d passed' % (sum(ok), len(ok)))
sys.exit(0 if all(ok) else 1)
