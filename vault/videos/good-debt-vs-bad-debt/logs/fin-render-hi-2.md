# fin-render — good-debt-vs-bad-debt · cut hi · attempt 2 · invocation 1 (GATE-TWO FRAME CHECK, pre-encode / re-snapshot)

status: PASS (frame gate)
date: 2026-07-28
stage: gate two — frame-level QA before the orchestrator's 18-min encode. NO encode run here; no master exists yet. This invocation re-verifies the 5 backgrounds fin-assets re-sourced after the attempt-1 frame-gate FAIL.

## Scope
Attempt-1 failed 5 backgrounds (s2 Hindu-deity coin = revered-figure violation; s5 German legal text; s6 medieval-European gold; s7 Polish metallurgy book; s9 US road). fin-assets attempt-2 re-sourced all 5 in place (same filenames), index.html byte-unchanged. Re-ran the full 12-frame gate-two set at last-cue times, plus a full-resolution look at each of the 5 new raw source JPGs (grade can hide detail; raw pixels are the superset of what ships).

## What was inspected
- Inputs read: vault/CLAUDE.md, fin-render-hi-1.md (prior fail), fin-assets-hi-2.md (re-source), index.html, assets/img/manifest.json.
- 5 raw source JPGs at full res: s2, s5, s6, s7, s9 (content check — deity / demonetised note / foreign text / foreign scenery).
- 12 composited last-cue frames -> studio/videos/good-debt-vs-bad-debt-hi/snapshots/gate2-a2/ (times s): 19.5, 35.9, 58.8, 85.8, 100.5, 109.7, 130.7, 154.03, 157.5, 167.6, 175.6, 194.1. Two-phase scenes s5/s7/s8 captured in BOTH phases (phase A exits before the last cue).
- snapshot font load: "Fonts: 1 loaded" -> FinanceSans variable resolves; U+20B9 rupee + CSS arrow/triangle glyphs draw natively. --describe skipped (GEMINI_API_KEY unset); visual read done by hand per procedure.
- File integrity: the 5 changed .jpg have newer mtimes (21:58-22:27) than the 7 kept (20:17-20:46) -> consistent with an in-place re-source, wiring stable.

## The 5 re-sourced backgrounds — every attempt-1 defect resolved
- s2 [was HIGH / revered-figure] -> four rolled CURRENT legal-tender notes ₹10/₹20/₹50/₹100 on black. ₹ symbol on each; RBI seal is the Ashoka lion capital (national State Emblem, NOT a prophet/revered figure); portrait area = Mahatma Gandhi (national figure, standard on all INR, non-religious). NO multi-armed deity, NO halo/trishula, NO Persian/Nastaliq coin. None of these four denominations is demonetised (the withdrawn ₹2000 / old ₹500 are not present). CLEAN.
- s5 [was MED-HIGH / German] -> magnifier over a handwritten accounts ledger. Latin-script English cursive + bare figures + red/blue rule lines. NO German/Polish/foreign print; no currency symbol. On-keyword ("scrutinise the terms"). CLEAN.
- s6 [was LOW-MED / medieval gold] -> five ascending silver coin stacks (small->tall) on white. Edge-on milled coins, NO legible denomination / national marking / brand; not medieval, no crosses/Latin/fleur-de-lis. Currency-neutral money texture = authority-ladder endpoint. CLEAN.
- s7 [was MED-HIGH / Polish book] -> financial-calculator keypad macro. Key labels are ENGLISH (INV, LN, STO, DEPR, %, BRKEVN, 7-8-9 / 4-5-6, x, div). NO Polish text, NO legible brand (top row out of focus). CLEAN.
- s9 [was LOW / US road] -> green seedling in dark soil, soft bokeh. NO road/mailbox/geography, NO currency, NO text. Market-neutral, positive growth closer. CLEAN.
Net: no foreign-language text, no foreign/medieval imagery, no US/foreign scenery leaking onto the ₹ cut; no phone screens; no brand marks; all on-screen currency values INR (₹).

## Regression check — 7 kept scenes + hero integers + s1 split (all intact)
- s1 (kept bg): month-1 split PRESENT + arithmetically consistent -> YOU PAY ₹2,583 = INTEREST ₹1,667 + OFF THE DEBT ₹916; "IT'S A TRAP" stamp lands. No regression.
- s3 (kept s3/-cutA/-cutB): "TOOL THAT EARNS -> rent worth it" (green) / "DINNER, SALE BUY -> rent on a ghost" (red) legible; bag reads English "SHOPPING BAG". No regression.
- s4 (kept s4/-cut): two-column classifier fits inside safe area; GOOD (EDUCATION/A SKILL/A BUSINESS) vs BAD (CLOTHES/GADGETS/HOLIDAYS); "CARD REVOLVE = WORST". No regression.
- s7 HERO INTEGERS over the NEW keypad bg: LEGIBLE both phases -> "208 MONTHS · 17+ yrs", "still ₹40,044 owed", "INTEREST PAID ₹88,614"; phase-B punch "₹88,614 INTEREST > ₹50,000 BORROWED" clean. Dark panels give strong contrast over the keypad.
- s8 (kept alarm-clock, permitted per-scene grade override brightness 0.85): "DO THIS TODAY" + chips (OPEN CARD BILL -> PAY MINIMUM + ₹1,000 -> THIS MONTH) and phase-B rules legible. A blurred decorative card sits in the extreme bottom-left corner (outside the 110/150 safe padding) — pre-existing in this kept image, benign (not a face/figure/currency), accepted in attempt 1. No regression.
- s9 chips + "▶ SUBSCRIBE" CTA (CSS .tri triangle draws) legible over the seedling.

## Measured / verified (render-integrity — static, pre-encode)
- Scenes rendering: 9/9, no blank frames, no missing images (all s1-s9 bg + cut layers present; snapshot loaded every one).
- Root data-duration: 195.17 s (== attempt-1-verified timing.json total 195.17 s).
- Scene starts (s): 0, 22.141, 37.282, 61.278, 88.722, 112.691, 133.03, 159.586, 178.305.
- VO placement (static from HTML): every audio data-start == scene_start + 0.40 s for all 9 lines (0.4, 22.541, 37.682, 61.678, 89.122, 113.091, 133.43, 159.986, 178.705) -> consistent. Actual drift is an invocation-2 (post-encode) measure.
- Safe area: all scenes inside padding 110/150; s4 two-column and s7 3-row bill fit; no overflow/clipping.
- Contrast: PASS every scene (radial scrim + text-shadow). Softest element = s6 sub "Every extra rupee hits the principal directly" (muted gray over the graded white-ground coin shot) — still clearly legible; the standing grade (brightness 0.62) + scrim knocks the white ground down to muted gray-green, so NO blowout (fin-assets luminance-check confirmed; no grade override needed).

## Minor bookkeeping nit (NOT a gate issue, zero render impact)
manifest.json still records s2's query as "indian 2000 rupee note pink#2" — stale/misleading (a ₹2000 note would be demonetised), but the SHIPPED s2.jpg pixels are the rolled ₹10-100 notes and are clean. The render references the .jpg by filename, not the manifest, so no render effect. Flag for fin-assets to correct the ledger string; does not block.

## Deferred to invocation 2 (post-encode master QA — cannot run now; renders/FINAL-1080p-hi.mp4 does not exist yet)
faster-whisper re-transcribe + VO drift vs data-start table (target <=0.1 s); peak level (< -1 dBTP, ffmpeg astats/loudnorm read-only); blackdetect scan; actual runtime vs timing.json 195.17 s. Runtime / max VO drift / peak dBTP: N/A this invocation (no master).

## Verdict
FRAME GATE: PASS. All 5 re-sourced backgrounds clean (s2 revered-figure violation resolved; s5/s6/s7/s9 keyword-appropriate, no foreign text/imagery/scenery); no regression on the 7 kept scenes; s7 hero integers (208 MONTHS / ₹88,614) legible; s1 month-1 split intact. Cleared for the orchestrator's encode.

NEXT: orchestrator must run the render (PRODUCER_ENABLE_CHUNKED_ENCODE=true npm run render -- -q high --resolution 1080p --video-bitrate 12M) in its own background; then call fin-render invocation 2 for post-encode master QA.
