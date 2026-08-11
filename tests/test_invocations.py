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
    # A Windows drive root, not a line continuation. Testing for a bare
    # trailing backslash dropped this whole, valid command.
    ("clamscan", "clamscan.exe --recursive C:" + chr(92)),
    ("dd", "dd if=/dev/sda of=/dev/sdb"),
    ("dd", "dd if=/dev/zero of=/dev/hda bs=4K conv=noerror,sync"),
    ("dcfldd", 'dcfldd pattern="00FFAACC" of=/dev/sda'),
    ("md5sum", "md5sum -c files.md5"),
    # One bracketed group, nested: a real command, not a synopsis.
    ("xlmdeobfuscator",
     'xlmdeobfuscator --file d.xlsm --output-formula-format "[[INT-FORMULA]]"'),
    # A # with no space before it is part of the filename, not a comment.
    ("pdf-parser", "pdf-parser.py -o 16 Project#1542292355.pdf"),
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
    # The tool's own OUTPUT. Both of these were extracted and then captioned
    # with confident nonsense -- "Create forensic image of log file and
    # verify integrity" for a startup banner -- which is exactly the
    # authoritative-looking fake command this project exists to avoid.
    ("dc3dd", "dc3dd 7.2.646 started at 2018-12-01 13:37:20 -0500"),
    ("affcat", "affcat version 3.7.22"),
    ("ewfinfo", "ewfinfo 20140608"),
    # A prose parenthetical standing in for the arguments.
    ("mergecap", "mergecap -F (different options)"),
    # Truncated dd commands, where the device name was markup the text
    # extraction dropped. Both were captioned as wipes -- "Securely erase
    # drive data", "Wipe drive data with zeros". Half a destructive command
    # under a confident caption is the worst thing this guide could print.
    ("dd", "dd if=/dev/"),
    ("dd", "dd if=/dev/zero of=/dev/"),
    # Spacing mangled by the same extraction.
    ("dd", "dd if = /dev /sda2 of=~/hdadisk.img"),
    # Truncated mid-line, not only at the end.
    ("dd", "dd if=/home/u/linux_image.dd of=/dev/ conv=notrunc,noerror"),
    # A page title, where the giveaway is the proper noun after the bar.
    ("md5sum", "md5sum Linux Command (10 Examples) | phoenixNAP KB"),
    # Man-page notation rather than a command: bracketed options, and the
    # optional-suffix and placeholder-operand forms manuals use.
    ("readelf", "readelf [opts] <elf>"),
    ("xxd", "xxd -h[elp]"),
    # A bare -v with nothing to act on: version on readelf, verbose
    # elsewhere, and useless as a worked example either way. It was
    # captioned "Display notes from binary file", which is neither.
    ("readelf", "readelf -v"),
    ("xxd", "xxd -s +seek"),
    # Every operand a placeholder: a synopsis whatever bracket style it
    # uses. Distinct from `ewfmount image.E01 <folder>` in KEEP, which
    # names a real file and generalises one argument.
    ("olemeta", "olemeta <file>"),
    ("hydra", "hydra [ options ] <target> <service>"),
    # Two or more bracketed groups is a synopsis. The all-placeholder
    # rule misses it because "[-m" and "MAX-LEN]" are separate tokens.
    ("xortool", "xortool [-x] [-m MAX-LEN] [-f] [-t CHARSET] [FILE]"),
    # A tool listing, where the colon separates name from description.
    ("msodde",
     "msodde : to detect and extract DDE links from MS Office documents"),
    ("xxd", "xxd -s seek ,"),
    # A line continuation: the command is cut off, and half a command that
    # looks whole is worse than none.
    ("evtxexport", "evtxexport -p p1/ -s p1/config/SYSTEM " + chr(92)),
]

# Repaired rather than dropped: a split ran the heading into the command and
# doubled the tool's name. Running it would open the tool's name as a file.
REPAIR = [
    # Prose and shell noise the text extraction glued onto the end.
    ("rasm2", "rasm2 -a x86 -b 32 'mov eax, 33' Disassemble opcode:",
     "rasm2 -a x86 -b 32 'mov eax, 33'"),
    ("rahash2", "rahash2 -S 12333 -E ror -s hello && echo Cell{",
     "rahash2 -S 12333 -E ror -s hello"),
    # A real command that names one argument generically. NOT a synopsis --
    # this guide does the same with {{path/to/image.dd}}.
    ("ewfmount", "ewfmount image.E01 <folder>",
     "ewfmount image.E01 <folder>"),
    # A man page's own section headings run into the command.
    ("rasm2",
     "rasm2 -d 90 See Also radare2(1) Authors pancake <p@nopcode.org>",
     "rasm2 -d 90"),
    # A section heading and the script beneath it run into the command.
    ("ffind",
     'ffind -o 2048 "$EVIDENCE" 12345 Scripting a Complete Analysis #!/bin/sh',
     'ffind -o 2048 "$EVIDENCE" 12345'),
    # A cheat sheet's own inline caption, which would be pasted along with
    # the command.
    ("hashcat", "hashcat -m 100 hashes.txt wordlist.txt #SHA1",
     "hashcat -m 100 hashes.txt wordlist.txt"),
    ("EvtxECmd", "EvtxECmd.exe --sync # update 700+ community maps first",
     "EvtxECmd.exe --sync"),
    # HTML tokenisation split the home shortcut from its path. Pasted as-is
    # this runs against the home directory and an unrelated absolute path.
    ("regipy-dump", "regipy-dump ~ /Documents/Evidence/NTUSER.DAT -o /tmp/o.json",
     "regipy-dump ~/Documents/Evidence/NTUSER.DAT -o /tmp/o.json"),
    ("evtxexport",
     "evtxexport evtxexport -p c/ -r c/Windows/System32/config/ f.evtx",
     "evtxexport -p c/ -r c/Windows/System32/config/ f.evtx"),
]

ok = []


def check(name, cond):
    # bool(), because `got and got[0] == want` yields the empty LIST when
    # got is empty, and summing those at the end raised TypeError -- the
    # test harness crashed instead of reporting the failure it had found.
    cond = bool(cond)
    ok.append(cond)
    print(('PASS  ' if cond else 'FAIL  ') + name)


for tool, line in KEEP:
    got = inv.candidate_lines(line, tool)
    check('keep  %-52s' % line[:52], len(got) == 1)

for tool, line in DROP:
    got = inv.candidate_lines(line, tool)
    check('drop  %-52s' % line[:52], not got)

for tool, line, want in REPAIR:
    got = inv.candidate_lines(line, tool)
    check('fix   %-52s' % line[:52], got and got[0] == want)

# Entities must be decoded, not merely tolerated -- a command containing
# &quot; does not run when pasted.
got = inv.candidate_lines('mactime -b &quot;body.txt&quot; -d', 'mactime')
check('html entities decoded', got and '&quot;' not in got[0] and '"' in got[0])

# Hex entities too, not just the named ones -- a hand-written table handled
# &quot; and missed &#x3C;, so a command shipped with the entity still in it.
got = inv.candidate_lines(
    'ewfmount image.E01 &#x3C;folder> " title="Copy code" aria-label="Copy"',
    'ewfmount')
check('hex entity decoded, markup stripped',
      got and got[0] == 'ewfmount image.E01 <folder>')

# A trailing gloss is cut, the command kept.
got = inv.candidate_lines('icat image.dd 1234 > out.bin  →  extract by inode',
                          'icat')
check('trailing gloss removed', got and '→' not in got[0] and 'out.bin' in got[0])

print('\n%d/%d passed' % (sum(ok), len(ok)))
sys.exit(0 if all(ok) else 1)
