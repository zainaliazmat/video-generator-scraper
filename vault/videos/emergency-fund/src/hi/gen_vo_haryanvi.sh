#!/usr/bin/env bash
set -e
cd /home/zain-ali/Documents/YoutubeScraper/studio/videos/emergency-fund
TTS=/home/zain-ali/Documents/YoutubeScraper/tools/tts/elevenlabs_tts.py
for i in $(seq 1 9); do
  hid="h$i"
  node -e "process.stdout.write(require('./assets/voice/haryanvi-lines.json')['$hid'])" > "assets/voice/$hid.txt"
  echo "=== $hid ==="
  python3 "$TTS" --voice 9BHTbeEKC5ZqMmvZfLW6 --file "assets/voice/$hid.txt" --out "assets/voice/$hid.mp3" 2>&1 | tail -1
done
echo "=== DURATIONS ==="
for i in $(seq 1 9); do
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "assets/voice/h$i.mp3" 2>/dev/null)
  printf 'h%s\t%s\n' "$i" "$d"
done
echo "ALL DONE"
