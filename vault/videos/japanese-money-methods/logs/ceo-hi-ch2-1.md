# CEO · japanese-money-methods · hi · chapter 2 · attempt 1
VERDICT: REWORK

Watched `renders/DRAFT-ch2-v9.mp4` as a run, not scene by scene: fresh
`tools/chapter_sheet.py` sheet (12 cells), then a 12-frame pass sampled across
0.5→72.5s, then the **join** — ch1's last three frames (`DRAFT-ch1-v2.mp4`
50.0 / 53.0 / 55.5) butted against ch2's first six seconds (0.3 / 1.0 / 2.0 /
4.0 / 6.0 / 8.5). s11, s13, s18, s21 pulled at full res; s20's Lottie sampled
across its whole spread (59.25 / 61.6 / 64.0 / 65.4). Every on-screen figure
traced back to `facts-staging.md` J1/J2/J3.

## Would I keep watching?

Yes — from 0:08 onward. **Not for the first 8.5 seconds, and that is where I
would leave: chapter-local 0:03 (full cut ~0:59).**

Here is the join as a viewer gets it. Chapter 1 closes on a dark kitchen and a
consent question — *"Is this yours? Then this one is for you."* The viewer says
yes. What they are handed next is a wide, cold, near-static Kyoto rooftop
townscape, the darkest and lowest-contrast frame in the chapter, held for
**8.486s — the longest scene here, and scene one** — carrying a line that defers
rather than pays (*"Centuries old. In no finance course."*). Dark interior →
dark exterior, no change of register at the exact cut where the video changes
subject. The `ken` on s11 is real but invisible at that scale: frames at 0.5s
and 7.8s are indistinguishable. Three seconds in, the line has landed and
nothing on screen is moving, and there are still five seconds to go before the
first thing a viewer came for.

Everything after 0:08 earns its place, and some of it is the best work on this
channel. s13's `37.8%` in amber over the dark navy app grid is the most legible
frame in the chapter. The s14→s17 ministry ladder — Diet at dusk, the tower, the
Cabinet Office entrance at human scale with a legible 内閣府 board, the Ministry
of Finance — steps through four scales and two colour temperatures and is far
more precise than "grey building"; the editor is right that nobody should touch
it. s17's drawn bars are the frame I would put on the channel banner. s19's grid
and s20's spread each state something no photograph states. **The chapter's body
is not the problem. Its front door is.**

The ending does open a loop, properly: *"What survives in the methods — and what
it does to ₹30,000"* is a question, not a summary, and the ₹30,000 is caveated
in the foot on the same frame. Good last line.

## Findings

| # | scene/span | severity | what | fix |
|---|-----------|----------|------|-----|
| 1 | s11 · 0:00–0:08.49 (full cut 55.91–64.40) | **blocker** | The chapter opens on a mood shot with a soft line, for its longest hold. Wide generic townscape, darkest frame in the chapter even after the .80→.86 lift, no perceptible motion, following ch1's equally dark kitchen. Sound-off it says "an old Japanese town" — true, on-message, and not what the line is about. It is also the only frame here still on a 1280×853 preview (1.5× upscale before the ken), which is why it reads softer than its neighbours | Re-source the slot only. **The storyboard's own spec is the fix and was never built**: `img: a Japanese wooden shopfront noren curtain at dusk` — close, warm, human scale, specific. That gives the chapter a warm front door, makes s11→s12 (cool phone) → s13 (dark navy) step properly instead of running dark-dark-dark, and gets off the upscaled preview. **Do not change `data-duration` or `data-framings`** — chapter timings are the shipped cut's verbatim and must stay frame-exact for the concat. A two-framing split is not available: 1280×853 has no crop room at 1080p |
| 2 | s13, s15, s16, s17 · 13.6–44.3 | should-fix | **The chapter's central number is never labelled on screen.** `37.8%` (twice), `ABOUT 1%`, `30 TIMES` run across 25 seconds and the words *saving* / *saving rate* appear nowhere in the chapter — not in a kicker, not in a stmt. The Hindi VO says it plainly, so this only bites the muted viewer and the one who joins mid-chapter, but those are the two who most need it. My own rule: a number without a comparison is noise; a number without a *unit* is worse | One word, text-only, rides the same render. Name it once, early — e.g. s13 kicker `THE CLAIM` → `THE CLAIM · JAPAN'S SAVING RATE`. Not on all four; once is enough |
| 3 | s13 · 13.6–20.3 | should-fix | The kicker says **THE CLAIM** while the foot directly underneath cites the **Statistics Bureau of Japan, Table I-2-2**. The frame calls a government table "a claim", and it pre-empts s14's whole reveal (`IT IS REAL / Japan's own government publishes it`) 6 seconds before it lands. A first-time viewer reading both lines gets a mixed message for the length of the scene | Text-only, same render. Either the kicker stops calling it a claim, or the Bureau citation moves to s15 (which already carries the FIES foot) and s13 keeps only the number. Do not lose the source from the chapter |
| 4 | whole chapter | note | Eleven scenes, every one on the identical `+0.30 / +1.10 / +1.90` cue ladder plus a ken, 5.6–9.6s each, no acceleration anywhere in 73.5s. Mean scene length is **6.7s against ch1's 5.6s** — the chapter carrying the reveal is slower than the chapter that carried the pain. Structural to `blockframe-9` and ch1 shipped with it, so not a rework; flagging it as a question for chapters 3–8 | none now |
| 5 | s11 | note | Two modern air-conditioning condenser units are the brightest object in the top half of the frame, under a line reading "Centuries old." Moot if finding 1 is actioned | none |
| 6 | s11 | note | `--fund` green on "Centuries old. In no finance course." is what the storyboard assigns 2.1, but it reads against the storyboard's own colour law — *"green marks what the viewer does, never what Japan is"* — and s11 is entirely what Japan is. Internal inconsistency only; the same green already carried 1.2's promise in an approved chapter, so leave it | none |

## Honesty

Clean. `37.8%` is J2 (HARD, two sources, one the issuing agency) and cited on
screen. `ABOUT 1%` obeys J1's own instruction to say "about one percent" rather
than print the single-sourced decimal. `30 TIMES` is under a quoted "more than
30 times as high" — it understates its source rather than overstating, which is
the safe direction. `₹30,000` is caveated as this channel's worked example on
the frame that uses it. s18's form carries no legible text asserting a place or
an institution — I checked it at full res specifically because that is the error
class that got through twice already. CREDITS is 12 rows for 12 files with the
two re-sources updated. **I would be comfortable if Horioka watched this
chapter.**

## Regressions vs editor pass

**None.** Every attempt-2 and attempt-3 fix is intact in v9 and none of them
broke a neighbour:

- s13 carries no table; the amber number and the Table I-2-2 foot sit clean on
  the dark navy — verified at full res.
- s15's table reads as a table in the lower band on the sheet.
- s16 is the re-cropped Cabinet Office entrance — warm brick, a person, human
  scale, still the only warm frame in the 19.8→44.3 run.
- s17 is the Ministry of Finance (CREDITS: Kakidai, CC BY-SA 4.0); the bars are
  unchanged and the ~1.1% hairline still reads on the hedge line.
- s19's grid is visibly sparse — nowhere near the ~41% that read as 37.8%.
- s20 is Japan at night with no German print anywhere, and the fourth Lottie
  renders: two chips on a shared rule, one cascading, one alone. It states its
  sentence.
- s11's brightness lift is in the markup and applied. **Note that the lift did
  not solve the scene — finding 1 is a different problem at the same address,
  not a regression on that fix.**

The three carried notes are all still true and all still correctly ruled: s20's
stay-put token is dim but present at 440px; the s19b→s20 dissolve is muddy for
about 13 frames and costs nothing; s13's 2014 icon set still reads as social
media at a glance. **If s11 goes back to the stock providers anyway, that is the
moment to look for a current-era feed for s13 — but do not spend a round on it.**
