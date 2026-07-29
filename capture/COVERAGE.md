# Capture Coverage

What can be documented **from a real binary** today, and what cannot.
A tool without a capture cannot get a page — see [docs/FORMAT.md](../docs/FORMAT.md#5-verification-why-the-options-can-be-trusted).

- **102 tools captured** with real help text — ready to document
- **5 present but no usable help** — GUI-only, or help needs arguments; document workflow rather than flags
- **789 not in either container** — need a booted VM (Kali, FLARE-VM Windows guest) or are GUI/appliance-only
- probed against `cyberlab-aio:v1` and `dfir-aio:v4` on rick

## Captured — ready to document

| Command | Image | Via | Version | Help bytes |
|---|---|---|---|---|
| `7za` | cyberlab-aio | `--help` |  | 3,146 |
| `aeskeyfind` | cyberlab-aio | `--help` |  | 418 |
| `base64dump.py` | cyberlab-aio | `--help` | base64dump.py 0.0.30 | 3,352 |
| `binwalk` | cyberlab-aio | `--help` |  | 4,245 |
| `blkls` | cyberlab-aio | `--help` | The Sleuth Kit ver 4.11.1 | 872 |
| `capa` | cyberlab-aio | `--help` | capa 9.4.0 | 4,392 |
| `capinfos` | cyberlab-aio | `--help` | Capinfos (Wireshark) 4.0.17 (Git v4.0.17 package | 2,219 |
| `clamscan` | cyberlab-aio | `--help` | ClamAV 1.4.3 | 8,404 |
| `curl` | cyberlab-aio | `--help` | curl 7.88.1 (x86_64-pc-linux-gnu) libcurl/7.88.1 | 914 |
| `cyberchef` | cyberlab-aio | `--help` |  | 176 |
| `die` | cyberlab-aio | `--help` | Detect It Easy v3.10 | 403 |
| `diec` | cyberlab-aio | `--help` | die 3.10 | 1,545 |
| `dotnet` | cyberlab-aio | `--help` |  | 950 |
| `dumpcap` | cyberlab-aio | `--help` |  | 5,103 |
| `editcap` | cyberlab-aio | `--help` | Editcap (Wireshark) 4.0.17 (Git v4.0.17 packaged | 7,040 |
| `ezhexviewer` | cyberlab-aio | `--help` |  | 1,593 |
| `ffind` | cyberlab-aio | `--help` | The Sleuth Kit ver 4.11.1 | 748 |
| `file` | cyberlab-aio | `--help` | file-5.44 | 3,189 |
| `floss` | cyberlab-aio | `--help` | floss 3.1.1 | 2,337 |
| `fls` | cyberlab-aio | `--help` | The Sleuth Kit ver 4.11.1 | 1,353 |
| `foremost` | cyberlab-aio | `-h` | 1.5.7 | 830 |
| `freshclam` | cyberlab-aio | `--help` | ClamAV 1.4.3 | 3,341 |
| `frida` | cyberlab-aio | `--help` | 17.16.3 | 4,398 |
| `frida-discover` | cyberlab-aio | `--help` | 17.16.3 | 2,991 |
| `frida-kill` | cyberlab-aio | `--help` | 17.16.3 | 1,525 |
| `frida-ls-devices` | cyberlab-aio | `--help` | 17.16.3 | 270 |
| `frida-ps` | cyberlab-aio | `--help` | 17.16.3 | 1,649 |
| `frida-trace` | cyberlab-aio | `--help` | 17.16.3 | 4,999 |
| `fsstat` | cyberlab-aio | `--help` | The Sleuth Kit ver 4.11.1 | 679 |
| `hashcat` | cyberlab-aio | `--help` | v6.2.6 | 58,909 |
| `hivexsh` | cyberlab-aio | `help` | hivexsh: failed to open hive file: version: No s | 333 |
| `hydra` | cyberlab-aio | `--help` | Hydra v9.4 (c) 2022 by van Hauser/THC & David Ma | 237 |
| `icat` | cyberlab-aio | `--help` | The Sleuth Kit ver 4.11.1 | 877 |
| `ils` | cyberlab-aio | `--help` | The Sleuth Kit ver 4.11.1 | 1,068 |
| `img_stat` | cyberlab-aio | `--help` | The Sleuth Kit ver 4.11.1 | 340 |
| `inetsim` | cyberlab-aio | `--help` | INetSim 1.3.2 (2020-05-19) by Matthias Eckert &  | 1,646 |
| `istat` | cyberlab-aio | `--help` | The Sleuth Kit ver 4.11.1 | 1,004 |
| `john` | cyberlab-aio | `(no args)` | stat: version: No such file or directory | 1,552 |
| `log2timeline.py` | cyberlab-aio | `--help` | plaso - log2timeline version 20260512 | 18,762 |
| `mactime` | cyberlab-aio | `--help` | Unknown option: --version | 904 |
| `mergecap` | cyberlab-aio | `--help` | Mergecap (Wireshark) 4.0.17 (Git v4.0.17 package | 953 |
| `mmls` | cyberlab-aio | `--help` | The Sleuth Kit ver 4.11.1 | 796 |
| `mraptor` | cyberlab-aio | `--help` | MacroRaptor 0.56.2 - http://decalage.info/python | 790 |
| `msodde` | cyberlab-aio | `--help` |  | 1,187 |
| `ngrep` | cyberlab-aio | `--help` | ngrep: V1.47.1-git, libpcap version 1.10.3 (with | 1,702 |
| `nmap` | cyberlab-aio | `--help` | Nmap version 7.93 ( https://nmap.org ) | 5,996 |
| `nping` | cyberlab-aio | `--help` | Failed to resolve given hostname/IP: version.  N | 6,787 |
| `ntfs-3g` | cyberlab-aio | `--help` | ntfs-3g 2022.10.3 integrated FUSE 28 | 698 |
| `numbers-to-string.py` | cyberlab-aio | `--help` | numbers-to-string.py 0.0.11 | 1,331 |
| `objdump` | cyberlab-aio | `--help` | GNU objdump (GNU Binutils for Debian) 2.40 | 7,394 |
| `olebrowse` | cyberlab-aio | `--help` |  | 1,587 |
| `oledir` | cyberlab-aio | `--help` | oledir 0.54 - http://decalage.info/python/oletoo | 594 |
| `oledump.py` | cyberlab-aio | `--help` | oledump.py 0.0.85 | 2,814 |
| `olefile` | cyberlab-aio | `--help` | ERROR    Error while parsing file 'version' | 535 |
| `oleid` | cyberlab-aio | `--help` | oleid 0.60.1 - http://decalage.info/oletools | 910 |
| `olemap` | cyberlab-aio | `--help` |  | 1,718 |
| `olemeta` | cyberlab-aio | `--help` | olemeta 0.54 - http://decalage.info/python/oleto | 771 |
| `oleobj` | cyberlab-aio | `--help` | oleobj 0.60.1 - http://decalage.info/oletools | 1,277 |
| `oletimes` | cyberlab-aio | `--help` | oletimes 0.54 - http://decalage.info/python/olet | 773 |
| `olevba` | cyberlab-aio | `--help` | olevba 0.60.2 on Python 3.11.2 - http://decalage | 2,377 |
| `patch` | cyberlab-aio | `--help` | GNU patch 2.7.6 | 2,955 |
| `pcodedmp` | cyberlab-aio | `--help` | pcodedmp version 1.2.6 | 573 |
| `pdf-parser` | cyberlab-aio | `--help` | pdf-parser.py 0.7.14 | 2,862 |
| `pdf-parser.py` | cyberlab-aio | `--help` | pdf-parser.py 0.7.14 | 2,862 |
| `pdfid` | cyberlab-aio | `--help` | pdfid.py 0.2.10 | 1,700 |
| `pdfid.py` | cyberlab-aio | `--help` | pdfid.py 0.2.10 | 1,700 |
| `perl` | cyberlab-aio | `--help` | Summary of my perl5 (revision 5 version 36 subve | 2,023 |
| `photorec` | cyberlab-aio | `--help` | PhotoRec 7.1, Data Recovery Utility, July 2019 | 405 |
| `pinfo.py` | cyberlab-aio | `--help` | plaso - pinfo version 20260512 | 2,717 |
| `pkg-config` | cyberlab-aio | `--help` | 1.8.1 | 5,357 |
| `psort.py` | cyberlab-aio | `--help` | plaso - psort version 20260512 | 10,029 |
| `pyxswf` | cyberlab-aio | `--help` | pyxswf 0.54 - http://decalage.info/python/oletoo | 2,224 |
| `r2` | cyberlab-aio | `-h` | 6.1.9-124  r2 | 2,598 |
| `rabin2` | cyberlab-aio | `--help` | rabin2 6.1.9 +1 abi:124 @ linux-x86_64 | 3,071 |
| `radiff2` | cyberlab-aio | `-h` | radiff2 6.1.9 +1 abi:124 @ linux-x86_64 | 1,963 |
| `rafind2` | cyberlab-aio | `--help` | rafind2 6.1.9 +1 abi:124 @ linux-x86_64 | 122 |
| `rahash2` | cyberlab-aio | `--help` | rahash2 6.1.9 +1 abi:124 @ linux-x86_64 | 1,382 |
| `rasm2` | cyberlab-aio | `--help` | rasm2 6.1.9 +1 abi:124 @ linux-x86_64 | 1,757 |
| `rax2` | cyberlab-aio | `--help` | rax2 6.1.9 +1 abi:124 @ linux-x86_64 | 2,927 |
| `readelf.py` | cyberlab-aio | `--help` | readelf.py: based on pyelftools 0.33 | 1,637 |
| `reordercap` | cyberlab-aio | `--help` | Reordercap (Wireshark) 4.0.17 (Git v4.0.17 packa | 397 |
| `rip.pl` | cyberlab-aio | `--help` | Unknown option: -version | 1,417 |
| `rsakeyfind` | cyberlab-aio | `(no args)` |  | 221 |
| `rtfobj` | cyberlab-aio | `--help` | rtfobj 0.60.1 on Python 3.11.2 - http://decalage | 1,244 |
| `scalpel` | cyberlab-aio | `-h` | Scalpel version 1.60 | 1,993 |
| `sigtool` | cyberlab-aio | `--help` | ClamAV 1.4.3 | 4,407 |
| `ssdeep` | cyberlab-aio | `-h` | 2.14.1 | 915 |
| `tcpflow` | cyberlab-aio | `--help` | TCPFLOW 1.6.1 | 2,597 |
| `tcpxtract` | cyberlab-aio | `--help` | tcpxtract v1.0.1 | 488 |
| `testdisk` | cyberlab-aio | `--help` | TestDisk 7.1, Data Recovery Utility, July 2019 | 1,154 |
| `tshark` | cyberlab-aio | `--help` |  | 9,294 |
| `tsk_gettimes` | cyberlab-aio | `--help` | The Sleuth Kit ver 4.11.1 | 551 |
| `tsk_recover` | cyberlab-aio | `--help` | The Sleuth Kit ver 4.11.1 | 920 |
| `unzip` | cyberlab-aio | `--help` | UnZip 6.00 of 20 April 2009, by Debian. Original | 1,509 |
| `upx` | cyberlab-aio | `--help` | upx 4.2.4 | 5,655 |
| `vdbbin` | cyberlab-aio | `--help` |  | 1,025 |
| `vivbin` | cyberlab-aio | `--help` |  | 1,851 |
| `wget` | cyberlab-aio | `--help` | GNU Wget 1.21.3 built on linux-gnu. | 13,243 |
| `xlmdeobfuscator` | cyberlab-aio | `--help` |  | 3,820 |
| `xortool` | cyberlab-aio | `--help` | 1.1.0 | 1,670 |
| `yara` | cyberlab-aio | `--help` | 4.2.3 | 2,552 |
| `yarac` | cyberlab-aio | `--help` | 4.2.3 | 613 |

## Present, but no usable help text

These exist in a container but print nothing useful for `--help`. Most are GUI apps or need arguments first. They get workflow pages, not flag tables.

`exiftool`, `hivexget`, `runxlrd2.py`, `set`, `unshadow`

## Not available in a container

789 candidates were absent. This includes Windows-only (FLARE-VM), GUI-only, appliance services, and names that were never real commands (package names that do not map to a binary).

<details><summary>Full list</summary>

`010editor`, `0trace`, `1768.py`, `7-zip`, `7zip`, `above`, `absent`, `accept-all-ips`, `advanced-installer`, `aesfix`, `aeskeyfinder`, `affcat`, `affconvert`, `affinfo`, `afl++`, `aircrack-ng`, `androguard`, `androidprojectcreator`, `angr`, `anomy`, `apache-users`, `apache2`, `apimonitor`, `apkid`, `apktool`, `armitage`, `arp-scan`, `arping`, `asar`, `autoit-ripper`, `autopsy`, `avfs`, `aws-cli`, `baksmali`, `balbuzard`, `bbcrack`, `bbharvest`, `bbtrans`, `bearcommander`, `bearparser`, `bed`, `beef-xss`, `bettercap`, `binaryninja`, `bindiff`, `binee`, `binwalk3`, `bless`, `blobrunner`, `blobrunner64`, `blt`, `box-export`, `box-js`, `braa`, `brxor.py`, `bulk_extractor`, `burp-suite-community-edition`, `burpsuite`, `bytecode-viewer`, `bytecodeviewer`, `bytehist`, `cabextract`, `cadaver`, `capa-explorer-web`, `ccrypt`, `cewl`, `cfr`, `chepy`, `chkrootkit`, `chntpw`, `chrome.extensions`, `chromium-browser`, `cisco-global-exploiter`, `cisco-ocs`, `cisco-torch`, `clamdscan`, `clang`, `claude-code`, `cmder`, `cmospwd`, `code`, `codetrack`, `commix`, `convert`, `copy-router-config`, `crackle`, `creddump7`, `crunch`, `cryptcat`, `cryptotester`, `cryptsetup`, `cs-analyze-processdump.py`, `cs-decrypt-metadata.py`, `cs-extract-key.py`, `cs-parse-traffic.py`, `csce`, `cut-bytes.py`, `cutter`, `cutycapt`, `cygwin`, `cymothoa`, `d2j-dex2jar`, `darkstat`, `davtest`, `dbd`, `dc3-mwcp`, `dc3dd`, `dcfldd`, `ddrescue`, `de4dot`, `de4dot-cex`, `debloat`, `decai`, `decode-vbe.py`, `decompyle++`, `default-jre`, `default-mysql-server`, `dependencywalker`, `dex2jar`, `dexray`, `dhcpig`, `didier-stevens-beta`, `didier-stevens-suite`, `dirb`, `dirbuster`, `disitool`, `disitool.py`, `disktype`, `dislocker`, `display`, `dissect`, `dll-to-exe`, `dllcharacteristics.py`, `dmitry`, `dnfile`, `dnlib`, `dns2tcp`, `dnschef`, `dnsenum`, `dnslib`, `dnsmap`, `dnspyex`, `dnsrecon`, `dnsresolver.py`, `dnstracer`, `dnswalk`, `docker`, `domainstats`, `dos2unix`, `dotdotpwn`, `dotdumper`, `dotnet3.5`, `dotnetfile`, `driftnet`, `droidlysis`, `dsniff`, `dumpzilla`, `e2fsprogs`, `edb`, `edb-debugger`, `elastalert-2`, `elastic-agent`, `elastic-fleet`, `elasticsearch`, `emldump.py`, `ent`, `enum4linux`, `enumiax`, `epic-irc-client`, `epic5`, `etc`, `etherape`, `ettercap-graphical`, `evilclippy`, `evince`, `ewfacquire`, `ewfexport`, `ewfinfo`, `ewfmount`, `ewfverify`, `ex_pe_xor.py`, `exe2hexbat`, `exeinfope`, `exfat-extras`, `exfat-fuse`, `exif`, `exifprobe`, `exiv2`, `exploitdb`, `explorersuite`, `ext3grep`, `ext4magic`, `extract_msg`, `extreme_dumper`, `extundelete`, `eyewitness`, `ezviewer`, `fakedns`, `fakemail`, `fakenet-ng`, `fcrackzip`, `fdupes`, `feh`, `ferret-sidejack`, `fiddler`, `fierce`, `fiked`, `file-magic.py`, `filebeat`, `firefox`, `firewalk`, `firmware-mod-kit`, `flex`, `forensic-artifacts`, `forensics-colorize`, `format-bytes.py`, `fping`, `fragrouter`, `freerdp3-x11`, `freqserver`, `ftester`, `galculator`, `galleta`, `garbageman`, `gawk`, `gdb`, `gddrescue`, `ghex`, `ghidra`, `ghidrassistmcp`, `gnome-calculator`, `gnu-project-debugger`, `gnu-wget`, `gootloaderautojsdecode.py`, `goresym`, `gostringungarbler`, `gpart`, `gparted`, `gpp-decrypt`, `grafana`, `graphviz`, `grepcidr`, `grokevt`, `gthumb`, `guymager`, `gvm`, `gzrt`, `hachoir`, `hachoir-grep`, `hachoir-metadata`, `hachoir-strip`, `hachoir-wx`, `hakrawler`, `hamster-sidejack`, `hash-id`, `hash-id.py`, `hash-identifier`, `hashcat-utils`, `hashdeep`, `hashid`, `hashmyfiles`, `heartleech`, `hex-to-bin.py`, `hexedit`, `hexinject`, `hivexregedit`, `hollowshunter`, `hping3`, `httprint`, `httrack`, `hxd`, `hydra-gtk`, `iaxflood`, `ibus`, `ibus-setup`, `ida.plugin.capa`, `ida.plugin.comida`, `ida.plugin.delphihelper`, `ida.plugin.dereferencing`, `ida.plugin.diaphora`, `ida.plugin.flare`, `ida.plugin.flare-emu`, `ida.plugin.hashdb`, `ida.plugin.hrtng`, `ida.plugin.ifl`, `ida.plugin.xray`, `ida.plugin.xrefer`, `idafree`, `idr`, `idx_parser.py`, `ifpstools`, `ike-scan`, `ilm`, `ilspy`, `imagemagick`, `influxdb`, `info-zip`, `init`, `innoextract`, `innounp`, `inspircd-3`, `internet_detector`, `intrace`, `inviteflood`, `iodine`, `ipwhois`, `ipython`, `ipython3`, `irpas`, `isd`, `isr-evilgrade`, `jadx`, `jadx-gui`, `java-idx-parser`, `javascript-deobfuscator`, `javasnoop`, `javassist`, `jboss-autopwn`, `jd-gui`, `jd-gui-java-decompiler`, `johnny`, `joomscan`, `jq`, `js`, `js-ascii`, `js-beautifier`, `js-beautify`, `js-deobfuscator`, `js-file`, `js_unshroud`, `jsql-injection`, `jstillery`, `kdiff3`, `keystone`, `kibana`, `kpartx`, `laudanum`, `lbd`, `legion`, `lft`, `lief`, `list-cs-settings`, `logstash`, `ltrace`, `lvm2`, `lynis`, `mac-robber`, `mac2unix`, `macchanger`, `magicrescue`, `magika`, `magnus`, `mail-parser`, `malcat-lite`, `malchive`, `maltego`, `malware-jail`, `malwoverview`, `managerhype`, `manalyze`, `map`, `maskprocessor`, `masscan`, `mbcscan`, `mbcscan.py`, `md5deep`, `mdadm`, `mdbtools`, `medusa`, `memdump`, `mermaid-viewer`, `metacam`, `metagoofil`, `metasploit-framework`, `microsoft-office`, `mimikatz`, `miredo`, `missidentify`, `mitmdump`, `mitmproxy`, `mitmweb`, `mogrify`, `monitor-network`, `monodis`, `msfpc`, `msg-extractor`, `msgconvert`, `msoffcrypto-crack.py`, `msoffice-crypt`, `mtd-utils`, `mwcp`, `myip`, `myjson-filter.py`, `myrescue`, `name-that-hash`, `nasm`, `nasty`, `nautilus`, `nbd-client`, `nbtscan`, `nc`, `ncat`, `ncrack`, `net-reactor-slayer`, `netcat`, `netdiscover`, `netmask`, `netpbm`, `netsed`, `netsniff-ng`, `network-miner-free-edition`, `networkminer`, `netwox`, `nfdump`, `nginx`, `nikto`, `nishang`, `nomorexor.py`, `notepadplusplus`, `notepadpp.plugin.compare`, `notepadpp.plugin.jstool`, `notepadpp.plugin.xmltools`, `nsrllookup`, `nth`, `obfuscator-io-deobfuscator`, `objects.js`, `offvis`, `ofs2rva`, `ohrwurm`, `okular`, `olecfexport`, `olecfinfo`, `olecfmount`, `ollydbg`, `onboard`, `onedump.py`, `onenoteanalyzer`, `onesixtyone`, `onion-ai-assistant`, `open-iscsi`, `opencanary`, `opencode`, `openjdk`, `openssh`, `ophcrack`, `ophcrack-cli`, `orca`, `origamindee`, `oscanner`, `osquery`, `outguess`, `owasp-mantra-ff`, `p0f`, `p7zip-full`, `pack`, `pack2`, `padbuster`, `paros`, `parted`, `pasco`, `passing-the-hash`, `patator`, `pcode2code`, `pdbresym`, `pdfcop`, `pdfcrack`, `pdfdecompress`, `pdfdecrypt`, `pdfextract`, `pdfresurrect`, `pdfstreamdumper`, `pdftk`, `pdftk-java`, `pdftool.py`, `pdg`, `pdnstool`, `pe-tree`, `pe_unmapper`, `peass`, `pebear`, `pecheck.py`, `pedis`, `pedump`, `peepdf-3`, `pefile`, `peframe`, `pehash`, `peid`, `peldd`, `pepack`, `peres`, `pescan`, `pesec`, `pesieve`, `pestr`, `pestudio`, `pev`, `phonon`, `php`, `php-mysql`, `pipal`, `pkg-unpacker`, `playbook`, `pma-labs`, `polarproxy`, `polenum`, `portex`, `powershell`, `powershell-core`, `powersploit`, `procdot`, `processdump`, `procmonmcp`, `procyon`, `protos-sip`, `proxychains4`, `proxytunnel`, `psnotify`, `pst-utils`, `psteal.py`, `ptunnel`, `pv`, `pwnat`, `pwsh`, `pycdas`, `pycdc`, `pyelftools`, `pyinstaller-extractor`, `pyinstxtractor-ng`, `pyinstxtractor.py`, `pylingual`, `qemu`, `qemu-utils`, `qiling`, `qpdf`, `qsslcaudit`, `r2ai`, `r2pipe`, `rainbowcrack`, `rar`, `rar2john`, `rarcrack`, `rat-king-parser`, `rcracki-mt`, `re-search.py`, `readpe`, `rebind`, `recaf`, `recon-ng`, `recoverdm`, `recoverjpeg`, `recstudio`, `redis`, `redress`, `redsocks`, `reg_export`, `regcool`, `reglookup`, `regshot`, `remnux-installer`, `remnux-mcp-server`, `rephrase`, `resourcehacker`, `responder`, `restrict-egress`, `rhino-debugger`, `rifiuti`, `rifiuti2`, `rip`, `rizin`, `rizin-cutter`, `rkhunter`, `rsakeyfinder`, `rsmangler`, `rtfdump.py`, `rtpbreak`, `rtpflood`, `rtpinsertsound`, `rtpmixsound`, `rundotnetdll`, `runsc`, `rva2ofs`, `rz-bin`, `rz-find`, `rz-ghidra`, `safecopy`, `samdump2`, `sandfly-processdecloak`, `sbd`, `scdbg`, `scite`, `sclauncher`, `sclauncher64`, `scrounge-ntfs`, `sctpscan`, `seclists`, `security-onion-console`, `sensoroni`, `sets.py`, `sfextract`, `sftp`, `sfuzz`, `sha256deep`, `shcode2exe`, `shellcode2exe.bat`, `shellcode_launcher`, `shellnoob`, `shellter`, `sidguesser`, `siege`, `signsrch`, `silversearcher-ag`, `siparmyknife`, `sipcrack`, `sipp`, `sipsak`, `sipvicious`, `skipfish`, `sleuth-kit`, `slowhttptest`, `smbmap`, `smtp-user-enum`, `sniffjoke`, `snmpcheck`, `so-apt-cacher-ng`, `so-firewall`, `so-idstools`, `socat`, `sortcanon.py`, `speakeasy`, `spidermonkey`, `spike`, `sqldict`, `sqlite`, `sqlite3`, `sqlitebrowser`, `sqlmap`, `sqlninja`, `sqlsus`, `ssh`, `sshpass`, `ssldump`, `sslh`, `sslscan`, `sslsniff`, `sslsplit`, `sslyze`, `ssview`, `statsprocessor`, `steghide`, `stegosuite`, `stegsnow`, `stenographer`, `stpyv8`, `strace`, `strdeob.pl`, `strelka`, `strings.py`, `stunnel4`, `sucrack`, `suricata`, `suricatasc`, `swaks`, `swig`, `sysinternals`, `systeminformer`, `t50`, `tcl`, `tcpdump`, `tcpick`, `tcpreplay`, `tcpslice`, `tcpstat`, `tcptrace`, `tcptrack`, `telegraf`, `termineter`, `tesseract`, `tesseract-ocr`, `texteditor.py`, `thc-ipv6`, `thc-pptp-bruter`, `thc-ssl-dos`, `thefuzz`, `theharvester`, `thehive`, `thug`, `time-decode`, `tlssled`, `tnscmd10g`, `tofrodos`, `tor`, `translate.py`, `transmission`, `trid`, `tridupdate`, `truecrack`, `ttd`, `twofi`, `udptunnel`, `ugrep`, `uncompyle6`, `undbx`, `unfurl`, `unhide`, `unicode`, `unicornscan`, `uniextract2`, `uniscan`, `unity-control-center`, `unix-privesc-check`, `unix2dos`, `unix2mac`, `unpyc3`, `unrar`, `unrar-free`, `unxor`, `urlcrazy`, `vb-decompiler-lite`, `vbdec`, `vbindiff`, `vcbuildtools`, `vcredist-all`, `veil`, `vinetto`, `virtuoso-minimal`, `virustotal-search`, `virustotal-search.py`, `virustotal-submit`, `virustotal-submit.py`, `visual-studio-code`, `vivisect`, `voiphopper`, `volatility-framework`, `vscode`, `vscode.extension.jupyter`, `vscode.extension.python`, `wafw00f`, `wapiti`, `watobo`, `wazuh`, `wce`, `webacoo`, `webcrack`, `webscarab`, `webshells`, `weevely`, `wfuzz`, `whatweb`, `wifi-honey`, `winbind`, `windbg`, `windows-terminal`, `wine`, `winregfs`, `wordlists`, `wpscan`, `wxhexeditor`, `x64dbg`, `x64dbg-automate-mcp`, `x64dbg.plugin.dbgchild`, `x64dbg.plugin.ollydumpex`, `x64dbg.plugin.scyllahide`, `x64dbg.plugin.x64dbgpy`, `xdot`, `xfsprogs`, `xlmmacrodeobfuscator`, `xmldump.py`, `xmount`, `xor-kpa.py`, `xorbruteforcer.py`, `xorsearch`, `xorsearch.py`, `xorstrings`, `xplico`, `xsser`, `yara-forge-rules`, `yara-rules`, `yara-x`, `yersinia`, `zaproxy`, `zbarimg`, `zeek`, `zeek-cut`, `zenity`, `zenmap`, `zip`, `zip2john`, `zipdump.py`

</details>