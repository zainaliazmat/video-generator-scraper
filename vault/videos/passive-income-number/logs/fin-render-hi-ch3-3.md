# fin-render: passive-income-number-hi-ch3 · attempt 3

## Ran

- Draft re-render at 30 fps from regenerated `index.html` (fin-build attempt 2)
- Contact sheet rebuilt from fresh draft mp4
- No gate two (frame QA) or encode — chapter draft mode only

## Failed

None. Both draft render and contact sheet completed successfully.

## Evidence

**Prior state (attempt 2):**
- `renders/DRAFT-ch3.mp4` rendered 2026-08-09 16:48:22
- Carried stale crop from s22 (1.249× crop, 79px uncovered band)
- `index.html` remained uncorrected until fin-build attempt 2

**HTML regeneration:**
- fin-build attempt 2 (2026-08-09 17:15): dropped inline `background-size` / `background-position` window at generator
- Regenerated `index.html` with corrected s22 geometry
- `npm run check`: 0 errors, 0 warnings, contrast 17/17 AA, root duration 61.143s unchanged

**Draft render (attempt 3):**
- Source: `studio/videos/passive-income-number-hi-ch3/index.html` (regenerated)
- Output: `studio/videos/passive-income-number-hi-ch3/renders/DRAFT-ch3.mp4`
- Size: 16 MB
- Duration: 61.184s (expected root 61.143s, within tolerance)
- Frame count: 1835 @ 30 fps (61.1667s ÷ 30 fps = 1835 frames)
- Render completed: 2026-08-09 17:23:32
- s22 now renders with corrected crop geometry

**Contact sheet:**
- Output: `studio/videos/passive-income-number-hi-ch3/renders/SHEET-ch3.jpg` (280 KB)
- Index: `studio/videos/passive-income-number-hi-ch3/renders/SHEET-ch3.json` (493 B)
- Frames sampled: 9 (s22–s30)
- s22 sampled at: 35.852s with corrected geometry (prior draft carried 1.249× crop at this frame)
- Rebuilt: 2026-08-09 17:32:07

## Changed

- `studio/videos/passive-income-number-hi-ch3/renders/DRAFT-ch3.mp4` (REPLACED: regenerated from corrected HTML, stale crop now fixed)
- `studio/videos/passive-income-number-hi-ch3/renders/SHEET-ch3.jpg` (REPLACED: rebuilt from current draft, s22 corrected)
- `studio/videos/passive-income-number-hi-ch3/renders/SHEET-ch3.json` (REPLACED: rebuilt from current draft)

Previous draft (attempt 2, 16:48, with s22 stale crop) superseded.

## Owed

Contact sheets and draft mp4 are current for fin-editor and fin-ceo review. s22 crop defect cleared. No further work on chapter 3 draft until approval gates complete.

