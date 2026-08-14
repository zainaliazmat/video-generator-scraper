---
summary: Evidence review of the US faceless-YouTube market. Kills the open-web CPM tables as fiction, establishes that AdSense is ~1.5% of income at small scale, and reframes niche choice around what the audience buys rather than niche CPM.
updated: 2026-07-21
source: Two deep-research passes (206 agents, adversarial verification). Primary sources only — Google Help, YouTube Creator Liaison, Fortune, Tubefilter, Indie Hackers creator dashboards, OpenSponsorship transaction data.
stage: ADOPTED — niche research; figures carry their own dates
---

# US faceless market — evidence review (2026-07-21)

Two deep-research passes (206 agents, adversarial verification). Round one's
economics were **all refuted**; round two hit a session limit before synthesis.
This note keeps only what traced to a creator dashboard, a journalist, or a
platform doc.

## Rule zero: the CPM tables are fiction

Every "CPM by niche" table on the open web (outlierkit, vidIQ, easyviral,
faceless.my, youtubeniches, fluxnote, frameloop) is uncited lead-gen content.
All 14 economics claims sourced from them were refuted 0-3. One page,
`outlierkit.com/blog/untapped-youtube-niches`, was fetched twice and contains
**zero** dollar figures, zero RPMs and zero subscriber counts for the six
channels it names — the numbers people quote from it were invented downstream.

Never cite a niche CPM figure in this project without a dashboard behind it.

## Observed RPMs (the only ones with provenance)

| Source | Format | Evidence class | Effective RPM |
|---|---|---|---|
| Fortune, Dec 2025 — 5-channel AI network | mass faceless AI | journalist (creator-stated) | ~$0.67–1.00 |
| Code With Andrea (Indie Hackers) | screen-recorded tutorial | creator dashboard | ~$2.80 AdSense |
| Hank Green, 12h white noise | long-form ambience | creator dashboard | ~$17.90 blended |

The first and third are *my* arithmetic on stated figures, not published RPMs.
Order-of-magnitude only.

Platform facts (Google Help `answer/9314357`): RPM includes memberships,
Premium, Super Chat — not just ads. CPM is pre-revenue-share. **RPM ≈ 40-60% of
CPM**; the 45/55 split alone floors it near 45%.

## The load-bearing finding: AdSense is a rounding error at small scale

Code With Andrea, ~30.5k subs, **33,200 views in the month**, zero new uploads:

- Course sales $3,721
- Affiliate sales $2,184
- Sponsors $137
- **AdSense $93** (1.5% of total)
- **Total $6,136**

~$185 per thousand views, vs $2.80 on ads for the same views — **65×**. One
affiliate campaign made $2,000+ in a week, beating a month of AdSense 20×.

**Therefore: choose a niche by what its audience will buy, not by its CPM.**

## Sponsorships don't rescue small channels

OpenSponsorship, **1,527 completed paid deliverables**, Jan 2025–Jun 2026
(platform transaction records, not a rate card):

- under 10k followers: median **$134** per deliverable
- 10k–50k band: median **$150**

Low hundreds, not thousands. Agency claims of "$500–$2,000 per finance mid-roll"
are marketing. Caveat: cross-platform, not YouTube-isolated.

## Policy constraints (verified, primary sources)

- **2025-07-15** was a *rename*: "repetitious content" → "inauthentic content".
  YouTube: "a minor update to our longstanding guideline." Faceless is not
  banned; AI tooling is not banned.
- Discriminator is **added value**, not the missing face. Explicitly targeted:
  *"image slideshows, templated storylines or scrolling text with minimal or no
  narrative, commentary or educational value"*; *"characters put in the same
  situation over and over with the same outcome."*
- **2026 clarification: AI "expert" personas in health, legal, finance and
  politics are ineligible regardless of added value.** This guts the highest-CPM
  verticals for a synthetic-narrator build. See `depiction-no-prophet-faces` (Claude memory)
  for the parallel rule on our own content.
- **Enforcement is channel-level.** A pattern across recent uploads kills
  monetisation for the whole channel. Documented: 588k-sub Bible-story channel
  at ~$30k/mo demonetised while still doing ~1M views/mo. Tubefilter: *True
  Crime Case Files*, 150+ AI videos, one at ~2M views monetised — channel
  terminated outright.
- Do **not** repeat two widely-circulated numbers: the "last 30 uploads" review
  window, and "Jan 2026: 16 channels / 35M subs / 4.7B views terminated". Both
  unsupported.

## The core tension

Cheapest-to-produce formats == the enumerated enforcement targets. Production-cost
floor and policy-risk floor are the same variable. "Easy to generate" and
"survives 2026 policy" pull against each other.

## Views needed for $500/mo on ads alone

| Model | RPM | Views/mo |
|---|---|---|
| Mass AI faceless | $1.00 | 500,000 |
| Small quality faceless | $2.80 | 180,000 |
| Optimistic high-intent | $8.00 | 62,000 |

At 5k views/video the middle row is 36 uploads/month, forever — which is exactly
the pattern that triggers channel-level enforcement. **The $500–1,000/mo target
is reachable, but not through AdSense.**

## Five candidate niches (product-first)

Ranked. Judgment built on the constraints above, not yet validated against
observed channels.

1. **Software walkthroughs for non-tech professions** — QuickBooks for
   landscapers, Excel for church treasurers, Canva for realtors. Direct
   Code-With-Andrea analogue; sell the template pack. The profession is the
   niche, the software is incidental — this is not a tech channel.
2. **Boring durable-goods buying guides** — water heaters, generators, sump
   pumps. Highest purchase intent per view; affiliate pays regardless of volume.
3. **US admin & paperwork walkthroughs** — REAL ID, IRS forms, VA benefits,
   SNAP. Sell a checklist pack. Narrate the official `.gov` process; claim no
   expertise (see the 2026 YMYL carve-out).
4. **Hyper-local US relocation guides** — "cost of living in Chattanooga".
   Local realtors/mortgage brokers sponsor direct at tiny audience sizes.
5. **Long-form sleep/ambience history** — cost floor ~$60/video (Fortune). Hank
   Green's 12h white noise: $8,832 Premium vs $1,374 ads — **watch time, not
   views, is the lever**. Closest to the enforcement line; single data point.

## Open

- Real observed RPMs by niche from Studio screenshots / a Social Blade cohort.

## ✅ RESOLVED 2026-07-28 — the carve-out triggers on the PERSONA, not the voice

Verified against Google's own policy page (`support.google.com/youtube/answer/1311392`),
not secondary blogs. The open question above is closed.

**Permitted, verbatim:** *"Content that utilizes creative tools to assist in
delivering a unique, well-researched, or creative narrative, like using AI to edit
your video scripts or generate a unique background visual."* Synthetic narration
alone does **not** disqualify content.

**Prohibited, verbatim:** the *"AI Personas Related to Sensitive Topics"* section —
*"channels uploading this content will not be allowed to monetize"* when presenting
AI-generated personas as expert advice-givers on health, legal, financial or
political matters. Named examples: *"An AI 'doctor' providing medical diagnoses"*
and **"AI-generated podcast hosts offering financial guidance, investment tips, or
wealth management advice."**

**Enforcement:** channel-level for most violations — *"monetization may be removed
from your entire channel"* — with individual videos able to receive limited or no
ad earnings independently. Three-strike path (warning → 90-day suspension →
permanent YPP removal) for mass-produced/recycled content.

### What this means for [[channels|D CashGuruGuides]] and [[channels|E moneymavens101]]

The narration is **not** the exposure. The current framing is already close to the
right side of the line: sourced numbers, no product recommended, and an explicit
on-screen disclaimer (*"general financial education hai, financial advice nahi.
Koi bank, app ya fund recommend nahi kiya gaya hai"*). Keep all of that.

The binding rules, now evidence-backed:
1. **No host persona, ever.** Never a named/implied AI presenter, never
   first-person expertise ("I recommend", "my advice"). Narrate cited sources.
2. **No investment tips, stock/fund picks, or wealth-management advice** — the
   exact language of the prohibited example. Budgeting and general education are
   a different category and stay fine.
3. **Toggle the altered/synthetic-content disclosure** in Studio on every upload.
4. **The real remaining risk is category 1 — mass production**, not the persona:
   template-based, near-identical uploads. That is a channel-level pattern, so a
   fixed 9-segment template across every upload on both channels is the live
   exposure. Vary format, length and structure across consecutive uploads.

**Net:** the finance vertical is monetisable for this build. The synthetic-narrator
worry that shaped [[../../..|the pipeline review]] was aimed at the wrong axis;
sameness is the axis that matters.
- vidIQ MCP connector is unauthorised; authorising it unlocks per-keyword
  competition data instead of inference. See `two-home-memory-architecture` (Claude memory).
