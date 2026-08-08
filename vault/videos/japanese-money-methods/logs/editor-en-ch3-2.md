# editor · japanese-money-methods · en · chapter 3 · attempt 2
VERDICT: REWORK

Scope: -hi-parity image + drawn-art audit of -en ch3, against
`studio/videos/japanese-money-methods-hi-ch3/` (index.html, chapter.json,
renders/SHEET-ch3.jpg, renders/CD-ch3.mp4). Draft reviewed:
`studio/videos/japanese-money-methods-en-ch3/renders/CD-ch3.mp4` (88.704s, 12 scenes,
13 sheet cells).

## Where the two cuts genuinely differ (not findings)
- Copy is a 1:1 beat map. 3.1–3.12 carry the same twelve points in the same order.
  Only 3.5 differs in wording (-en says "US cash 11.5% · US equity 41.5%", -hi says
  "Cash 11.5% · Equity 41.5%") — same claim, US-market labelling. Correct for -en.
- -en s25 runs 7.754s with one framing; -hi s25 runs 9.452s with two (5.2 / 3.802).
  A shorter VO line, so one framing is defensible on its own. See finding 2 for why
  it still has to become two.

## Drawn-art parity: HOLDS
Every drawn layer -hi carries is present and wired in -en, and every number is
computed right. No blocker under the "-hi has art, -en does not" test.

| beat | -hi | -en | figures check |
|---|---|---|---|
| 3.2 · 90 / 3 split | svg, art-forward | same svg, art-forward | 576/640 = 90.0% ✓ · 19/640 = 2.97% ✓ |
| 3.4 · 51.0% | measure bar, target | same measure bar | to: 0.51 ✓ |
| 3.5 · 11.5 vs 41.5 | two tracks | same two tracks (+ art-lift) | 74/640 = 11.6% ✓ · 266/640 = 41.6% ✓ |
| 3.8 · 25 years in 8 decades | band + era block | same | era 492–980 on a 200–1720 rule ≈ 1961–1986 ✓ |
| 3.11 · count of five | 5 tally strokes | same | 5 strokes, 5 reasons ✓ |
| 3.9 · 23.2% | art-off (photo is already a peak) | art-off | correct — rule 8 |

Lotties: 0 in either cut, cap is 4 (`tools/format.json`). Every number / comparison /
date / count beat already carries drawn art, so I am not asking for one. No invented work.

## Findings
| # | scene | severity | what | why it fails | fix |
|---|-------|----------|------|--------------|-----|
| 1 | s28 | blocker | b/w photo of a European cobbled street — Western shopfronts, a figure in a hat, no Japanese signage | the line is "Japan was not always a nation of savers." The frame asserts the wrong country under a claim about Japan; that is a factual error, not a taste call. -hi's counterpart at least does not contradict. It is also graded to near-black — at t=47.5 almost nothing is legible | `source new: archival Showa-era (1950s–60s) Japanese street or commuter crowd, black-and-white, grain intact` — @commons if stock cannot name the era. Fallback `reuse hi:studio/videos/japanese-money-methods-hi-ch3/assets/img/s28.jpg`. Lift the grade so the subject reads |
| 2 | s25 | blocker | a blue-toned open book with blank pages, under "51.0% — Bank of Japan Flow of Funds, Chart 2" | (a) the line names a published central-bank TABLE; the picture shows a novel. Sound-off, this cell says "book", not "the BOJ's number". (b) s22 is already an open book (a vintage ledger). Two open books in a twelve-cell chapter is the repeat this pass exists to catch — it is the strongest cell-to-cell resemblance on the sheet | `reuse hi:studio/videos/japanese-money-methods-hi-ch3/assets/img/s25.jpg` (a chart of bars, reads as a chart at a glance). Better: `source new: a printed statistical table page, rows of figures in two columns, under a desk lamp` — and use it for s25 AND s26, see #3 |
| 3 | s26 | blocker | head reads "SAME TABLE, NEXT COLUMN"; the photograph is a man in a suit holding a colourful chart card and a pink folder — a completely different object from s25's open book | the picture argues with its own kicker. The chapter's one sanctioned cross-market comparison is the argument this scene exists to make, and nothing on screen connects it to s25. The render at t=33 is also visually chaotic: the art plate's grey rect and amber bars fight a multicoloured stock infographic underneath | `source new` the ONE table photo from #2 and give it to s25 (framing 1, wide) and s26 (framing 2, tight on the next column). Two framings of one sheet is the literal claim, not an image repeat — say so in the build comment so it is not flagged later. Do NOT reuse hi:s26.jpg: it carries legible "Revenue report" / "MARKET RESERCH" wording on a frame cited to a BOJ table |
| 4 | s31 | blocker | close-up of hands filling in a multiple-choice bubble answer sheet with a pencil | the line is "The largest study of that history says…" and the quote is cited to Horioka, NBER WP 33181. The frame reads as a school exam — wrong subject, and it undercuts the one scene in the chapter that has to look like scholarship. The asset's own `.src` says "thick academic working paper on a desk"; the fetched photo does not match its own keyword | `reuse hi:studio/videos/japanese-money-methods-hi-ch3/assets/img/s31.jpg` (thick gilt-edged volume, warm) — or `source new: a stapled working paper on a desk, dense body text, one paragraph in focus` |
| 5 | s33 | blocker | -en drops the head. -hi has `<p class="kicker">THE HONEST LINE</p>` + `<p class="stamp fund">`; -en has only `<p class="huge fundc">`. Only cue is `pop("#s33-stmt", 82.928)` = scene start +1.403s | (a) the storyboard specifies `head: THE HONEST LINE` for 3.12 and -en silently drops it. (b) first cue at +1.40s breaks the by-0.5s rule — verified at t=82, a bare unlit photograph with no type at all. (c) this is the hinge line of the whole video and -en gives it the weakest treatment in the chapter | copy the -hi s33 stack verbatim: kicker + `p.stamp.fund`, kicker at +0.30, stamp at ~+1.10. `reuse hi:` markup, keep the -en photo |
| 6 | s29 | should-fix | the rightmost decade tick sits at `x=1756`, but the rule is `x=200 width=1520` and ends at 1720 — a detached stray mark floating past the end of the timeline, visible at t=55 | a measurement graphic with a tick outside its own axis reads as a rendering bug, and it is an -en-only regression: -hi has the same tick at `x=1716`, inside the rule | in `chapter.json` s29 svg, change the last tick `x="1756"` to `x="1716"` to match -hi |
| 7 | s24 | should-fix | photo is a row of gym/school lockers with coloured plastic padlocks; the stack then draws a red padlock icon on top | (a) rule 8: the drawn padlock depicts exactly what the photograph already shows. -hi gets away with it because its locker photo is blurred past recognition; -en's padlocks are sharp and central. (b) coloured plastic padlocks read "school gym", not "a bank that will not lend your savings out" | `source new: a wall of steel safe-deposit boxes, all shut, cold light` (the storyboard's own line) — or drop the icon from the s24 stack |
| 8 | s23 | should-fix | at t=10.5 the photograph is unreadable murk — a dark shape and a hand somewhere near a desk. `.src` says "bank branch interior counter"; nothing on screen says bank | the drawn 90/3 split carries the point, so the scene is not silent, but the photo contributes nothing under the chapter's most-quoted number. -hi's counterpart (a paper form being filled at a counter) reads instantly | `reuse hi:studio/videos/japanese-money-methods-hi-ch3/assets/img/s23.jpg` |
| 9 | s27 | should-fix | a honey jar with a wooden honey dipper and a flower beside it | under "Japan is an example of saving, not of investing", the dipper and blossom make the subject read as HONEY, i.e. food, not a sealed store of value. The storyboard asked for "a sealed jar, full, lid still on" — the dipper is the one prop that says the jar gets opened | `source new: a plain sealed glass jar, full, lid on, no serving implement in frame` — or crop the dipper and blossom out |
| 10 | chapter | note | s27, s28, s32 and s33 all sit at or below the point where the photograph stops being a photograph. Four near-black cells in a twelve-cell chapter, three of them consecutive (s27–s29) | not false, and the arc justifies the cool/red trough — but the sheet reads as a run of dark rectangles | lift `--f1` opacity ~10% on s27 and s33; s28 is covered by finding 1 |
| 11 | s32 | note | the first framing is a bare plaster wall texture — no subject | -hi does the same and the archetype-D band + five tally strokes is deliberately the subject here, so this is parity, not a regression. The second framing (poster wall at +5.66) does the work | leave it; noted so the next pass does not "fix" it into something busier |

## Separately: the `.measure-lab` overlap (asked for, not a finding)
**The fix has NOT landed in this encode — but it is correct in source.**
- In `renders/CD-ch3.mp4` at t=26.5 the amber fill still strikes clean through
  "HOUSEHOLD FINANCIAL ASSETS" on s25. Cropped and confirmed at 2x.
- `assets/chapter-design.css` in the -en-ch3 studio dir DOES carry the fix
  (`.measure-lab { … margin: 0; line-height: 1; }`), identical to
  `tools/scaffold/assets/chapter-design.css`. So does -hi.
- Arithmetic says it will land: `.measure-lab.under` top 868 + 22px at
  line-height 1 → bottom 890; `.measure.under` top 910. 20px clear.
- CD-ch3.mp4 (08:27) is stamped after the css (08:03), so the mtimes lie —
  the render used the pre-fix stylesheet. The next ch3 encode is the proof;
  s25 is the only measure scene in this chapter, so one frame at ~t=26.5 settles it.

## What is working
- All five drawn layers are present, correctly wired, and every proportion checks out
  against the cited figures — 90/3, 51.0%, 11.5/41.5, the 1961–86 window and the count
  of five. The -en cut is NOT missing art relative to -hi; the gap is entirely photographic.
- s29 is the best cell in either cut: tree rings under an eight-decade rule with
  twenty-five years lit inside it says "a short window in a long span" with the sound off.
- s30 and s31 correctly keep art off — a drawn peak over a photographed peak graph is the
  depictive failure rule 8 names, and the chapter.json comments say so. Do not add art there.
- Cue ladder is clean everywhere except s33: every gap ≥0.8s, first cue at +0.30 on eleven
  of twelve scenes, and the last scene carries a bare duration with no framings.
