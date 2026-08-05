"""Only real command lines survive extraction.

Every string here was produced by an earlier draft of candidate_lines from a
real retrieved page. The KEEP list is what a reader should be able to copy
into a terminal; the DROP list is what the first drafts let through -- prose
beginning with the tool name, a table row, a heading with a shell prompt
spliced into it, and HTML entities that would break the command if pasted.
"""
import os
import sys

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(R, 'scripts'))
import invocations as inv  # noqa: E402

KEEP = [
    ("mactime", "mactime -b body.txt -d > timeline.csv"),
    ("mactime", 'mactime -b "$OUTPUT/body.txt" -d -z UTC > "$OUTPUT/t.csv"'),
    ("icat", 'icat -o 2048 "$EVIDENCE" 12345 | md5sum'),
    ("icat", "icat image.dd 1234 > recovered_file.txt"),
    ("ngrep", "ngrep -wi -d any 'user|pass' port 21"),
    ("tcpflow", "tcpflow -e scan_http -o outdir host sundown"),
    ("tcpflow", "tcpflow -a -o outdir -Fk -r packets.pcap"),
    ("fls", "fls -rp -o 2048 image.dd"),
]

DROP = [
    # prose that happens to start with the tool name
    ("icat", "icat extracts file contents by inode; useful when gone"),
    ("mactime", "mactime -- Parses The Sleuth Kit mactime bodyfiles."),
    ("tcpflow", "tcpflow does not understand 802.11 headers."),
    # navigation / table furniture
    ("tcpflow", "tcpflow | Kali Linux Tools"),
    # a heading with a shell prompt spliced in
    ("tcpflow", "tcpflow TCP flow recorder root@kali:~# tcpflow -h"),
    # repeated name, no substance
    ("tcpflow", "tcpflow tcpflow tcpflow"),
    # installation, not usage
    ("ngrep", "sudo apt install ngrep"),
    # bare invocation teaches nothing
    ("fls", "fls"),
]

ok = []


def check(name, cond):
    ok.append(cond)
    print(('PASS  ' if cond else 'FAIL  ') + name)


for tool, line in KEEP:
    got = inv.candidate_lines(line, tool)
    check('keep  %-52s' % line[:52], len(got) == 1)

for tool, line in DROP:
    got = inv.candidate_lines(line, tool)
    check('drop  %-52s' % line[:52], not got)

# Entities must be decoded, not merely tolerated -- a command containing
# &quot; does not run when pasted.
got = inv.candidate_lines('mactime -b &quot;body.txt&quot; -d', 'mactime')
check('html entities decoded', got and '&quot;' not in got[0] and '"' in got[0])

# A trailing gloss is cut, the command kept.
got = inv.candidate_lines('icat image.dd 1234 > out.bin  →  extract by inode',
                          'icat')
check('trailing gloss removed', got and '→' not in got[0] and 'out.bin' in got[0])

print('\n%d/%d passed' % (sum(ok), len(ok)))
sys.exit(0 if all(ok) else 1)
