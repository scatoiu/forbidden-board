#!/bin/zsh
# Dataset freeze + final analysis pass. Run from project/tournament at the freeze time.
set -e
cd "$(dirname "$0")"
STAMP=$(date -u +%Y%m%dT%H%M%SZ)
echo "== freeze at $STAMP (UTC)"
echo "-- runners still alive (expected: only the absent-high repair, which is cut now):"
pgrep -fl 'coop.cli run-population' | sed 's#./##' | awk '{print $1, $NF}' || true
echo "-- freeze: terminating every remaining runner (repaired games already on disk are merged; the rest stay unobserved)"
pkill -TERM -f 'coop.cli run-population' || true
sleep 8
pkill -KILL -f 'coop.cli run-population' 2>/dev/null || true
sleep 2
n=$(pgrep -f 'coop.cli run-population' | wc -l | tr -d ' ')
if [ "$n" -ne 0 ]; then echo "!! $n runners still alive — wait for them or stop them, then rerun"; pgrep -fl 'coop.cli run-population' | awk '{print $1,$NF}'; exit 1; fi
echo "-- no runners. Inventory of every root (bytes, lines, sha256):"
INV=reports/FREEZE-$STAMP-inventory.tsv
printf "path\tbytes\tlines\tsha256\n" > $INV
for f in runs/v3/*/moves.jsonl runs/v3b/*/moves.jsonl runs/v3-mimo/*/moves.jsonl runs/v4-a4096/*/moves.jsonl runs/v5-d30/*/moves.jsonl runs/v6-low/*/moves.jsonl runs/v7-repair/*/moves.jsonl; do
  printf "%s\t%s\t%s\t%s\n" "$f" "$(stat -f %z "$f")" "$(wc -l < "$f" | tr -d ' ')" "$(shasum -a 256 "$f" | cut -d' ' -f1)" >> $INV
done
echo "   $(($(wc -l < $INV)-1)) files inventoried -> $INV"
echo "-- final analysis pass"
OUT=reports/final-$STAMP
.venv/bin/python -m analysis.run_all --runs runs/v3 runs/v3b runs/v3-mimo --repairs runs/v7-repair --replication runs/v4-a4096 --out $OUT 2>&1 | tail -8
echo "-- exploratory add-ons (separate loads, never pooled): low arm and -30 deficit"
.venv/bin/python -m analysis.run_all --runs runs/v6-low --out $OUT-lowarm 2>&1 | tail -3 || echo "(low-arm pass failed; see above)"
.venv/bin/python -m analysis.run_all --runs runs/v5-d30 --out $OUT-d30 2>&1 | tail -3 || echo "(d30 pass failed; see above)"
echo "-- post-freeze inventory check"
CHK=0
while IFS=$'\t' read -r p b l s; do [ "$p" = "path" ] && continue; s2=$(shasum -a 256 "$p" | cut -d' ' -f1); [ "$s" = "$s2" ] || { echo "!! CHANGED after freeze: $p"; CHK=1; }; done < $INV
[ $CHK -eq 0 ] && echo "   inventory unchanged: dataset frozen" 
echo "== done: $OUT"
