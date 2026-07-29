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

**dd**, `dc3dd`, `dcfldd`, `ewfacquire`, `guymager`, `affconvert`

### Verify evidence integrity with hashes

**rahash2**, **ssdeep**, **sha256sum**, **md5sum**, **sigtool**, `hashdeep`, `md5deep`, `sha256deep`

### Inspect or mount a forensic image container

**img_stat**, **ntfs-3g**, **vshadowinfo**, **bdeinfo**, `ewfinfo`, `ewfmount`, `ewfverify`, `ewfexport`, `affinfo`, `affcat`

### Capture live network traffic

**dumpcap**, **tshark**, `tcpdump`


## Examine the filesystem

### See the partition and volume layout

**mmls**, **fsstat**, **img_stat**, **testdisk**

### List files and directories, including deleted ones

[**fls**](filesystem-analysis/fls.md), **ffind**, **ils**, **tsk_recover**

### Recover deleted or lost files

**tsk_recover**, **icat**, **photorec**, **testdisk**, **blkls**, `ext4magic`, `extundelete`, `ext3grep`

### Carve files out of unstructured data

**foremost**, **scalpel**, **binwalk**, **tcpxtract**, `bulk_extractor`, `magicrescue`

### Inspect metadata for one file or inode

**istat**, **ils**, **file**, **stat**, `exiftool`, `trid`, `magika`

### Search raw data for a pattern

**rafind2**, **strings**, **grep**, **xxd**, `lightgrep`, `bulk_extractor`


## Build the timeline

### Build a super-timeline from many artifact sources

**log2timeline.py**, **psort.py**, **pinfo.py**, `psteal.py`

### Build a filesystem MAC-time timeline

[**fls**](filesystem-analysis/fls.md), **mactime**, **tsk_gettimes**


## Windows artifacts

### Parse registry hives

**rip.pl**, **regripper**, **hivexsh**, **regfexport**, **regfinfo**, **regfmount**, **regipy-dump**, **regipy-parse-header**, **regipy-plugins-run**, **regipy-diff**, **RECmd**, `hivexget`, `hivexml`

### Parse Windows event logs

**evtxexport**, **evtxinfo**, **EvtxECmd**, **chainsaw**, **hayabusa**, `evtx_dump`

### Parse ESE / SRUM / Amcache databases

**esedbexport**, **esedbinfo**, **SrumECmd**, **AmcacheParser**

### Parse execution and persistence artifacts

**PECmd**, **AppCompatCacheParser**, **MFTECmd**, **AmcacheParser**, `analyzeMFT`

### Parse mail stores

`pffexport`, `pffinfo`, `readpst`


## Memory forensics

### Analyse a memory image

**vol**, **volatility3**, **volshell**, `vol.py`, `rekall`

### Recover encryption keys from memory

**aeskeyfind**, **rsakeyfind**, `bulk_extractor`


## Network analysis

### Read and filter packet captures

**tshark**, **capinfos**, **ngrep**, **tcpflow**

### Split, merge or repair capture files

**editcap**, **mergecap**, **reordercap**

### Extract files and payloads from traffic

**tcpxtract**, **tcpflow**, **foremost**

### Detect intrusions in traffic

`suricata`, `suricatasc`, `zeek`, `zeek-cut`, `rita`

### Probe or scan hosts and services

**nmap**, **nping**, `ncat`, `arp-scan`, `netdiscover`

### Simulate network services for detonation

**inetsim**, `fakedns`, `fakenet`


## Malware triage — static

### Identify what a file actually is

**file**, **die**, **diec**, `trid`, `magika`, `exiftool`

### Scan with signatures for known-bad

**yara**, **yarac**, **clamscan**, **freshclam**, **sigtool**, `clamdscan`

### Identify capabilities in a binary

**capa**, **floss**

### Extract strings, including obfuscated ones

**floss**, **strings**, **base64dump.py**, **numbers-to-string.py**

### Inspect PE / ELF structure

**rabin2**, **readelf**, **readelf.py**, **objdump**, `pescan`, `pecheck.py`, `peframe`

### Detect and reverse packing

**upx**, **die**, **diec**, **binwalk**, **7za**, **unzip**

### Compare or cluster samples

**ssdeep**, **radiff2**, `bytehist`


## Malware triage — documents

### Analyse Office documents and macros

**olevba**, **oleid**, **oledump.py**, **olemeta**, **oletimes**, **olemap**, **oledir**, **olebrowse**, **olefile**, **oleobj**, **mraptor**, **msodde**, **pcodedmp**, **pyxswf**, **xlmdeobfuscator**, `runxlrd2.py`, `vipermonkey`

### Analyse RTF documents and embedded objects

**rtfobj**, **oleobj**, `rtfdump.py`

### Analyse PDFs

**pdfid**, **pdfid.py**, **pdf-parser**, **pdf-parser.py**, `peepdf`, `qpdf`

### Analyse other container formats

**7za**, **unzip**, **msoffcrypto-tool**, `onenoteanalyzer`


## Reverse engineering

### Disassemble and explore a binary

**r2**, **rabin2**, **rasm2**, **objdump**, **vivbin**, **vdbbin**, `rizin`, `ghidra`, `cutter`

### Diff two binaries

**radiff2**, `bindiff`

### Emulate or instrument execution

**frida**, **frida-trace**, **frida-ps**, **frida-discover**, **frida-kill**, **frida-ls-devices**, `speakeasy`, `qiling`, `scdbg`, `unicorn`

### Analyse shellcode

**rasm2**, **xortool**, `scdbg`, `shellcode2exe`


## Decode & deobfuscate

### Decode, decrypt or transform encoded data

**cyberchef**, **base64dump.py**, **rax2**, **xxd**, **openssl**, **numbers-to-string.py**

### Break simple obfuscation

**xortool**, **floss**, **xlmdeobfuscator**, `de4dot`

### Crack passwords and hashes

**hashcat**, **john**, **hydra**, `unshadow`, `zip2john`, `rar2john`, `fcrackzip`, `hashid`

### Find hidden data

**binwalk**, **ssdeep**, `steghide`, `stegosuite`


## Report & support

### Fetch and verify external references

**curl**, **wget**

### Inspect files by hand

**xxd**, **ezhexviewer**, **less**, `hexdump`


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