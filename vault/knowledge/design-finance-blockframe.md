---
summary: The durable design system for the finance channels (@cashguruguides ₹ · @moneymavens101 $) — dark blockframe, photographic backgrounds under a single grade, heavy type, chip/stamp motion language. Extracted from the shipped needs-vs-wants pair. Copy into each video's DESIGN.md.
updated: 2026-07-28
source: distilled from studio/videos/needs-vs-wants/index.html + needs-vs-wants-en/index.html (both shipped) and vault/videos/needs-vs-wants/storyboard-hi.md · verified against the rendered output 2026-07-28
---

# DESIGN — Finance blockframe (dark grade)

> **This file supersedes [[design-techtooltester]] for all finance work.**
> That note is the **bright** TechToolTester system — white/pastel gradient,
> *"No grain. No vignette. No black."* The finance format is its opposite:
> `#0d1017`, full-bleed photography, grain, four-layer scrim. Pointing a
> scripting or storyboard agent at the wrong one is how drift starts on run #1.

The channel's visual register: **dark, dense, confident.** Money facts stated
plainly in heavy type over photographic texture. Nothing decorative, nothing cute.

---

## 1. Stage and grade

| Property | Value |
|---|---|
| Stage | 1920 × 1080, `#root` with `data-composition-id="main"` |
| Scene padding | `110px 150px` |
| Base | `--bg: #0d1017` |
| Photo layer | `.bg`, `inset: -8%` (bleed for the Ken Burns move), `background-size: cover` |
| **The grade** | `filter: grayscale(0.32) brightness(0.62) contrast(1.05)` |
| Grain | `.grain`, opacity `0.05`, `mix-blend-mode: overlay` |
| Track index | scenes `1`, audio `10` |

**The grade is load-bearing.** It is the single reason nine unrelated stock photos
read as one film. A per-scene `filter:` override is permitted only for a near-black
texture that the grade crushes flat, and **never more than once per video** — past
that the unity is gone.

### The scrim (four layers, in order)

```css
.scrim {
  position: absolute; inset: 0; z-index: 1;
  background:
    radial-gradient(ellipse 72% 64% at 50% 52%, var(--tint, transparent), transparent 72%),
    radial-gradient(ellipse 88% 78% at 50% 53%, rgba(13,16,23,0.46), transparent 80%),
    radial-gradient(ellipse 115% 105% at 50% 54%, rgba(13,16,23,0.14), rgba(13,16,23,0.58)),
    linear-gradient(180deg, rgba(13,16,23,0.40), rgba(13,16,23,0.10) 46%, rgba(13,16,23,0.52));
}
```

Layer 1 carries the per-scene `--tint`. Layers 2-4 are fixed: they pull the centre
down so type reads, then vignette the frame.

---

## 2. Colour — roles, never meanings

```css
--bg     #0d1017    --panel  #161b25    --ink   #f5f3ec    --muted #98a2b3
--fund   #22c55e    --warn   #ef4444    --target #f59e0b   --pop   #ff5c39
```

| Token | Role | Not |
|---|---|---|
| `--fund` green | the good outcome, the kept thing, the safe path | "needs" |
| `--warn` red | the loss, the leak, the trap being exposed | "wants" |
| `--target` amber | the thing under examination, the decision point | "wants" |
| `--pop` orange | the call to action, the do-this-now stamp | — |
| `--muted` grey | kickers, feet, subtitles — never a focal element | — |

**Semantics are per-video, derived from the thesis — not a channel rule.** The
shipped needs-vs-wants deliberately inverted the emergency-fund system: there,
wants render amber and red is reserved for the leak alone, because that video's
argument is *"wants aren't the enemy."* Reuse the inversion blindly on a
credit-card video and red should be the interest trap, not a subscription.

**Every storyboard must open with a four-line colour table for that video**, and
the audit stage checks each coloured element against it. The check that matters:
*does any element render in a colour that argues against the script?*

### Per-scene tint (shipped reference)

```
s1 red .12   s2 —(photo-free)  s3 green .10   s4 amber .12   s5 green .10
s6 green .10 s7 —(photo-free)  s8 orange .12  s9 green .13
```
*(Historical reference — needs-vs-wants shipped with photo-free s2/s7. As of
2026-07-28 every scene carries a `.bg`; the tint ladder still applies.)*

Tint tracks the scene's emotional register, at 0.10-0.13 alpha. Above ~0.15 it
stops reading as light and starts reading as a colour wash.

---

## 3. Typography

Self-hosted variable face — no system-font dependency, no network fetch:

```css
@font-face {
  font-family: "FinanceSans";
  src: url(assets/fonts/NotoSansFinance-var.woff2) format("woff2-variations");
  font-weight: 100 900; font-style: normal; font-display: block;
}
--font: "FinanceSans", system-ui, sans-serif;
```

Noto Sans, subset to Latin + punctuation + currency, width axis pinned, **weight
axis live at 100-900**. 32 KB. Carries `₹` U+20B9.

> **Do not substitute Archivo Black**, despite [[design-techtooltester]] naming it.
> Verified with fontTools: Archivo Black has **no U+20B9 (₹)** and no U+2192 (→).
> Using it breaks the rupee sign in the Hindi channel's hero number.

### The ladder — step down it, never interpolate

| Class | px | Use |
|---|---|---|
| `.mega` | 290 | the one enormous number (a rule, a count) |
| `.huge` | 112 | the scene's single focal statement |
| `.counter` | 96 | a running/animated figure |
| `.arrow` | 72 | standalone flow arrow |
| `.head2` | 54 | secondary headline |
| `.billrow.total` | 50 | the summed line |
| `.cta` | 46 | subscribe block |
| `.stamp` | 44 | the rotated verdict |
| `.sub` `.billrow` `.decision` | 40 | supporting statement, bill lines |
| `.chip` `.statstrip` | 32 | enumerated items |
| `.kicker` | 30 | the scene's opening whisper |
| `.collabel` | 28 | column headers |
| `.foot` | 26 | source line, caveat |

Overriding inline is allowed **only to a value already on the ladder** (the shipped
pair drops `.huge` to 88 and 76, `.mega` to 240). Shrinking a focal element below
76 to make it fit is a layout failure, not a type decision — restructure instead.

**Numerals:** `font-variant-numeric: tabular-nums` on `.counter .mega .billrow
.head2 .huge`, so animated figures do not shimmy. Grouping is locale-bound —
`Intl.NumberFormat("en-IN")` for `-hi` (gives `1,24,564`), `"en-US"` for `-en`.
A plain `\B(?=(\d{3})+(?!\d))` regex is **wrong for India** and prints `124,564`.

**Text shadow** on every text class: `0 2px 22px rgba(0,0,0,.7), 0 1px 4px rgba(0,0,0,.55)`.

---

## 4. Components

- **`.chip`** — pill, `--panel` fill, 3px border, `999px` radius. Border colour
  carries the role (`.fund` `.warn` `.target`). Max **3 per row**, **≤22 chars
  each**; rows declared explicitly in the storyboard. `.row` has `flex-wrap: wrap`,
  so four long chips silently wrap 3+1 into a ragged orphan that no checker flags.
- **`.stamp`** — the verdict. Solid role-colour fill, `#0d1017` text,
  `rotate(-4deg)`, `back.out` entry. One per scene at most.
- **`.bill` / `.billrow`** — the itemised money block, 780px wide,
  `justify-content: space-between`, `.total` bordered in `--warn`.
- **`.decision`** — `LABEL → verdict-pill` rows (`.v-cancel` `.v-down` `.v-keep`).
- **`.track2` / `.fill2` / `.ticks`** — 740px progress bar; ticks are a repeating
  gradient at `100%/12` for a twelve-month read.
- **`.statstrip`** — a cited statistic on a translucent `--warn` bed.
- **`.cta`** — `--pop` block, `#0d1017` text, closes the video.
- **`.arrow` / `.arr` / `.tri`** — `→` and `▶` are **drawn in CSS**, not typed.
  Both are absent from the subset; em-based so they scale with the host font-size.

**No SFX.** The finance format is voice + motion only.
**No logo outro.** Neither finance channel has a brand mark yet
([[channels]] D/E) — the video closes on the `.cta` block. Build the wordmarks
before reinstating the standing logo rule.

---

## 5. Motion

Nine helpers, all on one paused GSAP timeline registered to `window.__timelines`:

| Helper | Motion | Default |
|---|---|---|
| `rise` | fade + travel up | `y:40`, `0.7s`, `expo.out` |
| `pop` | fade + scale from 0.6 | `0.6s`, `back.out(1.7)` |
| `fade` | opacity only | `0.5s`, `power1.out` |
| `pulse` | scale blip, yoyo | `1.12×`, `0.16s` |
| `fill` | `scaleX` from 0 | `0.8s`, `power2.out` |
| `countUp` | number tween, locale-formatted | `1.2s`, `power1.out` |
| `breathe` | slow yoyo scale, **odd repeat count** so it ends where it began | `1.035×`, `1.5s` cycles |
| `ken` | the background move | `1.0 ↔ 1.16` scale, `∓2.5 xPercent` |
| `drift` | slow one-way scale for photo-free scenes | `1.035×`, `ease:"none"` |

### Rules

1. **Alternate `ken` direction.** Never two pushes in a row. Shipped order across
   the photo scenes: `in, out, in, out, in, out, in`.
2. **Every scene carries a full-bleed `.bg` photo under the grade — photo-free
   scenes are RETIRED** (creator rule 2026-07-28, supersedes the earlier
   2-per-video rest-beat cap; `format.json photo_free_scene_ratio` is now 0).
   Every scene therefore gets `ken`; `drift` survives only as the motion for
   overlay stacks, not as a substitute for a background. **No scene may hold a
   static frame beyond ~2s.**
3. **Keyword-matched imagery** (creator rule 2026-07-28): when the VO names a
   concrete thing (gym, bill, phone, bank, family), the frame shows that thing —
   either as the scene's `.bg` or as a cut-in timed to the word's cue. The
   storyboard lists per scene: the bg keyword + each cut-in keyword with the VO
   word it lands on. Dense scenes still get the *calmest* background (texture
   reading of the keyword, not a busy literal shot) — density is managed by
   choosing a quieter image, never by dropping the image.
4. **One focal element per scene.** Never `.huge` and `.mega` together.
5. **Reveal spacing ≥0.8s** between consecutive cues, except a declared cascade
   (≤5 items at fixed 0.6-0.7s). Something must be on screen by scene start +0.5s.
6. **≤6 elements visible simultaneously.**

---

## 6. Timing contract

```
scene_duration = 0.4 (VO lead-in) + clip_duration + 1.0 (tail)
scene_start    = previous scene_start + previous scene_duration
audio start    = scene_start + 0.4
```

Verified across both shipped cuts (hi s1: `0.4 + 17.74 + 1.0 = 19.14` ✓;
en s4: `0.4 + 14.65 + 1.0 = 16.05` ✓).

The same numbers appear in **four** places — the `<section>` attributes, the JS
`S` map, the `<audio>` row, and the root `data-duration`. They must be generated
from one source, never hand-edited: updating three of four passes every check and
ships a video whose animations fire against the old timeline.

**Cue placement.** The shipped pair interpolates by character offset
(`0.4 + chars_before/total × clip_duration`). That is a stopgap — it drifts most
on Hindi, where delivery rate swings across a 26s clip. Anchor cues to **word-level
timings** from faster-whisper instead. Split offsets into two classes:

- **anchored** — scales with the clip, lands on its word
- **fixed** — cascades, arrows, stamp slams: constant regardless of clip length

Surplus time from a longer clip goes into **holds, never into a cascade**.

---

## 7. Imagery

Full rules in [[stock-photo-sourcing]]. The load-bearing ones:

- **Object-led, not scene-led.** Photos sit under `grayscale(.32) brightness(.62)`
  with heavy type on top — they are texture, not information. ₹500 notes carry
  "India" more reliably than any photo of a person, and they actually exist in the
  library (India-with-people queries are ~20% usable).
- **The densest scene gets the calmest background.** Reach for a texture first on
  any scene carrying more than ~4 stacked elements.
- **Never a phone-screen photo as a background.** The screen is someone else's
  brand and it is the brightest thing in frame. This has now shipped **three**
  times undetected — most recently `s8` of the Hindi cut, upside down, with the
  carrier string `MTN-SA` legible.
- **Faces fight the typography; hands and objects don't.** Also a licence issue:
  Pixabay bars unflattering use of identifiable people, and a recognisable face
  under a voiceover about wasted money is exactly that.
- **Check what the picture is saying** — a falling chart under a "this grows your
  money" line, demonetised pre-2016 ₹500 notes, dollars answering a ₹ query.
- **Drop a cut-in rather than fake it.** Single-photo scenes read fine.
- **No image may repeat across videos or channels.** Verified failure: one
  `s9.jpg` is byte-identical in three shipped projects across *both* channels,
  because Pixabay's top hit is deterministic and different queries collapse to it.
  Key an asset ledger by md5 and refuse a hash already used anywhere.

---

## 8. Determinism

- GSAP is **vendored** at `assets/js/gsap.min.js`. Never a CDN: if the fetch is
  slow past first paint, `gsap` is undefined, no timeline registers, and the render
  **succeeds** — producing a video with every element static from frame 0, which
  `npm run check` will not catch because it hits the same network.
- Font is self-hosted. No `Date.now()`, no unseeded `Math.random()`, no
  render-time fetches.
- Pin the CLI with a committed lockfile, not `npx --yes`.

## 9. The checker is evidence, not authority

`npm run check` is a gate, but a finding is not automatically a defect. The
rotated `.stamp` construct reports a false contrast failure when it sits on a
bright fill; the storyboard's standing instruction is *"do not fix it by lightening
the text."* An agent told to "fix until clean" will edit a design token and degrade
the signature element on every future video.

Carry a `known_benign` list of `{selector, rule, reason}`. Fail loudly on a **new**
finding; never edit a token to satisfy a checker.

> Note: after moving to a real 900 weight the shipped pair went from one failing
> contrast check to **41/41 passing** — that entry is no longer needed. Faux-bold
> on a 400-weight fallback was part of the original problem.

---

## Related

[[channels]] · [[stock-photo-sourcing]] · [[niches/india-finance-market]] ·
[[us-english-script-style]] · [[../workflows/voiceover-tts]] ·
[[design-techtooltester]] (the *other* system — bright, non-finance)
