# CEO · japanese-money-methods · en · chapter 8 · attempt 2

VERDICT: SHIP

Watched `renders/CD-ch8.mp4` end to end as a strip (sheet + frames pulled at
0.2 / 1 / 2 / 3 / 4 / 5 / 30 / 38.5 / 43.5 / 45.5 / 47.2 / 49.3 / 51.5 / 52.4s),
against `editor-en-ch8-2.md`, script-en 8.1–8.8 and storyboard-en §3a.

## The three blockers are actually closed

- **s85 photo** — now the stocked tea-shop shelf. There is a thing in frame to
  decide about, and it is the first frame of the payoff chapter. Good.
- **s85 fork** — **the X renders.** Confirmed at t=3.0 / 4.0 / 5.0: stem, lit
  green accept branch, dimmed refuse branch, red X sitting on the refuse branch,
  all inside the frame. The one assertion this frame exists to make is on screen.
- **s92** — two mugs side by side. "Send it to *the friend*" now has a second cup
  in it. The last frame of the video no longer argues against its own line.
- **s91** — closed notebook + capped pen. The s89 → s90 → s91 pen sentence
  (pen out / page written / pen down) now completes.

## Would I keep watching?

Yes, and the close earns the subscribe. The chapter does what a closing chapter
has to do: it converts eleven minutes of argument into four labelled things, then
one instruction with a time on it ("Fifteen minutes"), then the ask, then the
share. The last line is a *person*, not a verb — "the friend who says every
month: I have no idea where it goes" — which is the strongest share prompt in
the cut and is the right thing to leave the end-screen sitting on.

**The timestamp where attention is at risk: 12.5–19.7s (s87), the third of four
identical recap frames.** By then the viewer has learned the pattern — kicker,
green headline left, small drawn mark right, ~6.5s, repeat — and s87 is the
weakest of the four: the magnifier-on-old-ledger photo says *audit the past*
where the line says *write four questions at the start*, and the four-row figure
is the least legible of the four marks. That is where a thumb moves. It is a
soft risk, not a blocker: the ground temperature does move underneath
(warm → green → deeper green → amber), the mark changes every frame, and a recap
is the one place in a cut where a held layout is the point rather than the
failure. 26s of one archetype is the price of the list reading *as* a list.

**Does it close the loop the video opened?** Yes on the constructive half, and
that is the right choice. What the close does not echo is the debunk — the 37.8%
/ about-1% contradiction that is the hook of the whole video never gets a last
word. A viewer who came for "Japan's saving myth" leaves with a to-do list. I am
not asking for a re-script; noting it because it is the one structural thing I
would change if this cut were being written again (see note 3).

## Findings

| # | scene/span | severity | what | fix |
|---|-----------|----------|------|-----|
| 1 | s87 | note | magnifier-on-old-accounting-ledger under "four questions at the start" — reads *scrutinise the past*, and it is the weakest cell in the flattest stretch of the chapter | editor's finding 6, unchanged. If a photo pass ever reopens: a part-filled US household budget page in ballpoint, no magnifier. Not worth a render on its own |
| 2 | s85 | note | the accept branch terminates at vx=780 → screen x≈1900 on a 1920 frame, i.e. 20px of margin; `.p-b` is `left:1120px; width:860px` so the plate's own right edge is already 60px off-canvas | reads correctly today and is at -hi parity, so leave it. But the arch-b plate has no usable right margin — worth fixing in the CSS, not in this chapter, before the next cut draws anything past vx=760 |
| 3 | chapter | note | the recap restates the four methods without a last beat on the video's own contradiction | script-level, not fixable at this stage. Flagging for the next cut: a closing chapter that re-touches the hook retains better than one that only lists |
| 4 | s89 | note | green focal crosses the bright notebook plate; lowest type contrast in the chapter | legible at 1080p and on a phone. No action |

## Regressions vs editor pass

None. Nothing the editor caught has come back, and nothing the three image swaps
touched has broken a neighbour — the s89→s90→s91→s92 run reads better now than it
did before, not worse.

## One editor finding I am overruling, so it is not chased a third time

**Editor #5 (s90 missing `THE WHOLE VIDEO` kicker) is not a defect — -en is
right.** storyboard-en §3a: s90 is one of the **seven SOLO scenes** (s1, s17,
s33, s43, s65, s77, s90), and SOLO is defined as *"focal alone — **no kicker**"*,
`.huge` @88px, focal at the `stamp` offset. s65 in the full -en build renders the
same way — statement only, no kicker, `pop` at +1.402 — and s90's cue at 34.788
maps to full-cut 608.92, which is the exact time the storyboard's cue table
declares for it. The `head:` in the 8.6 script cue is superseded by the SOLO rule
for those seven scenes; the `index.html` comment "No kicker on this scene,
verbatim" is correct. -hi rendering a kicker there is -hi's deviation, not -en's.
Do not add it.

## What is carrying the chapter

- **s88** is still the best frame in the cut and the amber break lands exactly
  where the argument turns — the one method that governs the other three. Editor
  was right to protect it; nobody touch it.
- **s92** is now a genuinely good last frame: two used mugs, dark, warm, no
  people, nothing to read but the line. It is the frame I would put the channel's
  name on.
- **Honesty is clean.** No figure appears on screen anywhere in s85–s92, so there
  is nothing to trace and nothing to overclaim. No stock photo implies a place or
  institution it is not; the one Japanese shop frame sits under MOTTAINAI, which
  is what it is. I would be comfortable if the FIES/BOJ authors watched this.
