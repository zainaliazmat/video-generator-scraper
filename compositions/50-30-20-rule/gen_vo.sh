#!/usr/bin/env bash
set -e
cd /home/zain-ali/Documents/YoutubeScraper/studio/videos/50-30-20-rule
for i in $(seq 1 9); do
  sid="s$i"
  txt=$(node -e "process.stdout.write(require('./assets/voice/lines.json')['$sid'])")
  echo "=== $sid ==="
  printf '%s' "$txt" > "assets/voice/$sid.txt"
  npx --yes hyperframes@0.7.66 tts --text-file "assets/voice/$sid.txt" --voice am_michael --output "assets/voice/$sid.wav" 2>&1 | tail -2
done
echo "=== DURATIONS ==="
for i in $(seq 1 9); do
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "assets/voice/s$i.wav" 2>/dev/null)
  printf 's%s\t%s\n' "$i" "$d"
done
echo "ALL DONE"
