# review · passive-income-number · en · GATE TWO (assembled cut) · attempt 1
VERDICT: REWORK
PASS 1: 3 blockers, 0 should-fix
PASS 2: 0 blockers, 2 notes

Master read: `studio/videos/passive-income-number-en/renders/FINAL-1080p-en.mp4`
(527.915s, 15837 frames, 1920x1080, h264+aac).
Composition read: `studio/videos/passive-income-number-en-full/index.html` (81 scenes).

## What the boundaries themselves say (the job I was called for)

All five chapter joints were sampled at **-0.30 / -0.10 / +0.10 / +0.225 / +0.38 / +0.60**
(both `qa.dissolve_sample_offsets`, plus four more), and ch4->ch5 was additionally read
**frame by frame, 18 consecutive frames** across the whole 0.45s overlap.

| joint | t | verdict |
|---|---|---|
| ch1->ch2 s8->s9 | 46.42 | clean dissolve |
| ch2->ch3 s23->s24 | 151.938 | clean dissolve |
| ch3->ch4 s39->s40 | 248.539 | clean dissolve |
| ch4->ch5 s52->s53 | 335.817 | clean dissolve |
| ch5->ch6 s68->s69 | 441.9 | clean dissolve |

- **No outgoing layer survives over the incoming photograph.** The outgoing scene fades
  monotonically to zero across the overlap at all five joints; nothing paints at full
  opacity on top of the next scene. The 2026-08-01 `japanese-money-methods` stacking-context
  defect is **not** present.
- **No black, no freeze anywhere in the file.** `blackdetect d=0.2 pix_th=0.10` and
  `freezedetect n=-60dB d=1.0` over all 527.9s returned zero hits.
- **Watermark is single, full-opacity and pixel-identical at every dissolve midpoint** —
  cropped and compared at all five joints against a settled frame. Never doubled, never dimmed.
- **No CSS leak.** The assembled `<style>` has 18 rules; the 13 chapter rules are all
  prefixed `.ch1/.ch2/.ch3/.ch5`, and the 5 unscoped ones are the shared design-system
  `#root` and the four archetype plate rects `.p-a`-`.p-d`, identical in every chapter.
  ch4 and ch6 contributed no CSS. A leak is structurally unavailable.
- **Assembly arithmetic is exact.** Chapter root durations 46.42 + 105.518 + 96.601 + 87.279
  + 106.084 + 85.973 = 527.875 = the master root. Each chapter starts precisely where the
  previous one's root ended, and exactly the five chapter-final scenes (s8, s23, s39, s52,
  s68) gained the +0.45 overlap. No runtime added, none lost.

**So the boundaries are fine. The thing that is wrong is one file wide, and it only exists
in the assembled composition — which is why it belongs to this gate.**

## Findings
| # | pass | scene/span | severity | what | why it fails | fix |
|---|------|-----------|----------|------|--------------|-----|
| 1 | P1 | ALL 81 scenes | blocker | Every chapter's per-scene motion script was dropped at assembly. The assembled `index.html` has ONE inline script (4514 B) containing only `var S` / `var D` / `var IDS`, `sceneTransitions(IDS, S)`, the rate assert and `register()`. `loadLottie`=0, `playLottie`=0, `plateKen`=0, `cue(`=0, `fade(`=0, `draw(`=0, `tl.`=0 occurrences. Each chapter file carries TWO inline scripts (ch1 4362+2503 B, ch5 13286+4417 B …); only the second, the rate assert, survived. | Not one cue lands anywhere in the cut. Every stack is fully painted from its scene's first frame, so no line arrives on its word, no number counts, no drawn layer builds. Verified against the chapter drafts at identical timestamps: **ch1 s2** cascade — master has all three chips at 4.10s and they never move, draft brings them in at ~5.2 / ~5.8 / ~6.3s; **ch1 s6** — master shows three icons, three labels and three ticked checkboxes at 26.30s, draft shows nothing yet; **ch2 s16** — master reads a static `95%` with 95 squares filled at +4.19, draft is mid-count at `88%`; **ch4 s46** — master's tank is already full at 44.22s, draft's level is still low and rising; **ch6 s76** — master has the whole text stack and all five bars at final length, draft has no text and three bars part-grown. | Root cause is `tools/cut_assemble.py:184`: `script = html[html.rindex("<script>")…]` takes the **last** inline script, which in every chapter project is the rate-assert block, not the motion timeline. Select the inline `<script>` that contains `var IDS`/`sceneTransitions` and lift the motion from that one; keep `take_rate_assert` doing its own job. Re-assemble and re-render the draft. (`rebase_motion(ln, -offset)` is correct — it adds the offset back to absolute literals; `S.sN + x` forms need nothing. No `const` collides across the six chapters — only ch4 emits `function artOp`, once.) |
| 2 | P1 | s4 (ch1) | blocker | The chapter's declared drawn layer — the phone-notification Lottie — never loads. `<div id="s4l">` and `<script src="assets/lottie/phone_notify_credit_usd.js">` are both in the assembled file, but `loadLottie(...)` / `playLottie(...)` are not, so `#s4l` renders as an empty div. The composition's own guard (`if (!window.L_phone_notify_credit_usd) throw`) was dropped with them, so nothing errors. | This is the silent-blank Lottie mode exactly. The scene's photograph is deliberately a phone with a DARK screen (fin-assets deviation 1) precisely so the picture cannot claim money arrived — the banner was the only element on the frame that states it. In the master, the payoff of chapter 1's what-if is a bare photo with a headline. Confirmed on the encode: master at 18.778s has no banner, ch1 draft at the same 18.778s has it. | Falls out of finding 1 — but re-verify this one specifically on the new draft, at 18.778s, on the ENCODE, because it is the one element whose absence leaves no other trace. |
| 3 | P1 | s46, s49 (ch4) | blocker | ch4's two drawn layers are driven by `artOp()`, which tweens `--art-op` from 0 to `ART_OP` 0.74. That call went with the script, so `--art-op` is never written and the layers fall back to `chapter-design.css`'s `.has-photo .art { opacity: var(--art-op, .30) }`. | The 2026-08-12 pre-assembly ruling — scrim transmits ~38%, so drawn ink ships at 0.74, measured s46 vessel wall rgb 90 on gnd 31, ΔRGB 39.7 -> 57.0 — **is not in the file that ships**. ch2 s10 and ch5 s57/s61 are safe: they carry `style="--art-op:0.74"` in markup, which survived. ch4 was the one chapter that needed a script edit and it is the one that lost it. | Same fix. On the new draft, measure s46's vessel wall at 292.759s (= ch4-local 44.22s) and confirm it lands at the logged 0.74 value, not the .30 fallback. |

## Notes (not blockers, do not spend a render on them)
- **P2 · every dissolve in the cut, not just the joints.** Where two consecutive scenes both
  carry a centred multi-line headline in the same vertical band, the 0.45s cross-fade puts
  both sentences on top of each other for ~7 frames (0.23s) — b1 (s8/s9) and b4 (s52/s53) are
  the worst, and the outgoing headline is still legible at +0.38. This is **not** an assembly
  artifact: I sampled three within-chapter dissolves (s3->s4, s45->s46, s63->s64) in both the
  master and the chapter drafts and the behaviour is identical, so it is the shipped house
  transition and it was in every chapter draft. In motion it reads as a smear, not as text.
  Worth a design decision for a future cut (stagger the headline out before the scene ends,
  or offset the incoming stack's y), never a rework of this master.
- **P2 · the creator's sign-off does not cover this artifact, and nobody should think it does.**
  `passive-income-number-en-PREVIEW.mp4` is 528.085s = the exact sum of the six chapter draft
  renders (46.443+105.536+96.640+87.317+106.112+86.037), and it was written 2026-08-12 05:41,
  three days before `full/index.html` was generated (2026-08-15 05:19). It is a concatenation
  of the six chapter drafts — which still have all their motion — not a render of the
  assembled composition. FRAMES.png is stills, and stills cannot show a missing arrival.
  That is precisely how findings 1-3 reached this gate: **there was no artifact in which they
  were visible until this encode existed.**

## Would I keep watching?
Yes on the argument, and the joints themselves give me no reason to leave — s39's kicker-only
hand-off into `$5,000 A MONTH` and s68's `$7,271,759` into "It is not a settled number." are
both real cliffhangers, and the chapter joins are invisible, which is what they should be.
But the cut currently plays as **81 static slides that cross-dissolve**. Attention is at risk
first around **0:25-0:45**, where s6's three-cost count and s8's ladder line both land as
fully-formed tableaux with nothing arriving on the words, and again at **8:05-8:20** (s75-s77),
where three bar groups appear complete and simultaneous instead of building. Neither is a
picture problem — it is finding 1, everywhere.

## Regressions vs my last pass
n/a, attempt 1 (gate two).

## What is working — the next pass must not break these
- The five chapter joints, the durations arithmetic and the CSS scoping are correct and were
  verified numerically, not by eye. A fix to the motion lift must not touch `sceneTransitions`,
  the `+0.45` on the five chapter-final scenes, or the `.ch<N>` prefixes.
- The evidence discipline on screen is genuinely good and is the channel's asset: every corpus
  figure carries its rate in frame, every derived number carries `ILLUSTRATIVE ARITHMETIC`,
  every BLS figure carries agency + release date + series (s19, s25, s29, s66), the two source
  papers are named with journal, volume and page (s13, s15), the limits are quoted verbatim
  with attribution (s34, s37), and s61 says out loud that the ratio is rounded because it is a
  quotient of two soft decimals. Nothing on screen overclaims. US $ throughout; no `₹` anywhere.
- The watermark, the grade and the type ladder are consistent end to end.
