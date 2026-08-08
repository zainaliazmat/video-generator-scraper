#!/usr/bin/env bash
# Regenerate the en VO for japanese-money-methods (92 clips, ElevenLabs Brian).
# batch.py skips clips that already exist, so this is a free no-op once the cut
# is voiced — it just re-ffprobes and rewrites timing.json.
#
# One line changed?  python3 tools/tts/batch.py --project studio/videos/japanese-money-methods-en \
#                      --cut en --only 7.4      # 1 credit
# then run this script with no flags to rebuild timing.json from all 92 clips.
# KNOWN BUG (2026-08-01): --only also narrows the timing rebuild, so the --only
# run leaves a 1-entry timing.json and exits 1. The bare re-run above repairs it
# at zero cost. See vault/videos/japanese-money-methods/logs/fin-voice-en-3.md.
#
# --force redoes all 92 and re-spends 92 credits. Almost never what you want.
set -euo pipefail

# ponytail: repo root derived from this file, not hardcoded — the archived copy
# of a gen_vo script has to survive studio/ being deleted (vault/CLAUDE.md §5).
cd "$(dirname "$(readlink -f "$0")")/../../.."

python3 tools/tts/batch.py --project studio/videos/japanese-money-methods-en --cut en
