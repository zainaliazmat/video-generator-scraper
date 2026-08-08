---
summary: en chapter 2 DRAFT render + contact sheet. 3166/3166 frames, CFR 30, zero black, per-scene p90 luma curve and all 14 joint measurements for the editor/CEO gate. Three fin-build flags measured, none ruled.
updated: 2026-08-08
source: measured from studio/videos/passive-income-number-en-ch2/renders/DRAFT-ch2.mp4 (mtime 2026-08-08 11:27:24)
---

# fin-render · passive-income-number · en · ch2 · attempt 1

**MODE: CHAPTER DRAFT** (orchestrator §3b step 4). Gate two was NOT run and no
encode was run. Two review artifacts produced; everything below is measured from
the draft encode, not from the source.

## Commands run

```
npx hyperframes render . -c index.html -o renders/DRAFT-ch2.mp4 -q draft -f 30
python3 tools/chapter_sheet.py studio/videos/passive-income-number-en-ch2 \
        studio/videos/passive-income-number-en-ch2/renders/DRAFT-ch2.mp4 \
        -o studio/videos/passive-income-number-en-ch2/renders/SHEET-ch2.jpg
```

No `--resolution`, no `--gpu`, no `--video-bitrate`, no chunked encode. Render
took 6m13.2s (capture 5m52.3s, assemble 1.2s), 1 worker, captureMode `beginframe`.

## Artifacts

| Path | Bytes | mtime |
|---|---|---|
| `studio/videos/passive-income-number-en-ch2/renders/DRAFT-ch2.mp4` | 24,950,478 | 11:27:24 |
| `studio/videos/passive-income-number-en-ch2/renders/SHEET-ch2.jpg` | 410,487 | 11:30 |
| `studio/videos/passive-income-number-en-ch2/renders/SHEET-ch2.json` | 876 | 11:30 |

Freshness confirmed by mtime against wall clock at probe time (11:27:44) — the
file measured is the file just rendered. `SHEET-ch2.json` carries 16 entries
(15 scenes + s10's second framing) for the orchestrator's cross-chapter PNG.

## 1 · Frame count, duration, CFR — PASS

| Quantity | Expected | Measured |
|---|---|---|
| frames | ceil(105.518 x 30) = **3166** | **3166** (`nb_read_frames`, full decode) |
| video duration | 3166/30 = 105.5333s | **105.533333s** |
| container duration | — | 105.536000s (audio 105.536000s, aac 48kHz stereo) |
| `r_frame_rate` / `avg_frame_rate` | 30/1 | **30/1 / 30/1** |
| resolution | — | 1920x1080, h264, 1.89 Mb/s |

Renderer's own log agrees: `totalFrames 3166, framesCompleted 3166`, zero dropped.

**CFR verified from packet timestamps, not from the fps tag.** All 3165 inter-packet
deltas take exactly two values — `0.033333` (2110x) and `0.033334` (1055x) — which is
1/30 expressed in the 90kHz timebase, alternating to keep the rational exact. No
third delta, no duplicated or dropped PTS. First packet 0.0, last 105.5. Genuine CFR,
so the chapter's frames will sum with its siblings and no drift is introduced at the
joints.

## 2 · Black-segment scan — PASS, zero

- `blackdetect=d=0.05:pic_th=0.98:pix_th=0.10` → **0 segments** (no filter output at all).
- `blackframe=amount=95:threshold=32` → **0 frames**.

Both run over the whole 105.5s. Nothing anywhere, and specifically nothing in the
first half — see §5, this is the measurement that settles the overlay-count flag.

## 3 · Per-scene luminance — the real curve for the CEO gate

Method: decoded once to 192x108 greyscale at a 10fps grid (1055 samples). Each scene
measured over its BODY only — `start + 0.45` to `end - 0.45` — so no dissolve frames
contaminate a scene's own reading. Percentiles are of the pooled pixels of every
sample in that window.

| scene | body (s) | samples | p10 | p50 | **p90** | mean |
|---|---|---|---|---|---|---|
| s9  (2.1 open) | 0.00–5.16 | 52 | 21 | 46 | **57** | 44.0 |
| s10 (2.2) | 5.61–15.76 | 101 | 18 | 28 | **44** | 32.2 |
| s11 (2.3) | 16.21–23.93 | 77 | 18 | 37 | **53** | 38.1 |
| s12 (2.4) | 24.37–27.78 | 34 | 21 | 27 | **47** | 33.3 |
| s13 (2.5) | 28.23–34.67 | 64 | 16 | 46 | **57** | 44.7 |
| s14 (2.6) | 35.12–41.74 | 66 | 24 | 31 | **40** | 36.4 |
| s15 (2.7) | 42.19–48.81 | 67 | 23 | 37 | **53** | 39.6 |
| s16 (2.8) | 49.26–55.17 | 59 | 16 | 34 | **55** | 34.6 |
| s17 (2.9) | 55.62–62.66 | 70 | 24 | 32 | **46** | 36.7 |
| s18 (2.10) | 63.11–70.28 | 71 | 19 | 35 | **51** | 36.1 |
| s19 (2.11) | 70.73–76.82 | 61 | 17 | 39 | **59** | 39.3 |
| s20 (2.12) | 77.27–84.31 | 71 | 15 | 23 | **35** | 25.5 |
| s21 (2.13) | 84.76–90.39 | 56 | 15 | 25 | **44** | 28.5 |
| s22 (2.14) | 90.84–97.77 | 69 | 15 | 33 | **46** | 33.5 |
| s23 (2.15) | 98.22–105.52 | 72 | 16 | 30 | **44** | 31.5 |

**fin-build's claim is accurate.** It reported p90 57 at the open and a chapter range
of 35–60. Measured: open **57.0**, range **35.0–59.0**. Within one unit on the top end.

**But the CEO should read the shape, not the two endpoints.** Duration-weighted, by
tonal segment:

| segment | dur (s) | p90 range | p90 dur-wtd | mean dur-wtd |
|---|---|---|---|---|
| amber head s9–s11 | 25.27 | 44–57 | 50.0 | 36.8 |
| C evidence run s12–s15 | 26.68 | 40–57 | 49.5 | 39.1 |
| amber verdict s16–s17 | 14.75 | 46–55 | 50.2 | 35.7 |
| green method + bill s18–s20 | 23.00 | 35–59 | 47.9 | 33.4 |
| green corpus close s21–s23 | 22.11 | 44–46 | 44.7 | 31.3 |
| **whole chapter** | **105.52** | **35–59** | **48.4** | **35.4** |

Three things this says that the endpoints do not:

1. **The lighter open is real but it is 5.16s long.** s9 is p90 57; s10 immediately
   drops to 44, which is inside ch1's own band. The requirement "open measurably
   LIGHTER" is met at the literal opening scene (+12 p90 against ch1's ~45). Whether
   that satisfies the intent, or whether the intent was a lighter CHAPTER, is the
   CEO's call — because:
2. **The chapter as a whole sits at ch1's ceiling, not above it.** Duration-weighted
   p90 48.4 against ch1's reported band of 36–48. The last 30s weighs 42.1, inside
   ch1's band.
3. **What ch2 genuinely has that ch1 did not is an ARC.** Range span 24 (35–59)
   against ch1's 12 (36–48), and the segment curve descends 50.0 → 49.5 → 50.2 →
   47.9 → 44.7 into the green close. ch1 was one band; ch2 is a slope with a spike
   at the front. The brightest scene is s19 (59) at 70s, not the open.

**A lever, if the CEO wants more.** The p10 floor is 15–24 on all fifteen scenes —
essentially constant. Every bit of the tonal variation lives in the highlights; the
shadows are pinned by `.scrim`'s four stacked gradients. If the chapter needs to READ
lighter rather than merely peak lighter, the control is the scrim floor, not the
photographs.

## 4 · The fourteen joints

Method: `scdet=threshold=0` over all 3166 frames; peak score in `start-0.10 .. start+0.55`
(the 0.45s overlap plus a frame of margin either side). Luminance step is the outgoing
scene's last 0.8s before the overlap against the incoming scene's first 0.8s after it,
so neither figure contains a blended frame.

| joint | at (s) | scdet peak | @t | dp90 | dmed |
|---|---|---|---|---|---|
| s9→s10 | 5.162 | 0.179 | 5.500 | **−15** | −17 |
| s10→s11 | 15.758 | 0.167 | 15.833 | +9 | +11 |
| s11→s12 | 23.924 | 0.149 | 24.000 | −7 | −10 |
| s12→s13 | 27.781 | **0.243** | 27.900 | +8 | **+19** |
| s13→s14 | 34.667 | 0.198 | 34.767 | **−18** | −15 |
| s14→s15 | 41.737 | 0.210 | 41.667 | +12 | +6 |
| s15→s16 | 48.806 | 0.202 | 49.033 | −9 | −4 |
| s16→s17 | 55.170 | 0.172 | 55.300 | −12 | −2 |
| s17→s18 | 62.658 | **0.137** | 62.867 | +2 | +2 |
| s18→s19 | 70.276 | 0.226 | 70.567 | +8 | +6 |
| s19→s20 | 76.822 | 0.173 | 77.100 | **−23** | −14 |
| s20→s21 | 84.310 | 0.200 | 84.600 | +7 | +3 |
| s21→s22 | 90.387 | 0.138 | 90.667 | +1 | +7 |
| s22→s23 | 97.769 | 0.147 | 97.900 | −3 | −4 |

Plus the one in-scene framing swap: **s10 `fade(#s10-bg2)` @11.972, 0.40s** — peak
0.181, mean 0.027. Indistinguishable from a joint by score, which is the intent
(§6a resolves the 10.6s breach as a real dissolve, and it earns its own `transition`
cue in `audio.json`).

**scdet cannot rank these joints and the editor should not let it try.** The joint
peaks span 0.137–0.243. The in-scene motion floor is 0.011 mean, but its spikes reach
**0.482 @ 35.800** (s14's statement `rise` at +1.10), 0.358 @ 100.000, 0.326 @ 73.533.
Every text rise in this chapter scores HIGHER than every cross-dissolve, because a
0.45s dissolve spreads its change over 13 frames while a `rise` lands in ~4. So no
joint reads as a hard cut mechanically, and the hi ch1 s3→s4 lesson applies in full:
the number will not find the defect. What follows is what each joint SHOWS.

### Joints worth the editor's eye

- **s19→s20 @76.822 · peak 0.173 · dp90 −23 (the chapter's largest) · dmed −14.**
  OUT: an egg carton and leafy greens on a dark table, amber-graded — the BRIGHTEST
  scene in the chapter (p90 59). IN: a grocery bag with lettuce and a yellow pepper on
  a plaid cloth — the DARKEST scene in the chapter (p90 35). **Same subject matter
  (produce), back to back, with the biggest light step in the chapter.** The risk here
  is the inverse of s3→s4's: not "two pictures", but "one place where someone turned
  the lights off". Storyboard §7 claims s19 "owns 'food' without borrowing s20's bag
  or s21's loaf"; the two frames are distinguishable, but they are the closest pair in
  the chapter and they are adjacent. Editor's ruling.
- **s9→s10 @5.162 · 0.179 · dp90 −15 · dmed −17.** OUT: a blank kraft notebook page
  and a sharpened pencil, flat overhead, near-white, the chapter's bright open. IN: a
  row of brass taps on a steel manifold, deep shallow-DOF row, dark industrial. Shares
  the amber grade and the tint and **nothing else** — no object, no depth (flat-lay to
  receding row), no light direction. This is structurally the same shape the editor
  ruled two pictures on hi ch1 s3→s4, and it is the joint that spends the chapter's
  tonal opening. Editor's ruling.
- **s13→s14 @34.667 · 0.198 · dp90 −18 · dmed −15.** OUT: an open book, macro, bright
  page block filling the frame, warm. IN: a wall of card-catalogue drawers with one
  pulled out, deep receding perspective, cool grey. Subject carries (paper records),
  depth and colour temperature both invert. Second-largest p90 drop.
- **s12→s13 @27.781 · 0.243 (highest peak) · dp90 +8 · dmed +19 (largest median step).**
  OUT: two blank grey sheets on dark walnut, flat overhead, geometric. IN: an open book,
  macro, bright. The §7 C-run intent is that the ARTEFACT changes while the layout
  holds; that holds, but the scale jumps flat-wide → macro and the median light jumps
  +19 in one dissolve. Highest-scoring joint in the chapter on both metrics.
- **s17→s18 @62.658 · 0.137 (the gentlest joint) · dp90 +2 · dmed +2.** OUT: a wooden
  box of rubber type stamps, amber, overhead. IN: a hand writing on a kraft tag, and
  **the green grade begins**, with the drawn division-block arriving under the type.
  The numbers say almost nothing happens here; semantically it is the biggest step in
  the chapter (finding → method, amber → green). Worth confirming the green reads as
  an arrival rather than a drift, precisely because no measurement will flag it.

### The other nine, briefly

s10→s11 (0.167, +9): brass taps tight crop → a rusted nail through a weathered plank.
Both shallow-DOF macros of aged metal against wood, light from the same side; coherent.
s11→s12 (0.149, −7): nail macro → two blank sheets on walnut. Macro-organic to flat
graphic, and the chapter's first de-role (amber → neutral); low score because both are
low-detail. s14→s15 (0.210, +12): drawers → a closed bound volume, macro on the corner;
cool back to warm. s15→s16 (0.202, −9): bound volume → a stack of paper corners with the
chapter's first drawn layer (the 95/100 survival grid) entering at right. s16→s17
(0.172, −12): paper stack + grid → box of rubber stamps; both warm wood-and-paper
overheads, coherent. s18→s19 (0.226, +8): green kraft tag → amber egg carton; the
green→amber reversal is deliberate (§1: a BLS bill is not an answer). s20→s21 (0.200,
+7): grocery bag → the loaf under green grade with the ladder measure bar; neutral→green,
dark→dark. s21→s22 (0.138, +1): loaf → a rack of blank US time cards, both green, both
similar luma; the gentlest joint of the green run. s22→s23 (0.147, −3): time cards →
three rungs of a wooden ladder against dark planks; coherent close.

### Bonus: the dissolves are CORRECT (measured, not assumed)

The joint montage showed the outgoing statement faintly visible mid-overlap at several
joints, which is the visual signature of the `japanese-money-methods-hi` stacking-context
defect. **It is not that defect here.** Measured the outgoing text's band contrast
(p99.5 − p50 of the focal rows) across s14→s15 at 16 offsets:

```
rel to joint:  -0.94  -0.34  -0.04  +0.00  +0.06  +0.13  +0.20  +0.26
contrast:        216    216    217    217    213    166    110     82
rel to joint:  +0.32  +0.38  +0.41  +0.44  +0.46  +0.56  +0.86  +1.46
contrast:         36     13     10      9      9     10     10    123
```

Monotone decay to the incoming scene's floor (9) at **+0.44**, exactly the end of the
0.45s overlap; the rise back to 123 at +1.46 is s15's own statement landing. The
outgoing scene fades out on schedule and is fully gone when the overlap ends — a
correct cross-dissolve, at 6% residual at the `+0.38` sample point. Corroborated in
source: `.scene` carries `isolation: isolate` in `assets/blockframe.css:63` with the
japanese-money post-mortem written above it. The fix is present in this build.

## 5 · The three fin-build flags — MEASURED, NOT RULED

### Flag 1 · s22 emits `tick` where `reveal` is expected

**Confirmed, and the root cause is one line.** `tools/audio/cues.py`:

```python
hit = find("span", rf"#{sid}-mf") or find("pulse", rf"#{sid}-.*")
if hit:
    pick = (hit[0], "tick", f"{sid} · {hit[1]}")
```

The `pulse` arm is a **wildcard over every element in the scene**, and the tick rung
sits at priority 5 — above the `reveal` fallback at priority 7. s22 has exactly one
pulse, `pulse("#s22-rate", S.s22 + 1.90)`, so it emits `tick @ 92.287`. The cue that
would otherwise fire is `rise("#s22-stmt", S.s22 + 1.10)` → `reveal @ 91.487`.
`tick` is documented in the module docstring as *"a measure bar draining, a beat
landing"*. A pulse on a rate token inside a headline is neither.

**The same bug also runs backwards in this chapter, which is the stronger evidence
that it is the rung and not the scene.** The chapter's ONE genuine measure bar —
`span("#s21-mf", S.s21 + 2.55, 1.2, 0, 0.1295)`, the §9a corpus ladder actually
draining, i.e. the literal thing `tick` is defined for — emits **no tick at all**,
because s21 already matched `hero` on `pop("#s21-num")` at priority 3 and the loop
takes one content cue per scene. So in ch2 the tick is on the frame that has no bar
and absent from the frame that has one. Same cause: a priority list with a wildcard
at rung 5.

**Does it generalise to every §4 span-in-focal scene? No — and the correction matters.**
ch2 contains exactly **one** span-in-focal scene (s22), so the chapter has no sibling to
check. But the cut does: storyboard-en §4 lists three fused-form scenes, each mandated
to take *"a `pulse` at +1.90"* — **s22** (ch2), **s42** (ch4), **s60** (ch5, two spans).
Checking them against the cut's own table, `studio/videos/passive-income-number-en/assets/cues-tables.json`:

- **s22** — not in `dry`. Fires. **Observed.**
- **s42** — **IS in `dry`.** A dry scene takes its joint and no derived content cue at
  all, so its pulse can never reach the tick rung. **Cannot fire.**
- **s60** — not in `dry`. **Will fire**, unless its build gives it a higher-priority
  match (`pop #s60-cta` / `pop #s60-stmt` / any `#s60-num`). ch5 is not built, so this
  is a prediction to re-check at that gate, not a measurement. Note also that s60 has
  **two** rate spans and the tick rung returns a single hit, so its second rate is
  silent either way.

So: tool-level pattern, yes; every span-in-focal scene, no — 1 of 3 observed, 1 of 3
structurally exempt, 1 of 3 predicted. Not ruling; the fix belongs to whoever owns
`cues.py`.

### Flag 1b · `assets/audio.json` vs `tools/audio/cues.py` — one difference, and it is not the known bug

Ran `python3 tools/audio/cues.py studio/videos/passive-income-number-en-ch2` read-only
(no `--write`) and diffed against the build's `assets/audio.json`:

- **25 cues vs 25 cues, byte-identical in order, `at` and `name`.** Set difference empty
  both directions; ordered comparison `True`.
- The five non-cue `_dry` notes (s12, s14, s16, s19, s20) are identical.
- **The one difference: `music`.** Generator emits `"bed-resolve"` (hardcoded in
  `cues.py`); the build ships `"bed-tension"`. So `cues.py --write` on this chapter
  would **silently swap the chapter's music bed**. `music` is a per-chapter fact with
  no home in the generator and no home in `cues-tables.json` — it is a hardcoded literal
  in a tool that overwrites the file that holds it. Reporting as a system gap, same
  class as the hardcoded HOLDS/BUZZ table that was moved out on 2026-08-07.

**On the `counted` fix shipped today:** it is **not exercised by this chapter**, so this
diff carries no signal about it either way. `COUNTED` for this cut is `["s64","s75"]`
— neither is in ch2. The chapter's one `popEach` (`popEach("#s16-art .gr", S.s16+1.10,
0.11, 0.40)`) is silenced because s16 is declared `dry`, so the `counted` branch is
unreachable here. The stagger-vs-dur fix needs a chapter containing s64 or s75 to
verify against.

### Flag 2 · the `.scene.centred .stack` padding-left gap

**What the local patch is.** An inline `<style>` rule in `index.html:72`, emitted by
`build.mjs:495`:

```css
.scene.centred .stack { padding-left: 0; }
```

**What it looks like on screen without it.** `.arch-b .stack` carries
`padding-left: 62px` — the air the creator asked for between `.vrule` and the type on
2026-08-05. `.scene.centred .stack` re-centres the stack but resets everything B sets
*except* that padding, so a centred archetype-B scene renders its "centred" content
**31px right of frame centre**. Meanwhile `.vrule` is `display: none` three rules
below on exactly those scenes, so the padding is holding the type off an element that
is not being drawn. Invisible in isolation — which is why it survived — and visible
only when something genuinely centred shares the frame. 2.13 is that frame:
`.measure.under` is at `left: calc(50% - 460px)` and IS centred, so the ladder bar and
the figure above it disagreed by 31px.

**Measured from this encode, post-patch** (frame centre x = 960.0, 1920x1080):

| scene | element | x span | midspan | off-centre |
|---|---|---|---|---|
| s19 | focal `$10,169` | 788–1131 | 959.5 | **−0.5** |
| s20 | focal `$847` | 832–1088 | 960.0 | **+0.0** |
| s21 | focal `$254,225` | 664–1253 | 958.5 | **−1.5** |
| s21 | rate `.sub` 40px | 670–1253 | 961.5 | +1.5 |
| s22 | focal (2 lines) | 240–1681 | 960.5 | **+0.5** |
| s21 | **measure track** | **500–1419** (len **920**) | **959.5** | **−0.5** |

The ladder track lands at exactly `calc(50% - 460px)` = x 500 with width 920 — the
storyboard spec to the pixel — and agrees with the figure above it to **1.0px**. The
31px disagreement is gone. Kickers read −2 to −3px, which is glyph-shape asymmetry in
letter-spaced caps, not layout. All four centred arch-b scenes (2.11–2.14) verified.

**⚠ The upstream port is ALREADY DONE, and the local patch is now dead code.**
`diff -u tools/scaffold/assets/chapter-design.css
studio/videos/passive-income-number-en-ch2/assets/chapter-design.css` → **exit 0,
byte-identical**. Both carry `padding-left: 0` at line 189 under a comment ending
*"Ported here 2026-08-08 so the remaining chapters inherit it instead of each build
re-deriving the same patch."* The inline override in `index.html`/`build.mjs` is the
same declaration at the same value later in the cascade — harmless, but chapters 3–6
will carry a redundant patch and a "SYSTEM GAP, patched locally and reported" comment
that is no longer true. Suggest `build.mjs` drops the emit; the orchestrator owns that.

### Flag 3 · `composition_heavy_overlay_count_high` — 30 confirmed, zero measurable cost here

**Actual count: 30.** Replicated the check's own rule from
`node_modules/hyperframes/dist/cli.js:75945` (heavy = `filter:blur` | `radial-gradient`
| `clip-path`, via inline style or via a class/id selector in any loaded stylesheet;
`display:none` excluded, `opacity:0`/`visibility:hidden` counted in):

```
15  .scrim   (four stacked radial-/linear-gradients, inset:0)
15  .glow    (one radial-gradient, inset:0)
30  TOTAL
```

Exactly **two per scene**, both static (nothing animated), neither `filter:blur` nor
`clip-path`. So the projection is plain arithmetic and **fin-build is right: 81 scenes
x 2 = 162.** Thresholds for context: the check warns at **25**; the field-signal repro
was **~40**. This chapter is 30 — past the warn, below the repro.

**Cost at draft: none measurable.** The field signal's signature is *"solid-black for
the first ~half of the render, recovering near the end"*. Against that specifically:
`blackdetect` 0 segments, `blackframe` 0 frames, per-scene p90 luma 35–59 across all
fifteen scenes with **no dark zone anywhere and no darkening in the first half** (the
first three scenes weigh p90 50.0, above the chapter's own 48.4 average), and
3166/3166 frames captured with zero drops. At 30 heavy overlays the regression does
not appear.

**The finding that matters is not about this chapter.** `tools/cut_assemble.py`'s own
docstring is explicit that the master is *"ONE composition, rendered"* — not a concat
of chapter files (it rejects `chapter_preview.py`'s stream-concat as a preview because
that loses the real 0.45s dissolves at the joints). So the assembled 81-scene cut
**will** be captured as a single composition carrying ~162 heavy overlays — **4x the
element count of the field repro**, in the one render that costs ~18 minutes and is
the last thing before delivery. That is a decision for the orchestrator/fin-build, not
a draft-gate ruling; recording it here because this chapter is the point at which the
number became measurable rather than projected.

## Reference numbers for the next gate

Not measured at this stage (chapter draft mode): VO drift, peak dBTP, whisper coverage,
runtime vs `timing.json`. Those belong to the master QA pass on
`renders/FINAL-1080p-en.mp4`. Chapter total for the joint arithmetic: **3166 frames
@ 30fps = 105.5333s**, and s23 carries its BARE `scene_duration` (no successor in this
project), so `cut_assemble.py` adds +0.45 back at fold-in.
