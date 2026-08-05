#!/bin/sh
# Watch the research loop and exit when it dies or stops producing verdicts.
# Exiting raises a task notification, which is how this session gets woken.
#
# Reads a STABLE path. Earlier versions were pointed at loop5.log, then
# loop6.log, then loop7.log, so every restart orphaned the previous watchdog,
# which carried on watching a file nobody was writing to and eventually
# reported the loop as unproductive. Three false alarms came from that, and
# each one cost a real check to disprove.
#
# Health is measured in VERDICTS, never in log lines. A loop emitting backoff
# messages every five minutes grows its log indefinitely while producing
# nothing, and an earlier watchdog called that healthy for nine hours.
# No argument. The stable path is the whole point: this script was written
# because per-run logs orphaned a watchdog on every restart, and then I
# passed loop7.log and loop8.log explicitly anyway and orphaned two more.
# Removing the parameter removes the mistake.
LOG=/c/Users/m808b/dev/cyberlab-reference-guide/research_live.log
prev=0
barren=0
while true; do
  alive=$(powershell.exe -NoProfile -Command "(Get-CimInstance Win32_Process -Filter \"Name='python.exe'\" | Where-Object { \$_.CommandLine -like '*run_forever*' } | Measure-Object).Count" 2>/dev/null | tr -d '\r\n ')
  case "$alive" in ''|*[!0-9]*) alive=1 ;; esac
  if [ "$alive" -eq 0 ]; then
    echo "WATCHDOG: runner process is GONE at $(date +%H:%M)"
    exit 1
  fi
  n=$(grep -cE "(KEPT|MISS|REJECTED|REVIEW) " "$LOG" 2>/dev/null || echo 0)
  if [ "$n" -le "$prev" ]; then barren=$((barren + 1)); else barren=0; fi
  prev=$n
  if [ "$barren" -ge 20 ]; then
    echo "WATCHDOG: alive but UNPRODUCTIVE for ~20min (stuck at $n verdicts)"
    exit 3
  fi
  sleep 60
done
