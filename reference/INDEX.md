# Capability Index

**Start here when you have a problem.** Find what you need to *do*; it points you at the tool and its page.

Phases follow [NIST SP 800-86](https://csrc.nist.gov/pubs/sp/800/86/final) (collect → examine → analyse → report), ordered the way an investigation actually runs.

Legend: **bold** = captured from a real binary, page can be written · plain = in the kit but not captured yet (needs a booted VM or has no CLI).

## Phases

- [Acquire & preserve](#acquire-preserve)
- [Examine the filesystem](#examine-the-filesystem)
- [Build the timeline](#build-the-timeline)
- [Windows artifacts](#windows-artifacts)
- [Memory forensics](#memory-forensics)
- [Network analysis](#network-analysis)
- [Malware triage — static](#malware-triage-static)
- [Malware triage — documents](#malware-triage-documents)
- [Reverse engineering](#reverse-engineering)
- [Decode & deobfuscate](#decode-deobfuscate)
- [Report & support](#report-support)


## Acquire & preserve

### Image a disk, volume or device

[**dd**](acquire-preserve/dd.md), `dc3dd`, `dcfldd`, `ewfacquire`, `guymager`, `affconvert`

### Verify evidence integrity with hashes

[**rahash2**](acquire-preserve/rahash2.md), [**ssdeep**](acquire-preserve/ssdeep.md), [**sha256sum**](acquire-preserve/sha256sum.md), [**md5sum**](acquire-preserve/md5sum.md), [**sigtool**](acquire-preserve/sigtool.md), `hashdeep`, `md5deep`, `sha256deep`

### Inspect or mount a forensic image container

[**img_stat**](acquire-preserve/img_stat.md), [**ntfs-3g**](acquire-preserve/ntfs-3g.md), [**vshadowinfo**](acquire-preserve/vshadowinfo.md), [**bdeinfo**](acquire-preserve/bdeinfo.md), `ewfinfo`, `ewfmount`, `ewfverify`, `ewfexport`, `affinfo`, `affcat`

### Capture live network traffic

[**dumpcap**](acquire-preserve/dumpcap.md), [**tshark**](acquire-preserve/tshark.md), `tcpdump`


## Examine the filesystem

### See the partition and volume layout

[**mmls**](examine-the-filesystem/mmls.md), [**fsstat**](examine-the-filesystem/fsstat.md), [**img_stat**](acquire-preserve/img_stat.md), [**testdisk**](examine-the-filesystem/testdisk.md)

### List files and directories, including deleted ones

[**fls**](examine-the-filesystem/fls.md), [**ffind**](examine-the-filesystem/ffind.md), [**ils**](examine-the-filesystem/ils.md), [**tsk_recover**](examine-the-filesystem/tsk_recover.md)

### Recover deleted or lost files

[**tsk_recover**](examine-the-filesystem/tsk_recover.md), [**icat**](examine-the-filesystem/icat.md), [**photorec**](examine-the-filesystem/photorec.md), [**testdisk**](examine-the-filesystem/testdisk.md), [**blkls**](examine-the-filesystem/blkls.md), `ext4magic`, `extundelete`, `ext3grep`

### Carve files out of unstructured data

[**foremost**](examine-the-filesystem/foremost.md), [**scalpel**](examine-the-filesystem/scalpel.md), [**binwalk**](examine-the-filesystem/binwalk.md), [**tcpxtract**](examine-the-filesystem/tcpxtract.md), `bulk_extractor`, `magicrescue`

### Inspect metadata for one file or inode

[**istat**](examine-the-filesystem/istat.md), [**ils**](examine-the-filesystem/ils.md), [**file**](examine-the-filesystem/file.md), [**stat**](examine-the-filesystem/stat.md), `exiftool`, `trid`, `magika`

### Search raw data for a pattern

[**rafind2**](examine-the-filesystem/rafind2.md), [**strings**](examine-the-filesystem/strings.md), [**grep**](examine-the-filesystem/grep.md), [**xxd**](examine-the-filesystem/xxd.md), `lightgrep`, `bulk_extractor`


## Build the timeline

### Build a super-timeline from many artifact sources

[**log2timeline.py**](build-the-timeline/log2timeline.py.md), [**psort.py**](build-the-timeline/psort.py.md), [**pinfo.py**](build-the-timeline/pinfo.py.md), `psteal.py`

### Build a filesystem MAC-time timeline

[**fls**](examine-the-filesystem/fls.md), [**mactime**](build-the-timeline/mactime.md), [**tsk_gettimes**](build-the-timeline/tsk_gettimes.md)


## Windows artifacts

### Parse registry hives

[**rip.pl**](windows-artifacts/rip.pl.md), [**regripper**](windows-artifacts/regripper.md), [**hivexsh**](windows-artifacts/hivexsh.md), [**regfexport**](windows-artifacts/regfexport.md), [**regfinfo**](windows-artifacts/regfinfo.md), [**regfmount**](windows-artifacts/regfmount.md), [**regipy-dump**](windows-artifacts/regipy-dump.md), [**regipy-parse-header**](windows-artifacts/regipy-parse-header.md), [**regipy-plugins-run**](windows-artifacts/regipy-plugins-run.md), [**regipy-diff**](windows-artifacts/regipy-diff.md), [**RECmd**](windows-artifacts/RECmd.md), `hivexget`, `hivexml`

### Parse Windows event logs

[**evtxexport**](windows-artifacts/evtxexport.md), [**evtxinfo**](windows-artifacts/evtxinfo.md), [**EvtxECmd**](windows-artifacts/EvtxECmd.md), [**chainsaw**](windows-artifacts/chainsaw.md), [**hayabusa**](windows-artifacts/hayabusa.md), `evtx_dump`

### Parse ESE / SRUM / Amcache databases

[**esedbexport**](windows-artifacts/esedbexport.md), [**esedbinfo**](windows-artifacts/esedbinfo.md), [**SrumECmd**](windows-artifacts/SrumECmd.md), [**AmcacheParser**](windows-artifacts/AmcacheParser.md)

### Parse execution and persistence artifacts

[**PECmd**](windows-artifacts/PECmd.md), [**AppCompatCacheParser**](windows-artifacts/AppCompatCacheParser.md), [**MFTECmd**](windows-artifacts/MFTECmd.md), [**AmcacheParser**](windows-artifacts/AmcacheParser.md), `analyzeMFT`

### Parse mail stores

`pffexport`, `pffinfo`, `readpst`


## Memory forensics

### Analyse a memory image

[**vol**](memory-forensics/vol.md), [**volatility3**](memory-forensics/volatility3.md), [**volshell**](memory-forensics/volshell.md), `vol.py`, `rekall`

### Recover encryption keys from memory

[**aeskeyfind**](memory-forensics/aeskeyfind.md), [**rsakeyfind**](memory-forensics/rsakeyfind.md), `bulk_extractor`


## Network analysis

### Read and filter packet captures

[**tshark**](acquire-preserve/tshark.md), [**capinfos**](network-analysis/capinfos.md), [**ngrep**](network-analysis/ngrep.md), [**tcpflow**](network-analysis/tcpflow.md)

### Split, merge or repair capture files

[**editcap**](network-analysis/editcap.md), [**mergecap**](network-analysis/mergecap.md), [**reordercap**](network-analysis/reordercap.md)

### Extract files and payloads from traffic

[**tcpxtract**](examine-the-filesystem/tcpxtract.md), [**tcpflow**](network-analysis/tcpflow.md), [**foremost**](examine-the-filesystem/foremost.md)

### Detect intrusions in traffic

`suricata`, `suricatasc`, `zeek`, `zeek-cut`, `rita`

### Probe or scan hosts and services

[**nmap**](network-analysis/nmap.md), [**nping**](network-analysis/nping.md), `ncat`, `arp-scan`, `netdiscover`

### Simulate network services for detonation

[**inetsim**](network-analysis/inetsim.md), `fakedns`, `fakenet`


## Malware triage — static

### Identify what a file actually is

[**file**](examine-the-filesystem/file.md), [**die**](malware-triage-static/die.md), [**diec**](malware-triage-static/diec.md), `trid`, `magika`, `exiftool`

### Scan with signatures for known-bad

[**yara**](malware-triage-static/yara.md), [**yarac**](malware-triage-static/yarac.md), [**clamscan**](malware-triage-static/clamscan.md), [**freshclam**](malware-triage-static/freshclam.md), [**sigtool**](acquire-preserve/sigtool.md), `clamdscan`

### Identify capabilities in a binary

[**capa**](malware-triage-static/capa.md), [**floss**](malware-triage-static/floss.md)

### Extract strings, including obfuscated ones

[**floss**](malware-triage-static/floss.md), [**strings**](examine-the-filesystem/strings.md), [**base64dump.py**](malware-triage-static/base64dump.py.md), [**numbers-to-string.py**](malware-triage-static/numbers-to-string.py.md)

### Inspect PE / ELF structure

[**rabin2**](malware-triage-static/rabin2.md), [**readelf**](malware-triage-static/readelf.md), [**readelf.py**](malware-triage-static/readelf.py.md), [**objdump**](malware-triage-static/objdump.md), `pescan`, `pecheck.py`, `peframe`

### Detect and reverse packing

[**upx**](malware-triage-static/upx.md), [**die**](malware-triage-static/die.md), [**diec**](malware-triage-static/diec.md), [**binwalk**](examine-the-filesystem/binwalk.md), [**7za**](malware-triage-static/7za.md), [**unzip**](malware-triage-static/unzip.md)

### Compare or cluster samples

[**ssdeep**](acquire-preserve/ssdeep.md), [**radiff2**](malware-triage-static/radiff2.md), `bytehist`


## Malware triage — documents

### Analyse Office documents and macros

[**olevba**](malware-triage-documents/olevba.md), [**oleid**](malware-triage-documents/oleid.md), [**oledump.py**](malware-triage-documents/oledump.py.md), [**olemeta**](malware-triage-documents/olemeta.md), [**oletimes**](malware-triage-documents/oletimes.md), [**olemap**](malware-triage-documents/olemap.md), [**oledir**](malware-triage-documents/oledir.md), [**olebrowse**](malware-triage-documents/olebrowse.md), [**olefile**](malware-triage-documents/olefile.md), [**oleobj**](malware-triage-documents/oleobj.md), [**mraptor**](malware-triage-documents/mraptor.md), [**msodde**](malware-triage-documents/msodde.md), [**pcodedmp**](malware-triage-documents/pcodedmp.md), [**pyxswf**](malware-triage-documents/pyxswf.md), [**xlmdeobfuscator**](malware-triage-documents/xlmdeobfuscator.md), `runxlrd2.py`, `vipermonkey`

### Analyse RTF documents and embedded objects

[**rtfobj**](malware-triage-documents/rtfobj.md), [**oleobj**](malware-triage-documents/oleobj.md), `rtfdump.py`

### Analyse PDFs

[**pdfid**](malware-triage-documents/pdfid.md), [**pdfid.py**](malware-triage-documents/pdfid.py.md), [**pdf-parser**](malware-triage-documents/pdf-parser.md), [**pdf-parser.py**](malware-triage-documents/pdf-parser.py.md), `peepdf`, `qpdf`

### Analyse other container formats

[**7za**](malware-triage-static/7za.md), [**unzip**](malware-triage-static/unzip.md), [**msoffcrypto-tool**](malware-triage-documents/msoffcrypto-tool.md), `onenoteanalyzer`


## Reverse engineering

### Disassemble and explore a binary

[**r2**](reverse-engineering/r2.md), [**rabin2**](malware-triage-static/rabin2.md), [**rasm2**](reverse-engineering/rasm2.md), [**objdump**](malware-triage-static/objdump.md), [**vivbin**](reverse-engineering/vivbin.md), [**vdbbin**](reverse-engineering/vdbbin.md), `rizin`, `ghidra`, `cutter`

### Diff two binaries

[**radiff2**](malware-triage-static/radiff2.md), `bindiff`

### Emulate or instrument execution

[**frida**](reverse-engineering/frida.md), [**frida-trace**](reverse-engineering/frida-trace.md), [**frida-ps**](reverse-engineering/frida-ps.md), [**frida-discover**](reverse-engineering/frida-discover.md), [**frida-kill**](reverse-engineering/frida-kill.md), [**frida-ls-devices**](reverse-engineering/frida-ls-devices.md), `speakeasy`, `qiling`, `scdbg`, `unicorn`

### Analyse shellcode

[**rasm2**](reverse-engineering/rasm2.md), [**xortool**](reverse-engineering/xortool.md), `scdbg`, `shellcode2exe`


## Decode & deobfuscate

### Decode, decrypt or transform encoded data

[**cyberchef**](decode-deobfuscate/cyberchef.md), [**base64dump.py**](malware-triage-static/base64dump.py.md), [**rax2**](decode-deobfuscate/rax2.md), [**xxd**](examine-the-filesystem/xxd.md), [**openssl**](decode-deobfuscate/openssl.md), [**numbers-to-string.py**](malware-triage-static/numbers-to-string.py.md)

### Break simple obfuscation

[**xortool**](reverse-engineering/xortool.md), [**floss**](malware-triage-static/floss.md), [**xlmdeobfuscator**](malware-triage-documents/xlmdeobfuscator.md), `de4dot`

### Crack passwords and hashes

[**hashcat**](decode-deobfuscate/hashcat.md), [**john**](decode-deobfuscate/john.md), [**hydra**](decode-deobfuscate/hydra.md), `unshadow`, `zip2john`, `rar2john`, `fcrackzip`, `hashid`

### Find hidden data

[**binwalk**](examine-the-filesystem/binwalk.md), [**ssdeep**](acquire-preserve/ssdeep.md), `steghide`, `stegosuite`


## Report & support

### Fetch and verify external references

[**curl**](report-support/curl.md), [**wget**](report-support/wget.md)

### Inspect files by hand

[**xxd**](examine-the-filesystem/xxd.md), [**ezhexviewer**](report-support/ezhexviewer.md), [**less**](report-support/less.md), `hexdump`


---

## Coverage of this index

- **46 capabilities** across 11 phases
- **135 captured tools** are reachable through a capability
- **0 named kit tools map to no capability** (below)
- **2 capabilities have no captured tool** behind them yet

### Capabilities with nothing captured yet

These are real needs the kit may cover with GUI or Windows-only tools that a Linux container cannot capture.

- Windows artifacts / Parse mail stores
- Network analysis / Detect intrusions in traffic

### Named kit tools not yet mapped to a capability

These are named in the kit manifests, captured from a real binary, and reach no capability in this index. Each is a taxonomy gap to close or an explicit out-of-scope decision. Listed rather than silently dropped, because a missing capability is otherwise invisible.

_none_

### Container-provided commands (not named in the kit manifests)

Discovered by walking the container's `PATH`. They ship in a kit image but no kit manifest names them, so the great majority is OS plumbing rather than investigative tooling. Kept for completeness only.

<details><summary>796 container-provided commands</summary>

`2to3`, `7z`, `7zr`, `JLECmd`, `LECmd`, `RBCmd`, `RecentFileCacheParser`, `SBECmd`, `SumECmd`, `WxTCmd`, `XORSearch`, `add-shell`, `addgroup`, `addpart`, `addr2line`, `adduser`, `agetty`, `appcompat`, `apt`, `apt-cache`, `apt-cdrom`, `apt-config`, `apt-get`, `apt-key`, `apt-mark`, `ar`, `arch`, `arpd`, `as`, `asan_symbolize-15`, `awk`, `b2sum`, `badblocks`, `base32`, `base64`, `base64dump`, `basename`, `basenc`, `bashbug`, `bdemount`, `blkcalc`, `blkcat`, `blkdiscard`, `blkid`, `blkstat`, `blkzone`, `blockdev`, `bridge`, `bstrings`, `bunzip2`, `bzcat`, `bzip2`, `bzip2recover`, `bzless`, `bzmore`, `c++`, `c++filt`, `c89`, `c89-gcc`, `c99`, `c99-gcc`, `c_rehash`, `capa-offline`, `capsh`, `captoinfo`, `captype`, `cat`, `cc`, `cffi-gen-src`, `chage`, `chcon`, `chcpu`, `chfn`, `chgpasswd`, `chgrp`, `chmem`, `chmod`, `choom`, `chown`, `chpasswd`, `chroot`, `chrt`, `chsh`, `cksum`, `clambc`, `clamsubmit`, `clang++-15`, `clang-15`, `clang-cpp-15`, `clang-format-radare2`, `clear`, `clear_console`, `cmp`, `comm`, `corelist`, `cp`, `cpan`, `cpan5.36-x86_64-linux-gnu`, `cpgr`, `cpp`, `cpp-12`, `cppw`, `crontab`, `csplit`, `ctrlaltdel`, `ctstat`, `cut`, `cvtsudoers`, `date`, `dcb`, `deb-systemd-helper`, `debconf`, `debconf-communicate`, `debconf-copydb`, `debconf-escape`, `debconf-set-selections`, `debconf-show`, `debugfs`, `delgroup`, `delpart`, `deluser`, `delv`, `devlink`, `df`, `dfir`, `dh_perl_openssl`, `diel`, `diff`, `diff3`, `dig`, `dir`, `dircolors`, `dirmngr`, `dirmngr-client`, `dirname`, `dmesg`, `dnsdomainname`, `dnstap-read`, `domainname`, `dpkg`, `dpkg-architecture`, `dpkg-buildflags`, `dpkg-buildpackage`, `dpkg-checkbuilddeps`, `dpkg-deb`, `dpkg-distaddfile`, `dpkg-divert`, `dpkg-genbuildinfo`, `dpkg-genchanges`, `dpkg-gencontrol`, `dpkg-gensymbols`, `dpkg-maintscript-helper`, `dpkg-mergechangelogs`, `dpkg-name`, `dpkg-parsechangelog`, `dpkg-preconfigure`, `dpkg-query`, `dpkg-realpath`, `dpkg-reconfigure`, `dpkg-scanpackages`, `dpkg-scansources`, `dpkg-shlibdeps`, `dpkg-source`, `dpkg-split`, `dpkg-statoverride`, `dpkg-trigger`, `dpkg-vendor`, `dpl4hydra`, `du`, `dumpe2fs`, `dwp`, `e2fsck`, `e2image`, `e2scrub`, `e2scrub_all`, `e2undo`, `e4crypt`, `e4defrag`, `easy_install-2.7`, `echo`, `editor`, `egrep`, `elfedit`, `emldump`, `enc2xs`, `encguess`, `ex`, `expand`, `expiry`, `expr`, `factor`, `faillog`, `fallocate`, `false`, `fc-cache`, `fc-cat`, `fc-conflist`, `fc-list`, `fc-match`, `fc-pattern`, `fc-query`, `fc-scan`, `fc-validate`, `fcat`, `fgrep`, `fidentify`, `fincore`, `find`, `findfs`, `findmnt`, `fiwalk`, `flock`, `fmt`, `fold`, `free`, `frida-apk`, `frida-compile`, `frida-create`, `frida-itrace`, `frida-join`, `frida-ls`, `frida-pm`, `frida-pull`, `frida-push`, `frida-rm`, `frida-strace`, `fsck`, `fsck.cramfs`, `fsck.ext2`, `fsck.ext3`, `fsck.ext4`, `fsck.minix`, `fsfreeze`, `fstrim`, `ftguess`, `fusermount`, `fusermount3`, `g++-12`, `gcc-12`, `gcc-ar`, `gcc-ar-12`, `gcc-nm`, `gcc-nm-12`, `gcc-ranlib`, `gcc-ranlib-12`, `gcov`, `gcov-12`, `gcov-dump`, `gcov-dump-12`, `gcov-tool`, `gcov-tool-12`, `gencat`, `genl`, `getcap`, `getconf`, `getent`, `getopt`, `getpcaps`, `getty`, `git`, `git-receive-pack`, `git-upload-archive`, `git-upload-pack`, `gmake`, `gold`, `gp-archive`, `gp-collect-app`, `gp-display-html`, `gp-display-src`, `gp-display-text`, `gpasswd`, `gpg`, `gpg-agent`, `gpg-connect-agent`, `gpg-wks-server`, `gpg-zip`, `gpgcompose`, `gpgconf`, `gpgparsemail`, `gpgsm`, `gpgsplit`, `gpgtar`, `gpgv`, `gprof`, `gprofng`, `groupadd`, `groupdel`, `groupmems`, `groupmod`, `groups`, `grpck`, `grpconv`, `grpunconv`, `gunzip`, `gzexe`, `gzip`, `h2ph`, `h2xs`, `hardlink`, `hcli`, `head`, `hfind`, `host`, `hostid`, `hostname`, `httpx`, `hwclock`, `i386`, `iconv`, `iconvconfig`, `id`, `ida-hcli`, `idna`, `ifind`, `img_cat`, `infocmp`, `infotocap`, `install`, `instmodsh`, `invoke-rc.d`, `ionice`, `ip`, `ipcmk`, `ipcrm`, `ipcs`, `ischroot`, `isosize`, `jcat`, `jls`, `join`, `json_pp`, `kbxutil`, `kill`, `last`, `lastb`, `lastlog`, `lcf`, `ld`, `ld.bfd`, `ld.gold`, `ld.so`, `ldattach`, `ldconfig`, `ldd`, `libnetcfg`, `link`, `linux32`, `linux64`, `ln`, `lnstat`, `locale`, `localedef`, `log2timeline`, `logger`, `logname`, `logrotate`, `logsave`, `losetup`, `lowntfs-3g`, `ls`, `lsattr`, `lsblk`, `lscpu`, `lsfd`, `lsipc`, `lsirq`, `lslocks`, `lslogins`, `lsmem`, `lsns`, `lspgpot`, `lto-dump`, `lto-dump-12`, `lzcat`, `lzcmp`, `lzdiff`, `lzegrep`, `lzfgrep`, `lzgrep`, `lzless`, `lzma`, `lzmainfo`, `lzmore`, `markdown-it`, `mawk`, `mcookie`, `md5sum.textutils`, `mdig`, `mesg`, `migrate-pubring-from-classic-gpg`, `mkdir`, `mke2fs`, `mkfifo`, `mkfs`, `mkfs.bfs`, `mkfs.cramfs`, `mkfs.ext2`, `mkfs.ext3`, `mkfs.ext4`, `mkfs.minix`, `mkfs.ntfs`, `mknod`, `mkntfs`, `mkswap`, `mktemp`, `mmcat`, `mmstat`, `more`, `mount`, `mount.lowntfs-3g`, `mount.ntfs`, `mount.ntfs-3g`, `mountpoint`, `mv`, `namei`, `nawk`, `ncurses5-config`, `ncurses6-config`, `ncursesw5-config`, `ncursesw6-config`, `net-server`, `newusers`, `nice`, `nisdomainname`, `nl`, `nm`, `nohup`, `nproc`, `nsenter`, `nslookup`, `nstat`, `nsupdate`, `ntfs-3g.probe`, `ntfscat`, `ntfsclone`, `ntfscluster`, `ntfscmp`, `ntfscp`, `ntfsdecrypt`, `ntfsfallocate`, `ntfsfix`, `ntfsinfo`, `ntfslabel`, `ntfsls`, `ntfsmove`, `ntfsrecover`, `ntfsresize`, `ntfssecaudit`, `ntfstruncate`, `ntfsundelete`, `ntfsusermap`, `ntfswipe`, `numbers-to-hex.py`, `numfmt`, `objcopy`, `od`, `oledump`, `p7zip`, `pager`, `partx`, `passwd`, `paste`, `pathchk`, `pdb3`, `pdb3.11`, `pdfattach`, `pdfdetach`, `pdffonts`, `pdfimages`, `pdfinfo`, `pdfseparate`, `pdfsig`, `pdftocairo`, `pdftohtml`, `pdftoppm`, `pdftops`, `pdftotext`, `pdfunite`, `perl5.36-x86_64-linux-gnu`, `perl5.36.0`, `perlbug`, `perlivp`, `perlthanks`, `pgrep`, `piconv`, `pidof`, `pidwait`, `pinentry`, `pinentry-curses`, `pinfo`, `pinky`, `pip2.7`, `pip3.11`, `pivot_root`, `pkgconf`, `pkill`, `pldd`, `pmap`, `pod2html`, `pod2man`, `pod2text`, `pod2usage`, `podchecker`, `pr`, `prefetch`, `printenv`, `printf`, `prlimit`, `prove`, `ps`, `psort`, `pstat`, `ptar`, `ptardiff`, `ptargrep`, `ptx`, `pw-inspector`, `pwck`, `pwconv`, `pwd`, `pwdx`, `pwunconv`, `py3clean`, `py3compile`, `py3versions`, `pydoc`, `pydoc3`, `pydoc3.11`, `pygettext3`, `pygettext3.11`, `pygmentize`, `python2`, `python2.7`, `python3-config`, `python3.11`, `python3.11-config`, `r2agent`, `r2pm`, `r2r`, `r2sdb`, `radare2`, `rafs2`, `ragg2`, `randpkt`, `ranlib`, `rapatch2`, `rarun2`, `rasign2`, `ravc2`, `rawshark`, `rbash`, `rdma`, `readlink`, `readprofile`, `realpath`, `regipy-plugins-list`, `regipy-process-transaction-logs`, `remove-shell`, `rename.ul`, `renice`, `reset`, `resize2fs`, `resizepart`, `rev`, `rgrep`, `rich-click`, `rm`, `rmdir`, `rmt`, `rmt-tar`, `roman`, `routel`, `rpcgen`, `rtcwake`, `rtmon`, `rtstat`, `run-parts`, `runcon`, `runuser`, `rview`, `savelog`, `scalar`, `sccainfo`, `script`, `scriptlive`, `scriptreplay`, `sdiff`, `sed`, `sensible-editor`, `sensible-pager`, `seq`, `setarch`, `setcap`, `setpriv`, `setsid`, `setterm`, `sha1sum`, `sha224sum`, `sha384sum`, `sha512sum`, `sharkd`, `shasum`, `shred`, `shuf`, `sigfind`, `size`, `skill`, `slabtop`, `sleep`, `smtpd.py`, `snice`, `sort`, `sorter`, `splain`, `split`, `srch_strings`, `ss`, `start-stop-daemon`, `stdbuf`, `streamzip`, `strip`, `stty`, `su`, `sudo_logsrvd`, `sudo_sendlog`, `sudoedit`, `sudoreplay`, `sulogin`, `sum`, `swaplabel`, `swapoff`, `swapon`, `switch_root`, `sync`, `sysctl`, `tabs`, `tabulate`, `tac`, `tail`, `tar`, `tarcat`, `taskset`, `tc`, `tee`, `tempfile`, `text2pcap`, `tic`, `timeout`, `tload`, `top`, `touch`, `tput`, `tqdm`, `tr`, `true`, `truncate`, `tset`, `tsk_comparedir`, `tsk_imageinfo`, `tsk_loaddb`, `tsort`, `tty`, `tune2fs`, `tzselect`, `ucf`, `ucfq`, `ucfr`, `uclampset`, `umount`, `uname`, `uncompress`, `unexpand`, `uniq`, `unlink`, `unlzma`, `unshare`, `unxz`, `unzipsfx`, `update-alternatives`, `update-ca-certificates`, `update-catalog`, `update-locale`, `update-passwd`, `update-rc.d`, `update-shells`, `uptime`, `useradd`, `userdel`, `usermod`, `users`, `usnjls`, `utmpdump`, `vdir`, `vdpa`, `vi`, `view`, `vigr`, `vim.tiny`, `vipw`, `visudo`, `vivserver`, `vmstat`, `vshadowdebug`, `vshadowmount`, `w`, `wall`, `watch`, `watchgnupg`, `wc`, `wdctl`, `wheel`, `whereis`, `who`, `whoami`, `wipefs`, `x86_64`, `x86_64-linux-gnu-addr2line`, `x86_64-linux-gnu-ar`, `x86_64-linux-gnu-as`, `x86_64-linux-gnu-c++filt`, `x86_64-linux-gnu-cpp`, `x86_64-linux-gnu-cpp-12`, `x86_64-linux-gnu-dwp`, `x86_64-linux-gnu-elfedit`, `x86_64-linux-gnu-g++`, `x86_64-linux-gnu-g++-12`, `x86_64-linux-gnu-gcc`, `x86_64-linux-gnu-gcc-12`, `x86_64-linux-gnu-gcc-ar`, `x86_64-linux-gnu-gcc-ar-12`, `x86_64-linux-gnu-gcc-nm`, `x86_64-linux-gnu-gcc-nm-12`, `x86_64-linux-gnu-gcc-ranlib`, `x86_64-linux-gnu-gcc-ranlib-12`, `x86_64-linux-gnu-gcov`, `x86_64-linux-gnu-gcov-12`, `x86_64-linux-gnu-gcov-dump`, `x86_64-linux-gnu-gcov-dump-12`, `x86_64-linux-gnu-gcov-tool`, `x86_64-linux-gnu-gcov-tool-12`, `x86_64-linux-gnu-gold`, `x86_64-linux-gnu-gp-archive`, `x86_64-linux-gnu-gp-collect-app`, `x86_64-linux-gnu-gp-display-html`, `x86_64-linux-gnu-gp-display-src`, `x86_64-linux-gnu-gp-display-text`, `x86_64-linux-gnu-gprof`, `x86_64-linux-gnu-gprofng`, `x86_64-linux-gnu-ld`, `x86_64-linux-gnu-ld.bfd`, `x86_64-linux-gnu-ld.gold`, `x86_64-linux-gnu-lto-dump`, `x86_64-linux-gnu-lto-dump-12`, `x86_64-linux-gnu-nm`, `x86_64-linux-gnu-objcopy`, `x86_64-linux-gnu-objdump`, `x86_64-linux-gnu-pkg-config`, `x86_64-linux-gnu-pkgconf`, `x86_64-linux-gnu-python3-config`, `x86_64-linux-gnu-python3.11-config`, `x86_64-linux-gnu-ranlib`, `x86_64-linux-gnu-readelf`, `x86_64-linux-gnu-size`, `x86_64-linux-gnu-strings`, `x86_64-linux-gnu-strip`, `xargs`, `xortool-xor`, `xsubpp`, `xz`, `xzcat`, `xzcmp`, `xzdiff`, `xzegrep`, `xzfgrep`, `xzgrep`, `xzless`, `xzmore`, `yes`, `ypdomainname`, `zcat`, `zcmp`, `zdiff`, `zdump`, `zegrep`, `zfgrep`, `zforce`, `zgrep`, `zic`, `zipdetails`, `zipdump`, `zipgrep`, `zipinfo`, `zless`, `zmore`, `znew`, `zramctl`

</details>