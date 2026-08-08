# CEO · japanese-money-methods · en · chapter 4 · attempt 2
VERDICT: REWORK

Watched as a run: `renders/CD-ch4.mp4` (84.95s, 13 scenes, fresh — encoded
01:41, after every image and `index.html` change), sheet at `renders/SHEET.jpg`,
plus frames sampled at 0.5 / 2.6 / 5.0 / 10.5 / 17.0 / 19.5 / 22.5 / 25.5 /
30.5 / 34.2 / 36.5 / 39.5 / 43.6 / 49.5 / 55.5 / 62.3 / 70.0 / 74.6 / 82.5.

## Would I keep watching?

Mostly yes — and then no, at **36s**.

The run works. The argument moves: an old bowl, a regret, a shirt taken apart
into the four people who made it, and then the turn at 22.4s where the red
lands on *your* hours. That red frame (s37, the hall clock) is the best beat in
the chapter and it lands exactly where the argument turns. Then three green
checks the viewer can actually do, a red verdict, the question, the close. Both
the temperature arc and the archetype rhythm are real — cool → red at s37 →
green triple → red at s41 → green branch at s43 → warm bowl at s46; s43's
top-anchored rule and s44's left-type-plus-tally plate break the centred stack
twice. **The chapter does not read flat.** No note needed under item 6.

The place I would leave is **s39, 34–41s**. It is 7.5 seconds of a black
rectangle. Not "dark" — black: the source `s39-fix.jpg` measures mean
luminance **32.7/255 (p90 = 44)**, where every other photograph in the chapter
sits at **110–171**. Under the same grade s38 and s40 read fine and s39 goes to
zero, so this is the picture, not the field. And the phone in it is shot
edge-on with the screen facing away, so the subject the line names — a
subscriptions screen — is *still* not on screen. This is the middle of the one
sequence in the video that asks the viewer to stand up and do something, and
it is the check a US viewer is most likely to actually act on. It gets nothing
to look at.

Everything else I would keep watching for.

## Findings

| # | scene/span | severity | what | fix |
|---|-----------|----------|------|-----|
| 1 | s39 · 33.9–41.5s | **blocker** | Frame is effectively black for 7.5s (source mean lum 32.7 vs 110–171 for every other image in the chapter), and the phone is edge-on so no screen is visible. The line is "The subscriptions screen. All of it." Sound-off this cell says nothing at all; on the sheet it is a green void between two legible cells. | Re-source: a phone **screen-on, facing camera**, showing a recurring-payments / subscriptions settings list — rows of $ amounts, text illegible at frame scale, no brand marks. The lit screen is the point; it is also what gets the cell out of the black. Brightening the current file will not fix it — the screen is not in the picture. |
| 2 | s34 · 0–7.7s | should-fix | The kintsugi bowl is the right image and a real one — but at frame scale the **gold does not read**. The ken sits inside the bowl on mid-grey clay; the repair seams are at the rim and mostly cropped, and what survives reads as a dark crack, not gold. The chapter's hinge opens on "an old bowl", which is where the intact matcha bowl already was. | No re-source. Pull the ken back / shift right so the gold seams at the rim and the gold-filled chips on the foot are in frame, and let this scene sit a stop brighter than its neighbours. The gold is the argument; it should be the first thing the eye finds. |
| 3 | s46 · 79.7–85.0s | should-fix | Closing line on screen is "The next one starts at the dinner table." The VO says "…and it **ends inside your bank account**." The on-screen text keeps the setup and drops the hook — the chapter exits on the weaker half of its own loop. | Text only: set the s46 stmt to carry both halves, e.g. "Starts at the dinner table. Ends in your bank account." Costs nothing and is the last thing on screen before chapter 5. |
| 4 | s44 · 70s | note | `s44-fix.jpg` is genuinely a checkout belt — card terminal, divider, basket, cashier's hand — which is what was asked for. The ken then crops into the produce, so at 70s it reads "vegetables in a tray" and the purchase-decision reading is lost. | If the file is touched anyway, widen the framing to keep the terminal and divider in shot. Not worth a render on its own. |
| 5 | s36 · 14.6–22.8s | note | Chain order is now correct (cotton field → mill → truck) and the mill is legible. The field and the truck are not: at 17.0s the field reads as a brown blur and at 19.5/22.5s the truck reads as an anonymous dark highway. Only the middle link of the three actually says its phrase. | Lift the field and the truck framings toward their subject on any future pass. Chain is no longer wrong, just soft at both ends. |
| 6 | s38 / s41 | note | Logged as disagreement-free: I accept both deliberate holds. s38's illegible tags cost the scene its instruction, but every alternative carried a brand mark or foreign currency, and the line survives on VO. s41's flat trays are weak but not false. | None. Do not re-source either for this pass. |

**Honesty — clean.** Two figures on screen, both traceable: `ON $4,000` is the
channel's worked example and the foot says so in as many words ("not a
statistic"); the s34 etymology is hedged twice ("Roughly", "about the 13th
century"), which is correct given `facts-staging.md` marks that etymology
**SOFT** (the government page was never read direct). Nothing in the chapter
presents a proportion as a statistic, and no photograph implies a specific
institution it is not. I would be comfortable if the gov-online author watched
this.

**Clarity to a first-timer — clean.** "Mottainai" is glossed in the same frame
it appears. The three checks are three physical actions with no prior knowledge
required. No line needs two readings.

## Regressions vs editor pass

**None.** Every fix landed and nothing that was working came back broken:

- s36 chain reordered and now runs field → mill → truck against crop / mill /
  truck — verified at 17.0 / 18.8 / 22.5s. The mill exists in the -en cut for
  the first time. (editor #1) ✓
- Shirt rack retired from s36; the s36/s38 duplication is gone. (#2) ✓
- s45 is the worn work boot, legible and market-neutral. (#4) ✓
- s37 is the institutional hall clock, and it is now the red frame the design
  always specified — the strongest beat in the chapter. (#6) ✓
- s40 has no person; leftovers on a table read as food on its way out. (#7) ✓
- s42 is a hand on a packaged product in a retail case. (#8) ✓
- s44 is a supermarket checkout belt, not the derelict car-park cart. (#10) ✓
- s43 carries `THE QUESTION` at 76px, two clean lines above the rule, nothing
  touching the `brule`. (#11) ✓
- s35 is the denim with the visible hand-stitched seam. (#12) ✓
- The `.measure-lab` / `.measure` collision the editor said would clear on the
  next encode **has cleared** — at 36.5s and 43.6s "THE THREE CHECKS" sits
  above its track with a full gap. Confirmed, not assumed.

The one carry-over is **editor #3 (s39)**. It was actioned — the paper form is
gone — but the replacement does not solve the finding it was replacing: the
screen the line names is still not on screen, and the new file is dark enough
to erase the cell. Handing that one back, not re-opening it.

## Note on scope

One blocker, one cheap ken change, one text change. All three ride the same
render. I am not asking for anything else.
