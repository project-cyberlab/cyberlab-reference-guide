<!-- generated-by: scripts/generate_pages.py -->
# wget

**Kit:** REMnux  **Capability:** Fetch and verify external references  **Version:** GNU Wget 1.21.3
**Captured:** `cyberlab-aio` via `--help` on 2026-07-29  [raw](../../capture/cyberlab-aio/help/wget.help.txt)  **Docs:** <https://www.gnu.org/software/wget/>

## Purpose

Interact with servers via HTTP, HTTPS, FTP, and FTPS using this command-line tool.

## Synopsis

```
wget [OPTION]... [URL]...
```

## Common invocations

_TODO: up to 8 task-titled invocations._

## Options

All 184 options parsed from the captured help text. The final column is the judgement layer and is filled in by review.

| Flag | Argument | What it does | When you would use it |
|---|---|---|---|
| `-V` | — | display the version of Wget and exit | |
| `--version` | — | display the version of Wget and exit | |
| `-h` | — | print this help | |
| `--help` | — | print this help | |
| `-b` | — | go to background after startup | |
| `--background` | — | go to background after startup | |
| `-e` | COMMAND | execute a `.wgetrc'-style command | |
| `--execute` | COMMAND | execute a `.wgetrc'-style command | |
| `-o` | FILE | log messages to FILE | |
| `--output-file` | FILE | log messages to FILE | |
| `-a` | FILE | append messages to FILE | |
| `--append-output` | FILE | append messages to FILE | |
| `-d` | — | print lots of debugging information | |
| `--debug` | — | print lots of debugging information | |
| `-q` | — | quiet (no output) | |
| `--quiet` | — | quiet (no output) | |
| `-v` | — | be verbose (this is the default) | |
| `--verbose` | — | be verbose (this is the default) | |
| `--report-speed` | TYPE | output bandwidth as TYPE. TYPE can be bits | |
| `-i` | FILE | download URLs found in local or external FILE | |
| `--input-file` | FILE | download URLs found in local or external FILE | |
| `-F` | — | treat input file as HTML | |
| `--force-html` | — | treat input file as HTML | |
| `-B` | URL | resolves HTML input-file links (-i -F) relative to URL | |
| `--base` | URL | resolves HTML input-file links (-i -F) relative to URL | |
| `--config` | FILE | specify config file to use | |
| `--no-config` | — | do not read any config file | |
| `--rejected-log` | FILE | log reasons for URL rejection to FILE | |
| `-t` | NUMBER | set number of retries to NUMBER (0 unlimits) | |
| `--tries` | NUMBER | set number of retries to NUMBER (0 unlimits) | |
| `--retry-connrefused` | — | retry even if connection is refused | |
| `--retry-on-http-error` | ERRORS | comma-separated list of HTTP errors to retry | |
| `-O` | FILE | write documents to FILE | |
| `--output-document` | FILE | write documents to FILE | |
| `--no-netrc` | — | don't try to obtain credentials from .netrc | |
| `-c` | — | resume getting a partially-downloaded file | |
| `--continue` | — | resume getting a partially-downloaded file | |
| `--start-pos` | OFFSET | start downloading from zero-based position OFFSET | |
| `--progress` | TYPE | select progress gauge type | |
| `--show-progress` | — | display the progress bar in any verbosity mode | |
| `-N` | — | don't re-retrieve files unless newer than local | |
| `--timestamping` | — | don't re-retrieve files unless newer than local | |
| `--no-if-modified-since` | — | don't use conditional if-modified-since get requests in timestamping mode | |
| `--no-use-server-timestamps` | — | don't set the local file's timestamp by the one on the server | |
| `-S` | — | print server response | |
| `--server-response` | — | print server response | |
| `--spider` | — | don't download anything | |
| `-T` | SECONDS | set all timeout values to SECONDS | |
| `--timeout` | SECONDS | set all timeout values to SECONDS | |
| `--dns-timeout` | SECS | set the DNS lookup timeout to SECS | |
| `--connect-timeout` | SECS | set the connect timeout to SECS | |
| `--read-timeout` | SECS | set the read timeout to SECS | |
| `-w` | SECONDS | wait SECONDS between retrievals (applies if more then 1 URL is to be retrieved) | |
| `--wait` | SECONDS | wait SECONDS between retrievals (applies if more then 1 URL is to be retrieved) | |
| `--waitretry` | SECONDS | wait 1..SECONDS between retries of a retrieval (applies if more then 1 URL is to be retrieved) | |
| `--random-wait` | — | wait from 0.5*WAIT...1.5*WAIT secs between retrievals (applies if more then 1 URL is to be retrieved) | |
| `--no-proxy` | — | explicitly turn off proxy | |
| `-Q` | NUMBER | set retrieval quota to NUMBER | |
| `--quota` | NUMBER | set retrieval quota to NUMBER | |
| `--bind-address` | ADDRESS | bind to ADDRESS (hostname or IP) on local host | |
| `--limit-rate` | RATE | limit download rate to RATE | |
| `--no-dns-cache` | — | disable caching DNS lookups | |
| `--restrict-file-names` | OS | restrict chars in file names to ones OS allows | |
| `--ignore-case` | — | ignore case when matching files/directories | |
| `-4` | — | connect only to IPv4 addresses | |
| `--inet4-only` | — | connect only to IPv4 addresses | |
| `-6` | — | connect only to IPv6 addresses | |
| `--inet6-only` | — | connect only to IPv6 addresses | |
| `--prefer-family` | FAMILY | connect first to addresses of specified family, one of IPv6, IPv4, or none | |
| `--user` | USER | set both ftp and http user to USER | |
| `--password` | PASS | set both ftp and http password to PASS | |
| `--ask-password` | — | prompt for passwords | |
| `--use-askpass` | COMMAND | specify credential handler for requesting username and password. If no COMMAND is specified the WGET_ASKPASS or the SSH_ASKPASS environment variable is used. | |
| `--no-iri` | — | turn off IRI support | |
| `--local-encoding` | ENC | use ENC as the local encoding for IRIs | |
| `--remote-encoding` | ENC | use ENC as the default remote encoding | |
| `--unlink` | — | remove file before clobber | |
| `--xattr` | — | turn on storage of metadata in extended file attributes | |
| `-x` | — | force creation of directories | |
| `--force-directories` | — | force creation of directories | |
| `--protocol-directories` | — | use protocol name in directories | |
| `-P` | PREFIX | save files to PREFIX/.. | |
| `--directory-prefix` | PREFIX | save files to PREFIX/.. | |
| `--cut-dirs` | NUMBER | ignore NUMBER remote directory components | |
| `--http-user` | USER | set http user to USER | |
| `--http-password` | PASS | set http password to PASS | |
| `--no-cache` | — | disallow server-cached data | |
| `--default-page` | NAME | change the default page name (normally this is 'index.html'.) | |
| `-E` | — | save HTML/CSS documents with proper extensions | |
| `--adjust-extension` | — | save HTML/CSS documents with proper extensions | |
| `--ignore-length` | — | ignore 'Content-Length' header field | |
| `--header` | STRING | insert STRING among the headers | |
| `--compression` | TYPE | choose compression, one of auto, gzip and none. (default: none) | |
| `--max-redirect` | — | maximum redirections allowed per page | |
| `--proxy-user` | USER | set USER as proxy username | |
| `--proxy-password` | PASS | set PASS as proxy password | |
| `--referer` | URL | include 'Referer: URL' header in HTTP request | |
| `--save-headers` | — | save the HTTP headers to file | |
| `-U` | AGENT | identify as AGENT instead of Wget/VERSION | |
| `--user-agent` | AGENT | identify as AGENT instead of Wget/VERSION | |
| `--no-http-keep-alive` | — | disable HTTP keep-alive (persistent connections) | |
| `--no-cookies` | — | don't use cookies | |
| `--load-cookies` | FILE | load cookies from FILE before session | |
| `--save-cookies` | FILE | save cookies to FILE after session | |
| `--keep-session-cookies` | — | load and save session (non-permanent) cookies | |
| `--post-data` | STRING | use the POST method; send STRING as the data | |
| `--post-file` | FILE | use the POST method; send contents of FILE | |
| `--method` | HTTPMethod | use method "HTTPMethod" in the request | |
| `--body-data` | STRING | send STRING as data. --method MUST be set | |
| `--body-file` | FILE | send contents of FILE. --method MUST be set | |
| `--content-disposition` | — | honor the Content-Disposition header when choosing local file names (EXPERIMENTAL) | |
| `--content-on-error` | — | output the received content on server errors | |
| `--auth-no-challenge` | — | send Basic HTTP authentication information without first waiting for the server's challenge | |
| `--secure-protocol` | PR | choose secure protocol, one of auto, SSLv2, SSLv3, TLSv1, TLSv1_1, TLSv1_2, TLSv1_3 and PFS | |
| `--https-only` | — | only follow secure HTTPS links | |
| `--no-check-certificate` | — | don't validate the server's certificate | |
| `--certificate` | FILE | client certificate file | |
| `--certificate-type` | TYPE | client certificate type, PEM or DER | |
| `--private-key` | FILE | private key file | |
| `--private-key-type` | TYPE | private key type, PEM or DER | |
| `--ca-certificate` | FILE | file with the bundle of CAs | |
| `--ca-directory` | DIR | directory where hash list of CAs is stored | |
| `--crl-file` | FILE | file with bundle of CRLs | |
| `--ciphers` | STR | Set the priority string (GnuTLS) or cipher list string (OpenSSL) directly. Use with care. This option overrides --secure-protocol. The format and syntax of this string depend on the specific SSL/TLS e | |
| `--no-hsts` | — | disable HSTS | |
| `--hsts-file` | — | path of HSTS database (will override default) | |
| `--ftp-user` | USER | set ftp user to USER | |
| `--ftp-password` | PASS | set ftp password to PASS | |
| `--no-remove-listing` | — | don't remove '.listing' files | |
| `--no-glob` | — | turn off FTP file name globbing | |
| `--no-passive-ftp` | — | disable the "passive" transfer mode | |
| `--preserve-permissions` | — | preserve remote file permissions | |
| `--retr-symlinks` | — | when recursing, get linked-to files (not dir) | |
| `--ftps-implicit` | — | use implicit FTPS (default port is 990) | |
| `--ftps-resume-ssl` | — | resume the SSL/TLS session started in the control connection when opening a data connection | |
| `--ftps-clear-data-connection` | — | cipher the control channel only; all the data will be in plaintext | |
| `--ftps-fallback-to-ftp` | — | fall back to FTP if FTPS is not supported in the target server | |
| `--warc-file` | FILENAME | save request/response data to a .warc.gz file | |
| `--warc-header` | STRING | insert STRING into the warcinfo record | |
| `--warc-max-size` | NUMBER | set maximum size of WARC files to NUMBER | |
| `--warc-cdx` | — | write CDX index files | |
| `--warc-dedup` | FILENAME | do not store records listed in this CDX file | |
| `--no-warc-compression` | — | do not compress WARC files with GZIP | |
| `--no-warc-digests` | — | do not calculate SHA1 digests | |
| `--no-warc-keep-log` | — | do not store the log file in a WARC record | |
| `--warc-tempdir` | DIRECTORY | location for temporary files created by the WARC writer | |
| `-r` | — | specify recursive download | |
| `--recursive` | — | specify recursive download | |
| `-l` | NUMBER | maximum recursion depth (inf or 0 for infinite) | |
| `--level` | NUMBER | maximum recursion depth (inf or 0 for infinite) | |
| `--delete-after` | — | delete files locally after downloading them | |
| `-k` | — | make links in downloaded HTML or CSS point to local files | |
| `--convert-links` | — | make links in downloaded HTML or CSS point to local files | |
| `--convert-file-only` | — | convert the file part of the URLs only (usually known as the basename) | |
| `--backups` | N | before writing file X, rotate up to N backup files | |
| `-K` | — | before converting file X, back up as X.orig | |
| `--backup-converted` | — | before converting file X, back up as X.orig | |
| `-m` | — | shortcut for -N -r -l inf --no-remove-listing | |
| `--mirror` | — | shortcut for -N -r -l inf --no-remove-listing | |
| `-p` | — | get all images, etc. needed to display HTML page | |
| `--page-requisites` | — | get all images, etc. needed to display HTML page | |
| `--strict-comments` | — | turn on strict (SGML) handling of HTML comments | |
| `-A` | LIST | comma-separated list of accepted extensions | |
| `--accept` | LIST | comma-separated list of accepted extensions | |
| `-R` | LIST | comma-separated list of rejected extensions | |
| `--reject` | LIST | comma-separated list of rejected extensions | |
| `--accept-regex` | REGEX | regex matching accepted URLs | |
| `--reject-regex` | REGEX | regex matching rejected URLs | |
| `--regex-type` | TYPE | regex type (posix\|pcre) | |
| `-D` | LIST | comma-separated list of accepted domains | |
| `--domains` | LIST | comma-separated list of accepted domains | |
| `--exclude-domains` | LIST | comma-separated list of rejected domains | |
| `--follow-ftp` | — | follow FTP links from HTML documents | |
| `--follow-tags` | LIST | comma-separated list of followed HTML tags | |
| `--ignore-tags` | LIST | comma-separated list of ignored HTML tags | |
| `-H` | — | go to foreign hosts when recursive | |
| `--span-hosts` | — | go to foreign hosts when recursive | |
| `-L` | — | follow relative links only | |
| `--relative` | — | follow relative links only | |
| `-I` | LIST | list of allowed directories | |
| `--include-directories` | LIST | list of allowed directories | |
| `--trust-server-names` | — | use the name specified by the redirection URL's last component | |
| `-X` | LIST | list of excluded directories | |
| `--exclude-directories` | LIST | list of excluded directories | |

## Gotchas

_TODO: operational traps._

## See also

`curl`
