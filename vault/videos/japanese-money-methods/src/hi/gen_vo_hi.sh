#!/usr/bin/env bash
# Regenerate the hi VO for japanese-money-methods (92 clips, ElevenLabs Harsh).
# batch.py skips clips that already exist. To redo ONE line after a script edit:
#   python3 tools/tts/batch.py --project studio/videos/japanese-money-methods-hi \
#     --cut hi --only 7.4
# --force redoes all 92 and re-spends the credits for every one of them.
set -euo pipefail

# ponytail: repo root derived from this file, not hardcoded — the archived copy
# of a gen_vo script has to survive studio/ being deleted (vault/CLAUDE.md §5).
cd "$(dirname "$(readlink -f "$0")")/../../.."

python3 tools/tts/batch.py --project studio/videos/japanese-money-methods-hi --cut hi
