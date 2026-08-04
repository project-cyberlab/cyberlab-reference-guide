#!/bin/sh
# Exit as soon as there are notes I have not reviewed. Exiting raises a task
# notification, which is the only way this session gets woken between user
# messages -- so this is what turns "review after each round" from an
# intention into a mechanism.
cd /c/Users/m808b/dev/cyberlab-reference-guide
while true; do
  n=$(python -c "
import json
try:
    k=json.load(open('research_output.json',encoding='utf-8'))
except Exception: k=[]
try:
    d=json.load(open('research_decisions.json',encoding='utf-8'))
except Exception: d={}
print(sum(1 for r in k if not r.get('flag') and r['tool'] not in d))
" 2>/dev/null || echo 0)
  case "$n" in ''|*[!0-9]*) n=0 ;; esac
  if [ "$n" -ge 5 ]; then
    echo "REVIEW READY: $n tool notes awaiting judgement"
    exit 0
  fi
  sleep 120
done
