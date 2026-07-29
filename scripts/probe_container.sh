#!/usr/bin/env bash
# Probe a kit container for candidate commands and capture their real help text.
#
# Runs INSIDE the container. For each candidate: is it present, what version,
# and what does its own help output say. Every invocation is hard-timeout
# guarded -- vol/binwalk/clamscan have pinned CPU indefinitely on this project
# before, and one hanging tool must not stall the whole capture.
#
# usage: probe_container.sh <candidates-file> <outdir>
set -u

CANDS="${1:?candidates file}"
OUT="${2:?output dir}"
mkdir -p "$OUT/help"
COV="$OUT/coverage.tsv"
: > "$COV"
printf 'command\tstatus\thelp_flag\tbytes\tversion\n' >> "$COV"

TIMEOUT=8

grab() {  # grab <cmd> <flag...>  -> prints output, non-zero if useless
  # stdin MUST be /dev/null: a probed tool that reads stdin (cat, sqlite3,
  # openssl...) otherwise swallows lines straight out of the candidates file
  # that feeds the read-loop below, silently skipping those candidates.
  timeout -s KILL "$TIMEOUT" "$@" </dev/null 2>&1 | head -c 65536
}

n_present=0
n_absent=0
n_help=0

# Read on FD 3, not stdin, so no probed command can consume the candidate list.
while IFS= read -r cmd <&3; do
  [ -z "$cmd" ] && continue
  if ! command -v "$cmd" >/dev/null 2>&1; then
    printf '%s\tabsent\t\t0\t\n' "$cmd" >> "$COV"
    n_absent=$((n_absent+1))
    continue
  fi
  n_present=$((n_present+1))

  ver=""
  for vf in --version -V -v version; do
    ver="$(grab "$cmd" "$vf" | head -1 | tr -d '\t\r')"
    case "$ver" in
      *[Vv]ersion*|*[0-9].[0-9]*) break ;;
      *) ver="" ;;
    esac
  done

  body=""
  used=""
  for hf in --help -h -help help; do
    body="$(grab "$cmd" "$hf")"
    # A real help text mentions usage/options and is not a one-line error.
    if [ "$(printf '%s' "$body" | wc -c)" -gt 120 ]; then
      used="$hf"
      break
    fi
    body=""
  done

  # Some tools (fls, mmls) print usage only when run with no arguments.
  if [ -z "$body" ]; then
    body="$(grab "$cmd")"
    [ "$(printf '%s' "$body" | wc -c)" -gt 120 ] && used="(no args)"
  fi

  # Fall back to the man page.
  if [ -z "$used" ] && command -v man >/dev/null 2>&1; then
    body="$(timeout -s KILL "$TIMEOUT" man "$cmd" </dev/null 2>/dev/null | col -bx | head -c 65536)"
    [ "$(printf '%s' "$body" | wc -c)" -gt 120 ] && used="man"
  fi

  bytes=0
  if [ -n "$used" ]; then
    safe="$(printf '%s' "$cmd" | tr -c 'A-Za-z0-9._-' '_')"
    {
      printf '# command: %s\n# version: %s\n# captured-via: %s\n# image: %s\n#---\n' \
             "$cmd" "$ver" "$used" "${KIT_IMAGE:-unknown}"
      printf '%s\n' "$body"
    } > "$OUT/help/$safe.help.txt"
    bytes="$(printf '%s' "$body" | wc -c)"
    n_help=$((n_help+1))
  fi
  printf '%s\tpresent\t%s\t%s\t%s\n' "$cmd" "$used" "$bytes" "$ver" >> "$COV"
done 3< "$CANDS"

printf 'PROBE DONE present=%s absent=%s with_help=%s\n' "$n_present" "$n_absent" "$n_help"
