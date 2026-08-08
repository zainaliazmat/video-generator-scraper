# CEO · japanese-money-methods · en · chapter 3 · attempt 2
VERDICT: REWORK

Watched as a run: `renders/CD-ch3.mp4` (88.67s, 12 scenes), sheet rebuilt via
`tools/chapter_sheet.py`, frames sampled at 0.4 / 1.2 / 3.0 / 5.5 / 10 / 16.5 /
22.9 / 25.5 / 27 / 31 / 33.5 / 35 / 40 / 47 / 50 / 62 / 70 / 82 / 82.5 / 83.5 /
85.5 / 87.5.

## Would I keep watching?
Yes — from t=13.5 onward. **The timestamp I would leave at is t≈1–6 (s22).**
The chapter opens on a near-black ledger page with a grey kicker and a line that
only names a filing habit — "It also records where the surplus goes." Nothing is
promised, nothing is at stake, and the statement does not even arrive until
+1.10. The actual hook of this chapter — *Japan saves hard and puts almost none
of it to work* — is 13.5 seconds away. That is the softest six seconds in the
chapter and it is where a phone gets put down. Not a blocker (it is a storyboard
beat both cuts share, and re-cutting it is a script decision, not a render one),
but it is the honest answer and it is worth the creator's attention when ch3's
head-to-ch2-tail handoff is checked.

After s24 the chapter earns itself. The 90/3 split, 51.0%, the US column, the
25-year window, the 23.2% peak and the Horioka quote is a real argument with a
turn in it, and it ends on a genuine loop: "The methods work. They were never the
reason" sends the viewer straight into chapter 4 asking *then what were they for*.

**The strip does not read flat.** Ground temperature moves — warm neutral (s22) →
amber under examination (s23–s26) → cold at s27, the chapter's coldest beat, which
is exactly where the argument turns from "Japan saves" to "Japan does not invest"
→ red at s28 → warm wood at s29 → red hot at s30/s31 → grey paper at s32 → green
at s33. Archetype rhythm is A B A B B A A D B A D A, and s32's second framing at
+5.66 is the one internal move in a chapter of otherwise uniform 7–8.5s scenes.
No finding here, and nothing to add.

**The creator's question — do s25 and s26 read as one document at two framings?**
Yes. Unambiguously. Same paper, same diagonal, same typeface, and s26's tighter
crop genuinely lands on the adjacent year column. "SAME TABLE, NEXT COLUMN" is
now literally what the picture does, and the chapter's one cross-market comparison
finally has two halves that belong to each other. **The device is right. The
photograph is not** — see finding 1.

**What landed and should not be touched again:** the `.measure-lab` overlap is
gone (s25 at t=25.5 — "HOUSEHOLD FINANCIAL ASSETS" clears the amber bar with
daylight). s33's `THE HONEST LINE` kicker and the green stamp are restored and
cued at +0.30 / +1.10; the hinge line now carries the strongest treatment in the
chapter instead of the weakest. Every on-screen figure traces to
`facts-staging.md` (J5, J6, J7, J8, U3) and the two hedging foots — ILLUSTRATIVE
on the 90/3 split, ASSET MIX ONLY on the US column — are doing exactly the work
they were written for.

## Findings
| # | scene/span | severity | what | fix |
|---|-----------|----------|------|-----|
| 1 | s25 (t=20.4–28.2) + s26 (t=27.7–36.2) | **blocker** | The shared photograph is a real, named US charity's audited accounts. Legible at 1080p: **"FIND AID FOR THE AGED, INC. AND AFFILIATES"**, **"CONSOLIDATED STATEMENT OF FUNCTIONAL EXPENSES"**, "Year Ended December 31", "Senior Housing", "Senior Centers", "Fundraising", and column heads **2018 / 2017**. On s26 that text sits directly under a foot reading *"The SAME BOJ table states both markets."* We are showing an eldercare non-profit's expense schedule and calling it the Bank of Japan Flow of Funds, Chart 2, end-March 2025. The visible years are also seven years off the cited date. This is a named institution implied to be one it is not, on the single scene where the video asks to be trusted about a cross-market number | Do **not** re-source — the two-framings device works. Push both crops off the header band onto the numbers-only region so no heading text or year label is legible: s25 `background-position` down/right from `62% 62%`, s26 from `80% 55%`. Rows of figures, no words. Two CSS values |
| 2 | s28 (t=43.5–51.5) | **blocker** | Under *"Japan was not always a nation of savers,"* the frame is a b/w overhead crowd on a European cobbled square — Western coats, blonde hair, bicycles, market baskets, a woman in a wide-brim hat, Belgian-block setts, no Japanese signage anywhere. It is a different photograph from the one the editor blocked, and it is the same error: the frame asserts the wrong country under a claim about Japan, for 8 seconds, at the chapter's red peak. Our own video study logs this exact failure as what killed the LOW comparator ("the hook shows the wrong century") | `assets/img/s28-fix.jpg` is **already on disk, correctly sourced** (Higashi Chaya machiya street — wooden two-storey shopfronts, lanterns, unmistakably Japan) and is what the `.src` asks for. index.html:173 is wired to `s28-hi.jpg` instead. One-line swap |
| 3 | -hi ch3 | note → creator | `s28-hi.jpg` is byte-identical to the locked -hi cut's s28 (md5 ab7e58b0…). The European-square frame is in the Hindi cut too, under the same sentence | Not this chapter's call, but the -hi ch3 lock should be reopened for the same one-line swap before ship |
| 4 | s29 (t=51–58.5) | should-fix | Editor finding #6 was not applied: the last decade tick is still `x="1756"` on a rule that runs `x=200 width=1520` (ends 1720) — a detached cap floating 36px past the end of its own axis. The whole 9-tick ladder is on a 195px pitch that does not divide the rule | `x="1756"` → `x="1716"` in the s29 svg, as -hi has it |
| 5 | s30 (t=58.1–66.5) | note | The photograph is a hand-drawn maths-textbook decay curve with visible axis numbers and `(0,−9)` labelled on it, under "THE POSTWAR PEAK · 23.2%". It is the one frame in the chapter that would be at home in any generic finance video, and the curve is an exercise, not a series. Not a blocker — art is correctly off, the foot carries the real claim, and the shape does not contradict the argument | Leave for this pass. If it is ever re-sourced, the storyboard's own ask (a printed series with a visible peak) is better |
| 6 | s22 (t=0–6.6) | note | The retention answer above. Softest opening frame + softest opening line in the chapter | Script/storyboard decision, not a render fix. Flag to creator |

## Regressions vs editor pass
**Two, and they are both of the "the fix re-introduced the thing the editor named"
kind — which is why this is a REWORK and not a note-and-ship.**

- **Editor blocker #3** explicitly forbade the reuse of `hi:s26.jpg` *because* it
  carried legible "Revenue report" / "MARKET RESERCH" wording on a frame cited to
  a BOJ table. The newly sourced replacement has the same defect, larger: it names
  a real organisation and states the wrong years. The instruction was followed in
  structure and lost in the detail it was written to protect.
- **Editor blocker #1** blocked a European cobbled street on s28. The rebuild
  took the log's *fallback* (`reuse hi:`), and the fallback is also a European
  cobbled square. The editor's read that "-hi's counterpart at least does not
  contradict" does not survive a full-resolution look — it contradicts plainly.
  The right image was fetched, written to disk with the right `.src`, and then
  not wired.

Everything else the editor flagged as a blocker has landed and held: s24 is now
steel deposit boxes, s27 is a sealed jar with no serving implement, s31 is the
scholarly volume, s33 has its head and stamp back, and the `.measure-lab` overlap
is confirmed clear in this encode.

Both blockers are one line of CSS/markup each and neither touches drawn art,
timing or copy. This is a cheap re-render, and after it I would put the channel's
name on this chapter without hesitation.
