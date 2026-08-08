# CEO · japanese-money-methods · en · chapter 1 · attempt 3
VERDICT: REWORK

Reviewed as a run: `renders/CD-ch1.mp4` (57.19s), sheet `renders/SHEET.jpg`
(13 cells / 10 scenes), plus frame strips across 0–12s, 20.5s, 33.5–35.5s,
44.5–46.5s and 49–57s. Editor log `editor-en-ch1-3.md` read first.

## Would I keep watching?

The first six seconds, yes. `s1` is the best opening we have built on this
channel — a black frame, then a phone lighting up with a notification arriving
at ~1.2s under "The deposit is in." The picture states the beat before the
sentence does and it is drawn, not stock. That is ours, not a template.

**Then it dies at 0:05.** `s2` runs 4.039 → 11.924 (7.885s). The notification
fades at ~5.7s and from there the frame is a dark-green void with an unlit
phone ghost and static type until 11.9s. I sampled 5.0 / 5.5 / 6.5 / 7.5 / 8.5
/ 9.5 / 10.5 / 11.5s — eight frames, no perceptible change. There is a ken on
it; at this luminance it is invisible.

**I would leave at 0:06.** That is 6.4 seconds of nothing, and it is sitting
under *the promise line* — "Three Japanese methods make it last longer" — the
single highest-value sentence in the chapter and the reason the audit moved the
payoff clause forward to ≈8.7s in the first place. We won the argument to put
the promise at 8.7s and then delivered it over the flattest picture in the
chapter.

The study cuts both ways and I have weighed it. The category winner holds one
still for ~15s in its hook and survives — but the study's own distinction is a
long hold on a **photoreal scene** (its `hook-02/03/04` is a legible Indian
kitchen, October calendar, banking app on screen — a frame full of things to
read) versus a long hold on a **title card**. `s2` is functionally the second:
there is nothing in it to look at. So the fix is not "cut faster" — the VO owns
the duration. It is "make the frame worth holding."

After that the run recovers and holds. `s3` splitting to the kWh meter is a
real save, the bright s3 pair is the one temperature break in a dark chapter and
it earns its place, `s4`'s 1-vs-6 now says the sentence, `s7`'s calendar +
draining BALANCE rail is the best scene in the chapter, and `s9`'s streams
growing under "a little everywhere" lands the argument turn exactly where it
should. Temperature does move (cool → bright at s3 → dark run → red at s9 →
warm at s10) and archetype rhythm exists (7×arch-a, 2×arch-b, 1×arch-d, three
art-forward). The chapter does not read flat. One scene does.

Yes, I would put the channel's name on this — after `s2`.

## Findings

| # | scene/span | severity | what | fix |
|---|-----------|----------|------|-----|
| 1 | s2 · 0:05.7–0:11.9 | **blocker** | 6.4s of a perceptually static near-black frame under the video's promise line. The phone unlights and nothing replaces it. The in-file comment justifies the fade ("it landed once and it is already past") — that is an editorial idea no viewer will ever read, and it costs the frame its only light source. | Two changes, both on art already on screen. (a) **Hold the phone lit** through s2 — do not fade `#s2-note`; the line is literally *"for about two seconds that notification feels like relief"*, so the relief should still be glowing while we say it. (b) **Give s2 a count to hold**: the line says *three* methods. Three marks arriving one per beat (drawn tick/slot triad on or beside the phone screen, cued ~+1.2 / +2.0 / +2.8) turns 6 dead seconds into the video's promise being built in front of the viewer. This is the archetype fix — a real assertion on an existing plate, not a new empty layout. |
| 2 | s1 · 0:00–0:00.45 | should-fix | The video's literal first frame is near-black with no type and no notification; the phone is a silhouette. First cue lands ~0.45s, notification ~0.8–1.2s. | Pull the notification arrival to ~0.30s so the picture asserts "money landed" before the sentence appears. Costs nothing, buys the first impression. |
| 3 | s6 · 0:33 | note | The 44 drawn slips render as a 4×11 grid but are near-invisible at grade (I had to lift +0.18 to count them) and 44 is a count the copy never states. It reads as texture, not a count. | Either raise it so it is countable, or accept it as texture — it is the creator-approved -hi device and it is not overclaiming. Note only, do not rework. |
| 4 | s5.3 · 0:30 | note | Agreed with the brief: the near-black bed/remote for "auto-renewal" is the softest framing in the chapter. It is legible enough to pass and I am not spending a render on it. | Leave. Swap opportunistically if a subscription frame is ever sourced for another chapter. |
| 5 | s6 / s8 | note | Agreed: dollar bills on wood twice within two scenes (0:33 and 0:44). Both are on-subject and legible, so this is preference, not retention. | Leave. |
| 6 | s3.2 | note | The kWh meter reads "ABB" legibly. It is a meter manufacturer with no claim attached to it and no financial institution is implied — honest. | Leave. |
| 7 | s10 | note | "Then this one is for you." closes an identification rather than opening a loop. The loop is genuinely open — 1.2 promised three methods and has not paid — so the chapter does hand off. But the closing frame is the passive one. | Acceptable as built. If s2 gains the three marks (finding 1), the handoff gets stronger for free, because the viewer will have *seen* the three that are owed. |

Honesty: clean. Zero on-screen figures in this chapter, nothing to trace to
`facts-staging.md`, no frame implying a place or institution it is not. I would
be comfortable if the primary source's author watched this.

## Regressions vs editor pass

**One, partial.** Editor findings 1 and 2 (s1/s2: no phone; self-dissolve ghost
at 4.3s) are both genuinely fixed — the ghost is gone and s1 is now the
strongest scene in the chapter. But the same fix **hollowed out s2**: the old
build at least had a ken-burning photograph with counter texture through 4–12s;
the new one has a void. Net the trade is worth it, and the remedy is small (light
it, count on it) — but it is a regression in retention terms at the most
expensive twelve seconds we own, and it should not ship as-is.

Everything else the editor caught is confirmed fixed and stayed fixed: s3 split
+ meter (f3), s5 three framings (f4), s6 receipts + slips (f5), s7 calendar with
the 20th ringed (f6), s8 hand on a statement (f7), s9 -hi water plate with the
streams now surviving the grade (f8), s4 recounted to 1-vs-6 (f9), `data-framings`
present on s3/s5 (f11), one Lottie deployed (f12). The `.measure-lab` inline
label on s7 still holds.
