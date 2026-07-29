#!/usr/bin/env bash
# US-English VO for emergency-fund-en. Voice: ElevenLabs "Brian" (American male narrator).
set -e
cd /home/zain-ali/Documents/YoutubeScraper/studio/videos/emergency-fund-en
TTS=/home/zain-ali/Documents/YoutubeScraper/tools/tts/elevenlabs_tts.py
VOICE=${VOICE:-nPczCjzI2devNBz1zQrb}
for i in $(seq 1 9); do
  eid="en$i"
  node -e "process.stdout.write(require('./assets/voice/english-lines.json')['$eid'])" > "assets/voice/$eid.txt"
  echo "=== $eid ==="
  python3 "$TTS" --voice "$VOICE" --file "assets/voice/$eid.txt" --out "assets/voice/$eid.mp3" 2>&1 | tail -1
done
echo "=== DURATIONS ==="
for i in $(seq 1 9); do
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "assets/voice/en$i.mp3")
  printf 'en%s\t%s\n' "$i" "$d"
done
echo "ALL DONE"
