# fin-build · japanese-money-methods · en · chapter 1 · attempt 3
STATUS: ok — one file touched, `studio/videos/japanese-money-methods-en-ch1/chapter.json`.

Nothing scaffolded, nothing generated, nothing rendered, no snapshot pass. The
shipped cut and the chapter's `index.html` were read only. `npm run check` was
NOT run: the thing it checks does not exist until the caller re-runs
`tools/chapter_project.py`, which is the caller's step.

## What changed, per finding

### Finding 12 — Lotties, 0 → 2 (cap 4)
Top-level `"lottie": ["phone-on-counter-night", "calendar-20th-circled"]`, which
is what wires both `<script src="assets/lottie/<name>.js">` rows *and* pulls in
`lottie.min.js`. Both are loaded through `loadLottie` / `playLottie` and nothing
else — no `window.__hfLottie`, no bare `lottie.loadAnimation`, no `path:` URL.

**s1 · `phone-on-counter-night`.** `<div class="lottie v-phone" id="s1-phone">`,
z 0, `inset:-8%`, kenned. It plays at TRUE speed (180f / 30fps = 6.00s) inside a
4.489s scene rather than being compressed to fit — the asset's whole read is a
buzz, and 1.34× turns a buzz into a glitch. Frames past 4.489s are simply never
seen. Verified against the asset itself, not assumed: every layer is at opacity
100 from frame 0 **except layer 7, which is 0 until frame 24 and 100 at frame 27**
— so the phone and the counter are present at frame 0 of the video and only the
notification animates in, which is exactly what the work order asked for. Buzz 1
lands at 0.80s, buzz 2 at 3.60s, and the notification is still lit when s2
dissolves over it.

**s7 · `calendar-20th-circled`.** `<div class="lottie v-cal" id="s7-cal">` at
z 2 (above the scrim — a ringed date dimmed by the scrim is the one thing this
scene cannot afford), 740×460 in B's right half. Cue is `S.s7 + 1.30`, the same
cue the BALANCE bar spans on: the days burning down and the balance draining are
one sentence, not two. 105 frames over 3.05s = 1.15×, landing the ring at +4.35,
0.03s before the cross-dissolve starts, so a ringed 20th is the last thing the
scene holds. Its own colours are the asset's (retinted at fetch); nothing is
hard-coded here.

### Finding 5 — s6 drawn slip count
`art: "forward"` + `<g id="s6-slips">` + a 44-rect DOM build on the `i*7 mod 44`
offset, ported from -hi. Two notes the port turned up:

- **-hi's `#s6-slips` is dead code.** Its section is `arch-d has-photo art-off
  centred`, and both `.has-photo.art-off .art { display:none }` and
  `.scene.centred .plate { display:none }` fire, so the reference chapter never
  shows a single one of those 44 slips. The editor's finding describes art that
  is in the file but not on screen. Here they are actually on: `art-forward`,
  plate on (arch-a ⇒ `.p-a`, full frame), `centred` false by construction.
- Grid moved into the lower band (x 426–1493, y 680–950) so it clears the
  centred type and the watermark box, and got a `.band` at `z-index:0` behind it
  — the s9 pattern. **The photograph is not darkened; the band is.** (Rule 9.)
- -hi's dashed 300×264 "nothing big" rectangle was **not** ported. It needs a
  caption to read as an absence, and an uncaptioned empty box next to a field of
  filled ones is precisely the "reads as nothing" defect finding 9 raises against
  s4's stray red mark.

### Finding 9 — s4 art lies
**Recounted to ONE against SIX** (not 6-of-12) and I'll say why: "six months
where you budgeted one" has no denominator in it. One dim cell, a gap, six lit
cells at the same rect and the same pitch — no twelve, no ten, no percentage,
nothing that could be mistaken for a published figure. 6-of-12 would have
imported a calendar year the copy never mentions.

The stray red `62×8` at x=46 y=404 is **dropped**, and the space it occupied is
now two measurement rules — a 62-wide underline under the single cell and a
442-wide one under the six. That is the "or label it" half of the finding: the
mark now states the span of each group instead of sitting there.

**Plate geometry is untouched** as instructed: still `p-b`, still viewBox
`0 0 860 610`, still 62×138 cells on a 76 pitch, still baseline y=236/398. Only
the count and the horizontal spacing moved. `art-lift` and `art-forward` stay.

### Finding 8 — s9 invisible art
Root cause found, and it is not the number in the spec. `chapter-design.css`
carries `.has-photo.art-forward .art { opacity: .52 !important }`, so the spec's
inline `opacity:.6` on `#s9-art` was **dead** — the container rendered at .52 and
the streams carry their own `.6` on top, i.e. **.31 effective**. Raising the spec
value alone would have changed nothing and we'd have burned another render.

Fixed at both ends: the streams now carry no opacity of their own, the holes went
.55 → .85, the header rail .3 → .5, and the container is lifted by id in the
chapter's own `<style>`:

```css
#s6-art, #s9-art { opacity: .78 !important; }
```

Streams therefore render at .78 against .31. No design token moved and the global
cap is untouched — this is a per-scene, per-id lift, in the composition's own
style block, which is where a one-off belongs.

## Round 2 — the coordinator's two questions, resolved

### 1 · s1 + s2 — chose **(a)**, extend the Lottie across both. Implemented.
Two synchronised instances, `#s1-phone` and `#s2-phone`, identical markup and
identical `.v-phone` box, both playing from the **same absolute cue**:

```js
playLottie(phone,  S.s1, 6.00);   // s1
playLottie(phone2, S.s1, 6.00);   // s2 — S.s1, deliberately, not S.s2
```

`playLottie` derives its frame from the tween's own progress against the global
timeline, so two instances given the same window are showing the same frame at
every `t`. Through the 0.45s dissolve at 4.039 the outgoing and incoming layers
are pixel-identical and there is nothing for the cross-fade to ghost against —
which is the exact defect (self-dissolve flicker) the editor caught on the
photograph pair. Set the s2 cue to `S.s2` and the phone snaps back to frame 0
mid-cut; that is the one line in this file that will break silently.

**Why not one element, as -hi does it.** -hi hangs a single `#ch1-phone` off
`#root` on its own track spanning both scenes. `chapter.json` has no hook for
root-level markup — the generator emits `<section>`s and `<audio>` rows and
nothing else inside `#root` — and building a `clip` from script would be
invisible to `hyperframes lint` and to the renderer's DOM scan. Two synchronised
instances is the version that survives the generator without editing it.

**The push.** `plateKen`, matching your rewiring, on the phone elements instead
of the hidden `.bg`s: `plateKen("#s1-phone", 0, 4.039, 1.00, 1.10)` then
`plateKen("#s2-phone", 4.039, 7.885, 1.10, 1.24)`. Note s1's is **4.039, not
4.489**. Your `#s1-bg` version runs to 4.489, so at the handoff it is at 1.0898
while s2 starts at 1.100 — a 0.9% scale mismatch held across the whole dissolve.
Ending s1's push at 4.039 makes the handoff exact; the outgoing copy is then
static for 0.45s while it fades, which is strictly the smaller artefact. Worth
copying back onto `#s1-bg` / `#s2-bg` if you ever un-hide them.

**One pass, not two.** True speed, 180f / 30fps = 6.00s, then it holds on its
last frame while the push keeps moving. -hi plays the loop twice because it has
no other motion in the scene; here that would put a second notification on screen
at 6.8s, i.e. assert that the deposit landed twice. The ken carries the back half
of s2 instead. Notification arrives 0.80s, buzzes again 3.60s, gone by ~5.7s.

**Cost, stated plainly: `s1-fix.jpg` is now unused on both scenes** (`#s1-bg,
#s2-bg { display: none }`). I could not find a version that keeps it. Option (b)
is not achievable against this file and here is the specific reason, having
looked at it: the phone is lying at a steep perspective angle with the screen
face reading as a **quadrilateral**, not a rectangle — top-left corner around
0.21/0.39 of the frame, bottom-right around 0.79/0.63, home-button ellipse at
roughly 0.63/0.58. A notification bar has to land inside that quad and stay on it
through a 1.00 → 1.24 push. The tracking half is solvable exactly (wrap it in a
div at the same `inset:-8%` box and drive it with the identical `plateKen` —
same box, same origin, same scale, so it cannot drift). The **registration** half
is not: it is a hand-fitted perspective polygon on frame 0 of the video, at two
different scales, that I have no way to check because I cannot render. A
misregistered lit rectangle on a photographed phone is a worse defect than a
clean drawn phone, and it would also drop the Lottie the creator asked for by
name. If you want (b) anyway, say so and I will author the quad — but budget a
render to fit it.

Consolation: the photograph is not wasted work in the way a wrong-currency image
is. It is a correct, on-brief US night still and it is the natural candidate for
any later beat that wants "the phone, after" — but not in this chapter, where s1
and s2 are the only phone lines.

### 2 · s7 — the photograph brief
The scene already states its argument **twice**: the BALANCE bar draining on the
left and the month grid burning down to a ringed 20th on the right. So the
photograph must not argue at all. Its job is **the room and the hour** — where
and when this is happening — and nothing else. Anything that also says "the money
is gone" makes three voices saying one thing.

**Ask for:** *late-afternoon or early-evening sunlight falling in a low, hard
shaft across an empty kitchen wall and counter corner in a US apartment — no
objects on the surface, no people, no paper, no text, no device, deep shadow on
the near side, the light doing all the work. Shot slightly wide, subject in the
lower-centre band.*

Why this one:
- It is a **texture and a light direction**, not a subject, so it survives being
  the third layer under two graphic ones.
- It supplies the thing neither the bar nor the grid can: **an hour of the day**,
  which is what "by the twentieth" is actually about — time having passed.
- It rhymes with s1's night kitchen, so the chapter reads as one apartment across
  one month rather than as ten unrelated stock frames.

**Framing constraint to pass on:** the calendar occupies x 1140–1880 and the type
occupies x 212–1112, so any strong subject in the upper right will fight the
grid. An all-over texture or a lower-centre subject is safe; a single object in
the top-right corner is not.

**Fallback if that query returns nothing usable:** *the dark side of an apartment
hallway or doorway with the light on in the next room, no people, no text, no
screen.* Same properties — place and hour, no argument.

**Explicit negatives for the query:** no calendar, no clock, no date, no diary,
no planner, no phone, no laptop, no monitor, no envelope, no bill, no receipt, no
money, no readable text of any kind, no people. Also avoid an empty chair at a
table (that is s10) and water on glass (that is s9's new still).

### 3 · s6 — noted, no change. Left `art-forward`.

## Rule 8 / rule 9 / truth-bar calls you need to overrule or accept

These are the photograph-facing consequences of art you asked for. Photographs
are yours; these are the three places where your choice and mine have to agree.

1. **s1 + s2 — resolved above (option a).** `#s1-bg, #s2-bg { display: none }`;
   the Lottie is the picture for the whole 11.924s hold. Escape hatch if you want
   the photograph back: delete the `html`/`motion` blocks on s1 and s2 and the
   `#s1-bg, #s2-bg` rule from `css`. A third route exists if you ever want the
   photograph AND a drawn layer — `phone-notify-credit` (820×300, two layers,
   transparent, 2.5s, already in the cut's lottie dir) is a bare notification
   banner with a bloom, which is additive over a phone still — but it needs the
   perspective registration described above and a render to fit it.
2. **s7 — resolved above.** Brief written; the photograph must not be a calendar
   and must not carry a date.
3. **s6 is the marginal one.** 44 drawn slips over a photograph of fanned
   receipts is close to depictive. It survives rule 8 only on the count: uniform
   identical rects on a strict 11×4 grid read as a **tally**, which is a claim
   ("forty-four, none of them big"), where the photograph only says "some
   receipts". If the s6 still ends up being a large, legible, countable spread,
   set `"art": "off"` on s6 and drop its `svg`/`html`/`motion` — one edit.

Nothing added states a figure. No numerals, no percentages, no axis, no
denominator anywhere in s4, s6 or s9.

## One layout change beyond the four findings, flagged because you praised s7
s7 is now `"centred": false`. It had to be: `.scene.centred .plate` and the whole
re-centring block exist because `art-off` left B's right half empty, and it is
not empty any more. The stack moves to B's left column with the vrule back on and
the 900px `.huge` measure ends at x=1112; `.v-cal` starts at x=1140. **The measure
bar and its now-inline BALANCE label are untouched** — `.measure.under` /
`.measure-lab.under` are fixed at `calc(50% - 460px)` and are independent of the
stack, which is what the arch-b scenes in ch4 already look like.

## What to check in the encoded mp4 — Lottie has two silent-blank failure modes
I cannot render, so these are the frames that discriminate. Times are
chapter-local (add the chapter offset for the full cut).

**Before anything else:** re-run the generator with `--scaffold`. The chapter dir
has `assets/js/lottie.min.js` but **no `assets/lottie` symlink** — that link is
only created by `scaffold()`, and without it both `<script>` rows 404, both
`L_*` globals are undefined, `loadLottie` throws, and the two scenes render as
photograph-plus-type while `hyperframes check` passes clean.

| scene | frame | must show | what it means if it doesn't |
|---|---|---|---|
| s1 | **0.30s** | phone + counter, **no** notification bar | blank/flat field ⇒ asset never loaded (missing `assets/lottie` link, or a wrong `L_*` global) |
| s1 | **1.20s** | a lit notification bar above the phone | identical to 0.30s ⇒ the tween never advanced the frame (seek not wired) |
| s1 | **3.80s** | second buzz; bar still lit, phone offset | identical to 1.20s ⇒ same as above |
| s1→s2 | **4.15s** (mid-dissolve) | ONE phone, no doubled edge, no ghost | a doubled/offset phone ⇒ s2's `playLottie` cue is `S.s2` instead of `S.s1`, or the two `plateKen` endpoints do not meet at 1.10 |
| s2 | **8.00s** | same phone, pushed in further, notification gone | a phone with a notification again ⇒ someone added the second loop pass back |
| s7 | **37.61s** (S.s7+0.6) | right half empty, type left, vrule on | calendar already complete ⇒ frozen on last frame |
| s7 | **38.50s** (S.s7+1.5) | grid part-drawn, ring **not** yet closed | — |
| s7 | **41.20s** (S.s7+4.19) | the 20th ringed in `--warn`, days 1–19 dimmed | right half still empty ⇒ asset never loaded; identical to 38.50s ⇒ seek not wired |

The single strongest tell for both is **two frames of the same scene being
pixel-identical**. `playLottie` derives its frame from the tween's own progress,
so if any two of those timestamps match, the animation is stuck on frame 0 or on
its last frame and the wiring is wrong — that state passes `hyperframes check`.

Second tell, s6/s9 specifically: at **s6+3.9s** the 44 slips should be fully in
and *countable*; at **s9+2.6s** all 24 streams should be down and clearly red
against the band. If either is present-but-grey, `#s6-art, #s9-art` in the
generated `<style>` got dropped and the `.52 !important` cap is back.

## Not done / not mine
- No `npm run check`, no snapshot pass, no render — all three need the generated
  `index.html`, which is yours to produce.
- No photograph, `source new` or `reuse hi` row touched. Findings 1 (photo half),
  2, 3, 4, 6 (photo half), 7, 10 and 11 are untouched by this stage.
- No new icon written to `assets/icons/` — nothing here wanted one.
- No helper redefined inline; every motion call is `loadLottie` / `playLottie` /
  `ken` / `pop` / `popEach` / `fade` from `motion.js`, plus two `tl.fromTo` loops
  for the 44- and 24-element sets, which is the pattern -hi already uses and the
  only way to build a set that large deterministically.
