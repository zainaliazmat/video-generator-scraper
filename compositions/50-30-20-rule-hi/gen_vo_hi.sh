#!/usr/bin/env bash
# Standard-Hindi VO. Voice: ElevenLabs "Harsh" (hi, standard accent, informative_educational).
set -e
cd "$(dirname "$0")"
TTS=/home/zain-ali/Documents/YoutubeScraper/tools/tts/elevenlabs_tts.py
VOICE=${VOICE:-HTUuC7OeeEt6OL5fViVe}
for i in $(seq 1 9); do
  hid="hi$i"
  node -e "process.stdout.write(require('./assets/voice/hindi-lines.json')['$hid'])" > "assets/voice/$hid.txt"
  echo "=== $hid ==="
  python3 "$TTS" --voice "$VOICE" --file "assets/voice/$hid.txt" --out "assets/voice/$hid.mp3" \
    --stability 0.45 --similarity 0.8 --style 0.25 2>&1 | tail -1
done
echo "=== DURATIONS ==="
for i in $(seq 1 9); do
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "assets/voice/hi$i.mp3")
  printf 'hi%s\t%s\n' "$i" "$d"
done
