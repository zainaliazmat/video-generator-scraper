# fin-build · financial-freedom-after-50 · en · chapter 2 · attempt 1

New chapter project, scaffolded from `tools/scaffold/` (not from ch1, not from any shipped
`index.html`). 17 scenes (s12–s28, VO 2.1–2.17), **108.659 s**, one drawn layer (the s18
icon), one cut-in photo swap (s23b), one num scene (s17), one chip row (s16).
`npm run check` → **PASSED**, 0 errors, 12/12 contrast. 25 snapshot frames in 2 separate
`-o` directories, all 25 looked at.

## Ran

1. Read `vault/CLAUDE.md`, `tools/packs/fin-build.md`, `tools/format/fin-build.json`
   (`chapter_design`, `layout`, `scene`, `known_benign`), `storyboard-en.md` §§1–11,
   `script-en.md` ch2 (the `[img: …]` cues are the one home for every on-screen string),
   `facts-staging.md` §2, `logs/fin-assets-en-ch2-1.md`, `logs/fin-build-en-ch1-2.md`,
   and the three code homes: `blockframe.css`, `chapter-design.css`, `motion.js`.
   **No knowledge-note body opened** — no `OPENED-BODY:` line. **No `MISSING-CONSTANT:`.**
2. Scaffolded `studio/videos/financial-freedom-after-50-en-ch2/` by copying
   `tools/scaffold/{package.json,package-lock.json,assets/{blockframe.css,chapter-design.css,
   fonts,img,js/gsap.min.js,js/motion.js}}`, then `assets/voice/` = the 17 ch2 mp3s + their
   `.txt` + the cut's whole `timing.json` (ch1's layout: `chapter_timing()` slices it).
   `npm install` against the committed lockfile → hyperframes 0.7.66, no bare `npx --yes`.
   `lottie.min.js` deliberately NOT copied — 0 Lotties in this cut (§8).
3. Wrote `build.mjs` (the generator; `index.html` is its output) and ran it. Every
   `data-start` / `data-duration` / `data-framings`, the `S` map, the 17 `<audio>` rows and
   the root duration are derived from `timing.json`; the SPEC table owns the design only.
4. Drew one new icon and wrote it back to the library:
   **`assets/icons/step-arrow-down.svg`** (colourless, classless, `i-*` ids).
   `ls assets/icons/` first: 10 files, none of which is a descending step —
   `growth-arrow` rises, `reorder-rules` swaps two rules. Nothing reusable, so it was drawn.
5. `npm run check` → passed. Two snapshot batches into **two separate directories**
   (`snapshots/qa/b1`, `snapshots/qa/b2`), 17 + 8 frames, every one looked at; 4 read at full
   resolution. Both invocations succeeded first try — no `Navigation timeout` retry needed.
6. One design edit after looking at frames (the s18 icon bed, 240 → 200 px), rebuilt,
   re-checked, re-shot.

## Failed

- **Nothing blocked.** Three things were rejected on measurement or on rule before they
  reached the file:
  - **The stock `ken` on s16.** At its 1.16 end the visible window is 74.3 % of the image
    width against subjects spanning **18.8 %–89.5 %** — the right tap's cap goes off canvas,
    and the ±2.5 % `xPercent` pan walks it further. That is fin-assets Owed 1 as an actual
    number, not a worry. Replaced with `plateKen(0.90, 0.95)` (Evidence 2).
  - **A per-scene `filter:` anywhere**, including on `s23b`, which is the darkest frame in
    the chapter. `blockframe.css` sanctions a per-image *brightness* calibration for a
    near-black texture, but `storyboard-en.md` §9 says "No per-scene grade override anywhere"
    and the creator rejected exactly this lever on 2026-08-04. Left alone and handed up
    (Owed 2) rather than decided here.
  - **`.brule` on s16.** §6 marks it `ctr: N`; the rendered band says otherwise — see
    Evidence 4.
- `node build.mjs` threw once on the read-back assertions (a stray `'` inside the template
  literal's CSS comment). Same class as ch1's backtick gotcha: the header + inline `<style>`
  live INSIDE a template literal.

## Evidence

**1 — the four homes agree, and nothing was re-timed.** Emitted table, read back out of
`index.html` by the generator's own assertions (start, duration, framing sum, the 9.0 s
single-framing cap, track alternation, the 0.45 s overlap at all 16 boundaries, a real `.bg`
+ `has-photo` on all 17):

```
        start    d-dur   framings          track
s12     0        9.975   4.7,4.825          1
s13     9.525    6.109   5.659              2
s14     15.183   6.03    5.58               1
s15     20.764   7.702   7.252              2
s16     28.016   6.919   6.469              1
s17     34.485   8.486   8.036              2
s18     42.52    4.411   3.961              1
s19     46.481   5.978   5.528              2
s20     52.009   7.049   6.599              1
s21     58.609   4.672   4.222              2
s22     62.831   8.773   8.323              1
s23     71.154  10.158   4.8,4.908          2
s24     80.862   4.359   3.909              1
s25     84.77    7.467   7.017              2
s26     91.787   8.172   7.722              1
s27     99.51    3.601   3.151              2
s28    102.661   5.998   5.998   (bare)     1
root 108.659 · tracks 12121212121212121 · 17 <audio> rows
```

Every `start` is §6's `start` − 68.673 (s28: 171.334 − 68.673 = 102.661 ✓) and every `d-dur`
equals §6's `d-dur` column, s28 excepted, which is bare by the chapter rule. The chapter
plays from 0 with the shipped cut's relative gaps exact.

**`data-framings` is comma-separated on all 17 sections** (carry-forward 1), and the
generator now *asserts* it: a whitespace character anywhere in the attribute throws
`data-framings "…" is space-separated; check_build splits on "," only`. §3's DOM example
still shows the space-separated form and will trap the next chapter unless it is fixed at
the storyboard.

**2 — s16, the counted frame, in image pixels.** `s16.jpg` is a 3:2 file; the two taps'
centres sit at x 24.2 % and 80.8 %, and the outermost ink (left handle → right cap) spans
**18.8 %…89.5 %**. `.bg` is `inset:-8%` + `cover`, so a 3:2 source is cover-fitted by width
and the visible window is `0.8621 / k` of the image width, centred:

| framing | visible image window | verdict |
|---|---|---|
| stock `ken(in)` end, k=1.16, x=+2.5 | 12.9 %…87.2 % (then panned) | **right tap's cap off canvas** |
| stock `ken` widest, k=1.00 | 6.9 %…93.1 % | both, 3.6 % right margin |
| **shipped** `plateKen` start, k=0.90 | 2.1 %…97.9 % | both, 8.4 % right margin |
| **shipped** `plateKen` end, k=0.95 | 4.6 %…95.3 % | both, 5.8 % right margin |

Direction is preserved (it is still a push IN, so the alternation is intact) by running the
whole move *below* the stock ken's widest frame — the same trick ch1 used on s3, and it is
why fin-assets Owed 1 costs nothing. Verified on frames, not just in arithmetic:
`b1/frame-04` (30.316 s) and `b2/frame-01` (34.300 s, the tightest instant before s17
dissolves in) both show two complete taps flanking the two chips. The frame states the count
for the full 6.469 s.

**3 — s18, the icon, and why it has a bed.** fin-assets Owed 2 said the arrow must land over
the wallet's interior. Measured on the photograph: at ken k=1.00–1.08 the open wallet spans
frame **x 982–1327 / y 354–1010**, and its genuinely dark region (the inner slot) is only
**~107 px wide on screen** — narrower than any legible icon. So the honest numbers:

| ink on | luminance | contrast vs `--warn` #ef4444 |
|---|---|---|
| graded pale wood | ~122 | **1.13 — invisible** |
| graded wallet lining | ~122 | 1.13 |
| the inner slot | ~60 | 2.85 |
| **`.v-iconbed` at 0.78 alpha** | ~39 | **3.9** |

`.v-iconbed` is the composition's one inline `.v-*` component: a 200 px rounded panel at
`left:1050 top:690`, `rgba(13,16,23,.78)`, holding an `.icon.sm`. It is `.art-lift`'s idea
scoped to one element — it darkens BEHIND the drawn layer and cannot touch the photograph
outside its own box, so the whole-frame lever rule 9 forbids stays forbidden. Its rect was
chosen against two measurements: the wallet's opening (above) and the stack's own bottom
edge — two 76 px lines end at **y 648**, so the bed starts 42 px clear of them and
`hyperframes check` reports no `content_overlap` on s18. Read at full resolution
(`b1/frame-06`, `b2/frame-02`): the arrow sits inside the empty wallet, descending into it.

The icon itself is a 7-segment descending stair plus a down arrowhead, `class="icon sm
warnc"` (the colour-only role class — `.warn` would have painted it a modifier that does not
exist for `.icon`), `draw("#s18-icon path", +2.10, 0.90, 180)`. Stroke is
`currentColor` at the system's 6 units of 100, i.e. ~7.8 px at 130 px — above the
"nothing thinner than 9 px" floor once the bed is counted as the lift. Saved back to
`assets/icons/step-arrow-down.svg`.

**4 — s16 ships `centred`, and that is not a deviation from §6, it is §6 measured.**
`.arch-d .stack` is `align-self:start; margin-top:34px`, so a chip row renders at the TOP of
the frame; a `.brule` at `top:424px` would sit under it with the entire 656 px band empty.
That was P1 #3 on ch1 s9/s10 and it was fixed by centring both. s16 is the identical case
(arch D, `art-off`, one chip row, nothing on the other side) and takes the identical answer.
`grep 'brule' index.html` returns **0 element matches** (1 hit, inside a prose comment), and
**17 of 17** scenes carry `centred`. This is carry-forward 2 applied, and it keeps the two
chapters consistent rather than making them disagree.

**5 — the two-framing scenes, and the one that is a real photo swap.**
- **s12** (9.525 s, framings 4.700 / 4.825) is a re-crop of one file, as §5 declares: ONE
  continuous push `plateKen 1.00 → 1.075` then `1.075 → 1.16`, no self-dissolve (firaun
  rule). No second image slot exists for it.
- **s23** (9.708 s, 4.800 / 4.908) is the stronger form the fin-build contract asks for: the
  second framing is a **different photograph**. `s23b-bg` is a second `.bg` at `opacity:0`,
  `fade`d in over 0.60 s at +4.800 — under the word *roof*, which the char-position estimate
  puts at ≈+5.35 s, so the picture completes as the word lands — and `plateKen`ed from
  **exactly the value `s23-bg` holds at that instant** (1.16 − 0.10 × 4.8/10.158 = **1.113**)
  to the same 1.06 end. The outgoing photo keeps moving underneath on the identical curve, so
  the picture changes and the move does not. Read at 73.5 / 75.9 (engine bay) and 76.654
  (roof) — two frames that cannot be read as the same picture.

**6 — the ken alternation, including across the chapter joint.** ch1 closed on s11 pulling
BACK (`plateKen 1.08 → 0.98`), so this chapter opens pushing IN and runs even-index-in /
odd-index-out: s12 in · s13 out · … · s28 in. Four scenes take declared endpoints instead of
the stock push (s16, s20, s21 and the two pair-scenes); all four preserve their direction.
**s28 ends on an IN, so chapter 3's s29 must be an OUT** — Owed 4.

**7 — the pale run (s20 · s21 · s22), looked at rather than argued about.** fin-assets Owed 3
named the lever as the s20 archetype and forbade a per-scene filter. What shipped: s20's ken
never opens past **k=1.06** (1.06 → 1.16, the tightest framing in the chapter), so the white
marble surround stays out of frame and the envelopes/coins/calculator fill it; s21 pulls back
only from 1.16 to **1.08**, still inside the tighter half of the range. Judged from
`b2/frame-03` (56.5 s) and `b2/frame-04` (61.5 s) at full resolution: **neither frame reads
pale on screen.** The locked grade plus the four-layer scrim land the centre of frame at
~75 luma, so the amber focal and even the 26 px muted `.foot` read cleanly, and the run has
real subject, edges and falloff on all three frames. `stock-photo-sourcing` BOX rule 6 was
right and no lever was needed. Nothing was darkened, nothing re-fetched.

**8 — `npm run check` (hyperframes 0.7.66, pinned via the committed lockfile): PASSED.**

```
Lint      0 errors, 4 warnings, 2 infos
Runtime   0 errors, 0 warnings
Layout    0 errors, 0 warnings, 10 infos
Motion    0 errors, 0 warnings
Contrast  12/12 text checks pass WCAG AA
```

`known_benign` is `[]` and stays `[]`. **No design token was touched.** Two of the four
warnings are ch1's structural pair (`timeline_track_too_dense`, tracks 1 and 2 at 9 and 8
elements — that is exactly what the alternating-track transition rule requires, and the
suggested fix contradicts `chapter_design.one_root_html`). `composition_file_too_large`
(376 lines) is the same class. **The fourth is NEW and is reported loudly rather than
silenced** — see Owed 1. The 10 layout infos are all `container_overflow` on a `.bg`, which
is what `inset:-8%` is for.

**9 — snapshots: 25 frames, 2 batches, 2 directories, 25 looked at.**
- `snapshots/qa/b1/` — **17 frames**, one per scene at its own max-density instant, computed
  from that scene's last cue rather than from a fixed offset: `+1.80` for the 12 stmt scenes,
  `+2.30` for s16's chip row (`popEach` 1.10/0.65/0.40 lands the second chip at +2.15 —
  ch1's own sampling error, not repeated), the **anchored** `+4.215` for s17's num,
  `+3.05` for s18's drawn icon, `+2.60` for the two scenes carrying a foot, and `+5.50` for
  s23 (after the cut-in). Read as 2 contact sheets plus full-resolution reads of frames 04
  (s16), 05 (s17), 06 (s18) and 11 (s23b).
- `snapshots/qa/b2/` — **8 frames** at the ken extremes and the two boundary states the
  density pass cannot see: 9.4 (s12 mid-push), **34.3 (s16 at its tightest)**, 46.3 (s18
  with the resized bed), 56.5 / 61.5 (the pale run), 73.5 / 75.9 (s23 before the cut-in),
  108.5 (the chapter's last frame). Read as 1 contact sheet plus a full-resolution read of
  frame 03.
- What the frames show: `.stack` inside the safe area on all 25, nothing overflowing, the
  `cut-en` watermark painted bottom-right on every one including the dissolve frames. The
  en-dash in *3–6 months*, the em-dash in the two OPINION foots and the middle dots in
  *VERIFIED · FEDERAL RESERVE G.19 · AS OF AUGUST 2026* all draw as glyphs — **no tofu**,
  which is direct evidence for the check `uncovered_glyphs` performs and which is not on my
  allowlist to run.

**10 — a defect in the SYSTEM stylesheet, found while reading it, not triggered here.**
`tools/scaffold/assets/blockframe.css` line 187 closes the `.stamp` comment with `*/` and
then continues four more lines of prose before a second `*/`. After comment-stripping, that
prose is prepended to the `.stamp.warn` selector, so **the `.stamp.warn` rule is dropped by
any CSS parser** and `class="stamp warn"` renders red text with no fill — the exact defect
the dead comment says was fixed on 2026-08-12. `.stamp.fund/.target/.pop` survive.
Verified by parsing the file. It does not touch this chapter (§2 puts every verdict slam on
the cue ladder, so this cut emits no `.stamp` markup at all), and `tools/` is not mine to
write, so it is reported here — Owed 6.

## Changed

New, all under `studio/videos/financial-freedom-after-50-en-ch2/`:

| file | what it is |
|---|---|
| `build.mjs` | the generator — the SPEC table (17 rows) + the four-cue ladder. The only hand-authored design in the chapter. |
| `index.html` | its output. 17 `<section>`s, 17 `<audio>` rows, 1 inline `.v-iconbed`, 0 network references. |
| `assets/audio.json` | `bed-resolve` + 4 cues: 21.864 `reveal` · 37.991 `hero` · 63.931 `reveal` · 85.870 `chip`. |
| `package.json`, `package-lock.json`, `assets/{blockframe.css,chapter-design.css,fonts/,img/,js/}` | copied verbatim from `tools/scaffold/`; the two stylesheets and `motion.js` are LINKED, never edited. |
| `assets/voice/` | the 17 ch2 mp3s + `.txt` + the cut's `timing.json`. |

Plus one file outside the cut, by addition only:
**`assets/icons/step-arrow-down.svg`** — the library's first descending-step arrow.

Design, per scene (arch / ground / role are §6 and §7 verbatim, copy is `script-en.md`'s
`[img: …]` verbatim):

| scene | arch | ground | role | focal | motion beyond the ladder |
|---|---|---|---|---|---|
| s12 | A | `#1c2027` | — | stmt | push pair 1.00→1.075→1.16 |
| s13 | A | `#171d26` | — | stmt | |
| s14 | D | `#1f1e1c` | — | stmt | |
| s15 | D | `#2b1418` | warn | stmt | `reveal` |
| s16 | D | `#301519` | warn | **2 chips** | `plateKen 0.90→0.95` (the count) |
| s17 | B | `#38151a` | warn | **num** `North of 20%` + foot | **anchored** `pop`, `hero` |
| s18 | A | `#301519` | warn | stmt + **icon** | `draw` at +2.10 on its bed |
| s19 | C | `#1f1e1c` | — | stmt | |
| s20 | C | `#2a2113` | target | stmt + foot | `plateKen 1.06→1.16` |
| s21 | C | `#2a2113` | target | stmt | `plateKen 1.16→1.08` |
| s22 | D | `#0f2a1a` | fund | stmt | `reveal` |
| s23 | A | `#2b1418` | warn | stmt | **cut-in `s23b` at +4.800**, push carried on |
| s24 | C | `#301519` | warn | stmt | |
| s25 | D | `#0f2a1a` | fund | stmt (**`pop` entry**) + foot | `chip` |
| s26 | C | `#0f2a1a` | fund | stmt | |
| s27 | A | `#12351f` | fund | stmt | |
| s28 | A | `#12351f` | fund | stmt | last scene, bare duration |

Three copy decisions, each one resolving a conflict inside the source rather than inventing
anything:
1. **s17's num is `North of 20%`** — §6's focal column verbatim. The script's `stmt` line
   reads *"Credit card interest: north of 20% a year"*, but its own ⚠ (and `facts-staging`
   row 11) forbids a period label on this card, and *a year* is one. The card carries the
   shape and nothing else; the photograph is a brandless chip card, so the subject is stated
   by the picture.
2. **The `label:` cues ride in the `.foot`**, not in a fourth element: `VERIFIED · FEDERAL
   RESERVE G.19 · AS OF AUGUST 2026` (s17), `OPINION — A WIDELY USED METHOD, NOT AN AGENCY
   RULE` (s20), `OPINION / CONVENTION — THE STANDARD ADVICE, NOT A STATISTIC` (s25). §3's
   num/stmt stacks are `kicker → focal → foot`, so this keeps every scene at 3 elements and
   gives the label exactly one home. **s25 carries no agency name and no source line**
   (`facts-staging` §2), and no photograph in the chapter is asked to state "three to six" —
   that number exists only as type (fin-assets Owed 4).
3. **`window.__timelines = window.__timelines || {};` is restated** in the composition's own
   script above `register()` (carry-forward 3) — without it the lint error skips the layout
   and contrast passes entirely.

Not done, deliberately: no rail, no chapter/scene counter, no plate (the chapter's one drawn
layer is an `.icon`, not `.art`), no `body_class` on `#root` — `per-line-chapters` has no
entry in `architectures`, and ch1 shipped the empty default, so `class="cut-en"` is all
`#root` carries (carry-forward 4). No timing value was hand-typed anywhere.

## Owed

1. **To the orchestrator / fin-review — a NEW lint warning that names a render failure, and
   it scales with chapter length.** `composition_heavy_overlay_count_high`: this chapter has
   **34** elements carrying heavy-overlay CSS (radial-gradient) — two per scene, `.scrim` and
   `.glow`, both system components. The linter's field signal is that a composition with
   **~40** such elements "captures solid-black for the first ~half of the render", reproduces
   through every capture path, and is independent of duration. ch1 has 22 and never tripped
   it; ch2 is at 34; **ch3 is 26 scenes, i.e. 52, and ch5 is 19 → 38.** I did not touch it:
   the only fixes are deleting a system component or splitting into sub-compositions, and the
   latter is forbidden by `chapter_design.one_root_html`. **Watch the first ch2 draft for a
   black opening half**; if it is clean at 34 the threshold is loose, and if it is not, this
   is a system-level decision (a `.glow`-free variant, or per-chapter concat) and not a build
   one.
2. **To fin-review — s23b is the darkest frame in the chapter, by construction.** The roof
   silhouette and the water streams do read (`b1/frame-11`, full resolution) and the red
   focal is unmissable, but the frame is close to black. There is exactly one lever and it is
   contested: `blockframe.css` explicitly permits a per-image *brightness* calibration on one
   `.bg` for "a near-black texture [that] crushes flat at 0.62", while `storyboard-en.md` §9
   says "No per-scene grade override anywhere" and the creator rejected a per-scene filter on
   2026-08-04. I did not break that tie. If the draft reads dead there, the change is one
   inline `filter: grayscale(.32) brightness(.86) contrast(1.05)` on `#s23b-bg` **and** a line
   in §9 saying so — never a change to `grayscale` or `contrast`.
3. **To fin-review — s26's photograph is a saturated RED pair of binders under a `fund`
   (green) scene.** The grade only desaturates 32 %, so the frame reads red-and-green while
   the line is *"keep it separate"*. It is the one place in the chapter where the photograph's
   colour argues with the scene's role. The lever is the photograph, not the build.
4. **To fin-build ch3 — three things this chapter hands over.**
   - **The `s28 → s29` SHOVE is chapter 3's to emit.** `sceneTransitions` puts a transition on
     the INCOMING scene, and s29 is ch3's first: `sceneTransitions(IDS, S, {acts: ["s29"]})`.
     Nothing in ch2 can carry it, and ch2's own `sceneTransitions` call says so in a comment.
   - **§2 cue #9 (`transition`, abs 177.332 s) belongs to ch3's `assets/audio.json` at
     t=0.000**, not to ch2's. In ch2-local time it is 108.659 — the chapter's last instant —
     and mixing a hit onto the joint from the outgoing side would double it on concat.
   - **s28 ends on a push IN, so s29 must pull BACK** for the alternation to survive the joint.
5. **To fin-storyboard — §3's DOM example writes `data-framings="4.500 4.502"`, space
   separated.** `check_build` splits on `,` only, so that form parses as one token and
   crashes `float()`. This build asserts against it locally; the example is still wrong and
   will trap chapter 3.
6. **To whoever owns `tools/scaffold/` — `.stamp.warn` is dead** (Evidence 10). A four-line
   run of prose sits outside its comment and invalidates the rule's prelude. It costs this
   cut nothing (no `.stamp` markup anywhere in it) and it is a two-character fix, but it is
   in `tools/`, which this stage may not write.
7. **Not verified by me:** `pipeline_check check_build` is not on my allowlist, and no render
   was run — there is no `renders/` in this project yet. The generator asserts the same four
   properties `check_build` does (framing sum, the 9.0 s cap, track alternation, the 0.45 s
   overlap) plus two it does not (comma separation, a real `.bg` file on disk per scene).
