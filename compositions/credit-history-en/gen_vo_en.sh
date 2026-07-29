#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../../.."
python3 tools/tts/batch.py --project studio/videos/credit-history-en --cut en
