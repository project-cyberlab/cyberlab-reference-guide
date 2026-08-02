# Capture Coverage

What can be documented **from a real binary** today, and what cannot.
A tool without a capture cannot get a page — see [docs/FORMAT.md](../docs/FORMAT.md#5-verification-why-the-options-can-be-trusted).

- **973 tools captured** with real help text — ready to document
- **85 present but no usable help** — GUI-only, or help needs arguments; document workflow rather than flags
- **773 not in either container** — need a booted VM (Kali, FLARE-VM Windows guest) or are GUI/appliance-only
- probed against `cyberlab-aio:v1` and `dfir-aio:v4` on rick

## Captured — ready to document

| Command | Image | Via | Version | Help bytes |
|---|---|---|---|---|
| `2to3` | cyberlab-aio | `--help` |  | 1,301 |
| `7z` | cyberlab-aio | `--help` |  | 3,140 |
| `7za` | cyberlab-aio | `--help` |  | 3,146 |
| `7zr` | cyberlab-aio | `--help` |  | 3,127 |
| `AmcacheParser` | cyberlab-aio | `--help` | 2026.5.0+76dc8354aa98ce1e1c6f942abcfb09f583f411d | 1,710 |
| `AppCompatCacheParser` | cyberlab-aio | `--help` | 2026.5.0+0cf059f40c2f7b31acdccb14246194540221739 | 1,395 |
| `EvtxECmd` | cyberlab-aio | `--help` | 2026.5.0+bfc7f47ccbf65ffc9a3777cde5498db2fdd9466 | 2,865 |
| `JLECmd` | cyberlab-aio | `--help` | 2026.5.0+15d8f46f083d04c9a5cbb1f0fad37c1225da43f | 2,802 |
| `LECmd` | cyberlab-aio | `--help` | 2026.5.0+def1fc2686af4684d06a889b1315f225187ac8f | 2,317 |
| `MFTECmd` | cyberlab-aio | `--help` | 2026.5.0+4fd94a6bd12237e8501baff5fc9e5b1b01c5386 | 4,203 |
| `PECmd` | cyberlab-aio | `--help` | 2026.5.0+bde430c69ba4d97fea8b71fdddb6df7849419c1 | 2,313 |
| `RBCmd` | cyberlab-aio | `--help` | 2026.5.0+72d305ee2aa7e5bf4e5e1e01576b34ab402038a | 1,328 |
| `RECmd` | cyberlab-aio | `--help` | 2026.5.0+bcd0ac33ed98de61ea6de551eef96052bddbbd4 | 2,802 |
| `RecentFileCacheParser` | cyberlab-aio | `--help` | 2026.5.0+722ea4c06bcb9150cdadbe96a650f525578dbd6 | 1,177 |
| `SBECmd` | cyberlab-aio | `--help` | 2026.5.0+5d73145683f1bfaeb4aec4d080badcb7b7cadb9 | 1,718 |
| `SrumECmd` | cyberlab-aio | `--help` | 2026.5.0+880ad26bcb011976a8fc521eea63fc5e6e65ba0 | 1,290 |
| `SumECmd` | cyberlab-aio | `--help` | 2026.5.0+8227da19559d4d4f9f45aefabbae7a37fd4f638 | 1,003 |
| `WxTCmd` | cyberlab-aio | `--help` | 2026.5.0+adbf96ed9c73dc6806d97b96160bb96bccd48f7 | 1,063 |
| `XORSearch` | cyberlab-aio | `--help` | xorsearch.py 0.0.5 | 2,704 |
| `add-shell` | cyberlab-aio | `-h` |  | 151 |
| `addgroup` | cyberlab-aio | `--help` | adduser version 3.134 | 1,123 |
| `addpart` | cyberlab-aio | `--help` | addpart from util-linux 2.38.1 | 239 |
| `addr2line` | cyberlab-aio | `--help` | GNU addr2line (GNU Binutils for Debian) 2.40 | 1,279 |
| `adduser` | cyberlab-aio | `--help` | adduser version 3.134 | 1,123 |
| `aeskeyfind` | cyberlab-aio | `--help` |  | 418 |
| `affcat` | cyberlab-aio | `--help` | affcat version 3.7.20 | 806 |
| `affcompare` | cyberlab-aio | `--help` | affcompare version 3.7.20 | 2,258 |
| `affconvert` | cyberlab-aio | `--help` | affconvert version 3.7.20 | 144 |
| `affcrypto` | cyberlab-aio | `--help` | affcrypto version 3.7.20 | 1,763 |
| `affinfo` | cyberlab-aio | `--help` | affinfo version 3.7.20 | 1,149 |
| `affix` | cyberlab-aio | `--help` | affix version 3.7.20 | 179 |
| `affsegment` | cyberlab-aio | `--help` | affsegment version 3.7.20 | 1,359 |
| `affsign` | cyberlab-aio | `--help` | affsign version 3.7.20 | 686 |
| `affstats` | cyberlab-aio | `--help` | affstats version 3.7.20 | 184 |
| `affuse` | cyberlab-aio | `--help` |  | 3,145 |
| `affverify` | cyberlab-aio | `--help` | affverify version 3.7.20 | 287 |
| `agetty` | cyberlab-aio | `--help` | agetty from util-linux 2.38.1 (flow control, hin | 2,196 |
| `aircrack-ng` | cyberlab-aio | `--help` | aircrack-ng: unrecognized option '--version' | 3,017 |
| `appcompat` | cyberlab-aio | `--help` | Version: 0.9.1 | 2,435 |
| `apt` | cyberlab-aio | `--help` | apt 2.6.1 (amd64) | 1,289 |
| `apt-cache` | cyberlab-aio | `--help` | apt 2.6.1 (amd64) | 1,189 |
| `apt-cdrom` | cyberlab-aio | `--help` | apt 2.6.1 (amd64) | 656 |
| `apt-config` | cyberlab-aio | `--help` | apt 2.6.1 (amd64) | 634 |
| `apt-get` | cyberlab-aio | `--help` | apt 2.6.1 (amd64) | 1,618 |
| `apt-key` | cyberlab-aio | `--help` | Unknown option: --version | 738 |
| `apt-mark` | cyberlab-aio | `--help` | apt 2.6.1 (amd64) | 1,117 |
| `ar` | cyberlab-aio | `--help` | GNU ar (GNU Binutils for Debian) 2.40 | 2,178 |
| `arch` | cyberlab-aio | `--help` | arch (GNU coreutils) 9.1 | 351 |
| `arp-scan` | cyberlab-aio | `--help` | arp-scan 1.10.0 | 10,445 |
| `arpd` | cyberlab-aio | `--help` |  | 151 |
| `as` | cyberlab-aio | `--help` | GNU assembler (GNU Binutils for Debian) 2.40 | 10,853 |
| `asan_symbolize-15` | cyberlab-aio | `--help` |  | 1,914 |
| `awk` | cyberlab-aio | `(no args)` | awk: not an option: --version | 1,154 |
| `b2sum` | cyberlab-aio | `--help` | b2sum (GNU coreutils) 9.1 | 1,819 |
| `badblocks` | cyberlab-aio | `--help` |  | 294 |
| `base32` | cyberlab-aio | `--help` | base32 (GNU coreutils) 9.1 | 1,049 |
| `base64` | cyberlab-aio | `--help` | base64 (GNU coreutils) 9.1 | 1,049 |
| `base64dump` | cyberlab-aio | `--help` | base64dump.py 0.0.30 | 3,352 |
| `base64dump.py` | cyberlab-aio | `--help` | base64dump.py 0.0.30 | 3,352 |
| `basename` | cyberlab-aio | `--help` | basename (GNU coreutils) 9.1 | 956 |
| `basenc` | cyberlab-aio | `--help` | basenc (GNU coreutils) 9.1 | 1,677 |
| `bash` | cyberlab-aio | `--help` | GNU bash, version 5.2.15(1)-release (x86_64-pc-l | 764 |
| `bashbug` | cyberlab-aio | `--help` | GNU bashbug, version 5.2.15-release | 598 |
| `bdeinfo` | cyberlab-aio | `--help` |  | 768 |
| `bdemount` | cyberlab-aio | `--help` |  | 1,078 |
| `binwalk` | cyberlab-aio | `--help` |  | 4,245 |
| `blkcalc` | cyberlab-aio | `--help` | The Sleuth Kit ver 4.11.1 | 919 |
| `blkcat` | cyberlab-aio | `--help` | The Sleuth Kit ver 4.11.1 | 978 |
| `blkdiscard` | cyberlab-aio | `--help` | blkdiscard from util-linux 2.38.1 | 708 |
| `blkid` | cyberlab-aio | `--help` | blkid from util-linux 2.38.1  (libblkid 2.38.1,  | 2,033 |
| `blkls` | cyberlab-aio | `--help` | The Sleuth Kit ver 4.11.1 | 872 |
| `blkstat` | cyberlab-aio | `--help` | The Sleuth Kit ver 4.11.1 | 652 |
| `blkzone` | cyberlab-aio | `--help` | blkzone from util-linux 2.38.1 | 956 |
| `blockdev` | cyberlab-aio | `--help` | blockdev from util-linux 2.38.1 | 1,478 |
| `bridge` | cyberlab-aio | `--help` | Option "-version" is unknown, try "bridge help". | 337 |
| `bstrings` | cyberlab-aio | `--help` | 2026.5+6cca053120b10a1c5cb563e3574ec7b2e0e894e3 | 3,307 |
| `bulk_extractor` | cyberlab-aio | `--help` | bulk_extractor 2.2.0-DEVELOP | 8,755 |
| `bunzip2` | cyberlab-aio | `--help` | bzip2, a block-sorting file compressor.  Version | 1,248 |
| `bzcat` | cyberlab-aio | `--help` | bzip2, a block-sorting file compressor.  Version | 1,246 |
| `bzip2` | cyberlab-aio | `--help` | bzip2, a block-sorting file compressor.  Version | 1,246 |
| `bzip2recover` | cyberlab-aio | `(no args)` | bzip2recover 1.0.8: extracts blocks from damaged | 163 |
| `bzless` | cyberlab-aio | `--help` | ------> --version <------ | 1,269 |
| `bzmore` | cyberlab-aio | `--help` | ------> --version <------ | 1,269 |
| `c++` | cyberlab-aio | `--help` | c++ (Debian 12.2.0-14+deb12u1) 12.2.0 | 4,090 |
| `c++filt` | cyberlab-aio | `--help` | GNU c++filt (GNU Binutils for Debian) 2.40 | 1,006 |
| `c89` | cyberlab-aio | `--help` | gcc (Debian 12.2.0-14+deb12u1) 12.2.0 | 4,090 |
| `c89-gcc` | cyberlab-aio | `--help` | gcc (Debian 12.2.0-14+deb12u1) 12.2.0 | 4,090 |
| `c99` | cyberlab-aio | `--help` | gcc (Debian 12.2.0-14+deb12u1) 12.2.0 | 4,090 |
| `c99-gcc` | cyberlab-aio | `--help` | gcc (Debian 12.2.0-14+deb12u1) 12.2.0 | 4,090 |
| `c_rehash` | cyberlab-aio | `-h` |  | 152 |
| `cabextract` | cyberlab-aio | `--help` | cabextract version 1.9 | 986 |
| `capa` | cyberlab-aio | `--help` | capa 9.4.0 | 4,392 |
| `capa-offline` | cyberlab-aio | `--help` | capa 9.4.0 | 4,392 |
| `capinfos` | cyberlab-aio | `--help` | Capinfos (Wireshark) 4.0.17 (Git v4.0.17 package | 2,219 |
| `capsh` | cyberlab-aio | `--help` |  | 2,425 |
| `captoinfo` | cyberlab-aio | `--help` | ncurses 6.4.20221231 | 1,749 |
| `captype` | cyberlab-aio | `--help` | Captype (Wireshark) 4.0.17 (Git v4.0.17 packaged | 326 |
| `cat` | cyberlab-aio | `--help` | cat (GNU coreutils) 9.1 | 1,107 |
| `cc` | cyberlab-aio | `--help` | cc (Debian 12.2.0-14+deb12u1) 12.2.0 | 4,088 |
| `ccrypt` | cyberlab-aio | `--help` | ccrypt 1.11. Secure encryption and decryption of | 2,004 |
| `cffi-gen-src` | cyberlab-aio | `--help` |  | 406 |
| `chage` | cyberlab-aio | `--help` | chage: unrecognized option '--version' | 884 |
| `chainsaw` | cyberlab-aio | `--help` | chainsaw 2.16.0 | 1,336 |
| `chcon` | cyberlab-aio | `--help` | chcon (GNU coreutils) 9.1 | 2,039 |
| `chcpu` | cyberlab-aio | `--help` | chcpu from util-linux 2.38.1 | 494 |
| `chfn` | cyberlab-aio | `--help` | chfn: unrecognized option '--version' | 477 |
| `chgpasswd` | cyberlab-aio | `--help` | chgpasswd: unrecognized option '--version' | 569 |
| `chgrp` | cyberlab-aio | `--help` | chgrp (GNU coreutils) 9.1 | 1,949 |
| `chmem` | cyberlab-aio | `--help` | chmem from util-linux 2.38.1 | 482 |
| `chmod` | cyberlab-aio | `--help` | chmod (GNU coreutils) 9.1 | 1,079 |
| `choom` | cyberlab-aio | `--help` | choom from util-linux 2.38.1 | 369 |
| `chown` | cyberlab-aio | `--help` | chown (GNU coreutils) 9.1 | 2,614 |
| `chpasswd` | cyberlab-aio | `--help` | chpasswd: unrecognized option '--version' | 568 |
| `chroot` | cyberlab-aio | `--help` | chroot (GNU coreutils) 9.1 | 703 |
| `chrt` | cyberlab-aio | `--help` | chrt from util-linux 2.38.1 | 1,116 |
| `chsh` | cyberlab-aio | `--help` | chsh: unrecognized option '--version' | 232 |
| `cksum` | cyberlab-aio | `--help` | cksum (GNU coreutils) 9.1 | 2,165 |
| `clambc` | cyberlab-aio | `--help` | Clam AntiVirus Bytecode Testing Tool 1.4.3 | 1,229 |
| `clamscan` | cyberlab-aio | `--help` | ClamAV 1.4.3 | 8,404 |
| `clamsubmit` | cyberlab-aio | `--help` | ClamAV 1.4.3 | 819 |
| `clang++-15` | cyberlab-aio | `--help` | Debian clang version 15.0.6 | 65,536 |
| `clang-15` | cyberlab-aio | `--help` | Debian clang version 15.0.6 | 65,536 |
| `clang-cpp-15` | cyberlab-aio | `--help` | Debian clang version 15.0.6 | 65,536 |
| `clang-format-radare2` | cyberlab-aio | `--help` | clang-format-radare2 1.0 | 1,139 |
| `clear` | cyberlab-aio | `--help` | ncurses 6.4.20221231 | 181 |
| `clear_console` | cyberlab-aio | `--help` | clear_console: Version 0.1 | 192 |
| `cmp` | cyberlab-aio | `--help` | cmp (GNU diffutils) 3.8 | 1,314 |
| `comm` | cyberlab-aio | `--help` | comm (GNU coreutils) 9.1 | 1,436 |
| `corelist` | cyberlab-aio | `--help` |  | 3,964 |
| `cp` | cyberlab-aio | `--help` | cp (GNU coreutils) 9.1 | 4,822 |
| `cpan` | cyberlab-aio | `--help` | /usr/bin/cpan version 1.64 calling Getopt::Std:: | 780 |
| `cpan5.36-x86_64-linux-gnu` | cyberlab-aio | `--help` | /usr/bin/cpan5.36-x86_64-linux-gnu version 1.64  | 843 |
| `cpgr` | cyberlab-aio | `--help` | cpgr: version: No such file or directory | 193 |
| `cpp` | cyberlab-aio | `--help` | cpp (Debian 12.2.0-14+deb12u1) 12.2.0 | 4,090 |
| `cpp-12` | cyberlab-aio | `--help` | cpp-12 (Debian 12.2.0-14+deb12u1) 12.2.0 | 4,096 |
| `cppw` | cyberlab-aio | `--help` | cppw: version: No such file or directory | 193 |
| `crontab` | cyberlab-aio | `--help` | version: No such file or directory | 463 |
| `cryptsetup` | cyberlab-aio | `--help` | cryptsetup 2.6.1 flags: UDEV BLKID KEYRING KERNE | 14,471 |
| `csplit` | cyberlab-aio | `--help` | csplit (GNU coreutils) 9.1 | 1,472 |
| `ctrlaltdel` | cyberlab-aio | `--help` | ctrlaltdel from util-linux 2.38.1 | 193 |
| `ctstat` | cyberlab-aio | `--help` | ctstat Version 6.1.0 | 672 |
| `curl` | cyberlab-aio | `--help` | curl 7.88.1 (x86_64-pc-linux-gnu) libcurl/7.88.1 | 914 |
| `cut` | cyberlab-aio | `--help` | cut (GNU coreutils) 9.1 | 1,782 |
| `cvtsudoers` | cyberlab-aio | `--help` | cvtsudoers version 1.9.13p3 | 1,329 |
| `cyberchef` | cyberlab-aio | `--help` |  | 176 |
| `date` | cyberlab-aio | `--help` | date (GNU coreutils) 9.1 | 4,875 |
| `dc3dd` | cyberlab-aio | `--help` | dc3dd (dc3dd) 7.2.646 | 9,633 |
| `dcb` | cyberlab-aio | `--help` | dcb: unrecognized option '--version' | 361 |
| `dcfldd` | cyberlab-aio | `--help` | dcfldd (dcfldd) 1.9 | 2,520 |
| `dd` | cyberlab-aio | `--help` | dd (coreutils) 9.1 | 3,296 |
| `deb-systemd-helper` | cyberlab-aio | `--help` | Unknown option: version | 197 |
| `debconf` | cyberlab-aio | `--help` | Unknown option: version | 252 |
| `debconf-communicate` | cyberlab-aio | `--help` | Unknown option: version | 196 |
| `debconf-copydb` | cyberlab-aio | `--help` | Unknown option: version | 123 |
| `debconf-escape` | cyberlab-aio | `--help` | Unknown option: version | 168 |
| `debconf-set-selections` | cyberlab-aio | `--help` | Unknown option: version | 222 |
| `debconf-show` | cyberlab-aio | `--help` | Unknown option: version | 148 |
| `debugfs` | cyberlab-aio | `--help` | debugfs 1.47.0 (5-Feb-2023) | 220 |
| `delgroup` | cyberlab-aio | `--help` | deluser version 3.134 | 548 |
| `delpart` | cyberlab-aio | `--help` | delpart from util-linux 2.38.1 | 215 |
| `deluser` | cyberlab-aio | `--help` | deluser version 3.134 | 548 |
| `delv` | cyberlab-aio | `--help` | Invalid option: --version | 2,650 |
| `devlink` | cyberlab-aio | `--help` | devlink: unrecognized option '--version' | 375 |
| `df` | cyberlab-aio | `--help` | df (GNU coreutils) 9.1 | 2,430 |
| `dfir` | cyberlab-aio | `--help` |  | 1,713 |
| `dh_perl_openssl` | cyberlab-aio | `--help` | Can't locate Debian/Debhelper/Dh_Lib.pm in @INC  | 488 |
| `die` | cyberlab-aio | `--help` | Detect It Easy v3.10 | 403 |
| `diec` | cyberlab-aio | `--help` | die 3.10 | 1,545 |
| `diel` | cyberlab-aio | `--help` | Detect It Easy Lite v3.10 | 403 |
| `diff` | cyberlab-aio | `--help` | diff (GNU diffutils) 3.8 | 5,387 |
| `diff3` | cyberlab-aio | `--help` | diff3 (GNU diffutils) 3.8 | 1,996 |
| `dig` | cyberlab-aio | `--help` | Invalid option: --version | 269 |
| `dir` | cyberlab-aio | `--help` | dir (GNU coreutils) 9.1 | 7,732 |
| `dircolors` | cyberlab-aio | `--help` | dircolors (GNU coreutils) 9.1 | 908 |
| `dirmngr` | cyberlab-aio | `--help` | dirmngr (GnuPG) 2.2.40 | 3,211 |
| `dirmngr-client` | cyberlab-aio | `--help` | dirmngr-client (GnuPG) 2.2.40 | 1,333 |
| `dirname` | cyberlab-aio | `--help` | dirname (GNU coreutils) 9.1 | 691 |
| `dislocker` | cyberlab-aio | `--help` | dislocker: unrecognized option '--version' | 1,647 |
| `dislocker-fuse` | cyberlab-aio | `--help` | dislocker-fuse: unrecognized option '--version' | 1,647 |
| `dmesg` | cyberlab-aio | `--help` | dmesg from util-linux 2.38.1 | 2,915 |
| `dnsdomainname` | cyberlab-aio | `--help` | hostname 3.23 | 1,487 |
| `dnstap-read` | cyberlab-aio | `--help` |  | 198 |
| `domainname` | cyberlab-aio | `--help` | hostname 3.23 | 1,487 |
| `dotnet` | cyberlab-aio | `--help` |  | 950 |
| `dpkg` | cyberlab-aio | `--help` | Debian 'dpkg' package management program version | 4,837 |
| `dpkg-architecture` | cyberlab-aio | `--help` | Debian dpkg-architecture version 1.21.23. | 1,544 |
| `dpkg-buildflags` | cyberlab-aio | `--help` | Debian dpkg-buildflags version 1.21.23. | 960 |
| `dpkg-buildpackage` | cyberlab-aio | `--help` | Debian dpkg-buildpackage version 1.21.23. | 5,368 |
| `dpkg-checkbuilddeps` | cyberlab-aio | `--help` | Debian dpkg-checkbuilddeps version 1.21.23. | 853 |
| `dpkg-deb` | cyberlab-aio | `--help` | Debian 'dpkg-deb' package archive backend versio | 2,762 |
| `dpkg-distaddfile` | cyberlab-aio | `--help` | Debian dpkg-distaddfile version 1.21.23. | 244 |
| `dpkg-divert` | cyberlab-aio | `--help` | Debian dpkg-divert version 1.21.23 (amd64). | 1,367 |
| `dpkg-genbuildinfo` | cyberlab-aio | `--help` | Debian dpkg-genbuildinfo version 1.21.23. | 831 |
| `dpkg-genchanges` | cyberlab-aio | `--help` | Debian dpkg-genchanges version 1.21.23. | 1,763 |
| `dpkg-gencontrol` | cyberlab-aio | `--help` | Debian dpkg-gencontrol version 1.21.23. | 1,031 |
| `dpkg-gensymbols` | cyberlab-aio | `--help` | Debian dpkg-gensymbols version 1.21.23. | 1,742 |
| `dpkg-maintscript-helper` | cyberlab-aio | `--help` | Debian dpkg-maintscript-helper version 1.21.23. | 933 |
| `dpkg-mergechangelogs` | cyberlab-aio | `--help` | Debian dpkg-mergechangelogs version 1.21.23. | 439 |
| `dpkg-name` | cyberlab-aio | `--help` | Debian dpkg-name version 1.21.23. | 594 |
| `dpkg-parsechangelog` | cyberlab-aio | `--help` | Debian dpkg-parsechangelog version 1.21.23. | 1,223 |
| `dpkg-preconfigure` | cyberlab-aio | `--help` | Unknown option: version | 216 |
| `dpkg-query` | cyberlab-aio | `--help` | Debian dpkg-query package management program que | 1,638 |
| `dpkg-realpath` | cyberlab-aio | `--help` | Debian dpkg-realpath version 1.21.23. | 339 |
| `dpkg-reconfigure` | cyberlab-aio | `--help` | Unknown option: version | 435 |
| `dpkg-scanpackages` | cyberlab-aio | `--help` | Debian dpkg-scanpackages version 1.21.23. | 632 |
| `dpkg-scansources` | cyberlab-aio | `--help` | Debian dpkg-scansources version 1.21.23. | 623 |
| `dpkg-shlibdeps` | cyberlab-aio | `--help` | Debian dpkg-shlibdeps version 1.21.23. | 1,581 |
| `dpkg-source` | cyberlab-aio | `--help` | Debian dpkg-source version 1.21.23. | 4,152 |
| `dpkg-split` | cyberlab-aio | `--help` | Debian 'dpkg-split' package split/join tool; ver | 1,152 |
| `dpkg-statoverride` | cyberlab-aio | `--help` | Debian dpkg-statoverride version 1.21.23 (amd64) | 961 |
| `dpkg-trigger` | cyberlab-aio | `--help` | Debian dpkg-trigger package trigger utility vers | 799 |
| `dpkg-vendor` | cyberlab-aio | `--help` | Debian dpkg-vendor version 1.21.23. | 448 |
| `dpl4hydra` | cyberlab-aio | `--help` |  | 1,087 |
| `du` | cyberlab-aio | `--help` | du (GNU coreutils) 9.1 | 3,797 |
| `dumpcap` | cyberlab-aio | `--help` |  | 5,103 |
| `dumpe2fs` | cyberlab-aio | `--help` | dumpe2fs 1.47.0 (5-Feb-2023) | 138 |
| `dwp` | cyberlab-aio | `--help` | GNU dwp (GNU Binutils for Debian) 2.40 | 425 |
| `e2fsck` | cyberlab-aio | `--help` | e2fsck 1.47.0 (5-Feb-2023) | 856 |
| `e2image` | cyberlab-aio | `--help` | e2image 1.47.0 (5-Feb-2023) | 264 |
| `e2scrub` | cyberlab-aio | `--help` | e2scrub 1.47.0 (5-Feb-2023) | 321 |
| `e2scrub_all` | cyberlab-aio | `--help` | e2scrub_all 1.47.0 (5-Feb-2023) | 261 |
| `e2undo` | cyberlab-aio | `--help` |  | 122 |
| `e4crypt` | cyberlab-aio | `--help` | Unknown command: --version | 345 |
| `e4defrag` | cyberlab-aio | `--help` | e4defrag 1.47.0 (5-Feb-2023) | 165 |
| `easy_install-2.7` | cyberlab-aio | `--help` | setuptools 41.2.0 from /usr/local/lib/python2.7/ | 2,101 |
| `echo` | cyberlab-aio | `--help` | echo (GNU coreutils) 9.1 | 1,282 |
| `editcap` | cyberlab-aio | `--help` | Editcap (Wireshark) 4.0.17 (Git v4.0.17 packaged | 7,040 |
| `editor` | cyberlab-aio | `--help` | VIM - Vi IMproved 9.0 (2022 Jun 28, compiled Feb | 1,995 |
| `egrep` | cyberlab-aio | `--help` | grep (GNU grep) 3.8 | 4,041 |
| `elfedit` | cyberlab-aio | `--help` | GNU elfedit (GNU Binutils for Debian) 2.40 | 1,277 |
| `emldump` | cyberlab-aio | `--help` | emldump.py 0.0.16 | 1,292 |
| `enc2xs` | cyberlab-aio | `--help` | /usr/bin/enc2xs version 2.24 calling Getopt::Std | 975 |
| `encguess` | cyberlab-aio | `--help` | /usr/bin/encguess version [unknown] calling Geto | 994 |
| `env` | cyberlab-aio | `--help` | env (GNU coreutils) 9.1 | 1,472 |
| `esedbexport` | cyberlab-aio | `--help` |  | 1,141 |
| `esedbinfo` | cyberlab-aio | `--help` |  | 324 |
| `evtxexport` | cyberlab-aio | `--help` |  | 1,774 |
| `evtxinfo` | cyberlab-aio | `--help` |  | 611 |
| `ewfacquire` | cyberlab-aio | `--help` |  | 3,947 |
| `ewfacquirestream` | cyberlab-aio | `--help` |  | 3,239 |
| `ewfexport` | cyberlab-aio | `--help` |  | 3,013 |
| `ewfinfo` | cyberlab-aio | `--help` |  | 1,068 |
| `ewfmount` | cyberlab-aio | `--help` |  | 697 |
| `ewfrecover` | cyberlab-aio | `--help` |  | 1,236 |
| `ewfverify` | cyberlab-aio | `--help` |  | 1,397 |
| `ex` | cyberlab-aio | `--help` | VIM - Vi IMproved 9.0 (2022 Jun 28, compiled Feb | 1,995 |
| `expand` | cyberlab-aio | `--help` | expand (GNU coreutils) 9.1 | 1,069 |
| `expiry` | cyberlab-aio | `--help` | expiry: unrecognized option '--version' | 289 |
| `expr` | cyberlab-aio | `--help` | expr (GNU coreutils) 9.1 | 2,156 |
| `ezhexviewer` | cyberlab-aio | `--help` |  | 1,593 |
| `factor` | cyberlab-aio | `--help` | factor (GNU coreutils) 9.1 | 483 |
| `faillog` | cyberlab-aio | `--help` | faillog: unrecognized option '--version' | 749 |
| `fallocate` | cyberlab-aio | `--help` | fallocate from util-linux 2.38.1 | 931 |
| `false` | cyberlab-aio | `--help` | false (GNU coreutils) 9.1 | 604 |
| `fc-cache` | cyberlab-aio | `--help` | fontconfig version 2.14.1 | 776 |
| `fc-cat` | cyberlab-aio | `--help` | fontconfig version 2.14.1 | 424 |
| `fc-conflist` | cyberlab-aio | `--help` | fontconfig version 2.14.1 | 205 |
| `fc-list` | cyberlab-aio | `--help` | fontconfig version 2.14.1 | 521 |
| `fc-match` | cyberlab-aio | `--help` | fontconfig version 2.14.1 | 571 |
| `fc-pattern` | cyberlab-aio | `--help` | fontconfig version 2.14.1 | 455 |
| `fc-query` | cyberlab-aio | `--help` | fontconfig version 2.14.1 | 454 |
| `fc-scan` | cyberlab-aio | `--help` | fontconfig version 2.14.1 | 462 |
| `fc-validate` | cyberlab-aio | `--help` | fontconfig version 2.14.1 | 451 |
| `fcat` | cyberlab-aio | `--help` | The Sleuth Kit ver 4.11.1 | 759 |
| `ffind` | cyberlab-aio | `--help` | The Sleuth Kit ver 4.11.1 | 748 |
| `fgrep` | cyberlab-aio | `--help` | grep (GNU grep) 3.8 | 4,041 |
| `fidentify` | cyberlab-aio | `--help` | fidentify 7.1, Data Recovery Utility, July 2019 | 264 |
| `file` | cyberlab-aio | `--help` | file-5.44 | 3,189 |
| `fincore` | cyberlab-aio | `--help` | fincore from util-linux 2.38.1 | 599 |
| `find` | cyberlab-aio | `--help` | find (GNU findutils) 4.9.0 | 2,110 |
| `findfs` | cyberlab-aio | `--help` | findfs from util-linux 2.38.1 | 211 |
| `findmnt` | cyberlab-aio | `--help` | findmnt from util-linux 2.38.1 | 4,081 |
| `fiwalk` | cyberlab-aio | `--help` | SleuthKit Version: 4.11.1 | 1,711 |
| `flock` | cyberlab-aio | `--help` | flock from util-linux 2.38.1 | 896 |
| `floss` | cyberlab-aio | `--help` | floss 3.1.1 | 2,337 |
| `fls` | cyberlab-aio | `--help` | The Sleuth Kit ver 4.11.1 | 1,353 |
| `fmt` | cyberlab-aio | `--help` | fmt (GNU coreutils) 9.1 | 1,157 |
| `fold` | cyberlab-aio | `--help` | fold (GNU coreutils) 9.1 | 666 |
| `foremost` | cyberlab-aio | `-h` | 1.5.7 | 830 |
| `free` | cyberlab-aio | `--help` | free from procps-ng 4.0.2 | 1,074 |
| `freshclam` | cyberlab-aio | `--help` | ClamAV 1.4.3 | 3,341 |
| `frida` | cyberlab-aio | `--help` | 17.16.3 | 4,398 |
| `frida-apk` | cyberlab-aio | `--help` | 17.16.3 | 606 |
| `frida-compile` | cyberlab-aio | `--help` | 17.16.3 | 1,171 |
| `frida-create` | cyberlab-aio | `--help` | 17.16.3 | 535 |
| `frida-discover` | cyberlab-aio | `--help` | 17.16.3 | 2,991 |
| `frida-itrace` | cyberlab-aio | `--help` |  | 3,421 |
| `frida-join` | cyberlab-aio | `--help` | 17.16.3 | 3,379 |
| `frida-kill` | cyberlab-aio | `--help` | 17.16.3 | 1,525 |
| `frida-ls` | cyberlab-aio | `--help` | 17.16.3 | 1,537 |
| `frida-ls-devices` | cyberlab-aio | `--help` | 17.16.3 | 270 |
| `frida-pm` | cyberlab-aio | `--help` | 17.16.3 | 488 |
| `frida-ps` | cyberlab-aio | `--help` | 17.16.3 | 1,649 |
| `frida-pull` | cyberlab-aio | `--help` | 17.16.3 | 1,534 |
| `frida-push` | cyberlab-aio | `--help` | 17.16.3 | 1,533 |
| `frida-rm` | cyberlab-aio | `--help` | 17.16.3 | 1,642 |
| `frida-strace` | cyberlab-aio | `--help` | 17.16.3 | 2,134 |
| `frida-trace` | cyberlab-aio | `--help` | 17.16.3 | 4,999 |
| `fsck` | cyberlab-aio | `--help` | fsck from util-linux 2.38.1 | 969 |
| `fsck.cramfs` | cyberlab-aio | `--help` | fsck.cramfs from util-linux 2.38.1 | 521 |
| `fsck.ext2` | cyberlab-aio | `--help` | e2fsck 1.47.0 (5-Feb-2023) | 862 |
| `fsck.ext3` | cyberlab-aio | `--help` | e2fsck 1.47.0 (5-Feb-2023) | 862 |
| `fsck.ext4` | cyberlab-aio | `--help` | e2fsck 1.47.0 (5-Feb-2023) | 862 |
| `fsck.minix` | cyberlab-aio | `--help` | fsck.minix from util-linux 2.38.1 | 472 |
| `fsfreeze` | cyberlab-aio | `--help` | fsfreeze from util-linux 2.38.1 | 275 |
| `fsstat` | cyberlab-aio | `--help` | The Sleuth Kit ver 4.11.1 | 679 |
| `fstrim` | cyberlab-aio | `--help` | fstrim from util-linux 2.38.1 | 881 |
| `ftguess` | cyberlab-aio | `--help` | ftguess 0.60.2 on Python 3.11.2 - http://decalag | 918 |
| `fusermount` | cyberlab-aio | `--help` | fusermount3 version: 3.14.0 | 172 |
| `fusermount3` | cyberlab-aio | `--help` | fusermount3 version: 3.14.0 | 173 |
| `g++` | cyberlab-aio | `--help` | g++ (Debian 12.2.0-14+deb12u1) 12.2.0 | 4,090 |
| `g++-12` | cyberlab-aio | `--help` | g++-12 (Debian 12.2.0-14+deb12u1) 12.2.0 | 4,096 |
| `gcc` | cyberlab-aio | `--help` | gcc (Debian 12.2.0-14+deb12u1) 12.2.0 | 4,090 |
| `gcc-12` | cyberlab-aio | `--help` | gcc-12 (Debian 12.2.0-14+deb12u1) 12.2.0 | 4,096 |
| `gcc-ar` | cyberlab-aio | `--help` | GNU ar (GNU Binutils for Debian) 2.40 | 2,205 |
| `gcc-ar-12` | cyberlab-aio | `--help` | GNU ar (GNU Binutils for Debian) 2.40 | 2,205 |
| `gcc-nm` | cyberlab-aio | `--help` | GNU nm (GNU Binutils for Debian) 2.40 | 2,911 |
| `gcc-nm-12` | cyberlab-aio | `--help` | GNU nm (GNU Binutils for Debian) 2.40 | 2,911 |
| `gcc-ranlib` | cyberlab-aio | `--help` | GNU ranlib (GNU Binutils for Debian) 2.40 | 834 |
| `gcc-ranlib-12` | cyberlab-aio | `--help` | GNU ranlib (GNU Binutils for Debian) 2.40 | 834 |
| `gcov` | cyberlab-aio | `--help` | gcov (Debian 12.2.0-14+deb12u1) 12.2.0 | 1,993 |
| `gcov-12` | cyberlab-aio | `--help` | gcov (Debian 12.2.0-14+deb12u1) 12.2.0 | 1,993 |
| `gcov-dump` | cyberlab-aio | `--help` | gcov-dump (Debian 12.2.0-14+deb12u1) 12.2.0 | 392 |
| `gcov-dump-12` | cyberlab-aio | `--help` | gcov-dump (Debian 12.2.0-14+deb12u1) 12.2.0 | 392 |
| `gcov-tool` | cyberlab-aio | `--help` | gcov-tool (Debian 12.2.0-14+deb12u1) 12.2.0 | 1,350 |
| `gcov-tool-12` | cyberlab-aio | `--help` | gcov-tool-12 (Debian 12.2.0-14+deb12u1) 12.2.0 | 1,353 |
| `gencat` | cyberlab-aio | `--help` | gencat (Debian GLIBC 2.36-9+deb12u14) 2.36 | 882 |
| `genl` | cyberlab-aio | `-h` | Option "--version" is unknown, try "genl -help". | 150 |
| `getcap` | cyberlab-aio | `--help` | version (No such file or directory) | 148 |
| `getconf` | cyberlab-aio | `--help` | getconf (Debian GLIBC 2.36-9+deb12u14) 2.36 | 295 |
| `getent` | cyberlab-aio | `--help` | getent (Debian GLIBC 2.36-9+deb12u14) 2.36 | 819 |
| `getopt` | cyberlab-aio | `--help` | getopt from util-linux 2.38.1 | 903 |
| `getpcaps` | cyberlab-aio | `--help` | Cannot parse pid --version: (Invalid argument) | 472 |
| `getty` | cyberlab-aio | `--help` | getty from util-linux 2.38.1 (flow control, hint | 2,194 |
| `git` | cyberlab-aio | `--help` | git version 2.39.5 | 2,160 |
| `git-receive-pack` | cyberlab-aio | `(no args)` | error: unknown option `version' | 163 |
| `git-upload-archive` | cyberlab-aio | `-help` |  | 197 |
| `git-upload-pack` | cyberlab-aio | `-h` | error: unknown option `version' | 366 |
| `gmake` | cyberlab-aio | `--help` | GNU Make 4.3 | 2,714 |
| `gold` | cyberlab-aio | `--help` | GNU gold (GNU Binutils for Debian 2.40) 1.16 | 22,864 |
| `gp-archive` | cyberlab-aio | `--help` | GNU x86_64-linux-gnu-gp-archive binutils version | 2,397 |
| `gp-collect-app` | cyberlab-aio | `--help` | GNU x86_64-linux-gnu-gp-collect-app binutils ver | 4,392 |
| `gp-display-html` | cyberlab-aio | `--help` | gp-display-html GNU binutils version 2.40.00 | 2,761 |
| `gp-display-src` | cyberlab-aio | `--help` | GNU x86_64-linux-gnu-gp-display-src binutils ver | 1,571 |
| `gp-display-text` | cyberlab-aio | `--help` | GNU x86_64-linux-gnu-gp-display-text binutils ve | 1,554 |
| `gpasswd` | cyberlab-aio | `--help` | gpasswd: unrecognized option '--version' | 637 |
| `gpg` | cyberlab-aio | `--help` | gpg (GnuPG) 2.2.40 | 5,008 |
| `gpg-agent` | cyberlab-aio | `--help` | gpg-agent (GnuPG) 2.2.40 | 3,366 |
| `gpg-connect-agent` | cyberlab-aio | `--help` | gpg-connect-agent (GnuPG) 2.2.40 | 981 |
| `gpg-wks-server` | cyberlab-aio | `--help` | gpg-wks-server (GnuPG) 2.2.40 | 1,151 |
| `gpg-zip` | cyberlab-aio | `--help` |  | 347 |
| `gpgcompose` | cyberlab-aio | `--help` | Fatal: Unknown option: version | 1,149 |
| `gpgconf` | cyberlab-aio | `--help` | gpgconf (GnuPG) 2.2.40 | 1,650 |
| `gpgparsemail` | cyberlab-aio | `--help` | gpgparsemail: can't open '--version': No such fi | 485 |
| `gpgsm` | cyberlab-aio | `--help` | gpgsm (GnuPG) 2.2.40 | 4,606 |
| `gpgsplit` | cyberlab-aio | `--help` | gpgsplit (@GNUPG@) 2.2.40 | 628 |
| `gpgtar` | cyberlab-aio | `--help` | gpgtar (GnuPG) 2.2.40 | 1,309 |
| `gpgv` | cyberlab-aio | `--help` | gpgv (GnuPG) 2.2.40 | 793 |
| `gprof` | cyberlab-aio | `--help` | GNU gprof (GNU Binutils for Debian) 2.40 | 821 |
| `gprofng` | cyberlab-aio | `--help` | GNU x86_64-linux-gnu-gprofng binutils version 2. | 3,287 |
| `grep` | cyberlab-aio | `--help` | grep (GNU grep) 3.8 | 4,041 |
| `groupadd` | cyberlab-aio | `--help` | groupadd: unrecognized option '--version' | 810 |
| `groupdel` | cyberlab-aio | `--help` | groupdel: unrecognized option '--version' | 336 |
| `groupmems` | cyberlab-aio | `--help` | groupmems: unrecognized option '--version' | 578 |
| `groupmod` | cyberlab-aio | `--help` | groupmod: unrecognized option '--version' | 780 |
| `groups` | cyberlab-aio | `--help` | groups (GNU coreutils) 9.1 | 496 |
| `grpck` | cyberlab-aio | `--help` | grpck: unrecognized option '--version' | 414 |
| `grpconv` | cyberlab-aio | `--help` | grpconv: unrecognized option '--version' | 158 |
| `grpunconv` | cyberlab-aio | `--help` | grpunconv: unrecognized option '--version' | 160 |
| `gunzip` | cyberlab-aio | `--help` | gunzip (gzip) 1.12 | 1,059 |
| `gzexe` | cyberlab-aio | `--help` | gzexe (gzip) 1.12 | 351 |
| `gzip` | cyberlab-aio | `--help` | gzip 1.12 | 1,245 |
| `h2ph` | cyberlab-aio | `--help` | /usr/bin/h2ph version [unknown] calling Getopt:: | 730 |
| `h2xs` | cyberlab-aio | `--help` | Defaulting to backwards compatibility with perl  | 3,037 |
| `hardlink` | cyberlab-aio | `--help` | hardlink from util-linux 2.38.1 | 1,718 |
| `hashcat` | cyberlab-aio | `--help` | v6.2.6 | 58,909 |
| `hayabusa` | cyberlab-aio | `help` | error: unexpected argument '--version' found | 1,490 |
| `hcli` | cyberlab-aio | `--help` | hcli, version 0.18.3 | 3,022 |
| `head` | cyberlab-aio | `--help` | head (GNU coreutils) 9.1 | 1,394 |
| `hfind` | cyberlab-aio | `--help` | The Sleuth Kit ver 4.11.1 | 672 |
| `hivexsh` | cyberlab-aio | `help` | hivexsh: failed to open hive file: version: No s | 333 |
| `host` | cyberlab-aio | `--help` | host 9.18.49-1~deb12u1-Debian | 1,095 |
| `hostid` | cyberlab-aio | `--help` | hostid (GNU coreutils) 9.1 | 394 |
| `hostname` | cyberlab-aio | `--help` | hostname 3.23 | 1,487 |
| `httpx` | cyberlab-aio | `--help` |  | 4,378 |
| `hwclock` | cyberlab-aio | `--help` | hwclock from util-linux 2.38.1 | 1,949 |
| `hydra` | cyberlab-aio | `--help` | Hydra v9.4 (c) 2022 by van Hauser/THC & David Ma | 237 |
| `i386` | cyberlab-aio | `--help` | i386 from util-linux 2.38.1 | 1,017 |
| `icat` | cyberlab-aio | `--help` | The Sleuth Kit ver 4.11.1 | 877 |
| `iconv` | cyberlab-aio | `--help` | iconv (Debian GLIBC 2.36-9+deb12u14) 2.36 | 894 |
| `iconvconfig` | cyberlab-aio | `--help` | iconvconfig (Debian GLIBC 2.36-9+deb12u14) 2.36 | 770 |
| `id` | cyberlab-aio | `--help` | id (GNU coreutils) 9.1 | 1,023 |
| `ida-hcli` | cyberlab-aio | `--help` | ida-hcli, version 0.18.3 | 3,022 |
| `idna` | cyberlab-aio | `--help` | idna 3.18 | 980 |
| `ifind` | cyberlab-aio | `--help` | The Sleuth Kit ver 4.11.1 | 987 |
| `ils` | cyberlab-aio | `--help` | The Sleuth Kit ver 4.11.1 | 1,068 |
| `img_cat` | cyberlab-aio | `--help` | The Sleuth Kit ver 4.11.1 | 435 |
| `img_stat` | cyberlab-aio | `--help` | The Sleuth Kit ver 4.11.1 | 340 |
| `inetsim` | cyberlab-aio | `--help` | INetSim 1.3.2 (2020-05-19) by Matthias Eckert &  | 1,646 |
| `infocmp` | cyberlab-aio | `--help` | ncurses 6.4.20221231 | 1,433 |
| `infotocap` | cyberlab-aio | `--help` | ncurses 6.4.20221231 | 1,749 |
| `install` | cyberlab-aio | `--help` | install (GNU coreutils) 9.1 | 3,240 |
| `instmodsh` | cyberlab-aio | `--help` |  | 65,536 |
| `invoke-rc.d` | cyberlab-aio | `--help` | invoke-rc.d: syntax error: unknown option "--ver | 1,574 |
| `ionice` | cyberlab-aio | `--help` | ionice from util-linux 2.38.1 | 853 |
| `ip` | cyberlab-aio | `--help` | Option "-version" is unknown, try "ip -help". | 971 |
| `ipcmk` | cyberlab-aio | `--help` | ipcmk from util-linux 2.38.1 | 570 |
| `ipcrm` | cyberlab-aio | `--help` | ipcrm from util-linux 2.38.1 | 678 |
| `ipcs` | cyberlab-aio | `--help` | ipcs from util-linux 2.38.1 | 782 |
| `ischroot` | cyberlab-aio | `--help` | Debian ischroot, version 5.7Copyright (C) 2011 A | 240 |
| `isosize` | cyberlab-aio | `--help` | isosize from util-linux 2.38.1 | 339 |
| `istat` | cyberlab-aio | `--help` | The Sleuth Kit ver 4.11.1 | 1,004 |
| `jcat` | cyberlab-aio | `--help` | The Sleuth Kit ver 4.11.1 | 575 |
| `jls` | cyberlab-aio | `--help` | The Sleuth Kit ver 4.11.1 | 469 |
| `john` | cyberlab-aio | `(no args)` | stat: version: No such file or directory | 1,552 |
| `join` | cyberlab-aio | `--help` | join (GNU coreutils) 9.1 | 2,531 |
| `json_pp` | cyberlab-aio | `--help` | Unknown option: version | 135 |
| `kbxutil` | cyberlab-aio | `--help` | kbxutil (GnuPG) 2.2.40 | 856 |
| `kill` | cyberlab-aio | `--help` | kill from procps-ng 4.0.2 | 519 |
| `last` | cyberlab-aio | `--help` | last from util-linux 2.38.1 | 1,142 |
| `lastb` | cyberlab-aio | `--help` | lastb from util-linux 2.38.1 | 1,143 |
| `lastlog` | cyberlab-aio | `--help` | lastlog: unrecognized option '--version' | 565 |
| `lcf` | cyberlab-aio | `--help` | lcf: unrecognized option '--version' | 668 |
| `ld` | cyberlab-aio | `--help` | GNU ld (GNU Binutils for Debian) 2.40 | 32,569 |
| `ld.bfd` | cyberlab-aio | `--help` | GNU ld (GNU Binutils for Debian) 2.40 | 32,585 |
| `ld.gold` | cyberlab-aio | `--help` | GNU gold (GNU Binutils for Debian 2.40) 1.16 | 22,873 |
| `ld.so` | cyberlab-aio | `--help` | ld.so (Debian GLIBC 2.36-9+deb12u14) stable rele | 2,477 |
| `ldattach` | cyberlab-aio | `--help` | ldattach from util-linux 2.38.1 | 1,341 |
| `ldconfig` | cyberlab-aio | `--help` | ldconfig (Debian GLIBC 2.36-9+deb12u14) 2.36 | 1,134 |
| `ldd` | cyberlab-aio | `--help` | ldd (Debian GLIBC 2.36-9+deb12u14) 2.36 | 440 |
| `less` | cyberlab-aio | `--help` | version: No such file or directory | 13,066 |
| `libnetcfg` | cyberlab-aio | `--help` | /usr/bin/libnetcfg version [unknown] calling Get | 1,002 |
| `link` | cyberlab-aio | `--help` | link (GNU coreutils) 9.1 | 416 |
| `linux32` | cyberlab-aio | `--help` | linux32 from util-linux 2.38.1 | 1,020 |
| `linux64` | cyberlab-aio | `--help` | linux64 from util-linux 2.38.1 | 1,020 |
| `ln` | cyberlab-aio | `--help` | ln (GNU coreutils) 9.1 | 2,880 |
| `lnstat` | cyberlab-aio | `--help` | lnstat Version 6.1.0 | 672 |
| `locale` | cyberlab-aio | `--help` | locale (Debian GLIBC 2.36-9+deb12u14) 2.36 | 679 |
| `localedef` | cyberlab-aio | `--help` | localedef (Debian GLIBC 2.36-9+deb12u14) 2.36 | 2,284 |
| `log2timeline` | cyberlab-aio | `--help` | plaso - log2timeline version 20260512 | 18,612 |
| `log2timeline.py` | cyberlab-aio | `--help` | plaso - log2timeline version 20260512 | 18,762 |
| `logger` | cyberlab-aio | `--help` | logger from util-linux 2.38.1 | 1,688 |
| `logname` | cyberlab-aio | `--help` | logname (GNU coreutils) 9.1 | 358 |
| `logrotate` | cyberlab-aio | `--help` | logrotate 3.21.0 | 824 |
| `logsave` | cyberlab-aio | `--help` |  | 192 |
| `losetup` | cyberlab-aio | `--help` | losetup from util-linux 2.38.1 | 2,079 |
| `lowntfs-3g` | cyberlab-aio | `--help` | lowntfs-3g 2022.10.3 integrated FUSE 28 | 707 |
| `ls` | cyberlab-aio | `--help` | ls (GNU coreutils) 9.1 | 7,729 |
| `lsattr` | cyberlab-aio | `(no args)` | lsattr 1.47.0 (5-Feb-2023) | 159 |
| `lsblk` | cyberlab-aio | `--help` | lsblk from util-linux 2.38.1 | 4,109 |
| `lscpu` | cyberlab-aio | `--help` | lscpu from util-linux 2.38.1 | 2,352 |
| `lsfd` | cyberlab-aio | `--help` | lsfd from util-linux 2.38.1 | 2,524 |
| `lsipc` | cyberlab-aio | `--help` | lsipc from util-linux 2.38.1 | 2,650 |
| `lsirq` | cyberlab-aio | `--help` | lsirq from util-linux 2.38.1 | 574 |
| `lslocks` | cyberlab-aio | `--help` | lslocks from util-linux 2.38.1 | 1,209 |
| `lslogins` | cyberlab-aio | `--help` | lslogins from util-linux 2.38.1 | 2,883 |
| `lsmem` | cyberlab-aio | `--help` | lsmem from util-linux 2.38.1 | 1,125 |
| `lsns` | cyberlab-aio | `--help` | lsns from util-linux 2.38.1 | 1,395 |
| `lspgpot` | cyberlab-aio | `help` |  | 205 |
| `lto-dump` | cyberlab-aio | `--help` | lto-dump: fatal error: open version failed: No s | 65,536 |
| `lto-dump-12` | cyberlab-aio | `--help` | lto-dump-12: fatal error: open version failed: N | 65,536 |
| `lzcat` | cyberlab-aio | `--help` | xz (XZ Utils) 5.4.1 | 1,432 |
| `lzcmp` | cyberlab-aio | `--help` | xzcmp (XZ Utils) 5.4.1 | 349 |
| `lzdiff` | cyberlab-aio | `--help` | xzdiff (XZ Utils) 5.4.1 | 352 |
| `lzegrep` | cyberlab-aio | `--help` | xzegrep (XZ Utils) 5.4.1 | 231 |
| `lzfgrep` | cyberlab-aio | `--help` | xzfgrep (XZ Utils) 5.4.1 | 231 |
| `lzgrep` | cyberlab-aio | `--help` | xzgrep (XZ Utils) 5.4.1 | 227 |
| `lzless` | cyberlab-aio | `--help` | xzless (XZ Utils) 5.4.1 | 184 |
| `lzma` | cyberlab-aio | `--help` | xz (XZ Utils) 5.4.1 | 1,431 |
| `lzmainfo` | cyberlab-aio | `--help` | lzmainfo (XZ Utils) 5.4.1 | 253 |
| `lzmore` | cyberlab-aio | `--help` | xzmore (XZ Utils) 5.4.1 | 147 |
| `mactime` | cyberlab-aio | `--help` | Unknown option: --version | 904 |
| `make` | cyberlab-aio | `--help` | GNU Make 4.3 | 2,713 |
| `markdown-it` | cyberlab-aio | `--help` | markdown-it-py [version 4.2.0] | 707 |
| `mawk` | cyberlab-aio | `(no args)` | mawk: not an option: --version | 1,154 |
| `mcookie` | cyberlab-aio | `--help` | mcookie from util-linux 2.38.1 | 471 |
| `md5sum` | cyberlab-aio | `--help` | md5sum (GNU coreutils) 9.1 | 1,594 |
| `md5sum.textutils` | cyberlab-aio | `--help` | md5sum (GNU coreutils) 9.1 | 1,604 |
| `mdig` | cyberlab-aio | `--help` | Invalid option: --version | 175 |
| `mergecap` | cyberlab-aio | `--help` | Mergecap (Wireshark) 4.0.17 (Git v4.0.17 package | 953 |
| `mesg` | cyberlab-aio | `--help` | mesg from util-linux 2.38.1 | 236 |
| `migrate-pubring-from-classic-gpg` | cyberlab-aio | `--help` | There is no --version/pubring.gpg, no need to mi | 230 |
| `mkdir` | cyberlab-aio | `--help` | mkdir (GNU coreutils) 9.1 | 1,004 |
| `mke2fs` | cyberlab-aio | `--help` | mke2fs 1.47.0 (5-Feb-2023) | 510 |
| `mkfifo` | cyberlab-aio | `--help` | mkfifo (GNU coreutils) 9.1 | 737 |
| `mkfs` | cyberlab-aio | `--help` | mkfs from util-linux 2.38.1 | 570 |
| `mkfs.bfs` | cyberlab-aio | `--help` | mkfs.bfs from util-linux 2.38.1 | 491 |
| `mkfs.cramfs` | cyberlab-aio | `--help` | mkfs.cramfs from util-linux 2.38.1 | 851 |
| `mkfs.ext2` | cyberlab-aio | `--help` | mke2fs 1.47.0 (5-Feb-2023) | 516 |
| `mkfs.ext3` | cyberlab-aio | `--help` | mke2fs 1.47.0 (5-Feb-2023) | 516 |
| `mkfs.ext4` | cyberlab-aio | `--help` | mke2fs 1.47.0 (5-Feb-2023) | 516 |
| `mkfs.minix` | cyberlab-aio | `--help` | mkfs.minix from util-linux 2.38.1 | 613 |
| `mkfs.ntfs` | cyberlab-aio | `--help` | Failed to access 'version': No such file or dire | 1,517 |
| `mknod` | cyberlab-aio | `--help` | mknod (GNU coreutils) 9.1 | 1,328 |
| `mkntfs` | cyberlab-aio | `--help` | Failed to access 'version': No such file or dire | 1,517 |
| `mkswap` | cyberlab-aio | `--help` | mkswap from util-linux 2.38.1 | 729 |
| `mktemp` | cyberlab-aio | `--help` | mktemp (GNU coreutils) 9.1 | 1,567 |
| `mmcat` | cyberlab-aio | `--help` | The Sleuth Kit ver 4.11.1 | 516 |
| `mmls` | cyberlab-aio | `--help` | The Sleuth Kit ver 4.11.1 | 796 |
| `mmstat` | cyberlab-aio | `--help` | The Sleuth Kit ver 4.11.1 | 503 |
| `more` | cyberlab-aio | `--help` | more from util-linux 2.38.1 | 891 |
| `mount` | cyberlab-aio | `--help` | mount from util-linux 2.38.1 (libmount 2.38.1: s | 3,068 |
| `mount.lowntfs-3g` | cyberlab-aio | `--help` | lowntfs-3g 2022.10.3 integrated FUSE 28 | 707 |
| `mount.ntfs` | cyberlab-aio | `--help` | ntfs-3g 2022.10.3 integrated FUSE 28 | 698 |
| `mount.ntfs-3g` | cyberlab-aio | `--help` | ntfs-3g 2022.10.3 integrated FUSE 28 | 698 |
| `mountpoint` | cyberlab-aio | `--help` | mountpoint from util-linux 2.38.1 | 475 |
| `mraptor` | cyberlab-aio | `--help` | MacroRaptor 0.56.2 - http://decalage.info/python | 790 |
| `msodde` | cyberlab-aio | `--help` |  | 1,187 |
| `msoffcrypto-tool` | cyberlab-aio | `--help` |  | 505 |
| `mv` | cyberlab-aio | `--help` | mv (GNU coreutils) 9.1 | 2,116 |
| `namei` | cyberlab-aio | `--help` | namei from util-linux 2.38.1 | 540 |
| `nawk` | cyberlab-aio | `(no args)` | nawk: not an option: --version | 1,154 |
| `ncurses5-config` | cyberlab-aio | `--help` | 6.4.20221231 | 1,265 |
| `ncurses6-config` | cyberlab-aio | `--help` | 6.4.20221231 | 1,265 |
| `ncursesw5-config` | cyberlab-aio | `--help` | 6.4.20221231 | 1,280 |
| `ncursesw6-config` | cyberlab-aio | `--help` | 6.4.20221231 | 1,280 |
| `net-server` | cyberlab-aio | `--help` |  | 2,246 |
| `newusers` | cyberlab-aio | `--help` | newusers: unrecognized option '--version' | 262 |
| `ngrep` | cyberlab-aio | `--help` | ngrep: V1.47.1-git, libpcap version 1.10.3 (with | 1,702 |
| `nice` | cyberlab-aio | `--help` | nice (GNU coreutils) 9.1 | 892 |
| `nisdomainname` | cyberlab-aio | `--help` | hostname 3.23 | 1,487 |
| `nl` | cyberlab-aio | `--help` | nl (GNU coreutils) 9.1 | 1,978 |
| `nm` | cyberlab-aio | `--help` | GNU nm (GNU Binutils for Debian) 2.40 | 2,893 |
| `nmap` | cyberlab-aio | `--help` | Nmap version 7.93 ( https://nmap.org ) | 5,996 |
| `nohup` | cyberlab-aio | `--help` | nohup (GNU coreutils) 9.1 | 875 |
| `nping` | cyberlab-aio | `--help` | Failed to resolve given hostname/IP: version.  N | 6,787 |
| `nproc` | cyberlab-aio | `--help` | nproc (GNU coreutils) 9.1 | 568 |
| `nsenter` | cyberlab-aio | `--help` | nsenter from util-linux 2.38.1 | 1,178 |
| `nslookup` | cyberlab-aio | `help` | *** Invalid option: -version | 332 |
| `nstat` | cyberlab-aio | `--help` | nstat utility, iproute2-6.1.0 | 540 |
| `nsupdate` | cyberlab-aio | `--help` | nsupdate 9.18.49-1~deb12u1-Debian | 193 |
| `ntfs-3g` | cyberlab-aio | `--help` | ntfs-3g 2022.10.3 integrated FUSE 28 | 698 |
| `ntfs-3g.probe` | cyberlab-aio | `--help` | ntfs-3g.probe: Unknown option '--version'. | 282 |
| `ntfscat` | cyberlab-aio | `--help` |  | 563 |
| `ntfsclone` | cyberlab-aio | `--help` | ntfsclone v2022.10.3 (libntfs-3g) | 1,401 |
| `ntfscluster` | cyberlab-aio | `--help` | The device version doesn't exist | 684 |
| `ntfscmp` | cyberlab-aio | `--help` | ntfscmp: unrecognized option '--version' | 386 |
| `ntfscp` | cyberlab-aio | `--help` |  | 699 |
| `ntfsdecrypt` | cyberlab-aio | `--help` |  | 570 |
| `ntfsfallocate` | cyberlab-aio | `--help` | ntfsfallocate v2022.10.3 (libntfs-3g) | 801 |
| `ntfsfix` | cyberlab-aio | `--help` | ntfsfix v2022.10.3 | 519 |
| `ntfsinfo` | cyberlab-aio | `--help` |  | 579 |
| `ntfslabel` | cyberlab-aio | `--help` | The device version doesn't exist | 515 |
| `ntfsls` | cyberlab-aio | `--help` | The device version doesn't exist | 829 |
| `ntfsmove` | cyberlab-aio | `--help` |  | 726 |
| `ntfsrecover` | cyberlab-aio | `--help` | Failed to access 'version': No such file or dire | 846 |
| `ntfsresize` | cyberlab-aio | `--help` | ntfsresize v2022.10.3 (libntfs-3g) | 1,336 |
| `ntfssecaudit` | cyberlab-aio | `--help` | ntfssecaudit 1.5.0 : NTFS security data auditing | 1,257 |
| `ntfstruncate` | cyberlab-aio | `--help` | ntfstruncate v2022.10.3 (libntfs-3g) | 799 |
| `ntfsundelete` | cyberlab-aio | `--help` | The device version doesn't exist | 1,220 |
| `ntfsusermap` | cyberlab-aio | `(no args)` | Could not open "--version" | 203 |
| `ntfswipe` | cyberlab-aio | `--help` | The device version doesn't exist | 1,050 |
| `numbers-to-hex.py` | cyberlab-aio | `--help` | numbers-to-hex.py 0.0.4 | 881 |
| `numbers-to-string.py` | cyberlab-aio | `--help` | numbers-to-string.py 0.0.11 | 1,331 |
| `numfmt` | cyberlab-aio | `--help` | numfmt (GNU coreutils) 9.1 | 4,444 |
| `objcopy` | cyberlab-aio | `--help` | GNU objcopy (GNU Binutils for Debian) 2.40 | 8,429 |
| `objdump` | cyberlab-aio | `--help` | GNU objdump (GNU Binutils for Debian) 2.40 | 7,394 |
| `od` | cyberlab-aio | `--help` | od (GNU coreutils) 9.1 | 3,560 |
| `olebrowse` | cyberlab-aio | `--help` |  | 1,587 |
| `oledir` | cyberlab-aio | `--help` | oledir 0.54 - http://decalage.info/python/oletoo | 594 |
| `oledump` | cyberlab-aio | `--help` | oledump.py 0.0.85 | 2,814 |
| `oledump.py` | cyberlab-aio | `--help` | oledump.py 0.0.85 | 2,814 |
| `olefile` | cyberlab-aio | `--help` | ERROR    Error while parsing file 'version' | 535 |
| `oleid` | cyberlab-aio | `--help` | oleid 0.60.1 - http://decalage.info/oletools | 910 |
| `olemap` | cyberlab-aio | `--help` |  | 1,718 |
| `olemeta` | cyberlab-aio | `--help` | olemeta 0.54 - http://decalage.info/python/oleto | 771 |
| `oleobj` | cyberlab-aio | `--help` | oleobj 0.60.1 - http://decalage.info/oletools | 1,277 |
| `oletimes` | cyberlab-aio | `--help` | oletimes 0.54 - http://decalage.info/python/olet | 773 |
| `olevba` | cyberlab-aio | `--help` | olevba 0.60.2 on Python 3.11.2 - http://decalage | 2,377 |
| `openssl` | cyberlab-aio | `--help` | Invalid command '--version'; type "help" for a l | 2,906 |
| `p7zip` | cyberlab-aio | `--help` | /usr/bin/p7zip: ignoring unknown option --versio | 457 |
| `pager` | cyberlab-aio | `--help` | version: No such file or directory | 13,066 |
| `partx` | cyberlab-aio | `--help` | partx from util-linux 2.38.1 | 1,473 |
| `passwd` | cyberlab-aio | `--help` | passwd: unrecognized option '--version' | 1,230 |
| `paste` | cyberlab-aio | `--help` | paste (GNU coreutils) 9.1 | 787 |
| `patch` | cyberlab-aio | `--help` | GNU patch 2.7.6 | 2,955 |
| `pathchk` | cyberlab-aio | `--help` | pathchk (GNU coreutils) 9.1 | 566 |
| `pcodedmp` | cyberlab-aio | `--help` | pcodedmp version 1.2.6 | 573 |
| `pdb3` | cyberlab-aio | `--help` | Error: version does not exist | 539 |
| `pdb3.11` | cyberlab-aio | `--help` | Error: version does not exist | 539 |
| `pdf-parser` | cyberlab-aio | `--help` | pdf-parser.py 0.7.14 | 2,862 |
| `pdf-parser.py` | cyberlab-aio | `--help` | pdf-parser.py 0.7.14 | 2,862 |
| `pdfattach` | cyberlab-aio | `--help` | pdfattach version 22.12.0 | 530 |
| `pdfdetach` | cyberlab-aio | `--help` | pdfdetach version 22.12.0 | 874 |
| `pdffonts` | cyberlab-aio | `--help` | I/O Error: Couldn't open file '--version': No su | 639 |
| `pdfid` | cyberlab-aio | `--help` | pdfid.py 0.2.10 | 1,700 |
| `pdfid.py` | cyberlab-aio | `--help` | pdfid.py 0.2.10 | 1,700 |
| `pdfimages` | cyberlab-aio | `--help` | pdfimages version 22.12.0 | 1,180 |
| `pdfinfo` | cyberlab-aio | `--help` | I/O Error: Couldn't open file '--version': No su | 1,458 |
| `pdfseparate` | cyberlab-aio | `--help` | pdfseparate version 22.12.0 | 520 |
| `pdfsig` | cyberlab-aio | `-h` | I/O Error: Couldn't open file '--version': No su | 2,001 |
| `pdftocairo` | cyberlab-aio | `--help` | pdftocairo version 22.12.0 | 3,461 |
| `pdftohtml` | cyberlab-aio | `--help` | I/O Error: Couldn't open file '--version': No su | 1,782 |
| `pdftoppm` | cyberlab-aio | `--help` | I/O Error: Couldn't open file '--version': No su | 4,109 |
| `pdftops` | cyberlab-aio | `--help` | I/O Error: Couldn't open file '--version': No su | 3,513 |
| `pdftotext` | cyberlab-aio | `--help` | I/O Error: Couldn't open file '--version': No su | 2,176 |
| `pdfunite` | cyberlab-aio | `--help` | pdfunite version 22.12.0 | 447 |
| `perl` | cyberlab-aio | `--help` | Summary of my perl5 (revision 5 version 36 subve | 2,023 |
| `perl5.36-x86_64-linux-gnu` | cyberlab-aio | `--help` | Summary of my perl5 (revision 5 version 36 subve | 2,044 |
| `perl5.36.0` | cyberlab-aio | `--help` | Summary of my perl5 (revision 5 version 36 subve | 2,029 |
| `perlbug` | cyberlab-aio | `--help` | perlbug version 1.42 | 2,315 |
| `perlivp` | cyberlab-aio | `--help` |  | 360 |
| `perlthanks` | cyberlab-aio | `--help` | perlbug version 1.42 | 2,327 |
| `pgrep` | cyberlab-aio | `--help` | pgrep from procps-ng 4.0.2 | 1,786 |
| `photorec` | cyberlab-aio | `--help` | PhotoRec 7.1, Data Recovery Utility, July 2019 | 405 |
| `piconv` | cyberlab-aio | `--help` | Unknown option: version | 1,276 |
| `pidof` | cyberlab-aio | `-h` |  | 533 |
| `pidwait` | cyberlab-aio | `--help` | pidwait from procps-ng 4.0.2 | 1,592 |
| `pinentry` | cyberlab-aio | `--help` | pinentry-curses (pinentry) 1.2.1 | 1,081 |
| `pinentry-curses` | cyberlab-aio | `--help` | pinentry-curses (pinentry) 1.2.1 | 1,081 |
| `pinfo` | cyberlab-aio | `--help` | plaso - pinfo version 20260512 | 2,702 |
| `pinfo.py` | cyberlab-aio | `--help` | plaso - pinfo version 20260512 | 2,717 |
| `pinky` | cyberlab-aio | `--help` | pinky (GNU coreutils) 9.1 | 1,065 |
| `pip` | cyberlab-aio | `--help` | pip 26.1.2 from /opt/cyberlab-venv/lib/python3.1 | 4,639 |
| `pip2.7` | cyberlab-aio | `--help` | pip 19.2.3 from /usr/local/lib/python2.7/site-pa | 2,901 |
| `pip3` | cyberlab-aio | `--help` | pip 26.1.2 from /opt/cyberlab-venv/lib/python3.1 | 4,640 |
| `pip3.11` | cyberlab-aio | `--help` | pip 26.1.2 from /opt/cyberlab-venv/lib/python3.1 | 4,643 |
| `pivot_root` | cyberlab-aio | `--help` | pivot_root from util-linux 2.38.1 | 188 |
| `pkg-config` | cyberlab-aio | `--help` | 1.8.1 | 5,357 |
| `pkgconf` | cyberlab-aio | `--help` | 1.8.1 | 5,357 |
| `pkill` | cyberlab-aio | `--help` | pkill from procps-ng 4.0.2 | 1,719 |
| `pldd` | cyberlab-aio | `--help` | pldd (Debian GLIBC 2.36-9+deb12u14) 2.36 | 309 |
| `pmap` | cyberlab-aio | `--help` | pmap from procps-ng 4.0.2 | 890 |
| `pod2html` | cyberlab-aio | `--help` | Unknown option: version | 2,048 |
| `pod2man` | cyberlab-aio | `--help` | Unknown option: version | 8,667 |
| `pod2text` | cyberlab-aio | `--help` | Unknown option: version | 5,309 |
| `pod2usage` | cyberlab-aio | `--help` | Unknown option: version | 1,776 |
| `podchecker` | cyberlab-aio | `--help` | Unknown option: version | 550 |
| `pr` | cyberlab-aio | `--help` | pr (GNU coreutils) 9.1 | 4,162 |
| `prefetch` | cyberlab-aio | `--help` |  | 293 |
| `printenv` | cyberlab-aio | `--help` | printenv (GNU coreutils) 9.1 | 734 |
| `printf` | cyberlab-aio | `--help` | printf (GNU coreutils) 9.1 | 1,646 |
| `prlimit` | cyberlab-aio | `--help` | prlimit from util-linux 2.38.1 | 1,817 |
| `prove` | cyberlab-aio | `--help` | TAP::Harness v3.44 and Perl v5.36.0 | 3,059 |
| `ps` | cyberlab-aio | `--help` | ps from procps-ng 4.0.2 | 164 |
| `psort` | cyberlab-aio | `--help` | plaso - psort version 20260512 | 9,968 |
| `psort.py` | cyberlab-aio | `--help` | plaso - psort version 20260512 | 10,029 |
| `pstat` | cyberlab-aio | `--help` | The Sleuth Kit ver 4.11.1 | 496 |
| `ptar` | cyberlab-aio | `--help` | /usr/bin/ptar version [unknown] calling Getopt:: | 1,639 |
| `ptardiff` | cyberlab-aio | `--help` | /usr/bin/ptardiff version [unknown] calling Geto | 652 |
| `ptargrep` | cyberlab-aio | `--help` | Unknown option: version | 4,453 |
| `ptx` | cyberlab-aio | `--help` | ptx (GNU coreutils) 9.1 | 1,831 |
| `pw-inspector` | cyberlab-aio | `--help` |  | 1,173 |
| `pwck` | cyberlab-aio | `--help` | pwck: unrecognized option '--version' | 440 |
| `pwconv` | cyberlab-aio | `--help` | pwconv: unrecognized option '--version' | 157 |
| `pwd` | cyberlab-aio | `--help` | pwd (GNU coreutils) 9.1 | 722 |
| `pwdx` | cyberlab-aio | `--help` | pwdx from procps-ng 4.0.2 | 166 |
| `pwunconv` | cyberlab-aio | `--help` | pwunconv: unrecognized option '--version' | 159 |
| `py3clean` | cyberlab-aio | `--help` | py3clean 3.11.2-1+b1 | 411 |
| `py3compile` | cyberlab-aio | `--help` | py3compile 3.11.2-1+b1 | 1,381 |
| `py3versions` | cyberlab-aio | `--help` | usage: py3versions [-v] [-h] [-d\|--default] [-s\| | 684 |
| `pydoc` | cyberlab-aio | `--help` | no Python documentation found for 'version' | 1,022 |
| `pydoc3` | cyberlab-aio | `--help` | No Python documentation found for 'version'. | 1,230 |
| `pydoc3.11` | cyberlab-aio | `--help` | No Python documentation found for 'version'. | 1,230 |
| `pygettext3` | cyberlab-aio | `--help` | pygettext.py (xgettext for Python) 1.5 | 4,592 |
| `pygettext3.11` | cyberlab-aio | `--help` | pygettext.py (xgettext for Python) 1.5 | 4,592 |
| `pygmentize` | cyberlab-aio | `--help` | Pygments version 2.20.0, (c) 2006-present by Geo | 4,048 |
| `python` | cyberlab-aio | `--help` | Python 3.11.2 | 2,515 |
| `python2` | cyberlab-aio | `--help` | Python 2.7.18 | 2,913 |
| `python2.7` | cyberlab-aio | `--help` | Python 2.7.18 | 2,915 |
| `python3` | cyberlab-aio | `--help` | Python 3.11.2 | 2,516 |
| `python3-config` | cyberlab-aio | `--help` |  | 147 |
| `python3.11` | cyberlab-aio | `--help` | Python 3.11.2 | 2,519 |
| `python3.11-config` | cyberlab-aio | `--help` | Usage: /usr/bin/python3.11-config --prefix\|--exe | 150 |
| `pyxswf` | cyberlab-aio | `--help` | pyxswf 0.54 - http://decalage.info/python/oletoo | 2,224 |
| `r2` | cyberlab-aio | `-h` | 6.1.9-124  r2 | 2,598 |
| `r2agent` | cyberlab-aio | `--help` | r2agent 6.1.9 +1 abi:124 @ linux-x86_64 | 498 |
| `r2pm` | cyberlab-aio | `--help` | r2pm 6.1.9 +1 abi:124 @ linux-x86_64 | 1,518 |
| `r2r` | cyberlab-aio | `--help` | r2r 6.1.9 +1 abi:124 @ linux-x86_64 | 123 |
| `r2sdb` | cyberlab-aio | `-h` | sdb 2.4.8 | 712 |
| `rabin2` | cyberlab-aio | `--help` | rabin2 6.1.9 +1 abi:124 @ linux-x86_64 | 3,071 |
| `radare2` | cyberlab-aio | `-h` | 6.1.9-124  r2 | 2,598 |
| `radiff2` | cyberlab-aio | `-h` | radiff2 6.1.9 +1 abi:124 @ linux-x86_64 | 1,963 |
| `rafind2` | cyberlab-aio | `--help` | rafind2 6.1.9 +1 abi:124 @ linux-x86_64 | 122 |
| `rafs2` | cyberlab-aio | `--help` | rafs2 6.1.9 +1 abi:124 @ linux-x86_64 | 914 |
| `ragg2` | cyberlab-aio | `-h` | ragg2 6.1.9 +1 abi:124 @ linux-x86_64 | 1,927 |
| `rahash2` | cyberlab-aio | `--help` | rahash2 6.1.9 +1 abi:124 @ linux-x86_64 | 1,382 |
| `randpkt` | cyberlab-aio | `--help` | randpkt: unrecognized option: version | 1,166 |
| `ranlib` | cyberlab-aio | `--help` | GNU ranlib (GNU Binutils for Debian) 2.40 | 816 |
| `rapatch2` | cyberlab-aio | `-h` | rapatch2 6.1.9 +1 abi:124 @ linux-x86_64 | 248 |
| `rarun2` | cyberlab-aio | `-h` | rarun2 6.1.9 +1 abi:124 @ linux-x86_64 | 962 |
| `rasign2` | cyberlab-aio | `--help` | rasign2 6.1.9 +1 abi:124 @ linux-x86_64 | 882 |
| `rasm2` | cyberlab-aio | `--help` | rasm2 6.1.9 +1 abi:124 @ linux-x86_64 | 1,757 |
| `ravc2` | cyberlab-aio | `-h` | ravc2 6.1.9 +1 abi:124 @ linux-x86_64 | 739 |
| `rawshark` | cyberlab-aio | `--help` | Rawshark (Wireshark) 4.0.17 (Git v4.0.17 package | 1,827 |
| `rax2` | cyberlab-aio | `--help` | rax2 6.1.9 +1 abi:124 @ linux-x86_64 | 2,927 |
| `rbash` | cyberlab-aio | `--help` | GNU bash, version 5.2.15(1)-release (x86_64-pc-l | 768 |
| `rdma` | cyberlab-aio | `--help` | rdma utility, iproute2-6.1.0 | 237 |
| `readelf` | cyberlab-aio | `--help` | GNU readelf (GNU Binutils for Debian) 2.40 | 4,681 |
| `readelf.py` | cyberlab-aio | `--help` | readelf.py: based on pyelftools 0.33 | 1,637 |
| `readlink` | cyberlab-aio | `--help` | readlink (GNU coreutils) 9.1 | 1,353 |
| `readprofile` | cyberlab-aio | `--help` | readprofile from util-linux 2.38.1 | 900 |
| `realpath` | cyberlab-aio | `--help` | realpath (GNU coreutils) 9.1 | 1,045 |
| `regfexport` | cyberlab-aio | `--help` |  | 762 |
| `regfinfo` | cyberlab-aio | `--help` |  | 717 |
| `regfmount` | cyberlab-aio | `--help` |  | 861 |
| `regipy-diff` | cyberlab-aio | `--help` |  | 153 |
| `regipy-dump` | cyberlab-aio | `--help` |  | 1,223 |
| `regipy-parse-header` | cyberlab-aio | `--help` |  | 128 |
| `regipy-plugins-list` | cyberlab-aio | `help` |  | 124 |
| `regipy-plugins-run` | cyberlab-aio | `--help` |  | 1,034 |
| `regipy-process-transaction-logs` | cyberlab-aio | `--help` |  | 188 |
| `regripper` | cyberlab-aio | `--help` | Unknown option: -version | 1,417 |
| `remove-shell` | cyberlab-aio | `-h` |  | 151 |
| `rename.ul` | cyberlab-aio | `--help` | rename.ul from util-linux 2.38.1 | 540 |
| `renice` | cyberlab-aio | `--help` | renice from util-linux 2.38.1 | 555 |
| `reordercap` | cyberlab-aio | `--help` | Reordercap (Wireshark) 4.0.17 (Git v4.0.17 packa | 397 |
| `reset` | cyberlab-aio | `--help` | ncurses 6.4.20221231 | 562 |
| `resize2fs` | cyberlab-aio | `--help` | resize2fs 1.47.0 (5-Feb-2023) | 177 |
| `resizepart` | cyberlab-aio | `--help` | resizepart from util-linux 2.38.1 | 226 |
| `rev` | cyberlab-aio | `--help` | rev from util-linux 2.38.1 | 167 |
| `rgrep` | cyberlab-aio | `--help` | grep (GNU grep) 3.8 | 4,041 |
| `rich-click` | cyberlab-aio | `--help` | rich-click, version 1.9.8 | 5,138 |
| `rip.pl` | cyberlab-aio | `--help` | Unknown option: -version | 1,417 |
| `rm` | cyberlab-aio | `--help` | rm (GNU coreutils) 9.1 | 2,013 |
| `rmdir` | cyberlab-aio | `--help` | rmdir (GNU coreutils) 9.1 | 731 |
| `rmt` | cyberlab-aio | `--help` | rmt (GNU tar) 1.34 | 498 |
| `rmt-tar` | cyberlab-aio | `--help` | rmt (GNU tar) 1.34 | 502 |
| `roman` | cyberlab-aio | `--help` |  | 270 |
| `routel` | cyberlab-aio | `help` | option --version not recognized | 3,782 |
| `rpcgen` | cyberlab-aio | `--help` | rpcgen (rpcsvc-proto) 1.4.3 | 1,377 |
| `rsakeyfind` | cyberlab-aio | `(no args)` |  | 221 |
| `rtcwake` | cyberlab-aio | `--help` | rtcwake from util-linux 2.38.1 | 896 |
| `rtfobj` | cyberlab-aio | `--help` | rtfobj 0.60.1 on Python 3.11.2 - http://decalage | 1,244 |
| `rtmon` | cyberlab-aio | `help` | Argument "--version" is unknown, try "rtmon help | 203 |
| `rtstat` | cyberlab-aio | `--help` | rtstat Version 6.1.0 | 672 |
| `run-parts` | cyberlab-aio | `--help` | Debian run-parts program, version 5.7 | 1,119 |
| `runcon` | cyberlab-aio | `--help` | runcon (GNU coreutils) 9.1 | 880 |
| `runuser` | cyberlab-aio | `--help` | runuser from util-linux 2.38.1 | 1,256 |
| `rview` | cyberlab-aio | `--help` | VIM - Vi IMproved 9.0 (2022 Jun 28, compiled Feb | 1,995 |
| `savelog` | cyberlab-aio | `--help` | Rotated `version' at Wed Jul 29 08:22:16 AM UTC  | 953 |
| `scalar` | cyberlab-aio | `--help` | git version 2.39.5 | 168 |
| `scalpel` | cyberlab-aio | `-h` | Scalpel version 1.60 | 1,993 |
| `sccainfo` | cyberlab-aio | `--help` |  | 293 |
| `script` | cyberlab-aio | `--help` | script from util-linux 2.38.1 | 1,107 |
| `scriptlive` | cyberlab-aio | `--help` | scriptlive from util-linux 2.38.1 | 642 |
| `scriptreplay` | cyberlab-aio | `--help` | scriptreplay from util-linux 2.38.1 | 918 |
| `sdiff` | cyberlab-aio | `--help` | sdiff (GNU diffutils) 3.8 | 1,831 |
| `sed` | cyberlab-aio | `--help` | sed (GNU sed) 4.9 | 1,837 |
| `sensible-editor` | cyberlab-aio | `--help` | VIM - Vi IMproved 9.0 (2022 Jun 28, compiled Feb | 1,995 |
| `sensible-pager` | cyberlab-aio | `--help` | version: No such file or directory | 13,066 |
| `seq` | cyberlab-aio | `--help` | seq (GNU coreutils) 9.1 | 1,463 |
| `setarch` | cyberlab-aio | `--help` | setarch from util-linux 2.38.1 | 1,093 |
| `setcap` | cyberlab-aio | `--help` |  | 613 |
| `setpriv` | cyberlab-aio | `--help` | setpriv from util-linux 2.38.1 | 1,502 |
| `setsid` | cyberlab-aio | `--help` | setsid from util-linux 2.38.1 | 347 |
| `setterm` | cyberlab-aio | `--help` | setterm from util-linux 2.38.1 | 2,371 |
| `sha1sum` | cyberlab-aio | `--help` | sha1sum (GNU coreutils) 9.1 | 1,600 |
| `sha224sum` | cyberlab-aio | `--help` | sha224sum (GNU coreutils) 9.1 | 1,600 |
| `sha256sum` | cyberlab-aio | `--help` | sha256sum (GNU coreutils) 9.1 | 1,602 |
| `sha384sum` | cyberlab-aio | `--help` | sha384sum (GNU coreutils) 9.1 | 1,602 |
| `sha512sum` | cyberlab-aio | `--help` | sha512sum (GNU coreutils) 9.1 | 1,602 |
| `sharkd` | cyberlab-aio | `--help` |  | 723 |
| `shasum` | cyberlab-aio | `--help` | 6.02 | 1,911 |
| `shred` | cyberlab-aio | `--help` | shred (GNU coreutils) 9.1 | 1,971 |
| `shuf` | cyberlab-aio | `--help` | shuf (GNU coreutils) 9.1 | 1,036 |
| `sigfind` | cyberlab-aio | `--help` | The Sleuth Kit ver 4.11.1 | 393 |
| `sigtool` | cyberlab-aio | `--help` | ClamAV 1.4.3 | 4,407 |
| `size` | cyberlab-aio | `--help` | GNU size (GNU Binutils for Debian) 2.40 | 1,055 |
| `skill` | cyberlab-aio | `--help` | skill from procps-ng 4.0.2 | 1,432 |
| `slabtop` | cyberlab-aio | `--help` | slabtop from procps-ng 4.0.2 | 681 |
| `sleep` | cyberlab-aio | `--help` | sleep (GNU coreutils) 9.1 | 601 |
| `smtpd.py` | cyberlab-aio | `--help` | Python SMTP proxy version 0.2 | 892 |
| `snice` | cyberlab-aio | `--help` | snice from procps-ng 4.0.2 | 1,400 |
| `sort` | cyberlab-aio | `--help` | sort (GNU coreutils) 9.1 | 4,082 |
| `sorter` | cyberlab-aio | `--help` | Unknown option: --version | 1,491 |
| `splain` | cyberlab-aio | `--help` | /usr/bin/splain version 1.39 calling Getopt::Std | 618 |
| `split` | cyberlab-aio | `--help` | split (GNU coreutils) 9.1 | 2,325 |
| `srch_strings` | cyberlab-aio | `--help` | 'version': No such file | 779 |
| `ss` | cyberlab-aio | `--help` | ss utility, iproute2-6.1.0 | 3,143 |
| `ssdeep` | cyberlab-aio | `-h` | 2.14.1 | 915 |
| `start-stop-daemon` | cyberlab-aio | `--help` | start-stop-daemon 1.21.23 for Debian | 3,162 |
| `stat` | cyberlab-aio | `--help` | stat (GNU coreutils) 9.1 | 3,862 |
| `stdbuf` | cyberlab-aio | `--help` | stdbuf (GNU coreutils) 9.1 | 1,409 |
| `streamzip` | cyberlab-aio | `--help` | 1.002 | 1,503 |
| `strings` | cyberlab-aio | `--help` | GNU strings (GNU Binutils for Debian) 2.40 | 1,577 |
| `strip` | cyberlab-aio | `--help` | GNU strip (GNU Binutils for Debian) 2.40 | 2,471 |
| `stty` | cyberlab-aio | `--help` | stty (GNU coreutils) 9.1 | 7,998 |
| `su` | cyberlab-aio | `--help` | su from util-linux 2.38.1 | 1,064 |
| `sudo` | cyberlab-aio | `--help` |  | 3,210 |
| `sudo_logsrvd` | cyberlab-aio | `--help` | sudo_logsrvd version 1.9.13p3 | 383 |
| `sudo_sendlog` | cyberlab-aio | `--help` | sudo_sendlog version 1.9.13p3 | 818 |
| `sudoedit` | cyberlab-aio | `--help` |  | 1,704 |
| `sudoreplay` | cyberlab-aio | `--help` | sudoreplay version 1.9.13p3 | 802 |
| `sulogin` | cyberlab-aio | `--help` | sulogin from util-linux 2.38.1 | 393 |
| `sum` | cyberlab-aio | `--help` | sum (GNU coreutils) 9.1 | 560 |
| `swaplabel` | cyberlab-aio | `--help` | swaplabel from util-linux 2.38.1 | 294 |
| `swapoff` | cyberlab-aio | `--help` | swapoff from util-linux 2.38.1 | 633 |
| `swapon` | cyberlab-aio | `--help` | swapon from util-linux 2.38.1 | 1,877 |
| `switch_root` | cyberlab-aio | `--help` | switch_root from util-linux 2.38.1 | 240 |
| `sync` | cyberlab-aio | `--help` | sync (GNU coreutils) 9.1 | 602 |
| `sysctl` | cyberlab-aio | `--help` | sysctl from procps-ng 4.0.2 | 1,108 |
| `tabs` | cyberlab-aio | `--help` | ncurses 6.4.20221231 | 670 |
| `tabulate` | cyberlab-aio | `--help` | option --version not recognized | 971 |
| `tac` | cyberlab-aio | `--help` | tac (GNU coreutils) 9.1 | 732 |
| `tail` | cyberlab-aio | `--help` | tail (GNU coreutils) 9.1 | 2,776 |
| `tar` | cyberlab-aio | `--help` | tar (GNU tar) 1.34 | 16,662 |
| `tarcat` | cyberlab-aio | `--help` | cat (GNU coreutils) 9.1 | 1,107 |
| `taskset` | cyberlab-aio | `--help` | taskset from util-linux 2.38.1 | 795 |
| `tc` | cyberlab-aio | `-h` | Option "--version" is unknown, try "tc -help". | 401 |
| `tcpflow` | cyberlab-aio | `--help` | TCPFLOW 1.6.1 | 2,597 |
| `tcpxtract` | cyberlab-aio | `--help` | tcpxtract v1.0.1 | 488 |
| `tee` | cyberlab-aio | `--help` | tee (GNU coreutils) 9.1 | 1,169 |
| `tempfile` | cyberlab-aio | `--help` |  | 508 |
| `testdisk` | cyberlab-aio | `--help` | TestDisk 7.1, Data Recovery Utility, July 2019 | 1,154 |
| `text2pcap` | cyberlab-aio | `--help` | Text2pcap (Wireshark) 4.0.17 (Git v4.0.17 packag | 6,450 |
| `tic` | cyberlab-aio | `--help` | ncurses 6.4.20221231 | 1,737 |
| `timeout` | cyberlab-aio | `--help` | timeout (GNU coreutils) 9.1 | 2,057 |
| `tload` | cyberlab-aio | `--help` | tload from procps-ng 4.0.2 | 249 |
| `top` | cyberlab-aio | `--help` | top from procps-ng 4.0.2 | 1,336 |
| `touch` | cyberlab-aio | `--help` | touch (GNU coreutils) 9.1 | 1,579 |
| `tput` | cyberlab-aio | `--help` | ncurses 6.4.20221231 | 433 |
| `tqdm` | cyberlab-aio | `--help` | 4.68.3 | 6,818 |
| `tr` | cyberlab-aio | `--help` | tr (GNU coreutils) 9.1 | 2,575 |
| `true` | cyberlab-aio | `--help` | true (GNU coreutils) 9.1 | 599 |
| `truncate` | cyberlab-aio | `--help` | truncate (GNU coreutils) 9.1 | 1,325 |
| `tset` | cyberlab-aio | `--help` | ncurses 6.4.20221231 | 560 |
| `tshark` | cyberlab-aio | `--help` |  | 9,294 |
| `tsk_comparedir` | cyberlab-aio | `--help` | The Sleuth Kit ver 4.11.1 | 763 |
| `tsk_gettimes` | cyberlab-aio | `--help` | The Sleuth Kit ver 4.11.1 | 551 |
| `tsk_imageinfo` | cyberlab-aio | `--help` | The Sleuth Kit ver 4.11.1 | 318 |
| `tsk_loaddb` | cyberlab-aio | `--help` | The Sleuth Kit ver 4.11.1 | 697 |
| `tsk_recover` | cyberlab-aio | `--help` | The Sleuth Kit ver 4.11.1 | 920 |
| `tsort` | cyberlab-aio | `--help` | tsort (GNU coreutils) 9.1 | 458 |
| `tty` | cyberlab-aio | `--help` | tty (GNU coreutils) 9.1 | 453 |
| `tune2fs` | cyberlab-aio | `--help` |  | 483 |
| `tzselect` | cyberlab-aio | `--help` | tzselect (Debian GLIBC 2.36-9+deb12u14) 2.36 | 704 |
| `ucf` | cyberlab-aio | `--help` | ucf: unrecognized option '--version' | 1,854 |
| `ucfq` | cyberlab-aio | `--help` | Unknown option: version | 417 |
| `ucfr` | cyberlab-aio | `--help` | ucfr: unrecognized option '--version' | 912 |
| `uclampset` | cyberlab-aio | `--help` | uclampset from util-linux 2.38.1 | 706 |
| `umount` | cyberlab-aio | `--help` | umount from util-linux 2.38.1 (libmount 2.38.1:  | 1,306 |
| `uname` | cyberlab-aio | `--help` | uname (GNU coreutils) 9.1 | 988 |
| `uncompress` | cyberlab-aio | `--help` | gunzip (gzip) 1.12 | 1,063 |
| `unexpand` | cyberlab-aio | `--help` | unexpand (GNU coreutils) 9.1 | 1,184 |
| `uniq` | cyberlab-aio | `--help` | uniq (GNU coreutils) 9.1 | 1,744 |
| `unlink` | cyberlab-aio | `--help` | unlink (GNU coreutils) 9.1 | 398 |
| `unlzma` | cyberlab-aio | `--help` | xz (XZ Utils) 5.4.1 | 1,433 |
| `unshare` | cyberlab-aio | `--help` | unshare from util-linux 2.38.1 | 2,236 |
| `unxz` | cyberlab-aio | `--help` | xz (XZ Utils) 5.4.1 | 1,431 |
| `unzip` | cyberlab-aio | `--help` | UnZip 6.00 of 20 April 2009, by Debian. Original | 1,509 |
| `unzipsfx` | cyberlab-aio | `--help` | UnZipSFX 6.00 of 20 April 2009, by Info-ZIP (htt | 141 |
| `update-alternatives` | cyberlab-aio | `--help` | Debian update-alternatives version 1.21.23. | 2,335 |
| `update-ca-certificates` | cyberlab-aio | `(no args)` |  | 124 |
| `update-catalog` | cyberlab-aio | `--help` |  | 485 |
| `update-locale` | cyberlab-aio | `--help` | Unknown option: version | 379 |
| `update-passwd` | cyberlab-aio | `--help` | update-passwd 3.6.1 | 1,013 |
| `update-rc.d` | cyberlab-aio | `--help` |  | 277 |
| `update-shells` | cyberlab-aio | `--help` | unrecognized option --version | 180 |
| `uptime` | cyberlab-aio | `--help` | uptime from procps-ng 4.0.2 | 240 |
| `upx` | cyberlab-aio | `--help` | upx 4.2.4 | 5,655 |
| `useradd` | cyberlab-aio | `--help` | useradd: unrecognized option '--version' | 2,252 |
| `userdel` | cyberlab-aio | `--help` | userdel: unrecognized option '--version' | 612 |
| `usermod` | cyberlab-aio | `--help` | usermod: unrecognized option '--version' | 2,098 |
| `users` | cyberlab-aio | `--help` | users (GNU coreutils) 9.1 | 465 |
| `usnjls` | cyberlab-aio | `--help` | The Sleuth Kit ver 4.11.1 | 559 |
| `utmpdump` | cyberlab-aio | `--help` | utmpdump from util-linux 2.38.1 | 386 |
| `vdbbin` | cyberlab-aio | `--help` |  | 1,025 |
| `vdir` | cyberlab-aio | `--help` | vdir (GNU coreutils) 9.1 | 7,735 |
| `vdpa` | cyberlab-aio | `--help` | vdpa: unrecognized option '--version' | 158 |
| `vi` | cyberlab-aio | `--help` | VIM - Vi IMproved 9.0 (2022 Jun 28, compiled Feb | 1,995 |
| `view` | cyberlab-aio | `--help` | VIM - Vi IMproved 9.0 (2022 Jun 28, compiled Feb | 1,995 |
| `vigr` | cyberlab-aio | `--help` | vigr: unrecognized option '--version' | 367 |
| `vim.tiny` | cyberlab-aio | `--help` | VIM - Vi IMproved 9.0 (2022 Jun 28, compiled Feb | 1,995 |
| `vipw` | cyberlab-aio | `--help` | vipw: unrecognized option '--version' | 367 |
| `visudo` | cyberlab-aio | `--help` | visudo version 1.9.13p3 | 481 |
| `vivbin` | cyberlab-aio | `--help` |  | 1,851 |
| `vivserver` | cyberlab-aio | `--help` | /data/version is not a valid directory! | 300 |
| `vmstat` | cyberlab-aio | `--help` | vmstat from procps-ng 4.0.2 | 722 |
| `vol` | cyberlab-aio | `--help` | INFO     volatility3.cli: Volatility plugins pat | 26,683 |
| `volatility3` | cyberlab-aio | `--help` | INFO     volatility3.cli: Volatility plugins pat | 26,790 |
| `volshell` | cyberlab-aio | `--help` | INFO     root        : Volatility plugins path:  | 3,215 |
| `vshadowdebug` | cyberlab-aio | `--help` |  | 359 |
| `vshadowinfo` | cyberlab-aio | `--help` |  | 434 |
| `vshadowmount` | cyberlab-aio | `--help` |  | 640 |
| `w` | cyberlab-aio | `--help` | w from procps-ng 4.0.2 | 449 |
| `wall` | cyberlab-aio | `--help` | wall from util-linux 2.38.1 | 369 |
| `watch` | cyberlab-aio | `--help` | watch from procps-ng 4.0.2 | 887 |
| `watchgnupg` | cyberlab-aio | `--help` | watchgnupg (GnuPG) 2.2.40 | 798 |
| `wc` | cyberlab-aio | `--help` | wc (GNU coreutils) 9.1 | 1,212 |
| `wdctl` | cyberlab-aio | `--help` | wdctl from util-linux 2.38.1 | 1,101 |
| `wget` | cyberlab-aio | `--help` | GNU Wget 1.21.3 built on linux-gnu. | 13,243 |
| `wheel` | cyberlab-aio | `--help` | usage: wheel [-h] {unpack,pack,convert,tags,info | 570 |
| `whereis` | cyberlab-aio | `--help` | whereis from util-linux 2.38.1 | 594 |
| `who` | cyberlab-aio | `--help` | who (GNU coreutils) 9.1 | 1,541 |
| `whoami` | cyberlab-aio | `--help` | whoami (GNU coreutils) 9.1 | 412 |
| `wipefs` | cyberlab-aio | `--help` | wipefs from util-linux 2.38.1 | 1,208 |
| `x86_64` | cyberlab-aio | `--help` | x86_64 from util-linux 2.38.1 | 1,019 |
| `x86_64-linux-gnu-addr2line` | cyberlab-aio | `--help` | GNU addr2line (GNU Binutils for Debian) 2.40 | 1,313 |
| `x86_64-linux-gnu-ar` | cyberlab-aio | `--help` | GNU ar (GNU Binutils for Debian) 2.40 | 2,229 |
| `x86_64-linux-gnu-as` | cyberlab-aio | `--help` | GNU assembler (GNU Binutils for Debian) 2.40 | 10,870 |
| `x86_64-linux-gnu-c++filt` | cyberlab-aio | `--help` | GNU c++filt (GNU Binutils for Debian) 2.40 | 1,023 |
| `x86_64-linux-gnu-cpp` | cyberlab-aio | `--help` | x86_64-linux-gnu-cpp (Debian 12.2.0-14+deb12u1)  | 4,124 |
| `x86_64-linux-gnu-cpp-12` | cyberlab-aio | `--help` | x86_64-linux-gnu-cpp-12 (Debian 12.2.0-14+deb12u | 4,130 |
| `x86_64-linux-gnu-dwp` | cyberlab-aio | `--help` | GNU dwp (GNU Binutils for Debian) 2.40 | 442 |
| `x86_64-linux-gnu-elfedit` | cyberlab-aio | `--help` | GNU elfedit (GNU Binutils for Debian) 2.40 | 1,277 |
| `x86_64-linux-gnu-g++` | cyberlab-aio | `--help` | x86_64-linux-gnu-g++ (Debian 12.2.0-14+deb12u1)  | 4,124 |
| `x86_64-linux-gnu-g++-12` | cyberlab-aio | `--help` | x86_64-linux-gnu-g++-12 (Debian 12.2.0-14+deb12u | 4,130 |
| `x86_64-linux-gnu-gcc` | cyberlab-aio | `--help` | x86_64-linux-gnu-gcc (Debian 12.2.0-14+deb12u1)  | 4,124 |
| `x86_64-linux-gnu-gcc-12` | cyberlab-aio | `--help` | x86_64-linux-gnu-gcc-12 (Debian 12.2.0-14+deb12u | 4,130 |
| `x86_64-linux-gnu-gcc-ar` | cyberlab-aio | `--help` | GNU ar (GNU Binutils for Debian) 2.40 | 2,205 |
| `x86_64-linux-gnu-gcc-ar-12` | cyberlab-aio | `--help` | GNU ar (GNU Binutils for Debian) 2.40 | 2,205 |
| `x86_64-linux-gnu-gcc-nm` | cyberlab-aio | `--help` | GNU nm (GNU Binutils for Debian) 2.40 | 2,911 |
| `x86_64-linux-gnu-gcc-nm-12` | cyberlab-aio | `--help` | GNU nm (GNU Binutils for Debian) 2.40 | 2,911 |
| `x86_64-linux-gnu-gcc-ranlib` | cyberlab-aio | `--help` | GNU ranlib (GNU Binutils for Debian) 2.40 | 834 |
| `x86_64-linux-gnu-gcc-ranlib-12` | cyberlab-aio | `--help` | GNU ranlib (GNU Binutils for Debian) 2.40 | 834 |
| `x86_64-linux-gnu-gcov` | cyberlab-aio | `--help` | gcov (Debian 12.2.0-14+deb12u1) 12.2.0 | 1,993 |
| `x86_64-linux-gnu-gcov-12` | cyberlab-aio | `--help` | gcov (Debian 12.2.0-14+deb12u1) 12.2.0 | 1,993 |
| `x86_64-linux-gnu-gcov-dump` | cyberlab-aio | `--help` | gcov-dump (Debian 12.2.0-14+deb12u1) 12.2.0 | 392 |
| `x86_64-linux-gnu-gcov-dump-12` | cyberlab-aio | `--help` | gcov-dump (Debian 12.2.0-14+deb12u1) 12.2.0 | 392 |
| `x86_64-linux-gnu-gcov-tool` | cyberlab-aio | `--help` | x86_64-linux-gnu-gcov-tool (Debian 12.2.0-14+deb | 1,367 |
| `x86_64-linux-gnu-gcov-tool-12` | cyberlab-aio | `--help` | x86_64-linux-gnu-gcov-tool-12 (Debian 12.2.0-14+ | 1,370 |
| `x86_64-linux-gnu-gold` | cyberlab-aio | `--help` | GNU gold (GNU Binutils for Debian 2.40) 1.16 | 22,915 |
| `x86_64-linux-gnu-gp-archive` | cyberlab-aio | `--help` | GNU x86_64-linux-gnu-gp-archive binutils version | 2,397 |
| `x86_64-linux-gnu-gp-collect-app` | cyberlab-aio | `--help` | GNU x86_64-linux-gnu-gp-collect-app binutils ver | 4,392 |
| `x86_64-linux-gnu-gp-display-html` | cyberlab-aio | `--help` | gp-display-html GNU binutils version 2.40.00 | 2,761 |
| `x86_64-linux-gnu-gp-display-src` | cyberlab-aio | `--help` | GNU x86_64-linux-gnu-gp-display-src binutils ver | 1,571 |
| `x86_64-linux-gnu-gp-display-text` | cyberlab-aio | `--help` | GNU x86_64-linux-gnu-gp-display-text binutils ve | 1,554 |
| `x86_64-linux-gnu-gprof` | cyberlab-aio | `--help` | GNU gprof (GNU Binutils for Debian) 2.40 | 838 |
| `x86_64-linux-gnu-gprofng` | cyberlab-aio | `--help` | GNU x86_64-linux-gnu-gprofng binutils version 2. | 3,287 |
| `x86_64-linux-gnu-ld` | cyberlab-aio | `--help` | GNU ld (GNU Binutils for Debian) 2.40 | 32,637 |
| `x86_64-linux-gnu-ld.bfd` | cyberlab-aio | `--help` | GNU ld (GNU Binutils for Debian) 2.40 | 32,653 |
| `x86_64-linux-gnu-ld.gold` | cyberlab-aio | `--help` | GNU gold (GNU Binutils for Debian 2.40) 1.16 | 22,924 |
| `x86_64-linux-gnu-lto-dump` | cyberlab-aio | `--help` | x86_64-linux-gnu-lto-dump: error: version: file  | 65,536 |
| `x86_64-linux-gnu-lto-dump-12` | cyberlab-aio | `--help` | x86_64-linux-gnu-lto-dump-12: error: version: fi | 65,536 |
| `x86_64-linux-gnu-nm` | cyberlab-aio | `--help` | GNU nm (GNU Binutils for Debian) 2.40 | 2,927 |
| `x86_64-linux-gnu-objcopy` | cyberlab-aio | `--help` | GNU objcopy (GNU Binutils for Debian) 2.40 | 8,463 |
| `x86_64-linux-gnu-objdump` | cyberlab-aio | `--help` | GNU objdump (GNU Binutils for Debian) 2.40 | 7,445 |
| `x86_64-linux-gnu-pkg-config` | cyberlab-aio | `--help` | 1.8.1 | 5,357 |
| `x86_64-linux-gnu-pkgconf` | cyberlab-aio | `--help` | 1.8.1 | 5,357 |
| `x86_64-linux-gnu-python3-config` | cyberlab-aio | `--help` |  | 164 |
| `x86_64-linux-gnu-python3.11-config` | cyberlab-aio | `--help` | Usage: /usr/bin/x86_64-linux-gnu-python3.11-conf | 167 |
| `x86_64-linux-gnu-ranlib` | cyberlab-aio | `--help` | GNU ranlib (GNU Binutils for Debian) 2.40 | 850 |
| `x86_64-linux-gnu-readelf` | cyberlab-aio | `--help` | GNU readelf (GNU Binutils for Debian) 2.40 | 4,681 |
| `x86_64-linux-gnu-size` | cyberlab-aio | `--help` | GNU size (GNU Binutils for Debian) 2.40 | 1,089 |
| `x86_64-linux-gnu-strings` | cyberlab-aio | `--help` | GNU strings (GNU Binutils for Debian) 2.40 | 1,611 |
| `x86_64-linux-gnu-strip` | cyberlab-aio | `--help` | GNU strip (GNU Binutils for Debian) 2.40 | 2,505 |
| `xargs` | cyberlab-aio | `--help` | xargs (GNU findutils) 4.9.0 | 3,120 |
| `xlmdeobfuscator` | cyberlab-aio | `--help` |  | 3,820 |
| `xortool` | cyberlab-aio | `--help` | 1.1.0 | 1,670 |
| `xortool-xor` | cyberlab-aio | `--help` | error: option --version not recognized | 481 |
| `xsubpp` | cyberlab-aio | `--help` | Unknown option: version | 205 |
| `xxd` | cyberlab-aio | `--help` |  | 1,344 |
| `xz` | cyberlab-aio | `--help` | xz (XZ Utils) 5.4.1 | 1,429 |
| `xzcat` | cyberlab-aio | `--help` | xz (XZ Utils) 5.4.1 | 1,432 |
| `xzcmp` | cyberlab-aio | `--help` | xzcmp (XZ Utils) 5.4.1 | 349 |
| `xzdiff` | cyberlab-aio | `--help` | xzdiff (XZ Utils) 5.4.1 | 352 |
| `xzegrep` | cyberlab-aio | `--help` | xzegrep (XZ Utils) 5.4.1 | 231 |
| `xzfgrep` | cyberlab-aio | `--help` | xzfgrep (XZ Utils) 5.4.1 | 231 |
| `xzgrep` | cyberlab-aio | `--help` | xzgrep (XZ Utils) 5.4.1 | 227 |
| `xzless` | cyberlab-aio | `--help` | xzless (XZ Utils) 5.4.1 | 184 |
| `xzmore` | cyberlab-aio | `--help` | xzmore (XZ Utils) 5.4.1 | 147 |
| `yara` | cyberlab-aio | `--help` | 4.2.3 | 2,552 |
| `yarac` | cyberlab-aio | `--help` | 4.2.3 | 613 |
| `yes` | cyberlab-aio | `--help` | yes (GNU coreutils) 9.1 | 401 |
| `ypdomainname` | cyberlab-aio | `--help` | hostname 3.23 | 1,487 |
| `zcat` | cyberlab-aio | `--help` | zcat (gzip) 1.12 | 707 |
| `zcmp` | cyberlab-aio | `--help` | zcmp (gzip) 1.12 | 375 |
| `zdiff` | cyberlab-aio | `--help` | zdiff (gzip) 1.12 | 314 |
| `zdump` | cyberlab-aio | `--help` | zdump (Debian GLIBC 2.36-9+deb12u14) 2.36 | 471 |
| `zegrep` | cyberlab-aio | `--help` | zgrep (gzip) 1.12 | 453 |
| `zfgrep` | cyberlab-aio | `--help` | zgrep (gzip) 1.12 | 453 |
| `zforce` | cyberlab-aio | `--help` | zforce (gzip) 1.12 | 157 |
| `zgrep` | cyberlab-aio | `--help` | zgrep (gzip) 1.12 | 453 |
| `zic` | cyberlab-aio | `--help` | zic (Debian GLIBC 2.36-9+deb12u14) 2.36 | 254 |
| `zipdetails` | cyberlab-aio | `--help` | 2.104 | 685 |
| `zipdump` | cyberlab-aio | `--help` | zipdump.py 0.0.35 | 2,830 |
| `zipgrep` | cyberlab-aio | `--help` |  | 131 |
| `zipinfo` | cyberlab-aio | `--help` | ZipInfo 3.00 of 20 April 2009, by Greg Roelofs a | 1,035 |
| `zless` | cyberlab-aio | `--help` | zless (gzip) 1.12 | 195 |
| `zmore` | cyberlab-aio | `--help` | zmore (gzip) 1.12 | 158 |
| `znew` | cyberlab-aio | `--help` | znew (gzip) 1.12 | 649 |
| `zramctl` | cyberlab-aio | `--help` | zramctl from util-linux 2.38.1 | 1,693 |

## Present, but no usable help text

These exist in a container but print nothing useful for `--help`. Most are GUI apps or need arguments first. They get workflow pages, not flag tables.

`Activate.ps1`, `VSCMount`, `activate`, `activate.csh`, `activate.fish`, `addgnupghome`, `affrecover`, `applygnupgdefaults`, `bzcmp`, `bzdiff`, `bzegrep`, `bzexe`, `bzfgrep`, `bzgrep`, `chattr`, `cron`, `dash`, `deb-systemd-invoke`, `debconf-apt-progress`, `disktype`, `dpkg-fsys-usrunmess`, `e2freefrag`, `e2label`, `e2mmpstatus`, `exiftool`, `faillock`, `filefrag`, `fstab-decode`, `funzip`, `git-shell`, `helpztags`, `hivexget`, `hivexml`, `hydra-wizard`, `idle`, `install-sgmlcatalog`, `installkernel`, `jpeg_extract`, `killall5`, `lessecho`, `lessfile`, `lesskey`, `lesspipe`, `locale-gen`, `login`, `mailer`, `make-first-existing-target`, `mkhomedir_helper`, `mklost+found`, `mmdbresolve`, `mount.fuse`, `mount.fuse3`, `newgrp`, `nologin`, `pam-auth-update`, `pam_getenv`, `pam_namespace_helper`, `pam_timestamp_check`, `perldoc`, `pl2pm`, `policy-rc.d`, `pwhistory_helper`, `python2.7-config`, `r2p`, `rtacct`, `runxlrd2.py`, `select-editor`, `sensible-browser`, `service`, `set`, `sg`, `sh`, `shadowconfig`, `test`, `tipc`, `toe`, `unafs`, `unique`, `unix_chkpwd`, `unix_update`, `unshadow`, `update-mime-database`, `validlocale`, `which`, `which.debianutils`

## Not available in a container

773 candidates were absent. This includes Windows-only (FLARE-VM), GUI-only, appliance services, and names that were never real commands (package names that do not map to a binary).

<details><summary>Full list</summary>

`010editor`, `0trace`, `1768.py`, `7-zip`, `7zip`, `X11`, `above`, `absent`, `accept-all-ips`, `advanced-installer`, `aesfix`, `aeskeyfinder`, `afl++`, `androguard`, `androidprojectcreator`, `angr`, `anomy`, `apache-users`, `apache2`, `apimonitor`, `apkid`, `apktool`, `armitage`, `arping`, `asar`, `autoit-ripper`, `autopsy`, `avfs`, `aws-cli`, `baksmali`, `balbuzard`, `bbcrack`, `bbharvest`, `bbtrans`, `bearcommander`, `bearparser`, `bed`, `beef-xss`, `bettercap`, `binaryninja`, `bindiff`, `binee`, `binwalk3`, `bless`, `blobrunner`, `blobrunner64`, `blt`, `box-export`, `box-js`, `braa`, `brxor.py`, `burp-suite-community-edition`, `burpsuite`, `bytecode-viewer`, `bytecodeviewer`, `bytehist`, `cadaver`, `capa-explorer-web`, `cewl`, `cfr`, `chepy`, `chkrootkit`, `chntpw`, `chrome.extensions`, `chromium-browser`, `cisco-global-exploiter`, `cisco-ocs`, `cisco-torch`, `clamdscan`, `clang`, `claude-code`, `cmder`, `cmospwd`, `code`, `codetrack`, `commix`, `convert`, `copy-router-config`, `crackle`, `creddump7`, `crunch`, `cryptcat`, `cryptotester`, `cs-analyze-processdump.py`, `cs-decrypt-metadata.py`, `cs-extract-key.py`, `cs-parse-traffic.py`, `csce`, `cut-bytes.py`, `cutter`, `cutycapt`, `cygwin`, `cymothoa`, `d2j-dex2jar`, `darkstat`, `davtest`, `dbd`, `dc3-mwcp`, `ddrescue`, `de4dot`, `de4dot-cex`, `debloat`, `decai`, `decode-vbe.py`, `decompyle++`, `default-jre`, `default-mysql-server`, `dependencywalker`, `dex2jar`, `dexray`, `dhcpig`, `didier-stevens-beta`, `didier-stevens-suite`, `dirb`, `dirbuster`, `disitool`, `disitool.py`, `display`, `dissect`, `dll-to-exe`, `dllcharacteristics.py`, `dmitry`, `dnfile`, `dnlib`, `dns2tcp`, `dnschef`, `dnsenum`, `dnslib`, `dnsmap`, `dnspyex`, `dnsrecon`, `dnsresolver.py`, `dnstracer`, `dnswalk`, `docker`, `domainstats`, `dos2unix`, `dotdotpwn`, `dotdumper`, `dotnet3.5`, `dotnetfile`, `driftnet`, `droidlysis`, `dsniff`, `dumpzilla`, `e2fsprogs`, `edb`, `edb-debugger`, `elastalert-2`, `elastic-agent`, `elastic-fleet`, `elasticsearch`, `emldump.py`, `ent`, `enum4linux`, `enumiax`, `epic-irc-client`, `epic5`, `etc`, `etherape`, `ettercap-graphical`, `evilclippy`, `evince`, `ex_pe_xor.py`, `exe2hexbat`, `exeinfope`, `exfat-extras`, `exfat-fuse`, `exif`, `exifprobe`, `exiv2`, `exploitdb`, `explorersuite`, `ext3grep`, `ext4magic`, `extract_msg`, `extreme_dumper`, `extundelete`, `eyewitness`, `ezviewer`, `fakedns`, `fakemail`, `fakenet-ng`, `fcrackzip`, `fdupes`, `feh`, `ferret-sidejack`, `fiddler`, `fierce`, `fiked`, `file-magic.py`, `filebeat`, `firefox`, `firewalk`, `firmware-mod-kit`, `flex`, `forensic-artifacts`, `forensics-colorize`, `format-bytes.py`, `fping`, `fragrouter`, `freerdp3-x11`, `freqserver`, `ftester`, `galculator`, `galleta`, `garbageman`, `gawk`, `gdb`, `gddrescue`, `ghex`, `ghidra`, `ghidrassistmcp`, `gnome-calculator`, `gnu-project-debugger`, `gnu-wget`, `gootloaderautojsdecode.py`, `goresym`, `gostringungarbler`, `gpart`, `gparted`, `gpp-decrypt`, `grafana`, `graphviz`, `grepcidr`, `grokevt`, `gthumb`, `guymager`, `gvm`, `gzrt`, `hachoir`, `hachoir-grep`, `hachoir-metadata`, `hachoir-strip`, `hachoir-wx`, `hakrawler`, `hamster-sidejack`, `hash-id`, `hash-id.py`, `hash-identifier`, `hashcat-utils`, `hashdeep`, `hashid`, `hashmyfiles`, `heartleech`, `hex-to-bin.py`, `hexedit`, `hexinject`, `hivexregedit`, `hollowshunter`, `hping3`, `httprint`, `httrack`, `hxd`, `hydra-gtk`, `iaxflood`, `ibus`, `ibus-setup`, `ida.plugin.capa`, `ida.plugin.comida`, `ida.plugin.delphihelper`, `ida.plugin.dereferencing`, `ida.plugin.diaphora`, `ida.plugin.flare`, `ida.plugin.flare-emu`, `ida.plugin.hashdb`, `ida.plugin.hrtng`, `ida.plugin.ifl`, `ida.plugin.xray`, `ida.plugin.xrefer`, `idafree`, `idr`, `idx_parser.py`, `ifpstools`, `ike-scan`, `ilm`, `ilspy`, `imagemagick`, `influxdb`, `info-zip`, `init`, `innoextract`, `innounp`, `inspircd-3`, `internet_detector`, `intrace`, `inviteflood`, `iodine`, `ipwhois`, `ipython`, `ipython3`, `irpas`, `isd`, `isr-evilgrade`, `jadx`, `jadx-gui`, `java-idx-parser`, `javascript-deobfuscator`, `javasnoop`, `javassist`, `jboss-autopwn`, `jd-gui`, `jd-gui-java-decompiler`, `johnny`, `joomscan`, `jq`, `js`, `js-ascii`, `js-beautifier`, `js-beautify`, `js-deobfuscator`, `js-file`, `js_unshroud`, `jsql-injection`, `jstillery`, `kdiff3`, `keystone`, `kibana`, `kpartx`, `laudanum`, `lbd`, `legion`, `lft`, `lief`, `list-cs-settings`, `logstash`, `ltrace`, `lvm2`, `lynis`, `mac-robber`, `mac2unix`, `macchanger`, `magicrescue`, `magika`, `magnus`, `mail-parser`, `malcat-lite`, `malchive`, `maltego`, `malware-jail`, `malwoverview`, `managerhype`, `manalyze`, `map`, `maskprocessor`, `masscan`, `mbcscan`, `mbcscan.py`, `md5deep`, `mdadm`, `mdbtools`, `medusa`, `memdump`, `mermaid-viewer`, `metacam`, `metagoofil`, `metasploit-framework`, `microsoft-office`, `mimikatz`, `miredo`, `missidentify`, `mitmdump`, `mitmproxy`, `mitmweb`, `mogrify`, `monitor-network`, `monodis`, `msfpc`, `msg-extractor`, `msgconvert`, `msoffcrypto-crack.py`, `msoffice-crypt`, `mtd-utils`, `mwcp`, `myip`, `myjson-filter.py`, `myrescue`, `name-that-hash`, `nasm`, `nasty`, `nautilus`, `nbd-client`, `nbtscan`, `nc`, `ncat`, `ncrack`, `net-reactor-slayer`, `netcat`, `netdiscover`, `netmask`, `netpbm`, `netsed`, `netsniff-ng`, `network-miner-free-edition`, `networkminer`, `netwox`, `nfdump`, `nginx`, `nikto`, `nishang`, `nomorexor.py`, `notepadplusplus`, `notepadpp.plugin.compare`, `notepadpp.plugin.jstool`, `notepadpp.plugin.xmltools`, `nsrllookup`, `nth`, `obfuscator-io-deobfuscator`, `objects.js`, `offvis`, `ofs2rva`, `ohrwurm`, `okular`, `olecfexport`, `olecfinfo`, `olecfmount`, `ollydbg`, `onboard`, `onedump.py`, `onenoteanalyzer`, `onesixtyone`, `onion-ai-assistant`, `open-iscsi`, `opencanary`, `opencode`, `openjdk`, `openssh`, `ophcrack`, `ophcrack-cli`, `orca`, `origamindee`, `oscanner`, `osquery`, `outguess`, `owasp-mantra-ff`, `p0f`, `p7zip-full`, `pack`, `pack2`, `padbuster`, `paros`, `parted`, `pasco`, `passing-the-hash`, `patator`, `pcode2code`, `pdbresym`, `pdfcop`, `pdfcrack`, `pdfdecompress`, `pdfdecrypt`, `pdfextract`, `pdfresurrect`, `pdfstreamdumper`, `pdftk`, `pdftk-java`, `pdftool.py`, `pdg`, `pdnstool`, `pe-tree`, `pe_unmapper`, `peass`, `pebear`, `pecheck.py`, `pedis`, `pedump`, `peepdf-3`, `pefile`, `peframe`, `pehash`, `peid`, `peldd`, `pepack`, `peres`, `pescan`, `pesec`, `pesieve`, `pestr`, `pestudio`, `pev`, `phonon`, `php`, `php-mysql`, `pipal`, `pkg-unpacker`, `playbook`, `pma-labs`, `polarproxy`, `polenum`, `portex`, `powershell`, `powershell-core`, `powersploit`, `procdot`, `processdump`, `procmonmcp`, `procyon`, `protos-sip`, `proxychains4`, `proxytunnel`, `psnotify`, `pst-utils`, `psteal.py`, `ptunnel`, `pv`, `pwnat`, `pwsh`, `pycdas`, `pycdc`, `pyelftools`, `pyinstaller-extractor`, `pyinstxtractor-ng`, `pyinstxtractor.py`, `pylingual`, `qemu`, `qemu-utils`, `qiling`, `qpdf`, `qsslcaudit`, `r2ai`, `r2pipe`, `rainbowcrack`, `rar`, `rar2john`, `rarcrack`, `rat-king-parser`, `rcracki-mt`, `re-search.py`, `readpe`, `rebind`, `recaf`, `recon-ng`, `recoverdm`, `recoverjpeg`, `recstudio`, `redis`, `redress`, `redsocks`, `reg_export`, `regcool`, `registry-diff`, `reglookup`, `regshot`, `remnux-installer`, `remnux-mcp-server`, `rephrase`, `resourcehacker`, `responder`, `restrict-egress`, `rhino-debugger`, `rifiuti`, `rifiuti2`, `rip`, `rizin`, `rizin-cutter`, `rkhunter`, `rsakeyfinder`, `rsmangler`, `rtfdump.py`, `rtpbreak`, `rtpflood`, `rtpinsertsound`, `rtpmixsound`, `rundotnetdll`, `runsc`, `rva2ofs`, `rz-bin`, `rz-find`, `rz-ghidra`, `safecopy`, `samdump2`, `sandfly-processdecloak`, `sbd`, `scdbg`, `scite`, `sclauncher`, `sclauncher64`, `scrounge-ntfs`, `sctpscan`, `seclists`, `security-onion-console`, `sensoroni`, `sets.py`, `sfextract`, `sftp`, `sfuzz`, `sha256deep`, `shcode2exe`, `shellcode2exe.bat`, `shellcode_launcher`, `shellnoob`, `shellter`, `sidguesser`, `siege`, `signsrch`, `silversearcher-ag`, `siparmyknife`, `sipcrack`, `sipp`, `sipsak`, `sipvicious`, `skipfish`, `sleuth-kit`, `slowhttptest`, `smbmap`, `smtp-user-enum`, `sniffjoke`, `snmpcheck`, `so-apt-cacher-ng`, `so-firewall`, `so-idstools`, `socat`, `sortcanon.py`, `speakeasy`, `spidermonkey`, `spike`, `sqldict`, `sqlite`, `sqlite3`, `sqlitebrowser`, `sqlmap`, `sqlninja`, `sqlsus`, `ssh`, `sshpass`, `ssldump`, `sslh`, `sslscan`, `sslsniff`, `sslsplit`, `sslyze`, `ssview`, `statsprocessor`, `steghide`, `stegosuite`, `stegsnow`, `stenographer`, `stpyv8`, `strace`, `strdeob.pl`, `strelka`, `strings.py`, `stunnel4`, `sucrack`, `suricata`, `suricatasc`, `swaks`, `swig`, `sysinternals`, `systeminformer`, `t50`, `tcl`, `tcpdump`, `tcpick`, `tcpreplay`, `tcpslice`, `tcpstat`, `tcptrace`, `tcptrack`, `telegraf`, `termineter`, `tesseract`, `tesseract-ocr`, `texteditor.py`, `thc-ipv6`, `thc-pptp-bruter`, `thc-ssl-dos`, `thefuzz`, `theharvester`, `thehive`, `thug`, `time-decode`, `tlssled`, `tnscmd10g`, `tofrodos`, `tor`, `translate.py`, `transmission`, `trid`, `tridupdate`, `truecrack`, `ttd`, `twofi`, `udptunnel`, `ugrep`, `uncompyle6`, `undbx`, `unfurl`, `unhide`, `unicode`, `unicornscan`, `uniextract2`, `uniscan`, `unity-control-center`, `unix-privesc-check`, `unix2dos`, `unix2mac`, `unpyc3`, `unrar`, `unrar-free`, `unxor`, `urlcrazy`, `vb-decompiler-lite`, `vbdec`, `vbindiff`, `vcbuildtools`, `vcredist-all`, `veil`, `vinetto`, `virtuoso-minimal`, `virustotal-search`, `virustotal-search.py`, `virustotal-submit`, `virustotal-submit.py`, `visual-studio-code`, `vivisect`, `voiphopper`, `volatility-framework`, `vscode`, `vscode.extension.jupyter`, `vscode.extension.python`, `wafw00f`, `wapiti`, `watobo`, `wazuh`, `wce`, `webacoo`, `webcrack`, `webscarab`, `webshells`, `weevely`, `wfuzz`, `whatweb`, `wifi-honey`, `winbind`, `windbg`, `windows-terminal`, `wine`, `winregfs`, `wordlists`, `wpscan`, `wxhexeditor`, `x64dbg`, `x64dbg-automate-mcp`, `x64dbg.plugin.dbgchild`, `x64dbg.plugin.ollydumpex`, `x64dbg.plugin.scyllahide`, `x64dbg.plugin.x64dbgpy`, `xdot`, `xfsprogs`, `xlmmacrodeobfuscator`, `xmldump.py`, `xmount`, `xor-kpa.py`, `xorbruteforcer.py`, `xorsearch`, `xorsearch.py`, `xorstrings`, `xplico`, `xsser`, `yara-forge-rules`, `yara-rules`, `yara-x`, `yersinia`, `zaproxy`, `zbarimg`, `zeek`, `zeek-cut`, `zenity`, `zenmap`, `zip`, `zip2john`, `zipdump.py`

</details>