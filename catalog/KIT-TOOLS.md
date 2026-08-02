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
| [cURL](../reference/report-support/curl.md) | [`curl`](../reference/report-support/curl.md) | Interact with servers via supported protocols, including HTTP, HTTPS, FTP, IMAP, etc. using this command-line tool. |
| EPIC IRC Client | `epic5` | Examine IRC activities with this IRC client. |
| GNU Wget | [`wget`](../reference/report-support/wget.md) | Interact with servers via HTTP, HTTPS, FTP, and FTPS using this command-line tool. |
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
| [cURL](../reference/report-support/curl.md) | [`curl`](../reference/report-support/curl.md) | Interact with servers via supported protocols, including HTTP, HTTPS, FTP, IMAP, etc. using this command-line tool. |
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
| aesfix | `aesfix` |  |
| [aeskeyfind](../reference/memory-forensics/aeskeyfind.md) | [`aeskeyfind`](../reference/memory-forensics/aeskeyfind.md) |  |
| ccrypt | `ccrypt` |  |
| steghide | `steghide` |  |
| stegosuite | `stegosuite` |  |
| stegsnow | `stegsnow` |  |

### Database

| Tool | Command(s) | Purpose |
|---|---|---|
| jsql-injection | `jsql-injection` |  |
| mdbtools | `mdbtools` |  |
| oscanner | `oscanner` |  |
| sidguesser | `sidguesser` |  |
| sqldict | `sqldict` |  |
| sqlitebrowser | `sqlitebrowser` |  |
| sqlmap | `sqlmap` |  |
| sqlninja | `sqlninja` |  |
| sqlsus | `sqlsus` |  |
| tnscmd10g | `tnscmd10g` |  |

### Exploitation

| Tool | Command(s) | Purpose |
|---|---|---|
| armitage | `armitage` |  |
| beef-xss | `beef-xss` |  |
| exploitdb | `exploitdb` |  |
| metasploit-framework | `metasploit-framework` |  |
| msfpc | `msfpc` |  |
| set | `set` |  |
| shellnoob | `shellnoob` |  |
| sqlmap | `sqlmap` |  |
| termineter | `termineter` |  |

### Forensics

| Tool | Command(s) | Purpose |
|---|---|---|
| 7zip | `7zip` |  |
| afflib-tools | `afflib-tools` |  |
| apktool | `apktool` |  |
| autopsy | `autopsy` |  |
| [binwalk](../reference/examine-the-filesystem/binwalk.md) | [`binwalk`](../reference/examine-the-filesystem/binwalk.md) |  |
| binwalk3 | `binwalk3` |  |
| bulk-extractor | `bulk-extractor` |  |
| bytecode-viewer | `bytecode-viewer` |  |
| cabextract | `cabextract` |  |
| chkrootkit | `chkrootkit` |  |
| creddump7 | `creddump7` |  |
| [dc3dd](../reference/acquire-preserve/dc3dd.md) | [`dc3dd`](../reference/acquire-preserve/dc3dd.md) |  |
| [dcfldd](../reference/acquire-preserve/dcfldd.md) | [`dcfldd`](../reference/acquire-preserve/dcfldd.md) |  |
| ddrescue | `ddrescue` |  |
| dumpzilla | `dumpzilla` |  |
| edb-debugger | `edb-debugger` |  |
| ewf-tools | `ewf-tools` |  |
| exifprobe | `exifprobe` |  |
| exiv2 | `exiv2` |  |
| ext3grep | `ext3grep` |  |
| ext4magic | `ext4magic` |  |
| extundelete | `extundelete` |  |
| fcrackzip | `fcrackzip` |  |
| firmware-mod-kit | `firmware-mod-kit` |  |
| [foremost](../reference/examine-the-filesystem/foremost.md) | [`foremost`](../reference/examine-the-filesystem/foremost.md) |  |
| forensic-artifacts | `forensic-artifacts` |  |
| forensics-colorize | `forensics-colorize` |  |
| galleta | `galleta` |  |
| gdb | `gdb` |  |
| gpart | `gpart` |  |
| gparted | `gparted` |  |
| grokevt | `grokevt` |  |
| guymager | `guymager` |  |
| hashdeep | `hashdeep` |  |
| [inetsim](../reference/network-analysis/inetsim.md) | [`inetsim`](../reference/network-analysis/inetsim.md) |  |
| jadx | `jadx` |  |
| javasnoop | `javasnoop` |  |
| libhivex-bin | `libhivex-bin` |  |
| libsmali-java | `libsmali-java` |  |
| lvm2 | `lvm2` |  |
| lynis | `lynis` |  |
| mac-robber | `mac-robber` |  |
| magicrescue | `magicrescue` |  |
| md5deep | `md5deep` |  |
| mdbtools | `mdbtools` |  |
| memdump | `memdump` |  |
| metacam | `metacam` |  |
| missidentify | `missidentify` |  |
| myrescue | `myrescue` |  |
| nasm | `nasm` |  |
| nasty | `nasty` |  |
| ollydbg | `ollydbg` |  |
| parted | `parted` |  |
| pasco | `pasco` |  |
| [pdf-parser](../reference/malware-triage-documents/pdf-parser.md) | [`pdf-parser`](../reference/malware-triage-documents/pdf-parser.md) |  |
| [pdfid](../reference/malware-triage-documents/pdfid.md) | [`pdfid`](../reference/malware-triage-documents/pdfid.md) |  |
| plaso | `plaso` |  |
| polenum | `polenum` |  |
| pst-utils | `pst-utils` |  |
| python3-capstone | `python3-capstone` |  |
| python3-dfdatetime | `python3-dfdatetime` |  |
| python3-dfvfs | `python3-dfvfs` |  |
| python3-dfwinreg | `python3-dfwinreg` |  |
| python3-distorm3 | `python3-distorm3` |  |
| radare2 | `radare2` |  |
| readpe | `readpe` |  |
| recoverdm | `recoverdm` |  |
| recoverjpeg | `recoverjpeg` |  |
| recstudio | `recstudio` |  |
| reglookup | `reglookup` |  |
| [regripper](../reference/windows-artifacts/regripper.md) | [`regripper`](../reference/windows-artifacts/regripper.md) |  |
| rephrase | `rephrase` |  |
| rifiuti | `rifiuti` |  |
| rifiuti2 | `rifiuti2` |  |
| rizin-cutter | `rizin-cutter` |  |
| rkhunter | `rkhunter` |  |
| [rsakeyfind](../reference/memory-forensics/rsakeyfind.md) | [`rsakeyfind`](../reference/memory-forensics/rsakeyfind.md) |  |
| rz-ghidra | `rz-ghidra` |  |
| safecopy | `safecopy` |  |
| samdump2 | `samdump2` |  |
| [scalpel](../reference/examine-the-filesystem/scalpel.md) | [`scalpel`](../reference/examine-the-filesystem/scalpel.md) |  |
| scrounge-ntfs | `scrounge-ntfs` |  |
| sleuthkit | `sleuthkit` |  |
| sqlitebrowser | `sqlitebrowser` |  |
| [ssdeep](../reference/acquire-preserve/ssdeep.md) | [`ssdeep`](../reference/acquire-preserve/ssdeep.md) |  |
| tcpdump | `tcpdump` |  |
| [tcpflow](../reference/network-analysis/tcpflow.md) | [`tcpflow`](../reference/network-analysis/tcpflow.md) |  |
| tcpick | `tcpick` |  |
| tcpreplay | `tcpreplay` |  |
| truecrack | `truecrack` |  |
| undbx | `undbx` |  |
| unhide | `unhide` |  |
| unrar | `unrar` |  |
| upx-ucl | `upx-ucl` |  |
| vinetto | `vinetto` |  |
| wce | `wce` |  |
| winregfs | `winregfs` |  |
| wireshark | `wireshark` |  |
| xmount | `xmount` |  |
| xplico | `xplico` |  |
| [yara](../reference/malware-triage-static/yara.md) | [`yara`](../reference/malware-triage-static/yara.md) |  |

### Fuzzing

| Tool | Command(s) | Purpose |
|---|---|---|
| afl++ | `afl++` |  |
| sfuzz | `sfuzz` |  |
| spike | `spike` |  |
| wfuzz | `wfuzz` |  |

### Information Gathering

| Tool | Command(s) | Purpose |
|---|---|---|
| 0trace | `0trace` |  |
| arping | `arping` |  |
| braa | `braa` |  |
| dmitry | `dmitry` |  |
| dnsenum | `dnsenum` |  |
| dnsmap | `dnsmap` |  |
| dnsrecon | `dnsrecon` |  |
| dnstracer | `dnstracer` |  |
| dnswalk | `dnswalk` |  |
| enum4linux | `enum4linux` |  |
| fierce | `fierce` |  |
| firewalk | `firewalk` |  |
| fping | `fping` |  |
| fragrouter | `fragrouter` |  |
| ftester | `ftester` |  |
| hping3 | `hping3` |  |
| ike-scan | `ike-scan` |  |
| intrace | `intrace` |  |
| irpas | `irpas` |  |
| lbd | `lbd` |  |
| legion | `legion` |  |
| maltego | `maltego` |  |
| masscan | `masscan` |  |
| metagoofil | `metagoofil` |  |
| nbtscan | `nbtscan` |  |
| ncat | `ncat` |  |
| netdiscover | `netdiscover` |  |
| netmask | `netmask` |  |
| [nmap](../reference/network-analysis/nmap.md) | [`nmap`](../reference/network-analysis/nmap.md) |  |
| onesixtyone | `onesixtyone` |  |
| p0f | `p0f` |  |
| qsslcaudit | `qsslcaudit` |  |
| recon-ng | `recon-ng` |  |
| smbmap | `smbmap` |  |
| smtp-user-enum | `smtp-user-enum` |  |
| snmpcheck | `snmpcheck` |  |
| ssldump | `ssldump` |  |
| sslh | `sslh` |  |
| sslscan | `sslscan` |  |
| sslyze | `sslyze` |  |
| swaks | `swaks` |  |
| thc-ipv6 | `thc-ipv6` |  |
| theharvester | `theharvester` |  |
| tlssled | `tlssled` |  |
| twofi | `twofi` |  |
| unicornscan | `unicornscan` |  |
| urlcrazy | `urlcrazy` |  |
| wafw00f | `wafw00f` |  |
| zenmap | `zenmap` |  |

### Passwords

| Tool | Command(s) | Purpose |
|---|---|---|
| cewl | `cewl` |  |
| chntpw | `chntpw` |  |
| cisco-auditing-tool | `cisco-auditing-tool` |  |
| cmospwd | `cmospwd` |  |
| crackle | `crackle` |  |
| creddump7 | `creddump7` |  |
| crunch | `crunch` |  |
| fcrackzip | `fcrackzip` |  |
| freerdp3-x11 | `freerdp3-x11` |  |
| gpp-decrypt | `gpp-decrypt` |  |
| hash-identifier | `hash-identifier` |  |
| [hashcat](../reference/decode-deobfuscate/hashcat.md) | [`hashcat`](../reference/decode-deobfuscate/hashcat.md) |  |
| hashcat-utils | `hashcat-utils` |  |
| hashid | `hashid` |  |
| [hydra](../reference/decode-deobfuscate/hydra.md) | [`hydra`](../reference/decode-deobfuscate/hydra.md) |  |
| hydra-gtk | `hydra-gtk` |  |
| [john](../reference/decode-deobfuscate/john.md) | [`john`](../reference/decode-deobfuscate/john.md) |  |
| johnny | `johnny` |  |
| maskprocessor | `maskprocessor` |  |
| medusa | `medusa` |  |
| mimikatz | `mimikatz` |  |
| ncrack | `ncrack` |  |
| onesixtyone | `onesixtyone` |  |
| ophcrack | `ophcrack` |  |
| ophcrack-cli | `ophcrack-cli` |  |
| pack | `pack` |  |
| pack2 | `pack2` |  |
| passing-the-hash | `passing-the-hash` |  |
| patator | `patator` |  |
| pdfcrack | `pdfcrack` |  |
| pipal | `pipal` |  |
| polenum | `polenum` |  |
| rainbowcrack | `rainbowcrack` |  |
| rarcrack | `rarcrack` |  |
| rcracki-mt | `rcracki-mt` |  |
| rsmangler | `rsmangler` |  |
| samdump2 | `samdump2` |  |
| seclists | `seclists` |  |
| sipcrack | `sipcrack` |  |
| sipvicious | `sipvicious` |  |
| smbmap | `smbmap` |  |
| sqldict | `sqldict` |  |
| statsprocessor | `statsprocessor` |  |
| sucrack | `sucrack` |  |
| thc-pptp-bruter | `thc-pptp-bruter` |  |
| truecrack | `truecrack` |  |
| twofi | `twofi` |  |
| wordlists | `wordlists` |  |

### Post Exploitation

| Tool | Command(s) | Purpose |
|---|---|---|
| cymothoa | `cymothoa` |  |
| dbd | `dbd` |  |
| dns2tcp | `dns2tcp` |  |
| exe2hexbat | `exe2hexbat` |  |
| iodine | `iodine` |  |
| laudanum | `laudanum` |  |
| mimikatz | `mimikatz` |  |
| miredo | `miredo` |  |
| nishang | `nishang` |  |
| powersploit | `powersploit` |  |
| proxychains4 | `proxychains4` |  |
| proxytunnel | `proxytunnel` |  |
| ptunnel | `ptunnel` |  |
| pwnat | `pwnat` |  |
| sbd | `sbd` |  |
| shellter | `shellter` |  |
| sslh | `sslh` |  |
| stunnel4 | `stunnel4` |  |
| udptunnel | `udptunnel` |  |
| veil | `veil` |  |
| webacoo | `webacoo` |  |
| weevely | `weevely` |  |

### Reverse Engineering

| Tool | Command(s) | Purpose |
|---|---|---|
| apktool | `apktool` |  |
| bytecode-viewer | `bytecode-viewer` |  |
| clang | `clang` |  |
| dex2jar | `dex2jar` |  |
| edb-debugger | `edb-debugger` |  |
| jadx | `jadx` |  |
| javasnoop | `javasnoop` |  |
| jd-gui | `jd-gui` |  |
| metasploit-framework | `metasploit-framework` |  |
| ollydbg | `ollydbg` |  |
| radare2 | `radare2` |  |
| recstudio | `recstudio` |  |
| rizin | `rizin` |  |
| rizin-cutter | `rizin-cutter` |  |
| rz-ghidra | `rz-ghidra` |  |

### Sniffing Spoofing

| Tool | Command(s) | Purpose |
|---|---|---|
| above | `above` |  |
| bettercap | `bettercap` |  |
| darkstat | `darkstat` |  |
| dnschef | `dnschef` |  |
| driftnet | `driftnet` |  |
| dsniff | `dsniff` |  |
| ettercap-graphical | `ettercap-graphical` |  |
| ferret-sidejack | `ferret-sidejack` |  |
| fiked | `fiked` |  |
| hamster-sidejack | `hamster-sidejack` |  |
| hexinject | `hexinject` |  |
| isr-evilgrade | `isr-evilgrade` |  |
| macchanger | `macchanger` |  |
| mitmproxy | `mitmproxy` |  |
| netsniff-ng | `netsniff-ng` |  |
| rebind | `rebind` |  |
| responder | `responder` |  |
| sniffjoke | `sniffjoke` |  |
| sslsniff | `sslsniff` |  |
| sslsplit | `sslsplit` |  |
| [tcpflow](../reference/network-analysis/tcpflow.md) | [`tcpflow`](../reference/network-analysis/tcpflow.md) |  |
| tcpreplay | `tcpreplay` |  |
| wifi-honey | `wifi-honey` |  |
| wireshark | `wireshark` |  |

### Vulnerability

| Tool | Command(s) | Purpose |
|---|---|---|
| afl++ | `afl++` |  |
| bed | `bed` |  |
| cisco-auditing-tool | `cisco-auditing-tool` |  |
| cisco-global-exploiter | `cisco-global-exploiter` |  |
| cisco-ocs | `cisco-ocs` |  |
| cisco-torch | `cisco-torch` |  |
| copy-router-config | `copy-router-config` |  |
| dhcpig | `dhcpig` |  |
| enumiax | `enumiax` |  |
| gvm | `gvm` |  |
| iaxflood | `iaxflood` |  |
| inviteflood | `inviteflood` |  |
| legion | `legion` |  |
| lynis | `lynis` |  |
| nikto | `nikto` |  |
| [nmap](../reference/network-analysis/nmap.md) | [`nmap`](../reference/network-analysis/nmap.md) |  |
| ohrwurm | `ohrwurm` |  |
| peass | `peass` |  |
| protos-sip | `protos-sip` |  |
| rtpbreak | `rtpbreak` |  |
| rtpflood | `rtpflood` |  |
| rtpinsertsound | `rtpinsertsound` |  |
| rtpmixsound | `rtpmixsound` |  |
| sctpscan | `sctpscan` |  |
| sfuzz | `sfuzz` |  |
| siege | `siege` |  |
| siparmyknife | `siparmyknife` |  |
| sipp | `sipp` |  |
| sipsak | `sipsak` |  |
| sipvicious | `sipvicious` |  |
| slowhttptest | `slowhttptest` |  |
| spike | `spike` |  |
| t50 | `t50` |  |
| thc-ssl-dos | `thc-ssl-dos` |  |
| unix-privesc-check | `unix-privesc-check` |  |
| voiphopper | `voiphopper` |  |
| yersinia | `yersinia` |  |

### Web

| Tool | Command(s) | Purpose |
|---|---|---|
| apache-users | `apache-users` |  |
| apache2 | `apache2` |  |
| beef-xss | `beef-xss` |  |
| burpsuite | `burpsuite` |  |
| cadaver | `cadaver` |  |
| commix | `commix` |  |
| cutycapt | `cutycapt` |  |
| davtest | `davtest` |  |
| default-mysql-server | `default-mysql-server` |  |
| dirb | `dirb` |  |
| dirbuster | `dirbuster` |  |
| dotdotpwn | `dotdotpwn` |  |
| eyewitness | `eyewitness` |  |
| ferret-sidejack | `ferret-sidejack` |  |
| ftester | `ftester` |  |
| hakrawler | `hakrawler` |  |
| hamster-sidejack | `hamster-sidejack` |  |
| heartleech | `heartleech` |  |
| httprint | `httprint` |  |
| httrack | `httrack` |  |
| [hydra](../reference/decode-deobfuscate/hydra.md) | [`hydra`](../reference/decode-deobfuscate/hydra.md) |  |
| hydra-gtk | `hydra-gtk` |  |
| jboss-autopwn | `jboss-autopwn` |  |
| joomscan | `joomscan` |  |
| jsql-injection | `jsql-injection` |  |
| laudanum | `laudanum` |  |
| lbd | `lbd` |  |
| maltego | `maltego` |  |
| medusa | `medusa` |  |
| mitmproxy | `mitmproxy` |  |
| ncrack | `ncrack` |  |
| nikto | `nikto` |  |
| nishang | `nishang` |  |
| [nmap](../reference/network-analysis/nmap.md) | [`nmap`](../reference/network-analysis/nmap.md) |  |
| oscanner | `oscanner` |  |
| owasp-mantra-ff | `owasp-mantra-ff` |  |
| padbuster | `padbuster` |  |
| paros | `paros` |  |
| patator | `patator` |  |
| php | `php` |  |
| php-mysql | `php-mysql` |  |
| proxychains4 | `proxychains4` |  |
| proxytunnel | `proxytunnel` |  |
| qsslcaudit | `qsslcaudit` |  |
| redsocks | `redsocks` |  |
| sidguesser | `sidguesser` |  |
| siege | `siege` |  |
| skipfish | `skipfish` |  |
| slowhttptest | `slowhttptest` |  |
| sqldict | `sqldict` |  |
| sqlitebrowser | `sqlitebrowser` |  |
| sqlmap | `sqlmap` |  |
| sqlninja | `sqlninja` |  |
| sqlsus | `sqlsus` |  |
| ssldump | `ssldump` |  |
| sslh | `sslh` |  |
| sslscan | `sslscan` |  |
| sslsniff | `sslsniff` |  |
| sslsplit | `sslsplit` |  |
| sslyze | `sslyze` |  |
| stunnel4 | `stunnel4` |  |
| thc-ssl-dos | `thc-ssl-dos` |  |
| tlssled | `tlssled` |  |
| tnscmd10g | `tnscmd10g` |  |
| uniscan | `uniscan` |  |
| wafw00f | `wafw00f` |  |
| wapiti | `wapiti` |  |
| watobo | `watobo` |  |
| webacoo | `webacoo` |  |
| webscarab | `webscarab` |  |
| webshells | `webshells` |  |
| weevely | `weevely` |  |
| wfuzz | `wfuzz` |  |
| whatweb | `whatweb` |  |
| wireshark | `wireshark` |  |
| wpscan | `wpscan` |  |
| xsser | `xsser` |  |
| zaproxy | `zaproxy` |  |


## FLARE-VM

### All Packages (choco)

| Tool | Command(s) | Purpose |
|---|---|---|
| 010editor | `010editor` |  |
| 7zip | `7zip` |  |
| advanced-installer | `advanced-installer` |  |
| angr | `angr` |  |
| apimonitor | `apimonitor` |  |
| apktool | `apktool` |  |
| asar | `asar` |  |
| autoit-ripper | `autoit-ripper` |  |
| binaryninja | `binaryninja` |  |
| bindiff | `bindiff` |  |
| blobrunner | `blobrunner` |  |
| blobrunner64 | `blobrunner64` |  |
| bytecodeviewer | `bytecodeviewer` |  |
| [capa](../reference/malware-triage-static/capa.md) | [`capa`](../reference/malware-triage-static/capa.md) |  |
| capa-explorer-web | `capa-explorer-web` |  |
| chrome.extensions | `chrome.extensions` |  |
| cmder | `cmder` |  |
| codetrack | `codetrack` |  |
| cryptotester | `cryptotester` |  |
| cutter | `cutter` |  |
| [cyberchef](../reference/decode-deobfuscate/cyberchef.md) | [`cyberchef`](../reference/decode-deobfuscate/cyberchef.md) |  |
| cygwin | `cygwin` |  |
| de4dot-cex | `de4dot-cex` |  |
| dependencywalker | `dependencywalker` |  |
| dex2jar | `dex2jar` |  |
| didier-stevens-beta | `didier-stevens-beta` |  |
| didier-stevens-suite | `didier-stevens-suite` |  |
| [die](../reference/malware-triage-static/die.md) | [`die`](../reference/malware-triage-static/die.md) |  |
| dll-to-exe | `dll-to-exe` |  |
| dnlib | `dnlib` |  |
| dnspyex | `dnspyex` |  |
| dotdumper | `dotdumper` |  |
| dotnet3.5 | `dotnet3.5` |  |
| exeinfope | `exeinfope` |  |
| explorersuite | `explorersuite` |  |
| extreme_dumper | `extreme_dumper` |  |
| ezviewer | `ezviewer` |  |
| fakenet-ng | `fakenet-ng` |  |
| fiddler | `fiddler` |  |
| [file](../reference/examine-the-filesystem/file.md) | [`file`](../reference/examine-the-filesystem/file.md) |  |
| [floss](../reference/malware-triage-static/floss.md) | [`floss`](../reference/malware-triage-static/floss.md) |  |
| garbageman | `garbageman` |  |
| ghidra | `ghidra` |  |
| goresym | `goresym` |  |
| gostringungarbler | `gostringungarbler` |  |
| hashmyfiles | `hashmyfiles` |  |
| hollowshunter | `hollowshunter` |  |
| hxd | `hxd` |  |
| ida.plugin.capa | `ida.plugin.capa` |  |
| ida.plugin.comida | `ida.plugin.comida` |  |
| ida.plugin.delphihelper | `ida.plugin.delphihelper` |  |
| ida.plugin.dereferencing | `ida.plugin.dereferencing` |  |
| ida.plugin.diaphora | `ida.plugin.diaphora` |  |
| ida.plugin.flare | `ida.plugin.flare` |  |
| ida.plugin.flare-emu | `ida.plugin.flare-emu` |  |
| ida.plugin.hashdb | `ida.plugin.hashdb` |  |
| ida.plugin.hrtng | `ida.plugin.hrtng` |  |
| ida.plugin.ifl | `ida.plugin.ifl` |  |
| ida.plugin.xray | `ida.plugin.xray` |  |
| ida.plugin.xrefer | `ida.plugin.xrefer` |  |
| idafree | `idafree` |  |
| idr | `idr` |  |
| ifpstools | `ifpstools` |  |
| ilspy | `ilspy` |  |
| innoextract | `innoextract` |  |
| innounp | `innounp` |  |
| internet_detector | `internet_detector` |  |
| ipython | `ipython` |  |
| isd | `isd` |  |
| js-beautify | `js-beautify` |  |
| js-deobfuscator | `js-deobfuscator` |  |
| keystone | `keystone` |  |
| libraries.python3 | `libraries.python3` |  |
| magika | `magika` |  |
| malware-jail | `malware-jail` |  |
| map | `map` |  |
| microsoft-office | `microsoft-office` |  |
| nasm | `nasm` |  |
| net-reactor-slayer | `net-reactor-slayer` |  |
| [nmap](../reference/network-analysis/nmap.md) | [`nmap`](../reference/network-analysis/nmap.md) |  |
| notepadplusplus | `notepadplusplus` |  |
| notepadpp.plugin.compare | `notepadpp.plugin.compare` |  |
| notepadpp.plugin.jstool | `notepadpp.plugin.jstool` |  |
| notepadpp.plugin.xmltools | `notepadpp.plugin.xmltools` |  |
| obfuscator-io-deobfuscator | `obfuscator-io-deobfuscator` |  |
| offvis | `offvis` |  |
| onenoteanalyzer | `onenoteanalyzer` |  |
| pdbresym | `pdbresym` |  |
| pdfstreamdumper | `pdfstreamdumper` |  |
| pe_unmapper | `pe_unmapper` |  |
| pebear | `pebear` |  |
| peid | `peid` |  |
| pesieve | `pesieve` |  |
| pestudio | `pestudio` |  |
| pkg-unpacker | `pkg-unpacker` |  |
| pma-labs | `pma-labs` |  |
| procdot | `procdot` |  |
| processdump | `processdump` |  |
| psnotify | `psnotify` |  |
| pycdas | `pycdas` |  |
| pycdc | `pycdc` |  |
| pylingual | `pylingual` |  |
| rat-king-parser | `rat-king-parser` |  |
| recaf | `recaf` |  |
| reg_export | `reg_export` |  |
| regcool | `regcool` |  |
| regshot | `regshot` |  |
| resourcehacker | `resourcehacker` |  |
| rundotnetdll | `rundotnetdll` |  |
| scdbg | `scdbg` |  |
| sclauncher | `sclauncher` |  |
| sclauncher64 | `sclauncher64` |  |
| sfextract | `sfextract` |  |
| shellcode_launcher | `shellcode_launcher` |  |
| sysinternals | `sysinternals` |  |
| systeminformer | `systeminformer` |  |
| ttd | `ttd` |  |
| uncompyle6 | `uncompyle6` |  |
| uniextract2 | `uniextract2` |  |
| unpyc3 | `unpyc3` |  |
| [upx](../reference/malware-triage-static/upx.md) | [`upx`](../reference/malware-triage-static/upx.md) |  |
| vb-decompiler-lite | `vb-decompiler-lite` |  |
| vbdec | `vbdec` |  |
| vcbuildtools | `vcbuildtools` |  |
| vcredist-all | `vcredist-all` |  |
| vscode | `vscode` |  |
| vscode.extension.jupyter | `vscode.extension.jupyter` |  |
| vscode.extension.python | `vscode.extension.python` |  |
| windbg | `windbg` |  |
| windows-terminal | `windows-terminal` |  |
| wireshark | `wireshark` |  |
| x64dbg | `x64dbg` |  |
| x64dbg.plugin.dbgchild | `x64dbg.plugin.dbgchild` |  |
| x64dbg.plugin.ollydumpex | `x64dbg.plugin.ollydumpex` |  |
| x64dbg.plugin.scyllahide | `x64dbg.plugin.scyllahide` |  |
| x64dbg.plugin.x64dbgpy | `x64dbg.plugin.x64dbgpy` |  |
| [yara](../reference/malware-triage-static/yara.md) | [`yara`](../reference/malware-triage-static/yara.md) |  |


## SIFT Workstation

### Forensic Packages

| Tool | Command(s) | Purpose |
|---|---|---|
| absent | `absent` |  |
| [aeskeyfind](../reference/memory-forensics/aeskeyfind.md) | [`aeskeyfind`](../reference/memory-forensics/aeskeyfind.md) |  |
| afflib-tools | `afflib-tools` |  |
| aircrack-ng | `aircrack-ng` |  |
| android-sdk-platform-tools | `android-sdk-platform-tools` |  |
| [arp-scan](../reference/network-analysis/arp-scan.md) | [`arp-scan`](../reference/network-analysis/arp-scan.md) |  |
| autopsy | `autopsy` |  |
| avfs | `avfs` |  |
| aws-cli | `aws-cli` |  |
| bless | `bless` |  |
| blt | `blt` |  |
| bulk-extractor | `bulk-extractor` |  |
| cabextract | `cabextract` |  |
| ccrypt | `ccrypt` |  |
| chromium-browser | `chromium-browser` |  |
| clamav | `clamav` |  |
| claude-code | `claude-code` |  |
| cmospwd | `cmospwd` |  |
| cryptcat | `cryptcat` |  |
| cryptsetup | `cryptsetup` |  |
| [dc3dd](../reference/acquire-preserve/dc3dd.md) | [`dc3dd`](../reference/acquire-preserve/dc3dd.md) |  |
| [dcfldd](../reference/acquire-preserve/dcfldd.md) | [`dcfldd`](../reference/acquire-preserve/dcfldd.md) |  |
| default-jre | `default-jre` |  |
| disktype | `disktype` |  |
| dislocker | `dislocker` |  |
| docker | `docker` |  |
| dos2unix | `dos2unix` |  |
| dotnet | `dotnet` |  |
| driftnet | `driftnet` |  |
| dsniff | `dsniff` |  |
| e2fsprogs | `e2fsprogs` |  |
| ent | `ent` |  |
| epic5 | `epic5` |  |
| etherape | `etherape` |  |
| ettercap-graphical | `ettercap-graphical` |  |
| ewf-tools | `ewf-tools` |  |
| exfat-extras | `exfat-extras` |  |
| exfat-fuse | `exfat-fuse` |  |
| exif | `exif` |  |
| extundelete | `extundelete` |  |
| fdupes | `fdupes` |  |
| feh | `feh` |  |
| [file](../reference/examine-the-filesystem/file.md) | [`file`](../reference/examine-the-filesystem/file.md) |  |
| flex | `flex` |  |
| [foremost](../reference/examine-the-filesystem/foremost.md) | [`foremost`](../reference/examine-the-filesystem/foremost.md) |  |
| gawk | `gawk` |  |
| gdb | `gdb` |  |
| gddrescue | `gddrescue` |  |
| ghex | `ghex` |  |
| graphviz | `graphviz` |  |
| grepcidr | `grepcidr` |  |
| gthumb | `gthumb` |  |
| gzrt | `gzrt` |  |
| hashdeep | `hashdeep` |  |
| hexedit | `hexedit` |  |
| [hydra](../reference/decode-deobfuscate/hydra.md) | [`hydra`](../reference/decode-deobfuscate/hydra.md) |  |
| hydra-gtk | `hydra-gtk` |  |
| init | `init` |  |
| ipython3 | `ipython3` |  |
| jq | `jq` |  |
| kdiff3 | `kdiff3` |  |
| kpartx | `kpartx` |  |
| lft | `lft` |  |
| lvm2 | `lvm2` |  |
| magnus | `magnus` |  |
| mdadm | `mdadm` |  |
| mtd-utils | `mtd-utils` |  |
| nbd-client | `nbd-client` |  |
| nbtscan | `nbtscan` |  |
| netcat | `netcat` |  |
| netpbm | `netpbm` |  |
| netsed | `netsed` |  |
| netwox | `netwox` |  |
| nfdump | `nfdump` |  |
| [ngrep](../reference/network-analysis/ngrep.md) | [`ngrep`](../reference/network-analysis/ngrep.md) |  |
| nikto | `nikto` |  |
| [ntfs-3g](../reference/acquire-preserve/ntfs-3g.md) | [`ntfs-3g`](../reference/acquire-preserve/ntfs-3g.md) |  |
| okular | `okular` |  |
| onboard | `onboard` |  |
| open-iscsi | `open-iscsi` |  |
| openjdk | `openjdk` |  |
| ophcrack | `ophcrack` |  |
| ophcrack-cli | `ophcrack-cli` |  |
| orca | `orca` |  |
| outguess | `outguess` |  |
| p0f | `p0f` |  |
| p7zip-full | `p7zip-full` |  |
| patch | `patch` |  |
| pdftk-java | `pdftk-java` |  |
| perl | `perl` |  |
| pev | `pev` |  |
| pff-tools | `pff-tools` |  |
| phonon | `phonon` |  |
| pkg-config | `pkg-config` |  |
| plaso-tools | `plaso-tools` |  |
| powershell | `powershell` |  |
| pst-utils | `pst-utils` |  |
| pv | `pv` |  |
| python-flowgrep | `python-flowgrep` |  |
| python3-debian | `python3-debian` |  |
| python3-dfvfs | `python3-dfvfs` |  |
| python3-fuse | `python3-fuse` |  |
| python3-keyrings-alt | `python3-keyrings-alt` |  |
| python3-m2crypto | `python3-m2crypto` |  |
| python3-magic | `python3-magic` |  |
| python3-pefile | `python3-pefile` |  |
| python3-plaso | `python3-plaso` |  |
| python3-pypff | `python3-pypff` |  |
| python3-pyqt5 | `python3-pyqt5` |  |
| python3-pytsk3 | `python3-pytsk3` |  |
| python3-redis | `python3-redis` |  |
| python3-setuptools-rust | `python3-setuptools-rust` |  |
| python3-tk | `python3-tk` |  |
| python3-tsk | `python3-tsk` |  |
| python3-virtualenv | `python3-virtualenv` |  |
| python3-wxgtk4 | `python3-wxgtk4` |  |
| python3-xlsxwriter | `python3-xlsxwriter` |  |
| python3-yara | `python3-yara` |  |
| qemu | `qemu` |  |
| qemu-utils | `qemu-utils` |  |
| radare2 | `radare2` |  |
| rar | `rar` |  |
| [rsakeyfind](../reference/memory-forensics/rsakeyfind.md) | [`rsakeyfind`](../reference/memory-forensics/rsakeyfind.md) |  |
| safecopy | `safecopy` |  |
| samdump2 | `samdump2` |  |
| [scalpel](../reference/examine-the-filesystem/scalpel.md) | [`scalpel`](../reference/examine-the-filesystem/scalpel.md) |  |
| silversearcher-ag | `silversearcher-ag` |  |
| sleuthkit | `sleuthkit` |  |
| socat | `socat` |  |
| squashfs-tools | `squashfs-tools` |  |
| [ssdeep](../reference/acquire-preserve/ssdeep.md) | [`ssdeep`](../reference/acquire-preserve/ssdeep.md) |  |
| ssldump | `ssldump` |  |
| sslsniff | `sslsniff` |  |
| stunnel4 | `stunnel4` |  |
| swig | `swig` |  |
| tcl | `tcl` |  |
| [tcpflow](../reference/network-analysis/tcpflow.md) | [`tcpflow`](../reference/network-analysis/tcpflow.md) |  |
| tcpick | `tcpick` |  |
| tcpreplay | `tcpreplay` |  |
| tcpslice | `tcpslice` |  |
| tcpstat | `tcpstat` |  |
| tcptrace | `tcptrace` |  |
| tcptrack | `tcptrack` |  |
| [tcpxtract](../reference/examine-the-filesystem/tcpxtract.md) | [`tcpxtract`](../reference/examine-the-filesystem/tcpxtract.md) |  |
| [testdisk](../reference/examine-the-filesystem/testdisk.md) | [`testdisk`](../reference/examine-the-filesystem/testdisk.md) |  |
| tofrodos | `tofrodos` |  |
| transmission | `transmission` |  |
| ugrep | `ugrep` |  |
| unity-control-center | `unity-control-center` |  |
| unrar | `unrar` |  |
| upx-ucl | `upx-ucl` |  |
| vbindiff | `vbindiff` |  |
| virtuoso-minimal | `virtuoso-minimal` |  |
| vmfs-tools | `vmfs-tools` |  |
| winbind | `winbind` |  |
| wine | `wine` |  |
| wireshark | `wireshark` |  |
| xdot | `xdot` |  |
| xfsprogs | `xfsprogs` |  |
| xmount | `xmount` |  |
| zenity | `zenity` |  |
| zlib1g-dev | `zlib1g-dev` |  |


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
