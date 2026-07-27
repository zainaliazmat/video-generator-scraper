#!/usr/bin/env bash
# Draft-render a set of chapters back to back. Sequential on purpose: renders are
# scratch-disk hungry (§6 ledger — two orphaned work-* dirs once filled the disk).
set -e
cd "$(dirname "$0")"
for c in "$@"; do
  echo "=== building chapter $c ==="
  python3 build.py --chapter "$c" | head -1
  npx hyperframes lint . 2>&1 | grep -E "error\(s\)"
  npx hyperframes render . --quality draft --output "renders/ch${c}-draft.mp4" 2>&1 | tail -2
  df -h /home | tail -1
done
echo "ALL DONE"
