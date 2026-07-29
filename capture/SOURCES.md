# Source Validation

Checked 255 distinct URLs on 2026-07-29.
Control (`https://attack.mitre.org/`) responded, so this run is conclusive.

- **245 live**
- **10 dead or unreachable**

## Dead or unreachable

| URL | Status | Cited by |
|---|---|---|
| https://citp.princeton.edu/our-work/memory/ | 403 | catalog:REMnux:AESKeyFinder, catalog:REMnux:RSAKeyFinder, reference/memory-forensics/aeskeyfind.md |
| https://developer.mozilla.org/en-US/docs/Mozilla/Projects/Rhino/Debugger | 404 | catalog:REMnux:Rhino Debugger |
| https://developer.mozilla.org/en-US/docs/Mozilla/Projects/SpiderMonkey | 404 | catalog:REMnux:SpiderMonkey |
| https://eternal-todo.com/category/bruteforcer | 404 | catalog:REMnux:xorBruteForcer.py |
| https://hg.sr.ht/\~olly/fakemail | 418 | catalog:REMnux:fakemail |
| https://portswigger.net | 404 | catalog:REMnux:Burp Suite Community Edition |
| https://raw.githubusercontent.com/REMnux/docs/master/discover-the-tools | 404 | catalog:source |
| https://www.gnu.org/software/wget/ | URLError | catalog:REMnux:GNU Wget, reference/report-support/wget.md |
| https://www.mitec.cz/ssv.html | URLError | catalog:REMnux:SSView |
| https://www.winehq.org | 403 | catalog:REMnux:Wine |

A 403 usually means the host blocks automated clients rather than the page being gone; those are worth a manual look before removing the citation.
