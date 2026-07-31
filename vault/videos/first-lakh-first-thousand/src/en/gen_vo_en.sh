#!/usr/bin/env bash
set -euo pipefail
# Repo root is three levels up from this script (studio/videos/<slug>-<cut>/).
# ponytail: relative, not an absolute cd — the vault's finished-video rule notes
# that hardcoded studio paths die when the project is archived.
cd "$(dirname "${BASH_SOURCE[0]}")/../../.."
python3 tools/tts/batch.py --project studio/videos/first-lakh-first-thousand-en --cut en
