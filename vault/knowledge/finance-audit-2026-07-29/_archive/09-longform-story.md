# 09 — Long-form story scripting for the two finance channels (8:30 target)

Scope: the words and the structure for an 8–9 minute story-driven finance video, executable by
`/finance-video`. Faceless + synthetic TTS are fixed. No visuals/motion/sound/thumbnail design here.

Every claim is tagged **FACT** (measured in-repo, measured from a real artifact I retrieved, or a
cited public number) or **UNVALIDATED** (reasonable belief). **This channel has zero analytics**, so
nothing about *our* retention can be FACT. I have kept that line hard.

Read alongside: `vault/knowledge/finance-audit-2026-07-29/01-performance.md` (§3 benchmark) and
`02-script.md` (§3–§5). This note does not re-derive their findings; it builds the format they
recommended but did not specify.

---

## 0. The three-line verdict

1. **The runtime finding replicates and is the only strong signal.** FACT.
2. **"Story" is the right *filling* for 8:30 but is NOT what the data proves.** The single best
   small-channel breakout in the vault's own benchmark (Easy Life With Monika, 1,680 subs,
   57,911 views, **v/sub 34.45**) is an 8m13 **non-story list of ten household tips with almost no
   numbers in it**. FACT, measured from the transcript below. Any claim that story *causes* the
   traction is UNVALIDATED. What story buys is a *reason for 8 minutes to hold together* — which
   the blockframe-9 material demonstrably cannot supply (audit §2c: 44% of the shipped video is
   predictable from its own hook).
3. **The honest worked example already exists in the wild and both of its best executions are in
   Hindi.** A named character who is *declared to be an assumption set* — Zerodha Varsity's
   *"वरुण की हेल्प लेते हैं और कुछ अजम्पशन्स करते हैं"* ("let's take Varun's help and make some
   assumptions") and CA Rahul Malodia's mythological-joke brothers *Atapi and Vatapi*. FACT,
   both retrieved verbatim. That is the form to adopt; §2 rules on it.

---

## 1. What actually works at this length — 8 videos, reverse-engineered from the artifacts

**Method (FACT).** The project's own engine: `venv/bin/python -m yt_dlp` (2026.06.09), the same
library `backend/youtube_scraper.py` drives. For each video: full metadata (duration, view_count,
channel_follower_count, upload_date, chapters) + auto-caption VTT, de-rolled and re-bucketed into
20-second windows. Raw transcripts kept at
`…/scratchpad/research/tx/<video_id>.txt`; the fetcher is `…/scratchpad/research/grab.py`.
Nothing was written to `library.db` and nothing in the repo was modified.
Two Hindi candidates were dropped for irrelevance (SSOFTOONS `ERxrOOapNV4` is a comedy folk-tale,
not an explainer). Caption fetching is rate-limited — HTTP 429 after ~4 videos, so this is 8, not 20.

### 1a. The set

| # | Video | Mkt | Runtime | Views / subs | v/sub | Ch | Faceless? | Carried by |
|---|---|---|---|---|---|---|---|---|
| V1 | Easy Life With Monika — `MTtBq6dG6m0` | IN | **8m13** | 57,911 / 1,680 | **34.45** | 0 | no (host VO, hands-on demo) | **no story** — 10 tips |
| V2 | CA Rahul Malodia — Credit Score … Case Study — `vO_Ce1BdOro` | IN | 17m33 | 1,460,491 / 6.94M | 0.21 | 11 | no | **illustrative two-character case** |
| V3 | Zerodha Varsity Hindi — Why Should You Invest? — `Sfsdf-iKiwQ` | IN | 11m52 | 4,544 / 4,560 | 1.00 | 9 | **YES** (animation + VO) | **declared-assumption character + counterfactual twin** |
| V4 | GIGL — Power of Compounding — `KojTmd3vYoM` | IN | 10m23 | 1,500,314 / 7.17M | 0.21 | 0 | **YES** (animation + VO) | **guess → ladder thought-experiment** |
| V5 | The Frugal Rich — 126 MEALS FOR $30 — `ZU9ZpVlvwkE` | US | 10m37 | 365,991 / 92,400 | **3.97** | 0 | no | **real, cited third-party case** |
| V6 | Clever Girl Finance — No Savings. No Investments — `-uAOI6yJgm4` | US | 17m04 | 354,403 / 219,000 | **1.62** | 0 | no | **counterfactual frame** ("if I had to start from zero") |
| V7 | Humphrey Yang — Never Finance A Car This Way (2026) — `rIi3YI0zmNI` | US | 10m40 | 480,155 / 2.06M | 0.23 | 8 | no | **second-person scene + a quoted document** |
| V8 | SSOFTOONS — animated money folk-tale — `ERxrOOapNV4` | IN | 10m40 | 468,875 / 3.83M | 0.12 | 0 | **YES** | pure narrative (entertainment, not explainer — excluded from conclusions) |

All FACT as retrieved 2026-07-30. V1/V5/V6 are the vault benchmark's three highest-`v/sub`
long-form entries; V2/V3/V4/V7 were added because they are (a) on our exact topics, (b) recent, or
(c) faceless — the cohort the vault benchmark says it has no positive example of.

### 1b. First 30 seconds — what each one actually does

FACT, verbatim from the transcripts (translations mine).

- **V5 Frugal Rich (0:00–0:40):** names a real person and a real number, then plays a *guessing
  game* against the viewer: *"There's this woman named Christine who decided to feed her family of
  six for an entire week using x amount of dollars. I'm gonna let you guess how much money she
  used. 300? No. How about 100? Not even. … only $30."* Then converts the number into a worse unit:
  6 × 3 × 7 = **126 meals = 24 cents per meal**. Then the loop: *"But like, how?"* Then attribution:
  *"she's better known as the frugal fit mom, I'll put the link to her original video in the
  description."*
- **V2 Malodia (0:00–1:50, 110 seconds of pure story):** *"There were two brothers, Atapi and
  Vatapi."* Same school, same college, same job. They watch a film, decide to go to Spain, have no
  savings, ask friends (everyone blocks them), apply for a bank loan — **Atapi approved, Vatapi
  rejected.** Vatapi's bigger problem is *why*: "I have a car, a bungalow." Bank: *"Atapi's credit
  score is over 750. Yours is 550. Your car has a loan on it, so does the bungalow, so does the
  phone, you hold three credit cards and you've defaulted four times."* Only then, at 1:20, the
  question cascade — *"But what IS a credit score? How is it built? You, watching — what's yours?
  How would you find out? If it's low, why, and how do you raise it?"* — closed with *"Rahul will
  answer all of this in the next five minutes — for you, and for Vatapi."*
- **V4 GIGL (0:00–1:20):** a physical thought experiment with a pause-and-guess: how many times can
  you fold a sheet of paper? Four? Five? Eight? *"What if someone folded it 45 times — how thick?
  As thick as your phone? Your own height? Your building? Pause the video and guess."* Reveal:
  Earth to the Moon. 46 folds: there and back.
- **V3 Varsity Hindi (0:00–1:40):** *"Everyone says you should invest. Nobody tells you why."* Then:
  *"To understand it, **let's take Varun's help and make some assumptions.**"* Varun is 25, wants to
  retire at 50, fixed expenses, saves ₹20,000/month, 10% annual raise, 8% inflation, holds it all in
  cash. *"What do you think — 25 years, no investing, how much?"* → ₹3.27 crore. *"Not bad, right?
  But…"* (his expenses never changed, no car, no house, no vacation, and it may run out in 7–8
  years) → *"If Varun had invested: about ₹9.36 crore. 3×."*
- **V7 Humphrey Yang (0:00–0:40):** a second-person scene — you're in the dealership, the salesperson
  asks *"how much per month are you looking to spend?"*, you answer honestly, *"and the moment you
  reveal your number, you've lost the game — you've cost yourself thousands."*
- **V6 Clever Girl (0:00–0:40):** a counterfactual — *"If I had to start from zero, no savings, no
  investments, no financial cushion, what would I do?"* Then credentials (founder, author) — the one
  move we are barred from.
- **V1 Monika (0:00–0:30):** the *weakest* opening in the set and the highest `v/sub` in it:
  generic context ("running a household isn't easy, bills keep rising"), a self-introduction, and a
  literal table of contents ("10 simple and effective money-saving tips"). **This is the beat the
  audit tells us to kill, in the video with 34× reach.** UNVALIDATED but worth stating plainly:
  in a search-intent Hindi utility niche, the hook may matter far less than the vault assumes.

**Pattern (FACT across V2–V5, V7):** none opens with a definition. Five of eight open on a
*situation with an unresolved outcome*; three of eight hand the viewer an explicit **guess** before
revealing the number (V4, V5, V3). Zero open with a chip-list roadmap **except V1**.

### 1c. Where the explanation sits relative to the story

FACT, from chapter markers and transcript timestamps:

- **V2:** story 0:00–1:50 → definition 2:00 → mechanism 6:22 → causes of a low score 9:01 →
  fixes 12:54 → conclusion 16:39. **The story runs first and complete; the explanation is the
  answer to the story's question**, and the character is re-invoked to carry it ("for you, and for
  Vatapi").
- **V3:** the arithmetic *is* the story — the character exists only to hold the assumptions, and the
  payoff (₹3.27cr vs ₹9.36cr) lands at 1:40, before any concept is named. Concepts arrive after
  their consequence has been seen: inflation 1:50, standard of living 2:10, wealth 2:22,
  compounding 4:21, asset classes 5:30.
- **V4:** analogy → *verification of the analogy by arithmetic* → the concept named →
  a second analogy (bacteria doubling; "when was the test tube half full?").
- **V5/V7:** explanation is *interleaved* — each strategy/trap is one story unit with its own number.
- **V6:** no explanation layer at all. Ten actions, each self-contained.

**The generalisation (UNVALIDATED as a causal claim, FACT as a description of the sample):** at
8–17 minutes the explanation is never a *beat*. It is either the answer to a story already told
(V2), or induced from a ladder of arithmetic (V3, V4), or distributed one-unit-at-a-time (V5, V7).
**A standalone "concept" beat and a standalone "the math" beat — blockframe-9's slots 3 and 7 —
appear nowhere in this set.**

### 1d. How the middle (3:00–6:00) is held

This is the question blockframe-9 has never had to answer. FACT, per video:

| Video | The device that fills 3:00–6:00 |
|---|---|
| V5 | **A second timeline.** The presenter re-shops the 2020 list at Walmart *today* — chicken leg quarters $7.72, eggs $3.76 → $8 — so every strategy gets a fresh, verifiable number. Plus a comment prompt every ~60–90s and two deliberate micro-tangents (oatmeal/blood pressure, a live ChatGPT query). |
| V7 | **The same deal shown twice.** The dealer worksheet before and after negotiation: monthly payment $845/36mo → $476, while the price moves $34,000 → $33,980. Then a **quoted document** (2015 DOJ–Honda settlement, dealer markup capped at 125 basis points) and its arithmetic: +1% = **+$764 interest**. |
| V2 | **Three cause-clusters, each with its own number**, and a live screen demo (pulling a real credit report) at 4:00 — an action the viewer can copy mid-video. |
| V4 | **The ladder walked rung by rung with a physical yardstick at each rung:** 0.001cm → 0.002 → 0.004 → 10th fold 1.024cm → 20th fold 1,048cm ("about 34 feet — a three-storey building") → 45th 3.5 lakh km. |
| V3 | Named sub-questions ("how much to start with?", "when to start?"), each with a minimum-ticket number. |
| V6 | Ten numbered actions ≈ 100s each, plus a **designed self-promo break at 8:20 of 17:04 (49%)** — *"if you are enjoying this video… okay, let's get back to the video."* |
| V1 | Ten physical demonstrations, each a different object (pressure cooker, a frozen water bottle in the fridge door, batteries reversed in a rarely-used remote, the AC at 22–24°C). **Almost no numbers at all.** |

**The four transferable devices**, in order of fit to a faceless finance pipeline:
1. **The rung ladder** (V4, V3) — one mechanism, walked in equal steps, each step tied to something
   physical. Cheap for us: it is pure arithmetic, and the build calculator can lock every rung.
2. **The same thing shown twice** (V7, V3's counterfactual) — one variable changed, arithmetic
   re-run, the delta is the payoff.
3. **Named failure modes, each with its own number** (V2, V7) — three mini-loops.
4. **The verifiable instruction mid-video** (V2's live report pull, V7's "look at the four-square")
   — the viewer *does* something at ~5:00. This is the faceless channel's substitute for charisma
   and it is the one thing the audit already identified independently (§6 Hook 2).

### 1e. Chapters, and the faceless question

- FACT: chapters do not correlate with traction here. V1, V4, V5, V6 have **zero**; V2 has 11, V7
  has 8, V3 has 9. The vault's benchmark found the same (5 of 6 breakouts had none).
- FACT: **two of the four faceless videos in this set are exactly the format we need** (V3 Zerodha
  Varsity Hindi, V4 GIGL) and both carry a story with narration + graphics only. V3 is a
  4,560-sub channel at v/sub 1.00. **This closes the vault's "no positive faceless example" gap
  partially** — V4 does 1.5M views faceless, though on a 7.17M-sub channel, and V3's absolute
  numbers are small. UNVALIDATED that a faceless finance explainer *breaks out*; FACT that the
  format exists and is not a novelty.
- FACT: V3 and V4 are animation, not stock photography. Our format (graded stock + motion type) is
  a third thing. Nothing in this sample validates it.

---

## 2. The honest worked example — the ruling

### 2a. The problem, stated precisely

A faceless channel with synthetic narration has **no narrator to bond with**, and by
`niches/us-market-2026.md` rule 1 it may not acquire one. So three of the four engines the
benchmark videos run on are unavailable to us: first-person opinion (V7's *"drives me crazy"*),
credentialed authority (V6's founder/author intro), and personal fieldwork (V7's *"true story, I
went to a Toyota dealership this weekend"*).

What is left is the **situation** — and situations do not need a narrator. V4's paper-fold has no
character at all and holds 1.5M views. V2's Atapi/Vatapi is carried by a *predicament*, not by
Rahul: the interesting thing is that two identical men got opposite answers from the same bank.

**UNVALIDATED but load-bearing:** the bonding object for a faceless finance video is not a person,
it is **an unresolved number**. The viewer stays because a quantity has been promised and not yet
delivered. That is why every device in §1d is a number-delivery schedule.

### 2b. The five candidate forms, compared

| Form | Honest? | Engaging? | Verdict |
|---|---|---|---|
| **A. Fabricated testimony** — "my friend Rahul had ₹2 lakh on a credit card" | **No.** Presents invention as evidence. Also requires a first person we don't have. | high | **Banned.** Violates the vault's never-invent-a-fact rule and creates exactly the "AI slop / inauthentic content" exposure the persona rules exist to avoid. |
| **B. Real cited case** — V5's Christine, linked in the description | **Best available.** | highest in the set (v/sub 3.97) | **Use whenever `fin-facts` can find one.** Cost: a public, linkable, numerically specific case per topic. It does not exist for most mechanisms ("how amortisation works" has no case study). Not a base format. |
| **C. Second-person "you" only** — V7 | Honest *until it isn't*: "your payment is $596" asserts a fact about a viewer it may be false for. | good for a scene, weak over 8 min | **Use for the scene and the instructions, not as the spine.** "You" cannot be surprised, cannot be wrong, and cannot have an ending — so it cannot carry a reveal. |
| **D. Declared-assumption named character** — V3's Varun, V2's Atapi/Vatapi | **Yes, if declared once and never re-asserted as real.** Nothing is claimed about the world except the sourced inputs. | proven in both markets on our exact topics | **RECOMMENDED. This is the base format.** |
| **E. Unnamed "a buyer"** | Yes | forgettable — no one to follow | Fallback only. |

**Ruling: D, with C for the opening scene and the instruction beats, and B substituted for D
whenever a real cited case exists.** The character is not a witness; he is **a carrier for an
assumption set** — an arithmetic character. This is precisely how the two highest-traction Hindi
videos on our topics do it, and it survives the persona policy because the character is not the
narrator and claims no expertise.

### 2c. The exact framing language

The declaration must appear **once, inside the first 25 seconds**, in the same breath as the name —
never as a disclaimer bolted on later. Ship these strings (grep-checkable by the audit stage):

**US / `-en` cut**
> "Meet Marcus. Marcus isn't a real person — he's an average, built out of what Americans actually
> financed last year. Every number of his is real."

Shorter variant when the beat is tight:
> "Call him Marcus. He's not real — his numbers are."

**India / `-hi` cut** (Hinglish register per audit §5c — the VO says the term the screen says)
> "एक बंदा है — नाम रख लेते हैं रोहित। रोहित असली नहीं है, पर उसके सारे नंबर असली हैं।"
> *("There's a guy — let's call him Rohit. Rohit isn't real, but every one of his numbers is.")*

Alternative Hindi register that is *funnier and even more clearly non-real* — V2's device, and it
works: give the pair openly mock names and let the audience be in on the joke.
> "दो भाई थे — मान लो अतापी और वतापी। एक ही सैलरी, एक ही उम्र, एक ही शहर।"

**The six hard rules for the character** (these are what make the form honest, not the wording):
1. Declared illustrative in the **first 25 seconds**, in the sentence that introduces him.
2. **Every number attached to him traces to `facts-staging.md`** or is computed by the build
   calculator from numbers that do. Same rule the pipeline already enforces — it just now also
   covers "his salary" and "his loan".
3. **No testimony, ever.** He never "tried this and it worked", never speaks, never recommends. He
   is acted upon by arithmetic.
4. **No biography beyond what the arithmetic needs.** Age and income only if a number depends on
   them. No family drama, no emotions asserted as fact.
5. **The counterfactual twin is the same character with one variable changed** — "Marcus, same car,
   same rate, 48 months instead of 72" — not a second invented person. (V3 does exactly this;
   V2's two-brother version also works but doubles the invention.)
6. **A common generic first name, never a real public figure**, and a different name per video and
   per cut (this is also one of the anti-sameness controls — see §7).

**What this buys that "you" does not:** a reveal. The video can withhold his ending. **What it
costs:** the viewer must accept a stand-in. V5's data point suggests a *real* named case beats an
illustrative one (3.97 v/sub) — so B > D whenever B is obtainable.

### 2d. Making the arithmetic part of the story

Six rules, all derived from §1b/§1d and all machine-checkable:

1. **One number per VO line.** Two numbers in one spoken line is a lecture; one number per line with
   a scene under it is a beat. (Our per-line architecture makes this free.)
2. **Every number arrives as the answer to the previous line's question.** If a number can be
   deleted without leaving a hole, it was decoration.
3. **Guess before the biggest reveal.** V4, V5, V3 all do it. Faceless-safe: it addresses the
   viewer, not a persona. Costs one line: *"Before you hear the number — guess."*
4. **Unit flip.** The number lands in the unit that hurts, not the unit it was computed in: 126
   meals → **24 cents a meal** (V5); a payoff time → **"215 months. Not dollars — months"** (the
   audit's own §3c rewrite); total interest → **"$124 a month you never see again."**
5. **Ladder, not lump.** A mechanism is taught as equal steps with a physical yardstick per step
   (V4's phone → building → Earth-Moon). The rungs are what fill 1:45–4:50.
6. **The delta is the payoff.** The final number is never the loss — it is the *difference* between
   two runs of the same arithmetic with one variable changed. This is the structural reason the
   audit's complaint ("every scare is precise, the remedy is not") disappears: the remedy is now
   the only fully quantified thing in the video.

---

## 3. The beat sheet — `story-ladder-12` at 8:30 (510s)

Executable contract. `tiers.medium` = 510s, `per-line-chapters`; en 16.1 c/s → **8,211 chars**;
hi 12.5 c/s → **6,375 chars** (FACT, `tools/format.json`). One VO line = one TTS clip = one scene;
one image may be held across consecutive lines as a single continuous zoom (the Firaun rule).

Line budget: ~95 chars/line (en) / ~72 (hi) → **≈ 86 lines per cut**, ~5.9s each.

| # | Beat | Window | s | Lines | Job | What fails if it's missing |
|---|---|---|---|---|---|---|
| **B1** | **COLD OPEN — the situation, outcome withheld** | 0:00–0:25 | 25 | 4 | One scene, one character declared illustrative (§2c), one thing that already went wrong. No definition, no channel, no topic statement. | The 10–20s cliff. Without a withheld outcome there is no reason for second 21. |
| **B2** | **THE GUESS** | 0:25–0:50 | 25 | 4 | Hand the viewer the inputs, ask them to guess the outcome, reject two wrong anchors ("$3,000? No. $5,000? Not even."). | The reveal in B3 lands as a statistic instead of a result. No commitment micro-yes. |
| **B3** | **REVEAL + UNIT FLIP** | 0:50–1:15 | 25 | 4 | The number, then the same number in the unit that hurts. First payoff **before 1:15**. | The video becomes a promise-only opening; the audit's §3b window (0:20–0:32) is where the shipped format loses people. |
| **B4** | **THE OPEN QUESTION + DEFERRED VERDICT** | 1:15–1:45 | 30 | 5 | The character's unanswered question = the viewer's (V2 at 1:20). Promise **a verdict, not a list** ("by the end you'll know whether this was even a bad deal"), and tease the B10 reward. **This is slot 2's replacement and it may not enumerate sections.** | Without a deferred verdict there is nothing to stay for after the reveal; with a chip list you have rebuilt the beat `long_form_scripting.md` §4 bans. |
| **B5** | **LADDER, rungs 1–3** | 1:45–3:05 | 80 | 13 | Walk the mechanism in equal steps, one number per line, a physical yardstick per rung. **Do not name the mechanism yet.** | The mechanism becomes a definition; 3:00 is where a 3-minute video would already be over. |
| **B6** | **THE TURN** | 3:05–3:45 | 40 | 7 | The rung where intuition breaks ("this is where it stops being a straight line") — and only here, the mechanism gets its name, as a label for what was just watched. | The mid-video drift. This is the mandatory re-hook; without it the ladder becomes a spreadsheet read aloud. |
| **B7** | **LADDER, rungs 4–n → the loss number** | 3:45–4:50 | 65 | 12 | Run the ladder to the end. Land the video's biggest *loss* number at ~4:50 (57%). | The 8 minutes have no destination; the peak arrives too late to be believed. |
| **B8** | **SELF-CHECK INSTRUCTION** | 4:50–5:20 | 30 | 5 | An action the viewer executes in 20 seconds against their own document ("open the statement, find the line that says…"). **Beat boundary at 5:20 = the declared mid-roll break.** | Loses the only credibility device a faceless channel owns (verifiability), and an ad lands mid-argument. |
| **B9** | **THREE WAYS THIS GOES WRONG** | 5:20–6:25 | 65 | 11 | Three named failure modes, each its own mini-loop with its own number. Not a list — each opens on tension. | The 55–65% drop zone. Also the only beat that carries topic-specific detail, i.e. the anti-sameness beat. |
| **B10** | **THE COUNTER-CASE — the reward (teased in B4)** | 6:25–7:35 | 70 | 12 | Same character, **one variable changed**, arithmetic re-run, **the delta is the payoff.** Peak lands ~7:00 (82%). | The audit's core complaint: the scare is quantified, the remedy is not. Without this the video is a warning, not an answer. |
| **B11** | **THE HONEST LIMIT** | 7:35–8:00 | 25 | 3 | Where this advice stops working / who it does not apply to. Sourced caveat, not hedging. | Nobody in the niche does this (audit §4A beat 6); it is the cheapest available differentiator and it protects every claim above it. |
| **B12** | **THE PLAN + THE LOOP** | 8:00–8:30 | 30 | 4 | Three numbered steps, step 1 carrying a number; then **the named next video** that closes a loop opened in B4/B9. **No recap.** | 0 of 8 shipped scripts has a next-video loop (audit §2c) — a free session-time mechanism the canonical skill mandates. A recap here ends the video on its flattest beat. |

Totals: 510s, **86 lines**. Two peaks by design: the loss number at 57% and the delta at 82%
(peak-end).

### 3a. How this differs from blockframe-9, beat by beat

| blockframe-9 | Fate | Why |
|---|---|---|
| 1 hook | **survives, expanded** into B1–B3 (0:00–1:15) | The audit found the hook is the strongest part. It is now three beats instead of one paragraph, and it carries a guess. |
| 2 roadmap | **dies as a table of contents**; the slot becomes B4 | 6–7% of runtime restating the title inside the drop window, in a form `long_form_scripting.md` §4 explicitly bans. Only V1 in the traction set does it. |
| 3 concept | **dies as a beat**; folded into B5's rungs and B6's naming | No video in the traction set has a standalone definition beat. Definitions arrive *after* their consequence (V3, V4). |
| 4 contrast/rule | **survives, relocated** to B10 as the counter-case | A two-column classifier is a definition list (audit: "nobody in the target audience learns anything here"). A contrast with arithmetic on both sides is the payoff. |
| 5 mechanism/audit | **promoted to the spine** — B5+B6+B7, 185s of the 510 | This is *the only thing a 3-minute cut cannot do*, and therefore the actual reason to make a long one. |
| 6 action | **survives, split** — B8 (do it now, mid-video) + B12 (the plan) | One action beat at 65% of a 3-minute video is a CTA; two actions in an 8-minute video are a retention device. |
| 7 the math | **dies as a beat, because it is now the whole middle** | Isolating "the math" in one 27-second scene is what forced the other eight beats to be qualitative. |
| 8 do-today | **survives inside B12**, with a number attached | `DO THIS TODAY` appears in 8/8 scripts (audit §1) — the *beat* survives, the string must not. |
| 9 recap + CTA | **dies** | Replaced by B11 + B12. Peak-end says do not end on a summary; and the recap restates material under 90 seconds old. |

**Survivors: 5 of 9** (hook, contrast, mechanism, action, do-today) — all relocated. **Dead: 4**
(roadmap, concept, "the math" as a beat, recap).

### 3b. Pipeline consequences (the blocking ones)

- FACT: `max_elevenlabs_calls: 30` in `.claude/commands/finance-video.md:70` is shared across both
  cuts. **86 lines × 2 cuts = 172 calls plus retries.** Raise to **≥ 220** or the tier cannot run.
  This is a config guard, not a vendor limit, and ElevenLabs bills per character, so more calls at
  the same character count is not more money.
- FACT: `format.json.architectures` is the rotation source (`pipeline_check.py
  --next-architecture`). `story-ladder-12` must be added there with `"tier": "medium"` and a
  `lines` *range* rather than a fixed 9, or the rotation will keep handing back short-tier layouts.
- Images: ~30–40 distinct stills (one held across 2–3 consecutive lines), not 86. Roughly 2× the
  current per-video sourcing load, not 9×.
- Facts: B5/B7/B10 all run off **one** locked input set (price, rate, term) plus a build
  calculator. That is *fewer* sourced claims than blockframe-9's nine independent beats, not more —
  which contradicts the audit's assumption that option C costs "~4× the sourced claims". It costs
  4× the *arithmetic*, which is free, if and only if the topic is chosen for a single mechanism.

---

## 4. "Easy for everyone" — the concept budget

### 4a. How many new concepts

FACT, counted from the transcripts: V4 teaches **one** mechanism (compounding) with three
analogies in 10m23. V2 teaches **one** (the score) plus a taxonomy in 17m33. V3 teaches one
(compounding) and names four reasons. V6 teaches **zero mechanisms** and lists ~12 *actions*.
V1 teaches zero mechanisms and demonstrates 10 actions in 8m13 — the highest v/sub in the set.

**The rule (UNVALIDATED as a threshold; FACT as a description of the sample):**

> **One mechanism per video. At most three named terms. Unlimited actions.**

The important distinction the vault does not currently draw: **cognitive load comes from
mechanisms, not from items.** Ten tips cost the viewer nothing to follow (V1, V6); two mechanisms in
eight minutes will lose them. The shipped `good-debt-vs-bad-debt-en` carries four — renting money,
the good/bad taxonomy, the minimum formula, and compounding — in **2:47**, which is the real reason
its middle feels like elaboration.

### 4b. Sequencing

1. **Consequence before cause.** The number the viewer will care about is shown before the thing
   that produced it is named (V3: ₹3.27cr vs ₹9.36cr at 1:40; the word "compounding" at 4:21).
2. **Name it on the third rung, never the first.** The term is introduced as a *label for something
   already watched three times* (B6). If the viewer can already describe it, the word is free.
3. **Every new term must be needed to explain a number already on screen.** No term is introduced
   for completeness.
4. **The formal rule after the analogy, plus where the analogy breaks** — `long_form_scripting.md`
   §10, unchanged, and V4 does exactly this (folds → then the real centimetre arithmetic).
5. **One vocabulary per concept for the whole video.** Do not alternate "principal" and "the amount
   you borrowed". For `-hi`: **the VO says the word the screen says** (audit §4, change #4) —
   `कंपाउंडिंग` not `चक्रवृद्धि`, `EMI` not `किश्त`. V1 (34× reach) is drenched in exactly this
   register: मंथली बजट, अननेसेसरी खर्च, इलेक्ट्रिसिटी कंज्यूम, इंपल्स शॉपिंग. FACT — that is what
   the lane sounds like.

### 4c. Teaching a mechanism inside a story without a lecture beat

**The technique: the rung ladder.** Take the one variable that moves (a month, a year, a fold),
advance it in equal steps, and after each step state (a) the new number and (b) a physical
yardstick for it. The mechanism is *induced* — the viewer derives the rule before you say it, which
is why it feels like a story and not a definition. The character supplies the inputs so the rungs
are *his* months, not an abstract series.

### 4d. Two worked rewrites, from real shipped lines

**Rewrite 1 — `good-debt-vs-bad-debt/script-en.md` en4 (the "concept/rule" beat, 0:53–1:16,
identified in the audit as click-away risk #2).**

BEFORE (shipped, one paragraph, 324 chars):
> "So — the rule. Good debt buys what grows in value or income: a degree, a skill, a business. While
> you pay it down, it's earning for you. Bad debt just buys consumption — clothes, gadgets, a
> vacation, gone before the bill even lands. Worst of all: a credit-card balance. But debt is only
> good when the return beats the interest."

Diagnosis: a definition list with zero numbers in a video built entirely on quantification. It
teaches a taxonomy the title already gave away.

AFTER (per-line, B9 material — one failure mode, one number, one loop):
> L041 · "Marcus has two loans, and on paper they look like the same kind of debt."
> L042 · "Both are eleven thousand dollars. Both charge him interest every month."
> L043 · "The first one is a course that moved him from twenty-two dollars an hour to thirty-one."
> L044 · "That one pays its own interest and hands him the difference — about nineteen thousand a year."
> L045 · "The second one is a card balance, and the thing he bought with it was gone the same weekend."
> L046 · "Same eleven thousand dollars. One of them earns while he pays it. The other only charges."
> L047 · "So the test was never what you bought — it's whether the thing you bought is still working."
> L048 · "Which is why the next number matters more than the category: what's the interest, and what's the return?"

What changed: the taxonomy is *derived* from one character's two loans instead of asserted; every
line carries one number; the beat ends on an open question instead of a caveat; and the "good debt
is only good if the return beats the interest" caveat is now the *reason to keep watching* rather
than a foot-note. (Figures here are structural placeholders — `fin-facts` must source the wage
numbers or the beat drops to the sourced ones.)

**Rewrite 2 — `good-debt-vs-bad-debt/script-en.md` en5 (the mechanism beat, 1:16–1:39, the audit's
"third restatement of interest is paid first").**

BEFORE (shipped, 327 chars):
> "Now, how the trap works inside. Your minimum is about one percent of the balance, plus that
> month's interest — and interest is paid first. So the bank always collects, and barely one percent
> of the balance comes off. Then it's interest on the interest. Compounding grows your money when
> you invest — on a card, it runs against you."

Diagnosis: the rule stated, then restated, then named. Three sentences of mechanism, no rungs, no
yardstick, and the concept ("compounding") named before it has been seen happening.

AFTER (per-line ladder, B5 material — the same content as four rungs, ~48s):
> L018 · "Month one. Six thousand on the card, and the minimum asks for a hundred seventy dollars."
> L019 · "A hundred ten of that is interest. Sixty comes off what you owe."
> L020 · "So after your first payment, the balance is five thousand nine hundred and forty."
> L021 · "Month two, the minimum is a dollar lower — because the balance is sixty dollars smaller."
> L022 · "Month three, a dollar lower again. This is the whole pattern, and it does not speed up."
> L023 · "Twelve payments in, you have handed over about two thousand dollars."
> L024 · "And you still owe five thousand three hundred and eighteen."
> L025 · "A year of never missing a payment moved the balance six hundred and eighty-two dollars."
> L026 · "That's the part that has no name on your statement — the interest is charged first, every month, before anything you pay touches the debt."

What changed: four rungs with the balance re-stated each time; the yardstick is *a year of
compliant behaviour*; the mechanism is named only in the last line, after it has been watched
happening four times; and "compounding" is dropped entirely from this beat — it is a *second*
mechanism and §4a allows only one. (All figures already build-locked in the shipped script.)

---

## 5. A real outline — US/$ cut, ~8:30

**Topic: "The 72-Month Car Payment" — why the cheaper monthly payment is the more expensive loan.**

Why this topic: (a) one mechanism (front-loaded interest / how a term changes total cost), (b) the
entire shock is derivable from **two sourced inputs** (a vehicle price and an APR) so nothing needs
a depreciation model or a return assumption — the build calculator can lock every number and cannot
be wrong; (c) it does not repeat a shipped topic, and (d) it hands B12 a *real* next-video loop
into the existing `credit-history` cut ("the rate you were offered was decided before you walked
in"). It also passes the persona rules: no product pick, no fund, no advice from a credential —
a vehicle loan is a generic instrument and rates are price evidence.

**Inputs (STRUCTURAL PLACEHOLDERS — `fin-facts` must re-source all three; the arithmetic below is
mine and is internally consistent, but the inputs are not sourced facts):**
`B₀ = $34,000` · `APR = 8.0%` (i = 0.0066667/mo) · `term = 72 months`, compared against `48 months`.
Everything else is computed: payment $596.13/mo (72) vs $830/mo (48); total interest **$8,921** vs
**$5,842**; **delta $3,079**; month-1 split $227 interest / $369 principal; balance after 12
months $29,400; after 36 months **$19,024**; interest paid in the first 36 months $6,484 = **73% of
all interest on the loan**.

### The opening three lines — final script, verbatim

> **L001** · "Marcus wanted a payment under six hundred dollars a month, and the dealer found him one."
>
> **L002** · "Marcus isn't a real person — he's an average, built out of what Americans actually financed last year, so every number of his is real."
>
> **L003** · "He got the payment he asked for. Five hundred ninety-six dollars. And it cost him three thousand and seventy-nine dollars more than the car he almost bought instead — the same car."

(L001 96 chars · L002 152 · L003 178 → ~26s at 16.1 c/s. L002 runs long for a single line; if the
audit's per-line cap binds, split at the em-dash into L002a/L002b.)

### Beat-by-beat

**B1 · COLD OPEN (0:00–0:25, L001–L004).** L001–L003 above. L004: "Here's how a cheaper payment
becomes a more expensive loan." — the thesis stated once, flat, then never restated.

**B2 · THE GUESS (0:25–0:50, L005–L008).** The inputs handed over: thirty-four thousand dollars,
eight percent, six years. Then: "Before you hear the total — guess what six years of interest costs
on that. Four thousand? Not close. Six? Still low." Ends on "Guess high and you still probably
missed it."

**B3 · REVEAL + UNIT FLIP (0:50–1:15, L009–L012).** "Eight thousand nine hundred and twenty-one
dollars." → the flip: "That's a hundred twenty-four dollars a month, every month for six years,
that buys him nothing at all — no car, no equity, nothing." → "He didn't overpay for the car. He
overpaid for the *time*."

**B4 · OPEN QUESTION + DEFERRED VERDICT (1:15–1:45, L013–L017).** The character's question, which
is the viewer's: "And here's what Marcus couldn't see on the paperwork — the same car, the same
rate, on a shorter loan, was never shown to him." Deferred verdict + reward tease: "By the end of
this you'll know whether the payment you can afford and the loan you should sign are the same
number — and there's one month in this loan where everything changes. It's not the first one."
**No section list.**

**B5 · LADDER, rungs 1–3 (1:45–3:05, L018–L030).** Month 1: $596 leaves, $227 is interest, $369
touches the car. Yardstick: "the interest alone is a phone bill." Month 2, month 3 — the split
barely moves. Month 12: he has paid $7,154 and the balance has fallen $4,601. Yardstick: "a year of
payments, and more than four months' worth of them were rent." Mechanism still unnamed.

**B6 · THE TURN (3:05–3:45, L031–L037).** "Here's the part that isn't a straight line." The interest
is charged on what is *left*, so the first payments are the most expensive ones he will ever make —
and a longer loan does not add cheap months at the end, it adds *expensive months at the front*.
**Now the name arrives, once:** "That front-loading has a name — amortisation. It just means the
interest gets paid before the debt does."

**B7 · LADDER, rungs 4–n → the loss number (3:45–4:50, L038–L049).** Month 24, month 36: "Three
years in — half the payments made — he still owes nineteen thousand and twenty-four." Then the peak
of this half: "Of all the interest he will ever pay, seventy-three percent of it is already gone,
in the first three years." Yardstick: "he is halfway through the payments and nowhere near halfway
through the loan."

**B8 · SELF-CHECK (4:50–5:20, L050–L054).** "Open your own loan — the app, the statement, the
paperwork in the glovebox. Find the line that splits this month's payment into interest and
principal. Every lender shows it; most people have never looked at it." Then: "Whatever that
interest number is, multiply it by the months you have left. That's your version of Marcus's
eight thousand nine hundred." **Declared mid-roll boundary at 5:20.**

**B9 · THREE WAYS THIS GOES WRONG (5:20–6:25, L055–L065).** (1) *Negotiating the payment instead of
the price* — the four-square move, where the price barely moves and the term does all the work
(sourced to V7's documented practice; `fin-facts` to re-source). (2) *The dealer markup* — the rate
you qualify for and the rate you are offered are not the same number; +1 point on this loan is
+$764 (the 2015 DOJ–Honda settlement is a citable public document; `fin-facts` to verify current
practice). (3) *Trading it in early* — at month 36 he owes $19,024, and if the offer is less than
that, the shortfall rolls into the next loan. **Flag honestly: whether he is underwater depends on
the vehicle, and this is the one claim in the video that needs a depreciation source.**

**B10 · THE COUNTER-CASE — the reward (6:25–7:35, L066–L077).** Same Marcus, same car, same rate,
**48 months instead of 72.** The payment: $830 — $234 a month worse. The interest: $5,842. The
delta: **$3,079 saved by the loan that felt unaffordable.** Rung it: "Twenty-four fewer payments.
The whole difference is the twenty-four months he was never going to enjoy anyway." Then the honest
second option for people who genuinely cannot carry $830: "keep the six-year loan and pay it like a
four-year one — the extra goes to principal, and the front-loading works in reverse."

**B11 · THE HONEST LIMIT (7:35–8:00, L078–L080).** "This math only works this way when the rate is
the same on both terms — and sometimes it isn't; lenders price long and short loans differently, so
check both before you assume the short one wins. And if a longer term is the difference between a
car that gets you to work and no car at all, take the longer term. This is arithmetic, not a moral
position."

**B12 · THE PLAN + THE LOOP (8:00–8:30, L081–L086).** Three steps: (1) decide the *price* before you
walk in, never the payment; (2) get the rate from your own bank first, in writing, so you have a
number to compare; (3) run both terms and look at the total, not the monthly. Then the loop:
"Step two only works if you know what rate you actually qualify for — and that was decided by a
file you've never read, before you ever walked in. That's the next one." **No recap.**

### 5a. What changes for the India / ₹ cut

**Beyond currency — five things, and the story example is one of them.**

1. **The instrument changes, because the audience is different.** A ₹28 lakh car on a six-year loan
   is not the worked example for a 20–28-year-old on a first salary (`money-facts-2026`: salaried
   average **₹24,217/month**, PLFS). The Indian version of the same *thesis* is the long-tenure EMI
   on a thing that is not an asset: a phone or an appliance on a 24-month **"no-cost EMI"**, or a
   used two-wheeler / small used car on a 5–7 year loan. **The mechanism claim must be re-sourced,
   not converted** — "no-cost EMI" hides its cost in a forgone discount plus a processing fee,
   which is a *different* mechanism from front-loaded amortisation and needs its own facts pass.
   **A ₹-converted $34,000 car is a hard fail** in the same way a rupee in an `-en` cut is.
2. **The character is different and named differently** — Rohit, not a transliterated Marcus, and
   the declaration is the §2c Hindi string. The mock-mythic pair form (Atapi/Vatapi) is available
   and is proven at 1.46M views on our exact adjacent topic; if used, it replaces the single
   character, not supplements him.
3. **The char budget forces the rewrite.** 510s × 12.5 c/s = **6,375 chars** vs the en cut's
   **8,211** — the Hindi cut has 22% less room for the same runtime. Translating the en script
   overruns by ~29% by construction. **This is the cheapest anti-isomorphism control available and
   it costs nothing to enforce.**
4. **Register: Hinglish, not textbook Hindi.** The VO says the term the screen says (audit §4 change
   #4). V1 — the 34× breakout — is the proof of the register.
5. **Different yardsticks, and a different B9.** The three failure modes are market-specific: the
   dealer-markup mode has no Indian equivalent as documented; the Indian modes are the no-cost-EMI
   discount swap, the top-up/personal loan on top of an existing EMI, and the "kitna EMI banega"
   framing that is the exact analogue of negotiating the payment instead of the price. **B9 is the
   beat that must be independently written per market**; B5–B7 (the ladder) share only their
   *shape*.

---

## 6. Retention over eight minutes

Every row: the drop, the evidence tier, and the structural device.

| Zone | What happens | Tier | Device |
|---|---|---|---|
| 0:00–0:30 | The steepest drop of the whole curve; sources converge on seconds **10–20** and 30–40% gone by 0:30 | **FACT (cited, creator-tier — directional only)**, already logged in audit §3b with four sources; `long_form_scripting.md` §13's caveat stands | B1–B2: situation + withheld outcome + guess. No definition, no self-introduction, **no chip roadmap**. |
| 0:30–1:15 | Promise verification — the viewer is deciding whether the title will be paid off | UNVALIDATED | B3 delivers a real number **before 1:15**. Five of eight benchmark videos pay something off inside 90s (FACT). |
| 1:15–1:45 | The classic "roadmap slot" | **FACT** that our shipped format spends 6–7% of runtime here restating the title (audit §3b) | B4: deferred **verdict** + reward tease. Enumeration banned. |
| 1:45–3:00 | The point where a 3-minute video is already over — the first genuinely new stretch | UNVALIDATED | B5 ladder: a new number every ~20s, one per line. This is the pattern V3/V4 use for exactly this stretch (FACT). |
| **3:00–3:45** | **The hardest zone at this length.** The novelty of the setup is spent and the payoff is not in sight | UNVALIDATED (no analytics; the vault's own §6 puts the peak drop at 55–65%, which at 510s is 4:40–5:30) | **B6 THE TURN** — the mandatory re-hook, and the only place the mechanism is named. Structural, not decorative: the video's logic actually changes here. |
| ~4:50 | The loss number lands (57%) | UNVALIDATED | B7's peak. The audit found the shipped format's peak at 65–81% was correctly placed; at 8:30 there is room for two peaks, and the first must come before the mid-roll. |
| **5:00–5:30** | **The mid-roll break.** FACT: mid-rolls need **8:00** minimum; 510s clears it by 30s (audit §4C, vidIQ/FluxNote) | FACT for the gate; UNVALIDATED for the placement effect | **B8 is a declared beat boundary at 5:20.** Put the *viewer task* here: an ad interrupting an instruction is survivable; one interrupting an argument is not. Nothing straddles the boundary — lines are atomic by construction. |
| 5:20–6:25 | The 55–65% drop zone proper | UNVALIDATED for us; **FACT** that the canonical skill §6 names it and prescribes opening it on tension | B9: three mini-loops. Each opens on tension, each carries its own number. No "let's move on". |
| 6:25–7:35 | The reward window (74–88%) | **FACT** that `long_form_scripting.md` §6 prescribes a teased reward at ~70% and that the shipped format hit 65–81% | B10: the delta. Teased in B4, so it closes a loop rather than adding a beat. |
| 7:35–8:30 | The end. **FACT: 0 of 8 shipped scripts opens a next-video loop**; all end on recap + SUBSCRIBE | FACT | B11 (honest limit — the memorable beat nobody in the niche writes) then B12 (plan + named next video). Recap deleted: peak-end says the flattest possible ending is a summary. |

**Three honesty notes on this table.** (1) Not one row is validated against our own retention curve,
because there isn't one — the first 8:30 cut's analytics are the first real data this project will
ever have on retention, and the note that reads them should be written before the video ships.
(2) The 5–7 STP loops per 10–15 min dosage in `long_form_scripting.md` §3 maps to this sheet as
**five loops** (B1→B3, B2→B3, B4→B10, B6→B7, B9→B12), which is at the low end for 8:30 —
UNVALIDATED whether that matters. (3) Chapters: skip them or add them, the benchmark says it is not
a lever (FACT, 5 of 6 breakouts and 4 of 8 in my set have none). If added, they must match beat
boundaries so the mid-roll lands at B8/B9.

---

## 7. The five changes `.claude/agents/fin-script.md` needs

Ranked by "fix the default, don't add a gate" (creator, 2026-07-29).

1. **Add the `story-ladder-12` contract for `tier: medium`, in the same table shape as §3.** Today
   the file says only *"MEDIUM / LONG — per-line chapter architecture … None of the 9-segment
   constants apply"* — which is an absence, not a format, and an absence is why six consecutive
   blockframe-9s shipped. Give it: 12 beats, per-beat second windows and line counts, the char
   budget (`target_seconds × cuts.<cut>.chars_per_second`, ±10%), and a numbered line index
   (`L001…`) so the build maps 1:1 and `pipeline_check.py` can assert `lines × avg_chars` against
   the budget. Register the architecture in `format.json.architectures` so the rotation can select
   it.
2. **Write the illustrative-character contract in, as rules not prose** (§2b/§2c): named composite,
   declaration string **inside the first 25 seconds** (grep-checkable), every number about him
   traced to `facts-staging.md`, **no testimony**, the twin is the same character with one variable
   changed, a different name per video *and* per cut. Add the ban: a character presented as real,
   as a friend, or as a viewer's letter is a hard fail.
3. **Replace "read the Hindi script only for structure" with a transfer whitelist.** May transfer:
   the thesis, the beat sheet, the mechanism, the *role* each number plays. May **not** transfer:
   the character's name, the analogies, the yardsticks, the sentence order, the on-screen copy, the
   B9 failure modes, or the worked example's instrument if the market's instrument differs.
   Enforce the char budget per cut (en 8,211 / hi 6,375) — at 22% apart, a translation cannot fit,
   which is a control rather than a warning.
4. **Ban the fingerprint strings and mandate the tail.** Forbid `Four things:`, `DO THIS TODAY`,
   `Then don't say nobody warned you`, `तो बात सीधी है` as opener/closer (audit §1: 4/4, 8/8, 4/4,
   4/4). Require: **no recap beat**, an honest-limit beat, and a **named next-video loop** naming a
   real slug from `vault/videos/` (0 of 8 today). Add the `-hi` register rule: if the on-screen text
   uses the English term, the VO says the English term.
5. **Rule the arithmetic-as-story constraints** (§2d), because they are what make the middle
   readable: one number per line; every number answers the previous line's question; a
   guess-before-reveal line before the largest number; the unit flip; **one mechanism per video,
   at most three named terms** (§4a); the mechanism named only after three rungs; and the final
   number is a **delta**, never the loss.

**Dependency outside this file (blocking):** `max_elevenlabs_calls: 30` →
**≥ 220** in `.claude/commands/finance-video.md:70`. 86 lines × 2 cuts + retries. Config guard, not
a vendor limit; per-character billing means the raise costs nothing by itself.

---

## 8. What this contradicts in the vault

1. **`vault/skills/long_form_scripting.md` §0 and §2 describe a different channel.** They assume
   the creator's own recorded human voice, screen recordings, tool reviews, affiliate CTAs, honest
   verdicts on products, and *"I tested"* integrity — every one of which is either unavailable
   (human voice, first person) or banned (product picks, persona) on the finance channels. The
   structural halves (§3 arcs, §4 hooks, §6 retention, §7 psychology, §10 analogies) transfer;
   §0, §1.1–1.3, §5 affiliate, §8 delivery, §11.5 do not. **`fin-script.md` currently reads this
   file every run as its canonical creative skill with no map of which parts apply.** FACT.
2. **The vault's own benchmark contains a counter-example to the story premise, and it is the
   benchmark's strongest data point.** Easy Life With Monika (v/sub **34.45**, the highest in the
   set) is 8m13 of a *ten-item list with no story, no hook, a spoken table of contents, and almost
   no numbers* — it does four things §4/§6 of `long_form_scripting.md` call failures. **FACT**
   (measured from the transcript). The runtime finding survives this; the *story* recommendation is
   a design choice, not a data conclusion, and should be labelled as such wherever it is written
   down. The cheap A/B is a "10 things" utility cut at 8:30 against a story cut at 8:30.
3. **`01-performance.md` §3d says the faceless cohort is "essentially absent from the traction
   set". Two faceless positives now exist.** Zerodha Varsity Hindi (`Sfsdf-iKiwQ`, faceless
   animation + VO, 11m52, v/sub 1.00) and GIGL (`KojTmd3vYoM`, faceless animation + VO, 10m23,
   1.5M views) — and both use the exact story device recommended here. FACT. The gap is narrower
   than that note states; the honest residual is that neither is stock-photo-based and neither is a
   *small* channel breaking out (Varsity's absolute numbers are small; GIGL has 7.17M subs).
4. **`02-script.md` §4C costs option C at "~4× the sourced claims" and "medium" difficulty. On this
   beat sheet that is wrong in both directions.** Facts get *cheaper* per minute — B5/B7/B10 all run
   off one locked input set plus a build calculator, so an 8:30 story needs ~4–6 sourced claims
   versus blockframe-9's nine independent beats — while the **binding cost is the 86-line TTS call
   budget and ~2× image sourcing**. FACT (derived from the beat sheet; the audit's estimate assumed
   a per-line script implies per-line facts).
5. **`us-english-script-style.md` mandates keeping the sign-off *"then don't say nobody warned
   you"* as channel signature.** At 8:30 with a mandated next-video loop and no recap beat, that
   phrase has no slot left — and it is 4/4 verbatim across the en cuts. It should be retired or
   demoted to at most one video in three. FACT that it conflicts; UNVALIDATED that dropping it
   costs anything.
6. **`niches/us-market-2026.md` rule 1 versus §3c of the performance audit remains unresolved, and
   this note resolves the part it can.** The illustrative-character form in §2 needs no first
   person, no credential and no persona, so it is reachable under the rule as written. What is
   *not* reachable is the stated-emotion opinion opener ("what drives me crazy") that the highest
   v/sub US videos use. That tension stands; nothing here overrides the policy note.

---

## Sources

Retrieved artifacts (yt-dlp 2026.06.09, 2026-07-30) — transcripts in
`…/scratchpad/research/tx/`:
`MTtBq6dG6m0` · `vO_Ce1BdOro` · `Sfsdf-iKiwQ` · `KojTmd3vYoM` · `ZU9ZpVlvwkE` · `-uAOI6yJgm4` ·
`rIi3YI0zmNI` · `ERxrOOapNV4`.

In-repo: `vault/knowledge/finance-audit-2026-07-29/{01-performance,02-script}.md` ·
`vault/skills/long_form_scripting.md` · `vault/knowledge/{us-english-script-style,niches/india-finance-market}.md` ·
`vault/videos/good-debt-vs-bad-debt/script-{en,hi}.md` · `tools/format.json` ·
`.claude/agents/fin-script.md` · `.claude/commands/finance-video.md`.

External (creator-tier, directional only — carried over from audit §3b/§4C, not re-verified here):
PrePublish, Miraflow, Overseeros, Artiphik on the first 30 seconds; vidIQ and FluxNote on the
8-minute mid-roll gate.

**No claim in this document is validated against channel analytics, because none exist.**
