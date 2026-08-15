/* build.mjs — emits index.html + assets/audio.json for CHAPTER 6 of
 * passive-income-number, -en (@moneymavens101, $). THE LAST CHAPTER OF THE CUT.
 *
 *   node build.mjs        (or: npm run build)
 *
 * WHY A GENERATOR AND NOT HAND-TYPED HTML. Every data-start, data-duration,
 * data-framings, the JS `S`/`D` maps, every <audio> row and the root duration
 * are FOUR homes for the same number, and the failure this project keeps
 * hitting is durations that sum to exactly the right total while every internal
 * cut has drifted. All four are computed here from ONE source —
 * ../passive-income-number-en/assets/voice/timing.json — and the asserts under
 * the timing block compare GAPS, not totals, so a silent re-time throws instead
 * of shipping.
 *
 * Chapter 6 is lines 6.1-6.13 = scenes s69-s81. The rebase constant is
 * timing.json's own scene_start for 6.1 (441.900s), which is ch5's offset
 * 335.817 plus ch5's declared root 106.084 — so the six chapters concatenate
 * frame-exact. THIS CHAPTER HAS NO SUCCESSOR AT ALL: s81 carries its bare
 * scene_duration and the chapter root IS the cut's root minus the offset.
 *
 * SPEC, not invention. arch / ground / art / ctr / focal / ken / sfx are
 * storyboard-en.md §7 verbatim; the kicker / stmt / num / sub / foot strings are
 * script-en.md's own `[arch …]` cue blocks (one home per fact — the storyboard
 * deliberately does not restate copy). Structure ported from ch4's build.mjs
 * with ch5's later guards folded in.
 *
 * WHAT IS NEW IN THIS CHAPTER, and each is measured here rather than inherited:
 *
 *  1. s75.jpg DID NOT EXIST. §7/§10 declare it a derived crop of s76 — the
 *     INVERTED hold, where the wide frame is the fetched one — and ffmpeg is not
 *     on fin-assets' allowlist. Cut here at `crop=1280:720:20:250` and recorded
 *     in `s75.jpg.src`, `manifest.json` and `CREDITS.txt` in the same move, the
 *     ch2 `s10b` / ch4 `s42` / ch5 `s56b`+`s67b` convention. The rect is a
 *     MEASURED choice — see the s75 note.
 *
 *  2. THREE DRAWN LAYERS RESOLVE HERE (§8): `ladder-bars-1-3` on 6.7,
 *     `ladder-bars-4-5` on 6.8 and `ladder-overrun` on 6.9. This is en's
 *     declared device (`container_ladder_2026-08-09` records hi's PHOTOGRAPHIC
 *     container ladder as the thing it replaces) and it must never be ported to
 *     the hi cut. Every bar width is computed from ONE constant — the §9a scale,
 *     920px = $1,963,375 — and the assert below recomputes each from its own
 *     corpus figure, so a bar and the figure it draws cannot be edited apart
 *     (gotcha 7: a proportion's numerator and denominator are a PAIR).
 *     ⚠ `no_return_promise`: the five bars are five figures the video has ALREADY
 *     put on screen with their rate, and the overrun is 5,555,556/1,963,375 =
 *     2.8296 between two such figures. NOTHING here is a forecast, and the art
 *     carries no axis, no tick, no scale and no numeral — asserted on the emitted
 *     markup, with comments stripped first.
 *
 *  3. THE HOLD IS INVERTED AND RUNS OUT. §5: "s75->s76 is the ONE hold that runs
 *     OUT — a pull-back is what makes the ladder get bigger." plateKen 1.16->1.08
 *     then 1.08->1.00, one ground across both, no `transition` at the joint (the
 *     cut's cues-tables.json already lists the pair). Built as ONE continuous
 *     move the FIRST time (`chapters._carry_forward_en_ch1_to_ch2_ch6` names this
 *     exact pair; s3/s4 cost three rounds by being built as two files dissolving).
 *
 *  4. EVERY ANCHOR IS MEASURED AGAINST THE VOICE, and so is the hold hand-off.
 *     faster-whisper base.en word timestamps on this cut's own clips, all 13
 *     lines. §5's only published fallback for this chapter (s77 +6.08) is 0.49s
 *     LATE against the measured onset. The hold hand-off is measured too and
 *     reported rather than re-cut: a hold joint IS a scene boundary and
 *     timing.json is its only home.
 *
 *  5. s81 IS THE CUT'S ONE TERMINAL CTA. `.cta`, cue ladder D, `pop` at +0.40 —
 *     the one `--pop` element in 81 scenes. No `.stamp` pill anywhere in this cut
 *     (§13 D10), which is also why the `.stamp.warn` red-on-red fix landed
 *     upstream today and is NOT re-patched locally here: a second copy of a fix
 *     is how the bug comes back.
 */
import fs from "node:fs";
import { execFileSync } from "node:child_process";

const CH = 6;
const LINES = ["6.1", "6.2", "6.3", "6.4", "6.5", "6.6", "6.7",
               "6.8", "6.9", "6.10", "6.11", "6.12", "6.13"];
const FIRST = 69;                                   // scene s69 == line 6.1
const CUT = "../passive-income-number-en";
const TIMING = JSON.parse(fs.readFileSync(`${CUT}/assets/voice/timing.json`, "utf8"));
/* transition_seconds is READ, never retyped (owed item 2 of the hi ch5 log). */
const FMT = JSON.parse(fs.readFileSync("../../../tools/format.json", "utf8"));
const T = FMT.scene.transition_seconds;             // 0.45

const TARGET = "245,158,11";
const FUND   = "34,197,94";
const WARN   = "239,68,68";
const POP    = "255,92,57";

/* ---------------------------------------------------------------- the spec
 * arch   §7 `arch`            f1     §7 `ground` (the --f1 temperature arc, §11)
 * art    §7 `art`             ctr    §7 `ctr` (centred)
 * ken    §5: the direction flips at every boundary EXCEPT a hold, where the
 *        partner continues its predecessor's move. ch5 ended on s68 `i`, so this
 *        chapter opens `o` and alternates to s74; s75/s76 are the OUT hold; s77
 *        flips back to `i` and alternates to the end. ⚠ That flip inverts the
 *        odd/even parity for s77-s81 against s69-s74, which is not a mistake —
 *        it is what "flips at every boundary except the hold" means when the hold
 *        spends two scenes going the same way. Declared here so a later pass does
 *        not "restore" the parity and break the hold.
 * size   §3's deterministic focal rule, keyed on stmt LENGTH so it cannot drift
 *        when a string changes:  <=24 -> 112 · 25-48 -> 88 · else 76. Computed
 *        below, never written here.
 * role   §1: amber = a published figure under examination, green = a division
 *        that closed at a sourced rate, red = what an assumption costs, orange =
 *        the one CTA. 6.10 and 6.11 carry NO role, deliberately.
 * bgpos  the KEN OFFSET knob — moves the PHOTOGRAPH inside its own cover box,
 *        never the type, and it is not a grade knob. ONE scene uses it (s79) and
 *        the number behind it is in that scene's note.
 */
const SCENES = [
  { line: "6.1", arch: "a", f1: "#301519", art: "off", ctr: true, ken: "o", role: WARN,
    kick: "ONE MORE THING", stmt: "It is not a settled number.",
    img: "s69.jpg",
    note: "ONE MORE THING — the chapter opens by ADMITTING the rate is not settled, before it recaps anything. That admission is what stops the ladder reading as a promise (`no_return_promise`), and it is why the chapter's first frame is red rather than green. §10's own override for this slot (a brass plumb bob, chosen so s80's empty chair is not doubled) was worked through three sheets and 18 cells and does not exist in either pool; what ships is a ROOSTER WEATHER VANE in silhouette, compass arms visible — an instrument whose whole job is to keep turning, which states 6.1 more directly than a plumb bob would, and still not a chair. Declared by fin-assets and carried unchanged: the pantile roof reads Mediterranean as easily as US-Southwest (no signage, plates or vehicles in frame), and a rooster carries a faint dawn association that 6.11 later disclaims. It is the BRIGHTEST frame in the chapter on this build's composed chain (median 43.19), which is the right end of the run for the frame that opens it — `floor_stopping_rule_and_p10_comparator_2026-08-09` §2 gives the sound-off gate standing on a chapter's opening frame, and it passes: type covered, a viewer names a weather vane." },

  { line: "6.2", arch: "c", f1: "#2a2113", art: "off", ctr: true, ken: "i", role: TARGET,
    kick: "ONE ANSWER", num: "3.9%", numAt: 2.23,
    foot: "\"The State of Retirement Income: 2025 Edition\", published 3 Dec 2025,\nsets the rate for a 2026 retiree — 30-year horizon, 90% success probability, 30-50% equity",
    img: "s70.jpg",
    note: "ONE ANSWER — Morningstar. NO countUp and NO #s70-rate. No countUp because countUp rounds with Math.round and counting to 3.9 would settle on `4%`, which is a DIFFERENT published figure and the very one this scene exists to contrast with. No separate rate element because §4 lists s70 among the nine frames carrying a RATE AS THEIR FOCAL — printing a rate under itself reads as a defect — and the assert stays honest because the frame prints no dollar figure at all. The foot is the provenance and it is the whole defence of the number, so it takes cue 2 at +1.10 and is on screen 1.13s before the figure. Anchor MEASURED: faster-whisper puts `3` at 1.980s into the clip => scene +2.23 (§5 published no fallback for this line). ⚠ CARRIED FORWARD FROM fin-assets, unresolved and not hidden: the promoted photograph is a thick document fanned open on pale wood and about 40 words of body prose are legible at full resolution — CORPORATE-GOVERNANCE prose, no title, no figure, no agency and no brand, so it impersonates no source and asserts nothing false. fin-assets offered a free re-pick (`--pick s70=5`) whose only text-free alternative would have made s70 a near-twin of s81's closed notebook. Left as fin-review's call, on the encode." },

  { line: "6.3", arch: "c", f1: "#2e2411", art: "off", ctr: true, ken: "o", role: TARGET,
    kick: "ANOTHER ANSWER", num: "4.7%", numAt: 2.17,
    foot: "Bengen's \"Universal SAFEMAX\", A Richer Retirement, Wiley, August 2025 —\na wider asset mix, roughly 400 historical start dates, worst case still October 1968",
    img: "s71.jpg",
    note: "ANOTHER ANSWER — and it is BENGEN'S OWN, which is the reason this beat exists: the man who wrote the 4% rule moved his own number up. Same construction as s70 (no countUp, no #s71-rate, the foot at +1.10 as cue 2). Anchor MEASURED: `4` at 1.920s into the clip => scene +2.17. Amber, not green: a published rate under examination is exactly what `--target` means in this video, and green would say the division closed at it. PHOTOGRAPH RE-FETCHED at attempt 2 (review en-ch6-1 finding 2, closed by fin-assets en-ch6-2): the shipped frame was a foxed hand-bound antique volume with browned deckled leaves, which said *old book, old rule* directly under a foot reading `Wiley, August 2025` and inverted the beat's own point. It is now an open book hanging spine-up and seen edge-on — a bright white page block fanning down against a soft sage bokeh, with four neon plastic index flags (orange · cyan · yellow · magenta) marking pages. A book that has been gone through and marked up, which is what «he revised his own number upward» looks like, and an object that cannot exist in a 19th-century frame. §10's `no legible title, figure or agency name` is unchanged and still satisfied by the pose rather than by a crop: no title, no spine, no figure, no seal, no brand, and the only ink in frame is illegible handwriting on two of the flags. The frame is materially brighter than the one it replaces — re-measured on this build's own composed chain at attempt 2, 24.79 -> 31.43, rank 5 -> rank 7 of 13 — so the amber `4.7%` was RE-SAMPLED against the new ground rather than assumed (see the log; it is a real risk on a figure frame, since the whole point of the replacement is a white page block)." },

  { line: "6.4", arch: "c", f1: "#301519", art: "off", ctr: true, ken: "i", role: WARN,
    kick: "A THIRD ANSWER", stmt: "It did not hold up across most developed markets.",
    foot: "Pfau, \"An International Perspective on Safe Withdrawal Rates\",\nJournal of Financial Planning, December 2010 — 50-50 stocks and bills,\nzero tolerated failure. Japan's sustainable rate was 0.26%",
    img: "s72.jpg",
    note: "A THIRD ANSWER — and the one that is a WARNING rather than a candidate, which is why it is red where s70 and s71 are amber: Pfau's number is not an alternative rate to weigh, it is the finding that the rule does not travel. 49 chars => 76px on §3's ladder, the bottom step and never below it, over two measured lines. ⚠ `50/50 stocks and bills` RENDERS AS `50-50` — §3's build guard bans `/` in any on-screen string in this cut (`·` is the separator and the cut asks no rhetorical questions), the same replacement family as ch4's `$5,000 / MONTH` -> `A MONTH` and `payout DIVIDED BY price`. The fact is unchanged. Japan's 0.26% is kept in the foot because it is the single figure that makes `did not hold up` concrete, and it is Pfau's own. A folded world map with no country legible — no fabricated source document, and no country named on screen either." },

  { line: "6.5", arch: "d", f1: "#38151a", art: "off", ctr: true, ken: "o", role: WARN,
    verdict: true,
    kick: "WHY THE RATE IS ALWAYS SHOWN", stmt: "3.9% · 4.0% · 4.7%",
    img: "s73.jpg",
    note: "THE VERDICT, and the reason the whole video prints a rate beside every figure. One of the cut's five verdict scenes (§2): its stmt enters with `pop` (back.out(1.7)) instead of `rise`, and THAT is the slam — this cut has no `.stamp` component by design (§13 D10), because five rotated pills would be a tic. ⚠ THE `.stamp` CSS BUG THAT LANDED UPSTREAM TODAY CANNOT BITE HERE AND IS NOT PATCHED LOCALLY: a `.stamp` pill carrying the `.warn` modifier used to render red text on a red fill (`owed.stamp_warn_red_on_red_upstream`); the fix is now in `tools/scaffold/assets/blockframe.css` at (0,2,0) and this composition LINKS that file. A guard below throws if any `.stamp` appears in this chapter. MEASURED, though the cue is fixed: `three answers` runs clip 0.700-1.140 => scene +0.95 to +1.39, so the slam at +1.10 lands INSIDE the words it slams. The three figures are the three the chapter just showed, in the order it showed them, and the middle one is the 4.0% every rung in the video is divided by. ⚠ DECLARED BY fin-assets AND LEFT OPEN FOR fin-review: the photograph is an archery target with six arrows scattered from the gold out to the blue, and ch1's s5 is an archery target with ONE arrow in the gold. The rhyme is real and undeclared (§10 lists four returning objects; the target is not one) — and it says exactly what this chapter says, that chapter 1 promised one specific number and chapter 6 admits three answers. 68 scenes apart, legibly different with the sound off." },

  { line: "6.6", arch: "a", f1: "#0f2a1a", art: "off", ctr: true, ken: "i", role: FUND,
    kick: "THE LADDER", stmt: "All of it AT 4.0%.",
    img: "s74.jpg",
    note: "THE HAND-OFF into the recap — archetype A, which §7 reserves for opens and hand-offs, and the chapter's first green: the rate has just been argued about, and everything that follows is divided by ONE of the three. ⚠ `chapters._carry_forward_en_ch1_to_ch2_ch6` item 2 is the live one here: ch1's s8 already used the full-height ladder that §10 planned for this slot. fin-assets re-planned it rather than repeating the frame — s8 is a ladder running DIAGONALLY up an adobe pueblo wall against blue sky, s74 is a weathered ladder standing VERTICALLY against a flat orange stucco field with no sky and no building form — and then tested the literal reading by promoting a whole-height stepladder, which was rejected because dust sheets and a paint tray make the frame say `someone is redecorating`. STATED PLAINLY FOR fin-review: s74 does not show the whole ladder, against §10's `full height`; four ladder sheets returned no clean whole-ladder-against-a-plain-wall frame in either pool. A clean partial ladder inside the right scene beat a complete ladder inside the wrong one." },

  { line: "6.7", arch: "d", f1: "#12351f", art: "ladder13", ctr: false, ken: "o", role: FUND,
    hold: [1.16, 1.08], band: true, brule: 548,
    kick: "RUNGS ONE TO THREE", rate: "EACH AT A 4.0% WITHDRAWAL RATE",
    subs: ["Food · $254,225", "Car · $332,950", "Housing · $656,650"],
    subAt: [1.93, 3.79, 5.03], cascade: true,
    foot: "ILLUSTRATIVE ARITHMETIC",
    img: "s75.jpg",
    note: "RUNGS ONE TO THREE — the recap assembling, and the first half of the cut's third and last matched-frame hold. ⚠ s75.jpg IS DERIVED HERE: `ffmpeg crop=1280:720:20:250` out of s76.jpg (1880x1253), recorded in s75.jpg.src, manifest.json and CREDITS.txt. The pair is INVERTED against the other two holds — §6b makes s76 the SOURCE and s75 the tight crop — so the push runs OUT: plateKen 1.16->1.08 here, 1.08->1.00 on s76, one continuous pull-back across 15.419s, one ground shared, and no `transition` at the joint (cues-tables.json lists the pair under `holds`). Never a self-dissolve back to the same file (creator rule, firaun 2026-07-23). THE RECT IS A MEASURED CHOICE, not fin-assets' suggested +60+300 taken on trust: at y=352 the composed frame measures median 17.56 with a p90-p50 spread of 9.62 — the flattest frame in the chapter and the `dark and EMPTY` signature the floor rule actually predicts — and at y=250 the sky and the neighbouring house come in at median 18.37 with spread 18.60, while the tone step across the hold joint into s76 (19.92) falls from +2.36 to +1.55. A hold pair should not step, in temperature (§11 rule 1) or in tone. What the rect keeps: the low two-crate stack, the three-crate stack and the tall column, ascending left to right. What it holds back for the pull-back: the tall column's top and the two big stacks against the barn wall, which ARE rungs four and five. ⚠ THE PHOTOGRAPH DOES NOT CARRY THE COUNT and §14 item 4 said in advance that it would not have to — the file holds four stacks, not three, and THE DRAWN BARS CARRY THE COUNT, which is exactly why §8 marks both scenes art-forward. THE CASCADE IS SPEECH-ANCHORED, three separate rises at three MEASURED word onsets, never popEach at a fixed +1.10 (`owed.cascade_offsets_ignore_the_voice`): `a quarter of a million` starts at clip 1.680 => +1.93, `a third` at 3.540 => +3.79, `two thirds` at 4.780 => +5.03. Each line lands as its OWN figure is spoken, not as its category noun is — anchoring on `groceries` (clip 0.860 => +1.11) would have crowded the rate at +1.10 to a 0.01s gap. Gaps 0.83 / 1.86 / 1.24, all clear of the 0.80s floor without needing the cascade exemption." },

  { line: "6.8", arch: "d", f1: "#12351f", art: "ladder45", ctr: false, ken: "o", role: FUND,
    hold: [1.08, 1.00], band: true, brule: 548,
    kick: "RUNGS FOUR AND FIVE", rate: "BOTH AT A 4.0% WITHDRAWAL RATE",
    subs: ["$5,000 a month · $1,500,000", "$6,545 a month · $1,963,375"],
    subAt: [1.90, 4.75], cascade: true,
    foot: "ILLUSTRATIVE ARITHMETIC",
    img: "s76.jpg",
    note: "RUNGS FOUR AND FIVE — the pull-back, and the ladder completing. TWO `.sub` LINES, NOT ONE: §3's own exception table says so in as many words — `one line carrying four figures is not a focal` — and the script's `$5,000/mo $1,500,000 · $6,545/mo $1,963,375` also carries two solidi this cut does not print. The drawn layer continues ACROSS the dissolve: bars one to three are emitted at scale 1 with NO span call, exactly where s75 left them, so the mechanism holds still while the photograph pulls back and only rungs four and five arrive. Re-animating the first three would assert a second climb. THE HOLD HAND-OFF IS MEASURED, and it is the one offset on this chapter that could not be moved even if it were wrong: a hold joint IS a scene boundary and timing.json is its only home. The 0.45s cross-dissolve runs 43.661->44.111 with its MIDPOINT at 43.886, which is clip-local -0.025s of 6.8 — i.e. the picture changes 25ms before `Both at four percent`, the phrase that names rungs four and five, and inside the lead-in silence rather than across an earlier word. `chapters.hi.5.s57_swap_point_recut_2026-08-10` is the case this is checked against (that one would have completed 0.02s BEFORE its phrase and was re-cut); here the boundary is already on the phrase and nothing is re-timed. Anchors MEASURED: `5,000` at clip 1.240 => +1.49, floored to +1.90 so the rate at +1.10 keeps its 0.80s gap and still lands inside `five thousand a month` (clip 1.240-2.740 => +1.49 to +2.99); `the average household` at clip 4.500 => +4.75. This is the chapter's LONGEST-HELD frame at 8.323s, which matters to the floor rule: the floor is not this frame." },

  { line: "6.9", arch: "b", f1: "#38151a", art: "overrun", ctr: false, ken: "i", role: WARN,
    plate: "p-a", band: true, vrule: [196, 392],
    kick: "THE DIVIDENDS-ONLY PRICE", rate: "AT A 1.08% DIVIDEND YIELD",
    num: "$5,555,556", numTo: 5555556, numPrefix: "$", numAt: 5.59, numDur: 1.10,
    foot: "roughly four times the total-return figure\nILLUSTRATIVE ARITHMETIC",
    img: "s77.jpg",
    note: "THE CHAPTER'S PAYOFF FRAME — peak 2 paid a SECOND time (§9c), against a completed five-bar ladder the viewer has just watched assemble. ⚠ THE PLATE IS OVERRIDDEN TO `p-a` AND THAT IS LOAD-BEARING, not tidiness: `.p-b` maps viewBox x 1:1 to screen x on an 860px plate, so anything past vx=800 does not exist on the encode, and the overrun bar is 2,603px BY CONSTRUCTION. japanese-money-methods ch2 lost the entire point of a frame to exactly this with every check passing (gotcha 8). THE ARITHMETIC, at the point of edit: $5,555,556 / $1,963,375 = 2.8296, so the bar is the §9a track (920px) at scaleX 2.8296 = 2,603px from x=500 — 1,420px visible and the rest off-canvas BY DESIGN. It is the only element in the cut permitted to leave the frame, and leaving IS the assertion. Both figures in that ratio are on screen in this chapter with their rates ($1,963,375 on s76 at 4.0%, $5,555,556 here at 1.08%), so the bar asserts no quantity the video has not sourced — and there is no axis, no tick and no numeral in the drawing. Anchor MEASURED: `5` of `five point six million` at clip 5.340 => +5.59; §5's character-offset fallback said +6.08, i.e. 0.49s LATE — the same direction as all three of ch5's fallbacks. The countUp runs 1.10s rather than 1.20 so the figure is SETTLED 1.215s before the cross-dissolve starts (the 1.20s floor from fin-editor's hi-ch2 s18 finding); the anchor did not move to buy that, the duration did. ⚠ PAYOFF-LEGIBILITY CLAUSE, MEASURED AND DECLARED RATHER THAN CLAIMED — see the log; two of four limbs pass on this build's chain and the `background-position` sweep that would change the median rank cuts the container's own base out of frame, which is a framing cost paid for a rank. ⚠ RESOLVED ON THE ENCODE by review en-ch6-1: the ground measures 47.662, rank 7 of 13, ABOVE the chapter median and 8.79 above the floor, and the figure reads 4.86:1 against its own local background — the predicted rank did not reproduce, so neither the figure's geometry nor its timing was touched at attempt 2. What DID change is the five reference rungs, from ghosted `.fl` to solid `.flf` fund-green (finding 1) — the device's readability, not the figure's." },

  { line: "6.10", arch: "d", f1: "#1c2027", art: "off", ctr: true, ken: "o",
    kick: "WHAT THEY ALL ARE", stmt: "A division.\nOnly as good as its rate.",
    img: "s78.jpg",
    note: "WHAT THEY ALL ARE. NO role and no colour, deliberately: the line's content is that every figure in the video is the same arithmetic, and a role colour here would grade one of them. The chapter's one neutral ground, `#1c2027`, cooling out of the red payoff before the callback. THE FOCAL IS HARD-BROKEN AND THE BREAK IS A MEASUREMENT: unbroken at 88px it measures 1500.2px against the 1500px `.scene.centred .stack` cap — 0.2px over, i.e. a frame that re-wraps on a hair (ch4 rejected an 11px margin for the same reason and ch5 rejected 5.9px). Two sentences, two lines, 446.9px and 1032.5px. A pencil resting on a page of handwritten division, figures illegible — the arithmetic photographed rather than drawn, which is why §8 gives this scene no drawn layer even though it is the one line that NAMES the division." },

  { line: "6.11", arch: "a", f1: "#2d2214", art: "off", ctr: true, ken: "i",
    kick: "BACK TO THE DAY", stmt: "No alarm. No call. One buzz.",
    img: "s79.jpg", bgpos: "center top",
    note: "THE CALLBACK — study conclusion 11, and the peak-end beat the whole cold open was built to pay. It returns to chapter 1's images, NOT to the coffee-and-window version the format twins use, and §10 is explicit that it is a distinct fetch and not a reuse: the same nightstand and phone in late-afternoon light, the day over. NO ROLE COLOUR: the frame is a memory, not a claim. It also inherits ch1's approved treatment for a black-screen phone (§10's amended override — the screen is the DARKEST object, carries nothing, and states the beat more plainly than face-down); here the glass mirrors the window rather than showing anything, which is the same thing said in reflection. `bgpos: center top` is this build's one photograph knob and it is CONTENT-LED, with the measurement second: the source is 1713x1300-class against .bg's 1.778 box, so `cover` is width-limited and the only axis is 336 source rows of vertical slack — spending them upward drops dead foreground leather and brings in the warm window band, which IS the beat (*late-afternoon light, the day over*), and it moves the composed median 17.95 -> 19.35 with the phone still whole in frame at every point of the ken. §10 also declares this scene gets NO cut-in: the callback is one held image on purpose, and cutting back to ch1's own frames would be the reuse failure. MEASURED, though the cue is fixed at §5's +1.10: `no alarm` is spoken at clip 2.160 => scene +2.41, so the three clauses on screen lead the three clauses in the voice by 1.3s — variant A is a FIXED ladder and a statement that waits for its own words on a callback would read as a caption." },

  { line: "6.12", arch: "a", f1: "#12351f", art: "off", ctr: true, ken: "o", role: FUND,
    kick: "WHAT IT BUYS", stmt: "Not a lifestyle. The hours.",
    img: "s80.jpg",
    note: "WHAT THE NUMBER BUYS — green, because this is the one place in the chapter where a division that closed is spent rather than examined, and it is the video's answer to its own title. It deliberately refuses the thing the format's twins sell: the line says NOT a lifestyle, so the frame is an empty chair at a window and not a beach. §10 pairs it with s69 — the chapter's two `instrument or room` frames — and the plumb-bob override exists precisely so this is the chapter's ONLY chair. MEASURED, cue fixed at +1.10: `lifestyle` lands at clip 1.100-1.440 => +1.35, so the statement rises 0.25s ahead of the word it turns on." },

  { line: "6.13", arch: "a", f1: "#33200f", art: "off", ctr: true, ken: "i", role: POP,
    cta: "SUBSCRIBE",
    foot: "The next one prices the rungs nobody puts on a thumbnail.",
    img: "s81.jpg",
    note: "THE CUT'S ONE TERMINAL CTA — cue ladder D, the single `--pop` element in 81 scenes, at 98.6% of the video, with zero mid-roll CTA. §5's declared exception: 6.13 has no kicker (`head: —`), so the `.cta` block itself takes +0.40 and something authored is on screen inside `first_cue_by_seconds` 0.5 rather than only the photograph. The block is structurally immune to the role-class trap §1 warns about — it sets its own `background: var(--pop)` and dark ink — so it carries NO `popc` class, which would have painted orange text on an orange fill. The `<span class=\"tri\">` is blockframe's own CSS triangle, not a glyph: `▶` is banned by this cut's own build guard and would be tofu risk besides. ⚠ THE FOOT IS THE ONE STRING IN THIS CHAPTER NOT LIFTED FROM A `head:`/`stmt:`/`num:`/`foot:` FIELD, and it is declared rather than quietly invented: the script's `foot:` for 6.13 reads `The only CTA in the video, at 98.6%`, which is a production annotation about the frame and not copy for it. §5's ladder D declares a second cue at +1.20 on `s81-foot`, so the slot is real; what it carries is the REASON the line gives for subscribing, in the spoken line's own words (`the next one prices the rungs nobody puts on a thumbnail`). Nothing is promised that the VO does not say. MEASURED: `subscribe` is spoken at clip 1.860 => scene +2.11, so the block is on screen 1.71s before the word — which is the point of a terminal CTA rather than a slip. A closed hardback with its elastic band and a capped pen, on warm wood: fin-assets re-picked this after the first promotion shipped an OPEN, blank ruled notebook under `a closed notebook and a capped pen… finished`, which reads *start writing* on the last frame anyone looks at." },
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
/* The LAST chapter closes on the CUT's own root — timing.json's total, the one
 * home — not on a re-derived sum. Asserted, because this is the only chapter
 * where the two could disagree without any later scene to notice. */
if (Math.abs(TIMING.total - (OFF + ROOT)) > 0.002)
  throw new Error(`chapter root ${ROOT} + offset ${OFF} != timing.json total ${TIMING.total}`);

const sc = SCENES.map((s, i) => {
  const r = rows[i];
  if (r.id !== s.line) throw new Error(`spec/timing mismatch at ${i}`);
  const own = r.scene_duration;
  const n = FIRST + i;
  return {
    ...s, i, n, id: "s" + n,
    start: +(r.scene_start - OFF).toFixed(3),
    dur: own,                                                 // the scene's own hold
    dd: i < SCENES.length - 1 ? +(own + T).toFixed(3) : own,  // + the cross-dissolve overlap
    track: n % 2 ? 1 : 2,                                     // or overlapping_clips_same_track
    astart: +(r.audio_start - OFF).toFixed(3),
    adur: r.duration,
    // No scene in ch6 swaps its photograph — the s75/s76 hold is two SCENES, not
    // two framings of one — so each is a single value equal to the scene's own
    // hold. Emitting it anyway removes any question about whether an absent
    // attribute means "one framing" or "not declared" (§6c).
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
    if (f > FMT.scene.max_scene_seconds) throw new Error(`${s.id} holds one photo for ${f}s`);
  });
});

/* THE HOLD, asserted rather than trusted. A hold pair must be ONE continuous
 * move: the second scene's plateKen has to start at exactly the value the first
 * ended on, and both must share one ground, or the "cut that is not happening"
 * becomes visible. ⚠ THIS PAIR RUNS OUT (§5), so the endpoints DESCEND — the
 * assert is on continuity, never on direction, which is what lets the same line
 * cover ch4's ascending hold and this one. */
sc.forEach((s, i) => {
  if (!s.hold || i === 0 || !sc[i - 1].hold) return;
  const p = sc[i - 1];
  if (Math.abs(p.hold[1] - s.hold[0]) > 1e-9)
    throw new Error(`${p.id}->${s.id} hold is not continuous: ${p.hold[1]} then ${s.hold[0]}`);
  if (p.f1 !== s.f1)
    throw new Error(`${p.id}->${s.id} is a hold with two grounds (§11 rule 1)`);
  if (p.img === s.img)
    throw new Error(`${p.id}->${s.id} points at ONE file — a self-dissolve flickers`);
});

/* §3's build guard: no `/` and no `?` in any on-screen string. Both ARE in the
 * dumped 97-codepoint subset — the storyboard bans them as COPY. It also sweeps
 * the ₹ this cut is forbidden to show and any Devanagari that could arrive from
 * the sibling cut. Every character is checked against the FACE's own coverage,
 * because pipeline_check's uncovered_glyphs() is inert on a chapter project (it
 * keys off the literal string "FinanceSans" appearing in the composition, and
 * the face is named only in the LINKED blockframe.css). */
const SUBSET = new Set(
  " !\"#$%&'()*+,-./0123456789:;=?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]_" +
  "abcdefghijklmnopqrstuvwxyz|£·–—‘’“”€₹");
const strings = (s) =>
  [s.kick, s.stmt, s.num, s.rate, s.foot, s.cta, ...(s.subs || [])]
    .filter(Boolean).map(flat);
sc.forEach((s) => {
  strings(s).forEach((t) => {
    const bad = t.match(/[/?₹×≈~→▶¢]/);
    if (bad) throw new Error(`${s.id}: on-screen string carries "${bad[0]}" — banned in this cut`);
    if (/[ऀ-ॿ]/.test(t)) throw new Error(`${s.id}: Devanagari in the -en cut`);
    for (const ch of t)
      if (!SUBSET.has(ch)) throw new Error(`${s.id}: "${ch}" is not in the font subset — tofu`);
  });
  if (s.stmt && s.num) throw new Error(`${s.id}: never a stmt AND a num (§3)`);
  if (s.size && s.size < 76) throw new Error(`${s.id}: focal below the ladder floor`);
  if (s.subs && s.subAt.length !== s.subs.length)
    throw new Error(`${s.id}: ${s.subs.length} sub lines but ${s.subAt.length} measured onsets`);
  if (s.subs) s.subAt.forEach((t, k) => {
    if (k && t <= s.subAt[k - 1]) throw new Error(`${s.id}: sub onsets are not monotonic`);
    if (t + 0.7 > s.dur) throw new Error(`${s.id}: sub ${k + 1} finishes past the scene`);
  });
  /* the drawn layer never becomes the whole scene, and a centred scene has no
   * plate to put one in (.scene.centred .plate is display:none). */
  if (s.art !== "off" && s.ctr) throw new Error(`${s.id}: drawn art on a centred scene`);
  if (s.art !== "off" && !s.img) throw new Error(`${s.id}: art without a photograph`);
  if (s.art !== "off" && !s.band) throw new Error(`${s.id}: drawn art with no .band under it (rule 9)`);
  if (!s.img) throw new Error(`${s.id}: no photograph — photo_free_scene_ratio is 0`);
  /* §9a: the corpus measure bar appears on SIX frames in the cut and none is in
   * this chapter. The recap draws its own bars at the same scale instead, and a
   * second component drawing the same proportion in the same frame would be two
   * denominators for one numerator. */
  if (s.meas || s.mlab) throw new Error(`${s.id}: the §9a measure bar belongs to s21/s27/s31/s41/s42/s67`);
  /* the cut has no `.stamp` component (§13 D10). Belt and braces after
   * `owed.stamp_warn_red_on_red_upstream`: the fix is upstream, and this chapter
   * must not reintroduce the class it fires on. */
  /* (the .stamp guard runs on the EMITTED markup, below — a spec-side string
   * check would also fire on a note that MENTIONS the class, which is the
   * comments-are-stripped-first lesson from ch4's tank guard.) */
  /* §4: the nine rate-as-focal frames carry NO separate #sN-rate. s70 and s71
   * are two of them; printing a rate under itself reads as a defect. */
  if (s.rate && s.num && /^[\d.]+%$/.test(s.num))
    throw new Error(`${s.id}: a rate focal must not also carry a #${s.id}-rate`);
});

/* --------------------------------------------------------------- INVARIANT
 * `separation_not_rank_2026-08-09` §1 as amended by
 * `outlier_limb_is_subordinate_to_the_invariant_2026-08-10`. Live text, one
 * direction only: **a substantive beat must not be left in the chapter's darkest
 * frame.** The converse is RETIRED and "satisfied by construction" is not an
 * available answer — it quotes a sentence that no longer exists and it has
 * already been spent twice on this run in good faith.
 *
 * MEASURED on this build's own composed chain (cover-fit into .bg's inset:-8%
 * box -> ken 1.08 -> the locked grade -> .field at .38 carrying --f1 -> the four
 * .scrim layers including the per-scene --tint -> BT.601), 13 of 13 scenes:
 *
 *   s75 18.37 · s79 19.35 · s76 19.92 · s80 24.29 · s74 26.40 · s81 28.20 ·
 *   s71 31.43 · s72 33.77 · s77 34.96 · s70 36.17 · s73 36.21 · s78 40.85 ·
 *   s69 43.19
 *
 * s71 IS THE ONE NUMBER RE-MEASURED AT ATTEMPT 2, because it is the one
 * photograph that was replaced (review en-ch6-1 finding 2). 24.79 -> 31.43, rank
 * 5 -> rank 7 of 13, on the same chain: the instrument was re-implemented and
 * validated first against four scenes whose files are byte-unchanged (s70 +0.29,
 * s78 -0.09, s77 +0.34, s69 +0.16), so the new value is on the same scale as the
 * twelve it sits beside rather than on a second instrument. Nothing else in this
 * table moved and nothing else was re-measured — those twelve files are byte
 * identical. The direction is the safe one: s71 moves AWAY from the floor, so
 * the floor, its separation, the payoff and the CTA are all untouched by it.
 *
 * THE BOTTOM IS A CHAINED CLUSTER, NOT A STRANDED OUTLIER: the two adjacent gaps
 * at the bottom are 0.98 (s75->s79) and 0.57 (s79->s76), BOTH inside the 1.0
 * luma-point tie band, so no single frame is "the chapter's darkest" in any sense
 * the rule recognises — the same shape as the hi ch4 worked example (a four-way
 * tie spanning 1.08, ruled NOT a defect) and the opposite of en ch4's s44 and en
 * ch5's s54, which were alone at the bottom by 5.84 and 7.66.
 *
 * WHY THE BEAT THAT SITS THERE IS ACCEPTABLE, argued on CONTENT and open to
 * disagreement — s75/s76 are the recap, which is substantive, so this is not
 * waved through:
 *  (i) §10 ROUTES IT THERE ON PURPOSE. "The densest scenes get the calmest
 *      backgrounds. The seven art-forward frames and the five chip cascades are
 *      all routed to near-flat, low-key subjects. Density is managed by choosing
 *      a quieter image, NEVER by dropping one." Two of this chapter's three
 *      art-forward frames are s75 and s76. A dark, calm crate wall under a drawn
 *      measure ladder is the storyboard's own instruction, not drift.
 * (ii) THE BEAT IS NOT CARRIED BY THE PHOTOGRAPH'S TONE. Both frames state their
 *      figures in 40px `.sub` type over the scrim and in solid drawn bars at 52%
 *      over their own `.band` — a lift that exists BECAUSE rule 9 forbids
 *      darkening the photograph. Neither is a frame you read by reading the
 *      picture.
 *(iii) THE TWO BEATS THE BRIEF PROTECTS ARE NOWHERE NEAR THE BOTTOM: the payoff
 *      s77 is 34.96 (rank 9 of 13, 16.6 points clear of the floor) and the CTA
 *      s81 is 28.20 (rank 7 of 13).
 * (iv) THE ONE LEVER THIS STAGE OWNS WAS SPENT, NOT ARGUED AWAY. s75's file is
 *      derived HERE, so its crop rect is a build decision: the sweep moved it
 *      17.43 -> 22.16 across nine rects and the rect chosen (+0.81 median, +8.98
 *      spread) is the brightest one that still keeps the crates standing on the
 *      ground and still holds back the reveal. Everything above it cuts the
 *      crate bases out of frame, which is buying a rank with a framing.
 *
 * A fix that would move a MORE substantive beat to the bottom is FORBIDDEN, and
 * that is the other reason nothing further was spent: the next frames up are s79
 * (the callback) and s76 (the second half of the same recap).
 *
 * What the assert BUYS is that a later edit cannot quietly break the premise:
 * the floor must stay off the payoff, off the CTA and off the longest-held
 * frame, and the art-forward set must stay exactly the three §8 declares. */
const FLOOR = "s75", PAYOFF = "s77", CTA = "s81";
const TONE = { s75: 18.37, s79: 19.35, s76: 19.92, s80: 24.29, s74: 26.40, s81: 28.20,
               s71: 31.43, s72: 33.77, s77: 34.96, s70: 36.17, s73: 36.21, s78: 40.85,
               s69: 43.19 };
{
  const ranked = Object.entries(TONE).sort((a, b) => a[1] - b[1]);
  if (ranked[0][0] !== FLOOR) throw new Error(`INVARIANT: the measured floor is ${ranked[0][0]}, not ${FLOOR}`);
  if (FLOOR === PAYOFF) throw new Error("INVARIANT: the floor is the payoff frame");
  if (FLOOR === CTA) throw new Error("INVARIANT: the floor is the CTA — the last frame anyone looks at");
  const longest = sc.reduce((a, b) => (b.dur > a.dur ? b : a));
  if (longest.id === FLOOR) throw new Error("INVARIANT: the floor is the chapter's longest-held frame");
  if (Object.keys(TONE).length !== sc.length) throw new Error("INVARIANT: the tone run is not the chapter");
  /* the outlier limb: it fires only when the bottom frame is ALONE down there. */
  const sep = +(ranked[1][1] - ranked[0][1]).toFixed(2);
  if (sep > 1.0)
    throw new Error(`INVARIANT: ${FLOOR} is now alone at the bottom by ${sep} points — the outlier ` +
      `limb fires and the discharge above (a chained cluster inside the tie band) no longer holds. Re-argue it.`);
  const art = sc.filter((s) => s.art !== "off").map((s) => s.id).join(",");
  if (art !== "s75,s76,s77")
    throw new Error(`§8 declares three drawn layers here — s75, s76, s77 — and this build emits ${art}`);
}

/* ---------------------------------------------------------- the drawn layers
 * THREE, in a thirteen-scene chapter. The archetype note calls "three or four in
 * a twelve-to-fourteen scene chapter" the TOP of the range and not the target,
 * and §8 budgets ch6 exactly three; the other ten scenes are art-off and nine of
 * those are centred, because rule 8 retires a drawn layer wherever the
 * photograph already carries the beat.
 *
 * WHAT WAS DECLINED, so the choice is on the record rather than implied:
 *   · 6.5's three price stickers — the photograph IS three marks on one target
 *     and drawing three sizes over it is the ghost-envelope failure by name.
 *   · 6.10's division — the frame is a page of handwritten division. Depictive.
 *   · 6.12's hours — a drawn clock over "the hours" is decoration, and anything
 *     quantifying hours would be a figure the video never sourced.
 *   · a sixth bar for a "what if the rate were X" — that is a forecast, which is
 *     the shape `no_return_promise` forbids outright.
 *
 * THE §9a SCALE IS THE ONE SCALE, and this is where it is spent for the last
 * time: 920px = $1,963,375 (rung five, the whole BLS household at 4.0%), so
 * 1px = $2,134.10. Every width below is computed from that constant and from the
 * corpus figure the scene PRINTS, and the assert throws if either half is edited
 * alone (gotcha 7). The bars are the same arithmetic as the six measure-bar
 * frames of chapters 2-5, which is what makes the recap a recap. */
const LADDER_TOP = 1963375;
const TRACK = 920, LX = 500;
const RUNGS = [                                        // §9a, in ladder order
  { id: "r1", corpus: 254225,   from: "s75" },         // groceries
  { id: "r2", corpus: 332950,   from: "s75" },         // the car
  { id: "r3", corpus: 656650,   from: "s75" },         // housing
  { id: "r4", corpus: 1500000,  from: "s76" },         // $5,000 a month
  { id: "r5", corpus: 1963375,  from: "s76" },         // the whole household
];
const px = (corpus) => +(corpus / LADDER_TOP * TRACK).toFixed(2);
RUNGS.forEach((r) => { r.px = px(r.corpus); });
if (RUNGS[4].px !== TRACK) throw new Error("ladder: rung five IS the track — 920px = $1,963,375");
/* Every printed figure must be the one its bar draws, and every bar must be the
 * one its printed figure implies. Checked BOTH ways against the spec's strings. */
{
  const printed = sc.flatMap((s) => (s.subs || []).map((t) => [s.id, t]));
  RUNGS.forEach((r) => {
    const want = "$" + r.corpus.toLocaleString("en-US");
    const hit = printed.find(([sid, t]) => sid === r.from && t.includes(want));
    if (!hit) throw new Error(`ladder: ${r.id} draws ${want} and ${r.from} does not print it`);
  });
}
const OVERRUN_CORPUS = 5555556;
const OVERRUN = +(OVERRUN_CORPUS / LADDER_TOP).toFixed(4);   // 2.8296
if (Math.abs(OVERRUN * TRACK - 2603.2) > 1.0)
  throw new Error("ladder-overrun: 5,555,556 / 1,963,375 x 920 must be ~2,603px");
if (!sc.find((s) => s.id === "s77").num.includes(OVERRUN_CORPUS.toLocaleString("en-US")))
  throw new Error("ladder-overrun: s77 must PRINT the figure its bar is a ratio of");

/* Geometry, in the PLATE's own coordinate space and never in 1920x1080.
 *   p-d = `0 0 1920 656` mapping 1:1 to screen x, y+424.
 * Placement arithmetic for the two recap scenes: rows at plate y 140..464 =>
 * screen 564..888. Below the `.band`'s own top edge (54% of 1080 from the bottom
 * = y497), so every drawn thing sits on darkened ground; above the 970px bottom
 * safe line; x 500..1420, so the track is centred on the frame (500 + 920/2 =
 * 960) and clear of the watermark box (#root::after is right:64 bottom:40, 84x84
 * => x1772-1856, y956-1040), which no scene may paint into. */
const ROW = { y0: 160, h: 44, gap: 26 };
const rowY = (k) => ROW.y0 + k * (ROW.h + ROW.gap);

function ladder(id, shown, animate) {
  /* Solid fills only, nothing thinner than 44px: `.has-photo.art-forward .art`
   * is 52% and a thin outline at 0.4 alpha survives no encode. The ghost row IS
   * the denominator — a filled rect at .2, never an outline — and a proportion
   * without its denominator on screen is not a proportion.
   * ⚠ The per-scene `opacity` on the <svg> is a NO-OP (`.has-photo .art` and
   * `.has-photo.art-forward .art` both carry !important), so fade() cannot bring
   * this layer in and none is called on it. The only levers that reach the screen
   * are the weight and alpha of the elements INSIDE it, which is why every bar
   * arrives by TRANSFORM. */
  const L = [`<svg class="art v-ladder" id="${id}-art" viewBox="0 0 1920 656" preserveAspectRatio="xMidYMid slice">`];
  RUNGS.slice(0, shown).forEach((r, k) => {
    const y = rowY(k);
    const held = !animate.includes(r.id);
    L.push(`      <!-- rung ${k + 1}: $${r.corpus.toLocaleString("en-US")} / $${LADDER_TOP.toLocaleString("en-US")}`
      + ` x ${TRACK} = ${r.px}px${held ? "  (HELD from the previous scene — no span call)" : ""} -->`);
    L.push(`      <rect class="fl" id="${id}-${r.id}t" x="${LX}" y="${y}" width="${TRACK}" height="${ROW.h}" fill-opacity=".2"/>`);
    L.push(`      <rect class="flf" id="${id}-${r.id}" x="${LX}" y="${y}" width="${r.px}" height="${ROW.h}"`
      + ` style="transform-origin:0% 50%"/>`);
  });
  L.push("    </svg>");
  return L.join("\n");
}

/* THE OVERRUN — p-a, viewBox `0 0 1920 1080`, 1:1 with the screen. The completed
 * five-bar ladder is drawn in the SAME `.flf` fund-green as s75/s76 (the recap
 * the viewer has just watched assemble) and ONE new `.flw` bar leaves the frame.
 * Rows at y560..840, the overrun at y880..944 — above the 970 safe line and
 * above the watermark's y956.
 *
 * ⚠ ATTEMPT 1 SHIPPED THESE FIVE AS `.fl` AT fill-opacity .2 AND THAT WAS THE
 * CHAPTER'S BLOCKER (review en-ch6-1 finding 1). `.has-photo.art-forward .art`
 * is opacity .52, so .2 of --ink is ~0.10 effective alpha: measured on the
 * encode at deltaRGB 6-10 against the gap above each bar (1.07-1.09:1) against
 * the overrun bar's own deltaRGB ~40. The reference was not on screen, so the
 * video's payoff frame showed one red band with nothing to compare it to and
 * the layer asserted no proportion at all (rule 8). Solid green also carries
 * the sentence — five sourced rungs, one that does not fit.
 *
 * WHAT WAS DELIBERATELY *NOT* ADDED WITH THEM: no 920px ghost track behind the
 * rungs, no tick, no axis, no numeral. `no_return_promise` binds hardest
 * exactly here, and a visible reference must not become a measured SCALE — the
 * rungs are five figures this video has already sourced and printed with their
 * rates, the overrun is the comparison the VO makes, and nothing on the frame
 * may imply a projection. The denominator is on screen as rung 5 itself, which
 * IS the full 920px track. */
const OV = { y0: 560, h: 40, gap: 20, by: 880, bh: 64 };
function overrun(id) {
  const L = [`<svg class="art v-overrun" id="${id}-art" viewBox="0 0 1920 1080" preserveAspectRatio="xMidYMid slice">`,
    `      <!-- the completed ladder, in the same .flf fund-green it carried on s75/s76:`,
    `           the five figures this video has already put on screen, each with its`,
    `           rate, and the reference the overrun is measured against. No ghost track,`,
    `           no tick, no axis, no numeral — a reference, never a scale. Nothing here`,
    `           is new and nothing is a forecast: the widths are the same §9a arithmetic`,
    `           as chapters 2-5, over the same ${TRACK}px track. -->`];
  RUNGS.forEach((r, k) => {
    L.push(`      <rect class="flf" id="${id}-${r.id}" x="${LX}" y="${OV.y0 + k * (OV.h + OV.gap)}"`
      + ` width="${r.px}" height="${OV.h}"/>`);
  });
  L.push(`      <!-- and the one that does not fit: $${OVERRUN_CORPUS.toLocaleString("en-US")} / $${LADDER_TOP.toLocaleString("en-US")}`);
  L.push(`           = ${OVERRUN}, i.e. the 920px track at scaleX ${OVERRUN} = ${Math.round(OVERRUN * TRACK)}px from x=${LX}.`);
  L.push(`           ${1920 - LX}px of it are on screen and the rest is off-canvas BY DESIGN —`);
  L.push(`           leaving the frame IS the assertion, and it is the only element in`);
  L.push(`           the cut permitted to do it. -->`);
  L.push(`      <rect class="flw" id="${id}-over" x="${LX}" y="${OV.by}" width="${TRACK}" height="${OV.bh}"`
    + ` style="transform-origin:0% 50%"/>`);
  L.push("    </svg>");
  return L.join("\n");
}

/* The four absences, asserted on the emitted MARKUP rather than promised in
 * prose. ⚠ COMMENTS ARE STRIPPED FIRST — written naively this fires on the
 * drawing's own comment explaining the rule, i.e. it punishes the note and is
 * silenced by deleting it. Same shape as the Lottie guard that fired on the CSS
 * comment describing the trap it prevents (tool_fixes_this_run, 2026-08-08). */
{
  const lad = ladder("sX", 5, []).replace(/<!--[\s\S]*?-->/g, "");
  const ovr = overrun("sY").replace(/<!--[\s\S]*?-->/g, "");
  const svg = lad + ovr;
  for (const [what, re] of [["a numeral", /<text/], ["a tick or an axis", /tick|axis|scale=/i],
                            ["a projection", /forecast|project|estimate/i]])
    if (re.test(svg)) throw new Error(`ladder: the bars must carry no ${what} — they are a recap, not a chart`);
  if (!/fill-opacity="\.2"/.test(lad)) throw new Error("ladder: the denominator ghost is missing");
  /* The regression this chapter actually shipped, asserted on the markup: the
   * overrun's five REFERENCE rungs must be solid `.flf`, one per RUNG, and none
   * of them may carry a fill-opacity ever again — at .2 under `.art-forward`'s
   * .52 they measured deltaRGB 6-10 on the encode and the payoff frame compared
   * its bar to nothing. The inverse guard is the second half: the overrun may
   * NOT grow a ghost track, because a full-width rule behind five bars reads as
   * an axis and `no_return_promise` binds this layer. So: exactly RUNGS.length
   * `.flf` rects, exactly one `.flw`, and no fill-opacity anywhere. */
  if ((ovr.match(/class="flf"/g) || []).length !== RUNGS.length || /fill-opacity/.test(ovr))
    throw new Error("overrun: the five reference rungs must be solid .flf and carry no fill-opacity");
  if ((ovr.match(/class="flw"/g) || []).length !== 1 || (ovr.match(/<rect/g) || []).length !== RUNGS.length + 1)
    throw new Error("overrun: exactly five reference rungs and one overrun bar — no track, no axis");
}

/* ------------------------------------------------------------------ markup */
const esc = (t) => t.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
const brk = (t) => esc(t).replace(/\n/g, "<br>");
const PLATE = { a: "p-a", b: "p-b", c: "p-c", d: "p-d" };
const ART = { ladder13: (id) => ladder(id, 3, ["r1", "r2", "r3"]),
              ladder45: (id) => ladder(id, 5, ["r4", "r5"]),
              overrun };

function scene(s) {
  const cls = ["scene", "clip", "arch-" + s.arch, "has-photo"];
  if (s.art === "off") cls.push("art-off"); else cls.push("art-forward");
  if (s.ctr) cls.push("centred");
  if (s.lift) cls.push("art-lift");
  const alpha = s.role === FUND ? ".10" : s.role === POP ? ".13" : ".12";
  const style = s.role ? ` style="--tint:rgba(${s.role},${alpha})"` : "";
  const glow = s.role ? ` style="--gl:rgba(${s.role},.16)"` : "";
  const roleName = { [FUND]: "--fund", [TARGET]: "--target", [WARN]: "--warn", [POP]: "--pop" }[s.role] || "";
  const rc = { [FUND]: " fundc", [TARGET]: " targetc", [WARN]: " warnc" }[s.role] || "";
  const L = [];
  L.push(`\n<!-- ${s.line} · ${s.arch.toUpperCase()} · ${s.f1} · art ${s.art}` +
    `${s.ctr ? " · centred" : ""}${roleName ? " · " + roleName : ""}\n     ${s.note} -->`);
  L.push(`<section class="${cls.join(" ")}" id="${s.id}" data-track-index="${s.track}"` +
    ` data-start="${s.start}" data-duration="${s.dd}" data-framings="${s.framings.join(",")}"${style}>`);
  L.push(`  <div class="bg" id="${s.id}-bg" style="background-image:url(assets-ch6/final/${s.img})` +
    `${s.bgpos ? `;background-position:${s.bgpos}` : ""}"></div>`);
  L.push(`  <div class="field" style="--f1:${s.f1}"><div class="rules"></div><div class="glow"${glow}></div></div>`);
  if (s.band)
    // z-index 0 inline and BEFORE the plate in DOM order, so it paints UNDER the
    // drawn layer. `.band`'s own z-index is 1, which would put it OVER a z-0
    // plate and darken the very thing it exists to make readable. Rule 9: it
    // darkens BEHIND the art and never touches the photograph outside it.
    L.push(`  <div class="band" id="${s.id}-band" style="z-index:0"></div>`);
  if (s.art !== "off") {
    L.push(`  <div class="plate ${s.plate || PLATE[s.arch]}" id="${s.id}-plate">`);
    L.push(`    <div class="plate-in" id="${s.id}-pin"><div class="hatch"></div>`);
    L.push(`      ${ART[s.art](s.id)}`);
    L.push(`    </div>`);
    L.push(`  </div>`);
  }
  L.push(`  <div class="scrim"></div>`);
  if (s.brule) L.push(`  <div class="brule" id="${s.id}-br" style="top:${s.brule}px"></div>`);
  if (s.vrule) L.push(`  <div class="vrule" id="${s.id}-vr" style="top:${s.vrule[0]}px;height:${s.vrule[1]}px"></div>`);
  L.push(`  <div class="stack" id="${s.id}-stack">`);
  if (s.kick) L.push(`    <p class="kicker" id="${s.id}-kick">${esc(s.kick)}</p>`);
  if (s.rate) L.push(`    <p class="sub${rc}" id="${s.id}-rate">${esc(s.rate)}</p>`);
  if (s.num) L.push(`    <p class="huge${rc}" id="${s.id}-num">${esc(s.num)}</p>`);
  if (s.stmt) L.push(`    <p class="huge${rc}" id="${s.id}-stmt" style="font-size:${s.size}px">${brk(s.stmt)}</p>`);
  // The recap's figures are `.sub` LINES, not chips: §3 says a chip crushes a
  // figure-plus-its-rate, and these are five figures that each carry one.
  if (s.subs) s.subs.forEach((t, k) =>
    L.push(`    <p class="sub${rc}" id="${s.id}-l${k + 1}">${esc(t)}</p>`));
  if (s.cta)
    // NO role class: `.cta` sets its own background var(--pop) and #0d1017 ink,
    // so `popc` here would paint orange on orange — §1's own trap, and this is
    // the one element in the cut structurally immune to it.
    L.push(`    <div class="cta" id="${s.id}-cta"><span class="tri"></span>${esc(s.cta)}</div>`);
  if (s.foot) L.push(`    <p class="foot" id="${s.id}-foot">${brk(s.foot)}</p>`);
  L.push(`  </div>`);
  L.push(`  <div class="grain"></div>`);
  L.push(`</section>`);
  return L.join("\n");
}

const audio = sc.map((s) =>
  `<audio id="vo-${CH}-${s.i + 1}" class="clip" data-track-index="10" ` +
  `data-start="${s.astart}" data-duration="${s.adur}" src="assets/voice/${s.line}.mp3"></audio>`
).join("\n");

const map = (f) => "{ " + sc.map((s) => `${s.id}: ${f(s)}`).join(", ") + " }";

/* THE PHOTOGRAPH CARRIES THE MOTION — one move per scene, never a plate push
 * competing with a ken. The hold pair takes plateKen with EXPLICIT chained
 * endpoints on its `.bg`; every other scene takes ken's fixed 1.00<->1.16. */
const kenJs = sc.map((s) => s.hold
  ? `plateKen("#${s.id}-bg", S.${s.id}, D.${s.id}, ${s.hold[0].toFixed(2)}, ${s.hold[1].toFixed(2)});`
  : `ken("#${s.id}-bg", S.${s.id}, D.${s.id}, ${s.ken === "i"});`).join("\n");

/* ------------------------------------------------------- the per-scene cues
 * Built as DATA first so the same list can be emitted, gap-swept and
 * settle-checked. ch5's F1 finding is why: a cascade foot defaulted to variant
 * A's +1.90 and landed 0.60s before the next event, under cue_min_gap_seconds,
 * and `hyperframes check` passes that happily — the crowding lives in the MOTION
 * list and cues.py only validates the SOUND list. */
const cues = [];
const cue = (s, at, js, kind) => { cues.push({ sid: s.id, at: +at.toFixed(2), js, kind }); };

sc.forEach((s) => {
  if (s.kick) cue(s, 0.30, `rise("#${s.id}-kick", S.${s.id} + 0.30, 0.7, 14);`, "kick");
  if (s.band) cue(s, 0.55, `fade("#${s.id}-band", S.${s.id} + 0.55, 0.50);`, "band");
  /* ⚠ LADDER D'S TWO CUES ARE SWAPPED ON s81, AND IT IS A REAL FINDING RATHER
   * THAN A PREFERENCE. §5 declares `s81-cta` at +0.40 and `s81-foot` at +1.20.
   * At +0.40 the cut's ONE `cta` sound lands 0.40s after s81's own joint
   * `transition` — under `cue_min_gap_seconds` (0.8) — and tools/audio/cues.py
   * FAILS the chapter on it. cues.py already knows this shape: its `reveal` rung
   * is documented as "never the kicker at +0.30, which collides with its own
   * joint transition", and the `cta` rung simply has no equivalent guard because
   * no chapter before this one carried a CTA. Both floors are kept by inverting
   * the two cues INSIDE the same ladder: the foot takes +0.40, so something
   * authored is on screen inside `first_cue_by_seconds` (0.5) and it is not only
   * the photograph, and the block pops at +1.20 — 0.80s later exactly, 1.20s
   * clear of the joint. It also lands the block 0.91s before the spoken word
   * "subscribe" (clip 1.860 => +2.11) instead of 1.71s before it. */
  if (s.cta) cue(s, 1.20, `pop("#${s.id}-cta", S.${s.id} + 1.20, 0.6);`, "cta");
  if (s.rate) cue(s, 1.10, `rise("#${s.id}-rate", S.${s.id} + 1.10, 0.7, 18);`, "rate");
  if (s.stmt) cue(s, 1.10, s.verdict
    ? `pop("#${s.id}-stmt", S.${s.id} + 1.10, 0.6);`
    : `rise("#${s.id}-stmt", S.${s.id} + 1.10, 0.7, 18);`, "stmt");
  // variant B cue 2: the rate, else the sub, else the foot — at +1.10, so the
  // assumption is on screen BEFORE the figure arrives into it (§4).
  if (s.num && !s.rate) cue(s, 1.10, `rise("#${s.id}-foot", S.${s.id} + 1.10, 0.7, 18);`, "foot");
  if (s.subs) s.subs.forEach((_t, k) => {
    const at = s.subAt[k];
    cue(s, at, `rise("#${s.id}-l${k + 1}", S.${s.id} + ${at.toFixed(2)}, 0.6, 16);`, "cascade");
    const r = RUNGS.filter((x) => x.from === s.id)[k];
    if (r) cue(s, at, `span("#${s.id}-${r.id}", S.${s.id} + ${at.toFixed(2)}, 0.55, 0, 1);`, "cascade");
  });
  if (s.num) {
    cue(s, s.numAt, `pop("#${s.id}-num", S.${s.id} + ${s.numAt.toFixed(2)}, 0.6);`, "num");
    if (s.numTo != null)
      cue(s, s.numAt, `countUp("#${s.id}-num", S.${s.id} + ${s.numAt.toFixed(2)}, 0, ${s.numTo}, ` +
        `"en-US", ${s.numDur.toFixed(2)}, ${JSON.stringify(s.numPrefix || "")}, "");`, "num");
    if (s.art === "overrun")
      cue(s, s.numAt, `span("#${s.id}-over", S.${s.id} + ${s.numAt.toFixed(2)}, ` +
        `${s.numDur.toFixed(2)}, 0, ${OVERRUN});`, "num");
  }
  // the foot: variant A puts it at +1.90 on a statement scene, variant B at
  // num + 0.80, ladder C at last cascade item + 0.80, ladder D at +1.20.
  if (s.foot && s.rate === undefined && s.num && !s.subs) { /* took cue 2 above */ }
  else if (s.foot) {
    const at = s.cta ? 0.40                       // see the swap note above
      : s.subs ? s.subAt[s.subAt.length - 1] + 0.80
      : s.num ? s.numAt + 0.80
      : 1.90;
    cue(s, at, `fade("#${s.id}-foot", S.${s.id} + ${at.toFixed(2)}, 0.5);`, "foot");
  }
});

/* THE MOTION-LIST GAP SWEEP and the SETTLED-FIGURE FLOOR, both mechanised.
 * cue_min_gap_seconds is 0.8 and a DECLARED cascade is its one exemption
 * (format.json layout.cascade). The settle floor is fin-editor's hi-ch2 s18
 * finding: a figure still rolling when the cross-dissolve starts has not been
 * READ, so num + countUp must finish at least 1.20s before the scene's own
 * hold ends. On this chapter it binds on s77 and the DURATION moved, never the
 * spoken anchor. */
const GAP = FMT.layout.cue_min_gap_seconds, SETTLE = 1.20;
sc.forEach((s) => {
  /* The `.band` is excluded from the gap sweep and that is a decision, not an
   * oversight: cue_min_gap_seconds is about two authored ELEMENTS crowding each
   * other, and §3's own element budget puts `.field`, `.scrim` and `.grain`
   * outside the count as grade layers. The band is the plate-scoped member of
   * that family — rule 9's "darken BEHIND the art" — so it lifts 0.25s after the
   * kicker without being a second thing to read. It is still a real motion call,
   * so cues.py may bind a `reveal` to it; on the three scenes that have one, two
   * are on the cut's dry list and the third (s77) outranks it with `hero`. */
  const mine = cues.filter((c) => c.sid === s.id && c.kind !== "band");
  const at = [...new Set(mine.map((c) => c.at))].sort((a, b) => a - b);
  at.forEach((t, k) => {
    if (!k) return;
    const gap = +(t - at[k - 1]).toFixed(3);
    const both = (x) => mine.filter((c) => c.at === x).every((c) => c.kind === "cascade");
    if (gap + 1e-9 < GAP && !(both(t) && both(at[k - 1])))
      throw new Error(`${s.id}: cues at +${at[k - 1]} and +${t} are ${gap}s apart, under the ${GAP}s floor`);
  });
  const lastCue = Math.max(...at.map((t) => t));
  if (lastCue + 0.5 > s.dur)
    throw new Error(`${s.id}: last cue at +${lastCue} does not finish inside its ${s.dur}s hold`);
  if (s.numTo != null && s.numAt + s.numDur > s.dur - SETTLE)
    throw new Error(`${s.id}: the figure settles ${(s.dur - s.numAt - s.numDur).toFixed(3)}s before the ` +
      `cut, under the ${SETTLE}s floor — shorten the countUp, never the anchor`);
  if (at[0] > FMT.layout.first_cue_by_seconds)
    throw new Error(`${s.id}: first authored element at +${at[0]}, past first_cue_by_seconds`);
});

const cueJs = (kind) => cues.filter((c) => kind.includes(c.kind)).map((c) => c.js).join("\n");

const html = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>The Passive-Income Number — en · CHAPTER 6 · the day, again</title>

<!-- ===========================================================================
     CHAPTER 6 — THE LAST CHAPTER OF THE CUT. The rate is admitted to be
     unsettled BEFORE anything is recapped, then the ladder in one breath, then
     the callback to the morning the video opened on, then one CTA.
     Thirteen cuts, ${ROOT}s, s69-s81.

     GENERATED by build.mjs from ../passive-income-number-en/assets/voice/
     timing.json. Do not hand-edit a timing here: every data-start /
     data-duration / data-framings, the S and D maps, the thirteen <audio> rows
     and the root duration are computed from that one file and asserted against
     the shipped cut's GAPS — a re-time is exactly what produces a correct total
     with every internal cut drifted. Design lives in build.mjs's SCENES table.

     Chapter offset is ${OFF}s (timing.json's own scene_start for line 6.1), and
     ${OFF} + ${ROOT} is timing.json's own total of ${TIMING.total}s, asserted at
     build — this is the one chapter where the two could disagree with no later
     scene to notice. s81 carries its bare scene_duration because there is
     nothing after it in the video at all, not merely nothing in this project.

     Layout: blockframe-9 (run.json architecture, body_class "") under the
     chapter archetype layer. NO RAIL, no chapter title, no scene counter, no
     slide number — format.json chapter_design.rail is false and the viewer must
     never be shown that this video is chapter-based.

     Ten of thirteen scenes are art-off and nine of those are centred. Rule 8
     retires the drawn layer wherever the photograph already carries the beat,
     and .centred then re-centres the stack so the archetype's empty side is not
     a hole. Three scenes are NOT centred and each carries one of §8's three
     declared drawn layers: the ladder assembling (6.7), completing (6.8) and
     being overrun (6.9). That is the TOP of the archetype note's density range
     for a thirteen-scene chapter, not a target, and it is where the storyboard
     spends it.

     Every scene carries has-photo and a real full-bleed .bg under the LOCKED
     grade. No per-scene brightness override anywhere: photo_free_scene_ratio is
     0 and the photograph is the only variable there is. One scene sets a
     background-position, which moves the PHOTOGRAPH inside its own cover box
     and is not a grade knob.
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
   cut's two shoves are s39 -> s40 and s58 -> s59 (§12) and both are behind us.
   The s68 -> s69 chapter joint is a plain dissolve and belongs to the assembly;
   s81 has no successor at all. */
sceneTransitions(IDS, S);

/* THE PHOTOGRAPH CARRIES THE MOTION. Direction alternates, and s75 -> s76 is THE
   HOLD — the cut's third and last, and the ONE that runs OUT (§5): s75.jpg is a
   derived crop of s76.jpg, the push is chained 1.16 -> 1.08 -> 1.00, and the
   pull-back is what makes the ladder get bigger. The pair is in the cut's
   cues-tables.json "holds", so no transition sounds at the joint. Built this way
   the FIRST time, per chapters._carry_forward_en_ch1_to_ch2_ch6, which names
   this exact pair — s3/s4 cost three rounds by being built as two files
   dissolving. */
${kenJs}

/* THE TYPE — cue ladder variant A (storyboard §5) on the statement scenes:
   kicker +0.30, statement +1.10, then the foot at +1.90. Fixed offsets, constant
   whatever a clip's length; every gap is 0.80s and the photograph is already up
   at +0.00, so first_cue_by_seconds (0.5) is met by the kicker — except on s81,
   which has no kicker and whose .cta block takes +0.40 for exactly that reason. */
${cueJs(["kick", "cta"])}
${cueJs(["stmt"])}

/* THE RATE, ALWAYS FIRST (§4). #sN-rate is a first-class 40px .sub at +1.10, not
   a 26px foot a density pass can drop: the assumption is on screen BEFORE the
   corpus lands and the figure arrives into it. Three frames here, and all three
   carry a corpus token that the assert at the bottom of this file checks. */
${cueJs(["rate"])}

/* THE BAND lifts first so the drawn ladder has darkened ground to read against —
   rule 9, never the photograph. ⚠ There is deliberately NO fade() on the <svg>
   itself: ".has-photo.art-forward .art" carries "opacity: .52 !important", which
   beats any inline opacity GSAP writes, so a fade there is a silent no-op. Every
   bar therefore arrives by TRANSFORM, which is a lever the stylesheet does not
   pin. */
${cueJs(["band"])}

/* THE RECAP, SPEECH-ANCHORED. Each ".sub" line and its bar ride the same cue,
   and every cue is a MEASURED word onset — never popEach at a fixed offset
   (owed.cascade_offsets_ignore_the_voice). faster-whisper base.en on this cut's
   own clips, clip-local, +0.25 lead-in:
     6.7  "a quarter of a million"  1.680 -> +1.93
          "a third of a million"    3.540 -> +3.79
          "two thirds of a million" 4.780 -> +5.03
     6.8  "five thousand a month"   1.240 -> +1.49, FLOORED to +1.90 so the rate
                                    at +1.10 keeps its 0.80s gap; +1.90 is still
                                    inside the phrase (1.240-2.740 -> +1.49-2.99)
          "the average household"   4.500 -> +4.75
   Bars one to three do NOT re-animate on 6.8: they are emitted at scale 1 where
   6.7 left them, because re-filling a bar that did not change would assert a
   second climb across a hold that is one continuous shot. */
${cueJs(["cascade"])}

/* THE FIGURE SCENES — cue ladder variant B: kicker +0.30, then the rate (or,
   where §4 forbids one, the foot) at +1.10, then the number ANCHORED on its own
   spoken word with a +1.90 floor, then the foot at num + 0.80.

   EVERY ANCHOR IS MEASURED, not interpolated. faster-whisper base.en, word
   timestamps, on this cut's own clips; clips start at scene +0.25 (MEDIUM
   lead_in_seconds), which is the +0.25 in each figure:
     6.2  "3"  1.980s into the clip -> scene +2.23   (no fallback published)
     6.3  "4"  1.920s               -> scene +2.17   (no fallback published)
     6.9  "5"  5.340s               -> scene +5.59   (§5's fallback said +6.08,
                                                      i.e. 0.49s LATE)

   countUp is for MONEY. 3.9% and 4.7% take a bare pop(): countUp rounds with
   Math.round, so counting to 3.9 would settle on "4%" — which in THIS chapter is
   not a rounding error but a different published figure, and the one the scene
   exists to contrast with. */
${cueJs(["num"])}

/* The foot: +1.90 on a statement scene (variant A), num + 0.80 on a figure
   scene, last cascade item + 0.80 on the recap, +1.20 on the CTA (variant D). */
${cueJs(["foot"])}

window.__timelines = window.__timelines || {};  /* the LINTER reads this file, not motion.js */
register();                                    /* -> window.__timelines["main"] */
</script>

<script>
/* ===========================================================================
   THE RATE ASSERTS — run.json.constraints, mechanised. Carried forward VERBATIM
   from chapters 2, 3, 4 and 5, including the third BILL branch, because a
   per-chapter copy that drifts is worse than no assert: tools/check_vo_frame.py
   reads RATE and MARKER back out of THIS block, so the frame-side and the
   VO-side checks can never disagree about what a rate is.

   (1) withdrawal_rate_on_screen: "Every corpus figure must carry its assumed
       withdrawal/return rate ON SCREEN in the same frame as the number. A number
       without its assumption visible is a fabricated promise."
       LIVE HERE on s75 (\$254,225 · \$332,950 · \$656,650, all three under one
       #s75-rate .sub reading "EACH AT A 4.0% WITHDRAWAL RATE"), on s76
       (\$1,500,000 · \$1,963,375 under "BOTH AT A 4.0% WITHDRAWAL RATE") and on
       s77 (\$5,555,556 under "AT A 1.08% DIVIDEND YIELD").

   (2) derived_income_carries_assumption (EXTENDED 2026-08-07): a DERIVED INCOME
       figure — the corpus's own OUTPUT — carries the rate in frame or an explicit
       ILLUSTRATIVE marker. LIVE HERE on s76, which prints "\$5,000 a month" and
       "\$6,545 a month" beside the corpora they buy; the #s76-rate .sub covers
       both, and ILLUSTRATIVE ARITHMETIC is in the same frame as a second
       defence.

   (3) THE BILL BRANCH, added in ch2. (1) is deliberately narrow — it fires only
       on the eight CORPUS tokens, so a published numerator could render
       completely bare and pass. \$6,545 on s76 is exactly that shape, and it is
       covered twice over here.

   Throwing is the point: "hyperframes check"'s runtime pass fails on an uncaught
   page error, and a silent console.warn is what let this ship twice.

   ⚠ THIS ASSERT IS FRAME-ONLY BY CONSTRUCTION. It reads rendered text, so it
   cannot see a VO line that SPEAKS a figure over a bare frame
   (owed.derived_income_assert_is_frame_only). That half is
   tools/check_vo_frame.py, run against this file at build:
     python3 tools/check_vo_frame.py passive-income-number --cut en --chapter 6
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

/* The cut has no `.stamp` component (§13 D10) and `owed.stamp_warn_red_on_red_upstream`
 * asks every built chapter to be swept for one. Asserted on the EMITTED MARKUP with
 * comments stripped first, so a note that explains the rule cannot satisfy or trip it. */
if (/class="[^"]*\bstamp\b/.test(html.replace(/<!--[\s\S]*?-->/g, "")))
  throw new Error("a .stamp pill was emitted — this cut has none (§13 D10)");

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
 * storyboard §2 and already carrying this chapter's declarations: the s75/s76
 * HOLD (no transition at the joint), s75 under `counted`, and six of these
 * thirteen scenes under `dry`. Nothing in that file was touched by this build.
 *
 * ONE correction the tool cannot make: cues.py defaults `music` to bed-resolve,
 * and §2/D12 chooses **bed-tension** for this cut — its argument is a COST, not
 * a habit. The bed is a per-video fact. */
fs.rmSync("assets/audio.json", { force: true });
const derived = JSON.parse(execFileSync("python3",
  ["../../../tools/audio/cues.py", "."], { encoding: "utf8" }));
derived.music = "bed-tension";
derived._bed = "bed-tension (storyboard §2 / §13 D12) — cues.py defaults to "
  + "bed-resolve; this cut's argument is a cost, not a habit. Overridden by "
  + "build.mjs, not hand-edited into the generated file.";
derived._dry_vs_counted = "s75 is on BOTH the `counted` and the `dry` list in the "
  + "cut's cues-tables.json, which is the storyboard's own state (§2 lists it in "
  + "both). dry wins — cues.py silences derived content cues — so the three-line "
  + "recap cascade emits no clicks. Recorded rather than corrected: the table is "
  + "the fact's one home and this build does not edit it.";
fs.writeFileSync("assets/audio.json", JSON.stringify(derived, null, 1) + "\n");

const nCues = derived.sfx.filter((c) => c.at != null).length;
console.log(`assets/audio.json: ${nCues} cues (derived by tools/audio/cues.py)`);
console.log(`index.html: ${sc.length} scenes, root ${ROOT}s, offset ${OFF}s, ` +
  `cut total ${TIMING.total}s`);
console.log("ladder: " + RUNGS.map((r) => `${r.id} ${r.px}px`).join(" · ") +
  ` · overrun x${OVERRUN} = ${Math.round(OVERRUN * TRACK)}px (${1920 - LX}px visible)`);
sc.forEach((s) => console.log(
  `  ${s.id} ${s.line}  start ${String(s.start).padStart(7)}  dur ${String(s.dur).padStart(6)}` +
  `  d-dur ${String(s.dd).padStart(6)}  track ${s.track}  ${s.arch.toUpperCase()}` +
  `${s.ctr ? " centred" : ""} ${s.art}  tone ${TONE[s.id].toFixed(2)}` +
  `${s.size ? "  focal " + s.size : ""}${s.numAt ? "  num +" + s.numAt.toFixed(2) : ""}`));
