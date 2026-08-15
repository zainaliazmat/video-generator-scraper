# fin-voice-en attempt 1 — tools/tts/prepare.py

## Ran
cost guard, slice, `/home/zain-ali/Documents/YoutubeScraper/tools/tts/batch.py --project /home/zain-ali/Documents/YoutubeScraper/studio/videos/financial-freedom-after-50-en --cut en`

## Failed
nothing

## Evidence
123 VO lines sliced from script-en.md, 12,288 chars, 1.04× the 11,814-char budget (ceiling 1.3×); batch.py exit 0. Postconditions (clip bytes, ffprobe duration vs chars, silence, scene arithmetic) are asserted by `pipeline_check check voice`.

## Changed
lines.json, timing.json, the clips, gen_vo_en.sh

## Owed
nothing
