# 06 — Motion, animation, transitions, visual effects

Scope: what moves and how. Not colour/type/layout tokens, script wording, imagery
sourcing, sound, thumbnails.

Every claim is tagged **FACT** (verifiable from a spec, a source, or a rendered
artifact) or **UNVALIDATED** (untested belief about audience response).

Primary artifacts read:
- `/home/zain-ali/Documents/YoutubeScraper/vault/videos/good-debt-vs-bad-debt/src/en/index.html` (558 lines)
- `/home/zain-ali/Documents/YoutubeScraper/vault/videos/good-debt-vs-bad-debt/src/hi/index.html` (525 lines)
- the other 10 shipped compositions under `vault/videos/*/src/{hi,en}/index.html`
- `/home/zain-ali/Documents/YoutubeScraper/studio/videos/credit-history-{hi,en}/index.html` + their renders
- `/home/zain-ali/Documents/YoutubeScraper/studio/videos/credit-history-en/renders/FINAL-1080p-en.mp4` (259 MB, 1920×1080, 30 fps, 5197 frames)
- `/home/zain-ali/Documents/YoutubeScraper/studio/packages/core/src/runtime/init.ts` (clip lifecycle — the load-bearing constraint)
- `/home/zain-ali/Documents/YoutubeScraper/tools/pipeline_check.py`
- `/home/zain-ali/Documents/YoutubeScraper/tools/format.json`
- `/home/zain-ali/Documents/YoutubeScraper/vault/knowledge/design-finance-blockframe.md` §5
- installed skills `hyperframes-animation`, `hyperframes-keyframes`

---

## 1. What actually runs today

### 1.1 The vocabulary is not nine helpers — it is five different vocabularies

**FACT.** `design-finance-blockframe.md` §5 states "Nine helpers". No shipped
composition implements those nine. Function definitions found per composition:

| Video | helpers defined | missing from the documented nine | extra, undocumented |
|---|---|---|---|
| 50-30-20-rule hi/en | rise pop fade pulse breathe ken countUp + `segIn` `toPatch` `toSqueeze` | fill, drift | segIn, toPatch, toSqueeze |
| needs-vs-wants hi/en | rise pop countUp fill fade pulse drift breathe ken | — | — |
| emergency-fund hi | rise pop `riseEach` `popEach` countUp fill fade pulse breathe ken | drift | riseEach, popEach |
| emergency-fund en | rise pop popEach countUp fill fade pulse breathe ken | drift | popEach |
| pay-yourself-first hi/en | rise pop `countSteps` fill fade `exit` pulse drift breathe ken | countUp | countSteps, exit |
| **good-debt-vs-bad-debt hi/en** | rise pop popEach fade exit pulse breathe ken | **fill, countUp, drift** | popEach, exit |
| credit-history hi | rise pop popEach fade exit pulse breathe fill countUp ken + `paint` | drift | popEach, exit, paint |
| credit-history en | rise pop fade exit pulse breathe fill countUp ken | drift, popEach | exit |

Three different counter helpers exist across the six topics (`countUp`,
`countSteps`, and none). `exit` and `popEach` are used heavily and are in no
document. `drift` is in the doc and in 4 of 12 compositions, none of them recent.

This matters because `fin-build.md` step 1 instructs the build agent to read
**"the newest archived `vault/videos/<slug>/src/{hi,en}/index.html` as the
reference implementation."** The newest archive is good-debt — the composition
with the *smallest* vocabulary, missing `countUp`, `fill` and `drift`. The
reference-implementation rule is actively ratcheting the motion language down.

### 1.2 There is no transition between scenes. The video hard-cuts eight times.

**FACT — from the source.** In both good-debt cuts every boundary is exact:

```
scene-boundary overlap (s), en: s1:+0.000 s2:+0.000 s3:+0.000 s4:+0.000
                                s5:+0.000 s6:+0.000 s7:+0.000 s8:+0.000
scene-boundary overlap (s), hi: identical (worst |Δ| < 0.001)
```

`scene_start = previous scene_start + previous scene_duration` is the timing
contract in `design-finance-blockframe.md` §6 and it is honoured to the
millisecond. Adjacent `.clip` windows abut with zero overlap, so exactly one
`<section>` is ever visible. No helper crossfades, pushes, wipes or dips. There
is also no fade-in at t=0 and no fade-out at the end — the video begins on a
fully-lit frame and ends on one.

**FACT — from the rendered pixels.** ffmpeg's scene-change detector run over
`credit-history-en/renders/FINAL-1080p-en.mp4` (real 30 fps render, 5197 frames):

| declared boundary (s) | single-frame delta at boundary | mid-scene single-frame delta |
|---|---|---|
| 16.107 | **10.72** | t=8.0 → 0.087 |
| 26.833 | **6.13** | t=40.0 → 0.377 |
| 48.295 | **8.76** | t=75.0 → 0.084 |
| 65.995 | **7.85** | t=120.0 → 0.053 |
| 84.793 | **8.17** | t=165.0 → 0.058 |
| 104.896 | **9.32** | |
| 133.046 | **8.94** | |
| 153.620 | **5.85** | |

The boundary frame-delta is **16× to 200×** the in-scene frame-delta. At
`scdet=threshold=8`, five of the eight boundaries are classified as hard scene
cuts by a general-purpose cut detector; the other three only miss because the
adjacent photographs happen to share a tone. **This is a hard cut, measured, not
inferred.**

**Contradiction.** The installed `hyperframes-animation` skill
(`transitions/overview.md`) opens its "Animation Rules for Multi-Scene
Compositions" with: *"1. **Every composition uses transitions. No exceptions.**
Scenes without transitions feel like jump cuts."* Twelve shipped compositions
violate rule 1. `vault/skills/hyperframes_production.md` line 57 lists
`Transition` as a mandatory storyboard column; the finance storyboard template
dropped that column and no finance storyboard has ever specified one.

### 1.3 How much of each scene actually moves

Parsed every timeline call in both cuts, expanded each helper to its true
interval (including `pulse` = 0.32 s for the yoyo, `popEach` = 2×stagger+dur for
3 tags, and `breathe`'s real repeat expansion), took the union per scene, and
excluded `ken` so the number answers "is anything in the *foreground* moving".

**good-debt-vs-bad-debt — en cut (178.6 s, 9 scenes, 112 timeline calls)**

| scene | length | foreground moving | % | longest fully-static run | runs > 2 s |
|---|---|---|---|---|---|
| s1 HOOK | 18.8 | 9.44 | 50.3% | 2.30 | 1 |
| s2 ROADMAP | 11.2 | 3.20 | 28.4% | 2.15 | 2 |
| s3 CONCEPT | 23.1 | 9.92 | 43.0% | 4.00 | 2 |
| s4 RULE | 25.6 | 10.00 | 39.0% | 4.54 | 3 |
| s5 AUDIT | 20.1 | 4.94 | 24.6% | 2.70 | 4 |
| s6 ACTION | 17.4 | 9.42 | 54.3% | 3.36 | 1 |
| s7 THE MATH | 28.0 | 6.24 | **22.3%** | **6.60** | 4 |
| s8 DO THIS | 17.1 | 4.82 | 28.2% | 3.80 | 2 |
| s9 RECAP | 17.4 | 3.82 | 22.0% | 4.00 | 2 |
| **total** | **178.6** | **61.8** | **34.6%** | | **21** |

**good-debt-vs-bad-debt — hi cut (195.2 s, 114 calls): 77.8 s moving = 39.9%; 28
static runs > 2 s; worst 4.0 s.**

**FACT: 65.4% of the en cut and 60.1% of the hi cut has zero foreground motion.**
The frame during those 117 s is a photograph under a slow scale, plus type that
is not moving at all.

**FACT — the "no static frame beyond ~2s" rule is violated 21× per en cut and 28×
per hi cut, up to 6.6 s.** That rule appears in three places
(`format.json scene.max_static_hold_seconds: 2.0`,
`design-finance-blockframe.md` §5 rule 2, and the global guardrails block of every
storyboard) and **nothing checks it** — `tools/pipeline_check.py` contains zero
motion assertions; grepping it for `static`, `ken`, `motion`, `breathe`,
`cue_min_gap`, `max_simultaneous` returns nothing. `format.json`'s
`max_static_hold_seconds`, `cue_min_gap_seconds`, `max_simultaneous_elements` and
`cascade` are constants no tool reads.

### 1.4 The background move is below the perceptual floor on long scenes

`ken` tweens `scale 1.00 ↔ 1.16` and `xPercent ∓2.5` over the **whole scene**,
regardless of how long the scene is. The `.bg` box is `inset: -8%` → 2227×1253 px.
Displacement rate of an image feature at the frame edge:

| scene (en) | duration | zoom px/s | pan px/s | total px/s | **px per frame @30fps** |
|---|---|---|---|---|---|
| s2 | 11.2 | 13.65 | 9.90 | 23.6 | 0.79 |
| s8 | 17.1 | 8.98 | 6.51 | 15.5 | 0.52 |
| s1 | 18.8 | 8.18 | 5.93 | 14.1 | 0.47 |
| s4 | 25.6 | 5.99 | 4.34 | 10.3 | 0.34 |
| **s7** | **28.0** | **5.49** | **3.98** | **9.5** | **0.32** |

**FACT: on the longest and most important scene (s7, the math payoff), the entire
background camera move is 0.32 px per frame.** The measured mid-scene frame delta
at t=120 s (inside s7) is **0.053** — the lowest reading in the whole render.

**UNVALIDATED (but strongly implied by the measurement):** sub-pixel-per-frame
motion delivered through YouTube's VP9/AV1 transcode is at or below the level the
encoder will preserve. The scene that most needs to feel alive is the one where
the camera is closest to frozen.

Because `ken`'s *endpoints* are fixed and its *duration* varies 11–28 s, the
camera speed is inversely proportional to scene length — the pipeline is
automatically slowest exactly where scenes are longest.

### 1.5 `breathe` does nothing, and its parameter is a lie

**FACT.** `breathe` is `scale: 1.035`, `1.5 s` half-cycle. On a 112 px headline
that is ~4 px of total travel over 1.5 s ≈ **0.09 px/frame** — a quarter of the
already-invisible `ken`. It fires 8× in good-debt-hi and 4× in good-debt-en.

**FACT.** The `dur` argument is not the duration. The implementation is:

```js
function breathe(sel, at, dur) {
  var cyc = 1.5, n = Math.max(1, Math.round(dur / cyc)); if (n % 2 === 0) n += 1;
  tl.to(sel, { scale: 1.035, duration: cyc, ease: "sine.inOut", repeat: n, yoyo: true }, at);
}
```

`repeat: n` plays the tween `n+1` times, so real runtime is `1.5 × (n+1)`:

| call | real runtime | ratio |
|---|---|---|
| `breathe(x, t, 2.0)` | 3.0 s | 1.5× |
| `breathe(x, t, 2.2)` | 3.0 s | 1.4× |
| `breathe(x, t, 3.0)` | **6.0 s** | **2.0×** |
| `breathe(x, t, 3.5)` | 6.0 s | 1.7× |
| `breathe(x, t, 4.0)` | 6.0 s | 1.5× |

Consequence in shipped code: `breathe("#s1q", S.s1+5.50, 3.0)` runs 5.50→11.50,
but `exit("#s1q", S.s1+8.90)` fades that element out at 8.90. 2.6 s of the
breathe animates an invisible element. Harmless, but it means the composer's
mental model of the timeline is wrong, and `breathe` is being used as the alibi
that satisfies "no static frame beyond 2 s" while contributing no visible motion.

### 1.6 What the nine (eight, five, …) helpers add up to

Every entrance in the format is one of two gestures: **fade+translate up**
(`rise`) or **fade+scale up** (`pop`). `fade` is `rise` with the travel removed.
`popEach`/`riseEach` are the same two with a stagger. `pulse` and `breathe` are
the same scale gesture at two amplitudes. `fill`, `countUp`, `countSteps` are the
only content-aware motions and three of six topics ship without any of them.

**FACT: there is no motion in the entire format that travels sideways, that
leaves the frame, that reveals through a mask, that draws, that decreases, that
overshoots, or that separates the type layer from the photo layer.** Everything
appears in place by getting brighter and slightly bigger, and then stops.

---

## 2. Diagnosis — what the vocabulary is missing

Ordered by how visible the absence is.

**a. Scene transitions.** Section 1.2. Nothing. This is the single largest gap and
also the cheapest to close.

**b. Parallax between photo and type.** The `.bg` moves (barely); the `.stack`
sits at a fixed z with no counter-motion. There is a photo and there is text on
it; there is no *depth*. One counter-tween per scene converts the ken from "the
picture is scaling" into "a camera is moving through a scene", for ~5 lines.

**c. Masked reveals.** Zero. Every element in twelve compositions arrives by
opacity. A billrow that wipes in behind its own edge reads as printed/stamped;
the same billrow fading in reads as a slide deck. This is the most reliable
"professional vs template" tell available in a browser and it costs a wrapper div.

**d. Money-specific motion — none of it exists:**
- **a number that counts *down*** — `countUp` exists in 4/12 compositions; nothing
  ever descends. Half of personal finance is a number going down (balance, months
  remaining, interest saved). good-debt s7's whole thesis is "still $5,318 owed
  after a year" — delivered as static text.
- **a bar that overshoots and settles** — `fill` is `scaleX` with `power2.out`,
  which decelerates into its target. Money arriving should land with weight.
- **a stack that accumulates** — `popEach` pops items in place. Nothing ever
  *piles up*, which is the literal shape of saving.
- **a line chart drawing** — s5's focal claim is "INTEREST ON INTEREST" and s7's
  is a 215-month payoff. Both are curves. Both are rendered as capitalised text.
- **a coin/note leaving frame as it's spent** — no element in the format ever
  exits by moving. `exit` is opacity-only. Money leaving should travel.

**e. Camera moves that aren't Ken Burns.** One move exists, in two directions.
There is no push-in on a focal element, no rack focus, no lateral reframe. Focal
handoff is currently done by *emptying the frame* (`exit`, used 23× in
good-debt-en), which is why the static runs cluster right after every exit:
`exit` at +12.3 → `pop` at +13.0 → then 2.7 s of nothing.

**f. Type animation beyond fade-and-rise.** No per-word, per-line or per-character
motion anywhere. The format's focal moments are all-caps headlines that appear
whole. The installed skill ships 24 named text effects and a
`waterfall-entry` / `kinetic-beat-slam` rule set that are entirely unused.

**g. Nothing is synchronised to the voice beyond a hand-estimated character
offset.** Out of scope here (fin-voice / fin-storyboard own it) but it is the
reason cue spacing drifts and dead air pools at scene ends.

---

## 3. Benchmark

**Caveat on evidence quality (honesty note):** searching for "what 2026 finance
YouTube motion design looks like" returns almost entirely SEO listicles and
agency marketing. I could not find rigorous, measured comparisons. Everything in
this section is therefore **UNVALIDATED** except where it restates a technique
that is verifiable in our own toolchain. I have not watched competitor videos
frame-by-frame; that would be the honest way to close this and it is not
something I can do from here.

**UNVALIDATED — what the sources converge on:**

- The 2026 consensus is *restraint with intent*: motion that guides attention, not
  decorative motion. On that axis blockframe-9 is directionally right — the
  problem is not that we over-animate, it is that 65% of the runtime has no
  motion at all, which is a different failure than "too busy".
  ([digitalsilk](https://www.digitalsilk.com/web-design/web-trends/kinetic-typography/),
  [envato](https://elements.envato.com/learn/motion-design-trends))
- Financial explainers that read as premium make abstract mechanics *visible*
  through symbolic animation and system diagrams, rather than lettering the
  concept onto a photo. Our s5 ("INTEREST ON INTEREST" in 96 px caps over a
  photo of a statement) is the exact pattern that reads as cheap by this
  standard. ([contentbeta](https://www.contentbeta.com/blog/best-fintech-explainer-videos/),
  [advids](https://advids.co/blog/30-animated-financial-services-explainer-video-examples-to-inspire-innovation))
- Data-motion practice: bars grow, lines draw on, counters tick, paced like a
  story; 2–3 s per transition; ≤3–4 simultaneous changes; colour-pulse the item
  that changes rank. We do the ≤3–4 part (via `max_simultaneous_elements: 6`) and
  none of the rest.
  ([toptal](https://www.toptal.com/designers/data-visualization/mobile-data-visualization),
  [justanimations](https://justanimations.com/financial-data-visualization/))
- Masked reveals with spring physics are explicitly named as the amateur/
  award-winning dividing line in 2026 web motion writing.
  ([framer](https://www.framer.com/community/marketplace/components/mask-reveal/))
- Indian finance YouTube (Labour Law Advisor, Zerodha Varsity/Zing) is the
  reference set for the hi cut, but I found no usable description of their motion
  systems in search results — only channel descriptions.
  ([LLA](https://www.youtube.com/@LabourLawAdvisor/videos),
  [Varsity](https://www.youtube.com/@varsitybyzerodha),
  [Varsity Hindi](https://www.youtube.com/@ZerodhaVarsityHindi))

**Where our motion is visibly cheaper — UNVALIDATED as audience effect, FACT as
technical difference:**

1. Hard cuts between every scene (§1.2). No professional explainer channel cuts
   nine times with zero handling.
2. Static type over a still photo for 60–65% of runtime (§1.3).
3. Every number is set text, never animated (§1.6, §2d).
4. No depth — one flat plane of type on one flat plane of photograph (§2b).
5. Two entrance gestures for an entire nine-minute-equivalent catalogue.

---

## 4. What the platform genuinely gives us (verified, not assumed)

### 4.1 The clip runtime only owns `visibility` — this is why transitions are possible

**FACT.** `studio/packages/core/src/runtime/init.ts`, the timed-visibility pass
(~line 1662):

```js
rawNode.style.visibility = isVisibleNow ? "visible" : "hidden";
...
if (isVisibleNow) { if (isTimedClipInFlow(rawNode)) rawNode.style.removeProperty("display"); }
else if (isTimedClipInFlow(rawNode) && isTimedClipLeaf(rawNode)) { rawNode.style.display = "none"; }
```

- The runtime writes **only** `visibility` (and `display`, but only on **in-flow
  leaf** clips). Our `.scene` sections are `position: absolute` → `isTimedClipInFlow`
  is false → they are **never** given `display: none`, only `visibility`.
- **`opacity`, `transform`, `filter` and `clip-path` on a `.clip` section are
  entirely unowned by the framework.** GSAP can tween them freely, with no
  conflict, seek-safe.
- Two sections whose windows overlap are **both** `visibility: visible`
  simultaneously; both are `position:absolute; inset:0` with an opaque
  `background: var(--bg)`, so the later one in DOM order paints on top.

That is the whole mechanism a transition system needs, and it already exists.

### 4.2 `pipeline_check.py` does not forbid overlap

**FACT.** `check_html` (lines 268–284) asserts only:
- root `data-duration` ≈ **last** scene's `data-start + data-duration` (±0.5 s)
- scene count == `timing.json` line count
- root `data-duration` ≈ `timing.json total` (±0.5 s)

It never asserts that scenes tile without gaps or overlaps. **Extending
`data-duration` on scenes 1–8 by a transition length T, leaving `data-start`, the
`S` map, the `<audio>` rows, s9 and the root duration untouched, passes the
checker unchanged.** The VO timing contract is not touched at all.

### 4.3 Available in the installed toolchain

**FACT.** `tools/scaffold/assets/js/gsap.min.js` is **GSAP 3.15.0 core with
CSSPlugin only**. No DrawSVGPlugin, no MorphSVGPlugin (both are paid Club
plugins). Therefore:
- SVG stroke drawing must use raw `stroke-dasharray`/`stroke-dashoffset` + a
  build-time `getTotalLength()`. Fully supported. ✅
- SVG *shape morphing* is out unless we hand-roll it. ❌ (Don't.)
- `clipPath`, `filter: blur()`, `strokeDashoffset`, `backgroundPosition` all tween
  through the bundled CSSPlugin. ✅

**FACT.** `hyperframes-animation` provides: a full CSS scene-transition catalog
(`transitions/catalog.md` + 13 `css-*.md` category files), 60+ atomic motion
rules including `stat-bars-and-fills`, `svg-path-draw`, `depth-of-field-blur`,
`waterfall-entry`, `motion-blur-streak`, `spring-pop-entrance`,
`counting-dynamic-scale`, `viewport-change`, and 7 runtime adapters (GSAP,
Lottie, Three.js, Anime.js, CSS keyframes, WAAPI, TypeGPU). Also
`scripts/animation-map.mjs`, which enumerates every registered tween and
**computes dead zones** — i.e. it would have caught §1.3 automatically.

**FACT.** `@hyperframes/shader-transitions` v0.7.10 exists locally at
`studio/packages/shader-transitions/`. It captures DOM scenes to WebGL textures
via html2canvas. **Do not use it here.** Its `HyperShader.init()` owns scene
visibility and requires `class="clip"` be removed from scene divs
(`transitions/catalog.md`, Hard Rules) — that is incompatible with blockframe-9's
timing contract, and its html2canvas capture path imposes six CSS restrictions
(no `transparent` in gradients, no `var()` on captured elements, no gradients
under 4 px or below 0.15 opacity) that our four-layer `.scrim`, our CSS-drawn
`.arrow`/`.arr`/`.gt`/`.tri` glyphs and our `var(--tint)` scrims all violate.
CSS transitions give us everything we need with none of that.

### 4.4 Determinism rules everything proposed here must obey

**FACT** (from `hyperframes-keyframes` + `hyperframes-core` + our own
`fin-build.md` step 3):

Forbidden: `Date.now()`, `performance.now()`, unseeded `Math.random()`, timers,
async/`setTimeout`/Promise-constructed timelines, `repeat: -1`, hover/scroll
triggers, unregistered `requestAnimationFrame`, CDN script tags, render-time
fetches, CSS `transition` on animated elements.

Forbidden channels: `width`/`height`/`top`/`left`/`margin`/`padding` tweens,
duration-tweened raw `visibility`, `display` tweens, `gsap.set` on a `.clip`
itself.

Required: one **paused** timeline registered on `window.__timelines["main"]`,
built synchronously; `fromTo` with explicit from-states (never `from`, never
relative `+=`); state a pure function of timeline time; finite repeats;
`immediateRender: false` when a later tween re-owns a property another tween
already wrote.

**One gotcha that matters for `draw` below:** `getTotalLength()` must run at build
time. It works on an SVG inside a `visibility: hidden` element (it is geometry,
not layout) but returns 0 under `display: none`. Our absolutely-positioned scenes
never get `display: none` (§4.1), so this is safe — but it is safe *because* of
that runtime detail, and a future in-flow scene would silently break it. Measure
once at build, cache the number, never call it inside a tween.

---

## 5. Proposal — 8 new helpers

Same shape as the existing ones: a plain function that pushes `fromTo` onto the
shared `tl`. All seek-safe, all deterministic, all transform/paint-only.
LOC counts are the helper body, not call sites.

---

### 1. `wipe(sel, at, dur, dir)` — masked reveal

The element travels out from behind its own edge inside an `overflow: hidden`
wrapper. No opacity fade — it is *revealed*, not faded in.

```js
// DOM: <div class="mask"><div id="s7r1" class="billrow">…</div></div>
// CSS: .mask { overflow: hidden; }
function wipe(sel, at, dur, dir) {           // dir: 1 = from below (default), -1 = from above
  tl.fromTo(sel, { yPercent: (dir == null ? 1 : dir) * 105 },
                 { yPercent: 0, duration: dur == null ? 0.55 : dur, ease: "expo.out" }, at);
}
```

- **Serves:** every `.billrow` (s1 month-1 split, s7 the math), `.claim` rows
  (s3, s5), `.decision`. The itemised-money scenes — where a wipe reads as a
  statement line printing.
- **Why this form:** pure transform inside a static-overflow wrapper. No
  `clip-path` string interpolation, no filter, nothing that can render differently
  headless. Bulletproof under seek.
- **LOC:** 3 + one CSS rule. **Cost: cheap.**
- **Owner:** `fin-storyboard` (declares the wrapper) + `fin-build`.

---

### 2. `parallax(sel, at, dur, amt, sign)` — depth between type and photo

The `.stack` counter-moves against the `ken` on `.bg`, at a fraction of its rate
and in the opposite direction.

```js
// call with the SAME `at` and `dur` as the scene's ken, and the OPPOSITE sign.
function parallax(sel, at, dur, amt, sign) {
  var a = amt == null ? 18 : amt, s = sign == null ? 1 : sign;   // px of total travel
  tl.fromTo(sel, { x: -s * a / 2, scale: 1.0 },
                 { x:  s * a / 2, scale: 1.012, duration: dur, ease: "none" }, at);
}
```

- **Serves:** every scene, one call each, paired to that scene's `ken`.
- **Why:** it is the cheapest depth cue that exists and it makes the `ken` legible
  by giving the eye a stationary reference to measure it against. On s7 the ken is
  0.32 px/frame; add 18 px of counter-travel and the *relative* motion doubles for
  five lines of code.
- **Caution:** `x` on `.stack` must not collide with a `rise`'s `y` on a child —
  it does not, they are different elements.
- **LOC:** 4. **Cost: cheap.** **Owner:** `fin-build`.

---

### 3. `countDown(sel, from, to, at, dur)` — a number that descends

```js
function countDown(sel, from, to, at, dur, prefix, suffix) {
  var el = document.querySelector(sel), o = { v: from };
  tl.to(o, { v: to, duration: dur == null ? 1.6 : dur, ease: "power2.out",
    onUpdate: function () { el.textContent = (prefix || "") + NUMFMT.format(Math.round(o.v)) + (suffix || ""); } }, at);
}
```

- **Serves:** s7 THE MATH — balance falling $6,000 → $5,318 over a year;
  months-remaining 215 → 0; "interest saved" when the extra payment lands in s6.
  Also s1's `$170 → $60 off the debt`.
- **Seek-safe:** the proxy object is written by `onUpdate` only, so scrubbing
  backwards recomputes it from timeline time. `Math.round` + existing
  `tabular-nums` + the existing `NUMFMT` `Intl.NumberFormat` per cut locale.
- **Note:** this is `countUp` with the endpoints swapped and a decelerating ease.
  Merge them: `count(sel, from, to, …)` and delete `countUp`/`countSteps`. One
  helper, both directions, kills the three-different-counters drift in §1.1.
- **LOC:** 6. **Cost: cheap.** **Owner:** `fin-build`.

---

### 4. `drain(sel, at, dur, dx, dy)` — value leaving the frame

Accelerating exit with travel and a fading blur, instead of `exit`'s flat opacity.

```js
function drain(sel, at, dur, dx, dy) {
  tl.fromTo(sel, { x: 0, y: 0, opacity: 1, filter: "blur(0px)" },
                 { x: dx == null ? 0 : dx, y: dy == null ? -70 : dy, opacity: 0,
                   filter: "blur(6px)", duration: dur == null ? 0.5 : dur, ease: "power2.in" }, at);
}
```

- **Serves:** the "this is what you lose" beats — s1 `INTEREST $110` draining
  off-frame, s3's `RENT ON A GHOST`, s4's bad-debt tags. Also every focal handoff
  where the outgoing element is the *loss* rather than just the previous point.
- **Why it matters:** it is the only motion in the proposal with a *direction of
  meaning*. Money that leaves should travel; money that stays should not.
- **Caution:** `filter` on a text node is a paint op, cheap; do not apply to a
  full-frame layer.
- **LOC:** 5. **Cost: cheap.** **Owner:** `fin-build`.

---

### 5. `draw(sel, at, dur)` — SVG stroke drawing

```js
// build-time, once, outside the timeline:
//   var L = document.querySelector(sel).getTotalLength();
//   el.style.strokeDasharray = L; el.style.strokeDashoffset = L;
function draw(sel, at, dur) {
  var el = document.querySelector(sel), L = el.getTotalLength();
  el.style.strokeDasharray = L;
  tl.fromTo(el, { strokeDashoffset: L }, { strokeDashoffset: 0,
    duration: dur == null ? 1.4 : dur, ease: "power1.inOut" }, at);
}
```

- **Serves:** s5 `INTEREST ON INTEREST` — the compounding curve, which is the one
  idea in the whole video that *is* a shape. s7 — the 215-month payoff line. s6 —
  the "+$20/mo cuts years off" delta between two curves.
- **Determinism:** `getTotalLength()` runs at build (§4.4 gotcha). Works under
  `visibility: hidden`; would return 0 under `display: none`, which our
  absolutely-positioned scenes never get.
- **No DrawSVGPlugin** (not in the vendored bundle) — raw dasharray is the
  supported path and is what `hyperframes-animation/rules/svg-path-draw.md`
  specifies anyway.
- **Requires** an inline `<svg>` in the scene DOM → a storyboard change, not just
  a build change. That is what makes it medium rather than cheap.
- **LOC:** 6 helper + ~10 lines of SVG per use. **Cost: medium.**
  **Owner:** `fin-storyboard` (the curve is a storyboard decision) + `fin-build`.

---

### 6. `rack(focalSel, restSel, at, dur, px)` — rack focus instead of emptying the frame

```js
function rack(focalSel, restSel, at, dur, px) {
  var d = dur == null ? 0.6 : dur, b = px == null ? 5 : px;
  tl.to(restSel,  { filter: "blur(" + b + "px)", opacity: 0.45, duration: d, ease: "power2.out" }, at);
  tl.fromTo(focalSel, { filter: "blur(" + b + "px)", opacity: 0.45 },
                      { filter: "blur(0px)", opacity: 1, duration: d, ease: "power2.out" }, at);
}
```

- **Serves:** every scene that currently does `exit(a); exit(b); exit(c); pop(d)`
  — i.e. s1, s3, s5, s6, s7, s8 in good-debt-en. This is the direct fix for the
  dead-air problem in §1.3: the frame stays full, the focal changes optically, and
  the 2.5–6.6 s "empty stage then one lone pop" runs disappear.
- **Satisfies the standing "one focal per scene" rule** better than `exit` does,
  because a de-emphasised element still gives the composition mass.
- **Cost note:** `filter: blur()` on 3–4 text blocks is fine. Never blur the
  1920×1080 `.bg` this way — that is the one thing here that would cost real
  render minutes.
- **LOC:** 6. **Cost: medium** (render time, and it needs `will-change: filter`).
  **Owner:** `fin-build`, with `fin-storyboard` declaring which element is focal
  at each cue.

---

### 7. `slam(sel, at, over)` — impact arrival for the verdict

Replaces the ubiquitous `pop(...)` + `pulse(...)` pair (11–13 pulses per cut, §1.6)
with one call that actually reads as impact.

```js
function slam(sel, at, over) {
  var o = over == null ? 1.5 : over;
  tl.fromTo(sel, { opacity: 0, scale: o, rotation: 0 },
                 { opacity: 1, scale: 0.97, duration: 0.22, ease: "power4.in" }, at);
  tl.to(sel, { scale: 1, duration: 0.34, ease: "elastic.out(1, 0.55)" }, at + 0.22);
}
```

- **Serves:** `.stamp` (s1 `IT'S A TRAP`, s4 `CARD BALANCE = WORST`, s8
  `DO THIS TODAY`), the s7 punch headline, the `.cta`. The signature beats.
- **Why:** `pop` arrives *from small* — it grows into place, which reads gentle.
  A verdict should arrive *from large* and settle. Different physics, same LOC.
- **LOC:** 6. **Cost: cheap.** **Owner:** `fin-build`.

---

### 8. `stack(sel, at, gap, dur)` — accumulation

```js
function stack(sel, at, gap, dur) {
  var g = gap == null ? 0.16 : gap, d = dur == null ? 0.45 : dur;
  tl.fromTo(sel, { opacity: 0, y: 70, scaleY: 1.06 },
                 { opacity: 1, y: 0, scaleY: 1, duration: d, ease: "back.out(1.2)", stagger: g }, at);
}
```

- **Serves:** the roadmap chips (s2), the classifier tags (s4), the recap chips
  (s9) — everywhere `popEach` is used today. Also any savings/accumulation beat.
- **Why:** `popEach` pops items in place (they *appear*). `stack` travels them up
  from below with a squash on land — they *pile up*. Same cost, correct metaphor
  for money.
- **Guardrail:** `items × gap ≤ ~0.5 s` per the skill's contract, and the existing
  cascade rule (≤5 items @ 0.6–0.7 s) governs when it may be used at all.
- **LOC:** 5. **Cost: cheap.** Straight replacement for `popEach`/`riseEach`.
  **Owner:** `fin-build`.

---

## 6. Proposal — the scene-transition system

### 6.1 The mechanism (three lines of scaffolding, then it just works)

1. Add `T` to `data-duration` on sections **s1…s8**. Leave `data-start`, the JS
   `S` map, the `<audio>` rows, section **s9** and the root `data-duration`
   untouched.
2. Add `T` to the `ken(...)` duration for s1…s8 so the background doesn't freeze
   under the handoff.
3. Add the transition call at each boundary.

Why this is safe and cheap:
- `pipeline_check.check_html` only compares the root duration to the **last**
  scene's end (§4.2). Unchanged → still passes.
- The VO timing contract (`scene_duration = 0.4 + clip + 1.0`) is untouched —
  audio rows keep their own `data-start`.
- The clip runtime writes only `visibility` (§4.1), so `opacity`/`transform` on a
  section are free.
- All four copies of the timing numbers still agree, because only one of them
  (the section `data-duration`) changes and it changes by a constant the generator
  emits.
- **Two scenes are alive at once during the overlap** — the `max_simultaneous_elements: 6`
  rule is a per-scene rule; the overlap must not coincide with a cue. Rule:
  **no cue may fire within T of a scene boundary on either side.** Today the last
  cue in every scene already lands ≥1.0 s before the end (the tail), so T ≤ 0.6 s
  costs nothing.

### 6.2 The three transitions

#### T1 — `dissolve` — the primary, 6 of 8 boundaries

```js
function dissolve(nextSel, at, dur) {           // at = the incoming scene's data-start
  tl.fromTo(nextSel, { opacity: 0 }, { opacity: 1, duration: dur == null ? 0.45 : dur, ease: "power1.inOut" }, at);
}
```

One tween. The incoming section is later in DOM and opaque, so fading it in *is*
the crossfade — the outgoing scene needs no tween at all, which also means we
never violate the skill's "exits are banned as transitions" rule.

- **When:** default. Between related points inside the same act.
  good-debt boundaries s1→s2, s2→s3, s3→s4, s4→s5, s7→s8, s8→s9.
- **T = 0.45 s.** **LOC: 3.** **Cost: cheap.**

#### T2 — `shove` — the section break, at most 2 per video

```js
function shove(prevSel, nextSel, at, dur) {
  var d = dur == null ? 0.42 : dur;
  tl.to(prevSel,  { yPercent: -7, filter: "blur(7px)", duration: d, ease: "power3.in" }, at);
  tl.fromTo(nextSel, { yPercent: 7, opacity: 0 },
                     { yPercent: 0, opacity: 1, duration: d, ease: "power3.out" }, at);
}
```

Both scenes move at the same timeline position — the motion *is* the handoff, per
`transitions/overview.md`. Signals "new section, reset your attention".

- **When:** at a declared act change only. blockframe-9's act structure is
  hook+roadmap | concept+rule | mechanism+action | the math | do-this+recap.
  Use `shove` at the two structural breaks the storyboard names — for good-debt:
  **s5→s6** (mechanism → action).
- **T = 0.42 s.** **LOC: 5.** **Cost: medium** (a 0.42 s full-frame blur ×2).

#### T3 — `gate` — the climax, exactly once per video

```js
// DOM: one <div id="gate"> fixed full-frame, background: var(--bg), opacity: 0, z-index: 50
function gate(at, dur) {
  var d = dur == null ? 0.5 : dur;
  tl.fromTo("#gate", { opacity: 0 }, { opacity: 1, duration: d / 2, ease: "power2.in" }, at - d / 2);
  tl.to("#gate", { opacity: 0, duration: d / 2, ease: "power2.out" }, at);
}
```

A dip through the design system's own `--bg` (`#0d1017`, not black — it stays
inside the palette). The next scene emerges out of darkness.

- **When:** exactly once, on the boundary immediately before the video's single
  biggest number. good-debt: **s6→s7**, so `$9,506 INTEREST > $6,000 BORROWED`
  lands out of a dip instead of a cut.
- Requires the boundary to straddle the dip, so both scenes overlap by `d`.
- **T = 0.5 s.** **LOC: 4 + one div.** **Cost: cheap.**

#### Plus: open and close

```js
tl.fromTo("#gate", { opacity: 1 }, { opacity: 0, duration: 0.7, ease: "power2.out" }, 0);
```

Reuses the same `#gate` div for a 0.7 s fade-up from `--bg` at t=0. The video
currently starts on a fully-lit frame mid-thought. **LOC: 1. Cost: cheap.**

### 6.3 The selection rule (one paragraph, for the storyboard template)

> Default every boundary to `dissolve` (0.45 s). Promote a boundary to `shove`
> (0.42 s) only where the storyboard declares an act change — at most two per
> video. Use `gate` (0.5 s) exactly once, on the boundary immediately before the
> video's single biggest number. Never place two non-`dissolve` transitions
> adjacent. Open the video on a 0.7 s fade from `--bg`. No cue may fire within
> 0.6 s of any boundary, on either side. The storyboard names the transition per
> boundary in a `Transition` column — restoring the column that
> `vault/skills/hyperframes_production.md` line 57 already requires.

### 6.4 Total cost of the transition system

8 boundaries × 1 call, 3 helper functions (12 LOC), 1 `<div>`, 1 CSS rule, and a
constant added to nine `data-duration` values and nine `ken` durations by the
existing generator. **This is a one-evening change to `fin-build.md` plus one
column in the storyboard template.** It is the highest leverage item in this
document by a wide margin.

---

## 7. What to STOP doing

### Delete outright

**`breathe` — dead weight, delete.** §1.5: 1.035× over 1.5 s ≈ 0.09 px/frame on a
112 px headline — a quarter of the already-invisible `ken`, and comfortably below
the measured 0.053–0.377 in-scene frame-delta floor. It fires 8× per hi cut and
contributes nothing a viewer can see. Worse, it is the alibi that lets a composer
believe "no static frame beyond 2 s" is satisfied when §1.3 shows it is violated
21–28 times per cut. And its `dur` parameter runs 1.4–2.0× long, so the composer's
timeline model is wrong wherever it is used. If a genuine idle is wanted, one
helper at 1.09× / 2.0 s would be visible — but with `parallax` (#2) on every
scene there is no scene left that needs an idle.

**`drift` — dead documentation, delete.** `design-finance-blockframe.md` §5
defines it as "slow one-way scale **for photo-free scenes**". Photo-free scenes
were retired by creator rule 2026-07-28 and `format.json photo_free_scene_ratio`
is `0`. The doc then contradicts itself two lines later ("`drift` survives only as
the motion for overlay stacks"). It appears in 4 of 12 compositions and in neither
of the two most recent. `parallax` (#2) subsumes the only remaining use.

### Fold into something else

**`pulse` — stop shipping it standalone.** 11–13 calls per cut, and in nearly
every case it is `pop(x, t)` immediately followed by `pulse(x, t+0.5)` — two calls
to express one beat, and 0.16 s at 1.12× is five frames. It is the most
recognisable template tic in the format. Fold the impact into `slam` (#7) for
verdicts and into `pop`'s ease for everything else. Keep it available for the one
genuine use (re-emphasising an element already on screen when the VO names it a
second time), capped at ≤2 uses per video.

**`countUp` / `countSteps` — merge into one `count(sel, from, to, …)`.** Three
different counter helpers across six topics (§1.1) is pure copy-paste drift, and
the newest composition ships with none of them.

**`popEach` / `riseEach` — replace with `stack` (#8).** Same cost, better
metaphor, one name instead of two.

### Recalibrate, don't delete

**`ken` — make the *rate* constant, not the endpoints.** §1.4: fixed endpoints
over a variable duration means the camera is slowest on the longest scenes —
0.32 px/frame on s7, the payoff. Replace the fixed `1.00 ↔ 1.16` with a scale
delta derived from duration to hold ~25 px/s at the frame edge:
`delta = clamp(0.10, rate * dur / 960, 0.24)`. Roughly 2 extra lines inside `ken`.
**Cost: cheap. Highest ratio of visible improvement to LOC in this document
after the transitions.**

**`exit` — cut its use roughly in half, and never use it as a transition.** 23
calls in good-debt-en. Its legitimate job is focal handoff inside a scene, and
that job is real. But it is the direct cause of the dead-air clusters (§1.3):
`exit` at +12.3 → `pop` at +13.0 → 2.7 s of nothing. Replace the "clear the stage
then reveal" pattern with `rack` (#6) wherever the outgoing content is still
*true* (a mechanism you're building on), and with `drain` (#4) wherever it is a
*loss* (money spent, a bad option rejected). Reserve plain `exit` for content that
is genuinely finished. And once §6 lands, `exit` must never fire within T of a
boundary — that produces the "jump cut with a dip" the animation skill explicitly
bans.

### Nothing to stop — but a hole to plug

**Add a motion assertion to `tools/pipeline_check.py`.** `format.json` already
declares `scene.max_static_hold_seconds: 2.0`, `layout.cue_min_gap_seconds: 0.8`,
`layout.max_simultaneous_elements: 6` and the cascade window — and **nothing reads
any of them.** The parser in this research
(`scratchpad/q.py`, ~60 lines) computes the static-run table in §1.3 from
`index.html` alone. Porting it into `check_html` as a `motion` stage would have
caught 21 rule violations in the video that shipped last week. Alternatively, the
installed skill already ships
`hyperframes-animation/scripts/animation-map.mjs`, which computes dead zones from
the live timeline — free, and more accurate than a regex parser.

---

## 8. Contradictions with what the vault currently documents

| # | Vault says | Reality | Evidence |
|---|---|---|---|
| 1 | `design-finance-blockframe.md` §5: "**Nine helpers**" | 5 different vocabularies across 6 topics. good-debt (the newest, and the file `fin-build.md` names as the reference implementation) is missing `fill`, `countUp` **and** `drift`; `exit` and `popEach` are used heavily and documented nowhere | §1.1 |
| 2 | §5 rule 2 + `format.json max_static_hold_seconds: 2.0` + every storyboard's guardrail block: "**No static frame beyond ~2 s**" | 21 violations per en cut (worst **6.6 s**), 28 per hi cut. Nothing checks it — `pipeline_check.py` has zero motion assertions | §1.3, §7 |
| 3 | The vault documents **no scene transitions at all** | The installed `hyperframes-animation` skill's rule #1 is "**Every composition uses transitions. No exceptions.**" Twelve shipped compositions hard-cut, confirmed from rendered pixels | §1.2, §4 |
| 4 | `vault/skills/hyperframes_production.md` line 57 requires a `Transition` column in every storyboard row | The finance storyboard template dropped it; no finance storyboard has ever specified a transition | §1.2 |
| 5 | §5: "`breathe` … **odd repeat count** so it ends where it began, `1.5 s` cycles" | True about the endpoint, misleading about duration: `breathe(x, t, 3.0)` runs **6.0 s**. Composers mis-time it — good-debt s1 breathes an element for 2.6 s after `exit` has already hidden it | §1.5 |
| 6 | §5: "`drift` — slow one-way scale **for photo-free scenes**" | Photo-free scenes retired 2026-07-28; `photo_free_scene_ratio` is `0`. The same doc contradicts itself two lines later. Absent from both newest compositions | §7 |
| 7 | `fin-build.md` step 1: "read the **newest archived** `index.html` as the reference implementation" | The newest archive has the smallest vocabulary. This rule is a ratchet that loses a helper per video. The reference should be a checked-in `tools/scaffold/motion.js`, not whatever shipped last | §1.1 |
| 8 | §5 rule 1: "Alternate `ken` direction. Never two pushes in a row." | Sound in principle, but with hard cuts the background reverses direction instantly at every boundary. **UNVALIDATED** whether this is perceptible across a photo change; it becomes unambiguously correct once §6 lands and the reversal happens under a dissolve | §1.2 |

---

## 9. Ranked change list

| # | Tag | Change | Why | Cost | Owner |
|---|---|---|---|---|---|
| 1 | FACT | Ship the 3-transition system (§6): extend `data-duration` on s1–s8 by T, add `dissolve`/`shove`/`gate`, open on a 0.7 s fade from `--bg` | The video hard-cuts 8× — measured at 16–200× the in-scene frame delta. The framework only owns `visibility`, so opacity is already free; `pipeline_check` already permits overlap | cheap (12 LOC + 1 div + a constant in the generator) | `fin-build.md`, `.claude/agents/fin-storyboard.md` (add the `Transition` column), `vault/knowledge/design-finance-blockframe.md` §5 |
| 2 | FACT | Make `ken`'s **rate** constant instead of its endpoints | s7 currently moves 0.32 px/frame; the payoff scene is the closest thing to frozen in the video | cheap (2 LOC) | `fin-build.md` |
| 3 | FACT | Add `rack` + `drain`, cut `exit` use ~50% | `exit` is the direct cause of the 2.5–6.6 s dead-air runs; 65% of the en cut has zero foreground motion | medium | `fin-build.md`, `fin-storyboard.md` |
| 4 | FACT | Move the helper library into `tools/scaffold/motion.js` and delete "read the newest archive" from `fin-build.md` step 1 | 5 vocabularies, 3 counter helpers, and 3 missing helpers in the newest video — the reference-implementation rule is a ratchet | cheap | `.claude/agents/fin-build.md`, `tools/scaffold/` |
| 5 | FACT | Add a `motion` stage to `pipeline_check.py` asserting `max_static_hold_seconds`, `cue_min_gap_seconds`, `max_simultaneous_elements` | Four `format.json` constants are read by nothing; 21 violations shipped last week | cheap (~60 LOC, already written in `scratchpad/q.py`) or free via `animation-map.mjs` | `tools/pipeline_check.py` |
| 6 | FACT | Delete `breathe` and `drift`; fold `pulse` into `slam`; merge `countUp`/`countSteps` into `count`; replace `popEach` with `stack` | Invisible motion, retired-feature motion, and copy-paste drift | cheap (net deletion) | `fin-build.md`, design doc §5 |
| 7 | UNVALIDATED | Add `wipe` and `parallax` to every scene | Masked reveals + photo/type depth are the two most-cited premium tells and the two cheapest to add. No audience data | cheap | `fin-storyboard.md`, `fin-build.md` |
| 8 | UNVALIDATED | Add `draw` for the one curve per video (compounding, payoff) | The abstract-made-visible pattern is what the benchmark sources converge on; currently the curve is delivered as 96 px caps | medium (needs SVG in the storyboard) | `fin-storyboard.md` |
| 9 | FACT | Do **not** adopt `@hyperframes/shader-transitions` | Its `HyperShader.init()` requires removing `class="clip"` from scene divs, incompatible with blockframe-9's timing contract; and its html2canvas capture rules are violated by our `.scrim` gradients, `var(--tint)` and CSS-drawn glyphs | — | — |

---

## 10. Open questions I could not answer from here

1. **No competitor frame-by-frame.** §3's benchmark rests on SEO listicles. The
   honest version is to pull 3 top-performing videos each from @cashguruguides'
   and @moneymavens101's actual competitor set, measure their cut rate and their
   moving-vs-static ratio with the same `scdet` method used in §1.2, and compare
   to our 34.6%. That is a two-hour job with the tools already installed, and it
   would convert most of §3 from UNVALIDATED to FACT.
2. **No analytics.** Every claim about what motion does to retention is
   unvalidated by construction. The first A/B worth running is the transition
   system (§6) alone, on one pair, because it is one variable and one evening.
3. **The 0.32 px/frame perceptual claim** is arithmetic plus an inference about
   YouTube's transcode. Confirmable by uploading an unlisted 30 s clip and
   measuring the delivered stream's frame deltas.
