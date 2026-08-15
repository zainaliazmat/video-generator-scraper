/* build.mjs — emits index.html + assets/audio.json for CHAPTER 3 of
 * passive-income-number, -en (@moneymavens101, $).
 *
 *   node build.mjs        (or: npm run build)
 *
 * WHY A GENERATOR AND NOT HAND-TYPED HTML. Every data-start, data-duration,
 * data-framings, the JS `S`/`D` maps, every <audio> row and the root duration
 * are FOUR homes for the same number. The failure this project keeps hitting is
 * durations that sum to exactly the right total while every internal cut has
 * drifted, so all four are computed here from ONE source —
 * ../passive-income-number-en/assets/voice/timing.json — and nothing below is
 * typed by hand. A layout pass may not touch a timing (design-chapter-
 * archetypes.md, "Timing is never a design decision"), and the asserts at the
 * bottom of the timing block make a silent re-time throw instead of ship.
 *
 * Chapter 3 is lines 3.1-3.16 = scenes s24-s39. The chapter's rebase constant is
 * timing.json's own scene_start for 3.1 (151.938s) and is subtracted from every
 * start, exactly as ch1 does with its 0.000 and ch2 with its 46.420.
 *
 * SPEC, not invention. The arch / ground / art / centred / focal / ken columns
 * below are vault/videos/passive-income-number/storyboard-en.md §7 verbatim, and
 * the kicker / stmt / num / chip / foot strings are script-en.md's own `[arch …]`
 * cue blocks (one home per fact — the storyboard deliberately does not restate
 * copy).
 *
 * STRUCTURE COPIED FROM ch2, PATCHES DELIBERATELY NOT. en ch2's two local CSS
 * patches (`.scene.centred .stack { padding-left: 0 }` and the `.arch-b .huge`
 * 900px override) were ported UPSTREAM into tools/scaffold/assets/chapter-
 * design.css on 2026-08-08 and its `v-widefocal` hook was removed. Neither is
 * re-emitted here and the "SYSTEM GAP" comment that accompanied them is gone,
 * because it is no longer true.
 *
 * FIVE RULINGS CARRIED IN, all implemented and all measured:
 *
 *  1. THE OPENER SHOWS A SUBJECT, NOT A SURFACE (ceo_r2 carry_forward_to_ch3).
 *     ch2's s9 was a closed notebook COVER and it was the frame the median
 *     crowned — the in-hand proof that a numerical measure alone rewards
 *     emptiness. s24 is a red hatchback parked kerbside under a street light,
 *     with the ken ending TIGHTER ON THE CAR (see `ken` below) and the frame
 *     bottom-weighted so the empty night sky is cropped away rather than
 *     carried. Sound-off it says "a car parked on a street", which is 3.1.
 *
 *  2. THE PAYOFF CLAUSE (payoff_clause_and_metric_2026-08-08). Named,
 *     measured and reported in the build log rather than asserted here: this
 *     chapter's payoff is s34 (3.11), the one verbatim HARD-primary quotation
 *     the fine-print run exists to put on screen. ch3 delivers no hero number
 *     by construction — 3.16 hands it to chapter 4 in so many words.
 *     ⚠ RESOLVED 2026-08-09 (attempt 2). s31 — the chapter's LARGEST figure —
 *     sat on the chapter's luminance floor (composed median 7.1, LAST of 16;
 *     p10 0.0), the s21 shape the CEO blocked in ch2. The lever was the
 *     photograph and fin-assets pulled it: s31 and s27 are new files and this
 *     build re-measured both on its own chain rather than taking the numbers.
 *     s31 7.1 -> 70.7 median (#10), 0.0 -> 43.2 p10 (#3), step-in -52.8 ->
 *     +8.6. s27 25.4 -> 97.9 (#4), 0.0 -> 82.9 (#2), -67.0 -> +5.3.
 *     ⚠ THE FLOOR MOVED, IT WAS NOT ABOLISHED: it is s37 (line 3.14).
 *     RULED 2026-08-09 by fin-editor and NOT a defect. Checked rather than
 *     assumed: s37 is not the payoff (s34 is) and not the longest-held (s26
 *     is, 8.355s against 7.598s), and it is not an outlier — 22/15 against
 *     s24's 23/17 on the encode, a one-point gap arriving on -6, where s31's
 *     breach was 7.1/0.0 arriving on -52.8. The floor stands where it is and
 *     no attempt-3 change went near it.
 *     ⚠ AND THE INVARIANT ANSWERED POSITIVELY, because two agents discharged
 *     it on hi ch3 by quoting its literal converse ("satisfied by
 *     construction"). Stated as the question means it: THE FLOOR IS s37, the
 *     beat holding it is line 3.14 — the verbatim Trinity conclusion, "Early
 *     retirees who anticipate long payout periods should plan on lower
 *     withdrawal rates" — and that beat IS substantive; it is one of the two
 *     the whole fine-print run exists to deliver. So the darkest frame in this
 *     chapter holds a substantive beat, which is what the clause's BLOCKERS
 *     have always enforced against, and the reason it is nevertheless allowed
 *     to stand is the stopping rule plus the editor's outlier read above — not
 *     the sentence's literal wording, which currently says the opposite thing.
 *
 *  3. p90 IS RETIRED for legibility. Every luminance figure in the log is a
 *     composed MEDIAN with `p90 - p50` beside it, and near-zero spread is not
 *     claimed as a credit anywhere.
 *
 *  4. THE TANK OBJECT FAMILY. No scene in s24-s39 touches the vessel / tap /
 *     flow family, so nothing here rhymes on it and nothing here constrains
 *     s46 / s47 / s57 further.
 *
 *  5. CASCADE ANCHORS ARE MEASURED (tools/tts/clauses.py + faster-whisper).
 *     s26's four chips fire on four separate pop() calls at four measured word
 *     onsets, never on a fixed `popEach(+1.10, 0.6)`. See the s26 note.
 */
import fs from "node:fs";
import { execFileSync } from "node:child_process";

const CH = 3;
const LINES = ["3.1", "3.2", "3.3", "3.4", "3.5", "3.6", "3.7", "3.8",
               "3.9", "3.10", "3.11", "3.12", "3.13", "3.14", "3.15", "3.16"];
const FIRST = 24;                                   // scene s24 == line 3.1
const TIMING = JSON.parse(
  fs.readFileSync("../passive-income-number-en/assets/voice/timing.json", "utf8"));
const T = 0.45;                                     // format.json scene.transition_seconds

const TARGET = "245,158,11";
const FUND   = "34,197,94";
const WARN   = "239,68,68";

/* ---------------------------------------------------------------- the spec
 * arch   §7 `arch`            f1     §7 `ground` (the --f1 temperature arc, §11)
 * art    §7 `art`             ctr    §7 `ctr` (centred)
 * ken    §5: the direction flips at every boundary except a hold. ch3 has no
 *        hold; ch2 ended on s23 `o`, so ch3 opens `i` and alternates.
 * size   §3's deterministic focal rule, keyed on stmt LENGTH so it cannot drift
 *        when a string changes:  <=24 -> 112 · 25-48 -> 88 · else 76.
 *        Computed below, never written here.
 * role   §1: amber = a published figure under examination (every BLS numerator
 *        and the share), green = a division that closed at a sourced rate (the
 *        two corpora), red = what an assumption costs (rung three named, and
 *        the whole fine-print run). 3.1, 3.3, 3.9 and 3.16 carry NO role — a
 *        kerb, a division by twelve, a porch and a held breath assert nothing.
 * bgpos  the KEN OFFSET knob (ch2's s20). `.bg` is `background-size: cover`
 *        inside an inset:-8% box, so a source narrower than 16:9 carries real
 *        VERTICAL slack that `center` throws away symmetrically. Spending it
 *        moves the PHOTOGRAPH, never the type. Used on exactly four scenes,
 *        each because it buys measurable median and keeps the subject; the
 *        numbers are in the notes and in the log.
 */
const SCENES = [
  { line: "3.1", arch: "a", f1: "#1c2027", art: "off", ctr: true, ken: "i",
    kick: "RUNG TWO", stmt: "It is parked outside.",
    img: "s24.jpg", bgpos: "center bottom",
    note: "RUNG TWO. ⚠ THE ch2 CEO CARRY-FORWARD, IMPLEMENTED: the chapter opens on a SUBJECT, not a surface. A red hatchback at the kerb of a dark rowhouse street, double yellow line running out of frame — sound-off it says 'a car parked on a street', which is the whole line. It is also the chapter's darkest photograph (source p90 126, the lowest of sixteen) and that is deliberate per §11: ch3 opens cool and neutral before the rungs warm it. `bgpos` is why it is not darker still: the source is 1880x1253 against a 16:9 box, so cover leaves 196px of vertical slack, and `center bottom` spends all of it on the empty night sky. Measured on the graded cover-crop, composed median 26.6 -> 37.7 (+11.1) with p10 unchanged at 11.6-11.8 and the car fully in frame. The ken then ends TIGHTER AND LEFT (see the ken block), i.e. on the car." },

  { line: "3.2", arch: "b", f1: "#2a2113", art: "off", ctr: true, ken: "o", role: TARGET,
    kick: "TRANSPORTATION, ONE YEAR",
    num: "$13,318", numTo: 13318, numPrefix: "$", numAt: 2.45,
    foot: "Average annual transportation spending per consumer unit, 2024 — BLS Consumer Expenditures, 19 Dec 2025",
    img: "s25.jpg",
    note: "TRANSPORTATION, ONE YEAR. The numerator, amber: a published figure under examination, never green — a BLS bill is not an answer (§1 thesis check). The foot carries the full provenance, which is what satisfies the BILL branch of the assert below AND tools/check_vo_frame.py, whose MAGNITUDE pattern fires on this line's spoken 'thirteen thousand'. A fuel nozzle in a filler neck with the forecourt blurred out: the EMCO WHEATON wordmark that killed the first candidate is gone, and nothing legible remains. The num anchor is MEASURED — faster-whisper puts '$13' at 2.200s into the clip, clip starts at scene +0.25, so +2.45 (§5 published no fallback for this line)." },

  { line: "3.3", arch: "d", f1: "#1f1e1c", art: "off", ctr: false, ken: "i", brule: 400,
    kick: "PER MONTH",
    num: "$1,110", numTo: 1110, numPrefix: "$", numAt: 1.85,
    chips: [["Payment", "Insurance"], ["Fuel", "Repairs"]],
    chipAt: [4.37, 5.01, 5.89, 6.71],
    foot: "$13,318 divided by 12 — arithmetic, not a separate statistic",
    img: "s26.jpg",
    note: "PER MONTH. NO role, deliberately: a division of a published statistic by twelve is a measurement, not a landing (§1, §2's dry list). The foot states the derivation on screen, which keeps the figure out of the derived-income branch — it is a bill walked down to a month, not income drawn off a corpus (§4). ⚠ THE FOUR SLIPS ARE NOW ONLY IN THE CHIPS (fin-assets en ch3 §3): the storyboard assumed the photograph carried a payment stub, an insurance card, a fuel receipt and a repair invoice; six sheets could not buy that frame. So the cascade is load-bearing copy, not decoration, and it is not cut. ⚠ THE PHOTOGRAPH CHANGED 2026-08-09, and the SCALE ERROR is what changed it (editor-en-ch3-1 finding 3; predecessor at assets-ch3/superseded-r4/). The outgoing frame was an aerial car park of ~80 vehicles under a line about the running cost of ONE car — the viewer's car, the one s24 parked at the kerb — and it held that mismatch for the chapter's LONGEST span, 8.355s. The incoming frame is a full-frame macro of one worn tyre on speckled asphalt: one vehicle, and unreadable as a fleet. RE-MEASURED HERE on this stage's own chain rather than taken from the source log: composed median 85.3 (#9 of 16), p10 8.4, spread 25.2, step-in -8.5 out of s25 — against the outgoing 92.6 / 19.5 / 32.6. It is NOT the floor (s37 20.5, s24 36.7, s36 50.3, s33 57.9 all sit below it), which matters because this is the longest-held scene and the stopping rule makes a relocated floor a defect exactly there. No bgpos: the source is 1880x1058, already 16:9, so there is no slack in either axis to spend. ⚠ DECLARED JUDGEMENT CALL FOR THE EDITOR, not argued past them (fin-assets §2, and this build agrees): the frame names a car PART, not a car. Sound-off it says 'a worn tyre' — automotive, one of four, the part that visibly wears out and gets bought again — and it does NOT say 'the monthly cost of the car outside'. Three things carry it in context: it is the third beat of a four-scene car run (street / nozzle / tyre / door handle), the kicker reads PER MONTH, and the four chips already carry the enumeration. What it fixes is real (a claim about one car was illustrated with eighty); what it costs is that the whole object is gone. The ledger in fin-assets §3 is the evidence that no whole-car frame is buyable in this pool at >=1600px without a legible badge, and that the two brand-free ones that exist measure 11.6 / 2.2 — i.e. the floor, on the longest-held scene. ⚠ ONE THING THE SOURCE LOG CALLS 'EVEN' THAT IS NOT: the chip band measures median 86.7 / p10 9.1 (I reproduce it exactly), but a tread face is high-frequency texture with five hard black grooves, not a calm ground. It is safe HERE only because a .chip carries its own solid --panel fill and a 3px --edge border, so the cascade reads against its own ground and not against the rubber. The 112px focal has no such backing and is the one thing to look at on the sheet. ⚠ THE CASCADE IS SPEECH-ANCHORED, four separate pop() calls at four MEASURED onsets, never popEach at a fixed +1.10: faster-whisper puts 'Payment' 4.120s / 'insurance' 4.760 / 'gas' 5.640 / 'repairs' 6.460 into the clip (+0.25 lead-in => +4.37 +5.01 +5.89 +6.71). tools/tts/clauses.py --cells 4 independently returned +1.47 +4.50 +5.07 +5.88 and corroborates three of the four within 0.13s; its FIRST cell is 2.9s early because the line's second pause-separated part is 'that is about eleven hundred and ten dollars a month' and not a named item, which is exactly the failure mode the tool's own docstring warns against forcing. Word onsets win on this line. ⚠ brule 400, NOT ch1's 252 (found in the max-density snapshot pass, snapshots/qa/b1 at 16.27s): archetype D's rule is meant to compress the type band, and at 252 it ran straight THROUGH the $1,110 glyphs — .arch-d's stack starts at y144 (110px scene padding + 34px margin) and the 112px focal occupies y198-308, so 252 is inside it. ch1's 252 is correct for a stack whose focal is a chip row, not a .huge. 400 clears the foot's baseline at y361 and still sits 196px above the cascade. ctr is N because the declared cascade owns archetype D's band (§7's own rule), and the chips are 2+2 in two EXPLICIT rows — .row wraps, so four chips left to themselves silently orphan 3+1 and no checker flags it (§3)." },

  { line: "3.4", arch: "b", f1: "#12351f", art: "off", ctr: true, ken: "o", role: FUND,
    kick: "RUNG TWO", rate: "AT A 4.0% WITHDRAWAL RATE",
    num: "$332,950", numTo: 332950, numPrefix: "$", numAt: 3.57,
    foot: "$13,318 divided by 0.04 · ILLUSTRATIVE ARITHMETIC",
    meas: 0.1696, mlab: "THE LADDER",
    img: "s27.jpg", bgpos: "center top",
    note: "RUNG TWO, worked. #s27-rate is a first-class 40px .sub in the role colour and it arrives at +1.10, BEFORE the number lands at +3.57: the assumption is on screen first and the figure arrives into it (§4). Rung two on the §9a corpus ladder — ONE scale for the whole cut, 920px = $1,963,375, so $332,950 is scaleX 0.1696 = 156.0px. Numerator and denominator are a PAIR (gotcha 7): never move one without the other and never re-use this component at another scale. Anchor MEASURED: '$333' at 3.320s into the clip => scene +3.57 (§5's fallback said +3.73). ⚠ THE PHOTOGRAPH CHANGED 2026-08-08 (predecessor at assets-ch3/superseded-invariant-r1/): a flush door handle in its recess on a white car flank in daylight, with the door shut-line down the left, replacing the chrome handle on a dark sedan that measured composed median 25.4 / p10 0.0 and arrived on a -67.0 step. RE-MEASURED HERE on this stage's own chain, not taken from the source log: median 97.9 (#4 of 16), p10 82.9 (#2), step-in +5.3 out of s26. The white body does NOT grade to charcoal — 255 through brightness(.62) contrast(1.05) lands at 159.6 and grayscale(.32) is chroma-only — so the risk on a white subject is FLATNESS, never darkness, and that is what the spread is watched for. `bgpos: center top` is fin-assets' measured recommendation, TAKEN and verified by looking at both graded crops at composed size: `center` clips the top of the handle recess against the frame edge, `center top` brings the whole object in with clearance and costs nothing (median 97.0 -> 97.9, p10 82.2 -> 82.9, spread 26.1 -> 38.1); `center bottom` clips harder and collapses the spread to 12.4, which is the even-and-empty direction the CEO's sharpening names. ⚠ DECLARED: ~75% of this frame is a smooth panel gradient, so it is the chapter's emptiest photograph — kept because §10 routes the heaviest type frame (rate + mega + foot + the 156px measure bar) to the quietest picture, and the type band measures median 96 / p10 88, flatter and more legible than s28's already-passing 110." },

  { line: "3.5", arch: "a", f1: "#301519", art: "off", ctr: true, ken: "i", role: WARN,
    kick: "RUNG THREE", stmt: "The biggest line in the budget.",
    img: "s28.jpg",
    note: "RUNG THREE, named. The first red of the chapter: red is what an assumption COSTS, and 3.5's second clause is 'it has a landlord or a bank attached to it'. A bank of steel mailboxes receding down an apartment lobby — the address is someone else's building, which is the half of the line the type does not say. §10 declares the landlord-or-bank clause gets NO cut-in (a swap at f≈0.8 would leave a 1.2s second framing, under the floor)." },

  { line: "3.6", arch: "b", f1: "#2a2113", art: "off", ctr: true, ken: "o", role: TARGET,
    kick: "HOUSING, ONE YEAR",
    num: "$26,266", numTo: 26266, numPrefix: "$", numAt: 1.90,
    foot: "Average annual housing spending per consumer unit, 2024 — BLS Consumer Expenditures, 19 Dec 2025",
    img: "s29.jpg", bgpos: "center top",
    note: "HOUSING, ONE YEAR. Amber numerator, same treatment as 3.2. ⚠ THE ANCHOR IS THE DECLARED FLOOR, NOT THE WORD: faster-whisper puts '$26' at 0.680s into the clip = scene +0.93, which is BEFORE variant B's +1.90 floor and before the foot has taken cue 2 at +1.10 — the figure would land on top of its own provenance. §5's floor exists for exactly this and is applied: +1.90, 0.97s after the word. The alternative (dropping the foot to cue 3) would put a BLS numerator on screen with no provenance for two seconds, which is what the BILL branch of the assert exists to prevent. `bgpos: center top` keeps the two-storey brick houses and the dusk sky and drops the empty road: composed median 39.4 -> 58.5 (+19.1) on identical p10, the largest legibility gain any framing knob buys in this chapter." },

  { line: "3.7", arch: "b", f1: "#2e2411", art: "share", ctr: false, ken: "i", role: TARGET,
    lift: true, vrule: [150, 300],
    kick: "SHARE OF THE BUDGET", num: "33.4%", numAt: 1.90,
    sub: "$2,189 a month",
    foot: "Housing was 33.4% of total household spending in 2024; housing and transportation together were 50.4% — BLS",
    img: "s30.jpg",
    note: "SHARE OF THE BUDGET — the chapter's ONE drawn layer (§8 budgets ch3 exactly one). `housing-share`: one full-width bar = total household spending, its left 33.4% solid --target, the rest a ghost at GHOST_A. Rule 8 holds because a roof says 'housing' and cannot say 'a third of everything they spent'. §3 resolves this scene's double cue block: the script carries both `num: 33.4%` and `stmt: $2,189 a month`, so the stmt becomes the 40px qualifier #s30-sub and the num is the focal. NO countUp on this one — countUp rounds with Math.round, so counting to 33.4 would print `33%` on the settle frame, i.e. a DIFFERENT published figure; the focal is a literal string with a pop. Anchor: 'a third' is spoken at 0.480s into the clip = scene +0.73, under the +1.90 floor, so the floor applies (same call as 3.6). ⚠ THE PHOTOGRAPH CHANGED 2026-08-09 AND IT WAS THE CHAPTER'S BLOCKER (editor-en-ch3-1 finding 1; predecessor at assets-ch3/superseded-r4/). NOTHING DRAWN CHANGED — the bar was never the defect: it measures 0.342 fill with the tick at 0.334 on the encode, which is BLS CE 2024's housing share of $78,535. The defect was underneath it. The outgoing frame was birds on a brick parapet at dusk with NO roof, NO pitch, NO chimney and NO building form, so with the type covered it said 'a third of something' and never said HOUSING — the noun this scene exists to quantify. My own attempt-1 note defended it as 'a dusk roofline'; the photograph had no roofline in it, and the lesson is that a note may only describe a file that has been opened. The incoming frame IS the noun: a weathered shingle roof running across the lower half, three brick chimneys against a winter sky, a white clapboard gable at frame right. RE-MEASURED HERE: composed median 97.6 (#5 of 16), p10 36.3 (#5), spread 18.9, step-in +38.8 out of s29 — against the outgoing 62.1 / 12.6 / 16.3. No bgpos: the three crops differ by 1.4 median and 2.1 spread, inside this chain's own noise, and a knob that only moves a decimal is worse than no knob. `.art-lift` still applies and still for rule 9's reason, only now against a BRIGHT BLUE SKY rather than an orange one — the plate-scoped darken, which cannot touch the photograph outside the rect. ⚠ NOT `.band`: .band is bottom 54% and this plate's rect is y150-760. THE DRAWN LAYER'S OWN GROUND, checked by measuring the rect the bar actually occupies rather than the frame: the plate maps viewBox 1:1 and `meet` centres it, so the bar lands at screen x1190-1910, y395-515 — sky plus the large right-hand chimney, mean 87.7 / sd 31.0 / p10 36.1 / p90 112.8 before .art-lift, which then drops it to roughly 49 with the sd near 15. Two low-frequency regions, brick courses and sky; no competing texture under a 120px bar. ⚠ WATCH ON THE SHEET: the type band (left 55%, y15-75%) measures median 104.3 / p90 117.8, the BRIGHTEST type ground in the chapter — above s28's 110.5 p90 and s27's 96. Precedent says AA passes; precedent is not a check, so `npm run check`'s AA count is the thing to read, not the precedent." },

  { line: "3.8", arch: "b", f1: "#12351f", art: "off", ctr: true, ken: "o", role: FUND,
    kick: "RUNG THREE", rate: "AT A 4.0% WITHDRAWAL RATE",
    num: "$656,650", numTo: 656650, numPrefix: "$", numAt: 3.23,
    foot: "$26,266 divided by 0.04 · ILLUSTRATIVE ARITHMETIC",
    meas: 0.3345, mlab: "THE LADDER",
    img: "s31.jpg",
    note: "RUNG THREE, worked — the chapter's largest figure and rung three of five on the §9a ladder: $656,650 is scaleX 0.3345 = 307.7px of the 920px track, so the bar is now a third full and the climb is visible. Rate on screen at +1.10, number at a MEASURED +3.23 ('$657' at 2.980s into the clip; §5's fallback said +3.32). ⚠ THE INVARIANT BREACH IS FIXED AT ITS ONLY HONEST LEVER — THE PHOTOGRAPH. Attempt 1 escalated this frame rather than working around it: the outgoing brass-collared knob on a black ground measured composed median 7.1, LAST of sixteen, p10 0.0, arriving on -52.8, and the build PROVED no framing knob could reach it (zero horizontal slack; vertical framing moved the median half a point). fin-assets replaced the file (predecessor at assets-ch3/superseded-invariant-r1/) and this build re-measured the incoming one on its own chain: an ornate brass escutcheon and a cut-glass knob on a WHITE panelled door standing open onto a sunlit entry — median 70.7 (#10 of 16), p10 43.2 (#3), spread 59.9, step-in +8.6 out of s30. The chapter's largest figure is off the floor on every clause the ruling names. The spread is two real regions (a sunlit doorway against a shadowed hall), not the specular pinprick p90 was retired for. No bgpos: `center top` buys +1.2 median / +1.3 p10, under the measurement's own noise and not worth moving a composed frame for. Sound-off it reads as a way into a home, and the fitting is American vernacular (a crystal knob on a Victorian backplate, a storm door beyond), so place and era match the currency. The ken still runs `o`." },

  { line: "3.9", arch: "a", f1: "#241d15", art: "off", ctr: true, ken: "i",
    kick: "SAY IT SLOWLY", stmt: "It stopped sounding like savings.",
    img: "s32.jpg",
    note: "SAY IT SLOWLY — the warm domestic beat §11 puts here, and the chapter's only step back onto the neutral-warm axis before six red scenes. NO role: the line asserts nothing about a rate, and a colour here would claim one. An American front porch, white balusters and a brown door in late-afternoon shadow: the second half of the line is 'starts sounding like a house', so the photograph finishes the sentence the type stops halfway through. Composed median 90.9, p10 29.1 — 7th and 4th of sixteen, so it is a legible frame carrying a soft beat, which is the right way round." },

  { line: "3.10", arch: "c", f1: "#301519", art: "off", ctr: true, ken: "o", role: WARN,
    kick: "THEIR OWN FINE PRINT", stmt: "The papers say this themselves.",
    img: "s33.jpg",
    note: "THEIR OWN FINE PRINT. First of the fine-print run and the shortest scene in the chapter (3.569s), so the ladder finishes at +1.10 and the frame then holds for 2.4s under the ken alone — correct for a hand-off line. Hands leafing a thick stapled document seen along a glass desk: §10 allows hands and objects, never a face, and there is none. Archetype C with `.centred`, because .art-off leaves the ledger's artefact side empty and a split with nothing opposite is a hole." },

  { line: "3.11", arch: "c", f1: "#38151a", art: "off", ctr: true, ken: "i", role: WARN,
    kick: "LIMIT ONE",
    stmt: "“The study did not adjust for taxes or transaction costs.”",
    foot: "Cooley, Hubbard and Walz, AAII Journal, February 1998 — verbatim, from the study's own methodology",
    img: "s34.jpg",
    note: "LIMIT ONE — THIS CHAPTER'S PAYOFF FRAME (see the build log for the four-clause scoring). The one verbatim HARD-primary quotation the fine-print run exists to put on screen, at the hottest red the chapter reaches. ⚠ THE CURLY QUOTES ARE VERIFIED, NOT ASSUMED: storyboard §14 left `“ ”` open against the 97-codepoint subset; dumped with fontTools at build, all four of “ ” ‘ ’ are present, so the typographic marks the storyboard asked for are used rather than the straight fallback. (ch2's straight quotes stay as they are — those are cited paper TITLES in a 26px foot, not a display quotation.) A raking-light macro of contract clauses with a black pen: composed median 128.3 (#2 of 16) and p10 92.1 (#1 by 9 points over s27), the most legible photograph in the chapter by either measure. ⚠ THE CROP THE EDITOR ASKED FOR WAS ATTEMPTED, MEASURED AND STOPPED (editor-en-ch3-1 finding 2). The finding is real and I confirmed it ON THE ENCODE, not on the jpg: at t=64.0 `9. Insurance`, `The Contractor`, `10. Assignment` and `the prior written consent of the` are all plainly readable outside the type. But the file has no framing slack that reaches them. A 16:9 window over a 1733-wide source is 975 rows of 1300; the sharp band that carries every legible word occupies rows ~430-900, i.e. DEAD CENTRE, so both extreme full-width crops (rows 0-975 and 325-1300) contain the whole of it and `bgpos` is a no-op on the problem. Only a zoom crop can exclude the words, and the pen LIES ALONG the plane of focus — the same band. So the two families are: (a) keep the pen, which measures median 120.5 / p10 11.0 (x700-1733, y260-841) and 118.8 / 9.1 (x780-1733, y180-716), because the pen goes from ~8% of the frame to ~30% — that FAILS payoff clause 3 outright, where s27 sits at p10 82.9; (b) lose the pen. The best (b) is the top blurred band, y0-400 (y0-460 still reads `carry liab` at the lower edge): 124.0 / 110.3 / 9.1, which passes clauses 2, 3 and 4 more comfortably than the frame does today — and fails clause 1, the binary sound-off gate that runs FIRST and has standing to disqualify. I rendered it graded at composed size and looked at it: it is a soft grey field with diagonal smudges and no nameable object, which is the exact shape of the three frames the CEO's rationale of record names (the blank notebook page, the pale-sky field, the closed notebook cover). The bottom band (129.6 / 120.5 / 3.9) is worse still — its one legible object is the word `SIGNATURE` over a signature, which answers the editor's objection by shouting it. Every crop also costs a 2.9x upscale against today's 1.29x, on the one frame whose subject is fine print. STOPPED, per the brief's own instruction: the crop costs the clause. Kept as shipped, and the remaining lever is the editor's second option — a re-fetch to journal-style two-column body text with no headings and no clause numbers. §10's letter still holds meanwhile (no title, no figure, no agency name)." },

  { line: "3.12", arch: "d", f1: "#38151a", art: "off", ctr: true, ken: "o", role: WARN,
    kick: "WHAT THAT MEANS", stmt: "Every rung here is a BEFORE-TAX number.",
    img: "s35.jpg",
    note: "WHAT THAT MEANS — the CONSEQUENCE, which is why §7 breaks the C run with a D here: 3.10/3.11 and 3.13/3.14 are documents, and this is what the documents cost the viewer. A blank IRS 1040 and 1040-SR on a black ground. ⚠ The form is legibly dated 2020 (fin-assets §5, flagged not hidden): no line in this chapter makes a year claim, the shape is the current 1040, and every tax-form photograph in both pools carries some year. It is also the chapter's brightest frame on composed median (139.2, #1 of 16) sitting on the hottest red ground — deliberate under the invariant: the darkest longest-held frame must be the most substantive, and this is the inverse of that risk, not an instance of it." },

  { line: "3.13", arch: "c", f1: "#301519", art: "off", ctr: true, ken: "i", role: WARN,
    kick: "LIMIT TWO", num: "30 YEARS", numAt: 4.19,
    foot: "Bengen's worst case was a 30-year horizon; Trinity's payout periods ran 15, 20, 25 and 30 years",
    img: "s36.jpg",
    note: "LIMIT TWO. The focal is a HORIZON, not a money figure, so no countUp — a clock counting to thirty would animate a duration the papers state flatly. Anchor MEASURED and LATE: '30' is spoken at 3.940s into the clip = scene +4.19 on a 6.312s scene, so the foot takes cue 2 at +1.10 and the frame carries kicker + foot for three seconds before the figure lands on its own word. ⚠ tools/chapter_sheet.py samples at +2.6, so THIS SCENE WILL SHEET WITHOUT ITS FOCAL and that is not a defect — judge it from the mp4 (the same call ch2 recorded for s16 at +3.33). A plain white dial on oak slats; the MOBATIME wordmark that killed the first candidate is gone." },

  { line: "3.14", arch: "c", f1: "#38151a", art: "off", ctr: true, ken: "o", role: WARN,
    kick: "THEIR CONCLUSION",
    stmt: "“Early retirees who anticipate long payout periods should plan on lower withdrawal rates.”",
    foot: "Cooley, Hubbard and Walz, AAII Journal, February 1998, Conclusion — verbatim",
    img: "s37.jpg",
    note: "THEIR CONCLUSION — the longest string in the cut (90 characters with its quotation marks) and therefore the ladder's bottom step, 76px over three lines, which §3 sizes to 222px in an 860px box. Never interpolated and never below 76. An open book under a desk lamp against a deep blue wall, the text dissolved to grey blocks: §10 forbids a legible title, figure or agency name on this slot, and six sheets of the pool's Turkish, German, Polish and Bible pages are why this one is a book rather than the script's 'last page of a paper'. It is the fifth book-or-paper frame in the cut (fin-assets §4) — different scale, different ground, different subject from s33 and s34, and ch4 must not add a sixth." },

  { line: "3.15", arch: "a", f1: "#301519", art: "off", ctr: true, ken: "i", role: WARN,
    verdict: true,
    kick: "THE ONLY ONE", stmt: "And it is a warning, not a plan.",
    img: "s38.jpg", bgpos: "center top",
    note: "THE ONLY ONE — a verdict scene. Its stmt enters with `pop` (back.out(1.7)) rather than `rise`; that IS the slam, and it is what makes the `stamp` SFX legal without a .stamp pill and without one word of new copy (§2, §13 D10). This cut has no .stamp component by design: five lines are verdicts and five rotated pills would be a tic. An empty two-lane highway running to the horizon under flat light. `bgpos: center top` keeps the horizon — which is the whole subject — and drops foreground tarmac: composed median 63.8 -> 77.4 (+13.6) and p10 12.7 -> 28.7 (+16.0), the largest p10 gain in the chapter." },

  { line: "3.16", arch: "a", f1: "#101720", art: "off", ctr: true, ken: "o",
    kick: "NOW THE ONE YOU CAME FOR",
    img: "s39.jpg",
    note: "NOW THE ONE YOU CAME FOR. §5's declared one-element scene: a kicker and nothing else, at +0.30, held for 3.5s. It is the emptiest frame in the cut and that is the beat — a held breath before the SHOVE into 4.1. THE SHOVE IS NOT BUILT HERE: s39 -> s40 is a chapter BOUNDARY, s40 lives in ch4, and tools/cut_assemble.py is what puts the two projects next to each other. This project therefore carries no `acts` argument and s39 takes its BARE scene_duration — a chapter has no successor to cross-dissolve into. The ground is the chapter's coldest (#101720): fin-assets warned that the closed-laptop lid is the chapter's second-lightest photograph, so the cold has to come from the .field, and it does." },
];

/* ------------------------------------------------------------- the timings
 * Read straight off timing.json, rebased by the chapter's own offset. GAPS —
 * not totals — are what a re-time destroys, so the gaps are asserted below
 * against the shipped measurement, one joint at a time. */
const flat = (t) => t.replace(/\n/g, " ");

const rows = LINES.map((id) => {
  const l = TIMING.lines.find((x) => x.id === id);
  if (!l) throw new Error(`timing.json has no line ${id}`);
  return l;
});
const OFF = rows[0].scene_start;
const last = rows[rows.length - 1];
const ROOT = +(last.scene_start + last.scene_duration - OFF).toFixed(3);

const sc = SCENES.map((s, i) => {
  const r = rows[i];
  if (r.id !== s.line) throw new Error(`spec/timing mismatch at ${i}`);
  const own = r.scene_duration;
  const n = FIRST + i;
  return {
    ...s, i, n, id: "s" + n,
    start: +(r.scene_start - OFF).toFixed(3),
    dur: own,                                                // the scene's own hold
    dd: i < SCENES.length - 1 ? +(own + T).toFixed(3) : own,  // + the cross-dissolve overlap
    track: n % 2 ? 1 : 2,                                    // or overlapping_clips_same_track
    astart: +(r.audio_start - OFF).toFixed(3),
    adur: r.duration,
    // the declared framings — one value per photograph the scene holds. No
    // scene in ch3 swaps its photograph, so each is a single value equal to the
    // scene's own hold; emitting it anyway removes any question about whether
    // an absent attribute means "one framing" or "not declared" (§6c).
    framings: [own],
    /* The focal size is keyed on the COPY's length, so a "\n" — a typographic
     * break decision, not copy — is flattened out of the count first. */
    size: s.stmt == null ? null
      : flat(s.stmt).length <= 24 ? 112 : flat(s.stmt).length <= 48 ? 88 : 76,
  };
});

/* the asserts that make a silent re-time impossible ---------------------- */
sc.forEach((s, i) => {
  if (i === 0) { if (s.start !== 0) throw new Error("chapter does not start at 0"); return; }
  const gap = +(sc[i - 1].start + sc[i - 1].dd - s.start).toFixed(3);
  if (Math.abs(gap - T) > 0.005) throw new Error(`${s.id} overlaps by ${gap}, expected ${T}`);
  if (sc[i - 1].track === s.track) throw new Error(`${s.id} shares a track with its neighbour`);
  const shipped = +(rows[i].scene_start - rows[i - 1].scene_start).toFixed(3);
  if (Math.abs(shipped - (s.start - sc[i - 1].start)) > 1e-9)
    throw new Error(`${s.id} gap drifted from the shipped cut`);
});
if (Math.abs(sc[sc.length - 1].start + sc[sc.length - 1].dur - ROOT) > 1e-9)
  throw new Error("last scene does not land on the chapter root");
/* format.json scene.max_scene_seconds. The thing that must clear 9.0 is the
 * longest SINGLE FRAMING, and framings must partition the scene (check_build
 * asserts the same) or a cosmetic split would duck the guard. */
sc.forEach((s) => {
  const sum = +s.framings.reduce((a, b) => a + b, 0).toFixed(3);
  if (Math.abs(sum - s.dur) > 0.002)
    throw new Error(`${s.id} framings sum to ${sum}, scene holds ${s.dur}`);
  s.framings.forEach((f) => {
    if (f > 9.0) throw new Error(`${s.id} holds one photo for ${f}s (max 9.0)`);
  });
});

/* §3's build guard: no `/` and no `?` in any on-screen string. Both ARE in the
 * dumped 97-codepoint subset — and so are the curly quotes §14 left open, which
 * is why 3.11 and 3.14 render `“ ”` rather than the straight fallback —
 * but the storyboard bans them as COPY: `·` is this cut's separator and the cut
 * asks no rhetorical questions on screen. It also sweeps the ₹ this cut is
 * forbidden to show and any Devanagari that could arrive from the sibling cut.
 * SUBSET, dumped at build (fontTools, tools/scaffold/assets/fonts/
 * NotoSansFinance-var.woff2): every glyph used below is in it; a missing glyph
 * renders as tofu and no check catches it. */
const SUBSET = new Set(
  " !\"#$%&'()*+,-./0123456789:;=?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]_" +
  "abcdefghijklmnopqrstuvwxyz|£·–—‘’“”€₹");
const chipList = (s) => (s.chips || []).flat();
const strings = (s) =>
  [s.kick, s.stmt, s.num, s.rate, s.sub, s.foot, s.mlab, ...chipList(s)]
    .filter(Boolean).map(flat);
sc.forEach((s) => {
  strings(s).forEach((t) => {
    const bad = t.match(/[/?₹×≈~→▶¢]/);
    if (bad) throw new Error(`${s.id}: on-screen string carries "${bad[0]}" — banned in this cut`);
    if (/[ऀ-ॿ]/.test(t)) throw new Error(`${s.id}: Devanagari in the -en cut`);
    for (const ch of t)
      if (!SUBSET.has(ch)) throw new Error(`${s.id}: "${ch}" is not in the font subset — it renders as tofu`);
  });
  if (s.stmt && s.num) throw new Error(`${s.id}: never a stmt AND a num (§3)`);
  if (s.size && s.size < 76) throw new Error(`${s.id}: focal below the ladder floor`);
  chipList(s).forEach((c) => {
    if (c.length > 22) throw new Error(`${s.id}: chip "${c}" is ${c.length} chars (max 22)`);
  });
  if (s.chips && s.chipAt.length !== chipList(s).length)
    throw new Error(`${s.id}: ${chipList(s).length} chips but ${s.chipAt.length} measured onsets`);
  if (s.chips) {
    // §3: rows are declared EXPLICITLY, and format.json cascade tops out at 5.
    s.chips.forEach((r) => {
      if (r.length > 3) throw new Error(`${s.id}: more than 3 chips in one row`);
    });
    if (chipList(s).length > 5) throw new Error(`${s.id}: cascade over 5 items`);
    // a speech-anchored cascade must be monotonic and must land inside the scene
    s.chipAt.forEach((t, k) => {
      if (k && t <= s.chipAt[k - 1]) throw new Error(`${s.id}: chip onsets are not monotonic`);
      if (t + 0.6 > s.dur) throw new Error(`${s.id}: chip ${k + 1} finishes past the scene`);
    });
  }
  /* the drawn layer never becomes the whole scene, and a centred scene has no
   * plate to put one in (.scene.centred .plate is display:none). */
  if (s.art !== "off" && s.ctr) throw new Error(`${s.id}: drawn art on a centred scene`);
  if (s.art !== "off" && !s.img) throw new Error(`${s.id}: art without a photograph`);
  if (!s.img) throw new Error(`${s.id}: no photograph — photo_free_scene_ratio is 0`);
});

/* ---------------------------------------------------------- the drawn layer
 * ONE, in a sixteen-scene chapter, which is §8's own budget for ch3 and well
 * under the archetype note's "three or four in a twelve-to-fourteen scene
 * chapter is the TOP of the range". WHAT WAS DECLINED, so the choice is on the
 * record rather than implied:
 *   · 3.3's four costs — the count is carried by four CHIPS on ladder C and the
 *     photograph was deliberately routed to a subject with nothing countable in
 *     it. Drawing four boxes over four chips duplicates the chips, not the
 *     photograph, which is rule 8 one level up.
 *   · 3.13's thirty years — a drawn clock face over a photographed clock face is
 *     the ghost-envelope-over-an-envelope failure by name.
 *   · 3.11 / 3.14's fine print — a quotation is not a proportion. There is
 *     nothing to measure and §8's own test ("if you cannot say what the art
 *     asserts that the picture cannot") returns nothing.
 *   · 3.4 / 3.8's two corpora — they already carry the §9a measure bar, which is
 *     the cut's one climb device and is not a per-chapter drawn layer.
 *
 * s30 · housing-share — p-b, viewBox 0 0 800 610, xMidYMid meet.
 * THE ARITHMETIC, stated at the point of edit (gotcha 7): the filled part is
 * EXACTLY 0.334 of the track, because BLS CE 2024 puts housing at 33.4% of total
 * household spending. One number, written once, driving both the tick position
 * and the span() endpoint — so the drawing and its animation cannot disagree.
 * GEOMETRY: track x 40..760 inside an 800-wide viewBox; `meet` on an 860x610
 * plate scales 1.0 and centres, so plate x0 maps to screen 1150 and the whole
 * mechanism is on canvas (gotcha 8 — .p-b maps viewBox x 1:1 and anything past
 * vx=800 does not exist on the encode). 120px tall and SOLID: §8's floor is 9px
 * and a ghost track is a filled rect, never an outline.
 * GHOST_A is a FILL-opacity, not an opacity, and it is 0.55 for the reason ch2's
 * s14 settled on: --ink at full weight against --target (a dark gold) makes the
 * EMPTY two-thirds out-shout the filled third on the one frame whose job is to
 * say a third. fade() no longer clobbers an authored `opacity` (motion.js,
 * 2026-08-08) so either would now survive — fill-opacity is still the right
 * lever, because it leaves the entrance fade free to run 0 -> 1. */
const SHARE = 0.334, GHOST_A = 0.55,
  BAR_X = 40, BAR_W = 720, BAR_Y = 245, BAR_H = 120;
function housingShare(id) {
  if (SHARE !== 0.334) throw new Error("housing-share: BLS CE 2024 puts housing at 33.4%");
  if (BAR_X + BAR_W > 800) throw new Error("housing-share: the bar leaves the plate");
  const mark = BAR_X + BAR_W * SHARE;
  return [
    `<svg class="art" id="${id}-art" viewBox="0 0 800 610" preserveAspectRatio="xMidYMid meet">`,
    `      <rect class="fl" id="${id}-track" fill-opacity="${GHOST_A}" x="${BAR_X}" y="${BAR_Y}"` +
      ` width="${BAR_W}" height="${BAR_H}"/>`,
    `      <rect class="flt" id="${id}-fill" x="${BAR_X}" y="${BAR_Y}"` +
      ` width="${BAR_W}" height="${BAR_H}" style="transform-origin:0% 50%"/>`,
    `      <rect class="fl" id="${id}-mark" x="${mark - 5}" y="${BAR_Y - 34}"` +
      ` width="10" height="${BAR_H + 68}"/>`,
    `    </svg>`,
  ].join("\n");
}

/* §9a · the measure bar. 920px = $1,963,375 (rung five, the whole household at
 * 4.0%) => 1px = $2,134.10. This is the ONE scale for all six ladder frames in
 * the cut and it may not be re-used at another. */
const LADDER_TOP = 1963375;
sc.filter((s) => s.meas).forEach((s) => {
  const corpus = Number(s.num.replace(/[^0-9]/g, ""));
  const exact = corpus / LADDER_TOP;
  if (Math.abs(exact - s.meas) > 0.0005)
    throw new Error(`${s.id} measure ${s.meas} != ${corpus}/${LADDER_TOP} = ${exact.toFixed(4)}`);
});

/* ------------------------------------------------------------------ markup */
const esc = (t) => t.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
const PLATE = { a: "p-a", b: "p-b", c: "p-c", d: "p-d" };
const ART = { share: housingShare };

function scene(s) {
  const cls = ["scene", "clip", "arch-" + s.arch, "has-photo"];
  if (s.art === "off") cls.push("art-off"); else cls.push("art-forward");
  if (s.ctr) cls.push("centred");
  if (s.lift) cls.push("art-lift");
  const alpha = s.role === FUND ? ".10" : ".12";
  const style = s.role ? ` style="--tint:rgba(${s.role},${alpha})"` : "";
  const glow = s.role ? ` style="--gl:rgba(${s.role},.16)"` : "";
  const roleName = s.role === FUND ? "--fund" : s.role === TARGET ? "--target"
    : s.role === WARN ? "--warn" : "";
  const L = [];
  L.push(`\n<!-- ${s.line} · ${s.arch.toUpperCase()} · ${s.f1} · art ${s.art}` +
    `${s.ctr ? " · centred" : ""}${roleName ? " · " + roleName : ""}\n     ${s.note} -->`);
  L.push(`<section class="${cls.join(" ")}" id="${s.id}" data-track-index="${s.track}"` +
    ` data-start="${s.start}" data-duration="${s.dd}" data-framings="${s.framings.join(",")}"${style}>`);
  L.push(`  <div class="bg" id="${s.id}-bg" style="background-image:url(assets-ch3/final/${s.img})` +
    `${s.bgpos ? `;background-position:${s.bgpos}` : ""}"></div>`);
  L.push(`  <div class="field" style="--f1:${s.f1}"><div class="rules"></div><div class="glow"${glow}></div></div>`);
  if (s.art !== "off") {
    L.push(`  <div class="plate ${PLATE[s.arch]}" id="${s.id}-plate">`);
    L.push(`    <div class="plate-in" id="${s.id}-pin"><div class="hatch"></div>`);
    L.push(`      ${ART[s.art](s.id)}`);
    L.push(`    </div>`);
    L.push(`  </div>`);
  }
  L.push(`  <div class="scrim"></div>`);
  if (s.brule)
    L.push(`  <div class="brule" id="${s.id}-br" style="top:${s.brule}px"></div>`);
  if (s.vrule)
    L.push(`  <div class="vrule" id="${s.id}-vr" style="top:${s.vrule[0]}px;height:${s.vrule[1]}px"></div>`);
  L.push(`  <div class="stack" id="${s.id}-stack">`);
  L.push(`    <p class="kicker" id="${s.id}-kick">${esc(s.kick)}</p>`);
  const rc = s.role === FUND ? " fundc" : s.role === TARGET ? " targetc"
    : s.role === WARN ? " warnc" : "";
  if (s.rate)
    L.push(`    <p class="sub${rc}" id="${s.id}-rate">${esc(s.rate)}</p>`);
  if (s.num)
    L.push(`    <p class="huge${rc}" id="${s.id}-num">${esc(s.num)}</p>`);
  if (s.stmt)
    L.push(`    <p class="huge${rc}" id="${s.id}-stmt" style="font-size:${s.size}px">` +
      `${esc(s.stmt).replace(/\n/g, "<br>")}</p>`);
  if (s.sub)
    L.push(`    <p class="sub" id="${s.id}-sub">${esc(s.sub)}</p>`);
  if (s.foot)
    L.push(`    <p class="foot" id="${s.id}-foot">${esc(s.foot)}</p>`);
  L.push(`  </div>`);
  if (s.chips) {
    // Ladder C's cascade. NOT blockframe's .row: .row is a child of .stack, and
    // .arch-d hangs the stack at the TOP of the frame, while D's whole point is
    // that the mechanism owns the bottom two-thirds. Absolutely positioned into
    // .p-d, exactly as en ch1 does on 1.2 and 1.6 — which is what makes the
    // cascade genuinely occupy the archetype's other side and this scene not
    // `.centred`. Two EXPLICIT rows of two (§3): .row wraps, so four chips left
    // to themselves orphan 3+1 and no checker flags it.
    L.push(`  <div class="v-chiprow" id="${s.id}-chips">`);
    let k = 0;
    s.chips.forEach((row, r) => {
      L.push(`    <div class="v-chiprow-r" id="${s.id}-crow${r + 1}">`);
      row.forEach((c) => L.push(`      <div class="chip" id="${s.id}-c${++k}">${esc(c)}</div>`));
      L.push(`    </div>`);
    });
    L.push(`  </div>`);
  }
  if (s.meas) {
    // §9a. OUTSIDE .stack on purpose: .measure/.measure-lab position themselves
    // at left calc(50% - 460px), which is why `.centred` does not hide them and
    // why the device survives on a photo-led cut.
    L.push(`  <p class="measure-lab under" id="${s.id}-mlab">${esc(s.mlab)}</p>`);
    L.push(`  <div class="measure under" id="${s.id}-meas"><div class="measure-fill fund" id="${s.id}-mf"></div></div>`);
  }
  L.push(`  <div class="grain"></div>`);
  L.push(`</section>`);
  return L.join("\n");
}

const audio = sc.map((s) =>
  `<audio id="vo-${CH}-${s.i + 1}" class="clip" data-track-index="10" ` +
  `data-start="${s.astart}" data-duration="${s.adur}" src="assets/voice/${s.line}.mp3"></audio>`
).join("\n");

const map = (f) => "{ " + sc.map((s) => `${s.id}: ${f(s)}`).join(", ") + " }";

const kenJs = sc.map((s) =>
  `ken("#${s.id}-bg", S.${s.id}, D.${s.id}, ${s.ken === "i"});`).join("\n");

const html = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>The Passive-Income Number — en · CHAPTER 3 · rungs two and three, and the fine print</title>

<!-- ===========================================================================
     CHAPTER 3 — two more rungs worked at the same rate, then the two criticisms
     the papers make OF THEMSELVES, placed where the rule is being used rather
     than saved for a disclaimer nobody hears. Sixteen cuts, ${ROOT}s, s24-s39.

     GENERATED by build.mjs from ../passive-income-number-en/assets/voice/
     timing.json. Do not hand-edit a timing here: every data-start /
     data-duration / data-framings, the S and D maps, the sixteen <audio> rows
     and the root duration are computed from that one file and asserted against
     the shipped cut's GAPS — a re-time is exactly what produces a correct total
     with every internal cut drifted. Design lives in build.mjs's SCENES table.

     Chapter offset is ${OFF}s (timing.json's own scene_start for line 3.1), so
     this concatenates frame-exact. The LAST scene carries its bare
     scene_duration: a chapter has no successor to cross-dissolve into, and
     tools/cut_assemble.py adds the +0.45 overlap back at fold-in. The cut's
     first SHOVE sits on the s39 -> s40 boundary and therefore belongs to the
     assembly, not to this project.

     Layout: blockframe-9 (run.json architecture, body_class "") under the
     chapter archetype layer. NO RAIL, no chapter title, no scene counter, no
     slide number — format.json chapter_design.rail is false and the viewer must
     never be shown that this video is chapter-based.

     Fourteen of sixteen scenes are art-off, and thirteen of those are centred.
     Rule 8 retires the drawn layer wherever the photograph already carries the
     beat, and .centred then re-centres the stack so the archetype's empty side
     is not a hole. The two that are not centred each have something REAL on the
     other side: 3.3's four-chip cascade owning archetype D's band, and 3.7's
     housing-share bar — the chapter's one drawn layer, and the only beat here
     that is a PROPORTION rather than a figure.

     Every scene carries has-photo and a real full-bleed .bg under the LOCKED
     grade. No per-scene brightness override anywhere: photo_free_scene_ratio is
     0, fin-assets confirmed none is needed, and the photograph is the only
     variable there is. Four scenes set a background-position, which moves the
     PHOTOGRAPH inside its own cover box and is not a grade knob.
     =========================================================================== -->

<link rel="stylesheet" href="assets/blockframe.css">
<link rel="stylesheet" href="assets/chapter-design.css">
<style>
#root { position: relative; width: 1920px; height: 1080px; overflow: hidden; background: var(--bg); }
/* the four plate rects, one per archetype (format.json chapter_design.archetypes) */
.p-a { left: 0;      top: 0;     width: 1920px; height: 1080px; }
.p-b { left: 1120px; top: 150px; width: 860px;  height: 610px;  }
.p-c { left: 1046px; top: -60px; width: 934px;  height: 1200px; }
.p-d { left: 0;      top: 424px; width: 1920px; height: 656px;  }

/* ONE-OFF, this composition only (hence .v-): the declared chip cascade on 3.3.
   Not blockframe's .row — that is a child of .stack, which .arch-d hangs at the
   TOP of the frame, and D's whole point is that the mechanism owns the bottom
   two-thirds. Absolutely positioned into .p-d, the same component en ch1 uses on
   1.2 and 1.6, with one addition: 3.3 names FOUR things, so the rows are
   declared as two of two rather than left to .row's wrap (§3 — four chips
   silently orphan 3+1 and no checker flags it).
   Vertical arithmetic: a .chip is 32px type + 18px padding top and bottom + 3px
   border = 91px, so two rows plus the 18px gap is 200px. Top 596 puts the block
   at y596-796 — inside .p-d (424-1080), clear of the .stack above it (which
   ends at about y430 on this scene) and clear of the watermark box (y956-1040)
   and the 110px bottom safe padding. */
.v-chiprow   { position: absolute; z-index: 2; left: 0; right: 0; top: 596px;
               display: flex; flex-direction: column; align-items: center; gap: 18px; }
.v-chiprow-r { display: flex; align-items: center; justify-content: center; gap: 22px; }

/* ONE-OFF, SCOPED TO 3.7 (hence the id, not a class): THE ART-LIFT FEATHER.
   fin-editor blocker, editor-en-ch3-2 finding 1. '.has-photo.art-lift .plate-in'
   in chapter-design.css is a flat 'linear-gradient(140deg, rgba(13,16,23,.66),
   rgba(13,16,23,.34))' with NO falloff on any edge, so it terminates on a line at
   the plate rect. Over the outgoing near-black dusk still that line was invisible;
   over the incoming daylight sky it measured a 14.6-luma step across one pixel at
   x=1120, 10.6 at y=150 and 5.1 at y=760 — a translucent grey card with hard
   corners parked in frame right for 7.1s, on the chapter's only drawn moment.
   THE PANEL IS NOT THE DEFECT AND IS NOT REMOVED. It is rule 9's plate-scoped
   lever and the ghost track needs it. What changes is that the darkening now
   FALLS OFF to zero before it reaches the rect instead of being cut by it.

   Arithmetic, in the plate's own box (860x610 at 1120,150; the art viewBox is
   800x610 under 'meet', so it maps 1:1 with a 30px x-offset):
     bar   art x40-760  y245-365  -> plate-local x70-790,  y245-365
     tick  art x270-280 y211-399  -> plate-local x300-310, y211-399
   so everything drawn lives inside x 8.1-91.9% and y 34.6-65.4%. The plateau
   below (x >= 8%, y 34-66%) covers it exactly and the falloff uses the empty
   80% of the box that the editor counted: 211px of headroom above the tick,
   207px below, 70px to its left. THE RIGHT EDGE NEEDS NO FEATHER — the plate
   runs to x=1980 on a 1920 frame, so its right edge is off-canvas (this is the
   same declared geometry the check reports as 'panel_out_of_canvas #s30-pin
   right 60px', and note 3 of the same review ruled the p-b rect not to be moved).
   Stops are a smoothstep approximation, not linear: a linear ramp leaves a
   first-derivative kink at each end that reads as a faint Mach line on a flat sky.

   Structure: a ::before rather than the element itself, because a 'mask-image' on
   '#s30-pin' would mask its CHILDREN — the bar would fade out at its own left end
   and misreport where the fill starts. The pseudo-element is first in DOM order
   and unpositioned-z, so it paints under '.hatch' and '.art'. '#s30-pin' carries
   no plateKen (only 'ken("#s30-bg")'), so this layer is static and cannot drift.

   WHERE THIS BELONGS: '.has-photo.art-lift .plate-in' in
   tools/scaffold/assets/chapter-design.css, which has three users — this scene,
   en-ch2 s16 and hi-ch3 s28. This stage may not write tools/, so it is scoped
   here and the promotion is logged as owed. Measured no-op evidence for ch2 s16
   is in logs/fin-build-en-ch3-4.md. */
#s30-pin { background: none; }
#s30-pin::before {
  content: ""; position: absolute; inset: 0; pointer-events: none;
  background: linear-gradient(180deg,
      rgba(13,16,23,0)    0%,  rgba(13,16,23,.03)  8%,
      rgba(13,16,23,.14) 16%,  rgba(13,16,23,.36) 24%,
      rgba(13,16,23,.56) 30%,  rgba(13,16,23,.62) 34%,
      rgba(13,16,23,.62) 66%,  rgba(13,16,23,.56) 70%,
      rgba(13,16,23,.36) 76%,  rgba(13,16,23,.14) 84%,
      rgba(13,16,23,.03) 92%,  rgba(13,16,23,0)  100%);
  -webkit-mask-image: linear-gradient(90deg,
      rgba(0,0,0,0) 0%, rgba(0,0,0,.05) 1.5%, rgba(0,0,0,.22) 3%,
      rgba(0,0,0,.55) 4.5%, rgba(0,0,0,.85) 6%, rgba(0,0,0,.98) 7.4%,
      #000 8%, #000 100%);
          mask-image: linear-gradient(90deg,
      rgba(0,0,0,0) 0%, rgba(0,0,0,.05) 1.5%, rgba(0,0,0,.22) 3%,
      rgba(0,0,0,.55) 4.5%, rgba(0,0,0,.85) 6%, rgba(0,0,0,.98) 7.4%,
      #000 8%, #000 100%);
}
</style>
</head>
<body>
<div id="root" class="cut-en" data-composition-id="main" data-width="1920" data-height="1080" data-start="0" data-duration="${ROOT}">
${sc.map(scene).join("\n")}

<!-- Voice only. The bed and the SFX are the post-mix step (assets/audio.json ->
     tools/audio/mix.py): the renderer does not guarantee in-page volume
     automation, and a bed that silently failed to duck would bury the voice in a
     video that still passed every check. -->
${audio}

</div>

<script src="assets/js/gsap.min.js"></script>
<script src="assets/js/motion.js"></script>
<script>
/* S = scene starts · D = each scene's OWN hold (not its dissolve-padded
   data-duration), so the photograph's push finishes exactly as the next scene
   begins to fade up. Both generated from timing.json. */
var S = ${map((s) => s.start)};
var D = ${map((s) => s.dur)};
var IDS = ${JSON.stringify(sc.map((s) => s.id))};

/* Cross-dissolves, one call, before the per-scene cues. NO 'acts' argument: the
   cut's two shoves are s39 -> s40 and s58 -> s59 (§12) and both are chapter
   BOUNDARIES from this project's point of view — s39's successor is not in this
   file. s24's dissolve is against the incoming chapter boundary and is correct
   here; in the assembled cut it dissolves out of s23. */
sceneTransitions(IDS, S);

/* THE PHOTOGRAPH CARRIES THE MOTION — one move per scene, never a plate push
   competing with a ken. Direction alternates from s24's push-in (ch2 ended on
   s23 pulling back) and there is no hold in this chapter to interrupt it.
   ken(zoomIn) runs scale 1.00 -> 1.16 with xPercent -2.5 -> +2.5, and moving the
   element RIGHT shows content to its LEFT, so a push-in ends tighter and
   left-of-centre: on 3.1 that is the parked car, which is the ch2 CEO
   carry-forward paid in the motion as well as in the frame. */
${kenJs}

/* THE TYPE — cue ladder variant A (storyboard §5) on the statement scenes:
   kicker +0.30, statement +1.10, then the foot at +1.90. Fixed offsets, constant
   whatever a clip's length; every gap is 0.80s and the photograph is already up
   at +0.00, so first_cue_by_seconds (0.5) is met by the kicker. 3.16 is §5's
   declared one-element scene — a kicker and nothing else. */
${sc.map((s) => `rise("#${s.id}-kick", S.${s.id} + 0.30, 0.7, 14);`).join("\n")}
${sc.filter((s) => s.stmt && !s.verdict).map((s) => `rise("#${s.id}-stmt", S.${s.id} + 1.10, 0.7, 18);`).join("\n")}

/* 3.15 · THE VERDICT SLAM. §2: the five verdict scenes take pop() (back.out(1.7))
   on their stmt instead of rise(). That IS the slam — it needs no .stamp pill
   and no new copy, and it is what makes the "stamp" SFX legal here. */
${sc.filter((s) => s.verdict).map((s) => `pop("#${s.id}-stmt", S.${s.id} + 1.10, 0.6);`).join("\n")}

/* THE FIGURE SCENES — cue ladder variant B: kicker +0.30, then the rate (or the
   sub, or where there is neither, the foot) at +1.10, then the number ANCHORED
   on its own spoken word with a +1.90 floor, then the foot at num + 0.80 if the
   foot did not take cue 2. The rate is on screen BEFORE the corpus lands: the
   assumption is up first and the number arrives into it (§4).

   EVERY ANCHOR IS MEASURED, not interpolated. §5 gives character-offset
   fractions as a FALLBACK and says fin-build resolves each against
   faster-whisper WORD timings. Run on this cut's own clips (base.en, word
   timestamps), the figure's first spoken word starts at:
     3.2  "$13"      2.200s into the clip -> scene +2.45  (no fallback published)
     3.3  "$1"       1.600s                -> scene +1.85  (no fallback published)
     3.4  "$333"     3.320s                -> scene +3.57  (§5's fallback said 3.73)
     3.6  "$26"      0.680s                -> scene +0.93  -> FLOORED to +1.90
     3.7  "a third"  0.480s                -> scene +0.73  -> FLOORED to +1.90
     3.8  "$657"     2.980s                -> scene +3.23  (§5's fallback said 3.32)
     3.13 "30"       3.940s                -> scene +4.19  (no fallback published)
   Clips start at scene +0.25 (MEDIUM lead_in_seconds), which is the +0.25 in
   each figure above. TWO ARE FLOORED and both are declared in their scene notes:
   3.6 and 3.7 speak their figure inside the first second, which is before cue 2
   has put the provenance or the qualifier on screen. §5's floor is the rule for
   exactly that case and the number lands ~1s after its word rather than on top
   of its own foot.

   countUp is for MONEY. 33.4% and 30 YEARS take a bare pop(): countUp rounds
   with Math.round, so counting to 33.4 would settle on "33%" — a different
   published figure — and counting a horizon animates something the papers
   state flatly. */
${sc.filter((s) => s.num).map((s) => {
  const cue2 = s.rate ? "rate" : s.sub ? "sub" : "foot";
  const o = [];
  o.push(`rise("#${s.id}-${cue2}", S.${s.id} + 1.10, 0.7, 18);`);
  o.push(`pop("#${s.id}-num", S.${s.id} + ${s.numAt.toFixed(2)}, 0.6);`);
  if (s.numTo != null)
    o.push(`countUp("#${s.id}-num", S.${s.id} + ${s.numAt.toFixed(2)}, 0, ${s.numTo}, "en-US", 1.2, ` +
      `${JSON.stringify(s.numPrefix || "")}, ${JSON.stringify(s.numSuffix || "")});`);
  if (s.meas)
    o.push(`span("#${s.id}-mf", S.${s.id} + ${s.numAt.toFixed(2)}, 1.2, 0, ${s.meas});`);
  if (cue2 !== "foot" && s.foot)
    o.push(`fade("#${s.id}-foot", S.${s.id} + ${(s.numAt + 0.80).toFixed(2)}, 0.5);`);
  return o.join("\n");
}).join("\n")}

/* The foot on a STATEMENT scene is cue 3 (+1.90), not cue 4 — variant A puts the
   foot at +2.70 only when a rate or a sub already took +1.90. */
${sc.filter((s) => s.foot && s.stmt).map((s) => `fade("#${s.id}-foot", S.${s.id} + 1.90, 0.5);`).join("\n")}

/* 3.3 · THE CASCADE, SPEECH-ANCHORED. Four separate pop() calls at four measured
   word onsets — NOT popEach at a fixed offset, which is what put hi ch1's s6
   cascade 0.20s BEFORE its first noun and left 5.07s of dead air. cues.py reads
   this form and would emit one chip per call at that call's own time; 3.3 is on
   the storyboard's DRY list, so it emits none and the cascade is silent by
   choice. The four onsets are 0.64 / 0.88 / 0.82 apart, which is the shape of
   the sentence rather than a template's 0.6. */
${sc.filter((s) => s.chips).map((s) => chipList(s)
  .map((_c, k) => `pop("#${s.id}-c${k + 1}", S.${s.id} + ${s.chipAt[k].toFixed(2)}, 0.45);`)
  .join("\n")).join("\n")}

/* 3.7 · THE SHARE. The track is total household spending; the fill is housing,
   and it stops at EXACTLY ${SHARE.toFixed(3)} — the endpoint is the same constant
   the tick is drawn from, so the drawing and the animation cannot disagree.
   \`span\`, not \`fill\`: fill() always runs to scaleX 1 and a third-filled bar needs
   a declared endpoint. The mark lands last, on the boundary the fill stopped at.
   Assembled by +2.95, inside chapter_design's "about +3.3", so the contact
   sheet's +2.6 sample shows a mechanism nearly complete rather than a blank
   plate. 3.7 is DRY, so none of this emits a sound — the scene keeps its joint
   transition and nothing else, which is right for a measurement. */
fade("#s30-track", S.s30 + 1.55, 0.45);
span("#s30-fill", S.s30 + 1.90, 0.90, 0, ${SHARE});
fade("#s30-mark", S.s30 + 2.50, 0.40);

window.__timelines = window.__timelines || {};  /* the LINTER reads this file, not motion.js */
register();                                    /* -> window.__timelines["main"] */
</script>

<script>
/* ===========================================================================
   THE RATE ASSERTS — run.json.constraints, mechanised. Carried forward VERBATIM
   from chapter 2, including its third BILL branch, because a per-chapter copy
   that drifts is worse than no assert: tools/check_vo_frame.py reads RATE and
   MARKER back out of THIS block, so the frame-side and the VO-side checks can
   never disagree about what a rate is.

   (1) withdrawal_rate_on_screen: "Every corpus figure must carry its assumed
       withdrawal/return rate ON SCREEN in the same frame as the number. A number
       without its assumption visible is a fabricated promise."
       LIVE HERE on s27 (\$332,950) and s31 (\$656,650), both of which carry a
       first-class 40px #sN-rate .sub reading "AT A 4.0% WITHDRAWAL RATE".

   (2) derived_income_carries_assumption (EXTENDED 2026-08-07): a DERIVED INCOME
       figure — the corpus's own OUTPUT — carries the rate in frame or an explicit
       ILLUSTRATIVE marker. A BLS bill divided by twelve is NOT derived income, so
       the marker branch accepts a stated provenance (BLS / CONSUMER EXPENDITURE).
       LIVE HERE on s30, whose qualifier reads "\$2,189 a month" and whose foot
       carries the BLS provenance in the same frame.

   (3) THE BILL BRANCH, added in ch2. (1) is deliberately narrow — it fires only
       on the eight CORPUS tokens, so a published numerator could render
       completely bare and pass. \$13,318, \$1,110, \$26,266 and \$2,189 are exactly
       that shape. §4 says the corpus branch must NOT fire on them, correctly,
       but "must not demand a rate" is not "may be bare": a BILL has to carry, in
       frame, either a rate, the published provenance, or its own derivation.
       All four of this chapter's bills do — s25 and s29 by provenance, s26 by
       derivation ("\$13,318 divided by 12"), s30 by both — and the point of the
       assert is that a density pass which drops a foot line cannot silently make
       one of them a bare number.

   Throwing is the point: "hyperframes check"'s runtime pass fails on an uncaught
   page error, and a silent console.warn is what let this ship twice. All three
   branches were re-proven on THIS file by planting
   "\$656,650 \$2,500 a month \$13,318" into s33's kicker — a scene with no rate,
   no marker and no derivation — and confirming three separate messages; see the
   build log.

   ⚠ THIS ASSERT IS FRAME-ONLY BY CONSTRUCTION. It reads rendered text, so it
   cannot see a VO line that SPEAKS a figure over a bare frame
   (run.json.owed.derived_income_assert_is_frame_only). That half is
   tools/check_vo_frame.py, run against this file at build:
     python3 tools/check_vo_frame.py passive-income-number --cut en --chapter 3
   =========================================================================== */
(function () {
  var CORPUS  = /\\$(?:254,225|332,950|656,650|1,500,000|1,929,260|1,963,375|5,555,556|7,271,759)/;
  var RATE    = /4\\.0%|3\\.11%|1\\.08%/;
  var DERIVED = /\\$[\\d,]+\\s*(?:a month|A MONTH|per month|PER MONTH)/;
  var MARKER  = /ILLUSTRATIVE|BLS|CONSUMER EXPENDITURE/;
  var BILL    = /\\$(?:10,169|847|13,318|26,266|2,189|1,110|6,545|78,535)/;
  var DERIVATION = /divided by/i;
  var bad = [];
  Array.prototype.forEach.call(document.querySelectorAll("section.scene"), function (s) {
    var txt = s.textContent;
    var rated = Array.prototype.some.call(
      s.querySelectorAll('[id^="' + s.id + '-rate"]'),
      function (el) { return RATE.test(el.textContent); });
    var c = txt.match(CORPUS);
    if (c && !rated)
      bad.push(s.id + " renders " + c[0] + " with no #" + s.id + "-rate carrying a rate");
    var d = txt.match(DERIVED);
    if (d && !rated && !MARKER.test(txt))
      bad.push(s.id + " renders the derived income " + d[0] +
               " with neither a rate nor an ILLUSTRATIVE marker in frame");
    var b = txt.match(BILL);
    if (b && !rated && !MARKER.test(txt) && !DERIVATION.test(txt))
      bad.push(s.id + " renders the published figure " + b[0] +
               " with no rate, no provenance and no derivation in frame");
  });
  if (bad.length) throw new Error("RATE ASSERT FAILED — " + bad.join(" · "));
})();
</script>
</body>
</html>
`;

fs.writeFileSync("index.html", html);

/* ------------------------------------------------------------- the sound pass
 * DERIVED, never hand-typed (storyboard §2): tools/audio/cues.py reads the file
 * this script just wrote and emits one cue per REAL motion call, at that call's
 * own time, bound through tools/audio/kit.json's helper column. Running it from
 * here rather than as a second command is what guarantees the cue list and the
 * markup came from the same derivation of timing.json.
 *
 * The special cases cues.py cannot derive live in the CUT's own
 * studio/videos/passive-income-number-en/assets/cues-tables.json, written from
 * storyboard §2. ch3's dry scenes are s25, s26, s29, s30, s36 — every BLS
 * numerator, every division by twelve and the horizon — plus s27 and s31, the
 * two rungs: §2's own prose says "Rungs two, three and five (s27, s31, s67)" are
 * dry and §7's sfx column says "—" for both, but the JSON block they were
 * transcribed into lists only s67. Reconciled in the table file, which is that
 * fact's one home; the reasoning is in the build log. If every rung rings, the
 * ladder has no shape, and the measure bar is what gives it one visually.
 *
 * ONE correction the tool cannot make: cues.py defaults `music` to bed-resolve,
 * and §2/D12 chooses **bed-tension** for this cut — its argument is a COST, not
 * a habit. The bed is a per-video fact. */
/* cues.py validates the SHIPPED assets/audio.json as well as the list it just
 * derived, and exits 1 on a `cue_min_gap_seconds` breach in either. Left in
 * place, last build's file is what gets validated — so the run that FIXES a gap
 * dies on the artefact it is fixing, before it can write the replacement. Drop
 * it first: the next two lines regenerate it unconditionally. */
fs.rmSync("assets/audio.json", { force: true });
const derived = JSON.parse(execFileSync("python3",
  ["../../../tools/audio/cues.py", "."], { encoding: "utf8" }));
derived.music = "bed-tension";
derived._bed = "bed-tension (storyboard §2 / §13 D12) — cues.py defaults to "
  + "bed-resolve; this cut's argument is a cost, not a habit. Overridden by "
  + "build.mjs, not hand-edited into the generated file.";
fs.writeFileSync("assets/audio.json", JSON.stringify(derived, null, 1) + "\n");

const nCues = derived.sfx.filter((c) => c.at != null).length;
console.log(`assets/audio.json: ${nCues} cues (derived by tools/audio/cues.py)`);
console.log(`index.html: ${sc.length} scenes, root ${ROOT}s, offset ${OFF}s`);
sc.forEach((s) => console.log(
  `  ${s.id} ${s.line}  start ${String(s.start).padStart(7)}  dur ${String(s.dur).padStart(6)}` +
  `  d-dur ${String(s.dd).padStart(6)}  track ${s.track}  ${s.arch.toUpperCase()}` +
  `${s.ctr ? " centred" : ""} ${s.art}${s.size ? "  focal " + s.size : ""}` +
  `${s.numAt ? "  num +" + s.numAt.toFixed(2) : ""}`));
