# editor · passive-income-number · hi · chapter 1 · attempt 1
VERDICT: REWORK

Reviewed from `renders/SHEET-ch1.jpg` (7 cells, one per scene) plus 10 sampled frames
from `renders/DRAFT-ch1.mp4`, the raw files in `assets-ch1/final/` and their `.src`
records, against `storyboard-hi.md` §5/§7/§8/§9/§10 and `script-hi.md` ch1.
s4's grey slab is a known, already-queued swap and is not re-litigated below.

## Findings

| # | scene | severity | what | why it fails | fix |
|---|-------|----------|------|--------------|-----|
| 1 | s5 | **blocker** | An office desk: a 30 cm stack of paperclipped A4 printouts, a keyboard, reading glasses, a tray of coloured pushpins. `.src` query was `stack of white paper documents on a desk close up@pexels` | Line 1.5 names three things — बिजली का बिल, राशन, किराया — and the on-screen line is "Electricity. Ration. Rent." **None of the three is in the frame.** Sound-off, this reads "paperwork backlog at work": institutional, Western, and emotionally the opposite of the "quietly paid, effortless" beat. This is the sound-off rule's own named example (*"rent goes out" needs money changing hands, not a stack of paper*). Storyboard spec was "three household bills fanned on a table — electricity, a grocery slip, a rent receipt" | **Needs a new fetch.** Three household papers fanned on a home table — an Indian electricity bill, a kirana/grocery slip, a rent receipt. Warm domestic light, low-key original (see #4), no desk, no keyboard, no office |
| 2 | s2 | **blocker** | A top-down food-blog flat lay: chai glass + two ginger roots + burlap on bright **white marble**. `.src` query was `steel glass of chai tea india@pexels` | The line and the on-screen text both name **the window** ("Tea. The window. One buzz.") and there is no window, no room, no morning light, no depth — the whole "won morning" simulation the cold open is built on is missing from its own establishing frame. Storyboard spec was "a steel glass of chai steaming on a windowsill, morning street out of focus behind". Compounding it: the frame is ~85% white marble, so the locked `brightness(.62)` grade renders it **slate-blue**, against the declared warm ground `#221c17` and §10's "warm first light" opening | **Needs a new fetch.** Chai glass on a windowsill or ledge, side-on or low angle (not overhead), soft warm morning light, an out-of-focus street or curtain behind. Warm/low-key original |
| 3 | s3 | **blocker** | The `phone_notify_credit` card draws and animates correctly, but its content is a grey wireframe: blank app-mark square, grey title bar, white amount bar, grey timestamp dash. **Nothing on it says money.** The photo underneath is crushed to near-black, so the phone is not discernible either | 1.3 — «पैसा आ गया, सोते हुए» — is the one beat the entire 35 s cold open exists to deliver. With sound off and the text stripped, this frame says "a notification arrived", not "money arrived". Masking the *figure* is the declared device (§8, the open loop) and I am not asking for it to be broken — but masking the figure is not the same as removing every trace that it is money | Inside the device: in `assets/lottie/src/phone-notify-credit.py`, put a **₹ glyph** at the head of the amount bar and/or in the app-mark square, regenerate and re-tint. Digits stay masked, amount stays unreadable, open loop intact |
| 4 | s2 · s4 · s5 | should-fix | Three of the seven backgrounds are **high-key white-background stock** (white marble, grey card on pale wood, white paper on a white office). This is the root cause of the chapter's grey-mush look, not the scrim | The system grade is locked at `grayscale(.32) brightness(.62) contrast(1.05)` with **no per-scene override permitted** (§9). A white-dominant subject under that grade can only become flat charcoal — which is exactly what s4 already is. Replacing one white photo with another white photo re-breaks it | Standing instruction on the three re-fetches: choose **low-key / warm originals**, subject lit against a dark ground. Do **not** add a per-scene grade override — §9 forbids it |
| 5 | s3 | should-fix | The raw `s3.jpg` is a good photograph — a phone face-down on dark leather with warm amber light along the far edge — but after `brightness(.62)` plus the cool `#161f2b` field it is effectively black in the encode | Storyboard spec is "screen glow on the wood"; the glow is the only thing that makes the picture say "night, and something arrived". None of it survives | Re-fetch a **brighter** phone-face-down frame with the screen glow visibly spilling onto the surface, so it still reads after `.62`. No grade override |
| 6 | s6 | should-fix | Framing, not the asset. The raw is correct — a stone stair rising through a rock cleft toward a bright gap — but the delivered crop gives ~65% of frame to rock wall and buries the stair in the bottom third; the `ken(..., false)` pull-out then widens onto *more* rock | Sound-off, the frame reads "a dark ravine", not "a ladder to climb rung by rung", and the destination reads as darkness rather than the bright gap the photo actually has | Re-crop tighter onto the staircase and the light at the top. Keep `ken` direction `false` — the alternation rule (§5) forbids flipping it |
| 7 | s7 | should-fix | Both pans **empty and level**. Storyboard specified "a brass balance scale, **one pan holding a folded paper slip**" | The whole point of 1.7 is that a figure *travels with* its condition — two things together. An empty level balance states nothing; the slip is what turns "a scale" into "a figure and its rate ride together". It does not contradict the line, so not a blocker | Re-fetch, or re-crop to include the brass weights the `.src` query asked for (they are outside the delivered frame). A folded paper slip in one pan is the stronger option |
| 8 | audio | should-fix | `tools/audio/cues.py` reads the **wrong `<script>` block**: `script = html[html.rindex("<script>"):]` picks up the RATE-ASSERT block at `index.html:243`, which contains zero motion calls. So it parses no `rise`/`fill`/`playLottie` at all and can only ever emit joint transitions — 6 cues, no content cues | On ch1 this accidentally agrees with the storyboard, so nothing is wrong on screen here. On chapters 2–7 it will silently emit joints-only and reproduce **exactly** the "scene changes read as silent" defect the generator was written to fix. `hi` ch2 alone should be emitting ~12 joints + a `hero` on every `num` scene | Point the slice at the **second-to-last** `<script>` (or scan all script blocks and keep the one containing `var S =`). Not a ch1 blocker — ch1 ships `build.mjs`'s hand-written `assets/audio.json`, which is correct |
| 9 | audio | should-fix | `studio/videos/passive-income-number-hi/assets/cues-tables.json` does not exist, so `cues.py` runs with no HOLDS and no BUZZ (it prints the note and continues) | Chapter 2 carries the declared s13→s14 **matched-frame continuous zoom** (§6). Without that file the generator will drop a `transition` whoosh on a cut that is not happening — announcing a change the picture is deliberately not making | Write it before ch2: `{"holds": [["s13","s14"]], "buzz": {"s3": 0.90}, "counted": []}`, from storyboard §2's own table |
| 10 | s1 | note | The type ("The alarm did not go off") sits directly across the clock face, over the numerals and both hands | Legible, and the busiest type/subject overlap in the chapter — but it is the video's frame 0 and the clock is the subject, so it is a taste call, not a defect | Optional: crop slightly so the dial sits lower-left of the stack |
| 11 | s3 | note | `fill("#s3-br", +0.15)` and `rise("#s3-stmt", +0.30)` are 0.15 s apart, against §5's ≥0.8 s ladder rule | The brule is a structural band element, not a content cue, and index.html declares the pairing deliberately for a 2.55 s scene. Raising it would be a finding about the review | No action |

### The four questions this chapter was asked

**1 · Does the cold open earn 35 seconds?** Not as shipped, and not because of pacing —
because three of seven cells (s2, s4, s5) are stock filler, so the morning simulation
never actually builds. Fix those and 35 s is earned. **The one scene that could go
unnoticed is s6.** 1.6 is the roadmap line, it owns the weakest frame, and 1.7 restates
the same forward promise with more force one beat later; s5's bills would hand straight
to s7's condition and the open would run 29.9 s. That is an observation for the CEO, not
a fix — the line is in the locked script and every duration here is `timing.json`
verbatim.

**2 · Does the promise land at the gate?** Yes, and **earlier than the clock says**. VO
1.4 has a 0.486 s internal pause (measured, 1.108→1.594 in `1.4.mp3`), so the
number-naming clause starts at **14.17 s** and the word नंबर lands ≈15.4 s — but the
on-screen focal *"You just reached a number"* rises at `S.s4 + 1.10` = **13.43 s**, and
the kicker NOT RICH at 12.63 s. The viewer reads the promise 1.6 s before the clause
speaks it. The reason it *feels* late in this draft is entirely s4: the eye has nothing
to land on, so the beat reads as a pause instead of a reveal. With a real object on s4
the gate is comfortable, not marginal.

**3 · Sound density.** The chapter is dry **by declaration**, not by omission —
storyboard §2's DRY BEATS list says "Chapter 1 except s3's `buzz`. The cold open is paid
in recognition. Scene joints still carry their `transition`; nothing else fires until
2.1." All six joints (s2…s7) do carry a `transition`, so the creator's reported "scene
changes read as SILENT" defect is **not present here**. No joint is bare. I am not
asking for the declared device to be broken. The real finding is #8/#9: the generator is
parsing the wrong script block and has no tables file, which is why it scores 6 — and
which will bite hard on ch2 onward, where the ladder is supposed to fire.

**4 · No rail.** Confirmed. Nothing in the DOM names or numbers a chapter: no rail, no
title, no counter, no slide number; `format.json chapter_design.rail` is `false`; s4
carries only `kicker` + `huge` (the "Chapter 6" `foot:` is correctly absent). The only
persistent mark is `#root.cut-hi::after` — the @cashguruguides channel watermark,
bottom-right — which is the blockframe brand mark, not a chapter indicator.

### Checked and clean
Seven distinct images, no repeat (7 distinct md5s) · `ken` alternates i/o/i/o/i/o/i with
no repeat, per §5 · track index 1/2 by parity, no overlap collision · cue ladder A at
+0.30 / +1.10 / +1.90, every gap 0.80 s, first cue at +0.30 ≤ 0.5 s · `data-framings`
equals each scene's own hold on all seven · s7 carries its **bare** 6.599 s duration and
29.146 + 6.599 = 35.745 = root · rate-assert wired and vacuously true (no corpus frame in
ch1) · Lottie count 1 of a cap of 4, and **ch1 does not want more** — it has no number,
comparison, process, date, share or count beat, so the one drawn layer is exactly right
and the other six scenes' `art-off` is rule 8 applied correctly, not a shortage · the
`phone_notify_credit` layer passes the additive test (a photograph is structurally
forbidden from showing a legible notification here) and completes at 12.30 s, holding
before the 12.33 s dissolve.

## What is working
- **s1 and s7 are the two frames that survive the grade** — a warm dial and warm wood,
  both readable, both saying their line. Whatever the fix pass does, do not re-fetch them
  for consistency with the replacements.
- **The Lottie is real and correct in construction**: it draws, it animates, the amount
  stays masked, the phone stays face-down, it finishes before its cut, and it is the only
  scene in the chapter with something on the other side. Finding 3 is a content fix to the
  card's contents, **not** a reason to touch the loader, the timing or the face-down rule.
- **The no-rail discipline held** and the s4 "Chapter 6" foot was correctly dropped at
  build. Keep it dropped.
- **The cue ladder and the timing spine are exact** — every start, duration and framing
  is `timing.json` verbatim, the last scene is bare, and the chapter concatenates
  frame-exact. No re-time is needed for any of the fixes above; all eleven are asset,
  crop or generator changes.
