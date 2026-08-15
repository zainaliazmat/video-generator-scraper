/* build.mjs — emits index.html + assets/audio.json for CHAPTER 4 of
 * passive-income-number, -en (@moneymavens101, $).
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
 * Chapter 4 is lines 4.1-4.13 = scenes s40-s52. The rebase constant is
 * timing.json's own scene_start for 4.1 (248.539s), subtracted from every start,
 * exactly as ch1 does with 0.000, ch2 with 46.420 and ch3 with 151.938.
 *
 * SPEC, not invention. arch / ground / art / ctr / focal / ken / sfx are
 * storyboard-en.md §7 verbatim; the kicker / stmt / num / chip / foot strings are
 * script-en.md's own `[arch …]` cue blocks (one home per fact — the storyboard
 * deliberately does not restate copy). Structure copied from ch3's build.mjs.
 *
 * SEVEN RULINGS CARRIED IN. Each is implemented, and each is MEASURED here
 * rather than inherited:
 *
 *  1. THE TANK IS A DRAWN LAYER ON 4.7 (rulings_binding_on_both_cuts.
 *     en_tank_becomes_a_drawn_layer_2026-08-10). The VO says "Go back to the
 *     tank" over a photograph of an outdoor park standpipe — three sessions and
 *     40+ candidates proved the pools hold no tank-with-a-tap — so the vessel is
 *     drawn OVER the photograph the rule requires (`image_per_scene` untouched,
 *     s46 keeps its `.bg`). The script pre-authorised it: 2.2 carries
 *     `lottie candidate: a tank with a level line and one tap … the level is
 *     decorative, never a measurement` and 4.7 carries `the 2.2 tank with the tap
 *     opening and the level dropping`. ⚠ THE LEVEL IS DECORATIVE AND CARRIES NO
 *     MEASUREMENT — see `tank()` for the four things deliberately not drawn.
 *     Built as a parameterised, self-contained piece in the p-d plate's own
 *     coordinate space so `owed.en_ch2_s10_tank_layer` can drop it onto 2.2
 *     verbatim: s10 is ALSO `arch D` (§7), so the same plate rect and the same
 *     viewBox apply with no re-authoring. Drawn layers are in-family on -en and
 *     ONLY on -en; do not port to the hi cut.
 *
 *  2. THE INVARIANT, `separation_not_rank_2026-08-09` §1: *a substantive beat
 *     must not be left in the chapter's darkest frame.* Discharged ON THE
 *     CONTENT OF THE BEAT THAT SITS THERE, not with "satisfied by construction"
 *     — that phrase quotes the RETIRED converse and fin-build has already spent
 *     it once. The floor is s44, re-measured on this build's own chain at
 *     composed median 15.61 (fin-assets 14.91). Line 4.5 is the chapter's least
 *     loaded beat by this file's own census: it is the ONLY scene here carrying
 *     no figure, no rate, no foot, no citation, no drawn layer and no cascade —
 *     three countable elements against the chapter's 4.6 mean and s41's six. The
 *     four frames that MUST be read sit in the top half of the tone run
 *     (s41 #3, s42 #2, s40 #4, s50 #8 of 13). The assert at `INVARIANT` below
 *     mechanises exactly that: the floor scene must not be the chapter's most
 *     loaded frame, and it throws if a later edit gives s44 anything to read.
 *
 *  3. THE OUTLIER LIMB IS TRIGGERED ON s44 AND THE FIX IS FORBIDDEN
 *     (`outlier_limb_is_subordinate_to_the_invariant_2026-08-10`). s44 is alone
 *     at the bottom by 5.84 composed points on this build's chain (6.99 on
 *     fin-assets'), and it STAYS: seven bgpos values span 1.04 points, and the
 *     only other lever relocates the floor onto s48 — line 4.9, `payout DIVIDED
 *     BY price`, the mechanism beat. No knob was spent on it here.
 *
 *  4. TIMING IS MEASURED, NEVER AUTHORED, and so are the cascade offsets.
 *     `owed.cascade_offsets_ignore_the_voice`: s45's three chips fire on three
 *     separate pop() calls at three MEASURED word onsets, never on
 *     popEach(+1.10, 0.6). See the s45 note for why clauses.py's own answer was
 *     rejected on this line — with its own tool's docstring as the reason.
 *
 *  5. s41/s42 ARE ONE MATCHED-FRAME HOLD, BUILT THAT WAY THE FIRST TIME
 *     (`chapters._carry_forward_en_ch1_to_ch2_ch6` — s3/s4 cost three rounds).
 *     ONE photograph, ONE chained plateKen push (1.00->1.08, 1.08->1.16), one
 *     ground across both, no `transition` SFX at the joint (the cut's
 *     cues-tables.json already lists the pair), and the measure bar is HELD at
 *     s41's own value with no re-animation (§9a).
 *
 *  6. s40 AND s51 TAKE THE MEASURED bgpos KNOBS (fin-assets-en-ch4-2 §4), both
 *     re-measured here on this build's own chain rather than taken on trust.
 *
 *  7. s45 IS FRAMED SO THE BLANK SCREEN IS NOT THE SUBJECT
 *     (`chapters.en.4.s45_accepted_with_the_sound_off_question_left_open`).
 *     A build instruction, not a suggestion; the geometry is in the s45 note.
 */
import fs from "node:fs";
import { execFileSync } from "node:child_process";

const CH = 4;
const LINES = ["4.1", "4.2", "4.3", "4.4", "4.5", "4.6", "4.7",
               "4.8", "4.9", "4.10", "4.11", "4.12", "4.13"];
const FIRST = 40;                                   // scene s40 == line 4.1
const TIMING = JSON.parse(
  fs.readFileSync("../passive-income-number-en/assets/voice/timing.json", "utf8"));
const T = 0.45;                                     // format.json scene.transition_seconds

const TARGET = "245,158,11";
const FUND   = "34,197,94";
const WARN   = "239,68,68";

/* ---------------------------------------------------------------- the spec
 * arch   §7 `arch`            f1     §7 `ground` (the --f1 temperature arc, §11)
 * art    §7 `art`             ctr    §7 `ctr` (centred)
 * ken    §5: the direction flips at every boundary EXCEPT a hold, where the
 *        partner continues its predecessor's move. ⚠ ONE DECLARED DEVIATION,
 *        because §5 and §6b contradict each other here and it has to be
 *        resolved rather than papered over. Mechanically alternating from s1
 *        through ch1's s3/s4 hold puts s39 on `o`, which would make s40 `i` and
 *        s41 `o` — but §6b's table says the s41->s42 hold runs `i` 1.00->1.08
 *        then 1.08->1.16, and §5's own sentence says "s75->s76 is the ONE hold
 *        that runs OUT". Two statements against one, so the hold wins and s40
 *        takes `o` instead. The cost is two pull-backs across the s39->s40
 *        joint, which is a chapter boundary AND the cut's first SHOVE (§12) —
 *        i.e. the one joint in the cut where a direction repeat is least
 *        visible, and it is in the assembly rather than in this project. The
 *        alternative costs two push-ins side by side INSIDE the chapter.
 * size   §3's deterministic focal rule, keyed on stmt LENGTH so it cannot drift
 *        when a string changes:  <=24 -> 112 · 25-48 -> 88 · else 76.
 *        Computed below, never written here.
 * role   §1: amber = a figure chosen or published and under examination, green =
 *        a division that closed at a sourced rate, red = what an assumption
 *        costs. 4.4 carries NO role — a division is not a verdict.
 * bgpos  the KEN OFFSET knob. `.bg` is `background-size: cover` inside an
 *        inset:-8% box, so a source narrower than 16:9 carries real VERTICAL
 *        slack that `center` throws away symmetrically. Spending it moves the
 *        PHOTOGRAPH, never the type. Three scenes use it; every number in their
 *        notes was re-measured by this build.
 */
const SCENES = [
  { line: "4.1", arch: "b", f1: "#2a2113", art: "off", ctr: true, ken: "o", role: TARGET,
    kick: "THE WORKED FIGURE",
    num: "$5,000 A MONTH", numTo: 5000, numPrefix: "$", numSuffix: " A MONTH", numAt: 1.90,
    foot: "$60,000 a year, chosen below the BLS average of $6,545 a month so the figure is conservative and cannot be read as a promise",
    img: "s40.jpg", bgpos: "center 35%",
    note: "THE WORKED FIGURE. ⚠ `$5,000 / MONTH` RENDERS AS `$5,000 A MONTH` — §3's own exception table: `/` is not in the 97-codepoint subset and the handoff already replaced the solidus with `DIVIDED BY` elsewhere in this file. Verified against a fontTools dump of NotoSansFinance-var.woff2 at build, not assumed. AMBER, not green: $5,000 is a CHOSEN CONVENTION, not a result — the whole point of the foot is that it was picked BELOW the BLS average so it cannot be read as a promise. ⚠ DERIVED-INCOME BRANCH, satisfied deliberately: the frame renders `$5,000 A MONTH`, which is the DERIVED pattern, and it carries no #s40-rate. §4 routes it to the extension's explicit-MARKER branch and the foot is what pays for it — `BLS` is the marker and it is on screen in the same frame. The foot also carries $6,545, a BILL token, and the same marker covers it. Both branches are asserted at the bottom of the file. The number is a countUp because §5's ladder B says so; the DRY decision on this scene (§2) is about SOUND, not motion — a chosen convention should not RING, but it may still land. Anchor: faster-whisper puts '$5' at 0.000s into the clip = scene +0.25, well under variant B's +1.90 floor, so the floor applies and the figure arrives after its own foot rather than on top of it. `bgpos: center 35%` is fin-assets' measured recommendation (§4.1), TAKEN, and re-measured on this build's own composed chain: median 31.06 -> 30.03, and it is the step INTO the payoff that it buys — s40 -> s41 goes from +1.32 to +2.35 on this chain, and from -0.78 to +0.69 on fin-assets'. On BOTH instruments the knob is the only choice that is correct under either reading, which is the ground the recommendation actually stands on; the RAW instrument's -6.47 vs +6.42 is the same result with the noise stripped out. Four notes are fanned, not the storyboard's five (cosmetic), and the one serial in frame is clipped by the frame edge." },

  { line: "4.2", arch: "b", f1: "#0f3a20", art: "off", ctr: true, ken: "i", role: FUND,
    hold: [1.00, 1.08],
    kick: "RUNG FOUR", rate: "AT A 4.0% WITHDRAWAL RATE",
    num: "$1,500,000", numTo: 1500000, numPrefix: "$", numAt: 4.95,
    foot: "$60,000 divided by 0.04 · ILLUSTRATIVE ARITHMETIC",
    meas: 0.7640, mlab: "THE LADDER",
    img: "s41.jpg",
    note: "RUNG FOUR — PEAK 1 AND THIS CHAPTER'S PAYOFF FRAME (§9b). The hottest green in the video, `#0f3a20`, spent here and nowhere else (§11 rule 2). Rung four of five on the §9a corpus ladder: ONE scale for the whole cut, 920px = $1,963,375, so $1,500,000 is scaleX 0.7640 = 702.9px. NUMERATOR AND DENOMINATOR ARE A PAIR (gotcha 7) — the assert below recomputes 1500000/1963375 and throws if either half is edited alone, and this component may not be re-used at another scale. The rate is a first-class 40px .sub arriving at +1.10, BEFORE the number lands at +4.95: the assumption is on screen first and the figure arrives into it (§4). Anchor MEASURED, not interpolated: faster-whisper puts '$1' of 'one and a half million' at 4.700s into the clip => scene +4.95; §5's character-offset fallback said +5.18, i.e. the fallback was 0.23s late. PAYOFF CLAUSES, re-measured on this build's own composed chain rather than inherited (fin-assets' figures in brackets): sound-off gate PASS — two bank-vault doors set in a brick wall, locking bars, gearwork, a spoked handwheel and a combination dial, nameable in two words with the type covered; MEDIAN #3 of 13 at 32.38 [33.92], inside a top quartile of ceil(13/4) floored at 3 = 4; p10 #2 of 13 at 24.14 [25.95], behind only s42, which is s41's own continuation crop; STEP-IN +2.35 [+0.69], non-negative on both instruments with the s40 knob applied. Near-zero spread is NOT claimed as a credit: s41's p90-p50 is 14.13, 6th of 13, and the narrowest in the chapter is s45's 11.01 — the payoff did not win by being empty." },

  { line: "4.3", arch: "b", f1: "#0f3a20", art: "off", ctr: true, ken: "i", role: FUND,
    hold: [1.08, 1.16],
    kick: "BOTH HALVES, TOGETHER",
    stmt: "$1,500,000 AT 4.0% = $5,000 a month", rateSpan: "4.0%",
    measHeld: 0.7640, mlab: "THE LADDER",
    img: "s42.jpg",
    note: "BOTH HALVES, TOGETHER — the second half of the matched-frame hold, and the reason PEAK 1 has a device no other frame gets: the formula completes across ONE unbroken shot. s42.jpg is a DERIVED CROP of s41.jpg (ffmpeg crop=1600:900:280:186, recorded in s42.jpg.src, credit row re-keyed) — never the same file pointed at twice, which self-dissolves and flickers (creator rule, firaun 2026-07-23). The push is CHAINED: s41 runs plateKen 1.00->1.08 and s42 picks up at exactly 1.08 and runs to 1.16, so the two scenes are one continuous move; both share ONE ground (§11 rule 1) and the joint emits no `transition` (the cut's cues-tables.json lists the pair under `holds`). ⚠ DECLARED FOR THE EDITOR, from fin-assets §4.3 and confirmed on this build's own crop geometry: the crop is a 1.18x push on the WHOLE frame, not the storyboard's 'tighter on the dial' — both doors and most of the brick are still in it. The continuous-push requirement is met; ARRIVING AT THE DIAL is not, and a tighter rect cannot be cut from an 1880x1253 source at >=1600px. §4's fused form: the rate is an inline <span id='s42-rate'> inside the focal wrapping `4.0%`, taking a pulse at +1.90 fixed — no copy is reordered, nothing is printed twice, and there is a node for the assert to find. The focal is measured on its PLAIN TEXT (35 chars -> 88px), so the span markup cannot change the type size. The measure bar is HELD at 0.7640 with NO re-animation (§9a) — it is written as an inline scaleX on #s42-mf and carries no span() call, because re-filling a bar that did not change would assert a second climb." },

  { line: "4.4", arch: "d", f1: "#1c2027", art: "off", ctr: true, ken: "o",
    kick: "WHAT THIS IS", stmt: "Division. Not a forecast.",
    foot: "corpus = annual income DIVIDED BY the withdrawal rate",
    img: "s43.jpg",
    note: "WHAT THIS IS. NO role and no colour, deliberately: the line's own content is that this is not a forecast, not a market call and not a promise, and a role colour here would claim one of the three. The chapter's one neutral ground, `#1c2027`, sits between the green peak and the six reds that follow — §11's cooling step before the warning opens. `DIVIDED BY` in the foot is the same solidus replacement §3 makes on s40, applied to the same file's own convention rather than re-decided. Hands at a drafting board sharpening a pencil over a sheet of paper: sound-off it says working out, which is 4.4, and it is the chapter's second hand frame after s45 — §10 enumerates s18, s33, s45, s53, s58, so s43 is an addition to the enumeration and not to the rule (no face, no wrist brand, hands only). Declared by fin-assets and it survives here." },

  { line: "4.5", arch: "a", f1: "#2b1418", art: "off", ctr: true, ken: "i", role: WARN,
    kick: "NOW THE WARNING", stmt: "This is where the ladder breaks.",
    img: "s44.jpg",
    note: "NOW THE WARNING — the first red of the chapter and the turn into the trap. ⚠ THIS IS THE CHAPTER'S LUMINANCE FLOOR AND IT IS RULED, MEASURED AND DELIBERATELY NOT FIXED. Re-measured on this build's own composed chain: median 15.61, p10 12.06, arriving on -13.11; fin-assets measured 14.91 / 12.15 / -15.73 on theirs. Both instruments agree it is alone at the bottom — 5.84 composed points clear of s48 here, 6.99 there, the largest gap in the chapter on either — so the §3 OUTLIER LIMB genuinely fires. `outlier_limb_is_subordinate_to_the_invariant_2026-08-10` rules NO FIX and this build spent no knob on it: seven background-position values were already measured to span 1.04 points (the photograph is wet black asphalt end to end and has no brighter part to point at), and the only remaining lever relocates the floor onto s48 at a separation of 2.21 — line 4.9, `payout DIVIDED BY price`, the chapter's MECHANISM beat and the storyboard's declared 5:00 beat. THE INVARIANT'S LIVE CLAUSE — *a substantive beat must not be left in the chapter's darkest frame* — is discharged on the CONTENT of the beat that sits here, and NOT on the retired converse: 'satisfied by construction' quotes a sentence that no longer exists and is not an available answer. Two parts, and the second is the one that actually decides it. (i) MECHANISED: the floor frame carries nothing to read beyond its statement — no figure, no rate, no foot, no citation, no cascade, no drawn layer, no measure bar — three countable elements against a chapter mean of 3.85, on the second-shortest scene at 5.711s. The assert marked INVARIANT below re-derives that census at every build and throws if an edit gives this frame something to read. ⚠ THAT HALF IS NECESSARY AND NOT SUFFICIENT, and saying so is the point: FIVE scenes here tie at zero on that census (s44, s47, s48, s51, s52), so counting elements cannot pick out the least substantive beat and must not be presented as if it had. (ii) EDITORIAL, and stated so it can be argued with: of those five, 4.5 is the only one whose statement is a SIGNPOST rather than a claim. 'This is where the ladder breaks' points forward and asserts nothing about a yield, a price, a tank or a rate; 4.8 states what the papers tested, 4.9 defines the mechanism, 4.12 explains 1932 and 4.13 is the chapter's verdict. And the frames that must be READ are all in the top half of the tone run — s42 #2, s41 #3, s40 #4, s50 #8 of 13 on this build's chain — so there is no inversion anywhere between argumentative weight and legibility. It is also not the sourcing rule's failure mode: p10 12.06 / p90 30.94 is a spread of 15.33, 5th widest in the chapter — full-width crosswalk bars and coloured light laid into the water. DARK AND FULL, not dark and empty." },

  { line: "4.6", arch: "c", f1: "#301519", art: "off", ctr: false, ken: "o", role: WARN,
    kick: "ON YOUR FEED",
    chips: [["10%", "12%", "\"monthly income\""]],
    chipAt: [2.67, 3.57, 5.31],
    img: "s45.jpg", bgpos: "center bottom",
    note: "ON YOUR FEED — ladder C, the chips ARE the statement (§5). ⚠ THE FRAMING IS A BUILD INSTRUCTION, NOT A SUGGESTION (chapters.en.4.s45_accepted_with_the_sound_off_question_left_open_2026-08-10): the promoted file is a hand holding a SWITCHED-OFF phone with the screen facing camera, and a plainly-off screen says *there is nothing here* under a line that says *somewhere on your feed there IS a payout advertised*. Frame it so the blank screen is not the subject. THE GEOMETRY, derived rather than eyeballed: the source is 1733x1300 (1.333) against the .bg's 1.778 box, so `cover` is WIDTH-limited — there is ZERO horizontal slack and bgpos cannot move the phone sideways at all. What it can do is spend the 325 source rows of VERTICAL slack: `center` shows source rows 162-1137 and holds ~96% of the screen; `center bottom` shows 325-1300, cutting the top 195 rows of the screen (~22% of it) off the frame edge and bringing the wrist and sleeve in, so the frame reads *a phone in a hand extending out of frame* rather than *an empty screen*. The ken then runs `o`, starting at 1.16, which crops it harder still at the top of the scene where the chips arrive. Measured on this build's composed chain, the knob also pays twice over: median 35.80 -> 33.89 and p10 19.56 -> 16.34, pulling the chapter's BRIGHTEST frame — the one cell fin-assets reports jumping out of the composed run — back toward the tone run, which is exactly where §10 routes a chip cascade (`near-flat, low-key`). NOT `.centred`, per §7: archetype C is type left and artefact full-height right, and here the artefact is the PHOTOGRAPH's phone, which sits at screen x ~1067-1812 — so the 880px left stack column (x150-1030) clears it entirely and the split is not a hole. The chips ride in the stack's own .row, in the left column, and NOTHING is drawn on the phone screen: putting chips over that glass would be fabricating what the feed shows, which is the one thing `never_a_screen_vs_sound_off_2026-08-09` forbids on an internet beat. ⚠ THE CASCADE IS SPEECH-ANCHORED, three separate pop() calls at three MEASURED word onsets — never popEach at a fixed +1.10 (owed.cascade_offsets_ignore_the_voice). faster-whisper puts '10' at 2.420s into the clip, '12' at 3.320s and 'shortcut' at 5.060s (+0.25 lead-in => +2.67 +3.57 +5.31). tools/tts/clauses.py --n 3 returned +0.25 +3.51 +4.61 and its FIRST cell is 2.4s early, because this sentence's first pause-separated part is 'Somewhere on your feed there is a payout advertised at' and not a named item — the exact failure its own docstring warns against forcing. Two of three corroborate within 0.7s; word onsets win on this line, the same call ch3 made on 3.3. The third chip is a quoted advertising phrase that is never spoken, so it is bound to 'shortcut', the word that names what the promise looks like." },

  { line: "4.7", arch: "d", f1: "#38151a", art: "tank", ctr: false, ken: "i", role: WARN,
    band: true, brule: 400,
    kick: "A PROMISE ABOUT THE TAP", stmt: "12% is a wider tap.",
    img: "s46.jpg",
    note: "A PROMISE ABOUT THE TAP — THE TANK, AND IT IS DRAWN (en_tank_becomes_a_drawn_layer_2026-08-10). The VO says «Go back to the tank» and the photograph underneath is an ornate cast-iron park standpipe with a thin twisted trickle: no vessel, no lever, and the frame is being asked to carry the cut's load-bearing device. The pools do not hold a tank-with-a-tap — en ch2 spent 6 contact sheets on 36 candidates and en ch4 4 more — so the vessel is DRAWN over the photograph the rule requires, and s46 keeps its full-bleed `.bg` (image_per_scene is untouched; nothing was removed from the frame). RULE 8 IS SATISFIED THE STRONG WAY, not argued around: a photograph of a tap cannot state that there is a FINITE VESSEL behind it, and finiteness is the entire beat — 4.8 says the papers tested how long a tank LASTS. The drawn layer asserts the thing the picture is structurally incapable of asserting, which is the test. ⚠ THE LEVEL IS DECORATIVE AND ASSERTS NO QUANTITY (`no_return_promise`; the script says so at 2.2 in the same breath as authorising the drawing). Four things are therefore deliberately NOT drawn and the build asserts their absence: no tick marks, no scale, no numeral of any kind, and NO GHOST OF THE PREVIOUS LEVEL — a before/after marker is precisely what would turn a decorative level into a measured drop. The level does not slide, either: it is two rects and the upper slice EXITS, so the change reads as a state, not as a distance travelled down a scale. THE ART IS art-forward AND SITS ON A `.band` (§8) — rule 9 forbids darkening the photograph, so the band darkens BEHIND the mechanism only, at z-index 0 under the plate, exactly as en ch2's s18 does it. `.centred` comes OFF: §7 gives 4.7 `ctr Y` on the assumption the drawn layer was `off`, and a centred scene display:none's its own plate, so the ruling's layer could not exist on it. Archetype D's stack is top-left either way, so no type moves. Assembly finishes at +2.95 against chapter_design's 'about +3.3' and the sheet's late-settle keys off the `v-` class the svg carries, so this scene sheets built rather than half-drawn. ⚠ ONE THING THIS DOES NOT FIX, carried forward: `chapters._carry_forward_en_ch4_to_ch5_s57` — s46's photographed flow is already a thin trickle, so §10's four-frame flow ladder has nothing left to escalate DOWN to at 5.5, and 4.7's own «wider tap» is under-supported by the narrow stream in the frame beneath it. The drawn stream widens, which is the only part of that this chapter can pay. ⚠ PRE-ASSEMBLY PASS 2026-08-12, items 3 and 4 of owed.en_preassembly_batch, and NOTHING ELSE ON THIS SCENE MOVED — same timings, same photograph, same geometry, same ken. (3) `fade('#s46-art')` WAS A SILENT NO-OP: `.has-photo .art` is `opacity: ... !important` and `!important` beats a GSAP tween exactly as it beats an authored inline style, so the tank stood on screen from this scene's first frame instead of arriving, in a render every checker passed. It is now `artOp('#s46-art', +1.00, 0.60)`, a tween on the `--art-op` VARIABLE the stylesheet gained on 2026-08-12 — verified on frames, not asserted: at 41.80s the vessel wall region measures rgb 37 against a ground of 38 (absent), at 44.22s rgb 90 against 31 (arrived). (4) And the same tween carries the LIFT: it rests at ART_OP 0.74 rather than `.art-forward`'s .52, because the scrim composites over the plate and eats ~62% of the drawn layer. 1.73:1 / dRGB 39.7 becomes 2.27:1 / dRGB 57.0. See ART_OP for why the design's 4.3:1 is unreachable at any opacity." },

  { line: "4.8", arch: "a", f1: "#301519", art: "off", ctr: true, ken: "o", role: WARN,
    kick: "WHAT THE PAPERS TESTED", stmt: "How long a tank lasts at each rate.",
    img: "s47.jpg",
    note: "WHAT THE PAPERS TESTED. A brass gate valve on a copper riser, shut and dry, against foliage — the second beat of the two-frame argument (water running -> dry mouth, dry second pipe), and fin-assets verified on a composed sheet that it does NOT read as the same photograph as s46: different mass, different composition, and the flow/no-flow difference survives the grade. NO DRAWN LAYER HERE, and that is a refusal on the record: §8 refuses '4.8 — how long a tank lasts at each rate' because a balance falling to zero over time asserts a DEPLETION SCHEDULE this video has no source for, which is the shape `no_return_promise` forbids. The tank drawn one scene earlier makes the temptation stronger, not weaker; it is declined for the same reason it was declined before the tank existed. The line is carried by type and by the dry valve." },

  { line: "4.9", arch: "d", f1: "#2b1418", art: "off", ctr: true, ken: "i", role: WARN,
    kick: "WHAT A YIELD IS", stmt: "payout DIVIDED BY price",
    img: "s48.jpg",
    note: "WHAT A YIELD IS — the chapter's MECHANISM beat and the storyboard's declared 5:00 beat, the minute both format twins independently land their own 10-12% warning. It is also the frame the floor would relocate onto if s44 were ever re-fetched (see the s44 note), which is why the stopping rule ends here rather than one turn further round. `payout DIVIDED BY price` uses the same solidus replacement as s40 and s43 — a yield written with a `/` would be a glyph this cut does not own AND a second meaning for a mark the file uses nowhere else. A brass pan hanging on chains loaded with dried root slices, with a counterweight on a wooden beam. ⚠ DECLARED, from fin-assets' correction 2: it is a Chinese herbal apothecary, and only ONE pan is in frame against §7's 'a two-pan balance where the right pan has dropped' — so the frame shows the machine that COMPARES without showing a comparison. No signage, no language and no character is in frame, so a viewer reads *an old brass scale*; kept under `every frame is American` as a currency-neutral object, and named precisely here so the next reader is not surprised. Sound-off this is the weakest of the thirteen alongside s43." },

  { line: "4.10", arch: "d", f1: "#301519", art: "yield", ctr: false, ken: "o", role: WARN,
    band: true, brule: 430,
    kick: "THE PRICE FELL", stmt: "Same payout. Smaller price. Smaller tank.",
    /* THE BARS ARE NAMED (owed.en_preassembly_batch item 2, fin-review's only
     * TOP finding on this chapter). The proportions were never wrong: numerator
     * fixed, denominator halving, quotient doubling. What inverted the READING
     * is that the doubling bar sat unnamed directly under "Smaller tank.", so
     * the one thing growing on screen read as the tank. Naming it YIELD is the
     * whole fix. Positions are the bars' own screen centres: p-d maps plate x
     * 1:1 and plate y + 424, so PAYOUT sits on 600-680, PRICE on 744-824 and
     * YIELD on 864-944; the labels are a column at x780, clear of the widest
     * bar (x740) and 880px clear of the watermark box at x1772.
     * ⚠ THEY ARE `.measure-lab` AND THEY LIVE OUTSIDE THE PLATE, on purpose:
     * the system's own label component is z-index 2, i.e. ABOVE the scrim, so a
     * 22px glyph is not subject to the ~62% the scrim takes out of everything
     * inside the plate (item 4 of the same batch). A label drawn inside the
     * `.art` would have landed at the contrast the bars themselves are being
     * lifted to escape, and glyphs are exactly what does not survive there. */
    artlab: [["PAYOUT", 780, 629], ["PRICE", 780, 773], ["YIELD", 780, 893]],
    img: "s49.jpg",
    note: "THE PRICE FELL — §8's declared drawn layer for this chapter, and the only beat here that is a PROPORTION rather than a figure. `yield-fraction`: a numerator block that never moves, a heavy 14px divisor rule, a denominator that HALVES, and a quotient bar below and separate that DOUBLES. THE ARITHMETIC, stated at the point of edit (gotcha 7): denominator x0.5 => quotient x2.0, exactly, and both endpoints are computed from ONE constant so the drawing and the animation cannot disagree — the assert throws if either is edited alone. It is deliberately a FRACTION and not three parallel bars: the hi cut's funnel read as a rising growth curve, and parallel bars read as a chart, i.e. as data rather than as arithmetic. What it asserts that the photograph cannot: the picture can say the price changed; only the drawing can say the payout did NOT. It is the chapter's one `art-forward` scene (52%) and it sits on a `.band` at z-index 0 under the plate — rule 9, never the photograph. ⚠ WATCH THIS ONE ON THE ENCODE, and the reason is a corrected fact: fin-assets' attempt 1 recorded this photograph as 'a weathered board wall with peeling paint, raking light', and at full resolution it is WHITE SPRAY PAINT on dark blue-black planks — soft-edged strokes with overspray speckle. So the chapter's most graphic frame (p90-p50 15.85 on this chain, 18.62 on fin-assets') sits under the chapter's only 52% mechanism, which §10 routes to the calmest subject. The band is what makes it survivable and the strokes run diagonally against a mechanism that is entirely orthogonal, but only the encode settles it. §7 declares this scene's cue is `tick`, so the quotient takes a pulse when it finishes doubling — that pulse is a real beat on the element that just changed, and it is also what makes the declared cue derivable. ⚠ PRE-ASSEMBLY PASS 2026-08-12, items 2, 3 and 4 of owed.en_preassembly_batch. NO TIMING, NO GEOMETRY, NO IMAGE AND NO ARITHMETIC MOVED. (2) THE BARS ARE NAMED — fin-review's only TOP finding on this chapter, and it was a READING inversion rather than a proportion error: the quotient doubles directly under a third clause reading «Smaller tank.», so the one bar growing on screen read as the tank getting bigger. PAYOUT / PRICE / YIELD, three `.measure-lab` labels in a column at x780 on the bars' own screen centres, arriving with the art at +1.30. They sit OUTSIDE the plate deliberately: `.measure-lab` is z-index 2, i.e. above the scrim, and a 22px glyph inside the `.art` would land at the very contrast items 3-4 exist to escape. The fraction is untouched — still a fraction and still not three parallel bars. (3) `fade('#s49-art')` was the same silent no-op s46 carried and is now `artOp('#s49-art', +1.30, 0.60)`; measured absent at 58.90s (numerator region rgb 47 on its own ground) and arrived at 61.20s (rgb 100 on 45). (4) It rests at ART_OP 0.74, giving 2.36:1 / dRGB 56.0 on the numerator where .52 gave dRGB 39.4. ⚠ MEASURED AND RECORDED BECAUSE IT WILL BE RE-MEASURED: the two `--warn` bars are a CHROMA signal, not a luminance one — the denominator reads rgb 86 against its own ghost track's 41 in the red channel and 35-vs-34 / 40-vs-39 in the other two, so a WCAG luminance ratio (1.32:1 on the quotient) badly undersells what is on screen. Judge the red bars on dRGB or on the frame, never on the ratio." },

  { line: "4.11", arch: "b", f1: "#38151a", art: "off", ctr: true, ken: "i", role: WARN,
    kick: "THE ALL-TIME HIGH", num: "13.84%", numAt: 3.05,
    foot: "S&P 500 dividend yield, series from 1871 — maximum 13.84% in June 1932; long-run mean 4.21%, median 4.19% · multpl.com, read 5 Aug 2026",
    img: "s50.jpg",
    note: "THE ALL-TIME HIGH. NO countUp and NO #s50-rate. No countUp because countUp rounds with Math.round and counting to 13.84 would settle on `14%` — a different figure from the one the foot cites — and because a published maximum is not a quantity that accumulates. No separate rate element because §4 lists s50 among the nine frames carrying a RATE AS THEIR FOCAL: printing `13.84%` under itself reads as a defect. The foot is the provenance and it is the whole defence of the number, so it takes cue 2 at +1.10 and is on screen a clear 1.95s before the figure. Anchor MEASURED: faster-whisper puts '13' at 2.800s into the clip => scene +3.05 (§5 published no fallback for this line). §2 declares this scene DRY and the reason is the argument, not the pace: a `hero` on a June-1932 yield sells a warning as a prize, which is the one thing this chapter exists to refuse. A stack of folded newsprint shot edge-on; 10x crop-zooms found one blackletter flourish and a register mark and NO word, headline or date anywhere — era-neutral rather than era-wrong, which matters on the one frame whose foot names 1871 and 1932." },

  { line: "4.12", arch: "c", f1: "#301519", art: "off", ctr: true, ken: "o", role: WARN,
    kick: "WHAT WAS HAPPENING",
    stmt: "The yield was enormous because the price had collapsed.",
    img: "s51.jpg", bgpos: "center bottom",
    note: "WHAT WAS HAPPENING — the one identifiably American frame in the chapter and the one archival exception (§10): a 1931 Chicago breadline, NARA, public domain. `bgpos: center bottom` is fin-assets' second measured recommendation, TAKEN, and it does two jobs. Legibility, re-measured on this build's own composed chain: median 23.25 -> 26.79, p10 14.01 -> 14.86, spread 15.02 -> 12.39 (fin-assets measured 24.11 -> 27.98 on theirs, the same move to within 0.4). And FRAMING: the source is 2939x2392, so `cover` keeps 1653 of 2392 rows and the visible window starts at source row ~853 at `bottom` against ~483 at `center`, which puts the painted banner `FREE SOUP COFFEE & DOUGHNUTS FOR THE UNEMPLOYED` (ending ~row 575) and the `ALBERT HORAN / BAILIFF` sign (~603) OUT of frame, along with `PARKING 25¢` — a frame that would otherwise carry three legible text blocks under a line about a collapse. What survives is the queue, the wet pavement and a small `FREE SOUP &` on the shop glass, and fin-assets confirmed on a composed render that it still reads unmistakably as a breadline. ⚠ DECLARED, unresolved and NOT hidden: the front-row faces ARE distinct, against §10's 'faces indistinct'. The subjects are 1931 and the claim is historical rather than personal, and the alternative crops cost the banner removal; fin-review settles it on the encode. The focal is 54 chars -> 76px over three lines, the ladder's bottom step and never below it." },

  { line: "4.13", arch: "d", f1: "#38151a", art: "off", ctr: true, ken: "i", role: WARN,
    verdict: true,
    kick: "THE RULE", stmt: "A very big yield is very often a very small price.",
    img: "s52.jpg",
    note: "THE RULE — a verdict scene, one of the cut's five (§2). Its stmt enters with `pop` (back.out(1.7)) instead of `rise`; THAT is the slam, and it is what makes the `stamp` SFX legal without a .stamp pill and without one word of new copy. This cut has no .stamp component by design — five rotated pills would be a tic. Smashed glazed pottery on bare dirt: the object is a broken vessel, which closes the tank line the chapter opened at 4.7 without drawing a second one, and it is the chapter's last frame before ch5. Back to `#38151a`, the hottest red spent in this chapter, matching 4.7's wide-open tap — the argument ends where it turned." },
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
    // scene in ch4 swaps its photograph (the s41/s42 hold is two SCENES, not
    // two framings of one), so each is a single value equal to the scene's own
    // hold; emitting it anyway removes any question about whether an absent
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
    if (f > 9.0) throw new Error(`${s.id} holds one photo for ${f}s (max 9.0)`);
  });
});

/* THE HOLD, asserted rather than trusted (chapters._carry_forward_en_ch1_to_
 * ch2_ch6 — s3/s4 cost three rounds because the pair was built as two files
 * dissolving). A hold pair must be ONE continuous push: the second scene's
 * plateKen has to start at exactly the value the first one ended on, and both
 * must share one ground, or the "cut that is not happening" becomes visible. */
sc.forEach((s, i) => {
  if (!s.hold || i === 0 || !sc[i - 1].hold) return;
  const p = sc[i - 1];
  if (Math.abs(p.hold[1] - s.hold[0]) > 1e-9)
    throw new Error(`${p.id}->${s.id} hold is not continuous: ${p.hold[1]} then ${s.hold[0]}`);
  if (p.f1 !== s.f1)
    throw new Error(`${p.id}->${s.id} is a hold with two grounds (§11 rule 1)`);
});

/* §3's build guard: no `/` and no `?` in any on-screen string. Both ARE in the
 * dumped 97-codepoint subset — but the storyboard bans them as COPY: `·` is this
 * cut's separator and the cut asks no rhetorical questions on screen. It also
 * sweeps the ₹ this cut is forbidden to show and any Devanagari that could
 * arrive from the sibling cut. SUBSET dumped with fontTools from
 * tools/scaffold/assets/fonts/NotoSansFinance-var.woff2 (97 codepoints,
 * re-verified at this build); a missing glyph renders as tofu and no check
 * catches it — pipeline_check's own uncovered_glyphs() is inert on a chapter
 * project, because it keys off the literal string "FinanceSans" appearing in
 * the composition and the face is named only in the LINKED blockframe.css. */
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
  if (s.rateSpan && !s.stmt.includes(s.rateSpan))
    throw new Error(`${s.id}: rate span "${s.rateSpan}" is not in the focal`);
  chipList(s).forEach((c) => {
    if (c.length > 22) throw new Error(`${s.id}: chip "${c}" is ${c.length} chars (max 22)`);
  });
  if (s.chips && s.chipAt.length !== chipList(s).length)
    throw new Error(`${s.id}: ${chipList(s).length} chips but ${s.chipAt.length} measured onsets`);
  if (s.chips) {
    s.chips.forEach((r) => {
      if (r.length > 3) throw new Error(`${s.id}: more than 3 chips in one row`);
    });
    if (chipList(s).length > 5) throw new Error(`${s.id}: cascade over 5 items`);
    s.chipAt.forEach((t, k) => {
      if (k && t <= s.chipAt[k - 1]) throw new Error(`${s.id}: chip onsets are not monotonic`);
      if (t + 0.6 > s.dur) throw new Error(`${s.id}: chip ${k + 1} finishes past the scene`);
    });
  }
  /* the drawn layer never becomes the whole scene, and a centred scene has no
   * plate to put one in (.scene.centred .plate is display:none). */
  if (s.art !== "off" && s.ctr) throw new Error(`${s.id}: drawn art on a centred scene`);
  if (s.art !== "off" && !s.img) throw new Error(`${s.id}: art without a photograph`);
  if (s.art !== "off" && !s.band) throw new Error(`${s.id}: drawn art with no .band under it (rule 9)`);
  if (!s.img) throw new Error(`${s.id}: no photograph — photo_free_scene_ratio is 0`);
});

/* --------------------------------------------------------------- INVARIANT
 * `separation_not_rank_2026-08-09` §1: a substantive beat must not be left in
 * the chapter's darkest frame. The rule cannot be discharged by construction —
 * that phrase quotes the RETIRED converse — so it is discharged on the CONTENT
 * of the beat that sits at the floor, and mechanised so a later edit cannot
 * quietly break it.
 *
 * THE FLOOR IS s44, on two independent instruments: this build re-measured the
 * composed chain (grade -> ken 1.08 -> .field .38 -> the four .scrim layers) at
 * median 15.61 against s48's 21.45, and fin-assets-en-ch4-2 §1 measured 14.91
 * against 21.90.
 *
 * ⚠ WHAT THIS ASSERT DOES AND DOES NOT DO. It re-derives a LOAD CENSUS — what a
 * viewer has to read in each frame — and holds the floor scene at zero. That is
 * NECESSARY AND NOT SUFFICIENT and the code says so rather than implying
 * otherwise: five scenes in this chapter tie at zero, so the census cannot pick
 * out the least substantive beat. The clause is decided in the s44 note, on the
 * content of the sentence that sits there. What the assert buys is that a later
 * edit cannot QUIETLY break the premise the ruling rested on — the moment s44
 * gains a figure, a foot, a citation, a cascade or a drawn layer, the build
 * stops and the invariant has to be re-argued instead of re-broken. The other
 * two limbs of the stopping rule are checked here too, because both are
 * mechanical: the floor must not be the payoff and must not be the longest-held
 * frame. */
const FLOOR = "s44", PAYOFF = "s41";
const load = (s) => [s.num, s.rate, s.sub, s.foot, s.meas || s.measHeld,
                     s.art !== "off" ? 1 : null, s.chips].filter(Boolean).length;
{
  const f = sc.find((s) => s.id === FLOOR);
  if (!f) throw new Error("INVARIANT: the declared floor scene is not in this chapter");
  if (load(f) !== 0)
    throw new Error(`INVARIANT: ${FLOOR} now carries ${load(f)} thing(s) to read; the floor ` +
      `was ruled acceptable BECAUSE 4.5 has nothing to read beyond its statement ` +
      `(outlier_limb_is_subordinate_to_the_invariant_2026-08-10). Re-argue it.`);
  if (FLOOR === PAYOFF)
    throw new Error("INVARIANT: the floor is the payoff frame — a defect under every reading");
  const longest = sc.reduce((a, b) => (b.dur > a.dur ? b : a));
  if (longest.id === FLOOR)
    throw new Error("INVARIANT: the floor is the chapter's longest-held frame");
  if (Math.max(...sc.map(load)) < 3)
    throw new Error("INVARIANT: the census stopped measuring anything");
}

/* ---------------------------------------------------------- the drawn layers
 * TWO, in a thirteen-scene chapter. §8 budgets ch4 exactly one (`yield-fraction`
 * on 4.10); the second is the tank, added by a ruling dated after the storyboard
 * (en_tank_becomes_a_drawn_layer_2026-08-10). Two is still well under the
 * archetype note's "three or four in a twelve-to-fourteen scene chapter is the
 * TOP of the range, not the target", and every other scene here is art-off.
 * WHAT WAS DECLINED, so the choice is on the record rather than implied:
 *   · 4.8's "how long a tank lasts at each rate" — §8 refuses it outright: a
 *     balance falling to zero over time asserts a depletion schedule we have no
 *     source for. Having drawn the tank one scene earlier does not buy it.
 *   · 4.7's "a 12% tap beside a 4% tap" — §8 refuses it on the script's own ⚠:
 *     two apertures side by side say a yield and a withdrawal rate are the same
 *     kind of thing, the exact conflation this chapter exists to avoid. ONE tank
 *     and ONE tap are drawn, and no comparison is.
 *   · 4.11's yield series since 1871 — drawing the curve asserts every point of
 *     a series we hold one figure from, and truth_bar forbids fabricating the
 *     source document. The archival page plus the foot's citation is the honest
 *     treatment.
 *   · 4.2's $1,500,000 — §8: no drawn layer of any kind on s41. It already
 *     carries the §9a measure bar, which is the cut's one climb device.
 */

/* ART_OP — THE RESTING LEVEL OF EVERY DRAWN LAYER IN THIS CHAPTER.
 * `.art-forward`'s .52 is what the stylesheet gives; this is what the frame
 * needs, and the difference is `owed.en_preassembly_batch` item 4: `.plate` is
 * z-index 0 and `.scrim` is z-index 1, so the scrim composites OVER the drawn
 * art while `.stack` type sits above it untouched. Measured from this
 * chapter's own frames, the scrim + grain + field stack transmits about 38% of
 * what is under it, so a contrast computed PRE-scrim lands at roughly half its
 * predicted value. That is a known compensation and not a z-order bug
 * (chapter-design.css:96 says so in as many words) — the knob is the resting
 * opacity, and `--art-op` is now exactly that knob.
 *
 * MEASURED ON RENDERED FRAMES, not computed (snapshots/qa/pre1 at .52 and
 * snapshots/qa/b1 at .74, same times, same ken):
 *                        .52                    .74
 *   s46 vessel wall      rgb 72 on 31           rgb 90 on 31
 *                        1.73:1 · dRGB 39.7     2.27:1 · dRGB 57.0
 *   s49 numerator        (same construction)    rgb 100 on 45
 *                                               2.36:1 · dRGB 56.0
 *
 * ⚠ THE DESIGN'S OWN 4.3-5:1 PREDICTIONS ARE STRUCTURALLY UNREACHABLE AND THAT
 * IS THE FINDING, not this number. Solving the measured line for 3.0:1 (WCAG
 * 1.4.11, non-text) needs --art-op 0.97, and 4.3:1 needs 1.21 — i.e. more than
 * fully opaque cream. No opacity reaches the target because the scrim floors
 * the ground and ceilings the ink at the same time. So the value is chosen
 * against the two limits the ruling DOES leave, both measured here:
 *   1. it must not compete with the TYPE — at .74 the drawn ink is L 0.087
 *      against the focal's 0.229 and the kicker's 0.358, i.e. 38% of the
 *      quietest type on the frame;
 *   2. it must not overpower the PHOTOGRAPH (rule 9) — at .74 the ink sits
 *      between the picture's own p99 (L 0.042) and p99.9 (L 0.174), so it is
 *      brighter than 99% of the frame and dimmer than the frame's highlights.
 * For calibration: ch6's rungs passed review on the ENCODE at dRGB 38.8-40.7,
 * which is exactly where .52 was sitting. .74 is a real lift above the band
 * that has already been shown to survive an encode, not a rescue. */
const ART_OP = 0.74;

/* THE TANK — 4.7 now, and 2.2 in the pre-assembly pass (owed.en_ch2_s10_tank_
 * layer), which is why it is a parameterised function over ONE origin rather
 * than geometry welded to this scene. s10 is also `arch D` (storyboard §7), so
 * the plate rect and the viewBox are identical there and this drops in verbatim
 * with `{drop:false, widen:false}` — at 2.2 the tank is being FILLED and neither
 * the level nor the tap has moved yet.
 *
 * ⚠ THE LEVEL IS DECORATIVE, NEVER A MEASUREMENT (no_return_promise). Four
 * things are deliberately absent and asserted absent below: a tick, a scale, a
 * numeral, and a ghost of the previous level. A before/after marker is exactly
 * what turns a decorative level into a measured drop, and a drawn level that
 * reads as a quantity is the video asserting a number it never sourced.
 *
 * CONSTRUCTION (design-chapter-archetypes, "what a drawn layer has to look like
 * to survive the encode"): solid fills only, nothing thinner than 22px, the
 * water at fill-opacity .5 — a fill-opacity, not an opacity, so the entrance
 * fade is free to run 0 -> 1 and so `.has-photo.art-forward .art`'s !important
 * 52% is the only global lever. Authored in the PLATE's own coordinate space
 * (p-d = 0 0 1920 656 mapping 1:1 to screen x, y+424), never in 1920x1080.
 *
 * PLACEMENT ARITHMETIC. The box is 697x356 at plate (600,180) => screen
 * x 600-1297, y 604-960. Below the `.band`'s start (y583) so everything drawn
 * is over darkened ground; above the 970px bottom safe line; and clear of the
 * watermark box (#root::after is right:64 bottom:40, 84x84 => x1772-1856,
 * y956-1040), which no scene may paint into. */
const TANK = {
  x: 600, y: 180,                      // origin in the p-d plate's own space
  wall: 22, w: 556, h: 356,            // vessel outer box (open top)
  lvl: 120,                            // interior y where the water surface sits
  slice: 96,                           // the upper slice that leaves when it drops
};
function tank(id, o) {
  const t = TANK, iw = t.w - 2 * t.wall, ix = t.x + t.wall;
  const fl = (x, y, w, h, cls, extra) =>
    `      <rect class="${cls}" ${extra || ""} x="${x}" y="${y}" width="${w}" height="${h}"/>`;
  const floorY = t.y + t.h - t.wall;
  const surf = t.y + t.lvl;
  return [
    `<svg class="art v-tank" id="${id}-art" viewBox="0 0 1920 656" preserveAspectRatio="xMidYMid slice">`,
    `      <!-- the vessel: an open-topped tank you filled. Solid ink, ${t.wall}px walls. -->`,
    fl(t.x, t.y, t.wall, t.h - t.wall, "fl"),
    fl(t.x + t.w - t.wall, t.y, t.wall, t.h - t.wall, "fl"),
    fl(t.x, floorY, t.w, t.wall, "fl"),
    `      <!-- the water. TWO rects, not one sliding rect: the upper slice EXITS,`,
    `           so the change reads as a state and not as a distance travelled down`,
    `           a scale. No tick, no scale, no numeral, no ghost of the old level. -->`,
    fl(ix, surf + t.slice, iw, floorY - surf - t.slice, "flw", `id="${id}-lvl" fill-opacity=".5"`),
    fl(ix, surf, iw, t.slice, "flw", `id="${id}-lvlx" fill-opacity=".5"`),
    `      <!-- one tap, on the vessel's own wall: outlet, down-turn, stem, crossbar -->`,
    fl(t.x + t.w, t.y + 180, 118, 24, "fl"),
    fl(t.x + t.w + 94, t.y + 180, 24, 76, "fl"),
    fl(t.x + t.w + 45, t.y + 136, 22, 44, "fl"),
    fl(t.x + t.w + 13, t.y + 118, 86, 22, "fl"),
    `      <!-- the stream. Broadens from the spout's own left edge when the tap`,
    `           opens wider. ⚠ transform-origin is "0% 50%" and that is MEASURED,`,
    `           not preferred: authored as "50% 0%" the rect rendered ~860px LEFT`,
    `           of its own x under GSAP's SVG transform handling, caught on the`,
    `           max-density snapshot at 44.22s (snapshots/qa/b2). "0% 50%" is the`,
    `           form every scaled rect in this run's ch2 and ch3 uses and the form`,
    `           the yield-fraction on 4.10 renders correctly with in the same`,
    `           file. Do not "tidy" it back to a centred origin. -->`,
    fl(t.x + t.w + 94, t.y + 256, 24, 100, "flw",
      `id="${id}-stream" fill-opacity=".5" style="transform-origin:0% 50%"`),
    `    </svg>`,
  ].join("\n");
}
/* The four absences, asserted on the emitted MARKUP rather than promised in
 * prose. ⚠ COMMENTS ARE STRIPPED FIRST, and that is not tidiness: written
 * naively this fired on the tank's own comment saying "no tick, no scale, no
 * numeral" — i.e. it punished the note explaining the rule and would have been
 * silenced by deleting it. Exactly the shape of the Lottie guard that fired on
 * the CSS comment describing the trap it prevents (tool_fixes_this_run,
 * 2026-08-08), reproduced here in a fresh file within the hour. */
{
  const svg = tank("sX", {}).replace(/<!--[\s\S]*?-->/g, "");
  for (const [what, re] of [["a numeral", /<text/], ["a tick or scale", /tick|scale|gauge/i],
                            ["a ghost level", /ghost|prev|before/i]])
    if (re.test(svg)) throw new Error(`tank: the level must carry no ${what} — it is decorative`);
  if (!/id="sX-lvlx"/.test(svg)) throw new Error("tank: the level slice is missing");
}

/* THE YIELD FRACTION — §8's declared layer for 4.10, p-d, viewBox 0 0 1920 656.
 * THE ARITHMETIC, at the point of edit (gotcha 7): the denominator halves and
 * the quotient therefore doubles, EXACTLY. One constant drives both, so the
 * drawing and its animation cannot disagree, and the assert below throws if
 * either endpoint is edited alone. This is arithmetic, not a statistic: nothing
 * here is a published figure and nothing is drawn to a source's scale.
 *
 * GEOMETRY, in the plate's own space => screen y+424. The whole mechanism lives
 * between plate y176 and y540 (screen 600-964): under the type band (arch-d's
 * stack ends at about screen y400 on this scene and the brule sits at 430),
 * below the `.band`'s start at screen 583 so it is drawn on darkened ground,
 * above the 970 bottom safe line, and left of x1500 so it cannot reach the
 * watermark. */
const FALL = 0.5;                                   // the price halves
const RISE = 1 / FALL;                              // so the yield doubles: 2.0
const YF = { x: 260, num: 176, rule: 288, den: 320, quo: 440, w: 480, h: 80, r: 14 };
function yieldFraction(id) {
  if (Math.abs(FALL * RISE - 1) > 1e-12)
    throw new Error("yield-fraction: denominator x quotient must be 1 — a yield IS payout/price");
  if (RISE !== 2) throw new Error("yield-fraction: the storyboard's arithmetic is halve => double");
  const y = YF;
  return [
    `<svg class="art v-yield" id="${id}-art" viewBox="0 0 1920 656" preserveAspectRatio="xMidYMid slice">`,
    `      <!-- numerator: the payout. It never changes, and that is the point. -->`,
    `      <rect class="fl" id="${id}-num2" x="${y.x}" y="${y.num}" width="${y.w}" height="${y.h}"/>`,
    `      <rect class="fl" id="${id}-rule" x="${y.x - 30}" y="${y.rule}" width="${y.w + 60}" height="${y.r}"/>`,
    `      <!-- denominator: the price. A ghost rect at .2 holds where it WAS —`,
    `           a proportion needs its own track, and here the track is a fill,`,
    `           never an outline (2-3px scaffolding does not survive the encode). -->`,
    `      <rect class="fl" id="${id}-ghost" x="${y.x}" y="${y.den}" width="${y.w}" height="${y.h}" fill-opacity=".2"/>`,
    `      <rect class="flw" id="${id}-den" x="${y.x}" y="${y.den}" width="${y.w}" height="${y.h}" style="transform-origin:0% 50%"/>`,
    `      <!-- the quotient, below and SEPARATE: the yield the fraction resolves to. -->`,
    `      <rect class="flw" id="${id}-quo" x="${y.x}" y="${y.quo}" width="${y.w / 2}" height="${y.h}" style="transform-origin:0% 50%"/>`,
    `    </svg>`,
  ].join("\n");
}

/* §9a · the measure bar. 920px = $1,963,375 (rung five, the whole household at
 * 4.0%) => 1px = $2,134.10. This is the ONE scale for all six ladder frames in
 * the cut and it may not be re-used at another. Rung four is this chapter's. */
const LADDER_TOP = 1963375;
sc.filter((s) => s.meas || s.measHeld).forEach((s) => {
  const src = s.num || s.stmt;
  const corpus = Number(src.match(/\$[\d,]+/)[0].replace(/[^0-9]/g, ""));
  const exact = corpus / LADDER_TOP;
  const val = s.meas || s.measHeld;
  if (Math.abs(exact - val) > 0.0005)
    throw new Error(`${s.id} measure ${val} != ${corpus}/${LADDER_TOP} = ${exact.toFixed(4)}`);
});

/* ------------------------------------------------------------------ markup */
const esc = (t) => t.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
const PLATE = { a: "p-a", b: "p-b", c: "p-c", d: "p-d" };
const ART = { tank, yield: yieldFraction };

function focalHtml(s) {
  let t = esc(flat(s.stmt)).replace(/\n/g, "<br>");
  if (s.rateSpan) {
    // §4's FUSED form: the rate is an inline span INSIDE the focal, wrapping the
    // rate token, carrying the role colour and taking a pulse. No copy is
    // reordered and nothing is printed twice.
    const rc = s.role === FUND ? "fundc" : s.role === TARGET ? "targetc" : "warnc";
    t = t.replace(s.rateSpan, `<span class="${rc}" id="${s.id}-rate">${s.rateSpan}</span>`);
  }
  return t;
}

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
  L.push(`  <div class="bg" id="${s.id}-bg" style="background-image:url(assets-ch4/final/${s.img})` +
    `${s.bgpos ? `;background-position:${s.bgpos}` : ""}"></div>`);
  L.push(`  <div class="field" style="--f1:${s.f1}"><div class="rules"></div><div class="glow"${glow}></div></div>`);
  if (s.band)
    // z-index 0 inline and BEFORE the plate in DOM order, so it paints UNDER the
    // drawn layer. `.band`'s own z-index is 1 (the .scrim's band), which would
    // put it OVER a z-0 plate and darken the art instead of the ground behind
    // it. Same construction as en ch2's s17/s18.
    L.push(`  <div class="band" id="${s.id}-band" style="z-index:0"></div>`);
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
      `${focalHtml(s)}</p>`);
  if (s.chips) {
    // Ladder C on archetype C. blockframe's own `.row` inside `.stack`, NOT a
    // hand-rolled flex row and NOT ch3's absolutely-positioned `.v-chiprow`:
    // `.arch-c .stack` is already an 880px left column, which is where these
    // belong (see the s45 note — the phone is the artefact on the right and the
    // chips must not be drawn onto its screen). Rows are declared EXPLICITLY
    // because `.row` wraps and a silent orphan is not flagged by any checker.
    s.chips.forEach((row, r) => {
      L.push(`    <div class="row" id="${s.id}-crow${r + 1}">`);
      row.forEach((c, k) => L.push(
        `      <div class="chip${rc ? " " + rc.trim().replace("c", "") : ""}"` +
        ` id="${s.id}-c${r * 3 + k + 1}">${esc(c)}</div>`));
      L.push(`    </div>`);
    });
  }
  if (s.sub)
    L.push(`    <p class="sub" id="${s.id}-sub">${esc(s.sub)}</p>`);
  if (s.foot)
    L.push(`    <p class="foot" id="${s.id}-foot">${esc(s.foot)}</p>`);
  L.push(`  </div>`);
  if (s.meas || s.measHeld) {
    // §9a. OUTSIDE .stack on purpose: .measure/.measure-lab position themselves
    // at left calc(50% - 460px), which is why `.centred` does not hide them and
    // why the device survives on a photo-led cut. s42 carries the bar HELD at
    // s41's own value — an inline scaleX and no span() call.
    const held = s.measHeld ? ` style="transform:scaleX(${s.measHeld})"` : "";
    L.push(`  <p class="measure-lab under" id="${s.id}-mlab">${esc(s.mlab)}</p>`);
    L.push(`  <div class="measure under" id="${s.id}-meas">` +
      `<div class="measure-fill fund" id="${s.id}-mf"${held}></div></div>`);
  }
  if (s.artlab)
    // Labels for a drawn mechanism. Same component as §9a's bar label and for
    // the same reason — z-index 2 puts a glyph ABOVE the scrim, where the bars
    // it names cannot go. No `.under` class: these are positioned per bar.
    s.artlab.forEach(([t, x, y], k) => L.push(
      `  <p class="measure-lab" id="${s.id}-al${k + 1}" style="left:${x}px;top:${y}px">${esc(t)}</p>`));
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
 * endpoints on its `.bg`, which is what makes two scenes one continuous zoom;
 * every other scene takes ken's fixed 1.00<->1.16. */
const kenJs = sc.map((s) => s.hold
  ? `plateKen("#${s.id}-bg", S.${s.id}, D.${s.id}, ${s.hold[0].toFixed(2)}, ${s.hold[1].toFixed(2)});`
  : `ken("#${s.id}-bg", S.${s.id}, D.${s.id}, ${s.ken === "i"});`).join("\n");

const html = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>The Passive-Income Number — en · CHAPTER 4 · rung four, and the number that is a warning</title>

<!-- ===========================================================================
     CHAPTER 4 — the hero corpus, then the trap: an advertised yield is a promise
     about the tap, and the reason it is a warning is that the tank shrank.
     Thirteen cuts, ${ROOT}s, s40-s52.

     GENERATED by build.mjs from ../passive-income-number-en/assets/voice/
     timing.json. Do not hand-edit a timing here: every data-start /
     data-duration / data-framings, the S and D maps, the thirteen <audio> rows
     and the root duration are computed from that one file and asserted against
     the shipped cut's GAPS — a re-time is exactly what produces a correct total
     with every internal cut drifted. Design lives in build.mjs's SCENES table.

     Chapter offset is ${OFF}s (timing.json's own scene_start for line 4.1), so
     this concatenates frame-exact. The LAST scene carries its bare
     scene_duration: a chapter has no successor to cross-dissolve into, and
     tools/cut_assemble.py adds the +0.45 overlap back at fold-in. The cut's
     first SHOVE sits on the s39 -> s40 boundary and therefore belongs to the
     assembly, not to this project.

     Layout: blockframe-9 (run.json architecture, body_class "") under the
     chapter archetype layer. NO RAIL, no chapter title, no scene counter, no
     slide number — format.json chapter_design.rail is false and the viewer must
     never be shown that this video is chapter-based.

     Eleven of thirteen scenes are art-off and ten of those are centred. Rule 8
     retires the drawn layer wherever the photograph already carries the beat,
     and .centred then re-centres the stack so the archetype's empty side is not
     a hole. Three scenes are NOT centred and each has something real on the
     other side: 4.6's chip cascade in archetype C's left column against the
     photographed phone on the right, 4.7's drawn TANK, and 4.10's drawn
     yield-fraction.

     Every scene carries has-photo and a real full-bleed .bg under the LOCKED
     grade. No per-scene brightness override anywhere: photo_free_scene_ratio is
     0 and the photograph is the only variable there is. Three scenes set a
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

/* ===========================================================================
   artOp — THE DRAWN LAYER'S ENTRANCE AND ITS RESTING LEVEL, IN ONE TWEEN.
   ⚠ NOT a redefinition of motion.js's fade(). It is the thing fade() cannot do
   on a \`.has-photo\` scene, and this build shipped the proof: chapter-design.css
   sets \`.has-photo .art { opacity: ... !important }\`, and \`!important\` beats a
   GSAP tween exactly as it beats an authored inline style — so
   \`fade("#s46-art")\` RAN, reported success and changed nothing. The layer stood
   on screen from frame 0 instead of arriving, in a render every checker passed.
   The stylesheet was fixed at the source on 2026-08-12 (the resting value is
   now \`var(--art-op, .30)\`, so the \`!important\` is on the declaration and not
   on the value); driving it needs a tween on the VARIABLE, on the \`.art\`
   ELEMENT itself — a value inherited from the scene loses to the class rule.
   motion.js has no helper that writes a custom property, and adding one is an
   edit to tools/scaffold, not something a build improvises, so this is two
   lines here and a gap named in the log.
   The end value is ${ART_OP}, not \`.art-forward\`'s .52 — see ART_OP. */
function artOp(sel, at, dur) {
  tl.fromTo(sel, { "--art-op": 0 },
    { "--art-op": ${ART_OP}, duration: dur == null ? 0.6 : dur, ease: "power1.out" }, at);
}

/* Cross-dissolves, one call, before the per-scene cues. NO 'acts' argument: the
   cut's two shoves are s39 -> s40 and s58 -> s59 (§12) and both are chapter
   BOUNDARIES from this project's point of view. s40's dissolve is against the
   incoming chapter boundary and is correct here; in the assembled cut
   tools/cut_assemble.py makes that joint the shove. */
sceneTransitions(IDS, S);

/* THE PHOTOGRAPH CARRIES THE MOTION. Direction alternates, and s41 -> s42 is
   THE HOLD: one photograph (s42.jpg is a derived crop of s41's source), one
   chained push, 1.00 -> 1.08 -> 1.16, so the second scene picks up exactly where
   the first ended and the formula completes across a single unbroken shot. The
   pair is in the cut's cues-tables.json "holds", so no transition sounds at the
   joint. Built this way the FIRST time, per the ch1 carry-forward — s3/s4 cost
   three rounds by being built as two files dissolving. */
${kenJs}

/* THE TYPE — cue ladder variant A (storyboard §5) on the statement scenes:
   kicker +0.30, statement +1.10, then the foot at +1.90. Fixed offsets, constant
   whatever a clip's length; every gap is 0.80s and the photograph is already up
   at +0.00, so first_cue_by_seconds (0.5) is met by the kicker. */
${sc.map((s) => `rise("#${s.id}-kick", S.${s.id} + 0.30, 0.7, 14);`).join("\n")}
${sc.filter((s) => s.stmt && !s.verdict).map((s) => `rise("#${s.id}-stmt", S.${s.id} + 1.10, 0.7, 18);`).join("\n")}

/* 4.13 · THE VERDICT SLAM. §2: the five verdict scenes take pop() (back.out(1.7))
   on their stmt instead of rise(). That IS the slam — it needs no .stamp pill
   and no new copy, and it is what makes the "stamp" SFX legal here. */
${sc.filter((s) => s.verdict).map((s) => `pop("#${s.id}-stmt", S.${s.id} + 1.10, 0.6);`).join("\n")}

/* 4.3 · THE FUSED RATE. §4's second form: the rate token lives as an inline span
   inside the focal and takes a pulse at +1.90 fixed, so the corpus and its
   assumption are one sentence rather than a figure with a caption under it.
   MEASURED for the record though the cue is fixed: "4%" is spoken at 1.800s into
   the clip = scene +2.05, so the pulse lands 0.15s ahead of its own word. */
${sc.filter((s) => s.rateSpan).map((s) => `pulse("#${s.id}-rate", S.${s.id} + 1.90, 1.08);`).join("\n")}

/* THE FIGURE SCENES — cue ladder variant B: kicker +0.30, then the rate (or the
   sub, or where there is neither, the foot) at +1.10, then the number ANCHORED
   on its own spoken word with a +1.90 floor, then the foot at num + 0.80 if the
   foot did not take cue 2. The rate is on screen BEFORE the corpus lands: the
   assumption is up first and the number arrives into it (§4).

   EVERY ANCHOR IS MEASURED, not interpolated. §5 gives character-offset
   fractions as a FALLBACK and says fin-build resolves each against
   faster-whisper WORD timings. Run on this cut's own clips (base.en, word
   timestamps), the figure's first spoken word starts at:
     4.1  "$5"    0.000s into the clip -> scene +0.25  -> FLOORED to +1.90
     4.2  "$1.5"  4.700s               -> scene +4.95  (§5's fallback said 5.18)
     4.11 "13"    2.800s               -> scene +3.05  (no fallback published)
   Clips start at scene +0.25 (MEDIUM lead_in_seconds), which is the +0.25 in
   each figure above. 4.1 is FLOORED and it is declared: the line opens ON the
   figure, which is before cue 2 has put the provenance on screen, and §5's floor
   exists for exactly that case — the number lands 1.65s after its word rather
   than on top of its own foot.

   countUp is for MONEY. 13.84% takes a bare pop(): countUp rounds with
   Math.round, so counting to 13.84 would settle on "14%" — a different figure
   from the one the foot cites. */
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

/* 4.6 · THE CASCADE, SPEECH-ANCHORED. Three separate pop() calls at three
   MEASURED word onsets — NOT popEach at a fixed offset, which is what put hi
   ch1's s6 cascade 0.20s BEFORE its first noun and left 5.07s of dead air
   (owed.cascade_offsets_ignore_the_voice). "10" is spoken at 2.420s into the
   clip, "12" at 3.320 and "shortcut" at 5.060 (+0.25 lead-in). The onsets are
   0.90 and 1.74 apart, which is the shape of this sentence rather than a
   template's 0.6. cues.py reads this form and emits one chip per call at that
   call's own time. */
${sc.filter((s) => s.chips).map((s) => chipList(s)
  .map((_c, k) => `pop("#${s.id}-c${k + 1}", S.${s.id} + ${s.chipAt[k].toFixed(2)}, 0.45);`)
  .join("\n")).join("\n")}

/* 4.7 · THE TANK. The band lifts first so the mechanism has darkened ground to
   read against (rule 9 — never the photograph), then the vessel, then the tap
   opens WIDER on "12%" and the level drops. MEASURED, for the record: "tank" is
   spoken at 0.520s into the clip (scene +0.77) and "12%" at 1.520 (scene +1.77),
   so the stream widens on its own word. The upper slice of the water EXITS
   rather than the level sliding: a slide down a fixed vessel invites the eye to
   read a distance, and THE LEVEL IS DECORATIVE, NEVER A MEASUREMENT. Assembled
   by +2.95 on a 4.744s scene, inside chapter_design's "about +3.3", so the
   contact sheet shows a finished mechanism.
   ⚠ MISSING HELPER, declared rather than improvised around: motion.js has span()
   (scaleX) and no scaleY equivalent, so a genuinely sliding level is not
   expressible with the shipped vocabulary. The exit/fade construction is the
   nearest thing that exists AND it is the better reading here, so nothing was
   added to the system for it — but a spanY() is the honest gap. */
fade("#s46-band", S.s46 + 0.90, 0.50);
artOp("#s46-art", S.s46 + 1.00, 0.60);
fade("#s46-stream", S.s46 + 1.85, 0.45);
span("#s46-stream", S.s46 + 1.85, 0.70, 1, 2.4);
exit("#s46-lvlx", S.s46 + 2.45, 0.50);

/* 4.10 · THE YIELD FRACTION. The band, then the fraction, then the price HALVES
   and the yield DOUBLES on the same cue — simultaneity is the assertion, because
   the line is that the payout did not move. The numerator never animates at all.
   The quotient takes a pulse when it lands: §7 declares this scene's cue is
   "tick", and a beat on the element that just changed is what makes that cue
   derivable from a real motion call rather than declared in a table. Assembled
   by +3.00 on a 7.383s scene. */
fade("#s49-band", S.s49 + 0.90, 0.50);
artOp("#s49-art", S.s49 + 1.30, 0.60);
fade("#s49-al1, #s49-al2, #s49-al3", S.s49 + 1.30, 0.60);
span("#s49-den", S.s49 + 2.10, 0.90, 1, ${FALL});
span("#s49-quo", S.s49 + 2.10, 0.90, 1, ${RISE});
pulse("#s49-quo", S.s49 + 3.00, 1.06);

window.__timelines = window.__timelines || {};  /* the LINTER reads this file, not motion.js */
register();                                    /* -> window.__timelines["main"] */
</script>

<script>
/* ===========================================================================
   THE RATE ASSERTS — run.json.constraints, mechanised. Carried forward VERBATIM
   from chapters 2 and 3, including the third BILL branch, because a per-chapter
   copy that drifts is worse than no assert: tools/check_vo_frame.py reads RATE
   and MARKER back out of THIS block, so the frame-side and the VO-side checks
   can never disagree about what a rate is.

   (1) withdrawal_rate_on_screen: "Every corpus figure must carry its assumed
       withdrawal/return rate ON SCREEN in the same frame as the number. A number
       without its assumption visible is a fabricated promise."
       LIVE HERE on s41 (\$1,500,000, a first-class 40px #s41-rate .sub reading
       "AT A 4.0% WITHDRAWAL RATE") and on s42, where the SAME corpus is restated
       and the rate is the inline #s42-rate span inside the focal.

   (2) derived_income_carries_assumption (EXTENDED 2026-08-07): a DERIVED INCOME
       figure — the corpus's own OUTPUT — carries the rate in frame or an explicit
       ILLUSTRATIVE marker. LIVE HERE TWICE. s42 renders "\$5,000 a month" beside
       the rate span, so the rate branch covers it. s40 renders "\$5,000 A MONTH"
       with NO rate, deliberately: it is a CHOSEN INPUT, not a result, and §4
       routes it to the explicit-marker branch — its foot states on screen that
       the figure was picked below the BLS average, so "BLS" is the marker and it
       is in the same frame as the number.

   (3) THE BILL BRANCH, added in ch2. (1) is deliberately narrow — it fires only
       on the eight CORPUS tokens, so a published numerator could render
       completely bare and pass. \$6,545 in s40's foot is exactly that shape.
       "Must not demand a rate" is not "may be bare": a BILL has to carry, in
       frame, either a rate, the published provenance, or its own derivation, and
       s40's BLS provenance is what pays for it. The point of the branch is that a
       density pass which drops a foot line cannot silently make one of them a
       bare number — and on s40 that same foot is ALSO what (2) depends on, so
       one deletion would fire two branches.

   Throwing is the point: "hyperframes check"'s runtime pass fails on an uncaught
   page error, and a silent console.warn is what let this ship twice.

   ⚠ THIS ASSERT IS FRAME-ONLY BY CONSTRUCTION. It reads rendered text, so it
   cannot see a VO line that SPEAKS a figure over a bare frame
   (owed.derived_income_assert_is_frame_only). That half is
   tools/check_vo_frame.py, run against this file at build:
     python3 tools/check_vo_frame.py passive-income-number --cut en --chapter 4
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
 * storyboard §2 and already carrying this chapter's three declarations: the
 * s41/s42 HOLD (no transition at the joint) and the DRY scenes s40, s42 and s50.
 * Nothing in that file was touched by this build.
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
  `${s.ctr ? " centred" : ""} ${s.art}  load ${load(s)}${s.size ? "  focal " + s.size : ""}` +
  `${s.numAt ? "  num +" + s.numAt.toFixed(2) : ""}`));
