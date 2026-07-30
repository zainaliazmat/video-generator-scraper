# 02 — Script writing audit: @cashguruguides + @moneymavens101

Scope: the words only (hook, structure, retention, delivery, CTA, two-market rewrite).
Read in full: `good-debt-vs-bad-debt/script-{hi,en}.md`, `credit-history/script-{hi,en}.md`,
`needs-vs-wants/script-hi.md`; lexical sweep across all 8 vault finance scripts;
`long_form_scripting.md`, `us-english-script-style.md`, `haryanvi-hindi-script-style.md`,
`.claude/agents/fin-script.md`, `templates/script-template.md`, `tools/format.json`.

Every claim tagged `FACT` (verifiable in-repo, a public number, or a cited source) or
`UNVALIDATED` (plausible but untested — **no analytics exist for any video**).

---

## 0. The one-paragraph verdict

The **hooks are the strongest part of these scripts** and have measurably improved across
the six pairs. Everything after second 19 is a template — and not merely a structural one:
it is **lexically identical across topics and across both channels.** The `-en` cut is a
genuine *fact* rewrite and a *script* translation: the numbers, institutions and statutes
are correctly re-sourced per market, while the sentences, the beat order, the analogies and
in several scenes the byte-for-byte on-screen copy are shared. The two highest-leverage
edits (kill the roadmap, kill the recap) cost one prompt file and one JSON key.

---

## 1. Evidence: the template is lexical, not just structural

This is the finding I did not expect and it is the most damaging one, because it needs no
analytics to prove.

**FACT** — sentence-frame reuse across the 8 vault finance scripts
(`vault/videos/{needs-vs-wants,pay-yourself-first,good-debt-vs-bad-debt,credit-history}/script-{hi,en}.md`):

| Beat | Verbatim string | Hit rate |
|---|---|---|
| s2 roadmap, en | `Four things:` — as the literal opening two words | **4 / 4** |
| s2 roadmap, hi | `चार बातें —` (needs-vs-wants: `चार चीज़ें —`) | **4 / 4** |
| s8 on-screen | `DO THIS TODAY` | **8 / 8**, twice per file |
| s9 recap, en | `Then don't say nobody warned you.` | **4 / 4** |
| s9 recap, en | `For money talk this straight — hit subscribe.` | 3 / 4 |
| s9 recap, hi | `तो बात सीधी है —` / `तो सीधी बात —` | **4 / 4** |
| s1 hook, en | `Quick question —` as the literal opening | 2 / 4 (the *earlier* two) |

A viewer who watches two videos on either channel hears the **same sentence-opening at
~0:19 and the same sentence-closing at ~2:50**, on a different topic. That is not a
structure you feel; it is a structure you can transcribe.

**FACT** — the sign-off phrase is deliberate: `us-english-script-style.md` says *"Keep the
mock-scold sign-off beat ('then don't say nobody warned you') — it's channel signature."*
A signature phrase is fine. A signature phrase inside an identical recap, inside an
identical 9-beat order, inside a 13-second runtime band, is not a signature — it is a
fingerprint.

**FACT** — the vault has already counted the structural half of this three times and
nothing changed (`vault/index.md:46`, `videos/credit-history/index.md:180–224`,
`videos/good-debt-vs-bad-debt/index.md:84–97`). `credit-history/index.md` diagnoses it
correctly: `tier` is chosen in `run.json` **before** fin-script runs, and the warning is
written into the publish pack, read **at upload, after the artifact exists**.
**The lexical half of the sameness has never been counted at all** — it is not in any
vault note, and it is invisible to a per-video review because it only shows up when you
diff two scripts.

---

## 2. The scripts as scripts

### 2a. Does the first line earn the second?

**Yes — and this is the part that works.** Quoting the two strongest openings verbatim:

> **good-debt-vs-bad-debt / en1:** "On a credit card, the most dangerous words are 'minimum
> payment.' It feels safe. It's a trap. On a six-thousand-dollar balance, the minimum runs
> about a hundred seventy dollars — and a hundred ten of that is pure interest. Only sixty
> dollars comes off what you owe."

Line 1 makes a claim that opens a gap; line 2 is a two-beat escalation
("safe" → "trap") that refuses to resolve it; line 3 resolves it with arithmetic **inside
8 seconds**. That is a textbook curiosity-gap-then-payoff and it obeys the vault's own
§4 three-phase opening. Same craft in:

> **credit-history / en1:** "There's a file on you that you've never read — and it decides
> whether you get a loan, and what interest you pay. The lender reads it before you ever
> walk in."

"before you ever walk in" is the best clause in the corpus — it converts an abstraction
(a credit file) into a scene with an antagonist.

**FACT — the hooks improved over time.** The two earlier pairs open with a question
(`Quick question — be honest.` / `एक सीधा सवाल —`); the two later pairs open with a
declarative claim. `long_form_scripting.md` §4 lists "clichés (*have you ever
wondered…*)" among hook mistakes and calls the open-loop hook "NOT an announcement." The
question-openers are the weaker form and the pipeline drifted away from them unprompted.
**Credit the pipeline for this; it is the only beat that has evolved.**

### 2b. Weakest lines, verbatim

> **good-debt-vs-bad-debt / en2 (roadmap):** "Four things: what debt really is, good debt
> versus bad debt, how the minimum works, and how interest compounds against you. Then one
> move to make today."

The weakest line shipped. It is `long_form_scripting.md`'s own banned construction —
*"in this video we're going to talk about…"* — reformatted as chips. It contains zero
facts, zero tension and zero new information, and it lands at **0:20–0:32 of a 2:59
video**. See §3.

> **good-debt-vs-bad-debt / en6 (the action beat):** "The day you add even a little on top,
> years of interest start falling away."

This is the *answer to the video's question* and it is the **only unquantified beat in a
video built entirely on quantification.** The script's own margin note explains why —
`facts-staging` supplied no build-locked figure for the minimum-plus-$20 case, so the
effect was kept qualitative. The discipline is admirable; the outcome is that the payoff
is vaguer than the problem. **UNVALIDATED** that this costs retention, **FACT** that it
inverts the video's own rhetorical contract: every scare is precise, the remedy is not.

> **good-debt-vs-bad-debt / en4 (the concept beat):** "Good debt buys what grows in value
> or income: a degree, a skill, a business. […] Bad debt just buys consumption — clothes,
> gadgets, a vacation."

Definition-list prose. Nobody in the target audience learns anything here. It occupies
0:52–1:15 — **13% of runtime** — restating the title. `long_form_scripting.md` §2 names
this exact failure: *"the filler middle (the #1 cause of mid-video drop-off)."*

> **credit-history / hi s7:** "तीस लाख के बीस साल के लोन पर उसका मतलब — हर महीने क़रीब
> पंद्रह सौ रुपये ज़्यादा"

The script's own margin note concedes the mismatch: a ₹30 lakh home loan aimed at a
₹30,000/month audience. The note argues the gap *is* the argument. It is a defensible
call, but it means the money beat of that cut is priced in a life the viewer does not
have yet — **UNVALIDATED**, and worth an A/B once analytics exist.

**Best non-hook line in the corpus, for contrast:**

> **credit-history / en5:** "And here's the part people get wrong — the clock doesn't start
> when you finally pay it off. It starts at the original missed payment."

This is the only beat in six pairs that **corrects a belief the viewer already holds**
rather than filling a blank. It has a villain (the misconception), a reversal, and a
consequence. It is also the beat with no Hindi counterpart — because it came from a fact,
not from the template. That is the whole lesson: *the good beats are the ones the template
did not generate.*

### 2c. Where I would click away — with real timecodes

Rendered timeline for `good-debt-vs-bad-debt-en` (**FACT** — script's own char budget plus
the 0.4s lead-in / 1.0s tail from `format.json`; sums to 179s, and the shipped render is
2:59 = 179s):

| Scene | Window | State |
|---|---|---|
| en1 hook | 0:00–0:21 | strong |
| **en2 roadmap** | **0:21–0:32** | **← click-away risk #1** |
| en3 concept (renting money) | 0:32–0:53 | strongest body beat |
| **en4 good vs bad** | **0:53–1:16** | **← click-away risk #2 (the real one)** |
| en5 mechanism | 1:16–1:39 | third restatement of "interest is paid first" |
| en6 action | 1:39–1:57 | the answer, unquantified |
| en7 the math (peak) | 1:57–2:26 | **peak at 65–81% — correctly placed** |
| en8 do-this-today | 2:26–2:43 | no new information |
| en9 recap | 2:43–2:59 | no new information |

**At 0:45** — yes, there is a reason to stay: the "debt is renting money" analogy is
genuinely good and is landing.
**At 1:30** — marginal. The mechanism scene is the third statement of the same idea the
hook already proved with arithmetic.
**At 2:30** — **no.** The video's last new fact lands at 2:26. The final 33 seconds
(18% of runtime) are an action beat and a recap, both of which restate material that is
under 90 seconds old.

**The structural diagnosis:** the hook spends the video's biggest shock (the month-1 split)
at 0:10, and en7 spends the same argument again with bigger arithmetic at 1:57. **Between
0:32 and 1:57 — 79 seconds, 44% of the video — there is nothing a viewer could not have
predicted from the hook.** The peak placement is right; the material between hook and peak
is not new, it is elaboration.

**Credit where due:** the peak lands at 65–81% of runtime, which is exactly what
`long_form_scripting.md` §6 prescribes ("plant a reward at ~70%"). That was designed, not
lucky.

**FACT — a rule the pipeline follows nowhere:** §6 also mandates *"end by opening a loop the
next video closes."* **Zero of eight scripts contains a next-video loop.** Every one ends
on a 4-chip recap and `SUBSCRIBE`. Both channels ship a paired cut of the same topic and a
back catalogue of five, and no script points at any of it. That is a free session-time
mechanism the pipeline's own canonical skill demands and has never once executed.

---

## 3. The 9-line straitjacket, and the roadmap specifically

### 3a. Is the skeleton helping?

It was a scaffold and it is now a cage. Distinguish two things:

- **What the 9 beats buy (real):** a machine-checkable contract. Nine VO lines → nine TTS
  clips → nine scenes, 1:1, with a char budget the audit stage can assert against. That is
  why the pipeline is reliable, and it should not be thrown away.
- **What the 9 beats cost:** the *order* is fixed, so every topic — a spending habit, a
  savings habit, a debt instrument, a credit bureau — is forced into
  `hook → roadmap → concept → contrast → mechanism → action → math → do-today → recap`.
  Credit history is not a contrast topic and got a contrast beat anyway. Pay-yourself-first
  is a behaviour topic and got a "the math" beat anyway.

**The fix is not to abandon 9 beats. It is to separate the count from the order.** The
count is what the build needs; the order is what the viewer feels. `fin-script.md` currently
welds them together in one line:

> `.claude/agents/fin-script.md:29–31` — *"**SHORT** — the proven 9-segment blockframe:
> hook · roadmap · concept · rule · audit · action · the math · do-this-today · recap+CTA"*

**FACT — the entire architecture lives in two places and nowhere else.** I grepped every
agent and every tool:

- `tools/format.json:42–43` → `"architecture": "blockframe-9"`, `"lines": 9`
- `.claude/agents/fin-script.md:29–31` → the beat order, in prose

No `.py`, no other agent, and no command file hardcodes 9. **This means changing the
architecture is a JSON value plus a paragraph of prose — not a pipeline rewrite.** Every
cost estimate below rests on this.

### 3b. The roadmap line — yes, it is costing you, and here is the specific reason

**FACT — placement.** The roadmap occupies **0:20–0:32** (hi) / **0:21–0:32** (en) of a
~2:50 video: 10–12s, **6–7% of total runtime.**

**FACT — 2026 external evidence puts that window at the steepest part of the curve.**
Current retention writing converges on a three-phase opening (pattern interrupt 0–5s,
specific payoff promise 5–15s, commitment hook 15–30s), with the steepest drop between
seconds **10 and 20** and an inflection around second 15; 30–40% of viewers are typically
gone by 0:30, and named hook failure modes include *"front-loading context before the
value promise"* and *"using the same hook formula for every video regardless of topic."*
([PrePublish](https://prepublish.ai/guides/first-30-seconds),
[Miraflow](https://miraflow.ai/blog/youtube-video-hooks-2026-save-first-30-seconds),
[Overseeros](https://www.overseeros.com/blog/youtube-retention-architecture-2026),
[Artiphik](https://artiphik.com/blog/the-first-10-seconds-retention-playbook))
Note these are creator-tier sources, not YouTube documentation — the vault's own §13 caveat
about creator-reported benchmarks applies and I am not overriding it.

**FACT — the pipeline's own canonical skill forbids the beat its own tier mandates.**
`long_form_scripting.md` §4 lists among "hook mistakes that burn attention (cut these)":
*"'in this video we're going to talk about…'"* and *">10s of slow context"*. The roadmap
scene is both, simultaneously, rendered as chips. §6 adds *"no slow intro (~33% drop in the
first 30s)"*. **`fin-script.md` reads `long_form_scripting.md` on every run and then writes
the beat that file bans.** This is an internal contradiction in the repo, not an opinion.

**FACT — the roadmap is the only scene with nothing to show.** Both scripts say so in
their own visual notes: *"bg keyword (calmest — roadmap rest beat, still carries a photo
per the every-frame-has-image rule)"*. Every other scene has a fact, a number or a contrast
driving its visual. This one has a photo because a rule requires a photo.

**UNVALIDATED** — that removing it lifts retention. There is no curve. What is *not*
unvalidated is that it burns 6–7% of runtime restating the title inside the window every
current source names as the most fragile, in a form the repo's own skill file bans.

### 3c. What replaces it

Do **not** delete the scene. Deleting changes the scene count, which touches
`format.json.tiers.short.lines`, the audit's char-budget assertion and every downstream
1:1 assumption. **Keep slot 2; change its job.** Zero build cost — one VO paragraph and one
on-screen block.

**Replacement spec (drop-in for `fin-script.md`):** slot 2 becomes **STAKES + OPEN LOOP**,
not a table of contents. It must contain (a) one number the hook did not use, (b) the cost
of *not* knowing it, (c) an explicitly unresolved question. It may not enumerate the video's
sections.

Worked example, good-debt-vs-bad-debt-en — replacing *"Four things: what debt really is,
good debt versus bad debt…"*:

> "Keep paying that hundred seventy a month and you clear this card in two hundred fifteen
> months. Not two hundred fifteen dollars — months. Eighteen years, on six thousand. There
> is one line on your statement that decides whether that's your number, and it isn't the
> interest rate."

Same slot, same ~11s, same nine scenes. It moves a real figure forward, converts the beat
from announcement to gap, and hands scene 3 a loop to close instead of a topic to
introduce. (`215 months` is already build-locked in `script-en.md` en7.)

**A second, free win in the same edit:** slot 9 currently recaps. In a sub-3-minute video
nobody has forgotten four points delivered 40 seconds ago. Convert slot 9 from
*recap + subscribe* to **payoff-restated-once + the loop into the paired/next video +
subscribe**. `long_form_scripting.md` §7 (peak-end rule) says end on a peak; a summary is
the flattest possible ending. This is the same edit — one prose paragraph in
`fin-script.md` — and it closes the "zero next-video loops in eight scripts" gap in §2c.

---

## 4. Three alternative architectures a code pipeline can execute

All three costed against the §3a finding: **architecture = `format.json` value + prose in
`fin-script.md`.** Where I say "cheap", I mean I checked that nothing else hardcodes it.

### A. `blockframe-9-v2` — same machine, different beat order (CHEAP)

The minimum viable de-templating. Same 9 lines, same 1:1 mapping, same char budget, same
build, same audit assertions.

| # | Current | Proposed |
|---|---|---|
| 1 | hook | hook *(unchanged — it works)* |
| 2 | **roadmap** | **stakes + open loop** (§3c) |
| 3 | concept | **the wrong belief** — what the viewer currently thinks, in their words |
| 4 | contrast | **the correction + why the wrong belief is reasonable** |
| 5 | mechanism | mechanism |
| 6 | action | **the honest limit** — where this advice stops working *(new; nobody in the niche does this)* |
| 7 | the math | the math *(peak stays at ~70% — it is correctly placed)* |
| 8 | do-today | do-today, **with a number attached** |
| 9 | **recap** | **payoff + loop into the next video** |

- **Runtime:** unchanged, ~2:45–3:15. **Fixes the beat order, not the runtime band** — so
  pair it with a deliberate runtime change or the 13-second band survives.
- **Suits:** every topic already shipped. Strongest on belief-correction topics
  (credit-history, good-debt) where beat 3/4 has real material.
- **Cost vs blockframe-9: cheapest possible.** `fin-script.md` §"Format by tier" prose +
  the `architecture` string in `format.json`. No Python, no new tier, no build change.
  Beat 6 ("the honest limit") is the only one needing a new input from `fin-facts` — a
  sourced caveat rather than a sourced number.
- **UNVALIDATED:** that any of this outperforms. **FACT:** it ends the verbatim
  sentence-frame repetition documented in §1.

### B. `micro-argument` — one number, 60–90s (CHEAP)

| Beat | Target |
|---|---|
| 1 the number, stated cold, no context | 0:00–0:05 |
| 2 what it is the price of | 0:05–0:15 |
| 3 the mechanism, one sentence | 0:15–0:35 |
| 4 the one move, quantified | 0:35–0:55 |
| 5 the loop into the full video on the same topic | 0:55–1:15 |

- **Runtime:** 60–90s. **Already legal:** `format.json.tiers.short.range_seconds` is
  `[60, 300]` — no new tier needed, only a new `architecture` string and a
  `default_target_seconds` override.
- **Suits:** any topic with one hero number — `needs-vs-wants` (₹24,564),
  `good-debt-vs-bad-debt` (₹88,614 / $9,506), `credit-history` (36 months / 7 years).
  It is also the natural **companion** format: a micro cut that loops into the long cut.
- **Cost: cheap and it is the fastest way out of the 2:46–2:59 band** — 75s is 100+ seconds
  outside it, which no amount of beat reshuffling achieves. 5 lines = 5 TTS calls and
  ~5 images, so it is *cheaper per unit* than what ships now.
- **Cost you must accept:** no mid-roll, and less watch time per view. This is a
  differentiation and catalogue-depth play, not a revenue play.

### C. `chapter-teardown` — 8:30–9:30, mid-roll eligible (MEDIUM — and cheaper than it looks)

**FACT — the long-form build already exists and has already shipped once.**
`format.json.tiers.medium` = 510s, `"architecture": "per-line-chapters"`, reference
`studio/videos/firaun-ka-anjaam/build.py` — **648 lines, present on disk.** It is the
Firaun architecture: single-sentence VO lines, one line = one clip = one scene, with one
image held across consecutive lines as a single continuous zoom. `fin-script.md` §"Format
by tier" *already documents it* and says *"None of the 9-segment constants apply."*
**The finance channels have never used a tier the pipeline already supports.**

Beat sheet (5 chapters; build/proof/re-render each chapter standalone, per the
chapter-wise production rule, then concat):

| Ch | Window | Job |
|---|---|---|
| 1 | 0:00–1:00 | **Cold open + stakes.** One concrete, explicitly-labelled illustrative situation and the number it ends at. Loop: "the mistake wasn't the obvious one." |
| 2 | 1:00–2:40 | **The mechanism, slowly** — the arithmetic done step by step on screen. *This is the only thing a 3-minute cut cannot do, and therefore the actual reason to make a long one.* |
| 3 | 2:40–4:30 | **Three ways people get this wrong** — three mini-loops, each with its own number. |
| — | **~5:00** | **A designed beat break for the mid-roll** — a chapter boundary, so an ad never lands mid-sentence. |
| 4 | 4:30–6:30 | **The counter-case / the honest limit** — when the standard advice is wrong. The reward beat, teased in Ch1. Lands at ~70%. |
| 5 | 6:30–8:45 | **The plan**, numbered and executable, then the loop into the paired cut. |

- **Runtime target 8:30–9:30.** **FACT:** mid-rolls require **8:00 minimum** — 7:59 cannot
  run them, 8:00 can; mid-rolls are reported to lift RPM meaningfully over pre-roll-only.
  ([vidIQ](https://vidiq.com/blog/post/youtube-8-minute-mid-roll-ads/),
  [FluxNote](https://fluxnote.io/guides/youtube-mid-roll-ads-minimum-video-length-8-minutes-2026))
  Note `tiers.medium.target_seconds` is **510s = 8:30**, which already clears the gate with
  30 seconds of margin. Whoever set that number chose it deliberately.
- **Suits:** topics with a mechanism worth 100 seconds of arithmetic —
  `good-debt-vs-bad-debt` (amortization), `credit-history` (score → rate → total cost),
  `50-30-20-rule` (a full budget built live). Do **not** put `needs-vs-wants` here; it has
  ~90 seconds of real content.
- **Cost: the build is cheap, the inputs are not.** Honest breakdown:
  - *Build code:* already written and proven. **~zero.**
  - *TTS characters:* ~8,100 (en @ 15 c/s) vs ~2,500 = **3.2×**. Billed per character.
  - *Pipeline call budget:* `.claude/commands/finance-video.md:70` sets
    `max_elevenlabs_calls: 30` **shared across both cuts of a run**. A per-line script is
    ~120–180 lines *per cut*. **This is the binding constraint and it is a config
    constant, not a vendor limit** — but per-line-chapters cannot run until it is raised
    or lines are batched into fewer calls. This is the single blocking item for option C.
  - *Images:* scales with visual beats, not lines (one still held across consecutive lines).
    ~50–60 vs ~20 = **~3×** — against a no-repeat md5 ledger, so sourcing effort is real.
  - *Facts:* ~4× the sourced claims. `fin-facts` is already the slowest stage and
    `library.db` has **no finance lane at all** (`credit-history/index.md:226` — 1,124 rows,
    zero finance matches, fin-research rescued twice). **This, not the build, is what makes
    option C expensive.**

**Recommended sequencing:** A on the next pair (cheap, immediate, unblocks nothing else),
B as the companion cut on the pair after (breaks the runtime band decisively), C once the
call-budget constant is raised and one finance-lane scrape exists.

---

## 5. The two-market rewrite — is the `-en` cut a real US rewrite?

**Verdict: a genuine rewrite at the fact layer, a translation at the script layer.**

### 5a. What is genuinely rewritten — this part is done well, and should be said

**FACT.** The two cuts do not share a number, an institution or a mechanism:

| Layer | hi | en |
|---|---|---|
| Minimum-payment rule | 5% of total due, ₹100 floor (RBI + issuer MITC) | 1% of balance + interest, $35 floor (Chase/Capital One, Reg Z) |
| APR | ~40% | ~22% (Fed G.19) |
| Balance | ₹50,000 | $6,000 |
| Credit score | CIBIL, 300–900, **no published weights** | FICO, 300–850, **35% / 30% published** |
| Negative-mark window | **36 months** (CIBIL) | **7 years** (FCRA §1681c(a)) |
| Money beat | ₹30 lakh / 20-yr home loan | $25,000 / 72-mo used car |

Both files carry explicit cross-contamination guards, and `credit-history` gets the hard
case exactly right: the two markets have **structurally different answers to the hero
question**, and the pipeline refused to import either. `fin-facts` also rejected the
"CICRA 2005 = 7-year auto-delete" claim asserted by nine Indian blogs — the US rule wearing
an Indian costume. **That is real, expensive, correct work and it is the strongest thing
this pipeline does.** Nothing below diminishes it.

### 5b. What is not rewritten — the script

**FACT — clause-for-clause isomorphism.** Same topic, same beat, no shared numbers:

> **hi s3:** "पहली बात — कर्ज़ यानी पैसा किराए पर लेना। जो ब्याज देते हैं, वो उस पैसे का
> किराया है। किराया देना हमेशा ग़लत नहीं — पर देखिए किस चीज़ के लिए। किराए का औज़ार अगर
> कमाई करा दे, तो किराया वसूल। पर बाहर के खाने या सेल की ख़रीदारी का किराया? चीज़ कल
> ख़त्म, किराया महीनों चलेगा।"

> **en3:** "First — what debt really is. Debt is renting money, and the interest is the
> rent. Renting money isn't always wrong — it depends what you rent it for. Rent a tool
> that earns, and the rent pays for itself. Rent it for a dinner or a sale, and it's gone
> by morning — the rent runs for years."

Six clauses, same six moves, same order, same analogy, same closing antithesis
("चीज़ कल ख़त्म, किराया महीनों चलेगा" ≡ "gone by morning — the rent runs for years").
Same pattern in s1 (four sentences, same four moves) and s9.

**FACT — the on-screen copy is byte-identical in multiple scenes.** On-screen text is
English in *both* cuts, so this is directly comparable. Identical strings across
`script-hi.md` and `script-en.md`:

- s2 chips: `WHAT DEBT REALLY IS` · `GOOD vs BAD DEBT` · `HOW THE MINIMUM WORKS` ·
  `COMPOUNDS AGAINST YOU`
- s3: `DEBT =` + `RENTING MONEY`, `Interest is the rent`
- s5: `INTEREST ON INTEREST`, `COMPOUNDING — for you when you invest, against you on a card`
- s6: `PAY MORE THAN THE` + `MINIMUM`
- s9 recap chips: `DEBT = RENTED MONEY` · `GOOD GROWS, BAD DRAINS`
- credit-history s2 chips: `WHAT THE REPORT IS` · `WHAT BUILDS IT` · `WHAT DESTROYS IT` ·
  `WHY IT MATTERS EARLY`; s3: `THE REPORT = the record` → `THE SCORE = the summary`

**A viewer who watches both cuts reads the same on-screen words.** Both `script-hi.md` and
`script-en.md` carry a bold callout — *"US REWRITE, NOT A TRANSLATION"* — directly above
text that shares its on-screen copy with the other cut. The claim is true of the facts and
false of the script, and the callout does not distinguish them.

**Why this happens is in the agent prompt, and it is fixable in one sentence.**
`fin-script.md:42–44`:

> *"**The `-en` cut is a US rewrite, not a translation** — $ amounts, US institutions […],
> US shocks, US b-roll. **Read the Hindi script only for structure.**"*

Every named item is a *noun*. "Read the Hindi script only for structure" is exactly what
was done — and structure, at 9 fixed beats, *is* the script. The fix: define what may
transfer (the thesis, the hero number's *role*, the beat count) and what may not (sentence
order, analogies, on-screen copy, the recap chips), and require the two cuts to use
**different analogies**. `credit-history` proves the pipeline can do this when the facts
force it — en5's "the clock doesn't start when you pay it off" has no Hindi twin and is the
best body beat in the corpus.

### 5c. Are the Hindi scripts written the way Hindi finance YouTube talks?

**Partly. The syntax is fine; the lexicon is inconsistent and the register is too formal.**

**FACT — the syntax is native, not calqued.** *"चीज़ कल ख़त्म, किराया महीनों चलेगा।"* and
*"एक चूक, और गिनकर छत्तीस महीने।"* are idiomatic verbless Hindi constructions with no
English equivalent structure. This is **not** English-in-Devanagari, and I want to be
precise about that because it is the accusation the brief invited and it is not supported.

**FACT — the lexicon fights the screen.** The VO reaches for Sanskritized/Perso-Arabic
formal vocabulary in exactly the places the on-screen text uses the English term the
audience actually says:

| Concept | VO says | Same scene's on-screen text |
|---|---|---|
| compounding | **चक्रवृद्धि** (Sanskrit, textbook) | `COMPOUNDING` |
| EMI / instalment | **किश्त** | `every EMI, on time` |
| principal | **मूल कर्ज़** (a coinage) | `PRINCIPAL` / `principal` |
| outstanding balance | **बक़ाया** (formal Urdu) | `balance` |

The viewer *hears* a word from a textbook and *reads* the word they use. Real Hindi finance
YouTube — AssetYogi, FinnovationZ and the rest of the lane — runs on **Hinglish**, which is
"perceived as a high prestige variety of spoken Hindi" while unmixed vernacular Hindustani
reads as low-prestige; the register exists specifically to reach small-town viewers who
don't operate in English.
([Wikipedia — Hinglish](https://en.wikipedia.org/wiki/Hinglish),
[bemoneyaware](https://bemoneyaware.com/youtube-india-personalfinance-investing-stocks/))

**FACT — the repo already contains the correct register, in the wrong file.** The Hinglish
*description* for the same video reads:

> *"Credit card par sabse khatarnak shabd: 'minimum payment'. Ye sahulat nahi, ek jaal hai."*

That is the lane's actual voice. The pipeline writes it for the description and abandons it
for the VO. Ship `कंपाउंडिंग` not `चक्रवृद्धि`, `EMI` not `किश्त`, `प्रिंसिपल` not
`मूल कर्ज़` — and add one rule to `fin-script.md`: **if the on-screen text uses the English
term, the VO says the English term too.** It is a one-line rule that eliminates the whole
class.

**Register, more cautiously.** The hi cuts use `आप` with the `-इए` imperative throughout
(कीजिए, समझिए, भरिए, देखिए). That is correct, courteous Hindi and is used by some
channels in the lane. It is also the register of a public-service announcement. Whether the
warmer `करो`/`कर लो` outperforms is **UNVALIDATED** — but note the vault's own
`haryanvi-hindi-script-style.md` prescribes exactly the warmer thing (*"a street-smart elder
telling you the obvious truth you keep ignoring"*), and `fin-script.md:24–25` explicitly
instructs the agent **not** to read it. That was a deliberate creator decision on
2026-07-28 (Standard Hindi, not Haryanvi), so it is not an error — but the *warmth* the
Haryanvi guide describes was thrown out along with the *dialect*, and only the dialect was
the thing being retired.

---

## 6. Three replacement hooks — `good-debt-vs-bad-debt-en` (live: youtu.be/gC2QlQiLqhw)

**Shipped:**

> "On a credit card, the most dangerous words are 'minimum payment.' It feels safe. It's a
> trap. On a six-thousand-dollar balance, the minimum runs about a hundred seventy dollars —
> and a hundred ten of that is pure interest. Only sixty dollars comes off what you owe.
> Today, the actual math."

**What is already right:** the claim-then-escalate-then-arithmetic shape, and the payoff
inside 8s. **What I would change:** (a) *"the most dangerous words are X"* announces that a
claim matters instead of making it; (b) it opens on the *instrument*, not the *viewer*;
(c) *"Today, the actual math"* is a roadmap promise that double-spends the promise the
roadmap scene is about to make again 10 seconds later.

All three below are Gate-2 clean (no persona, no first-person expertise, no product pick),
speak only build-locked figures from `script-en.md`, and run 10–13s at Brian's 15 c/s.

**Hook 1 — loss-framing on compliant behaviour**

> "Six thousand dollars on a credit card. Pay the minimum every month, on time, never miss
> one — and you'll hand the bank nine thousand five hundred dollars in interest. You did
> nothing wrong. That's the trap."

*Principle:* the shock is not "debt is bad" — it is that **doing exactly what you were told
still costs you more than you borrowed.** "never miss one" is the Von Restorff element: it
is the detail the viewer expects to protect them. It also pulls the video's largest number
from 1:57 to 0:00, and leaves "how is that possible?" as an unavoidable open loop, which
is what makes slot 2 replaceable by §3c's stakes beat rather than a table of contents.

**Hook 2 — verifiable second-person arithmetic**

> "Go look at your last card statement. Find the minimum payment. About two-thirds of that
> number never touches what you owe — it's rent. On six thousand dollars, that's a hundred
> ten dollars a month buying you nothing."

*Principle:* **an instruction the viewer can execute in second one, against their own
document.** Verifiability is the strongest available credibility for a faceless, persona-less
channel that is barred from claiming expertise — the statement checks itself. It is also a
Cialdini commitment micro-yes, and it plants "rent" in the hook so scene 3's
"debt is renting money" *closes a loop* instead of introducing a concept cold.

**Hook 3 — contrarian against the video's own title**

> "Good debt, bad debt — forget the categories. There's one line on your statement that
> decides which one you've got, and almost nobody reads it. Get it wrong on six thousand
> dollars and you're paying for it for eighteen years."

*Principle:* **refuse the frame the title sells.** The vault's own publish pack
(`youtube-metadata-en.md`) records that `good debt vs bad debt` is a live US search string
**but that Kiyosaki and Ramsey own it** — so the click arrives with a competitor's framing
pre-loaded. Rejecting the category in line one is the fastest available differentiator on
that SERP, and "one line… almost nobody reads it" is a *closable* Loewenstein gap that the
existing body already answers. Best paired with title option #4.

---

## 7. Contradictions with what the vault currently documents

1. **`long_form_scripting.md` §4/§6 ban the roadmap beat that `fin-script.md` mandates.**
   The banned constructions are *"in this video we're going to talk about…"* and *">10s of
   slow context"*; slot 2 is both. `fin-script.md` reads that skill every run. **FACT.**

2. **§6's "end by opening a loop the next video closes" is executed in 0 of 8 scripts.**
   All eight end on recap + `SUBSCRIBE`. Both channels have five back-catalogue videos and
   a paired cut of the same topic to point at. **FACT.**

3. **The vault documents the sameness as structural; it is also lexical, and that half is
   recorded nowhere.** Three notes count consecutive blockframe-9s. None records that
   `Four things:` opens 4/4 en roadmaps, `Then don't say nobody warned you` closes 4/4 en
   recaps, and `DO THIS TODAY` appears in 8/8 scripts. **FACT.**

4. **"US REWRITE, NOT A TRANSLATION" is asserted in both scripts above on-screen copy that
   is byte-identical between the two cuts.** True of facts, false of script; the callout
   does not distinguish them, and `fin-script.md:44`'s *"read the Hindi script only for
   structure"* is what produces it, because at 9 fixed beats structure *is* the script.
   **FACT.**

5. **`credit-history/index.md` says the control failed because it fires after the artifact
   exists. It also under-costs the fix.** That note frames changing architecture as an open
   decision. Grep says `lines: 9` and `blockframe-9` exist in exactly **two** places —
   `tools/format.json:42–43` and `fin-script.md:29–31` — and nothing in `tools/*.py` or any
   other agent hardcodes 9. **The change is cheaper than the note implies, which strengthens
   the note's own argument.** **FACT.**

6. **`tiers.medium` (510s, per-line-chapters, `firaun-ka-anjaam/build.py`, 648 lines on
   disk) is documented in `format.json` and in `fin-script.md`, and has never been used by
   either finance channel.** The mid-roll unlock is not a build project; it is an unused
   config path with one real blocker — `max_elevenlabs_calls: 30`
   (`.claude/commands/finance-video.md:70`), shared across both cuts, versus ~120–180 lines
   per cut. **FACT.**

7. **`haryanvi-hindi-script-style.md` is excluded by `fin-script.md:24–25`** (correctly —
   creator retired the dialect on 2026-07-28), **but its register guidance went with it.**
   The blunt, warm, mock-scold voice it describes is not dialect-specific and survives in
   the sign-off beat alone. **FACT** that it is excluded; **UNVALIDATED** that reinstating
   the warmth (as Standard Hindi) performs better.

8. **Minor, already adjudicated:** the recommended en title says `$9,506` while the video's
   on-screen figure is `$9,496`. `audit-en.md:19` explicitly accepted the ~$10 spread as
   "estimate rounding, not a defect". Recording it only because the packaging number and the
   on-screen number differ inside one video. **FACT**, low severity.

---

## 8. The five highest-leverage changes

| # | Tag | Change | Why | Cost | Owner |
|---|---|---|---|---|---|
| 1 | UNVALIDATED | Replace slot 2 (roadmap) with **stakes + open loop**; keep 9 scenes | 6–7% of runtime restating the title inside the 10–20s drop window, in a form `long_form_scripting.md` §4 bans | cheap | `.claude/agents/fin-script.md` |
| 2 | FACT | Ban reused sentence frames; require different **analogies** per cut and per topic; forbid identical on-screen copy across hi/en | `Four things:` 4/4, `Then don't say nobody warned you` 4/4, `DO THIS TODAY` 8/8, several on-screen blocks byte-identical between cuts | cheap | `.claude/agents/fin-script.md` |
| 3 | FACT | Convert slot 9 from recap to **payoff + loop into the next video** | §6 mandates a next-video loop; 0/8 scripts have one; §7 peak-end says don't end flat | cheap | `.claude/agents/fin-script.md` |
| 4 | FACT | VO uses the English term whenever the on-screen text does (`कंपाउंडिंग` not `चक्रवृद्धि`, `EMI` not `किश्त`) | VO register is textbook Hindi while the screen and the channel's own description are Hinglish — the lane's actual voice | cheap | `.claude/agents/fin-script.md` + `vault/knowledge/` (needs a hi style note; `haryanvi-*` is excluded by design) |
| 5 | FACT | Raise `max_elevenlabs_calls` and run one pair on `tiers.medium` (8:30, per-line-chapters) | mid-roll needs 8:00; `tiers.medium` = 510s and `firaun-ka-anjaam/build.py` already exist — the blocker is a 30-call config constant, not the build | medium (inputs ~3×; facts 4× and `library.db` has no finance lane) | `tools/format.json` + `.claude/commands/finance-video.md:70` + `fin-script.md` |

Changes 1–4 are one file. Change 5 is two config values and a script budget.

---

## Sources

- [PrePublish — First 30 Seconds of YouTube Videos (2026)](https://prepublish.ai/guides/first-30-seconds)
- [Miraflow — YouTube Video Hooks in 2026](https://miraflow.ai/blog/youtube-video-hooks-2026-save-first-30-seconds)
- [Overseeros — YouTube Retention Architecture 2026](https://www.overseeros.com/blog/youtube-retention-architecture-2026)
- [Artiphik — The first 10 seconds: a YouTube retention playbook](https://artiphik.com/blog/the-first-10-seconds-retention-playbook)
- [Humble & Brag — YouTube Audience Retention Benchmarks 2026](https://humbleandbrag.com/blog/youtube-audience-retention-benchmarks)
- [vidIQ — YouTube Mid-Roll Ads: The 8-Minute Minimum](https://vidiq.com/blog/post/youtube-8-minute-mid-roll-ads/)
- [FluxNote — Mid-Roll Ads Minimum Video Length 2026](https://fluxnote.io/guides/youtube-mid-roll-ads-minimum-video-length-8-minutes-2026)
- [Wikipedia — Hinglish](https://en.wikipedia.org/wiki/Hinglish)
- [bemoneyaware — Indian personal-finance YouTube channels](https://bemoneyaware.com/youtube-india-personalfinance-investing-stocks/)

Creator-tier retention sources are directional only — `long_form_scripting.md` §13's caveat
about creator-reported benchmarks stands and I have not overridden it. **No claim in this
document is validated against channel analytics, because none exist.**
