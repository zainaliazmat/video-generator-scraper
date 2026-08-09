# 08 — Packaging (title / thumbnail / description) + platform & policy risk

Scope: everything the viewer sees **before** pressing play, plus platform risk.
Date: 2026-07-29. Repo read-only; nothing under `/home/zain-ali/Documents/YoutubeScraper` was modified.

Every claim is tagged **FACT** (a spec, a primary source, a public number, a policy
document, or an artifact I opened myself) or **UNVALIDATED** (an untested belief about
audience response). **There are no analytics for these channels — no CTR, no
impressions, ever.** Nothing below is calibrated against performance, and anything that
claims to be is lying.

---

## 0. What I actually looked at

**FACT** — files read: `.claude/agents/fin-package.md`; publish packs for
`good-debt-vs-bad-debt` (hi+en), `credit-history` (hi+en), `needs-vs-wants` (hi);
`vault/knowledge/{channels,monetization,best-practices,design-finance-blockframe}.md`;
`vault/knowledge/niches/{us-market-2026,india-finance-market}.md`;
`tools/format.json`; `vault/workflows/finance-video.md`; `vault/CLAUDE.md`.

**FACT** — thumbnails I opened as images (not descriptions of them):

| File | Cut |
|---|---|
| `vault/videos/needs-vs-wants/src/hi/thumbnail-hi.png` | hi |
| `vault/videos/needs-vs-wants/src/en/thumbnail-en.png` | en |
| `vault/videos/emergency-fund/src/thumbs/thumbnail-hi.png` | hi |
| `vault/videos/emergency-fund/src/thumbs/thumbnail-en.png` | en |
| `vault/videos/50-30-20-rule/src/hi/thumbnail-hi.png` | hi |
| `vault/videos/pay-yourself-first/src/thumbs/thumbnail-hi-v2.png` | hi |
| `vault/videos/pay-yourself-first/src/thumbs/thumbnail-en-v2.png` | en |
| `vault/videos/good-debt-vs-bad-debt/src/thumbs/thumbnail-hi-v2.png` | hi (shipped) |
| `vault/videos/good-debt-vs-bad-debt/src/thumbs/thumbnail-en-v2.png` | en (shipped) |
| `studio/videos/credit-history-thumbs/thumbnail-{hi,en}-v2.png` | unshipped |

**FACT** — I could **not** reach the live YouTube pages. `curl` to
`i.ytimg.com` / the oEmbed endpoint returns `Forbidden` from this sandbox, and WebFetch
on `youtube.com/@cashguruguides/videos` returns only YouTube's page footer.
`maxresdefault.jpg` 404s for all ten IDs. So the *published* thumbnails were assessed
from the archived PNGs in `vault/videos/*/src/thumbs/`, which the vault's finished-video
rule states are byte-verified copies of the shipped deliverable. **Live view counts,
publish dates and the actual rendered channel grid are unverified.**

---

## 1. POLICY RISK — real policy vs. speculation

This is the section that matters most, so it is first, and every line is sourced.

### 1.1 What is REAL POLICY (primary sources only)

**FACT — the policy text.** YouTube channel monetization policies,
`support.google.com/youtube/answer/1311392`, last updated **15 July 2025**. That update
was a **rename**, not a new rule: "repetitious content" → **"inauthentic content"**,
defined as content that is *"mass-produced or repetitive."* The page requires content to
*"Be your original creation"* and *"Not be mass-produced, generic, repetitive, or
manipulative."*

**FACT — the three buckets, clarified July 2026.** On **16 July 2026** YouTube's trust
and safety lead **Matt Halprin** explained the policy in a **Creator Insider** video
(`youtube.com/watch?v=14Vm0CiyUVE`), reported by TechCrunch 20 July 2026. The three
categories that make a channel ineligible:

1. **Generic or repetitive content** — *"Similar or repetitive content with low
   educational value"*, *"Videos where characters are put in the same situation over and
   over again"*, *"Image slideshows, templated storylines, or scrolling text"*,
   *"AI-generated content made with generic or unoriginal templates."*
   Explicitly **allowed**: *"Same intro and outro for your videos, but the bulk of your
   content is different"*, and series where each episode has a *"distinct storyline,
   focus, or concept."*
2. **Unsatisfying or off-putting content** — content *"designed to shock or surprise
   viewers for the sole purpose of getting views."*
3. **AI personas related to sensitive topics** — channels using *"AI-generated personas
   to deliver information on sensitive topics"* (health, legal, financial, political)
   *"will not be allowed to monetize."* Named examples: *"An AI 'doctor' providing
   medical diagnoses"*; **"AI-generated podcast hosts offering financial guidance,
   investment tips, or wealth management advice"**; AI personas giving legal advice.

**FACT — AI is not the trigger.** YouTube: the policies are *independent of whether
content is made using generative AI, CGI, stock footage or other tools*. The
monetization page also permits *"Content that utilizes creative tools to assist in
delivering a unique, well-researched, or creative narrative, like using AI to edit your
video scripts or generate a unique background visual."*

**FACT — enforcement level.** The policy states monetization *"may be removed from your
entire channel."* Channel-level, not video-level.

**FACT — disclosure rule.** `support.google.com/youtube/answer/14328491`. Disclosure is
required for content that is **realistic and meaningfully altered or synthetically
generated**. The Studio upload question presents exactly three checkboxes: *"Makes a
real person appear to say or do something they didn't say or do"*, *"Alters footage of a
real event or place"*, *"Generates a realistic-looking scene that didn't actually
occur."* Explicit non-disclosure examples include *"Cloning one's own voice to create
voice overs or dubs"*, *"Caption creation"*, beauty/colour/blur filters, and
*"Production assistance, like using generative AI tools to create or improve a video
outline, script, thumbnail, title, or infographic."*

**FACT — disclosing costs nothing.** YouTube, same page: *"Disclosing AI content won't
limit a video's audience or impact its eligibility to earn money."* Repeatedly failing
to disclose when required can lead to label imposition, content removal, or **YPP
suspension**.

**FACT — the one primary sentence that cuts against the vault's reading.** YouTube's own
blog, *"How we're helping creators disclose altered or synthetic content"*,
**18 March 2024**, under the heading **"Using the likeness of a realistic person"**,
lists as requiring disclosure: *"Digitally altering content to replace the face of one
individual with another's **or synthetically generating a person's voice to narrate a
video**."* The current Help Centre exempts only *cloning **one's own** voice*. So the
platform has published two differently-scoped statements about synthetic narration and
has never reconciled them in writing.

**FACT — no finance category in the ad guidelines.** The advertiser-friendly content
guidelines (`answer/6162278`) contain **no** category for financial content, investment
advice, debt, credit or get-rich-quick. The 14 categories are language, violence, adult,
shocking, harmful acts/unreliable content, hateful, drugs, firearms, controversial
issues, sensitive events, enabling dishonest behavior, kids/families, tobacco,
incendiary/demeaning.

**FACT — appeal / reapply mechanics.** A monetization decision can be appealed; if not
appealed or unsuccessful, a channel may reapply to YPP after **90 days**.

### 1.2 What is SPECULATION (do not treat as policy)

- **UNVALIDATED — "YMYL" is not a YouTube policy.** "Your Money or Your Life" is a
  concept from **Google's Search Quality Rater Guidelines**, used by human raters to
  evaluate *Search* results. Google states rater data is **not used directly in ranking
  algorithms**, and the term appears nowhere in YouTube's monetization or community
  guidelines. Any recommendation framed as "YouTube requires E-E-A-T / YMYL compliance"
  is importing a Search concept into a platform that does not use it.
- **UNVALIDATED — "finance channels need credentials to monetize."** No YouTube policy
  requires credentials for finance content. Bucket 3 prohibits **AI personas presenting
  as experts**, which is a different rule: it targets the *persona*, not the *topic* and
  not the *narration*. Everything I found asserting a credential requirement was SEO
  blog content (quasa.io, vexub, influenceflow, mediacube, tubebuddy) with no primary
  citation.
- **UNVALIDATED — "a disclaimer protects you."** No primary source says a description
  disclaimer changes eligibility either way. It is good practice and costs nothing; it
  is not a shield.
- **UNVALIDATED — the specific enforcement numbers already flagged in the vault** (the
  "last 30 uploads" review window; the "Jan 2026: 16 channels / 35M subs terminated"
  figure). `us-market-2026.md` correctly refuses to repeat these. I found no primary
  source for either. That refusal is right; keep it.
- **UNVALIDATED — every "how many similar videos before you're flagged" number.** YouTube
  has published no threshold. The vault's "5th consecutive is the line, 6th is
  indefensible" is a **self-imposed internal control**, not a platform rule. It is a
  good control. It should not be described as if YouTube set it.

### 1.3 Plain risk assessment for @cashguruguides and @moneymavens101

**Bucket 3 (AI persona) — LOW, and the vault's 2026-07-28 resolution is correct.**
**FACT**: there is no named presenter, no first-person expertise, no product/fund/card
pick, and an explicit education-not-advice disclaimer in every description I read. The
prohibited example is an *"AI-generated podcast host offering financial guidance,
investment tips, or wealth management advice"* — narrating cited RBI/CFPB/Federal
Reserve figures with no recommendation is not that. **Keep all of it.**

One residual, not in the vault: **FACT** — both channel *names* assert expertise.
"CashGuru**Guides**" and "money**Mavens**" both mean "expert". **UNVALIDATED** — a
reviewer landing on a channel called CashGuruGuides, narrated end-to-end by a synthetic
voice, on financial topics, is being invited to read a persona that the scripts carefully
avoid. The names are not changeable cheaply; the **About section is**, and neither
channel has one. `vault/knowledge/channels.md` documents a written About description for
channels **A (TechToolTester)** and **B (HistoryFramesFilm)** and **none for D or E.**

**Bucket 1 (generic / repetitive / templated) — THIS IS THE REAL EXPOSURE, and it is
worse than the vault records.** The vault's own packs already flag it hard and correctly:
six consecutive blockframe-9 cuts per channel, nine beats in the same order every time,
five of six inside a 13-second runtime band (2:46–2:59). The `credit-history-en` pack's
diagnosis is the best thing in the vault — *the control is in the wrong place; a gate
that fires after the artifact is finished cannot change the artifact.*

**What the vault does not say, and what I own:** the sameness is not only in the
architecture. **It is in the packaging, which is the part a reviewer sees first.**

**FACT** — I opened **all ten shipped thumbnails** (both cuts of all five published
pairs) plus the two unshipped `credit-history` ones. **All ten shipped thumbnails share
one literal layout**:

```
[ coloured pill, top-left, ~11 chars, all-caps ]
[ WHITE condensed caps line ]
[ RED condensed caps line — the mega ]
[ small white sub-line with one coloured word ]
[ optional 12-segment horizontal bar ]
--------  photo, right ~55%, under the same grayscale(0.32) brightness(0.62) grade
```

Same font, same weight, same left margin, same dark `#0d1017` field, same red `#ef4444`
mega, same photo treatment. Only the words and the number change. The tenth
(`credit-history-en-v2`) swaps the sub-line for a two-row comparison table and is the
single genuine variation across the whole run.

**FACT** — the policy's own wording for bucket 1 is *"content that looks like it's made
with a template with little to no variation across videos."* A channel page is a grid of
thumbnails. **The thumbnail grid is the most efficient possible exhibit for that
sentence**, and it is the first thing any reviewer — or any viewer — sees.

**FACT** — `fin-package.md`'s sameness check is structurally incapable of catching this.
It compares the new thumbnail against "the channel's last 3" and asks whether *the number
and the scene photo* are near-identical. Varying the number while holding the layout
fixed **passes** that check every time, and that is exactly what happened ten times. The
good-debt-hi pack concludes *"no near-duplicate here"* — true on its own criterion, and
irrelevant to the criterion that matters.

**FACT** — cross-channel, the two channels have now shipped **the same six topics, in the
same order, in the same architecture, in the same runtime band, with the same thumbnail
grammar**. The `credit-history-en` pack makes this observation itself and correctly notes
sameness is judged per channel — but it also means the two-channel structure provides
**zero diversification** against the one risk that can end both.

**Disclosure — MEDIUM, and I disagree with how confidently the vault states it.**
The packs assert, in identical wording across six files: *"Altered-content disclosure
toggle: set 'No'."* On the **Studio question as actually worded** (the three checkboxes),
that is defensible: motion graphics over licensed stock photography makes no real person
appear to say anything, alters no real event, and generates no realistic scene. I would
answer "No" too.

But it is stated as a settled fact and it is an **interpretation of a rule YouTube has
scoped two different ways in two primary documents** (§1.1). The asymmetry is what
matters: the cost of being wrong is *systematic* non-disclosure across every upload on
two channels — which is precisely the pattern YouTube says can lead to YPP suspension —
and the cost of hedging is, by YouTube's own published statement, **zero**.

The `credit-history-en` pack argues against disclosing on the grounds that *"an
unnecessary disclosure invites the question of what was synthesised."* **UNVALIDATED** —
that is an untested belief about viewer response, presented in a compliance section as a
reason not to comply. It should be labelled as the opinion it is.

**Buckets: unsatisfying/off-putting — LOW.** Sourced, calm, no shock-farming, no
emotional manipulation. Nothing to fix.

### 1.4 Concrete steps that reduce the risk (ordered by value ÷ effort)

1. **FACT-grounded, ~15 min, highest value:** write an About description for **both**
   channels (neither has one) that states in plain words: (a) the narration is
   AI-generated, (b) the content is general financial education, not advice, (c) no
   product, bank or fund is recommended, (d) sources are cited on screen. This
   simultaneously answers the channel-name problem, pre-empts a bucket-3 reading, and
   removes any "concealment" framing from the disclosure ambiguity — without touching the
   Studio toggle. Owner: `vault/knowledge/channels.md` (the file already has the format,
   for channels A and B). Cost: one edit, no re-render.
2. **Break the packaging template before the next upload.** The architecture break is
   already owed and already owned (`run.json` `tier`); the *thumbnail-grid* break is not
   owned by anyone. Add to `fin-package.md`'s sameness check: compare **layout**, not
   just the number and photo — pill present/absent, text alignment, mega colour, number
   position. Reject a third consecutive identical layout. Cost: a few lines in one agent
   prompt.
3. **Add a one-line AI-narration credit to the description template** (e.g. "Narration:
   AI-generated voice. Written and fact-checked by a human."). Not the Studio toggle,
   not a policy label, no monetization effect, kills the concealment reading. Cost:
   one line in the description block `fin-package` already writes.
4. **Stop describing the internal sameness rule as a YouTube rule.** In
   `us-market-2026.md` and in every pack, "the 5th consecutive crosses the enforcement
   line" reads as a platform threshold. It is a house rule. Label it as one, so nobody
   later "discovers" that YouTube never said it and discards the whole control.
5. **Record the actual upload date and confirmed-live URL per cut.** The
   `credit-history-en` pack flags this itself: the production sequence and the published
   sequence have drifted, so the channel-level sameness count is ambiguous. A sameness
   control that cannot count its own inputs is not a control.

---

## 2. The real packaging, judged

### 2.1 Titles — what's working

**FACT** — the title research method in these packs is genuinely good and is the
strongest part of the whole packaging stage. Every pack pulls live YouTube autocomplete
per market (`tools/autocomplete.py`, `gl=in hl=hi` / `gl=us hl=en`), **records empties as
empties**, and titles into a verified demand cluster rather than the internal slug. The
`needs-vs-wants-hi` pack's finding that *"needs vs wants" is a children's keyword* and
must stay out of the title is exactly the kind of thing most channels never discover. The
`good-debt-hi` finding that `acha karz aur bura karz` returns **no suggestions** while
`good debt vs bad debt in hindi` does is a real, load-bearing result.

**FACT** — packs also correctly refuse high-volume clusters that mismatch the video
(`cibil score kharab hai` → wants "how do I still get a loan"; `delete late payment from
credit report` → wants removal of accurate marks). Refusing traffic on retention grounds
is the right instinct and rare.

**FACT** — title lengths of the six live titles: 63, 60, 65, 67, **80**, 61 characters.
Five sit in a sane band. One does not.

### 2.2 Titles — what's formulaic

**FACT** — every *recommended* title in every pack is built from the same two parts:
`[verified autocomplete cluster] + [hero number]`, joined by a colon or an em dash.

```
Credit Card Minimum Payment: Ek Jaal — ₹50,000 par ₹88,614 Byaj
The Credit Card Minimum-Payment Trap: $6,000 Costs You $9,506
CIBIL Score Kya Hota Hai? Ek Missed EMI = 36 Mahine
How Long Do Late Payments Stay on Your Credit Report? 7 Years
Har Saal ₹24,564 Chup-Chaap Gayab — Aapke Subscriptions Ka Sach
You Think You Spend $86 a Month on Subscriptions. It's $219.
```

That is one shape, six times. **UNVALIDATED** — whether this hurts click-through is
unknowable without analytics. **FACT** — it *does* mean the channel page reads as six
variations of one sentence, which compounds the bucket-1 packaging problem in §1.3. The
titles are individually well-researched and collectively siblings.

**FACT — the emergency-fund-hi title is the one clear defect:**
`One Repair From Broke — Emergency Fund Explained in Haryanvi | Start With ₹2,500`
— **80 characters** (the longest by 13), and it is in **English**, not Roman-Hindi, on a
channel whose stated convention is Roman-Hindi. Worse: **FACT** — it advertises
"Explained in Haryanvi", and `india-finance-market.md` records that Haryanvi was
**retired** as the finance register on 2026-07-28; the channel voice is now standard
Hindi (Harsh). The title now mis-sells the one thing a returning viewer would use it to
predict. A retitle is a 30-second Studio edit with no re-render.

### 2.3 Is Roman-script Hindi right for Indian search? — YES, and the vault contradicts itself on this

**FACT — the pipeline's own evidence settles it.** Autocomplete strings verified live by
`tools/autocomplete.py` (`gl=in, hl=hi`, 2026-07-27/28/29), all in **Roman script**:

```
credit card minimum payment kya hota hai      credit card ka byaj kitna lagta hai
credit card ke jaal se kaise bache            good debt vs bad debt in hindi
cibil score kitna hona chahiye                cibil score badhane ka tarika
paise kaise bachaye                           bachat kaise kare
auto debit kaise band kare                    upi autopay kaise band kare
fizul kharchi se kaise bache                  ghar ka kharcha kaise kam kare
```

**FACT** — and the pure-Hindi-vocabulary equivalents returned **nothing**:
`acha karz aur bura karz` → no suggestions. `how minimum payment works` (plain English)
→ no suggestions. So for India finance, the register people actually type is **Roman
Hinglish** — not English, not Devanagari. The creator's Roman-title rule is correct and
is now evidence-backed rather than a preference.

**CONTRADICTION IN THE VAULT — `vault/knowledge/best-practices.md`** states, as a
standing rule: *"Urdu/Hindi market searches in ENGLISH keywords + 'in urdu/hindi' —
tags/titles must ride English search strings; Roman-Urdu phrases don't autocomplete."*
That was generalised from **one Urdu history video** (Pompeii, 2026-07-18). The finance
packs' own pulls refute it for this market and this niche. Any future agent reading
best-practices.md for title guidance gets the wrong answer.

**CONTRADICTION IN THE VAULT — `vault/knowledge/niches/india-finance-market.md`** still
says *"Titles/descriptions: English (unchanged rule)"*. Stale. The live titles are
Roman-Hinglish and the creator rule superseded it.

**The one thing Roman-only leaves on the table.** **FACT** — a Roman title is not
findable by a viewer typing Devanagari. YouTube's multi-language metadata
(`support.google.com/youtube/answer/13338784`) lets a video carry **translated titles and
descriptions**, and YouTube states: *"Once your videos are translated, your videos can be
found when viewers search using a translated video title and description"*, with the
localized version shown to viewers whose language setting matches. It also supports
**localized thumbnails** (*"Viewers will be shown thumbnails that match their language
setting"*). So the hi channel can keep the Roman title as primary — readable by everyone,
which is the whole point of the creator's rule — and add a **Devanagari localized
title + description** that only widens search reach. No re-render, no design change.

---

## 3. Thumbnails

### 3.1 Is the v2 style a channel signature, or indistinguishable from itself?

**Both — and which one it is depends entirely on whether the viewer already knows the
channel, which at this size neither channel does.**

**FACT** — the composition is genuinely well-made: WCAG-AA checked, legibility asserted
at 320×180 (largest line ≥40% width), backgrounds are the video's own re-graded scenes so
the thumbnail and the film are one object, every numeral traced to the script. That last
rule — *"every numeral on the thumbnail must appear in the script"* — is better discipline
than most professional channels have. **Do not weaken any of it.**

**FACT** — and nine of ten thumbnails are the same layout with different words (§1.3).
The channel does not yet have the audience recognition that makes a rigid template an
asset. A signature works when a viewer scrolling their home feed thinks *"that's them
again"*. Before that point, an identical layout on every card produces the opposite: the
row of your own videos in a search result or a "from this channel" shelf reads as one
video repeated.

**UNVALIDATED** (no analytics, and this is a judgment) — at thumbnail size the only
element that resolves is the **red mega line**, 2–3 words. Everything else — the pill,
the sub-line, the 12-tick bar, the photo behind a `brightness(0.62)` grade — is below the
resolution the viewer gives it. So the channel is currently spending its whole design
budget on elements that do not survive to the decision, and the *one* element that does
survive is styled identically every time.

**The lazy fix is not a redesign.** It is: hold the design system (grade, font, palette,
discipline), and **vary the one thing that resolves**. Rotate which element is the mega —
a ₹/$ figure, a time span ("17 SAAL"), a flat statement ("EMPTY BY THE 20TH?"), a
two-row comparison (`credit-history-en-v2` already proves this works inside the system).
Rotate the mega's position. Rotate white-dominant vs red-dominant. The `credit-history-en`
thumbnail is the existing proof that variation is available **without** leaving the design
system — it is the only one of the ten I would not have guessed the layout of in advance.

**FACT — a rule in `fin-package.md` is not being followed.** *"Language: `hi` thumbnails
use Roman-script Hindi."* `emergency-fund/src/thumbs/thumbnail-hi.png` ships in
**Devanagari** ("एक झटका / अर तू कंगाल"). Every other hi thumbnail is Roman. Either the
rule or the artifact is wrong; right now the vault records the rule and the channel shows
the exception.

**FACT — the pill colour is inconsistent and carries no meaning across videos.** Green on
`emergency-fund` (both cuts), `50-30-20-hi` and `credit-history-en`; red on
`needs-vs-wants`, `pay-yourself-first-en`, `good-debt` (both); amber on
`credit-history-hi`. The design note is explicit that *"semantics are per-video, derived
from the thesis — not a channel rule"*, so this is internally consistent by design. Worth
knowing, not worth fixing.

**FACT — the thumbnail spec has no home in the vault.** `design-finance-blockframe.md` is
the channel's "durable design system" and contains **zero** mentions of thumbnails. The
entire thumbnail specification lives inside `.claude/agents/fin-package.md`. That
directly violates `vault/CLAUDE.md`'s own rule: *".claude/agents/ is procedure, not
memory… every fact lives in tools/format.json or a vault note."* The v2 style is a fact
about the channel, not a procedure of the packaging stage.

### 3.2 Do the two markets want different thumbnail logic?

*(See §6 for the market research findings and their evidence grade.)*

The structural point I can make from the artifacts alone: **FACT** — the two cuts today
receive *identical* thumbnail treatment — same layout, same palette, same type, same
grade — differing only in currency glyph and language. That is a production convenience
(one HyperFrames project, `§v1/§v2/§v3` for hi and `§env1/…` for en in one `index.html`),
not a market decision. **UNVALIDATED** — whether an Indian home feed and a US home feed
reward the same visual grammar. What is certain is that the current answer was never
chosen; it fell out of the build.

---

## 4. Descriptions, tags, chapters and the rest of the pack

### 4.1 What the pack has now (all FACT, read from the files)

- **Description**: 3 prose paragraphs (hook → what's inside → the one-line thesis).
  Well-written, market-native register (Hinglish for hi, plain American for en).
- **Chapters**: 9, real timestamps read from `assets/voice/timing.json` `scene_start`,
  floored to the second, first at 0:00, all ≥10s apart. **Verified against the render's
  ffprobe duration.** This is done properly and most channels fake it.
- **📊 SOURCES block**: every figure with its source (RBI norms + issuer MITC; CFPB
  Regulation Z; Federal Reserve G.19). Genuinely unusual for the niche.
- **⚠️ Disclaimer**: education-not-advice, no product recommended, "run your own number".
- **Hashtags**: 4–5 at the end.
- **Tags**: 15–18, autocomplete-verified, market-segregated (no Hindi strings in the en
  pack, no US strings in the hi pack), under the 500-char limit.
- **Gate 2 block**: disclosure toggle, category, language, made-for-kids, sameness audit,
  a pinned-comment suggestion, an end-screen note, and (in the newer packs) an
  "If this underperforms" lever list.

### 4.2 What a 2026 upload should carry and this one doesn't

Ranked by **effort ÷ value**. All FACT unless marked.

| # | Missing | Why it matters | Cost | Owner |
|---|---|---|---|---|
| 1 | **Subtitles / SRT** | Not mentioned in a single pack (`grep` for subtitle/caption across all 11 packs: **0 hits**). The VO lines (`assets/voice/*.txt`) and per-line timings (`timing.json`) are already on disk and already archived — an SRT is a mechanical join of two files the pipeline already produces. Auto-captions on synthetic Hindi narration are the weakest link in accessibility *and* in what YouTube can index. | ~20 lines in `tools/`; zero API spend | `tools/` + `fin-package` writes the path into the pack |
| 2 | **Native A/B test instructions** | **FACT**: YouTube's own Test & Compare (`support.google.com/youtube/answer/16391400`) now tests **up to 3 titles and/or thumbnails**, decides on **watch time** (not CTR), typically resolves in ≤2 weeks, desktop Studio, requires advanced features, excludes Shorts/kids/private/age-restricted. The pipeline already generates 4–5 researched title options and then throws four away. The creator's "one thumbnail" rule saves render cost and is fine — **but the title test is free.** | one `test:` block in the pack | `fin-package` |
| 3 | **Devanagari localized title + description (hi)** | §2.3. Widens search reach without changing the displayed Roman title. Localized thumbnails are also supported. | one extra metadata block per hi cut | `fin-package` |
| 4 | **Pinned comment as a copy-paste artifact** | Every pack *writes* a good pinned comment — inside the Gate 2 prose, where it reads as analysis rather than a thing to paste. It is the cheapest retention/engagement lever there is and it is currently buried. | move 2 lines | `fin-package` |
| 5 | **Playlists** | Zero mentions across all 11 packs. Six topics on each channel are one obvious series ("Money Basics"). Playlists are the only structural way a browse-led channel gets a second view from the same session. One-time setup, then one dropdown per upload. | ~10 min once | creator / `channels.md` |
| 6 | **Cross-channel link in the description** | Every pack's Gate 2 says "cross-link the sibling cut" — and **no description block contains a single URL**. `grep http` across all descriptions: 0 hits. The instruction exists; the artifact doesn't implement it. **UNVALIDATED** whether an Indian viewer wants the US cut (probably not) — but the *creator's own channel* link belongs there regardless. | one line | `fin-package` |
| 7 | **End screens / cards** | Mentioned as a note ("cross-link the -en cut when it ships"), never specified as timings. **FACT**: the render has a 1.0s tail (`format.json` `scene.tail_seconds`) — an end screen needs ≥5s of held frame to be usable. Today the videos are technically too tight at the end to carry one. This is a *build* constraint, so it needs the build agent, not just the pack. | needs a render change | `fin-build` / `fin-render` (flag only — not my scope to design) |
| 8 | **Shorts cut-down** | **UNVALIDATED** as a discovery lever for these channels. **FACT**: scene 7 (the math counter) is a self-contained beat with its own VO line and its own hero number — it is the natural 30–45s vertical. But it needs a 9:16 re-layout and a re-render, so it is the most expensive item here, and A/B testing is unavailable on Shorts. Genuine value, genuinely not cheap. | high | new stage; do not add until #1–6 are done |
| 9 | **Community posts** | Zero mentions. **UNVALIDATED** value at zero subscribers — the feature needs an audience to be worth anything. Correctly skipped for now; revisit at ~500 subs. | — | — |

### 4.3 Two channel-level items nobody owns

- **Branding watermark.** **FACT** — YouTube Studio → Customization → Branding lets a
  channel set a 150×150 image that overlays every video and is **clickable to
  subscribe** on desktop; display timing is configurable (whole video / last 15s /
  custom start). The "no logo or brand mark" rule is **not** a blocker: a plain
  "SUBSCRIBE" graphic in the channel's own type and palette satisfies it without
  inventing a logo. One-time, both channels, ~10 minutes total.
- **The description fold.** **UNVALIDATED** (blog sources only, but directly observable)
  — roughly the first ~150 characters of a description render before "Show more", and
  YouTube surfaces the **first 3 hashtags** from anywhere in the description above the
  video title. The packs already open with a strong first sentence and put hashtags last,
  so both behaviours are being served correctly by accident. Worth recording so nobody
  "fixes" it by moving the hashtags to the top.

**One thing to leave alone: tags.** **UNVALIDATED** — tags have had negligible ranking
weight for years and no primary source claims otherwise. The packs' tag work is
meticulous and is probably the lowest-yield rigour in the whole stage. It costs nothing
to keep, so keep it — but do not spend more effort there, and do not treat
"autocomplete-verified tags" as a discovery strategy.

---

## 5. Titles as a system — a formula a pipeline can execute without producing siblings

### 5.1 The design problem

A single formula **guarantees** siblings. The current implicit formula
(`[autocomplete cluster] + [hero number]`) produced six titles with the same skeleton.
Replacing it with a better single formula produces six new siblings.

The fix is a **rotation with a disqualification rule**, which is one field of state:

> **`fin-package` picks a title SHAPE. The shape used by this channel's previous upload
> is disqualified.** Record `last_title_shape` per channel in `run.json`.

That is ~3 lines of pipeline change and it makes sibling titles *structurally impossible*
rather than a thing an agent is asked to remember. Everything else stays: autocomplete
evidence still chooses *which* shape is supportable, and the number still has to be in
the script and on the thumbnail.

### 5.2 The four shapes (both markets)

| Shape | Skeleton | When the evidence supports it |
|---|---|---|
| **A — QUERY** | verbatim autocomplete question, then the specific answer | a deep informational cluster exists (`cibil score kitna hona chahiye`, `what happens if you only pay the minimum`) |
| **B — PRICE TAG** | the hero number *is* the proposition; subject stated plainly | the video's math is the differentiator and the number is calculator-locked |
| **C — CONTRADICTION** | a rule the viewer already believes, then broken | a named concept is owned by a bigger channel (Warikoo, Kiyosaki, Ramsey) — attack the concept instead of competing for it |
| **D — INSTRUCTION** | an action plus a constraint or deadline, **no shock number** | the video's payoff is a routine, not a revelation |

**Hard constraints, both markets** (all machine-checkable):
≤60 characters · **exactly one** number · that number appears in the script *and* on the
thumbnail · no `₹` in `-en`, no `$` in `-hi` · the first 45 characters must stand alone
(mobile truncation) · shape ≠ previous upload's shape on this channel.

### 5.3 Per-market formula

**@cashguruguides (hi)** — `<SHAPE, in Roman-script Hinglish> · <₹ figure | time span | "Pura Hisaab">`
Roman script only, never Devanagari in the primary title (Devanagari goes in the
localized metadata track, §2.3). Register is the Hinglish people *type*, not formal
Hindi — verified per §2.3.

**@moneymavens101 (en)** — `<SHAPE, plain American> · <$ figure | time span | plain promise>`
No em-dash default (three of the current six use one). `2026` is permitted only when the
video's claim is actually year-bound.

### 5.4 Worked examples — real topics, one per shape, no two alike

**hi:**

| Shape | Topic | Title | ch |
|---|---|---|---|
| **A — QUERY** | pay-yourself-first | `Salary Aate Hi Paise Kaise Bachaye? Pehle Khud Ko Do` | 52 |
| **B — PRICE TAG** | needs-vs-wants | `₹2,047 Har Mahine, Bina Pooche — 5 Auto-Debits` | 46 |
| **C — CONTRADICTION** | 50-30-20-rule | `50-30-20 Rule ₹30,000 ki Salary par Nahi Chalta` | 47 |

*(A rides `paise kaise bachaye`, verified live in the needs-vs-wants pack. B uses the
monthly figure so it matches thumbnail math rather than repeating the annual number
already used. C sidesteps Warikoo's ownership of the concept keyword — the exact move
the 50-30-20 pack identified but did not take.)*

**en:**

| Shape | Topic | Title | ch |
|---|---|---|---|
| **A — QUERY** | emergency-fund | `Where Should You Keep Your Emergency Fund in 2026?` | 49 |
| **B — PRICE TAG** | good-debt-vs-bad-debt | `$6,000 on a Credit Card Costs You $9,506 in Interest` | 51 |
| **D — INSTRUCTION** | pay-yourself-first | `Move $200 on Payday. That's the Whole System.` | 44 |

*(A rides the verified `where to put emergency fund` lane. B is the same evidence the
current title uses, restated so the number leads instead of trailing a colon. D carries
no shock number at all — which is the point: one upload in four must not.)*

**FACT** — every number above already exists in a shipped script or pack. **UNVALIDATED**
— all six are untested; without analytics no title claim on this project can be anything
else.

---

## 6. Market research — what earns clicks in 2026, India vs US

Dedicated research pass, 2026-07-29. Method: live YouTube channel `/videos` pages fetched
and parsed from `ytInitialData`, plus custom thumbnail JPGs downloaded and visually
inspected. India sample: Warikoo, Asset Yogi, Labour Law Advisor, Finance With Sharan,
CA Rachana Ranade, Pranjal Kamra, Neha Nagar, Shashank Udupa, FinnovationZ (**254
titles**). US sample: Graham Stephan, Caleb Hammer, The Money Guy Show, Nischa, George
Kamel, Whiteboard Finance, Humphrey Yang, Two Cents/PBS (**240 titles**).

### 6.1 Primary-source platform guidance (all fetched from support.google.com)

- **FACT** — *Thumbnail & title tips* (`answer/12340300`): *"90% of the best-performing
  videos have custom thumbnails."* Advises brevity and accuracy, and explicitly to
  **"limit ALL CAPS and emoji."** No pixel spec, no character limit given.
- **FACT** — *Add custom thumbnails* (`answer/72431`): 1280×720 recommended, min width
  640px, 16:9, JPG/GIF/PNG, 2 MB mobile / 50 MB desktop upload limit.
- **FACT** — *Test & Compare* (`answer/13861714`, and `answer/16391400`): up to **3**
  title/thumbnail variants; the winner is decided by **watch-time share**, explicitly
  *"over other metrics, like click-through-rate"*; Studio desktop only, Advanced Features
  required, resolves in 2 days–2 weeks; unavailable for Shorts, kids, mature, private and
  Premieres.
- **NOTHING CREDIBLE FOUND** on an official mobile home-feed title truncation character
  count. Every "40–55 characters" figure traces to SEO tool sites (fluxnote, wordcountr,
  thumbmagic), never to YouTube. The ≤60-char rule in §5.2 is therefore a **house
  convention**, not a platform spec — keep it, don't cite it as policy.
- **NOTHING CREDIBLE FOUND** on the widely-repeated "74% of Shorts views come from
  non-subscribers" stat. Aggregator blogs only.

### 6.2 India / Hindi personal finance

- **FACT** — **10/10** visually inspected India finance thumbnails show at least one
  **human face**, cropped close, high eye contact.
- **FACT** — thumbnail text is **3–7 bold sans words** on a **solid highlight block**
  (yellow, red or cyan). The `₹` glyph is used inline as the numeric hook
  ("LOST: ₹9/DOLLAR", "TAX HACKS ₹15L TO ₹2CR").
- **FACT** — on-thumbnail script is **overwhelmingly Roman/English**. Devanagari appears
  only code-mixed mid-phrase on one channel (Asset Yogi: "Salary बढ़ेगी या Tax?"), never
  as the dominant script.
- **FACT** — of 254 India titles, only **3% contain any Devanagari character**. Average
  length **67.5 characters**; **34%** use a question mark; **63%** contain a digit.
- **FACT** — **FinnovationZ** (2.66M subs), the channel most often cited by SEO blogs as
  the faceless/animated Hindi finance exemplar, now runs **face-forward** thumbnails
  (founder's face over an AI-illustrated backdrop).
- **UNVALIDATED** — *which script Indians type into YouTube search* has **no** platform or
  peer-reviewed source. Think with Google's *Hindi Matters in the Digital Age* reports
  ~54% audience preference for Hindi-**language** video — that is spoken-language
  preference, not query script. The 3%-Devanagari title figure is evidence about what
  **creators publish**, not about what **viewers type**.
  → Note this carefully: §2.3's conclusion that Indian finance search happens in **Roman
  Hinglish** rests on *our own* `tools/autocomplete.py` pulls, which is the stronger
  evidence for our purpose — autocomplete literally is the string people type. The market
  data corroborates the *output* side. Both point the same way.

### 6.3 US personal finance

- **FACT** — **12/12** sampled US thumbnails show a face. Identical rate to India.
- **FACT** — two visual dialects. **Tabloid** (Graham Stephan, Caleb Hammer): cable-news
  "NEWS ALERT" chyrons, red/black, shocked or distressed expression, 2–4 word ALL-CAPS
  text. **Calm** (Nischa): soft neutral background, neutral or smiling face, one clean big
  number ("$100,000"), minimal other text. Whiteboard Finance uses a literal hand-drawn
  whiteboard prop.
- **FACT** — of 240 US titles: average **50.2 characters** (17 shorter than India); only
  **10%** use a question mark (vs 34% India); **40%** contain a digit (vs 63% India).
- **FACT** — **Two Cents / PBS** (823k subs), the classic US "faceless animated finance"
  exemplar, now runs **live-action host faces** with exaggerated expressions.

### 6.4 Do the two markets want different thumbnail logic?

- **FACT** — the **visual** grammar converges: face + high contrast + 3–7 bold words + one
  accent colour, in both markets.
- **FACT** — the **title** grammar diverges measurably: India runs **17 characters longer**
  and uses question-mark curiosity **3.4× more often**; the US favours short flat
  statements and numbers. **UNVALIDATED** — the cause (Hinglish code-switching needing
  more words? looser title discipline?) is inference.

### 6.5 What this means for our two channels — honestly

- **FACT** — **22 of 22** sampled competitor thumbnails across both markets use a face.
  Our channels are faceless by creator decision. This is a structural disadvantage the
  packaging cannot design around; it is not a packaging error. **Given it**, the entire
  click job falls on the **number and the two or three words that survive at thumbnail
  size** — which *raises* the bar on varying them, and makes the ten-identical-layouts
  finding in §1.3 more costly, not less.
- **FACT** — the two "faceless finance works" exemplars most often cited (FinnovationZ in
  India, Two Cents in the US) have **both moved to faces**. Any vault note or plan that
  leans on "faceless finance channels do fine, look at X" should be checked against this;
  the examples have moved.
- **FACT vs our artifacts — ALL CAPS.** Every one of our ten shipped thumbnails is
  **100% upper case** (pill, headline, mega, and usually the sub-line). YouTube's own
  tips page advises to *"limit ALL CAPS."* Scoping caveat, stated honestly: that page
  covers thumbnails **and** titles and does not say which the advice attaches to. It is
  still the only primary-source style guidance that exists, and we are at the maximum of
  the thing it says to limit. Cheapest response: set the **sub-line in sentence case**.
  Costs nothing, breaks the uniform texture, and moves off the extreme.
- **FACT vs our artifacts — title length.** Our `-en` titles measure 60, 67 and 61
  characters against a US market average of **50.2**. We are consistently **10–17
  characters long** for that market. Our `-hi` titles measure 63, 65 and 80 against an
  India average of **67.5** — well matched, except the 80-char `emergency-fund` outlier
  (§2.2).
- **FACT vs our artifacts — question form.** 34% of India finance titles use a question
  mark. **Zero** of our three live hi titles do, and the hi packs repeatedly identify
  question-form autocomplete strings as the deepest verified clusters
  (`cibil score kitna hona chahiye`, `credit card minimum payment kya hota hai`,
  `…karne se kya hota hai`). Shape A in §5.2 exists precisely to use them and has not
  yet been shipped once.
- **FACT vs our artifacts — the solid highlight block.** The India market's standard
  device is bold words **on a solid colour block**. Our system has exactly one of those
  (the top-left pill), and it is used for a throwaway kicker ("MINIMUM = JAAL",
  "BE HONEST") rather than for the hook. **UNVALIDATED** — whether moving the block to
  the hook would help. It is a within-system change (the pill already exists, in the
  right colours) that would produce a visibly different card. Worth being one of the
  rotation options in §3.1, not a new house style.

---

## 7. Contradictions with what the vault currently documents

1. **`best-practices.md` → "Thumbnails (the ~50% lever)"** is written for the AI-tools
   channel and is **flatly opposite** to the finance system in production. It says
   *"ENERGY BEATS AUTHENTICITY… vivid saturated color, dramatic glow/fire/lightning,
   glossy… put the punch word in a colored keyword box (red/orange)"*. `fin-package.md`
   says the finance thumbnail must **never** be AI-collage, shocked-face or red-box, and
   the shipped system is desaturated, dark, grain, `brightness(0.62)`. Both notes are
   presented as current guidance in the same vault. The note does carry a 2026-07-18
   scoping correction ("the red-box/MrBeast text grammar is an AI-tools-niche pattern,
   not universal") — but that correction is buried at the bottom of a 40-line section
   whose heading and first 30 lines say the opposite. **Any agent skimming it for finance
   work gets the wrong answer.**
2. **`best-practices.md` → "Urdu/Hindi market searches in ENGLISH keywords"** is refuted
   for India finance by the pipeline's own autocomplete pulls (§2.3). Generalised from a
   single Urdu history video.
3. **`niches/india-finance-market.md` → "Titles/descriptions: English (unchanged rule)"**
   is stale; superseded by the Roman-Hinglish creator rule and by the six live titles.
4. **`fin-package.md` → "hi thumbnails use Roman-script Hindi"** has a shipped
   counter-example: `emergency-fund` hi is Devanagari.
5. **`design-finance-blockframe.md`** claims to be the channel's durable design system
   and contains **no thumbnail section**; the spec lives only in an agent prompt, against
   `vault/CLAUDE.md`'s explicit "agents are procedure, not memory" rule.
6. **The packs' "no near-duplicate" conclusion is true and misleading.** Per-video the
   check passes; the channel grid is nine identical layouts. The check compares number
   and photo, never layout, so it cannot detect the thing bucket 1 actually names.
7. **`fin-package.md` → "one per cut now, so it's a record, not an A/B pick"** was written
   as if A/B testing had been given up. YouTube's native Test & Compare takes **up to 3
   titles and/or thumbnails** and decides on **watch time**. The creator's rule retires
   the *production* of three variants; it does not have to retire testing, and the packs
   already contain 4–5 researched titles that cost nothing to enter.
8. **`channels.md` documents an About description for channels A and B and none for D or
   E** — the two live finance channels, the two with the AI-persona exposure, and the two
   whose names both mean "expert".
9. **`us-market-2026.md`'s framing "the enforcement line is crossed at the 5th"** reads as
   a platform threshold. No YouTube source states any threshold. It is a good house rule
   mislabelled as policy.
10. **The disclosure position is stated as fact in six files in identical words.** It is a
    defensible interpretation of an ambiguous rule, and the argument given against
    disclosing anyway (*"invites the question of what was synthesised"*) is an untested
    belief sitting inside a compliance section.

---

## 8. The five highest-leverage changes

Ranked by value ÷ cost. Format: `[grade] change — why — cost — owner`.

1. **[FACT] Write a channel About description for @cashguruguides and @moneymavens101 —**
   neither has one (`channels.md` documents Abouts for channels A and B only), both
   channel names literally mean "expert", every upload is synthetic-narrated finance, and
   bucket 3 of the inauthentic-content policy targets exactly that reading. The About is
   where "AI-generated narration · general education, not advice · no product recommended
   · sources cited on screen" costs nothing to say. — **~15 min, one file, no re-render**
   — `vault/knowledge/channels.md` (creator pastes into Studio).

2. **[FACT] Break the thumbnail *layout*, not just the number —** all ten shipped
   thumbnails are one literal layout; the policy's own words for bucket 1 are *"a template
   with little to no variation across videos"*, enforcement is channel-level, and a channel
   page is a grid of thumbnails. `fin-package`'s sameness check compares the number and
   the photo and therefore passes this every time. Add a **layout** comparison (pill
   present/absent · alignment · mega colour · mega position) and disqualify a third
   consecutive match; set the sub-line in sentence case (YouTube's own tips page says
   *"limit ALL CAPS"*, and we are at 100%). — **a few lines in one agent prompt** —
   `.claude/agents/fin-package.md`, with the spec moved into
   `vault/knowledge/design-finance-blockframe.md`, which currently has no thumbnail
   section at all.

3. **[FACT] Ship 2–3 titles into YouTube's native Test & Compare instead of picking one —**
   the feature takes up to 3 title and/or thumbnail variants and decides on **watch-time
   share, explicitly over CTR**, resolving in 2 days–2 weeks. Every pack already contains
   4–5 researched, evidence-backed titles and then discards all but one. The creator's
   one-thumbnail rule saves render cost and is fine; the **title** test costs nothing.
   Bonus: it is the only source of performance signal these channels will ever get without
   analytics. — **one `test:` block in the pack template** — `.claude/agents/fin-package.md`.

4. **[FACT] Retitle by market measurement, and rotate the title shape —** measured against
   240 US and 254 India finance titles: our `-en` titles run **60–67 chars against a US
   average of 50.2**, and **zero** of our live `-hi` titles use a question form against an
   India rate of **34%** — while the hi packs' own autocomplete pulls keep finding
   question-form strings as the deepest verified clusters. Add the shape rotation with the
   previous-upload disqualifier (§5.1) so six titles can never again share one skeleton.
   Also a 30-second Studio fix: `emergency-fund-hi` is 80 chars, in English on a
   Roman-Hindi channel, and advertises "Explained in Haryanvi" — a register the channel
   retired on 2026-07-28. — **~3 lines of pipeline state (`last_title_shape` in
   `run.json`) + one retitle** — `.claude/agents/fin-package.md`.

5. **[FACT] Emit an SRT per cut, and a Devanagari localized title/description for the hi
   channel —** captions are mentioned in **zero** of the eleven publish packs, yet the
   pipeline already writes both inputs (`assets/voice/*.txt` VO lines +
   `assets/voice/timing.json` per-line timings) and already archives them. Auto-captions on
   synthetic Hindi are the weakest thing YouTube can index on this channel. The same
   metadata slot carries the Devanagari title/description, which per YouTube's
   multi-language docs makes the video findable in Devanagari search **while the displayed
   Roman title stays exactly as the creator's rule requires**. — **~20 lines in `tools/`,
   zero API spend** — `tools/` + a path line in `fin-package`.

**Deliberately not in the top five:** Shorts cut-downs (real value, but needs a 9:16
re-layout and a re-render — expensive, and Test & Compare doesn't work on Shorts);
community posts (worthless at ~0 subscribers); end screens (blocked by a 1.0s render tail,
so it is a `fin-build` change, not a packaging one); more tag work (meticulous already, and
the lowest-yield rigour in the stage).

---

## Sources

Primary (policy):
- [YouTube channel monetization policies](https://support.google.com/youtube/answer/1311392?hl=en)
- [Disclosing use of altered or synthetic content](https://support.google.com/youtube/answer/14328491)
- [How we're helping creators disclose altered or synthetic content — YouTube Blog, 18 Mar 2024](https://blog.youtube/news-and-events/disclosing-ai-generated-content/)
- [Advertiser-friendly content guidelines](https://support.google.com/youtube/answer/6162278?hl=en)
- [A/B test titles and thumbnails](https://support.google.com/youtube/answer/16391400?hl=en) · [Test & Compare](https://support.google.com/youtube/answer/13861714)
- [Add multi-language features to your videos](https://support.google.com/youtube/answer/13338784?hl=en)
- [Thumbnail & title tips](https://support.google.com/youtube/answer/12340300) · [Add custom thumbnails](https://support.google.com/youtube/answer/72431)

Market sample (channel pages fetched 2026-07-29): [@warikoo](https://youtube.com/@warikoo) · [@AssetYogi](https://youtube.com/@AssetYogi) · [@LabourLawAdvisor](https://youtube.com/@LabourLawAdvisor) · [@FinancewithSharan](https://youtube.com/@FinancewithSharan) · FinnovationZ (`UCUMccND2H_CVS0dMZKCPCXA`) · [@GrahamStephan](https://youtube.com/@GrahamStephan) · [@calebhammer](https://youtube.com/@calebhammer) · [@MoneyGuyShow](https://youtube.com/@MoneyGuyShow) · [@nischa](https://youtube.com/@nischa) · [@WhiteboardFinance](https://youtube.com/@WhiteboardFinance) · [@humphrey](https://youtube.com/@humphrey) · [@TwoCentsPBS](https://youtube.com/@TwoCentsPBS)
- [Think with Google — Hindi Matters in the Digital Age](https://www.thinkwithgoogle.com/intl/en-apac/consumer-insights/consumer-trends/hindi-matters-digital-age/) (spoken-language preference only — **not** search-query script)
- [Creator Insider — Matt Halprin on inauthentic content, 16 Jul 2026](https://www.youtube.com/watch?v=14Vm0CiyUVE)

Secondary (reporting, used only to date and locate the primary):
- [TechCrunch — YouTube clarifies policies around AI slop, 20 Jul 2026](https://techcrunch.com/2026/07/20/youtube-clarifies-policies-around-ai-slop-and-upsetting-videos/)
- [Search Engine Land — What is YMYL](https://searchengineland.com/guide/ymyl) (used to establish YMYL is a *Search* rater concept)
