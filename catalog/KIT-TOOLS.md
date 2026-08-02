# Kit Tool List

The binding scope for the quick-reference guide. A tool absent from this
list is **not in the kit** and must not be documented in the guide.

Every entry is derived from an upstream machine-readable manifest; none
is written from memory. Sources are listed at the end.

## Contents

- [REMnux](#remnux) — 268 tools, 31 categories
- [Kali Linux](#kali-linux) — 403 tools, 12 categories
- [FLARE-VM](#flare-vm) — 137 tools, 1 categories
- [SIFT Workstation](#sift-workstation) — 162 tools, 1 categories
- [Security Onion](#security-onion) — 36 tools, 9 categories

**Total: 1006 tools across 5 platforms.**


## REMnux

### Analyze Documents / Email Messages

| Tool | Command(s) | Purpose |
|---|---|---|
| emldump.py | — | Parse and analyze EML files. |
| mail-parser | — | Parse raw SMTP and .MSG email messages and generate a parsed object from them. |
| msg-extractor | `extract_msg` | Extract emails and attachments from MSG files. |
| msgconvert | — | Convert MSG files to MBOX files. |

### Analyze Documents / General

| Tool | Command(s) | Purpose |
|---|---|---|
| [base64dump.py](../reference/malware-triage-static/base64dump.py.md) | — | Locate and decode strings encoded in Base64 and other common encodings. |
| Tesseract OCR | `tesseract` | Examine images to identify and extract text using optical character recognition \(OCR\). |

### Analyze Documents / Microsoft Office

| Tool | Command(s) | Purpose |
|---|---|---|
| EvilClippy | — | Modify aspects of Microsoft Office documents. |
| Hachoir | `hachoir-grep`, `hachoir-metadata`, `hachoir-strip`, `hachoir-wx` | View, edit, and carve contents of various binary file types. |
| libolecf | `olecfexport`, `olecfinfo`, `olecfmount`, `etc` | Microsoft Office OLE2 compound documents. |
| msoffcrypto-crack.py | — | Recover the password of an encrypted Microsoft Office document. |
| [msoffcrypto-tool](../reference/malware-triage-documents/msoffcrypto-tool.md) | — | Decrypt a Microsoft Office file with password, intermediate key, or private key which generated its escrow key. |
| msoffice-crypt | — | Encrypt and decrypt OOXML Microsoft Office documents. |
| [oledump.py](../reference/malware-triage-documents/oledump.py.md) | — | Analyze OLE2 Structured Storage files. |
| [olefile](../reference/malware-triage-documents/olefile.md) | — | Python package to parse, read and write MS OLE2 files. |
| oletools | [`mraptor`](../reference/malware-triage-documents/mraptor.md), [`msodde`](../reference/malware-triage-documents/msodde.md), [`olebrowse`](../reference/malware-triage-documents/olebrowse.md), [`oledir`](../reference/malware-triage-documents/oledir.md), [`oleid`](../reference/malware-triage-documents/oleid.md), [`olemap`](../reference/malware-triage-documents/olemap.md), [`olemeta`](../reference/malware-triage-documents/olemeta.md), [`oleobj`](../reference/malware-triage-documents/oleobj.md), [`oletimes`](../reference/malware-triage-documents/oletimes.md), [`olevba`](../reference/malware-triage-documents/olevba.md), [`pyxswf`](../reference/malware-triage-documents/pyxswf.md), [`rtfobj`](../reference/malware-triage-documents/rtfobj.md), [`ezhexviewer`](../reference/report-support/ezhexviewer.md) | Microsoft Office OLE2 compound documents. |
| onedump.py | — | Extract and analyze embedded files from OneNote documents. |
| pcode2code | — | Decompile VBA macro p-code from Microsoft Office documents. |
| [pcodedmp](../reference/malware-triage-documents/pcodedmp.md) | — | Disassemble VBA p-code. |
| rtfdump.py | — | Analyze a suspicious RTF file. |
| SSView | `ssview` | Analyze OLE2 Structured Storage files. |
| XLMMacroDeobfuscator | [`xlmdeobfuscator`](../reference/malware-triage-documents/xlmdeobfuscator.md), `runxlrd2.py` | Deobfuscate XLM macros (also known as Excel 4.0 macros) from Microsoft Office files. |
| xmldump.py | — | Extract contents of XML files, in particular OOXML-formatted Microsoft Office documents. |
| zipdump.py | — | Analyze zip-compressed files. |

### Analyze Documents / Pdf

| Tool | Command(s) | Purpose |
|---|---|---|
| Origamindee | `pdfcop`, `pdfdecompress`, `pdfdecrypt`, `pdfextract`, `etc` | Parse, modify, generate PDF files. |
| [pdf-parser.py](../reference/malware-triage-documents/pdf-parser.py.md) | — | Examine elements of the PDF file. |
| [pdfid.py](../reference/malware-triage-documents/pdfid.py.md) | — | Identify suspicious elements of the PDF file. |
| pdfresurrect | — | Extract previous versions of content from PDF files. |
| pdftk-java | `pdftk` | Edit, create, and examine PDF files. |
| pdftool.py | — | Analyze PDF files to identify incremental updates to the document. |
| peepdf-3 | — | Examine elements of the PDF file. |
| qpdf | — | Manipulate \(merge, convert, transform\) PDF files. |

### Dynamically Reverse-Engineer Code / Elf Files

| Tool | Command(s) | Purpose |
|---|---|---|
| edb | — | An AArch32/x86/x86-64 debugger, well suited for debugging ELF files. |
| GNU Project Debugger | — | Multi-language debugger. |
| ltrace | — | Trace library calls and signals. |
| strace | — | Trace process' system calls and signals. |

### Dynamically Reverse-Engineer Code / General

| Tool | Command(s) | Purpose |
|---|---|---|
| [Frida](../reference/reverse-engineering/frida.md) | [`frida`](../reference/reverse-engineering/frida.md), [`frida-ps`](../reference/reverse-engineering/frida-ps.md), [`frida-trace`](../reference/reverse-engineering/frida-trace.md), [`frida-discover`](../reference/reverse-engineering/frida-discover.md), [`frida-ls-devices`](../reference/reverse-engineering/frida-ls-devices.md), [`frida-kill`](../reference/reverse-engineering/frida-kill.md) | Trace the execution of a process to analyze its behavior. |
| r2pipe | — | Examine binary files, including disassembling and debugging. |
| radare2 | [`r2`](../reference/reverse-engineering/r2.md), [`rasm2`](../reference/reverse-engineering/rasm2.md), [`rabin2`](../reference/malware-triage-static/rabin2.md), [`rahash2`](../reference/acquire-preserve/rahash2.md), [`rafind2`](../reference/examine-the-filesystem/rafind2.md), `r2ai`, `decai`, `pdg` | Examine binary files, including disassembling and debugging. Includes r2ai and decai plugins for LLM-powered analysis (A |
| Wine | `wine` | Run Windows applications. |
| x64dbg Automate MCP (OpenCode skills) | — | Drive x64dbg on a remote Windows VM from OpenCode on REMnux, with eight AI commands for tracing, unpacking, state snapsh |

### Dynamically Reverse-Engineer Code / Scripts

| Tool | Command(s) | Purpose |
|---|---|---|
| box-js | `box-js`, `box-export` | Analyze suspicious JavaScript scripts. |
| JavaScript Deobfuscator | — | Deobfuscate JavaScript by removing common obfuscation techniques such as string arrays and proxy functions. |
| js_unshroud | — | Monitor and deobfuscate JavaScript behavior in a headless browser to analyze malicious web pages. |
| JStillery | `jstillery` | Deobfuscate JavaScript scripts using AST and Partial Evaluation techniques. |
| objects.js | — | Emulate common browser and PDF viewer objects, methods, and properties when deobfuscating JavaScript. |
| PowerShell Core | `pwsh` | Run PowerShell scripts and commands. |
| Rhino Debugger | `rhino-debugger` | GUI JavaScript debugger. |
| SpiderMonkey | `js` | Execute and deobfuscate JavaScript using Mozilla's standalone JavaScript engine. |
| SpiderMonkey (Patched) | `js-ascii`, `js-file` | Execute and deobfuscate JavaScript using a patched version of Mozilla's standalone JavaScript engine. |
| STPyV8 | — | Python3 and JavaScript interop engine, fork of the original PyV8 project. |
| Webcrack | — | Deobfuscate, unminify, and unpack bundled JavaScript, including scripts protected with obfuscator.io. |

### Dynamically Reverse-Engineer Code / Shellcode

| Tool | Command(s) | Purpose |
|---|---|---|
| libemu | — | A library for x86 code emulation and shellcode detection. |
| Qiling | — | Emulate code execution of PE files, shellcode, etc. for a variety of OS and hardware platforms. |
| runsc | — | Run shellcode to trace and analyze its execution. |
| scdbg | — | Analyze shellcode by emulating its execution. |
| shcode2exe | — | Convert 32 and 64-bit shellcode to a Windows executable file. |
| shellcode2exe.bat | — | Convert 32 and 64-bit shellcode to a Windows executable file. |
| Speakeasy | — | Emulate code execution, including shellcode, Windows drivers, and Windows PE files. |
| XORSearch | `xorsearch` | Locate and decode strings obfuscated using common techniques. |

### Examine Static Properties / .Net

| Tool | Command(s) | Purpose |
|---|---|---|
| dnfile | — | Analyze static properties of .NET files. |
| dotnetfile | — | Analyze static properties of .NET files. |
| monodis | — | Disassemble and extract resources from .NET assemblies. |

### Examine Static Properties / Deobfuscation

| Tool | Command(s) | Purpose |
|---|---|---|
| 1768.py | — | Analyze Cobalt Strike beacons. |
| Balbuzard | `balbuzard`, `bbcrack`, `bbharvest`, `bbtrans` | Extract and deobfuscate patterns from suspicious files. |
| [base64dump.py](../reference/malware-triage-static/base64dump.py.md) | — | Locate and decode strings encoded in Base64 and other common encodings. |
| brxor.py | — | Bruteforce XOR'ed strings to find those that are English words. |
| Chepy | `chepy` | Decode and otherwise analyze data using this command-line tool and Python library. |
| Cobalt Strike Configuration Extractor (CSCE) and Parser <a href="#csce" id="csce"></a> | `csce`, `list-cs-settings` | Analyze Cobalt Strike beacons. |
| cs-analyze-processdump.py | — | Analyze Cobalt Strike beacon process dumps to detect sleep mask encoding. |
| cs-decrypt-metadata.py | — | Decrypt Cobalt Strike metadata. |
| cs-extract-key.py | — | Extract AES and HMAC keys from Cobalt Strike beacon process memory. |
| cut-bytes.py | — | Cut out a part of a data stream. |
| [CyberChef](../reference/decode-deobfuscate/cyberchef.md) | [`cyberchef`](../reference/decode-deobfuscate/cyberchef.md) | Decode and otherwise analyze data using this browser app. |
| DC3-MWCP | `mwcp` | Parsing configuration information from malware. |
| ex_pe_xor.py | — | Search an XOR'ed file for indications of executable binaries. |
| [FLOSS](../reference/malware-triage-static/floss.md) | [`floss`](../reference/malware-triage-static/floss.md) | Extract and deobfuscate strings from PE executables. |
| format-bytes.py | — | Decompose structured binary data with format strings. |
| hex-to-bin.py | — | Convert hexadecimal text dumps to binary data. |
| Malchive | — | Perform static analysis of various aspects of malicious code. |
| NoMoreXOR.py | — | Help guess a file's 256-byte XOR by using frequency analysis. |
| [numbers-to-string.py](../reference/malware-triage-static/numbers-to-string.py.md) | — | Translate number sequences into ASCII characters. |
| re-search.py | — | Search files using regular expressions from a built-in library or custom patterns. |
| sets.py | — | Perform set operations on lines or bytes in text files. |
| strdeob.pl | — | Locate and decode stack strings in executable files. |
| translate.py | — | Translate bytes according to a Python expression. |
| unicode | — | Display Unicode character properties. |
| unXOR | — | Deobfuscate XOR'ed files. |
| xor-kpa.py | — | Implement a XOR known plaintext attack. |
| xorBruteForcer.py | — | Bruteforce an XOR-encoded file. |
| XORSearch | `xorsearch` | Locate and decode strings obfuscated using common techniques. |
| xorsearch.py | — | Search for XOR, ROL, ROT, and SHIFT encoded strings with YARA and regex support. |
| XORStrings | — | Search for XOR encoded strings in a file. |
| [xortool](../reference/reverse-engineering/xortool.md) | — | Analyze XOR-encoded data. |

### Examine Static Properties / Elf Files

| Tool | Command(s) | Purpose |
|---|---|---|
| pyelftools | [`readelf.py`](../reference/malware-triage-static/readelf.py.md) | Python library for parsing and analyzing ELF files and DWARF debugging information. |

### Examine Static Properties / General

| Tool | Command(s) | Purpose |
|---|---|---|
| 7-Zip | [`7za`](../reference/malware-triage-static/7za.md) | Compress and decompress files using a variety of algorithms. |
| [binwalk](../reference/examine-the-filesystem/binwalk.md) | — | Extract and analyze firmware images. |
| [bulk_extractor](../reference/examine-the-filesystem/bulk_extractor.md) | — | Extract interesting strings from binary files. |
| ClamAV | [`clamscan`](../reference/malware-triage-static/clamscan.md), [`freshclam`](../reference/malware-triage-static/freshclam.md) | Scan files for malware signatures. |
| Detect-It-Easy | — | Determine types of files and examine file properties. |
| disitool | `disitool.py` | Manipulate embedded digital signatures. |
| DroidLysis | `droidlysis` | Perform static analysis of Android applications. |
| ExifTool | `exiftool` | Tool to read from, write to, and edit EXIF metadata of various file types. |
| [file](../reference/examine-the-filesystem/file.md) | — | Identify file type using "magic" numbers. |
| file-magic.py | — | Identify file types using the Python magic module. |
| Hachoir | `hachoir-grep`, `hachoir-metadata`, `hachoir-strip`, `hachoir-wx` | View, edit, and carve contents of various binary file types. |
| Hash ID | `hash-id.py` | Identify different types of hashes. |
| LIEF | — | Parse and analyze PE, ELF, MachO, DEX, OAT, VDEX, ART, and DWARF executable formats. |
| Magika | — | Identify file type using signatures. |
| Malcat Lite | — | Analyze binary files using a hex editor, disassembler, and file dissector. |
| msitools <a href="#msitools" id="msitools"></a> | — | Create, inspect and extract Windows Installer (.msi) files. |
| Name-That-Hash | `nth` | Identify dfferent types of hashes. |
| numbers-to-string.py <a href="#numbers-to-string" id="numbers-to-string"></a> | — | Convert decimal numbers to strings. |
| re-search.py | — | Search the file for built-in regular expressions of common suspicious artifacts. |
| signsrch | — | Find patterns of common encryption, compression, or encoding algorithms. |
| Sleuth Kit | — | Analyze disk images and recover files from them. |
| [ssdeep](../reference/acquire-preserve/ssdeep.md) | — | Compute Context Triggered Piecewise Hashes (CTPH), also known as fuzzy hashes. |
| strings.py | — | Extract ASCII and Unicode strings from binary files with length sorting and filtering. |
| thefuzz | — | Fuzzy String Matching in Python. |
| TrID | `trid`, `tridupdate` | Identify file type using signatures. |
| wxHexEditor | — | Hex editor. |
| Yara Rules | — | Scan a file with YARA rules to identify capabilities and behaviors (packer detection, anti-debug, networking). |
| YARA-Forge Rules | — | Scan files with curated YARA rules from 45+ sources for malware family identification. |

### Examine Static Properties / Go

| Tool | Command(s) | Purpose |
|---|---|---|
| GoReSym | `GoReSym` | Extract metadata and symbols from Go binaries, including stripped ones. |
| Redress | `redress` | Analyze stripped Go binaries to recover symbols, types, source structure, and integrate with Radare2. |

### Examine Static Properties / Pe Files

| Tool | Command(s) | Purpose |
|---|---|---|
| bearparser | `bearcommander` | Parse PE file contents. |
| debloat | — | Remove junk contents from bloated Windows executables. |
| disitool.py | — | Extract, delete, copy, and inject digital signatures in PE files. |
| dllcharacteristics.py | — | Read and set DLL characteristics of a PE file. |
| Manalyze | — | Perform static analysis of suspicious PE files. |
| PE Tree | `pe-tree` | Examine contents and structure of PE files. |
| pecheck.py | — | Analyze static properties of PE files. |
| pedump | — | Statically analyze PE files and extract their components (e.g., resources). |
| pefile | — | Python library for analyzing static properties of PE files. |
| PEframe | `peframe` | Statically analyze PE and Microsoft Office files. |
| pev | `pestr`, `readpe`, `pedis`, `pehash`, `pescan`, `peldd`, `peres` | Analyze PE files and extract strings from them. |
| PortEx | `portex` | Statically analyze PE files. |
| readpe (formerly pev) | `readpe`, `pestr`, `pedis`, `pehash`, `pescan`, `pesec`, `peldd`, `pepack`, `peres`, `ofs2rva`, `rva2ofs` | Analyze PE files and extract strings from them. |

### Explore Network Interactions / Connecting

| Tool | Command(s) | Purpose |
|---|---|---|
| Anomy | `anomy` | A wrapper around wget, ssh, sftp, ftp, and telnet to route these connections through Tor to anonymize your traffic. |
| cURL | `curl` | Interact with servers via supported protocols, including HTTP, HTTPS, FTP, IMAP, etc. using this command-line tool. |
| EPIC IRC Client | `epic5` | Examine IRC activities with this IRC client. |
| GNU Wget | `wget` | Interact with servers via HTTP, HTTPS, FTP, and FTPS using this command-line tool. |
| netcat | `nc` | Read and write data across network connections. |
| thug | — | Examine suspicious website using this low-interaction honeyclient. |
| tor | — | Obfuscate your origins by routing traffic through a network of anonymizing nodes. |
| Unfurl | — | Deconstruct and decode data from a URL. |
| zbarimg | `zbarimg` | Decode QR codes and barcodes from image files. |

### Explore Network Interactions / Monitoring

| Tool | Command(s) | Purpose |
|---|---|---|
| Burp Suite Community Edition | `burpsuite` | Investigate website interactions using this web proxy. |
| cs-parse-traffic.py | — | Decrypt and parse Cobalt Strike beacon network traffic. |
| mitmproxy | `mitmproxy`, `mitmdump`, `mitmweb` | Investigate website interactions using this web proxy. |
| monitor-network | — | Monitor traffic on the first active network interface using tshark, printing a live summary to the screen or saving it t |
| Network Miner Free Edition | `networkminer` | Examine network traffic and carve PCAP capture files. |
| [ngrep](../reference/network-analysis/ngrep.md) | — | Look for patterns in network traffic. |
| PolarProxy | `polarproxy` | Intercept and decrypt TLS traffic. |
| tcpdump | — | Capture and analyze network traffic with this command-line sniffer. |
| [tcpflow](../reference/network-analysis/tcpflow.md) | — | Analyze the flow of network traffic. |
| tcpick | — | Capture and analyze network traffic with this command-line sniffer. |
| [tcpxtract](../reference/examine-the-filesystem/tcpxtract.md) | — | Extract files from network traffic. |
| [tshark](../reference/acquire-preserve/tshark.md) | — | Capture and analyze network traffic with this console-based sniffer. |
| wireshark | — | Capture and analyze network traffic with this sniffer. |

### Explore Network Interactions / Services

| Tool | Command(s) | Purpose |
|---|---|---|
| accept-all-ips | — | Accept connections to all IPv4 and IPv6 addresses and redirect it to the corresponding local port. |
| dnsresolver.py | — | DNS resolver tool for dynamic analysis with wildcard and tracking support. |
| fakedns | — | Respond to DNS queries with the specified IP address. |
| fakemail | — | Intercept and examine SMTP email activity with this fake SMTP server. |
| FakeNet-NG | — | Emulate common network services and interact with malware. |
| [INetSim](../reference/network-analysis/inetsim.md) | [`inetsim`](../reference/network-analysis/inetsim.md) | Emulate common network services and interact with malware. |
| inspircd 3 | — | Examine IRC activity with this IRC server. |
| netcat | `nc` | Read and write data across network connections. |
| Nginx | — | Web server. |

### Gather And Analyze Data / General

| Tool | Command(s) | Purpose |
|---|---|---|
| DeXRAY | `dexray` | Extract and decode data from antivirus quarantine files. |
| dissect | — | Perform a variety of forensics and incident response tasks using this DFIR framework and toolset. |
| dnslib | — | Python library to encode/decode DNS wire-format packets. |
| ioc\_parser | — | Extract IOCs from security report PDFs. |
| ipwhois | — | Retrieve and parse whois data for IP addresses. |
| malwoverview | `malwoverview` | Query public repositories of malware data (e.g., VirusTotal, HybridAnalysis). |
| nsrllookup | — | Look up MD5 file hashes in the NIST National Software Reference Library (NSRL). |
| pdnstool | — | Query passive DNS databases for DNS data. |
| [Scalpel](../reference/examine-the-filesystem/scalpel.md) | — | Carve contents out of binary files, such as partitions. |
| time-decode | — | Decode and encode date and timestamps. |
| virustotal-search | `virustotal-search.py` | Search VirusTotal for file hashes. |
| virustotal-submit | `virustotal-submit.py` | Submit files to VirusTotal. |
| [Yara](../reference/malware-triage-static/yara.md) | [`yara`](../reference/malware-triage-static/yara.md) | Identify and classify malware samples using Yara rules. |
| YARA-X | — | Scan files using YARA rules, the next generation of YARA written in Rust. |

### General Utilities / General

| Tool | Command(s) | Purpose |
|---|---|---|
| 7-Zip | [`7za`](../reference/malware-triage-static/7za.md) | Compress and decompress files using a variety of algorithms. |
| cabextract | — | Extract Microsoft cabinet (cab) files. |
| cURL | `curl` | Interact with servers via supported protocols, including HTTP, HTTPS, FTP, IMAP, etc. using this command-line tool. |
| Docker | — | Run and manage containers. |
| Firefox | `firefox` | Web browser. |
| GNOME Calculator | `galculator` | Calculator. |
| IBus | `ibus-setup` | Adjust input methods for the GUI. |
| Info-ZIP | `zip`, [`unzip`](../reference/malware-triage-static/unzip.md) | Compress and decompress files using the zip algorithm. |
| myip | — | Determine the IP address of the default network interface. |
| myjson-filter.py | — | Filter data formatted using the JSON format used by Didier Stevens' tools. |
| nasm | — | An x86-64 assembler. |
| Nautilus | — | Graphical file manager. |
| OpenSSH | `sftp`, `ssh`, `etc` | Initiate and receive SSH and SFTP connections. |
| PowerShell Core | `pwsh` | Run PowerShell scripts and commands. |
| RAR | `rar` | Compress and decompress files using a variety of algorithms. |
| REMnux Installer | — | Install and update the REMnux distro. |
| restrict-egress | — | Restrict outbound network access to an allowlist of domains and CIDRs using an nftables default-deny egress policy. It i |
| sortcanon.py | — | Sort text files using canonicalization functions built into this tool. |
| SQLite | `sqlite3` | Manage and interact with SQL database files. |
| sshpass | `sshpass` | Supply a password to SSH non-interactively for automated logins. |
| texteditor.py | — | Edit text files from the command line using search-and-replace commands. |
| unrar-free | `unrar` | Decompress files using a variety of algorithms. |
| Wine | `wine` | Run Windows applications. |

### Investigate System Interactions / General

| Tool | Command(s) | Purpose |
|---|---|---|
| ProcDOT | `procdot` | Visualize and examine the output of Process Monitor. |
| ProcmonMCP | — | MCP server that lets AI assistants analyze Process Monitor (Procmon) XML captures. |
| sandfly-processdecloak | — | Find hidden processes on the local Linux system. |
| Unhide | — | Find hidden processes or connections on the local Linux system. |

### Perform Memory Forensics / General

| Tool | Command(s) | Purpose |
|---|---|---|
| AESKeyFinder | [`aeskeyfind`](../reference/memory-forensics/aeskeyfind.md) | Find 128-bit and 256-bit AES keys in a memory image. |
| [bulk_extractor](../reference/examine-the-filesystem/bulk_extractor.md) | — | Extract interesting strings from binary files. |
| RSAKeyFinder | [`rsakeyfind`](../reference/memory-forensics/rsakeyfind.md) | Find BER-encoded RSA private keys in a memory image. |
| Volatility Framework | — | Memory forensics tool and framework. |

### Statically Analyze Code / .Net

| Tool | Command(s) | Purpose |
|---|---|---|
| de4dot | — | Deobfuscate and unpack .NET programs. |
| ILSpy | — | Examine and decompile .NET programs. |

### Statically Analyze Code / Android

| Tool | Command(s) | Purpose |
|---|---|---|
| androguard | — | Examine Android files. |
| AndroidProjectCreator | — | Convert an Android APK application file into an Android Studio project for easier analysis. |
| APKiD | `apkid` | Identify compilers, packers, and obfuscators used to protect Android APK and DEX files. |
| apktool | — | Reverse-engineer Android APK files. |
| baksmali | — | Disassembler for the dex format used by Dalvik, Android's Java VM implementation. |
| dex2jar | `dex-tools`, `d2j-dex2jar` | Examine Dalvik Executable (dex) files. |
| DroidLysis | `droidlysis` | Perform static analysis of Android applications. |
| JADX | `jadx`, `jadx-gui` | Generate Java source code from Dalvik Executable (dex) and Android APK files. |

### Statically Analyze Code / General

| Tool | Command(s) | Purpose |
|---|---|---|
| Cutter | — | Reverse engineering platform powered by Rizin. |
| Detect-It-Easy <a id="detect-it-easy"></a> | — | Determine types of files and examine file properties. |
| Ghidra | — | Software reverse engineering tool suite. |
| [objdump](../reference/malware-triage-static/objdump.md) | — | Disassemble binary files. |
| Qiling | — | Emulate code execution of PE files, shellcode, etc. for a variety of OS and hardware platforms. |
| radare2 | [`r2`](../reference/reverse-engineering/r2.md), [`rasm2`](../reference/reverse-engineering/rasm2.md), [`rabin2`](../reference/malware-triage-static/rabin2.md), [`rahash2`](../reference/acquire-preserve/rahash2.md), [`rafind2`](../reference/examine-the-filesystem/rafind2.md), `r2ai`, `decai`, `pdg` | Examine binary files, including disassembling and debugging. Includes r2ai and decai plugins for LLM-powered analysis (A |
| Vivisect | [`vivbin`](../reference/reverse-engineering/vivbin.md), [`vdbbin`](../reference/reverse-engineering/vdbbin.md) | Statically examine and emulate binary files. |

### Statically Analyze Code / Java

| Tool | Command(s) | Purpose |
|---|---|---|
| cfr | — | Java decompiler. |
| Java IDX Parser | `idx_parser.py` | Analyze Java IDX files. |
| Javassist | — | Java bytecode engineering toolkit/library. |
| JD-GUI Java Decompiler | `jd-gui` | Java decompiler with GUI. |
| Procyon | `procyon` | Java decompiler. |

### Statically Analyze Code / Pe-Files

| Tool | Command(s) | Purpose |
|---|---|---|
| binee (Binary Emulation Environment) | — | Analyze I/O operations of a suspicious PE file by emulating its execution. |
| [capa](../reference/malware-triage-static/capa.md) | — | Detect suspicious capabilities in PE files. |
| Malchive | — | Perform static analysis of various aspects of malicious code. |
| mbcscan | `mbcscan.py` | Scan a PE file to list the associated Malware Behavior Catalog (MBC) details. |
| Speakeasy | — | Emulate code execution, including shellcode, Windows drivers, and Windows PE files. |

### Statically Analyze Code / Python

| Tool | Command(s) | Purpose |
|---|---|---|
| Decompyle++ | `pycdas`, `pycdc` | Python bytecode disassembler and decompiler. |
| PyInstaller Extractor | `pyinstxtractor.py` | Extract contents of a PyInstaller-generated PE files. |
| pyinstxtractor-ng | `pyinstxtractor-ng` | Extract contents of PyInstaller-generated executables without requiring a matching Python version. |
| uncompyle6 | `uncompyle6` | Python cross-version bytecode decompiler for Python 1.0 through 3.8. |

### Statically Analyze Code / Scripts

| Tool | Command(s) | Purpose |
|---|---|---|
| AutoIt-Ripper | `autoit-ripper` | Extract AutoIt scripts embedded in PE binaries. |
| decode-vbe.py | — | Decode encoded VBS scripts (VBE). |
| GootLoaderAutoJsDecode.py | — | Statically deobfuscate GootLoader (GOOTLOADER) malicious JScript to recover the payload and extract C2 domains. |
| JS Beautifier | `js-beautify` | Reformat JavaScript scripts for easier analysis. |

### Statically Analyze Code / Unpacking

| Tool | Command(s) | Purpose |
|---|---|---|
| [binwalk](../reference/examine-the-filesystem/binwalk.md) | — | Extract and analyze firmware images. |
| Bytehist | `bytehist` | Generate byte-usage-histograms for all types of files with a focus on PE files. |
| ClamAV | [`clamscan`](../reference/malware-triage-static/clamscan.md), [`freshclam`](../reference/malware-triage-static/freshclam.md) | Scan files for malware signatures. |
| TrID | `trid`, `tridupdate` | Identify file type using signatures. |
| [UPX](../reference/malware-triage-static/upx.md) | [`upx`](../reference/malware-triage-static/upx.md) | Pack and unpack PE files. |

### Use Artificial Intelligence / General

| Tool | Command(s) | Purpose |
|---|---|---|
| GhidrAssistMCP | — | MCP server for AI-assisted reverse engineering in Ghidra. |
| OpenCode | — | Open-source AI coding agent for the terminal. |
| ProcmonMCP | — | MCP server that lets AI assistants analyze Process Monitor (Procmon) XML captures. |
| radare2 | [`r2`](../reference/reverse-engineering/r2.md), [`rasm2`](../reference/reverse-engineering/rasm2.md), [`rabin2`](../reference/malware-triage-static/rabin2.md), [`rahash2`](../reference/acquire-preserve/rahash2.md), [`rafind2`](../reference/examine-the-filesystem/rafind2.md), `r2ai`, `decai`, `pdg` | Examine binary files, including disassembling and debugging. Includes r2ai and decai plugins for LLM-powered analysis (A |
| REMnux MCP Server | `remnux-mcp-server` | MCP server for using the REMnux malware analysis toolkit via AI assistants. |
| x64dbg Automate MCP (OpenCode skills) | — | Drive x64dbg on a remote Windows VM from OpenCode on REMnux, with eight AI commands for tracing, unpacking, state snapsh |

### View Or Edit Files / General

| Tool | Command(s) | Purpose |
|---|---|---|
| dos2unix | `dos2unix`, `mac2unix`, `unix2dos`, `unix2mac` | Convert text files with Windows or macOS line breaks to Unix line breaks and vice versa. |
| Evince | `evince` | View documents in a variety of formats, including PDF. |
| feh | — | View images. |
| ImageMagick | `display`, `convert`, `mogrify`, `etc` | View and manipulate image and related files. |
| Mermaid Viewer | — | View Mermaid diagrams, such as AI-generated code-analysis workflow diagrams, in a local browser. |
| SciTE | — | Edit text files. |
| VBinDiff | `vbindiff` | Compare binary files. |
| Visual Studio Code | `code` | Powerful source code editor. |
| wxHexEditor | — | Hex editor. |


## Kali Linux

### Crypto Stego

| Tool | Command(s) | Purpose |
|---|---|---|
| aesfix | `aesfix` | Tool for correcting bit errors in an AES key schedule. |
| [aeskeyfind](../reference/memory-forensics/aeskeyfind.md) | [`aeskeyfind`](../reference/memory-forensics/aeskeyfind.md) | Tool for locating AES keys in a captured memory image. |
| ccrypt | `ccrypt` | Secure encryption and decryption of files and streams. |
| steghide | `steghide` | Steganography hiding tool. |
| stegosuite | `stegosuite` | Steganography tool to hide information in image files. |
| stegsnow | `stegsnow` | Steganography using ASCII files. |

### Database

| Tool | Command(s) | Purpose |
|---|---|---|
| jsql-injection | `jsql-injection` | Java tool for automatic database injection. |
| mdbtools | `mdbtools` | JET / MS Access database (MDB) tools. |
| oscanner | `oscanner` | Oracle assessment framework. |
| sidguesser | `sidguesser` | Guesses sids against an Oracle database. |
| sqldict | `sqldict` | Dictionary attack tool for SQL Server. |
| sqlitebrowser | `sqlitebrowser` | GUI editor for SQLite databases. |
| sqlmap | `sqlmap` | Automatic SQL injection tool. |
| sqlninja | `sqlninja` | SQL server injection and takeover tool. |
| sqlsus | `sqlsus` | MySQL injection tool. |
| tnscmd10g | `tnscmd10g` | Tool to prod the oracle tnslsnr process. |

### Exploitation

| Tool | Command(s) | Purpose |
|---|---|---|
| armitage | `armitage` | Cyber attack management for Metasploit. |
| beef-xss | `beef-xss` | Browser Exploitation Framework (BeEF). |
| exploitdb | `exploitdb` | Searchable Exploit Database archive. |
| metasploit-framework | `metasploit-framework` | Framework for exploit development and vulnerability research. |
| msfpc | `msfpc` | MSFvenom Payload Creator (MSFPC). |
| set | `set` | Social-Engineer Toolkit. |
| shellnoob | `shellnoob` | Shellcode writing toolkit. |
| sqlmap | `sqlmap` | Automatic SQL injection tool. |
| termineter | `termineter` | Smart meter testing framework. |

### Forensics

| Tool | Command(s) | Purpose |
|---|---|---|
| 7zip | `7zip` | 7-Zip file archiver with a high compression ratio. |
| afflib-tools | `afflib-tools` | Advanced Forensics Format Library (utilities). |
| apktool | `apktool` | Tool for reverse engineering Android apk files. |
| autopsy | `autopsy` | Graphical interface to SleuthKit. |
| [binwalk](../reference/examine-the-filesystem/binwalk.md) | [`binwalk`](../reference/examine-the-filesystem/binwalk.md) | Tool library for analyzing binary blobs and executable code. |
| binwalk3 | `binwalk3` | Tool library for analyzing binary blobs and executable code. |
| bulk-extractor | `bulk-extractor` |  |
| bytecode-viewer | `bytecode-viewer` | Java 8+ Jar & Android APK Reverse Engineering Suite. |
| cabextract | `cabextract` | Microsoft Cabinet file unpacker. |
| chkrootkit | `chkrootkit` | Rootkit detector. |
| creddump7 | `creddump7` | Python tool to extract credentials and secrets from Windows registry hives. |
| [dc3dd](../reference/acquire-preserve/dc3dd.md) | [`dc3dd`](../reference/acquire-preserve/dc3dd.md) | Patched version of GNU dd with forensic features. |
| [dcfldd](../reference/acquire-preserve/dcfldd.md) | [`dcfldd`](../reference/acquire-preserve/dcfldd.md) | Enhanced version of dd for forensics and security. |
| ddrescue | `ddrescue` | Data recovery and protection tool. |
| dumpzilla | `dumpzilla` | Mozilla browser forensic tool. |
| edb-debugger | `edb-debugger` | Cross platform x86/x86-64 debugger. |
| ewf-tools | `ewf-tools` | Collection of tools for reading and writing EWF files. |
| exifprobe | `exifprobe` | Read metadata from digital pictures. |
| exiv2 | `exiv2` | EXIF/IPTC/XMP metadata manipulation tool. |
| ext3grep | `ext3grep` | Tool to help recover deleted files on ext3 filesystems. |
| ext4magic | `ext4magic` | Recover deleted files from ext3 or ext4 partitions. |
| extundelete | `extundelete` | Utility to recover deleted files from ext3/ext4 partition. |
| fcrackzip | `fcrackzip` | Password cracker for zip archives. |
| firmware-mod-kit | `firmware-mod-kit` | Deconstruct and reconstruct firmware images. |
| [foremost](../reference/examine-the-filesystem/foremost.md) | [`foremost`](../reference/examine-the-filesystem/foremost.md) | Forensic program to recover lost files. |
| forensic-artifacts | `forensic-artifacts` | Knowledge base of forensic artifacts (data files). |
| forensics-colorize | `forensics-colorize` | Show differences between files using color graphics. |
| galleta | `galleta` | Internet Explorer cookie forensic analysis tool. |
| gdb | `gdb` | GNU Debugger. |
| gpart | `gpart` | Guess PC disk partition table, find lost partitions. |
| gparted | `gparted` | GNOME partition editor. |
| grokevt | `grokevt` | Scripts for reading Microsoft Windows event log files. |
| guymager | `guymager` | Forensic imaging tool based on Qt. |
| hashdeep | `hashdeep` | Recursively compute hashsums or piecewise hashings. |
| [inetsim](../reference/network-analysis/inetsim.md) | [`inetsim`](../reference/network-analysis/inetsim.md) | Software suite for simulating common internet services. |
| jadx | `jadx` | Dex to Java decompiler. |
| javasnoop | `javasnoop` | Intercept Java applications locally. |
| libhivex-bin | `libhivex-bin` | Utilities for reading and writing Windows Registry hives. |
| libsmali-java | `libsmali-java` | Assembler/disassembler for Android's dex format. |
| lvm2 | `lvm2` | Linux Logical Volume Manager. |
| lynis | `lynis` | Security auditing tool for Unix based systems. |
| mac-robber | `mac-robber` | Collects data about allocated files in mounted filesystems. |
| magicrescue | `magicrescue` | Recover files by looking for magic bytes. |
| md5deep | `md5deep` |  |
| mdbtools | `mdbtools` | JET / MS Access database (MDB) tools. |
| memdump | `memdump` | Utility to dump memory contents to standard output. |
| metacam | `metacam` | Extract EXIF information from digital camera files. |
| missidentify | `missidentify` | Find win32 applications. |
| myrescue | `myrescue` | Rescue data from damaged disks. |
| nasm | `nasm` | General-purpose x86 assembler. |
| nasty | `nasty` | Tool which helps you to recover your GPG passphrase. |
| ollydbg | `ollydbg` | 32-bit assembler level analysing debugger. |
| parted | `parted` | Disk partition manipulator. |
| pasco | `pasco` | Internet Explorer cache forensic analysis tool. |
| [pdf-parser](../reference/malware-triage-documents/pdf-parser.md) | [`pdf-parser`](../reference/malware-triage-documents/pdf-parser.md) | Parses PDF files to identify fundamental elements. |
| [pdfid](../reference/malware-triage-documents/pdfid.md) | [`pdfid`](../reference/malware-triage-documents/pdfid.md) | Scans PDF files for certain PDF keywords. |
| plaso | `plaso` | Super timeline all the things -- metapackage. |
| polenum | `polenum` | Extracts the password policy from a Windows system. |
| pst-utils | `pst-utils` | Tools for reading Microsoft Outlook PST files. |
| python3-capstone | `python3-capstone` | Lightweight multi-architecture disassembly framework - Python bindings. |
| python3-dfdatetime | `python3-dfdatetime` | Digital Forensics date and time library for Python 3. |
| python3-dfvfs | `python3-dfvfs` | Digital Forensics Virtual File System. |
| python3-dfwinreg | `python3-dfwinreg` | Digital Forensics Windows Registry library for Python 3. |
| python3-distorm3 | `python3-distorm3` | Powerful disassembler library for x86/AMD64 binary streams (Python3 bindings). |
| radare2 | `radare2` | Free and advanced command line hexadecimal editor. |
| readpe | `readpe` | Command-line tools to manipulate Windows PE files. |
| recoverdm | `recoverdm` | Recover files on disks with damaged sectors. |
| recoverjpeg | `recoverjpeg` | Recover JFIF (JPEG) pictures and MOV movies. |
| recstudio | `recstudio` |  |
| reglookup | `reglookup` | Utility to analysis for Windows NT-based registry. |
| [regripper](../reference/windows-artifacts/regripper.md) | [`regripper`](../reference/windows-artifacts/regripper.md) | Perform forensic analysis of registry hives. |
| rephrase | `rephrase` | Specialized passphrase recovery tool for GnuPG. |
| rifiuti | `rifiuti` | MS Windows recycle bin analysis tool. |
| rifiuti2 | `rifiuti2` | Replacement for rifiuti, a MS Windows recycle bin analysis tool. |
| rizin-cutter | `rizin-cutter` | Reverse engineering platform powered by rizin. |
| rkhunter | `rkhunter` | Rootkit, backdoor, sniffer and exploit scanner. |
| [rsakeyfind](../reference/memory-forensics/rsakeyfind.md) | [`rsakeyfind`](../reference/memory-forensics/rsakeyfind.md) | Locates BER-encoded RSA private keys in memory images. |
| rz-ghidra | `rz-ghidra` | Ghidra decompiler and sleigh disassembler for rizin. |
| safecopy | `safecopy` | Data recovery tool for problematic or damaged media. |
| samdump2 | `samdump2` | Dump Windows 2k/NT/XP password hashes. |
| [scalpel](../reference/examine-the-filesystem/scalpel.md) | [`scalpel`](../reference/examine-the-filesystem/scalpel.md) | Fast filesystem-independent file recovery. |
| scrounge-ntfs | `scrounge-ntfs` | Data recovery program for NTFS filesystems. |
| sleuthkit | `sleuthkit` | Tools for forensics analysis on volume and filesystem data. |
| sqlitebrowser | `sqlitebrowser` | GUI editor for SQLite databases. |
| [ssdeep](../reference/acquire-preserve/ssdeep.md) | [`ssdeep`](../reference/acquire-preserve/ssdeep.md) | Recursive piecewise hashing tool. |
| tcpdump | `tcpdump` | Command-line network traffic analyzer. |
| [tcpflow](../reference/network-analysis/tcpflow.md) | [`tcpflow`](../reference/network-analysis/tcpflow.md) | TCP flow recorder. |
| tcpick | `tcpick` | TCP stream sniffer and connection tracker. |
| tcpreplay | `tcpreplay` | Tool to replay saved tcpdump files at arbitrary speeds. |
| truecrack | `truecrack` | Bruteforce password cracker for TrueCrypt volumes. |
| undbx | `undbx` | Tool to extract, recover and undelete e-mail messages from .dbx files. |
| unhide | `unhide` | Forensic tool to find hidden processes and ports. |
| unrar | `unrar` |  |
| upx-ucl | `upx-ucl` | Efficient live-compressor for executables. |
| vinetto | `vinetto` | Forensics tool to examine Thumbs.db files. |
| wce | `wce` |  |
| winregfs | `winregfs` | Windows registry FUSE filesystem. |
| wireshark | `wireshark` | Network traffic analyzer - graphical interface. |
| xmount | `xmount` | Tool for crossmounting between disk image formats. |
| xplico | `xplico` | Network Forensic Analysis Tool (NFAT). |
| [yara](../reference/malware-triage-static/yara.md) | [`yara`](../reference/malware-triage-static/yara.md) | Pattern matching swiss knife for malware researchers. |

### Fuzzing

| Tool | Command(s) | Purpose |
|---|---|---|
| afl++ | `afl++` | Instrumentation-driven fuzzer for binary formats. |
| sfuzz | `sfuzz` | Black Box testing utilities. |
| spike | `spike` | Network protocol fuzzer. |
| wfuzz | `wfuzz` | Web application bruteforcer. |

### Information Gathering

| Tool | Command(s) | Purpose |
|---|---|---|
| 0trace | `0trace` | Traceroute tool that can run within an existing TCP connection. |
| arping | `arping` | Sends IP and/or ARP pings (to the MAC address). |
| braa | `braa` | Mass SNMP scanner. |
| dmitry | `dmitry` | Deepmagic Information Gathering Tool. |
| dnsenum | `dnsenum` | Tool to enumerate domain DNS information. |
| dnsmap | `dnsmap` | DNS domain name brute forcing tool. |
| dnsrecon | `dnsrecon` | Powerful DNS enumeration script. |
| dnstracer | `dnstracer` | Trace DNS queries to the source. |
| dnswalk | `dnswalk` | Checks dns zone information using nameserver lookups. |
| enum4linux | `enum4linux` | Enumerates info from Windows and Samba systems. |
| fierce | `fierce` | Domain DNS scanner. |
| firewalk | `firewalk` | Active reconnaissance network security tool. |
| fping | `fping` | Sends ICMP ECHO_REQUEST packets to network hosts. |
| fragrouter | `fragrouter` | IDS evasion toolkit. |
| ftester | `ftester` | Tool for testing firewalls and Intrusion Detection System (IDS). |
| hping3 | `hping3` | Active Network Smashing Tool. |
| ike-scan | `ike-scan` | Discover and fingerprint IKE hosts (IPsec VPN Servers). |
| intrace | `intrace` | Traceroute-like application piggybacking on existing TCP connections. |
| irpas | `irpas` |  |
| lbd | `lbd` | Load balancer detector. |
| legion | `legion` | Semi-automated network penetration testing tool. |
| maltego | `maltego` |  |
| masscan | `masscan` | TCP port scanner. |
| metagoofil | `metagoofil` | Tool designed for extracting metadata of public documents. |
| nbtscan | `nbtscan` | Scan networks searching for NetBIOS information. |
| ncat | `ncat` | NMAP netcat reimplementation. |
| netdiscover | `netdiscover` | Active/passive network address scanner using ARP requests. |
| netmask | `netmask` | Helps determine network masks. |
| [nmap](../reference/network-analysis/nmap.md) | [`nmap`](../reference/network-analysis/nmap.md) | The Network Mapper. |
| onesixtyone | `onesixtyone` | Fast and simple SNMP scanner. |
| p0f | `p0f` | Passive OS fingerprinting tool. |
| qsslcaudit | `qsslcaudit` | Test SSL/TLS clients how secure they are. |
| recon-ng | `recon-ng` | Web Reconnaissance framework written in Python. |
| smbmap | `smbmap` | Handy SMB enumeration tool. |
| smtp-user-enum | `smtp-user-enum` | Username guessing tool for the SMTP service. |
| snmpcheck | `snmpcheck` | SNMP service enumeration tool. |
| ssldump | `ssldump` | SSLv3/TLS network protocol analyzer. |
| sslh | `sslh` | Applicative protocol multiplexer. |
| sslscan | `sslscan` | Tests SSL/TLS enabled services to discover supported cipher suites. |
| sslyze | `sslyze` | Fast and full-featured SSL scanner. |
| swaks | `swaks` | SMTP command-line test tool. |
| thc-ipv6 | `thc-ipv6` | The Hacker Choice's IPv6 Attack Toolkit. |
| theharvester | `theharvester` | Tool for gathering e-mail accounts and subdomain names from public sources. |
| tlssled | `tlssled` | Evaluates the security of a target SSL/TLS (HTTPS) server. |
| twofi | `twofi` | Twitter words of interest. |
| unicornscan | `unicornscan` | Userland distributed TCP/IP stack. |
| urlcrazy | `urlcrazy` |  |
| wafw00f | `wafw00f` | Identify and fingerprint Web Application Firewall products. |
| zenmap | `zenmap` |  |

### Passwords

| Tool | Command(s) | Purpose |
|---|---|---|
| cewl | `cewl` | Custom word list generator. |
| chntpw | `chntpw` | NT SAM password recovery utility. |
| cisco-auditing-tool | `cisco-auditing-tool` | Scans Cisco routers for vulnerabilities. |
| cmospwd | `cmospwd` | Decrypt BIOS passwords from CMOS. |
| crackle | `crackle` | Crack and decrypt BLE encryption. |
| creddump7 | `creddump7` | Python tool to extract credentials and secrets from Windows registry hives. |
| crunch | `crunch` | Tool for creating wordlist. |
| fcrackzip | `fcrackzip` | Password cracker for zip archives. |
| freerdp3-x11 | `freerdp3-x11` | RDP client for Windows Terminal Services (X11 client tramsitional package). |
| gpp-decrypt | `gpp-decrypt` | Group Policy Preferences decrypter. |
| hash-identifier | `hash-identifier` | Tool to identify hash types. |
| [hashcat](../reference/decode-deobfuscate/hashcat.md) | [`hashcat`](../reference/decode-deobfuscate/hashcat.md) | World's fastest and most advanced password recovery utility. |
| hashcat-utils | `hashcat-utils` | Set of small utilities for advanced password cracking. |
| hashid | `hashid` | Identify the different types of hashes used to encrypt data. |
| [hydra](../reference/decode-deobfuscate/hydra.md) | [`hydra`](../reference/decode-deobfuscate/hydra.md) | Very fast network logon cracker. |
| hydra-gtk | `hydra-gtk` | Very fast network logon cracker - GTK+ based GUI. |
| [john](../reference/decode-deobfuscate/john.md) | [`john`](../reference/decode-deobfuscate/john.md) | Active password cracking tool. |
| johnny | `johnny` | GUI for John the Ripper. |
| maskprocessor | `maskprocessor` | High-performance word generator with a per-position configurable charset. |
| medusa | `medusa` | Fast, parallel, modular, login brute-forcer for network services. |
| mimikatz | `mimikatz` | Uses admin rights on Windows to display passwords in plaintext. |
| ncrack | `ncrack` | High-speed network authentication cracking tool. |
| onesixtyone | `onesixtyone` | Fast and simple SNMP scanner. |
| ophcrack | `ophcrack` | Microsoft Windows password cracker using rainbow tables (gui). |
| ophcrack-cli | `ophcrack-cli` | Microsoft Windows password cracker using rainbow tables (cmdline). |
| pack | `pack` | Password analysis and cracking kit. |
| pack2 | `pack2` | Password analysis and cracking kit 2. |
| passing-the-hash | `passing-the-hash` | Patched tools to use password hashes as authentication input. |
| patator | `patator` | Multi-purpose brute-forcer. |
| pdfcrack | `pdfcrack` | PDF files password cracker. |
| pipal | `pipal` | Statistical analysis on password dumps. |
| polenum | `polenum` | Extracts the password policy from a Windows system. |
| rainbowcrack | `rainbowcrack` | Rainbow table password cracker. |
| rarcrack | `rarcrack` | Password cracker for rar archives. |
| rcracki-mt | `rcracki-mt` | Version of rcrack that supports hybrid and indexed tables. |
| rsmangler | `rsmangler` | Wordlist mangling tool. |
| samdump2 | `samdump2` | Dump Windows 2k/NT/XP password hashes. |
| seclists | `seclists` | Collection of multiple types of security lists. |
| sipcrack | `sipcrack` | SIP login dumper/cracker. |
| sipvicious | `sipvicious` | Tools to audit SIP based VoIP systems. |
| smbmap | `smbmap` | Handy SMB enumeration tool. |
| sqldict | `sqldict` | Dictionary attack tool for SQL Server. |
| statsprocessor | `statsprocessor` | Word generator based on per-position Markov chains. |
| sucrack | `sucrack` | Multithreaded su bruteforcer. |
| thc-pptp-bruter | `thc-pptp-bruter` | THC PPTP Brute Force. |
| truecrack | `truecrack` | Bruteforce password cracker for TrueCrypt volumes. |
| twofi | `twofi` | Twitter words of interest. |
| wordlists | `wordlists` | Contains the rockyou wordlist. |

### Post Exploitation

| Tool | Command(s) | Purpose |
|---|---|---|
| cymothoa | `cymothoa` | Stealth backdooring tool. |
| dbd | `dbd` | Netcat clone with encryption. |
| dns2tcp | `dns2tcp` | TCP-over-DNS tunnel server and client. |
| exe2hexbat | `exe2hexbat` | Convert EXE to bat. |
| iodine | `iodine` | Tool for tunneling IPv4 data through a DNS server. |
| laudanum | `laudanum` | Collection of injectable web files. |
| mimikatz | `mimikatz` | Uses admin rights on Windows to display passwords in plaintext. |
| miredo | `miredo` | Teredo IPv6 tunneling through NATs. |
| nishang | `nishang` | Collection of PowerShell scripts and payloads. |
| powersploit | `powersploit` | PowerShell Post-Exploitation Framework. |
| proxychains4 | `proxychains4` | Redirect connections through socks/http proxies (proxychains-ng). |
| proxytunnel | `proxytunnel` | Help SSH and other protocols through HTTP(S) proxies. |
| ptunnel | `ptunnel` | Tunnel TCP connections over ICMP packets. |
| pwnat | `pwnat` | NAT to NAT client-server communication. |
| sbd | `sbd` | Secure backdoor for Linux and Windows. |
| shellter | `shellter` |  |
| sslh | `sslh` | Applicative protocol multiplexer. |
| stunnel4 | `stunnel4` | Universal SSL tunnnel for network daemons - compatibility package. |
| udptunnel | `udptunnel` | Tunnel UDP packets over a TCP connection. |
| veil | `veil` | Generates payloads to bypass anti-virus solutions. |
| webacoo | `webacoo` | Web backdoor cookie script kit. |
| weevely | `weevely` | Stealth tiny web shell. |

### Reverse Engineering

| Tool | Command(s) | Purpose |
|---|---|---|
| apktool | `apktool` | Tool for reverse engineering Android apk files. |
| bytecode-viewer | `bytecode-viewer` | Java 8+ Jar & Android APK Reverse Engineering Suite. |
| clang | `clang` | C, C++ and Objective-C compiler (LLVM based), clang binary. |
| dex2jar | `dex2jar` | Tools to work with android .dex and java .class files. |
| edb-debugger | `edb-debugger` | Cross platform x86/x86-64 debugger. |
| jadx | `jadx` | Dex to Java decompiler. |
| javasnoop | `javasnoop` | Intercept Java applications locally. |
| jd-gui | `jd-gui` | GUI Java .class decompiler. |
| metasploit-framework | `metasploit-framework` | Framework for exploit development and vulnerability research. |
| ollydbg | `ollydbg` | 32-bit assembler level analysing debugger. |
| radare2 | `radare2` | Free and advanced command line hexadecimal editor. |
| recstudio | `recstudio` |  |
| rizin | `rizin` | Reverse engineering framework and command-line toolset. |
| rizin-cutter | `rizin-cutter` | Reverse engineering platform powered by rizin. |
| rz-ghidra | `rz-ghidra` | Ghidra decompiler and sleigh disassembler for rizin. |

### Sniffing Spoofing

| Tool | Command(s) | Purpose |
|---|---|---|
| above | `above` | Network security sniffer for finding vulnerabilities in the network. |
| bettercap | `bettercap` | Complete, modular, portable and easily extensible MITM framework. |
| darkstat | `darkstat` | Network traffic analyzer. |
| dnschef | `dnschef` | DNS proxy for penetration testers. |
| driftnet | `driftnet` | Picks out and displays images from network traffic. |
| dsniff | `dsniff` | Various tools to sniff network traffic for cleartext insecurities. |
| ettercap-graphical | `ettercap-graphical` | Ettercap GUI-enabled executable. |
| ferret-sidejack | `ferret-sidejack` | Monitors data and extracts interesting data. |
| fiked | `fiked` | Cisco VPN attack tool. |
| hamster-sidejack | `hamster-sidejack` | Sidejacking tool. |
| hexinject | `hexinject` | Versatile packet injector and sniffer. |
| isr-evilgrade | `isr-evilgrade` | Evilgrade framework. |
| macchanger | `macchanger` | Utility for manipulating the MAC address of network interfaces. |
| mitmproxy | `mitmproxy` | SSL-capable man-in-the-middle HTTP proxy. |
| netsniff-ng | `netsniff-ng` | Linux network packet sniffer toolkit. |
| rebind | `rebind` | DNS rebinding tool. |
| responder | `responder` | LLMNR/NBT-NS/mDNS Poisoner. |
| sniffjoke | `sniffjoke` | Transparent TCP connection scrambler. |
| sslsniff | `sslsniff` | SSL/TLS man-in-the-middle attack tool. |
| sslsplit | `sslsplit` | Transparent and scalable SSL/TLS interception. |
| [tcpflow](../reference/network-analysis/tcpflow.md) | [`tcpflow`](../reference/network-analysis/tcpflow.md) | TCP flow recorder. |
| tcpreplay | `tcpreplay` | Tool to replay saved tcpdump files at arbitrary speeds. |
| wifi-honey | `wifi-honey` | Wi-Fi honeypot. |
| wireshark | `wireshark` | Network traffic analyzer - graphical interface. |

### Vulnerability

| Tool | Command(s) | Purpose |
|---|---|---|
| afl++ | `afl++` | Instrumentation-driven fuzzer for binary formats. |
| bed | `bed` | A network protocol fuzzer. |
| cisco-auditing-tool | `cisco-auditing-tool` | Scans Cisco routers for vulnerabilities. |
| cisco-global-exploiter | `cisco-global-exploiter` | Simple and fast Cisco exploitation tool. |
| cisco-ocs | `cisco-ocs` | Mass Cisco scanner. |
| cisco-torch | `cisco-torch` | Cisco device scanner. |
| copy-router-config | `copy-router-config` | Copies Cisco configs via SNMP. |
| dhcpig | `dhcpig` | DHCP exhaustion script using scapy network library. |
| enumiax | `enumiax` | IAX protocol username enumerator. |
| gvm | `gvm` | Remote network security auditor - metapackage and useful scripts. |
| iaxflood | `iaxflood` | VoIP flooder tool. |
| inviteflood | `inviteflood` | SIP/SDP INVITE message flooding over UDP/IP. |
| legion | `legion` | Semi-automated network penetration testing tool. |
| lynis | `lynis` | Security auditing tool for Unix based systems. |
| nikto | `nikto` |  |
| [nmap](../reference/network-analysis/nmap.md) | [`nmap`](../reference/network-analysis/nmap.md) | The Network Mapper. |
| ohrwurm | `ohrwurm` | RTP fuzzer. |
| peass | `peass` | Privilege Escalation Awesome Scripts SUITE. |
| protos-sip | `protos-sip` | SIP test suite. |
| rtpbreak | `rtpbreak` | Detects, reconstructs, and analyzes RTP sessions. |
| rtpflood | `rtpflood` | Tool to flood any RTP device. |
| rtpinsertsound | `rtpinsertsound` | Inserts audio into a specified stream. |
| rtpmixsound | `rtpmixsound` | Mixes pre-recorded audio in real-time. |
| sctpscan | `sctpscan` | SCTP network scanner for discovery and security. |
| sfuzz | `sfuzz` | Black Box testing utilities. |
| siege | `siege` | HTTP regression testing and benchmarking utility. |
| siparmyknife | `siparmyknife` | SIP fuzzing tool. |
| sipp | `sipp` | Traffic generator for the SIP protocol. |
| sipsak | `sipsak` | SIP Swiss army knife. |
| sipvicious | `sipvicious` | Tools to audit SIP based VoIP systems. |
| slowhttptest | `slowhttptest` | Application layer Denial of Service attacks simulation tool. |
| spike | `spike` | Network protocol fuzzer. |
| t50 | `t50` | Multi-protocol packet injector tool. |
| thc-ssl-dos | `thc-ssl-dos` | Stress tester for the SSL handshake. |
| unix-privesc-check | `unix-privesc-check` | Script to check for simple privilege escalation vectors. |
| voiphopper | `voiphopper` | Runs a VLAN hop security test. |
| yersinia | `yersinia` | Network vulnerabilities check software. |

### Web

| Tool | Command(s) | Purpose |
|---|---|---|
| apache-users | `apache-users` | Enumerate usernames on systems with Apache UserDir module. |
| apache2 | `apache2` | Apache HTTP Server. |
| beef-xss | `beef-xss` | Browser Exploitation Framework (BeEF). |
| burpsuite | `burpsuite` | Platform for security testing of web applications. |
| cadaver | `cadaver` | Command-line WebDAV client. |
| commix | `commix` | Automated All-in-One OS Command Injection and Exploitation Tool. |
| cutycapt | `cutycapt` | Utility to capture WebKit's rendering of a web page. |
| davtest | `davtest` | Testing tool for WebDAV servers. |
| default-mysql-server | `default-mysql-server` | MySQL database server binaries and system database setup (metapackage). |
| dirb | `dirb` | URL bruteforcing tool. |
| dirbuster | `dirbuster` | Web server directory brute-forcer. |
| dotdotpwn | `dotdotpwn` | Directory Traversal Fuzzer. |
| eyewitness | `eyewitness` | Rapid web application triage tool. |
| ferret-sidejack | `ferret-sidejack` | Monitors data and extracts interesting data. |
| ftester | `ftester` | Tool for testing firewalls and Intrusion Detection System (IDS). |
| hakrawler | `hakrawler` | Web crawler designed for easy, quick discovery of endpoints and assets. |
| hamster-sidejack | `hamster-sidejack` | Sidejacking tool. |
| heartleech | `heartleech` | Scanner detecting systems vulnerable to the heartbleed OpenSSL bug. |
| httprint | `httprint` |  |
| httrack | `httrack` | Copy websites to your computer (Offline browser). |
| [hydra](../reference/decode-deobfuscate/hydra.md) | [`hydra`](../reference/decode-deobfuscate/hydra.md) | Very fast network logon cracker. |
| hydra-gtk | `hydra-gtk` | Very fast network logon cracker - GTK+ based GUI. |
| jboss-autopwn | `jboss-autopwn` | JBoss script for obtaining remote shell access. |
| joomscan | `joomscan` | OWASP Joomla Vulnerability Scanner Project. |
| jsql-injection | `jsql-injection` | Java tool for automatic database injection. |
| laudanum | `laudanum` | Collection of injectable web files. |
| lbd | `lbd` | Load balancer detector. |
| maltego | `maltego` |  |
| medusa | `medusa` | Fast, parallel, modular, login brute-forcer for network services. |
| mitmproxy | `mitmproxy` | SSL-capable man-in-the-middle HTTP proxy. |
| ncrack | `ncrack` | High-speed network authentication cracking tool. |
| nikto | `nikto` |  |
| nishang | `nishang` | Collection of PowerShell scripts and payloads. |
| [nmap](../reference/network-analysis/nmap.md) | [`nmap`](../reference/network-analysis/nmap.md) | The Network Mapper. |
| oscanner | `oscanner` | Oracle assessment framework. |
| owasp-mantra-ff | `owasp-mantra-ff` |  |
| padbuster | `padbuster` | Script for performing Padding Oracle attacks. |
| paros | `paros` | Web application proxy. |
| patator | `patator` | Multi-purpose brute-forcer. |
| php | `php` | Server-side, HTML-embedded scripting language (default). |
| php-mysql | `php-mysql` | MySQL module for PHP [default]. |
| proxychains4 | `proxychains4` | Redirect connections through socks/http proxies (proxychains-ng). |
| proxytunnel | `proxytunnel` | Help SSH and other protocols through HTTP(S) proxies. |
| qsslcaudit | `qsslcaudit` | Test SSL/TLS clients how secure they are. |
| redsocks | `redsocks` | Arbitrary TCP connection redirector to a SOCKS or HTTPS proxy server. |
| sidguesser | `sidguesser` | Guesses sids against an Oracle database. |
| siege | `siege` | HTTP regression testing and benchmarking utility. |
| skipfish | `skipfish` | Fully automated, active web application security reconnaissance tool. |
| slowhttptest | `slowhttptest` | Application layer Denial of Service attacks simulation tool. |
| sqldict | `sqldict` | Dictionary attack tool for SQL Server. |
| sqlitebrowser | `sqlitebrowser` | GUI editor for SQLite databases. |
| sqlmap | `sqlmap` | Automatic SQL injection tool. |
| sqlninja | `sqlninja` | SQL server injection and takeover tool. |
| sqlsus | `sqlsus` | MySQL injection tool. |
| ssldump | `ssldump` | SSLv3/TLS network protocol analyzer. |
| sslh | `sslh` | Applicative protocol multiplexer. |
| sslscan | `sslscan` | Tests SSL/TLS enabled services to discover supported cipher suites. |
| sslsniff | `sslsniff` | SSL/TLS man-in-the-middle attack tool. |
| sslsplit | `sslsplit` | Transparent and scalable SSL/TLS interception. |
| sslyze | `sslyze` | Fast and full-featured SSL scanner. |
| stunnel4 | `stunnel4` | Universal SSL tunnnel for network daemons - compatibility package. |
| thc-ssl-dos | `thc-ssl-dos` | Stress tester for the SSL handshake. |
| tlssled | `tlssled` | Evaluates the security of a target SSL/TLS (HTTPS) server. |
| tnscmd10g | `tnscmd10g` | Tool to prod the oracle tnslsnr process. |
| uniscan | `uniscan` | LFI, RFI, and RCE vulnerability scanner. |
| wafw00f | `wafw00f` | Identify and fingerprint Web Application Firewall products. |
| wapiti | `wapiti` | Web application vulnerability scanner. |
| watobo | `watobo` | Semi-automated web application scanner. |
| webacoo | `webacoo` | Web backdoor cookie script kit. |
| webscarab | `webscarab` | Web application review tool. |
| webshells | `webshells` | Collection of webshells. |
| weevely | `weevely` | Stealth tiny web shell. |
| wfuzz | `wfuzz` | Web application bruteforcer. |
| whatweb | `whatweb` | Next generation web scanner. |
| wireshark | `wireshark` | Network traffic analyzer - graphical interface. |
| wpscan | `wpscan` |  |
| xsser | `xsser` | XSS testing framework. |
| zaproxy | `zaproxy` | Testing tool for finding vulnerabilities in web applications. |


## FLARE-VM

### All Packages (choco)

| Tool | Command(s) | Purpose |
|---|---|---|
| 010editor | `010editor` | Professional text and hex editor with Binary Templates technology. |
| 7zip | `7zip` | 7-Zip file archiver with a high compression ratio. |
| advanced-installer | `advanced-installer` | Advanced Installer is a Windows installer authoring tool that can be used to analyze MSI files. |
| angr | `angr` | Angr is a multi-architecture binary analysis toolkit providing features like disassembly, IR lifting, program instr... |
| apimonitor | `apimonitor` | API Monitor lets you monitor and control API calls made by applications and services. |
| apktool | `apktool` | Tool for reverse engineering Android apk files. |
| asar | `asar` | Asar decompresses .asar archives. |
| autoit-ripper | `autoit-ripper` | Extracts compiled AutoIt scripts from PE executables. |
| binaryninja | `binaryninja` | Binary Ninja is an interactive decompiler, disassembler, debugger, and binary analysis platform built by reverse en... |
| bindiff | `bindiff` | A comparison tool for binary files that assists in quickly finding differences and similarities in disassembled code. |
| blobrunner | `blobrunner` | BlobRunner is a simple tool to quickly debug shellcode extracted during malware analysis. |
| blobrunner64 | `blobrunner64` | BlobRunner is a simple tool to quickly debug shellcode extracted during malware analysis. |
| bytecodeviewer | `bytecodeviewer` | A lightweight user-friendly Java/Android Bytecode Viewer, Decompiler and more. |
| [capa](../reference/malware-triage-static/capa.md) | [`capa`](../reference/malware-triage-static/capa.md) | Capa detects capabilities in executable files. You run it against a PE file or shellcode and it tells you what it t... |
| capa-explorer-web | `capa-explorer-web` | Web interface for exploring and understanding capa results. |
| chrome.extensions | `chrome.extensions` | A package for multiple useful chrome extensions from the Chrome webstore. |
| cmder | `cmder` | Metapackage for cmder. |
| codetrack | `codetrack` | A free .NET Performance Profile and Execution Analyzer. |
| [cryptotester](../reference/decode-deobfuscate/CryptoTester-gui.md) | [`cryptotester`](../reference/decode-deobfuscate/CryptoTester-gui.md) | Utility tool for performing cryptanalysis with a focus on ransomware cryptography. |
| cutter | `cutter` | Disconnect routed IP connections. |
| [cyberchef](../reference/decode-deobfuscate/cyberchef.md) | [`cyberchef`](../reference/decode-deobfuscate/cyberchef.md) | Cyber Swiss Army Knife. |
| cygwin | `cygwin` | Wrapper for cygwin and useful cygwin packages. |
| de4dot-cex | `de4dot-cex` | A de4dot fork with full support for vanilla ConfuserEx. |
| dependencywalker | `dependencywalker` | Scans PE files and builds a hierarchical tree diagram of all dependent modules. |
| dex2jar | `dex2jar` | Tools to work with android .dex and java .class files. |
| didier-stevens-beta | `didier-stevens-beta` | Beta versions of Didier Stevens's software. |
| didier-stevens-suite | `didier-stevens-suite` | Tools colection by Didier Stevens. |
| [die](../reference/malware-triage-static/die.md) | [`die`](../reference/malware-triage-static/die.md) | Detect It Easy, or abbreviated "DIE" is a program for determining types of files. |
| dll-to-exe | `dll-to-exe` | Converts a DLL into a ready-to-use EXE. |
| dnlib | `dnlib` | .NET module/assembly reader/writer library. |
| dnspyex | `dnspyex` | DnSpyEx is a unofficial continuation of the dnSpy project which is a debugger and .NET assembly editor. You can use... |
| dotdumper | `dotdumper` | An automatic unpacker and logger for DotNet Framework targeting files. |
| dotnet3.5 | `dotnet3.5` |  |
| exeinfope | `exeinfope` | Displays metadata for a variety of file types and identifies many executable packers. |
| explorersuite | `explorersuite` | A suite of tools including CFF Explorer and a process viewer. |
| extreme_dumper | `extreme_dumper` | .NET Assembly Dumper from memory of processes. |
| ezviewer | `ezviewer` | Standalone, zero dependency viewer for .doc, .docx, .xls, .xlsx, .txt, .log, .rtf, .otd, .htm, .html, .mht, .csv, a... |
| fakenet-ng | `fakenet-ng` | FakeNet-NG is a next generation dynamic network analysis tool for malware analysts and penetration testers. |
| fiddler | `fiddler` | Intercepts, decrypts, and analyzes HTTPS traffic. |
| [file](../reference/examine-the-filesystem/file.md) | [`file`](../reference/examine-the-filesystem/file.md) | Recognize the type of data in a file using "magic" numbers. |
| [floss](../reference/malware-triage-static/floss.md) | [`floss`](../reference/malware-triage-static/floss.md) | FLOSS uses advanced static analysis techniques to automatically deobfuscate strings from malware binaries. You can... |
| garbageman | `garbageman` | A set of tools designed for .NET heap analysis. |
| ghidra | `ghidra` | Software Reverse Engineering Framework. |
| goresym | `goresym` | Go symbol recovery tool. |
| gostringungarbler | `gostringungarbler` | GoStringUngarbler deobfuscates strings in Go binaries obfuscated by garble. |
| [hashmyfiles](../reference/acquire-preserve/HashMyFiles-gui.md) | [`hashmyfiles`](../reference/acquire-preserve/HashMyFiles-gui.md) | HashMyFiles is small utility that allows you to calculate the MD5 and SHA1 hashes of one or more files in your syst... |
| hollowshunter | `hollowshunter` | Scans all running processes. Recognizes and dumps a variety of potentially malicious implants (replaced/implanted P... |
| hxd | `hxd` | Freeware hex editor. |
| ida.plugin.capa | `ida.plugin.capa` | Capa explorer is an IDAPython plugin that integrates capa with IDA Pro. |
| ida.plugin.comida | `ida.plugin.comida` | IDA Plugin that help analyzing modules using COM. |
| ida.plugin.delphihelper | `ida.plugin.delphihelper` | DelphiHelper. |
| ida.plugin.dereferencing | `ida.plugin.dereferencing` | IDA Pro plugin that implements new registers and stack views. |
| ida.plugin.diaphora | `ida.plugin.diaphora` | Diaphora is a program diffing IDA plugin. |
| ida.plugin.flare | `ida.plugin.flare` | IDA Pro plugins used by the FLARE team. |
| ida.plugin.flare-emu | `ida.plugin.flare-emu` | A user friendly scriptable emulation framework that supports multiple binary analysis tools. |
| ida.plugin.hashdb | `ida.plugin.hashdb` | Malware string hash lookup plugin for IDA Pro. |
| ida.plugin.hrtng | `ida.plugin.hrtng` | IDA Pro plugin with features such as decryption, automation, deobfuscation, patching, lib code recognition and pseu... |
| ida.plugin.ifl | `ida.plugin.ifl` | Interactive Functions List IDA Pro plugin. |
| ida.plugin.xray | `ida.plugin.xray` | Hexrays decompiler plugin that colorizes and filters the decompiler's output based on regular expressions. |
| ida.plugin.xrefer | `ida.plugin.xrefer` | Custom navigation interface within IDA. |
| idafree | `idafree` | Free version of IDA, a powerful Interactive DisAssembler and debugger. |
| [idr](../reference/reverse-engineering/idr-gui.md) | [`idr`](../reference/reverse-engineering/idr-gui.md) | Interactive Delphi Reconstructor. |
| ifpstools | `ifpstools` | IFPSTools.NET: tools for working with RemObject PascalScript compiled bytecode files. |
| ilspy | `ilspy` | ILSpy is a .NET assembly browser and decompiler. |
| innoextract | `innoextract` | Tool for extracting data from an Inno Setup installer. |
| innounp | `innounp` | Unpacker for Inno Setup installers. |
| internet_detector | `internet_detector` | Tool that changes the background and a taskbar icon if it detects internet connectivity. |
| ipython | `ipython` | A powerful interactive Python shell. |
| isd | `isd` | Inno Setup Decompiler. |
| js-beautify | `js-beautify` | JavaScript beautifier and deobfuscator. |
| js-deobfuscator | `js-deobfuscator` | Deobfuscator to remove common JS obfuscation techniques. |
| keystone | `keystone` | OpenStack identity service. |
| libraries.python3 | `libraries.python3` | Metapackage to install common Python 3.9 libraries. |
| magika | `magika` | Magika is an AI powered file type detection tool that uses deep learning to provide accurate detection. |
| malware-jail | `malware-jail` | Sandbox for semi-automatic Javascript malware analysis, deobfuscation and payload extraction. |
| map | `map` | Handful of small utility type applications useful for analyzing malicious code. |
| microsoft-office | `microsoft-office` | Microsoft Office ProPlusRetail. |
| nasm | `nasm` | General-purpose x86 assembler. |
| net-reactor-slayer | `net-reactor-slayer` | NETReactorSlayer is an open source (GPLv3) deobfuscator and unpacker for Eziriz .NET Reactor. |
| [nmap](../reference/network-analysis/nmap.md) | [`nmap`](../reference/network-analysis/nmap.md) | The Network Mapper. |
| notepadplusplus | `notepadplusplus` | Wrapper for Notepad++. |
| notepadpp.plugin.compare | `notepadpp.plugin.compare` | ComparePlus plugin for Notepad++. |
| notepadpp.plugin.jstool | `notepadpp.plugin.jstool` | A JavaScript (JSON) tool for Notepad++ (formerly JSMinNpp). |
| notepadpp.plugin.xmltools | `notepadpp.plugin.xmltools` | XML Tools plugin for Notepad++. |
| obfuscator-io-deobfuscator | `obfuscator-io-deobfuscator` | A deobfuscator for scripts obfuscated by Obfuscator.io. |
| [offvis](../reference/malware-triage-documents/OffVis-gui.md) | [`offvis`](../reference/malware-triage-documents/OffVis-gui.md) | The Microsoft Office Visualization Tool (OffVis) is a tool from Microsoft that helps understanding the Microsoft Of... |
| onenoteanalyzer | `onenoteanalyzer` | A C# based tool for analyzing malicious OneNote documents. |
| pdbresym | `pdbresym` | Download PDBs. |
| [pdfstreamdumper](../reference/malware-triage-documents/PDFStreamDumper-gui.md) | [`pdfstreamdumper`](../reference/malware-triage-documents/PDFStreamDumper-gui.md) | PDFStreamDumper is a free, open source tool to analyze malicious PDF documents. |
| pe_unmapper | `pe_unmapper` | Small tool to convert beteween the PE alignments (raw and virtual). |
| pebear | `pebear` | Delivers fast and flexible "first view" for malware analysts. |
| peid | `peid` | PEiD detects most common packers, cryptors and compilers for PE files. |
| pesieve | `pesieve` | Pe-sieve recognizes and dumps variety of implants within the scanned process. |
| pestudio | `pestudio` | The goal of pestudio is to spot artifacts of executable files in order to ease and accelerate Malware Initial Asses... |
| pkg-unpacker | `pkg-unpacker` | Unpacker for pkg applications. |
| pma-labs | `pma-labs` | Binaries for the book Practical Malware Analysis. |
| procdot | `procdot` | Creates visual graphs from procmon output. |
| processdump | `processdump` | Process Dump is a Windows reverse-engineering command-line tool to dump malware memory components back to disk for... |
| psnotify | `psnotify` | A POC tool to fight .NET anti-dumping tricks. |
| pycdas | `pycdas` | Python byte-code disassembler. |
| pycdc | `pycdc` | Python decompiler. |
| pylingual | `pylingual` | Python decompiler for modern Python versions. |
| rat-king-parser | `rat-king-parser` | Multi-family RAT config parser/extractor. |
| recaf | `recaf` | Java bytecode editor. |
| reg_export | `reg_export` | A CLI that exports the raw content of a registry value to a file. |
| regcool | `regcool` | In addition to all the features that you can find in RegEdit and RegEdt32, RegCool adds many powerful features that... |
| regshot | `regshot` | Regshot is a small, free and open-source registry compare utility that allows you to quickly take a snapshot of you... |
| resourcehacker | `resourcehacker` | Resource Hacker is a resource editor for 32bit and 64bit Windows applications. |
| rundotnetdll | `rundotnetdll` | A simple utility to list all methods of a given .NET Assembly and to invoke them. |
| scdbg | `scdbg` | Scdbg is an emulation based shellcode API logger and debugger. |
| sclauncher | `sclauncher` | A small program to load 32-bit shellcode and allow for execution or debugging. Can also output PE files from shellc... |
| sclauncher64 | `sclauncher64` | A small program to load 64-bit shellcode and allow for execution or debugging. Can also output PE files from shellc... |
| sfextract | `sfextract` | Command-line utility to extract files from single file bundles in .NET. |
| shellcode_launcher | `shellcode_launcher` | Shellcode launcher utility. |
| sysinternals | `sysinternals` | Sysinternals suite. |
| systeminformer | `systeminformer` | A free, powerful, multi-purpose tool that helps you monitor system resources, debug software and detect malware. |
| ttd | `ttd` | Time travel debugging command line utility. |
| uncompyle6 | `uncompyle6` | A decompiler for Python 1.0-3.8. |
| uniextract2 | `uniextract2` | Universal Extractor 2 is an unofficial updated and extended version of the original UniExtract by Jared Breland. |
| unpyc3 | `unpyc3` | A decompiler for Python 3.7+. |
| [upx](../reference/malware-triage-static/upx.md) | [`upx`](../reference/malware-triage-static/upx.md) | UPX is a free, secure, portable, extendable, high-performance executable packer for several executable formats. |
| vb-decompiler-lite | `vb-decompiler-lite` | VB Decompiler is a decompiler for Visual Basic, VB.NET and C# applications. |
| [vbdec](../reference/reverse-engineering/vbdec-gui.md) | [`vbdec`](../reference/reverse-engineering/vbdec-gui.md) | VBDec works as a VB6 disassembler, PCode debugger, structure viewer for all vb6 executables, and can generate IDA s... |
| vcbuildtools | `vcbuildtools` | Metapackage that requires the dependencies below: - visualstudio2017buildtools - visualstudio2017-workload-vctools. |
| vcredist-all | `vcredist-all` |  |
| vscode | `vscode` | VSCode is a modern, open-source code editor. |
| vscode.extension.jupyter | `vscode.extension.jupyter` | Jupyter notebook support, interactive programming and computing that supports Intellisense, debugging and more. |
| vscode.extension.python | `vscode.extension.python` | Python language support with extension access points for IntelliSense (Pylance), Debugging (Python Debugger), linti... |
| windbg | `windbg` | WinDbg is a debugger that can be used to analyze crash dumps, debug live user-mode and kernel-mode code, and examin... |
| windows-terminal | `windows-terminal` | Windows Terminal is a new, modern, feature-rich, productive terminal application for command-line users. |
| wireshark | `wireshark` | Network traffic analyzer - graphical interface. |
| x64dbg | `x64dbg` | An open-source x64/x32 debugger for Windows. |
| x64dbg.plugin.dbgchild | `x64dbg.plugin.dbgchild` | DbgChild is an x64dbg plugin to automatically attach to spawned child processes. |
| x64dbg.plugin.ollydumpex | `x64dbg.plugin.ollydumpex` | This plugin is process memory dumper for OllyDbg and Immunity Debugger. OllyDumpEx = OllyDump + PE Dumper - obsolet... |
| x64dbg.plugin.scyllahide | `x64dbg.plugin.scyllahide` | ScyllaHide is an advanced open-source x64/x86 user mode Anti-Anti-Debug library. |
| x64dbg.plugin.x64dbgpy | `x64dbg.plugin.x64dbgpy` | Automating x64dbg using Python. |
| [yara](../reference/malware-triage-static/yara.md) | [`yara`](../reference/malware-triage-static/yara.md) | Pattern matching swiss knife for malware researchers. |


## SIFT Workstation

### Forensic Packages

| Tool | Command(s) | Purpose |
|---|---|---|
| absent | `absent` |  |
| [aeskeyfind](../reference/memory-forensics/aeskeyfind.md) | [`aeskeyfind`](../reference/memory-forensics/aeskeyfind.md) | Tool for locating AES keys in a captured memory image. |
| afflib-tools | `afflib-tools` | Advanced Forensics Format Library (utilities). |
| aircrack-ng | `aircrack-ng` | Wireless WEP/WPA cracking utilities. |
| android-sdk-platform-tools | `android-sdk-platform-tools` | Tools for interacting with an Android platform. |
| [arp-scan](../reference/network-analysis/arp-scan.md) | [`arp-scan`](../reference/network-analysis/arp-scan.md) | Arp scanning and fingerprinting tool. |
| autopsy | `autopsy` | Graphical interface to SleuthKit. |
| avfs | `avfs` | Virtual filesystem to access archives, disk images, remote locations. |
| aws-cli | `aws-cli` |  |
| bless | `bless` | A full featured hexadecimal editor. |
| blt | `blt` | Graphics extension library for Tcl/Tk - run-time. |
| bulk-extractor | `bulk-extractor` |  |
| cabextract | `cabextract` | Microsoft Cabinet file unpacker. |
| ccrypt | `ccrypt` | Secure encryption and decryption of files and streams. |
| chromium-browser | `chromium-browser` | Transitional package - chromium-browser -> chromium snap. |
| clamav | `clamav` | Anti-virus utility for Unix - command-line interface. |
| claude-code | `claude-code` |  |
| cmospwd | `cmospwd` | Decrypt BIOS passwords from CMOS. |
| cryptcat | `cryptcat` | Lightweight version netcat extended with twofish encryption. |
| cryptsetup | `cryptsetup` | Disk encryption support - startup scripts. |
| [dc3dd](../reference/acquire-preserve/dc3dd.md) | [`dc3dd`](../reference/acquire-preserve/dc3dd.md) | Patched version of GNU dd with forensic features. |
| [dcfldd](../reference/acquire-preserve/dcfldd.md) | [`dcfldd`](../reference/acquire-preserve/dcfldd.md) | Enhanced version of dd for forensics and security. |
| default-jre | `default-jre` | Standard Java or Java compatible Runtime. |
| disktype | `disktype` | Detection of content format of a disk or disk image. |
| dislocker | `dislocker` | Read/write encrypted BitLocker volumes. |
| docker | `docker` | Transitional package. |
| dos2unix | `dos2unix` | Convert text file line endings between CRLF and LF. |
| dotnet | `dotnet` |  |
| driftnet | `driftnet` | Picks out and displays images from network traffic. |
| dsniff | `dsniff` | Various tools to sniff network traffic for cleartext insecurities. |
| e2fsprogs | `e2fsprogs` | Ext2/ext3/ext4 file system utilities. |
| ent | `ent` | Pseudorandom number sequence test program. |
| epic5 | `epic5` | Epic irc client, version 5. |
| etherape | `etherape` | Graphical network monitor. |
| ettercap-graphical | `ettercap-graphical` | Ettercap GUI-enabled executable. |
| ewf-tools | `ewf-tools` | Collection of tools for reading and writing EWF files. |
| exfat-extras | `exfat-extras` |  |
| exfat-fuse | `exfat-fuse` | Read and write exFAT driver for FUSE. |
| exif | `exif` | Command-line utility to show EXIF information in JPEG files. |
| extundelete | `extundelete` | Utility to recover deleted files from ext3/ext4 partition. |
| fdupes | `fdupes` | Identifies duplicate files within given directories. |
| feh | `feh` | Imlib2 based image viewer. |
| [file](../reference/examine-the-filesystem/file.md) | [`file`](../reference/examine-the-filesystem/file.md) | Recognize the type of data in a file using "magic" numbers. |
| flex | `flex` | Fast lexical analyzer generator. |
| [foremost](../reference/examine-the-filesystem/foremost.md) | [`foremost`](../reference/examine-the-filesystem/foremost.md) | Forensic program to recover lost files. |
| gawk | `gawk` | GNU awk, a pattern scanning and processing language. |
| gdb | `gdb` | GNU Debugger. |
| gddrescue | `gddrescue` | GNU data recovery tool. |
| ghex | `ghex` | GNOME Hex editor for files. |
| graphviz | `graphviz` | Rich set of graph drawing tools. |
| grepcidr | `grepcidr` | Filter IP addresses matching IPv4/IPv6 CIDR/network specification. |
| gthumb | `gthumb` | Image viewer and browser. |
| gzrt | `gzrt` | Gzip recovery toolkit. |
| hashdeep | `hashdeep` | Recursively compute hashsums or piecewise hashings. |
| hexedit | `hexedit` | Viewer and editor in hexadecimal or ASCII for files or devices. |
| [hydra](../reference/decode-deobfuscate/hydra.md) | [`hydra`](../reference/decode-deobfuscate/hydra.md) | Very fast network logon cracker. |
| hydra-gtk | `hydra-gtk` | Very fast network logon cracker - GTK+ based GUI. |
| init | `init` | Metapackage ensuring an init system is installed. |
| ipython3 | `ipython3` | Enhanced interactive Python 3 shell. |
| jq | `jq` | Lightweight and flexible command-line JSON processor. |
| kdiff3 | `kdiff3` | Compares and merges 2 or 3 files or directories. |
| kpartx | `kpartx` | Create device mappings for partitions. |
| lft | `lft` | Layer-four traceroute. |
| lvm2 | `lvm2` | Linux Logical Volume Manager. |
| magnus | `magnus` | Very simple screen magnifier. |
| mdadm | `mdadm` | Tool for managing Linux MD devices (software RAID). |
| mtd-utils | `mtd-utils` | Memory Technology Device Utilities. |
| nbd-client | `nbd-client` | Network Block Device protocol - client. |
| nbtscan | `nbtscan` | Scan networks searching for NetBIOS information. |
| netcat | `netcat` | TCP/IP swiss army knife -- transitional package. |
| netpbm | `netpbm` | Graphics conversion tools between image formats. |
| netsed | `netsed` | Network packet-altering stream editor. |
| netwox | `netwox` | Networking utilities. |
| nfdump | `nfdump` | Netflow capture daemon. |
| [ngrep](../reference/network-analysis/ngrep.md) | [`ngrep`](../reference/network-analysis/ngrep.md) | Grep for network traffic. |
| nikto | `nikto` |  |
| [ntfs-3g](../reference/acquire-preserve/ntfs-3g.md) | [`ntfs-3g`](../reference/acquire-preserve/ntfs-3g.md) | Read/write NTFS driver for FUSE. |
| okular | `okular` | Universal document viewer. |
| onboard | `onboard` | Simple On-screen Keyboard. |
| open-iscsi | `open-iscsi` | ISCSI initiator tools. |
| openjdk | `openjdk` | Metapackage for OpenJDK to ensure all packages use the same OpenJDK version. |
| ophcrack | `ophcrack` | Microsoft Windows password cracker using rainbow tables (gui). |
| ophcrack-cli | `ophcrack-cli` | Microsoft Windows password cracker using rainbow tables (cmdline). |
| orca | `orca` | Scriptable screen reader. |
| outguess | `outguess` | Universal steganographic tool. |
| p0f | `p0f` | Passive OS fingerprinting tool. |
| p7zip-full | `p7zip-full` | 7z and 7za file archivers with high compression ratio. |
| patch | `patch` | Apply a diff file to an original. |
| pdftk-java | `pdftk-java` | Pdftk port to java - a tool for manipulating PDF documents. |
| perl | `perl` | Larry Wall's Practical Extraction and Report Language. |
| pev | `pev` | Text-based tool to analyze PE files. |
| pff-tools | `pff-tools` | Utilities for MS Outlook PAB, PST and OST files. |
| phonon | `phonon` |  |
| pkg-config | `pkg-config` | Manage compile and link flags for libraries (transitional package). |
| plaso-tools | `plaso-tools` |  |
| powershell | `powershell` | PowerShell is an automation and configuration management platform. |
| pst-utils | `pst-utils` | Tools for reading Microsoft Outlook PST files. |
| pv | `pv` | Shell pipeline element to meter data passing through. |
| python-flowgrep | `python-flowgrep` |  |
| python3-debian | `python3-debian` | Python 3 modules to work with Debian-related data formats. |
| python3-dfvfs | `python3-dfvfs` | Digital Forensics Virtual File System. |
| python3-fuse | `python3-fuse` | Python bindings for FUSE (Filesystems in USErspace) (Python 3 package). |
| python3-keyrings-alt | `python3-keyrings-alt` |  |
| python3-m2crypto | `python3-m2crypto` | Python wrapper for the OpenSSL library (Python 3 modules). |
| python3-magic | `python3-magic` | Python3 interface to the libmagic file type identification library. |
| python3-pefile | `python3-pefile` | Portable Executable (PE) parsing module for Python. |
| python3-plaso | `python3-plaso` | Super timeline all the things -- Python 3. |
| python3-pypff | `python3-pypff` | Python 3 bindings for libpff. |
| python3-pyqt5 | `python3-pyqt5` | Python 3 bindings for Qt5. |
| python3-pytsk3 | `python3-pytsk3` |  |
| python3-redis | `python3-redis` | Python bindings for Redis, a persistent key-value database. |
| python3-setuptools-rust | `python3-setuptools-rust` | Setuptools Rust extension plugin. |
| python3-tk | `python3-tk` | Tkinter - Writing Tk applications with Python 3.x. |
| python3-tsk | `python3-tsk` | Python Bindings for The Sleuth Kit. |
| python3-virtualenv | `python3-virtualenv` | Python virtual environment creator. |
| python3-wxgtk4 | `python3-wxgtk4` |  |
| python3-xlsxwriter | `python3-xlsxwriter` | Python 3 module for creating Excel XLSX files. |
| python3-yara | `python3-yara` | Python 3 bindings for YARA. |
| qemu | `qemu` | Fast processor emulator, dummy package. |
| qemu-utils | `qemu-utils` | QEMU utilities. |
| radare2 | `radare2` | Free and advanced command line hexadecimal editor. |
| rar | `rar` |  |
| [rsakeyfind](../reference/memory-forensics/rsakeyfind.md) | [`rsakeyfind`](../reference/memory-forensics/rsakeyfind.md) | Locates BER-encoded RSA private keys in memory images. |
| safecopy | `safecopy` | Data recovery tool for problematic or damaged media. |
| samdump2 | `samdump2` | Dump Windows 2k/NT/XP password hashes. |
| [scalpel](../reference/examine-the-filesystem/scalpel.md) | [`scalpel`](../reference/examine-the-filesystem/scalpel.md) | Fast filesystem-independent file recovery. |
| silversearcher-ag | `silversearcher-ag` | Very fast grep-like program, alternative to ack. |
| sleuthkit | `sleuthkit` | Tools for forensics analysis on volume and filesystem data. |
| socat | `socat` | Multipurpose relay for bidirectional data transfer. |
| squashfs-tools | `squashfs-tools` | Tool to create and append to squashfs filesystems. |
| [ssdeep](../reference/acquire-preserve/ssdeep.md) | [`ssdeep`](../reference/acquire-preserve/ssdeep.md) | Recursive piecewise hashing tool. |
| ssldump | `ssldump` | SSLv3/TLS network protocol analyzer. |
| sslsniff | `sslsniff` | SSL/TLS man-in-the-middle attack tool. |
| stunnel4 | `stunnel4` | Universal SSL tunnnel for network daemons - compatibility package. |
| swig | `swig` | Generate scripting interfaces to C/C++ code. |
| tcl | `tcl` | Tool Command Language (default version) - shell. |
| [tcpflow](../reference/network-analysis/tcpflow.md) | [`tcpflow`](../reference/network-analysis/tcpflow.md) | TCP flow recorder. |
| tcpick | `tcpick` | TCP stream sniffer and connection tracker. |
| tcpreplay | `tcpreplay` | Tool to replay saved tcpdump files at arbitrary speeds. |
| tcpslice | `tcpslice` | Extract pieces of and/or glue together tcpdump files. |
| tcpstat | `tcpstat` | Network interface statistics reporting tool. |
| tcptrace | `tcptrace` | Tool for analyzing tcpdump output. |
| tcptrack | `tcptrack` | TCP connection tracker, with states and speeds. |
| [tcpxtract](../reference/examine-the-filesystem/tcpxtract.md) | [`tcpxtract`](../reference/examine-the-filesystem/tcpxtract.md) | Extract files from network traffic based on file signatures. |
| [testdisk](../reference/examine-the-filesystem/testdisk.md) | [`testdisk`](../reference/examine-the-filesystem/testdisk.md) | Partition scanner and disk recovery tool, and PhotoRec file recovery tool. |
| tofrodos | `tofrodos` | Converts DOS <-> Unix text files, alias tofromdos. |
| transmission | `transmission` | Lightweight BitTorrent client. |
| ugrep | `ugrep` | Faster grep with an interactive query UI. |
| unity-control-center | `unity-control-center` | Utilities to configure the GNOME desktop. |
| unrar | `unrar` |  |
| upx-ucl | `upx-ucl` | Efficient live-compressor for executables. |
| vbindiff | `vbindiff` | Visual binary diff, visually compare binary files. |
| virtuoso-minimal | `virtuoso-minimal` | High-performance database - core dependency package. |
| vmfs-tools | `vmfs-tools` | Tools to access VMFS filesystems. |
| winbind | `winbind` | Service to resolve user and group information from Windows NT servers. |
| wine | `wine` | Windows API implementation - standard suite. |
| wireshark | `wireshark` | Network traffic analyzer - graphical interface. |
| xdot | `xdot` | Interactive viewer for Graphviz dot files. |
| xfsprogs | `xfsprogs` | Utilities for managing the XFS filesystem. |
| xmount | `xmount` | Tool for crossmounting between disk image formats. |
| zenity | `zenity` | Display graphical dialog boxes from shell scripts. |
| zlib1g-dev | `zlib1g-dev` | Compression library - development. |


## Security Onion

### DB/Search

| Tool | Command(s) | Purpose |
|---|---|---|
| Elasticsearch | — | NoSQL index for logs/metadata/alerts |
| ILM | — | Index Lifecycle Management (aging/rolling/deletion) |
| Kibana | — | Search analytics & dashboards |

### Detection

| Tool | Command(s) | Purpose |
|---|---|---|
| ATT&CK Navigator | — | Visual defensive-coverage matrix |
| ElastAlert 2 | — | Continuous alert-indicator scanner |
| Playbook | — | Custom detections mapped to MITRE ATT&CK |
| Sigma / Sigma-CLI | — | Translate YAML detection rules to Elastic queries |
| so-idstools | — | Manage/update Suricata ET rules |

### Diagnostics

| Tool | Command(s) | Purpose |
|---|---|---|
| Grafana | — | Infra/node-health dashboards |
| InfluxDB | — | Time-series store for hardware metrics |
| Telegraf | — | Hardware health/CPU/mem/disk agent |

### File Analysis

| Tool | Command(s) | Purpose |
|---|---|---|
| DomainStats | — | Domain-age checks to flag malicious sites |
| FreqServer | — | Entropy analysis to detect DGAs |
| Strelka | — | Real-time file extraction & YARA/file carving |

### Host/EDR

| Tool | Command(s) | Purpose |
|---|---|---|
| Elastic Agent | — | Host log/metric/audit collector |
| Elastic Fleet | — | Central agent config & deployment |
| OpenCanary | — | Network honeypot / decoy services |
| Osquery | — | Live endpoint queries via SQL |
| Wazuh | — | HIDS - File Integrity Monitoring & rootkit checks |

### IR/AI

| Tool | Command(s) | Purpose |
|---|---|---|
| [CyberChef](../reference/decode-deobfuscate/cyberchef.md) | — | Visual data decode/parse/analysis |
| Onion AI Assistant | — | AI triage assistance for analysts |
| Security Onion Console (SOC) | — | Web UI for threat hunting & grid management |
| TheHive | — | Collaborative IR & case management |

### Identity/Infra

| Tool | Command(s) | Purpose |
|---|---|---|
| ManagerHype | — | Hypervisor integration for VM mapping |
| Nginx (so-nginx) | — | Reverse proxy for internal web traffic |
| Ory Kratos & Dex | — | IAM - SSO/auth/sessions |
| so-apt-cacher-ng | — | Local package caching proxy |
| so-firewall | — | iptables/nftables wrapper for inter-node comms |

### Log Routing

| Tool | Command(s) | Purpose |
|---|---|---|
| Filebeat | — | Lightweight log shipper |
| Logstash | — | Data pipeline - ECS normalize & enrich |
| Redis | — | Log ingestion queue/broker |
| Rsyslog / Syslog-ng | — | Ingest traditional syslog from appliances |

### Network Visibility

| Tool | Command(s) | Purpose |
|---|---|---|
| Sensoroni | — | Backend API agent retrieving/extracting PCAPs |
| Stenographer | — | High-speed raw full packet capture daemon |
| Suricata | — | Signature-based IDS/IPS & packet capture |
| Zeek | — | Network traffic analyzer & protocol metadata logging |


## Sources

- `remnux_docs` — https://raw.githubusercontent.com/REMnux/docs/master/discover-the-tools
- `kali_control` — https://gitlab.com/kalilinux/packages/kali-meta/-/raw/kali/master/debian/control
- `flare_config` — https://raw.githubusercontent.com/mandiant/flare-vm/main/config.xml
