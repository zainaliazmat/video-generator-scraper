#!/usr/bin/env bash
set -euo pipefail
# Regenerate the en VO for passive-income-number (ElevenLabs Brian, per format.json cuts.en).
# Resume is per-clip: batch.py skips any <id>.mp3 whose <id>.txt still matches
# lines.json, and REGENs the ones whose text changed. Add --only 5.6 6.7 to
# re-voice named lines; --force re-spends every credit.
# Relative cd (not absolute) so this still works after archive_cut.py moves the
# source into vault/videos/<slug>/src/ — see the gotcha in vault/CLAUDE.md.
cd "$(dirname "$0")/../../.."   # -> repo root (paths below are repo-relative)
python3 tools/tts/batch.py --project studio/videos/passive-income-number-en --cut en
