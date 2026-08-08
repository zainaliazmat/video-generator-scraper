# editor · japanese-money-methods · hi · chapter 2 · attempt 3
VERDICT: PASS

Reviewed `renders/DRAFT-ch2-v9.mp4` (30 fps, 2205 frames, 73.479s). Fresh sheet
built from v9 (`tools/chapter_sheet.py`, 12 cells), each cell read against its
VO line from `script-hi.md` §Chapter 2. Full-res frames pulled from the encoded
mp4 at 43.0 / 54.7 / 58.5 / 59.25 / 59.6 / 60.6 / 61.6 / 62.6 / 63.6 / 64.6 /
65.6s; s20 additionally at 440px (phone scale) and as a 1920x560 lower-band
crop; s17's bars cropped and upscaled 1.27x. Lit dots in s19 counted from the
encoded frame by connected components. Vendored `.js` diffed against the
library `.json` for all three generated assets.

## Attempt-2 findings — all five verified fixed

1. **BLOCKER, s20 German newsprint — RESOLVED, both halves.** The German print
   is gone with the photograph. The replacement is Japan, at night, and is not a
   fourth screen frame. The fourth Lottie renders in the encoded file (this is
   the case where the two silent-blank modes bite; it is not blank), starts at
   +1.90, spreads +2.70→+5.20 and is finished 0.78s before the framing ends.
2. **SHOULD-FIX, s17 wrong arm of the state — RESOLVED and verified to source.**
   `_cand/s17a.json` shows the candidate set came from the *Ministry of Finance
   (Japan)* article; the promoted file is Kakidai's, CC BY-SA 4.0, and CREDITS
   carries it. National, not metropolitan; the money ministry in a money video.
   Wide eye-level scale kept, so the s14→s17 ladder still steps.
3. **SHOULD-FIX, s19 proportion — RESOLVED.** `LIT = 28` in the generator, and
   **28 lit dots counted off the encoded frame at 54.7s** — the vendored asset is
   the regenerated one, not a stale copy. 25.9% no longer lands anywhere near
   the 37.8% two lines above it. Down rather than up was the right call: the
   sweep to "everyone" still arrives as an obvious increase.
4. **SHOULD-FIX, CREDITS — RESOLVED.** Twelve rows for twelve files, s17 and s20
   updated to the new sources. Your s19b check is right and I withdraw the
   implied doubt: the frame is a young woman in front of a shop, so a
   "girl-portrait-woman-face-model" slug is the honest URL, not a mismatch.
5. **NOTE, s13 icon set — left, as agreed.**

## The three checks you asked for

**The new Lottie — hardest look, and it holds.**
- *Does it read at a glance?* Yes. Two identical chips land on a shared rule by
  +2.10, then one throws off a rolling cascade into the empty band above its own
  half while the other's territory stays untouched. The split field is what
  makes it legible; the first cut's failure mode (spread over the origins' own y)
  is not present in v9.
- *At phone scale?* Read at 440px wide. The red cluster is unmistakable; the
  grey chip is the dimmest thing on the frame but it is there and it is on the
  same line as the red one, which is what the sentence needs. See note 1.
- *Sound-off, text covered?* "One multiplies, one doesn't." That is the point of
  the line. It does not tell you the two things are *published figures* on its
  own — the kicker does that — but the sound-off rule asks whether the picture
  says the point, and it does.
- *Honest?* Nothing in it reads as a measurement. No text, no axis, no labels;
  the chips overlap and vary 52–98% in size so counting is never invited. 22 is
  unmappable onto anything in the video: the real ratio is 34.4 ("more than 30
  times", Horioka p.7), 37.8 and 1.1 are the only other live numbers, and 108/28
  belongs to s19. Deliberately identical tokens is the right reading of
  `truth_bar` — drawing size here would have re-asserted a magnitude the frame
  is not measuring, two scenes after s17 measured it properly.

**s17 regression — none.** Against the brighter, emptier lower band the green
column reads *better* than it did over the old dark facade, and the ~1.1%
hairline still reads: it lands on the dark hedge line rather than on the road,
which is the one place on this photograph it could have disappeared. Both bars
share a clean baseline on the hedge/kerb boundary. The grade (`grayscale .3
brightness .7`) did not need to move — it is the chapter's heaviest grade and
the photograph is its brightest, which is why they cancel. Heights re-checked
against the generator: 340px / 9.9px at 340/37.8 px per point, from J1/J2.

**Lottie cap.** 4 of 4 — s15 table, s17 bars, s19 grid, s20 spread. I am not
asking for a fifth and nothing in the chapter is now a beat that only drawing
can serve. If a fifth were ever forced, the one earning its place least is
**s15's table**: it is decorative rather than measuring (it draws "a statistics
table exists", which the photograph and the sourced foot already say), where the
other three each carry an argument no photograph states.

## Findings
| # | scene | severity | what | why it fails | fix |
|---|-------|----------|------|--------------|-----|
| 1 | s20 | note | the grey token is the dimmest element on the frame (82% of `--muted` on a near-black plate) and it carries half the sentence | it survives 440px, so it is not failing — but if a viewer's eye never finds it the frame says "a number multiplied" and loses "and the other one didn't" | if s20 is ever re-rendered for another reason, take the stay-put token's fill opacity 82 → ~92 in `one-number-travels.py`. **Not worth a render on its own** |
| 2 | s19b→s20 | note | the chapter's only near-pair: a dark shopfront under Japanese signage cutting into a dark neon block. Mid-dissolve (≈59.25s) both signage fields sit on top of each other and the 0.45s overlap reads muddy | not a reuse and not a sameness failure — different scale, different subject, one has a person — and 13 frames of muddy dissolve costs no viewer | no action. Flag for chapters 3–8: do not put a third night-signage frame anywhere near these two |
| 3 | s19 | note | 28/108 ≈ 26% now reads as "about a quarter" where the real salaried share of Japanese households is nearer half | nothing on screen cites it, `facts-staging` has no published household-share figure to contradict, and the grid's job is set-vs-subset, not magnitude — this is the residual cost of the fix I asked for and it is the cheaper cost | leave it. Do **not** chase a "correct" proportion here: the moment the grid is accurate it becomes a statistic and needs a source it does not have |
| 4 | s13 | note | the ~2014 app grid (Google+, the Twitter bird, the old Instagram camera) | carried from attempt 2, ruled taste, still taste | leave |

## What is working
- **The three-ministry run is the chapter's quiet best work and nobody should
  touch it.** s15 is the government complex that houses the Statistics Bureau's
  parent (FIES), s16 is the Cabinet Office (National Accounts), s17 is the
  Ministry of Finance — three different publishers of three different things, in
  the order the script names them, at four different scales and two colour
  temperatures. It is far more precise than "grey building" and it survived two
  re-sources without losing the ladder.
- **s17's bars are still the best frame in the chapter** and are now better
  placed than in v7: the hairline has dark hedge to sit on instead of dark stone.
- **Twelve scenes, twelve distinct pictures, no image used twice**, and the
  chapter now carries four Lotties that each state something no photograph
  states. s21 still closes clean: modern coins, the old note cropped out, the
  ₹30,000 caveated, bare duration on the last scene, cue ladder 0.30 / 1.10 /
  1.90 throughout.
