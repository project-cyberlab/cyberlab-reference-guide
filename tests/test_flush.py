import json, os, sys, shutil, tempfile
R = os.path.join('C:', os.sep, 'Users', 'm808b', 'dev', 'cyberlab-reference-guide')
sys.path.insert(0, os.path.join(R, 'scripts'))
import enrich_loop as e

tmp = tempfile.mkdtemp()
e.OUT = __import__('pathlib').Path(tmp) / 'out.json'
e.REVIEW = __import__('pathlib').Path(tmp) / 'review.json'
e.MISSES = __import__('pathlib').Path(tmp) / 'miss.json'

ok = []


def check(name, cond):
    ok.append(cond)
    print(('PASS  ' if cond else 'FAIL  ') + name)


# 1. review is actually written -- the bug
res = [{'tool': 'fls', 'flag': None, 'top_score': 3}]
rev = [{'tool': 'istat', 'flag': None, 'top_score': 2}]
mis = [{'tool': 'ils', 'flag': '-m', 'top_score': 0}]
e.flush(res, rev, mis)
check('research_review.json is created at all', e.REVIEW.exists())
check('review record persisted', json.loads(e.REVIEW.read_text())[0]['tool'] == 'istat')

# 2. idempotent: flushing the same lists again must not duplicate
e.flush(res, rev, mis)
e.flush(res, rev, mis)
check('repeat flush does not duplicate (out)', len(json.loads(e.OUT.read_text())) == 1)
check('repeat flush does not duplicate (review)', len(json.loads(e.REVIEW.read_text())) == 1)

# 3. accumulating across tools keeps everything
res.append({'tool': 'mmls', 'flag': None, 'top_score': 5})
e.flush(res, rev, mis)
check('second tool accumulates', len(json.loads(e.OUT.read_text())) == 2)

# 4. better-evidenced attempt wins on dedup
e.flush([{'tool': 'fls', 'flag': None, 'top_score': 9}], [], [])
rows = {r['tool']: r for r in json.loads(e.OUT.read_text())}
check('higher top_score replaces lower', rows['fls']['top_score'] == 9)
check('lower score does not replace higher',
      (e.flush([{'tool': 'fls', 'flag': None, 'top_score': 1}], [], []) or
       {r['tool']: r for r in json.loads(e.OUT.read_text())}['fls']['top_score'] == 9))

# 5. --replace does not merge, and accumulation keeps prior tools in-run
e.flush([{'tool': 'a', 'flag': None, 'top_score': 1}], [], [], True)
e.flush([{'tool': 'a', 'flag': None, 'top_score': 1},
         {'tool': 'b', 'flag': None, 'top_score': 1}], [], [], True)
got = {r['tool'] for r in json.loads(e.OUT.read_text())}
check('replace mode keeps accumulated in-run tools', got == {'a', 'b'})

shutil.rmtree(tmp, ignore_errors=True)
print('\n%d/%d passed' % (sum(ok), len(ok)))
sys.exit(0 if all(ok) else 1)
