# fin-render — good-debt-vs-bad-debt · cut hi · attempt 1 · invocation 1 (GATE-TWO FRAME CHECK, pre-encode)

status: FAIL (frame gate)
date: 2026-07-28
stage: gate two — frame-level QA before the orchestrator's 18-min encode. No encode run here; no master exists yet.

## What was inspected
- Inputs read: vault/CLAUDE.md, index.html, assets/voice/timing.json, assets/img/manifest.json.
- 12 fresh last-cue frames snapshotted to studio/videos/good-debt-vs-bad-debt-hi/snapshots/gate2/
  (one+ per scene; two-phase scenes s5/s7/s8 captured in BOTH phases since phase A exits before the last cue).
  Times (s): 19.5, 35.9, 58.8, 85.8, 100.5, 109.7, 130.7, 154.03, 157.5, 167.6, 175.6, 194.1
- 2 high-density (3x) zoom proofs: snapshots/gate2/zoom/frame-00-at-154.03s.png (s7 bill),
  snapshots/gate2/zoom-s2/frame-00-at-35.9s.png (s2 coin).
- snapshot font load: "Fonts: 1 loaded" every run — FinanceSans variable resolves; U+20B9 rupee and weights render natively.

## Measured / verified (render-integrity numbers — the artifact)
- Scenes rendering: 9 / 9, no blank frames, no missing images (all s1-s9 bg + cut layers present).
- Root data-duration: 195.17 s  ==  timing.json total: 195.17 s  -> MATCH.
- VO placement (static, from HTML/timing.json; actual drift is an invocation-2 post-encode measure):
  every audio_start == scene_start + 0.40 s for all 9 lines (0.4, 22.541, 37.682, 61.678, 89.122,
  113.091, 133.43, 159.986, 178.705) -> consistent.
- Safe area: all scenes inside padding 110/150; s4 two-column classifier fits; no overflow/clipping.
- Contrast: PASS every scene (radial scrim + text-shadow); all text legible over the grade.
- Brand marks: none. Phone screens: none. On-screen currency VALUES: all INR (rupee) and correct.
- s1 month-1 split: PRESENT and arithmetically consistent -> YOU PAY 2,583 = INTEREST 1,667 + OFF THE DEBT 916.
- s7 hero integers: LEGIBLE (full-frame + zoom) -> "208 MONTHS . 17+ yrs", INTEREST PAID "88,614",
  "still 40,044 owed"; phase-B punch "88,614 INTEREST > 50,000 BORROWED" clean.
- Arrows/triangle/rupee glyphs (CSS .arr/.arrow/.tri + font) all draw correctly.

## Findings (why FAIL) — b-roll fails the keyword-match rule; s2 breaches the revered-figure rule
- s2.jpg [HIGH] keyword "indian rupee coins" -> actually an ANTIQUE DEVOTIONAL COIN depicting a HINDU
  DEITY (multi-armed, haloed nimbus, trishula/trident, tiger-or-lion mount, serpent) + a 2nd coin with
  Persian/Nastaliq script. Confirmed via zoom. This is a likeness of a revered religious figure (violates
  the #1 visual rule), tone-deaf under the "MINIMUM = A TRAP / most dangerous words" framing, and not
  currency at all. Must not ship.
- s5.jpg [MED-HIGH] keyword "printed bank statement" -> GERMAN corporate-law book text
  ("Gesellschaftsvertrag", "Beschraenkte Nachschusspflicht") under a magnifier. Foreign, off-market, legible.
- s7.jpg [MED-HIGH] keyword "scientific calculator on dark table" -> calculator resting on a POLISH
  metallurgy textbook (legible "Rys. 2 | Histogramy... z polskich hut... EPSTAL", "granica plastycznosci")
  with a visible histogram chart intruding into the money-math scene.
- s6.jpg [LOW-MED] keyword "gold coins" -> medieval EUROPEAN gold coins (crosses/fleur-de-lis/Latin), non-INR.
- s9.jpg [LOW] keyword "empty open country road" -> US-style road (yellow centerline + roadside mailbox).

Composition logic, layout, timing, on-screen copy and all computed integers are GOOD — this is an
asset-only defect (re-source the backgrounds), not a build/logic rebuild.

## Deferred to invocation 2 (post-encode master QA — cannot run now, no renders/FINAL-1080p-hi.mp4)
faster-whisper re-transcribe + VO drift vs data-start (target <=0.1 s); peak level (< -1 dBTP);
blackdetect scan; actual runtime vs timing.json 195.17 s.

## Verdict
FRAME GATE: FAIL. Render integrity sound; b-roll mismatched and s2 shows a revered figure. One build
retry remains; a second bad frame set is terminal for the cut.

NEXT: fin-build must re-source the mismatched backgrounds (priority s2 Hindu-deity coin -> modern Indian
rupee coins/notes; then s5 German -> Indian/English statement, s7 Polish-book -> plain calculator/desk,
s6 medieval gold -> generic gold, s9 US road -> neutral road), then re-snapshot for gate two.
