#!/usr/bin/env bash
# Serial VO generation — one kokoro line at a time (the shared engine's
# Promise.all exhausts RAM with 50 parallel model loads). Skips existing wavs.
set -uo pipefail
export PATH="/home/zain-ali/.nvm/versions/node/v22.18.0/bin:/usr/local/bin:/usr/bin:/bin"
unset VIRTUAL_ENV
HF=/home/zain-ali/Documents/ClaudeHyperFrame
V2=$HF/videos/video-02-claude-edits-video
cd "$V2"
mkdir -p assets/voice /tmp/vo-lines

node -e '
const r = require("./audio_request.json");
for (const l of r.lines) require("fs").writeFileSync("/tmp/vo-lines/"+l.id+".txt", l.text);
console.log(r.lines.length + " line files written");
'

ok=0; fail=0
for f in /tmp/vo-lines/*.txt; do
  id=$(basename "$f" .txt)
  out="assets/voice/$id.wav"
  if [ -s "$out" ]; then echo "[$id] exists — skip"; ok=$((ok+1)); continue; fi
  if (cd "$HF" && npx hyperframes tts "$f" --voice bm_george --output "videos/video-02-claude-edits-video/$out" >/dev/null 2>&1) && [ -s "$out" ]; then
    echo "[$id] ok"; ok=$((ok+1))
  else
    echo "[$id] FAILED"; fail=$((fail+1))
  fi
done
echo "done: $ok ok, $fail failed"

# Rebuild audio_meta.json from what exists (id, path, ffprobe duration)
node -e '
const { execSync } = require("child_process");
const fs = require("fs");
const req = require("./audio_request.json");
const voices = [];
let total = 0;
for (const l of req.lines) {
  const p = "assets/voice/" + l.id + ".wav";
  if (!fs.existsSync(p)) continue;
  const d = parseFloat(execSync(`ffprobe -v error -show_entries format=duration -of csv=p=0 "${p}"`).toString());
  voices.push({ id: l.id, path: p, duration_s: Math.round(d * 1000) / 1000, words: [] });
  total += d;
}
fs.writeFileSync("./audio_meta.json", JSON.stringify({
  tts_provider: "kokoro", voice_id: "bm_george", bgm: null, bgm_pending: false,
  voices, sfx: [], total_duration_s: Math.round(total * 1000) / 1000
}, null, 2));
console.log("audio_meta.json: " + voices.length + " voices, " + Math.round(total) + "s total");
'
