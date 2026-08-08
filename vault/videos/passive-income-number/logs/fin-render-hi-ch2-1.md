---
summary: Chapter-2 draft render + contact sheet for passive-income-number-hi, style E (s9-s21). Encode measures clean — 2446 frames, CFR, no black, no comma collision, cue list matches — with three timing/composition findings for fin-editor.
updated: 2026-08-08
source: measured from studio/videos/passive-income-number-hi-ch2/renders/DRAFT-ch2.mp4 (mtime 2026-08-08 13:02:32)
---

# fin-render — passive-income-number-hi ch2, attempt 1

Mode: CHAPTER DRAFT (orchestrator §3b step 4). Gate two and the encode were NOT run;
this is a draft for judging images, motion and timing.

## Provenance — what these numbers were measured on

| Artifact | mtime | Note |
|---|---|---|
| `renders/DRAFT-ch2.mp4` | 2026-08-08 13:02:32 | 20.2 MB, rendered in 2m 28.7s, this run |
| `renders/SHEET-ch2.jpg` | 2026-08-08 13:02:51 | 13 cells, built from the mp4 above |
| `renders/SHEET-ch2.json` | 2026-08-08 13:02:51 | sample-time index |
| `index.html` / `build.mjs` | 2026-08-08 12:48 | the style-E build these came from |

Retired style-A files still present and NOT reported on: `DRAFT-ch2-v2.mp4`,
`SHEET-ch2-v2.*`, `SHEET.*`, `SHEET-ch2.json.superseded` — all 2026-08-07, different
scene numbering. `DRAFT-ch2.mp4` and `SHEET-ch2.jpg` were overwritten.

Command: `npx hyperframes render . -c index.html -o renders/DRAFT-ch2.mp4 -q draft -f 30`
— draft quality only, no `--resolution`, no `--gpu`, no chunked encode.

## 1. Frame count, duration, CFR

| Measure | Expected | Measured | Verdict |
|---|---|---|---|
| Frames | ceil(81.531 x 30) = 2446 | **2446** (`ffprobe -count_frames`) | PASS |
| Video stream duration | 81.531s | 81.533333s | PASS |
| Container duration | — | 81.536000s | PASS |
| Root `data-duration` | — | 81.531 (s21 73.025 + 8.506) | consistent |
| fps tag | 30/1 | r_frame_rate 30/1, avg 30/1 | — |

**CFR verified from PACKET TIMESTAMPS, not the fps tag.** 2446 packets, 2445 deltas,
exactly two values and no third:

    0.033333  x 1630
    0.033334  x  815

First pts 0.0, last pts 81.5. Same signature as the en ch2 check. Frame counts sum;
chapters will not drift at the joint.

## 2. Black-segment scan

`blackdetect=d=0.05:pix_th=0.10` → **0 segments**. No dip-to-black at any joint; every
transition is a true cross-dissolve (confirmed frame-by-frame in §5).

## 3. Luminance — per-scene p90 and the real curve

p90 of luma, sampled at 4 fps over each scene's SETTLED span (start+0.45 to the next
scene's start, so dissolve frames are excluded and do not flatten the endpoints).

| Scene | Settled span | p90 mean | p90 min | p90 max | frame mean | span s |
|---|---|---|---|---|---|---|
| s9  | 0.00-5.29   | 43.6 | 42 | 45 | 32.6 | 5.29 |
| s10 | 5.74-11.55  | 45.2 | 41 | 46 | 30.8 | 5.81 |
| s11 | 12.00-17.68 | 55.0 | 55 | 55 | 46.0 | 5.68 |
| s12 | 18.13-25.54 | 46.0 | 45 | 46 | 36.8 | 7.40 |
| s13 | 25.98-31.25 | 43.3 | 42 | 44 | 28.0 | 5.26 |
| s14 | 31.70-37.66 | 59.0 | 59 | 59 | 41.7 | 5.97 |
| s15 | 38.11-44.73 | 59.0 | 59 | 59 | 43.2 | 6.62 |
| s16 | 45.18-50.08 | **37.3** | 37 | 38 | 27.2 | 4.89 |
| s17 | 50.53-55.42 | 48.8 | 47 | 49 | 36.2 | 4.89 |
| s18 | 55.87-60.06 | 49.9 | 49 | 50 | 34.7 | 4.19 |
| s19 | 60.51-66.61 | 53.9 | 52 | 55 | 31.8 | 6.10 |
| s20 | 67.06-73.03 | **38.9** | 38 | 39 | 29.1 | 5.97 |
| s21 | 73.48-81.53 | 42.9 | 42 | 43 | 38.3 | 8.06 |

**Duration-weighted chapter p90 = 48.0** over 76.13s of settled span.
Whole-timeline mean p90 including dissolves = 47.9. Open (0-2s) 43.0, close (last 2s) 43.0.

The curve, 4s buckets — this is the shape, not the endpoints:

    0-  4s  43.5
    4-  8s  43.8
    8- 12s  46.3
   12- 16s  55.0   <- s11 pale sky, the first lift
   16- 20s  50.3
   20- 24s  46.0
   24- 28s  44.3
   28- 32s  45.1
   32- 36s  59.0   \
   36- 40s  59.0    >  s14/s15 notebook hold — the chapter's bright plateau, 11.6s
   40- 44s  59.0   /
   44- 48s  42.4   <- s16 cash, -21.7 step, the chapter's darkest run
   48- 52s  41.7
   52- 56s  49.1
   56- 60s  49.9
   60- 64s  53.1
   64- 68s  49.2
   68- 72s  39.0   <- s20 textiles, second darkest
   72- 76s  41.4
   76- 80s  43.0
   80- 84s  43.0

Read against the tracked CEO issue: en ch1 ran one band (36-48); en ch2 opened at 57
but came in duration-weighted at 48.4, i.e. ch1's ceiling. **hi ch2 lands at 48.0 —
the same ceiling, reached a different way.** It does not open light (43.0) and it does
not sit in one band either: it has a genuine 21-point range (37.3 to 59.0) and one real
11.6s bright plateau at s14/s15. The plateau is a HOLD — one photograph under one
continuous zoom — so the chapter's brightness variety is carried by a single sustained
image rather than distributed across scenes. Strip the plateau and the other eleven
scenes average p90 44.9, which IS one band. The open and the close are the same value
(43.0), so the chapter has no luminance arc end to end.

## 4. Joints — scdet peak, luminance step, and what the joint SHOWS

Peak `lavfi.scd.score` inside each 0.45s overlap window, the settled p90 step across it,
and a description, because scdet cannot rank these.

| Joint | t | scdet peak | p90 step | Kind | What it shows |
|---|---|---|---|---|---|
| s9→s10  | 5.29  | 0.195 | +1.6  | dissolve | Wooden trunk on white brick → desk lamp over paper stacks. No shared object, no shared depth; bridged only by warm tungsten light. Two pictures. |
| s10→s11 | 11.55 | 0.306 | +9.8  | dissolve | Night interior desk → exterior water tank on a pale dusk sky. Interior→exterior, dark→light, nothing shared. Hardest visual break in the chapter. |
| s11→s12 | 17.68 | 0.146 | -9.0  | dissolve | Water tank on a stand → brass taps on a wall. Same subject matter (water plumbing), wide→close. Reads as one argument stepping forward. |
| s12→s13 | 25.54 | 0.173 | -2.7  | dissolve | Brass wall taps → hands holding an old brass hand-pump. Same object class, push to hands. Strongest continuity in the chapter. |
| s13→s14 | 31.25 | 0.252 | +15.7 | dissolve | Hands with brass tap → notebook and pen on a desk. Largest luminance RISE; the water metaphor ends and the abstraction begins. A deliberate chapter turn, but a hard break. |
| s14→s15 | 37.66 | **0.063** | +0.0 | **HOLD** | Same notebook; s15.jpg is the 91.74% derived crop. Lowest score in the chapter — confirms no cut is being made. |
| s15→s16 | 44.73 | 0.193 | **-21.7** | dissolve | Notebook → hands counting current-series ₹500 notes. Biggest luminance DROP (59.0→37.3). Object change is wanted here (rate → corpus). |
| s16→s17 | 50.08 | 0.228 | +11.5 | dissolve | Hands with notes → adding-machine keys. No shared object; both close-up, hand-scale, dark ground, but light direction differs (notes front-left, keys top). Cash → arithmetic. |
| s17→s18 | 55.42 | **0.101** | +1.1 | **HOLD** | Same adding machine, derived crop push-in. Second lowest score — the declared s17→s18 push-in reads as one continuous shot, not a cut. |
| s18→s19 | 60.06 | 0.189 | +4.0  | dissolve | Adding machine (green-tinted) → cable bundle. Both dense repeating-object textures at similar depth; reads as texture-to-texture. s19 is much busier. |
| s19→s20 | 66.61 | **0.546** | -15.0 | dissolve | Cable bundle → green folded textiles. HIGHEST joint score in the chapter and a -15.0 drop. Two unrelated objects, no shared depth or light. |
| s20→s21 | 73.03 | 0.138 | +4.0  | dissolve | Green textiles → brick wall. Both flat, frontal, textured surfaces at similar scale. Surface-to-surface; works. |

**scdet cannot rank these, confirmed again on this chapter.** Top in-scene (non-joint)
peaks:

    t=47.83  0.592   <- s16 countUp landing on ₹10,00,000
    t= 1.13  0.524   <- s9 statement rise (+1.10)
    t=75.00  0.520   <- s21 statement rise
    t=61.20  0.497   <- s19 statement rise
    t=26.67  0.414

Joint peaks span 0.063-0.546. Two of the chapter's three highest scdet scores are TEXT
RISES, not cuts, and eleven of the twelve joints score below the top in-scene peak. Any
gate that ranks joints by scdet would flag s16's number landing and pass s10→s11. The
two HOLDs are the only joints scdet places correctly, and only because a hold genuinely
has no cut.

## 5. Dissolve interiors — no double-paint

Sampled at BOTH `format.json` `qa.dissolve_sample_offsets` (0.225 and 0.38) at all twelve
joints, plus a fine strip at 0.00/0.10/0.20/0.30/0.38/0.44/0.50/0.60 on s10→s11 and a
full-res text-band crop at 0.20/0.30/0.38/0.44 on s16→s17 (the worst case — both scenes
carry the string ₹10,00,000, so a double-paint would show as a doubled number).

Result: **the japanese-money-methods stacking-context defect is NOT present.** The
outgoing `.stack` fades monotonically with its own scene and is composited UNDER the
incoming background:

    +0.00/+0.10   outgoing at full opacity, incoming not yet visible
    +0.20/+0.30   outgoing dimming, incoming .bg rising behind it, incoming kicker up at +0.30
    +0.38         outgoing a faint ghost, incoming kicker legible
    +0.44         outgoing ink GONE
    +0.50         clean incoming scene

Observation, not a defect: because the incoming kicker rises at +0.30 and the outgoing
ink survives to ~+0.42, two centred kickers occupy nearly the same y for roughly 0.10s
at every joint (clearest at s16→s17, where "RUNG ONE" and "THE SUM" stack). It is faint
and brief and is inherent to a centred stack under a 0.45s dissolve — flagging it so
fin-editor rules rather than discovers it.

## 6. Comma-descender clearance — measured from the encode

The scaffold fix is present: `assets/chapter-design.css:141-142`
`.arch-b .mega { font-size: 300px !important; line-height: .84; letter-spacing: -14px; padding-bottom: .11em; }`

Per-column minimum vertical clearance between ink of one line and ink of the next,
measured on full-resolution frames from the mp4 (not the browser):

| Scene | String | Pair measured | Min per-column clearance |
|---|---|---|---|
| s14 | `3.0%` (`.mega` 300px) | mega → foot | **71px** (row gap 69px) |
| s16 | `₹10,00,000` (`.huge` 112px) | number → foot | **27px** |
| s17 | `₹10,00,000 AT 3.0%` / `IS ₹30,000 A YEAR` (`.huge` 88px, two lines) | line 1 commas → line 2 caps | **12px** (at x=712) |
| s17 | — | line 2 → foot | **33px** |
| s18 | `₹2,500` (`.huge` 112px) | number → foot | no shared column (unbounded) |

**No comma descender touches the glyph below it anywhere in the chapter.** The tightest
case is s17's two-line `.huge`, at 12px, which is clear but is the number to watch if
that line ever grows a digit or the size is raised.

⚠ **One thing the fix does not cover, worth knowing before ch3-7.** The style-A defect
was `₹10,00,000` in a 300px `.mega`. In style E the lakh/crore rungs are `.huge`
(112px / 88px), and the only `.mega` in the cut is s14's `3.0%`, which has no comma.
So `.arch-b .mega { padding-bottom: .11em }` is applied and correct — s14 measures 71px
of clearance with it — but it is **not what is protecting this chapter's rungs**; the
smaller `.huge` size is. The clearance ch3-7 depend on is `.huge`'s, which no rule
guarantees and which is 12px at its tightest today. If a later chapter promotes a
comma'd figure to `.mega`, the fix will carry it; if one raises `.huge` or adds a digit
to a two-line rung, nothing will.

## 7. Cue list — `tools/audio/cues.py` read-only diff

    python3 tools/audio/cues.py studio/videos/passive-income-number-hi-ch2

**Exit 0**, empty stderr. No `cue_min_gap_seconds` violation in either the generated or
the shipped list.

| | Generated | Shipped `assets/audio.json` |
|---|---|---|
| Cue count | 17 | 17 |
| Times | identical | identical |
| `music` | `bed-resolve` | `bed-resolve` |
| transition / reveal / hero / tick | 11 / 3 / 2 / 1 | 11 / 4 / 1 / 1 |
| Minimum gap | 1.100s | 1.100s (limit 0.8s) |

One difference, and it is intentional and documented in the shipped file: the derived
`hero` at 35.736 (s14 `pop(#s14-num)`) is **downgraded to `reveal` by build.mjs** —
storyboard §2 rings s16, s62 and s64 and no other rung, and cues.py cannot know which
number is the one that lands. `_hero` records the downgrade. Every other cue matches
byte for byte.

Both suppressed joints are correct: s15 (37.662) and s18 (55.422) take no `transition`
because `assets/cues-tables.json` declares `["s14","s15"]` and `["s17","s18"]` as holds.
§4 confirms from the encode that neither is a cut (scdet 0.063 and 0.101, the two lowest
in the chapter), so the suppression matches the picture.

## 8. Audio on the draft

| Measure | Value |
|---|---|
| Stream | aac, 48 kHz, stereo, 81.536s |
| Sample peak (`astats`) | **-3.80 dB** (limit: below -1 dBTP) |
| RMS | -26.23 dB |
| Flat factor | 0.000 |
| Longest silence (`silencedetect n=-45dB:d=1.2`) | 1.397s at 65.590-66.986 |

Eleven silences, all 1.212-1.397s and all at scene joints — consistent with the MEDIUM
tier's per-line padding (tail 0.55 + lead_in 0.25 = 0.80) plus the 0.45s transition.
No dead zone anywhere; every scene carries VO. Music bed and SFX are not in the draft.

## 9. Headline contrast — settled frame, per scene

Otsu-separated ink vs local background in the tallest type band, WCAG contrast:

| Scene | contrast | Scene | contrast | Scene | contrast |
|---|---|---|---|---|---|
| s9  | 14.23:1 | s13 | 14.52:1 | s18 | 5.74:1 |
| s10 | 14.84:1 | s14 | 5.27:1 (foot; mega not yet up) | s19 | 14.44:1 |
| s11 | **6.11:1** | s15 | 5.94:1 | s20 | 5.52:1 |
| s12 | 6.63:1  | s16 | 15.25:1 | s21 | 13.62:1 |
|     |         | s17 | 14.20:1 |     |         |

Lowest is s14's foot at 5.27:1. **Every band clears AA for large text (3:1) and normal
text (4.5:1) with margin.** Notably s11's orange headline on the pale sky — the declared
caveat — measures 6.11:1 against its local background, so that caveat is compositional,
not a contrast failure.

## 10. Measurements against the five caveats and two deviations (for fin-editor)

Not rulings — numbers and descriptions so fin-editor can rule.

- **s19 busy frame.** Confirmed dense: the cable bundle is high-frequency black cable
  edge to edge with no rest area. Headline survives on the scrim at 14.44:1 and p90 is
  53.9, one of the brighter scenes. It is the busiest frame in the chapter by a wide
  margin. It does carry both named things (phone cable, network cable), is brand-free
  and currency-neutral.
- **s11 pale sky.** p90 55.0 with min=max=55 — a completely flat, even field, the pale
  sky filling roughly the upper two-thirds. Contrast 6.11:1, so legible. It is the
  chapter's second-brightest scene and the +9.8 step into it is the second-largest rise.
- **s17 numeric keys.** The adding-machine keys read `70 50 30 10` on the front row and
  `80 60 40 20` behind, all clearly legible at full resolution, sitting directly behind
  a numeric claim (`₹10,00,000 AT 3.0% IS ₹30,000 A YEAR`). No currency, no language, no
  brand. Two sets of numbers on one frame is the thing to rule on; the green ground and
  the scrim do separate them.
- **s10/s17 adding-machine through-line.** Measured: there is no through-line in the
  pictures. s10 is a white desk lamp over stacks of loose paper; there is no adding
  machine in the frame. s17/s18 are the adding machine. The two share a warm desk mood
  and nothing else — no object, no depth, no light direction. If the through-line was
  meant to be visible, it is not.
- **s9 chests vs the ch4 trunk.** s9 is a single wooden-and-metal travel trunk with
  metal banding and a hasp, shot three-quarter against a whitewashed brick wall, warm
  key from upper-left. That is the same object class as a trunk, so the cross-chapter
  repetition risk is real and will need the numbered cross-chapter PNG to settle.
- **s15 "The reason comes later."** Renders exactly as declared, replacing the script's
  "The reason is in Chapter 5." No chapter reference appears anywhere in the chapter.
- **s17→s18 push-in.** Works. scdet 0.101 (second lowest of twelve), p90 step +1.1, and
  the frames show the same adding machine at 91.74% crop. Reads as one continuous shot;
  the suppressed `transition` cue is right.

## 11. Findings this run turned up that were not on the caveat list

1. **s18's ₹2,500 holds settled for only 0.629s.** Measured on the glyph-ink mask: the
   countUp first paints at 58.533, last changes at 59.433, and the dissolve to s19 begins
   at 60.062. So the video's FIRST derived income figure is at its final value for 0.63s
   before the next scene starts fading over it (~1.08s until fully gone). Compare s16,
   the chapter's declared hero: counts 46.767→47.833 and then holds settled **2.244s**.
   The most important number in the chapter gets a third of the hero's settle time.
2. **The s14 cell of the contact sheet shows no number, and that is honest.** s14's mega
   is anchored to the spoken «तीन परसेंट» and pops at 35.736 (start+4.49); chapter_sheet
   samples s14 at start+2.6 = 33.846. The mega does render — verified at t=36.8, 300px,
   71px of clearance to the foot. Do not read the empty s14 cell as a missing number.
   (The sheet handles s16 and s18 correctly, sampling both at start+4.5 for the countUp.)
3. **s20's photograph does not say its line.** The frame is a stack of green-tinted
   folded textiles. The line is "Not one rupee out of the salary" under the kicker
   "ALL TWELVE MONTHS". Neither twelve months nor salary is in the picture. It is also
   the chapter's second-darkest scene (p90 38.9) and the incoming side of the chapter's
   highest-scoring joint (0.546). Raised against the sound-off image rule.
4. **The chapter has no luminance arc.** Open and close are both p90 43.0, and outside
   the s14/s15 plateau the other eleven scenes average 44.9.

## Verdict

**STATUS: ok** — this is a draft, so nothing here is a gate-two ruling. The encode is
mechanically sound on every measured axis: frame count exact, CFR clean, no black, cue
list matching, comma clearance holding, peak well under, contrast clear everywhere.
The open questions are compositional (§10, §11) and belong to fin-editor and fin-ceo.
