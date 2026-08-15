# review · passive-income-number · en · GATE TWO (assembled cut) · attempt 2
VERDICT: PASS
PASS 1: 0 blockers, 0 should-fix  (not this gate's checklist — every scene passed pass 1 on its chapter draft)
PASS 2: 0 blockers, 0 should-fix  (3 notes, all carried forward, none new to this render)

Master read: `studio/videos/passive-income-number-en/renders/FINAL-1080p-en.mp4`
— 527.914667s, 15837 frames, 1920x1080 @30, h264+aac, 796,775,507 B (759.9 MB).
Composition read: `studio/videos/passive-income-number-en-full/index.html` (81 scenes,
one 54,913 B merged inline script — was 4,514 B in round 1).

## 1 · The round-1 blocker is gone. Verified on the pixels, not the HTML.

Re-ran the exact five comparisons that proved it, master vs chapter draft at identical
relative times (master is absolute, drafts are chapter-local; offsets ch1 0 / ch2 46.42 /
ch3 151.938 / ch4 248.539 / ch5 335.817 / ch6 441.9 applied).

| scene | master t | draft t | round 1 (static) | round 2 (this render) |
|---|---|---|---|---|
| ch1 s2 chips | 4.100 | 4.100 | all three chips already up | **kicker only, no chips** — identical to draft, cascade arrives |
| ch1 s4 Lottie | 18.778 | 18.778 | `#s4l` an empty div, no banner | **banner present and drawn** — `$` notification, identical to draft |
| ch1 s6 ticks | 26.300 | 26.300 | 3 icons + 3 labels + 3 ticks up | **kicker only** — identical to draft |
| ch2 s16 count | 99.416 | 52.996 | static `95%`, 95 squares | **`88%`, 88 squares — mid-count**, identical to draft |
| ch4 s46 tank | 292.759 | 44.220 | tank already full | **part-filled at the draft's exact level** |
| ch6 s76 bars | 490.000 | 48.100 | 5 bars at final length | **4 bars part-grown, growing**, identical to draft |

Every one of the six is now pixel-equivalent to its chapter draft: mean |RGB diff| 1.2–1.8
of 255, and fewer than 1.1% of pixels differ by more than 16 (h264 ringing on type edges).

**Blocker 2 (ch1 s4's Lottie) specifically confirmed on the encode**, because it is the one
element whose absence leaves no other trace: the phone-notification banner is on the frame at
18.778s in the master, and `loadLottie("#s4l", window.L_phone_notify_credit_usd)` +
`playLottie(s4art, S.s4 + 1.13, 2.50)` are both in the merged script, once each.

**Blocker 3 (ch4's `--art-op` fallback) confirmed by measurement, not by eye.** s46's vessel
wall against its ground, sampled over the art band: master delta 55.3, draft delta 54.0 —
the logged 0.74 value (target ~57.0), not the `.30` fallback (39.7). The three markup-carried
`--art-op:0.74` (s10/s57/s61) also survive; `artOp` is defined once and called twice.

## 2 · Nothing regressed in the merge. No call landed on the wrong scene.

- **382 motion calls carried against 382 declared, per helper, not just in total.** Counted
  independently of `verify_motion` (comments and `//` stripped on both sides):
  ken 76, rise 154, pop 43, popEach 3, fade 48, draw 5, pulse 5, fill 4, exit 1,
  countUp 17, span 17, plateKen 8, playLottie 1. Zero short on every one.
- **Every one of the 382 calls fires inside its own scene's window.** Parsed each call's
  selector and its time argument out of the master and checked it against that scene's
  `data-start`/`data-duration`. **0 calls outside their window; 0 calls with an `S.sX + d`
  whose X is not the selector's scene; 0 calls that finish after their scene ends.** A
  misrebase is not a subtle error here — the smallest chapter offset is 46.42s against
  scenes of 5–9s, so any call rebased by the wrong offset would land tens of seconds outside
  its window. None does.
- `var S` matches `data-start` on all 81 sections to within 0.002s. No duplicate top-level
  declaration anywhere in the merged script. `sceneTransitions` 1, `register()` 1,
  RATE ASSERT 1, `var IDS`/`var S`/`var D` 1 each.
- **All 81 scenes compared master vs chapter draft on the encode.** 27 scenes at two offsets
  (0.25 and 0.70 of duration) plus the remaining 54 at mid-scene = 108 frame pairs. Worst
  divergence in the whole cut: 2.41% of pixels (s72, ch6). Nothing above 6%. No scene
  animates anything its chapter did not ask for, and no scene is missing anything its chapter
  did.

## 3 · The five joints still read as one deliberate transition with motion live — new info.

Sampled at −0.10 / +0.10 / **+0.225** / **+0.380** / +0.55 (both
`qa.dissolve_sample_offsets` plus three more) at every joint.

| joint | t | verdict with motion on both sides |
|---|---|---|
| ch1→ch2 s8→s9 | 46.42 | clean; incoming `START WITH THE RATE` rises at +0.38, headline still to come at +0.55 |
| ch2→ch3 s23→s24 | 151.938 | clean; incoming `RUNG TWO` rises at +0.38 |
| ch3→ch4 s39→s40 | 248.539 | clean; incoming `THE WORKED FIGURE` rises at +0.38 |
| ch4→ch5 s52→s53 | 335.817 | clean; incoming `THE TITLE QUESTION` rises at +0.38 |
| ch5→ch6 s68→s69 | 441.9 | clean; incoming `ONE MORE THING` rises at +0.38 |

The outgoing scene still fades monotonically to zero at all five; nothing paints at full
opacity over the incoming photograph. **And the joints are now provably the house transition,
not an assembly behaviour:** three within-chapter dissolves (s3→s4, s45→s46, s75→s76) sampled
in the master at the same two offsets are pixel-identical to the same dissolves in their
chapter drafts (mean diff 1.33–1.65, pct>16 ≤ 0.75%) and read exactly like the joints — same
ghosted outgoing headline at +0.38, same incoming kicker rising. In round 1 I could only say
this of two static scenes; with both sides animating it holds unchanged.

- **No black, no freeze in the new 527.9s encode.** `blackdetect d=0.2 pix_th=0.10` and
  `freezedetect n=-60dB d=1.0` re-run over the whole file (this is a *different* file from
  round 1, so it was re-run, not carried) — zero hits.
- Duration, frame count and stream layout are unchanged from the static render: 15837 frames,
  527.914667s, so the motion fix cost no runtime and moved nothing.
- Watermark single and full-opacity in all 25 joint frames and all 108 sweep frames.

## Findings
| # | pass | scene/span | severity | what | why it fails | fix |
|---|------|-----------|----------|------|--------------|-----|
| — | — | — | — | none | — | — |

## Notes (do NOT spend a render on these)
- **P2 · note · every dissolve in the cut.** Where two consecutive scenes carry a centred
  headline in the same vertical band, the 0.45s cross-fade leaves the outgoing sentence
  legible over the incoming scene for ~7 frames — b1 (s8/s9) and b4 (s52/s53) are the worst.
  Confirmed again this round, and confirmed again that it is identical in the chapter drafts,
  so it is the shipped house transition, not assembly. Logged in round 1, unchanged.
- **P2 · note · s75→s76 (485.6s).** New observation, same class: both scenes carry a green
  bar group in the same band, so the dissolve briefly shows two sets of bars at different
  lengths. Identical in the ch6 draft, so it passed chapter review; worth the same future
  design decision as the headline overlap (stagger the outgoing group out, or offset the
  incoming y). Not a rework.
- **P2 · note · `passive-income-number-en-PREVIEW.mp4` is still not this cut.** It is
  528.085s = the sum of the six chapter drafts, written 2026-08-12. Anyone reaching for a
  "creator already approved it" argument should reach for `FINAL-1080p-en.mp4` instead.

## Would I keep watching?
Yes, and this round I can say it about the file that ships. Every place I named in round 1 as
an attention risk was a symptom of the dead merge and is gone: **0:25–0:45** now has s6's
three costs ticking in on the words and s8's ladder line building rather than arriving whole,
and **8:05–8:20** (s75–s77) now has the bar groups growing in sequence instead of appearing
complete and simultaneous. I could not find a timestamp I would leave at. The two structural
cliffhangers still land — s39's kicker-only hand-off into `$5,000 A MONTH` at 248.5s, and
s68's `$7,271,759` into "It is not a settled number." at 441.9s — and the chapter joins are
invisible, which is exactly what they should be.

## Regressions vs my last pass
**None.** Everything round 1 verified numerically is still true and was re-verified on the new
encode where it could have changed: joints clean at both dissolve offsets, no black, no freeze,
watermark single and full-opacity, duration arithmetic exact (527.914667s / 15837 frames,
bit-for-bit the same timing as the static render), CSS scoping untouched. `sceneTransitions`,
the `+0.45` on the five chapter-final scenes and the `.ch<N>` prefixes all survived the fix —
those were the three things I asked the fix not to break, and it did not.

## What is working — do not break these
- The merge is now verifiable rather than trusted: `verify_motion` counts against the source
  and refuses to write a short master. I re-derived its 382/382 independently, per helper, and
  it agrees. That check is the reason this defect can never ship silently again — keep it.
- The evidence discipline on screen is the channel's asset and is intact: every corpus figure
  carries its rate in frame, every derived number carries `ILLUSTRATIVE ARITHMETIC`, every BLS
  figure carries agency + release date + series (s19, s25, s29, s66), both source papers are
  named with journal/volume/page (s13, s15), the limits are quoted verbatim with attribution
  (s34, s37), and s61 says out loud that the ratio is rounded. Nothing on screen overclaims.
  US $ throughout, no `₹` anywhere.
- Grade, type ladder and watermark are consistent end to end across all 81 scenes.
