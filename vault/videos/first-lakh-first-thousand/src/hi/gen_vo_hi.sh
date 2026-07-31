#!/usr/bin/env bash
set -euo pipefail

# Regenerate the hi VO for first-lakh-first-thousand.
# batch.py is skip-if-exists: delete assets/voice/*.mp3 (or pass --force) to re-pay TTS.
# ponytail: ROOT is overridable so this still runs after archive_cut.py moves the
# project out of studio/ — the hardcoded-cd trap named in vault/CLAUDE.md.
ROOT="${YTS_ROOT:-/home/zain-ali/Documents/YoutubeScraper}"
cd "$ROOT"

python3 tools/tts/batch.py --project studio/videos/first-lakh-first-thousand-hi --cut hi
