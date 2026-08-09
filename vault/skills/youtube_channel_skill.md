---
summary: The business engine — money-first niche selection (Gate 0), angle validation (Gate 1), fact-finding, monetization ops, platform compliance (Gate 2). Load for any channel decision; companion long_form_scripting.md writes the scripts.
updated: 2026-07-04
source: creator's v5 skill (claude.ai project) + v5.1 vault refinement
stage: ADOPTED — channel strategy and compliance
---

SKILL — Faceless YouTube Channel: Money-First Research → Validation → Compliant Publish (v5.1)
Load this when working on the faceless YouTube channel.

v5.1 changelog (vault edition, 2026-07-04 — additive, nothing deleted): this vault copy is the
canonical, single source of truth. §1 gains the LOCAL SCRAPER path — in Claude Code sessions the
ytauto TUI + library.db (SQLite, deduped; 552 videos backfilled 2026-07-04) is the primary engine.
Documents the &sp= encoding gotcha.

v5.2 changelog (2026-07-04, same day — two additions): (1) STUDY LOOP — before scripting a
Gate-1-passed topic, run the competitor study (vault/workflows/video-study.md): top/mid/low videos
at 480p + transcripts + keyframes → analysis → findings into the vault (best-practices.md; ~3
confirmations promote into a skill). (2) KNOWLEDGE POLICY — the vault is the single knowledge base;
all findings, analysis, and decisions land in vault notes (§10 revised).

v5.3 changelog (2026-07-04, later — NARRATION REVISED): channel narration = Kokoro TTS for now.
The creator (native Urdu speaker) fumbles reading English scripts aloud — the own-voice rule
blocked publishing for two weeks, and an unexecutable rule is worse than an honest workaround.
The own-voice decision is PARKED, not deleted (revisit when comfortable). Consequences: scripts
ship in TTS-segment format (see videos/video-02-claude-edits-video/script-v2-tts.md — numbered
lines mapping to the project's audio_request.json); disclosure toggle = YES per video and said
IN the video (transparency as premise, not liability); long_form_scripting §8's human-delivery
system applies only if human VO returns. Gate-2 "inauthentic content" defense stays what it was:
material variation — own artifacts, own tests, own verdicts — not the voice.
Goal: build the channel into real income (target ~$10K/month). Money is the objective. The niche and format are chosen for monetization and newcomer-winnability, NOT personal interest. Claude has authority to choose/change the niche based on evidence.

This skill is now one of TWO. It owns the business engine — should we make this, will it earn, and is it compliant. Its companion, long_form_scripting.md, owns the creative engine — how to write and deliver the actual video (structure, hooks, retention architecture, persuasion psychology, the human-delivery system, frameworks, the analogy bank, and the script deliverable template).
When producing a video, load BOTH: clear the gates here first, then switch to long_form_scripting.md to write the script.


v5 changelog (additive — nothing deleted; scripting RELOCATED, not removed):

Scripting, packaging-craft, delivery, and the script deliverable template MOVED OUT to long_form_scripting.md. Old §5 (SCRIPT), the packaging half of old §6, and old §10 (deliverable template) now live there, expanded with research.
NARRATION CORRECTION (load-bearing): the channel's voice is the creator's OWN recorded voice, NOT TTS/synthetic. The old "write for a text-to-speech voice" guidance is gone; the companion skill carries a human-delivery system instead (the 9 speaking habits + a script-as-score markup method). ElevenLabs remains a reviewed tool and the primary affiliate — it is not how this channel narrates.
Findings folded in: all research from the deep-dive session (script structures, hook formulas, retention architecture, persuasion psychology, framework library, analogy bank) lives in the companion skill so generated scripts are non-generic.
Unchanged from v4: Gate 0/1/2 logic, the human-verified &sp= filter code, the vidIQ CSV parsing gotchas, the human↔AI scraping loop, the fact-finding hierarchy, the pricing-volatility rule, the monetization model. All v3/v4 engine specifics kept verbatim.



0. CORE PRINCIPLES (non-negotiable)

Money first. Every niche/format/topic choice is judged on: will this earn? Optimize for RPM + affiliate/sponsor potential + audience size + newcomer-winnability + cheap faceless production. Interest is irrelevant unless it also pays.
Scraping runs through the engine for the surface I'm on (never pretend to have browsed YouTube). In Claude Code: the ytauto TUI + library.db is the primary engine — I generate queries, the human runs the scrape in the TUI (or I query library.db directly for already-collected data). In claude.ai web sessions: I generate the exact URLs/channels; the human scrapes (vidIQ → CSV); I parse + analyze + decide the next move.
Never assert demand, a "gap", or "this will make money" without verification. Every claim comes from a scrape, a search, or a primary source.
Validate before producing, and stay compliant before publishing. Gates are ordered: Gate 0 (money-first niche) → Gate 1 (a specific winnable angle) → write the script (now governed by long_form_scripting.md) → Gate 2 (platform compliance, before publish). Do not skip a gate.
Be honest about money. $10K/month is rare, slow, and multi-stream. Never inflate odds. State realistic milestones, not the dream number.
Always append the verified filter code; never invent one. Every YouTube search URL must end with the human-verified This year filter &sp=EgIIBQ%253D%253D so the human never sets filters manually. (This exact code was confirmed in the human's browser. Do not guess new &sp= codes from memory — if a different filter is ever needed, ask the human to grab the code from their address bar.)
Compliance is survival. Platform rules can demonetize the entire channel, not just one video. Verify the current monetization + disclosure policy before every publish (Gate 2), and design content to comply (material variation, disclosure, cleared music). For a faceless channel this matters as much as picking a winnable niche.
Transparency is the moat; accuracy is the product. Honest "worth it / skip" verdicts, saying out loud when a free tool wins and when I earn no commission, disclosing affiliates, and only claiming tests that were actually run — this is the trust a giant-dominated "best X" lane can't fake, and it's what keeps a newcomer review channel alive. Honesty is not a constraint on the strategy; it is the strategy. (The full scripting expression of this principle — the "I tested" integrity rule, honest-verdict craft — lives in long_form_scripting.md.)


0.5 GATE 0 — MONEY-FIRST NICHE SELECTION (run before anything else)
A niche advances only if it clears ALL FOUR:

High commercial intent / RPM. Advertisers pay more where viewers are buying or deciding: software/SaaS/AI tools, personal finance/credit/investing, B2B/business, real estate, insurance, high-ticket products. Avoid pure-entertainment/low-RPM lanes unless volume is enormous.
Strong off-ad monetization. Are there good affiliate programs (recurring SaaS commissions are best; high-ticket or high-volume retail next), sponsor demand, and a path to an own product/lead-gen later? Ad revenue alone rarely reaches the goal.
Newcomer-winnable in an action format. Do small channels demonstrably break out here, in formats like buyer's guides, tutorials, comparisons, "best X for Y", "is X worth it", "how to"? (Our data: the only newcomer breakouts were action-oriented; neutral explainers were giant-dominated.) Verify with a scrape, don't assume.
Faceless + low-budget feasible. Can it be made with screen recordings / stock / voiceover, no on-camera presence, minimal spend? (Faceless = no face on camera. Narration is still the creator's own real voice over those visuals.)

Money signal to use: when deep-diving comparable small channels, read vidIQ's "est. monthly earnings" — a concrete read on whether the niche actually pays at small scale.
If a niche fails Gate 0, pick another candidate. Only Gate-0 niches proceed to keyword validation.

1. THE SCRAPING ENGINE (two paths — pick by surface)

PATH A — LOCAL (Claude Code sessions; PRIMARY as of 2026-07-04): the ytauto terminal app in this
repo. Human pastes keywords/URLs into the Scrape screen → yt-dlp pulls full detail (views, likes,
subscribers, upload date, tags) → everything upserts into library.db (SQLite; deduped by video_id;
re-seen videos refresh instead of duplicate; >50%-already-known searches auto-page deeper for
brand-new videos). I analyze by querying library.db / the history/ snapshots directly — no CSV
parsing, no manual filter-setting. Compare screen diffs runs over time. 552 videos / 377 channels
already backfilled (2026-07-04).
  ⚠️ Encoding gotcha: the TUI's internal filter table uses the single-encoded &sp=EgIIBQ%3D%3D;
  the double-encoded EgIIBQ%253D%253D below is the same filter as pasted from a browser address
  bar. Both are "Upload date: This year". Don't "fix" one to match the other.

PATH B — WEB (claude.ai sessions; vidIQ loop — unchanged from v5):
Cycle: I generate URLs → human scrapes (vidIQ) → CSVs back → I parse + analyze → I specify the next scrape.

YouTube search URLs: always build them with the verified This year filter already appended: https://www.youtube.com/results?search_query=keyword+with+plus+signs&sp=EgIIBQ%253D%253D. The &sp=EgIIBQ%253D%253D code (human-verified) applies Upload date: This year and is query-independent, so it goes on the end of every URL and the human clicks straight through — no manual filtering. (It does not also sort by view count; that's fine — vidIQ scrapes ~100 results per query, so the highest-view videos appear regardless and absolute views are read from the full set.)
Channel deep-dives: https://www.youtube.com/@handle/videos, sort by Popular; capture vidIQ est. earnings.
Reddit/web demand: https://www.google.com/search?q=site:reddit.com+keyword.
Parsing the vidIQ CSV (gotchas): columns are messy CSS-class names — video URL=yt-simple-endpoint href, duration=ytBadgeShapeText, title=style-scope 3, channel=yt-simple-endpoint, channel URL=yt-simple-endpoint href 3, views=inline-metadata-item, age=inline-metadata-item 2, outlier=vidiq-c-fvFDqp ("4.5x"). Subscriber count = the column immediately LEFT of the column whose values equal "Subscribers" (detect per file). Channel-page scrapes use a DIFFERENT layout (ytAttributedStringHost, ytLockupViewModelContentImage href). Parse K/M suffixes; dedupe by video id (v=); drop junk rows (off-topic results leak in).


2. STEP 1 — TOPIC/ANGLE VALIDATION (within a Gate-0 niche)
Scrape demand queries for the niche (action-format framings: best [X] for [Y], [tool] tutorial, [A] vs [B], how to [outcome], is [X] worth it). From the CSVs compute:

Demand ceiling: max views; counts ≥100k/500k/1M. Low ceiling = weak.
WHO won (critical): mega-channel or newcomer? A giant winning ≠ newcomer room.
Small-channel breakout count = the green light: channels under ~20k subs with views far exceeding subs. Zero = red flag. (Freight + storage explainer = zero.)
Look-alike graveyard / AI-slop check: many tiny channels with near-identical titles all at <few-hundred views = commoditized; verify if it's non-competitive slop (then real competition is thin) vs genuine.
Absolute views beat outlier multipliers: a 20x outlier on a 15-view-baseline micro-channel is still a failure. Always read absolute views.

⛔ GATE 1 — advance only if BOTH:

Real demand (decent ceiling), AND
A credible small-channel breakout in this niche/format (or clear proof the swarm is non-competitive slop and the angle is winnable with quality).

Fail Gate 1 → re-angle or pick another Gate-0 niche before scripting.

3. STEP 2 — DEMAND/ANGLE MINING (Reddit + comments)
site:reddit.com [niche] "can someone explain" / "best" / "worth it" / "vs"; sort Top; read whole threads; capture exact wording. Competitor YouTube comments reveal the gap the winner left ("I wish they compared…", "what about [tool]?"). Output: the specific question/decision this video resolves, in the audience's words. (Emotional demand ≠ a winnable format — still verify on YouTube.)

4. STEP 3 — FACT-FINDING (accuracy = trust = retained audience)

Source hierarchy: primary/official (vendor docs & pricing pages, SEC 10-Ks, regulator data) > trade press + academic > reputable journalism. Avoid SEO/AI listicles/affiliate-spam.
For buyer's-guide/tutorial/comparison formats, "facts" = accurate specs, current pricing, feature comparisons, and hands-on behavior. Verify every spec/price before publishing; they change constantly — date-stamp them.
Triangulate key claims across ≥2 sources; present ranges for conflicts; flag uncertainty rather than overstating. Keep a sources-to-fact-check list shipped with the script.
Useful tactic: find the industry's own jargon for a mechanic — fast route to authoritative sources and a built-in hook.

⚠️ Pricing-volatility rule (AI-tool niche especially)
AI-tool pricing is exceptionally volatile and cross-source-inconsistent: prices, tiers, free-tier limits, and the line where commercial rights begin change monthly, and third-party trackers disagree — often by a few dollars or a whole tier. So:

Reconcile every figure against the tool's official pricing page; treat trackers as leads, not truth.
Present ranges where sources conflict, date-stamp every number, and re-verify on publish day — not just at scripting.
In the script, speak prices as approximate ("around $X as I'm recording this") and tell viewers to check the live price via the link. Put the precise, dated figures in the fact-check table, not the spoken VO.


5. STEP 4 — SCRIPT → see the companion skill
Once Gate 1 passes, load long_form_scripting.md and write the script there. That skill is the full script-writing + human-delivery system: structure & length targets, the open-loop hook and the rest of the retention architecture, the persuasion-psychology toolkit, the human-narration delivery system (the 9 speaking habits + the script-as-score markup), the framework library, the analogy bank, and the deliverable template.
The money-relevant constraints from this skill still bind the script:

Action formats are the default and deliver value fast — don't withhold; viewers came for the answer. End with an honest verdict + affiliate CTA. Explainer formats only if Gate 1 proved a newcomer can win.
Honesty is the moat + the "I tested" integrity rule — only claim hands-on testing the human actually ran; say when a free tool wins and when there's no commission; never shill a worse product for a bigger payout.
Prices spoken as approximate, precise figures in the fact-check table (see §4).
Design for Gate 2 compliance — material variation (your own testing/angle/POV), and cleared music.


6. STEP 5 — MONETIZATION SETUP
(Packaging craft — titles, thumbnails, hook-alignment, and A/B testing — moved to long_form_scripting.md §Packaging, since it's part of the creative artifact. This section keeps the money operations.)
Affiliate operations (the rate is not the whole story)

Commission model > headline rate. Recurring (pays each billing cycle while the customer stays — compounds; best for SaaS you mention every video) beats one-time / first-cycle-only (bigger upfront, no compounding). Prioritize recurring + the tools you genuinely use most.
Sign-up priority: the highest-value recurring program for a tool you feature constantly, first; bigger-upfront one-time programs next; gated/low-value programs last (don't block on them).
Link placement: description (grouped by step; affiliate links for monetizable tools, plain links for the free ones), top 2–3 pinned in the comments, a disclosure line at the top of the description AND said on camera/in the VO.
Required disclosures: an FTC-style affiliate disclosure, always. Some programs add their own rules (e.g. a trademark-attribution line, no bidding on the brand's keywords, no affiliate links in paid ads) — read each program's terms.
Track the boring stuff per program: cookie window, payout minimum, and network (PartnerStack / Impact / FirstPromoter, etc.). Rates and terms change — verify per program and record them in the log.

Monetize from day one
Affiliate links (with disclosure) in the description and pinned comment; a lead magnet / email capture if relevant; structure videos so sponsors fit naturally.

7. GATE 2 — PLATFORM COMPLIANCE (run before EVERY publish)

A faceless, AI-tooling channel is a prime enforcement target. Verify the current policy from the platform's OWN Help Center / Creator blog — not SEO blogs, which routinely over- and under-state the rules. Clear all three:

AI / synthetic-media disclosure. Mark altered or synthetic content where required. Production-assistance AI (e.g. an AI-written script) is generally exempt; the trigger is realistic media that could mislead (cloned real voices, photoreal fake footage). This channel's narration is the creator's own real voice, so the narration itself doesn't trigger disclosure — but if a video's visuals include realistic AI-generated imagery/video that could mislead, the toggle may still apply. When unsure, disclose: it's free and (per the platform) carries no reach or revenue penalty — the only thing that hurts you is failing to disclose when you should have.
"Inauthentic / mass-produced content" (the strategic one). Templated, repetitive, low-variation content can disqualify the ENTIRE channel from monetization — not one video. Design implication (this shapes content strategy, not a checkbox): every video must be materially varied, carrying the creator's own testing, angle, voice, and point of view. The AI tools are production aids, not a replacement for the creator. This is why the action-format + honest-verdict approach wins — it's inherently varied and value-adding, the opposite of "inauthentic."
Music / Content ID. Copyrighted background music diverts that video's ad revenue to the rights holder (a claim, not usually a channel strike). Use cleared sources only (the platform's own audio library / royalty-free).


Note on staleness (important): the specific current rule names, dates, toggle locations, and thresholds belong in the decisions log — verify and record them per publish. This skill holds the durable procedure ("verify platform policy every publish; design to comply"), which stays true even as the specifics change. Do not hard-code today's policy details into this skill.

8. MONETIZATION MODEL (the income ladder — be honest)

Reality: ads alone rarely hit $10K/month (~500K–1M monthly views in a high-RPM niche, usually 1–2+ years in). Most channels never get there.
The real path = stacked streams: (1) ads (need YPP: 1,000 subs + 4,000 watch hours, or the Shorts-views equivalent), (2) affiliate — often the biggest early lever; recurring SaaS commissions compound, (3) sponsorships — pitch once you have a focused audience advertisers want, (4) own product / newsletter / lead-gen — the highest-margin endgame.
Design implication: prioritize niches and videos with strong affiliate/sponsor fit. Track progress by realistic milestones (monetization → first $100/mo → $1k/mo → scale), not by the headline number.


9. CAVEATS (stay honest)

vidIQ outlier scores and est. earnings are proprietary estimates — directional, not exact.
Affiliate/RPM figures vary widely; verify per program, and note rates/terms change.
Defamation law is jurisdiction-specific — conservative attribution for named companies.
Platform policies (monetization, AI disclosure, Content ID) change fast and are easy to mis-state — verify from the platform's own docs per publish (Gate 2), and treat the specific current details as log entries, not fixed skill content.
AI-tool pricing is unusually volatile — reconcile against official pages and re-verify at publish (§4).
Scripting/retention/delivery caveats (e.g. that creator-education retention and title percentages are directional benchmarks, not peer-reviewed) live in long_form_scripting.md §Caveats.


10. DELIVERABLE TEMPLATE → see the companion skill
Every script ships in the production-doc format defined in long_form_scripting.md §Deliverable Template (title options, thumbnail concepts + A/B plan, the two-track VO + on-screen-cue script, fact-check table, affiliate setup, pre-publish checklist).
Channel-ops requirement: the OBSIDIAN VAULT is the single knowledge base — verified facts, study findings, analysis, decisions, and status all land in vault notes during the session. Read `vault/index.md` + the relevant notes at session start; update them (in place, don't append-forever) at session end. Git history is the audit trail.

QUICK-REFERENCE RUNBOOK

GATE 0: pick a niche by RPM + affiliate/sponsor potential + newcomer-winnability (action formats) + cheap faceless production. Verify with a scrape (+ vidIQ est. earnings on small channels).
Scrape niche demand queries → analyze ceiling + WHO won + small-channel breakouts → GATE 1.
Mine Reddit + competitor comments → exact audience question/decision.
Fact-find (specs/prices/comparisons), triangulate + date everything, reconcile against official pages (AI prices move monthly) → sources list.
Write the script in long_form_scripting.md (action format = deliver value fast + honest verdict/CTA; engineer retention; write for the ear and for the creator's own voice).
Package + set up monetization — packaging/A-B testing per the companion skill; affiliate sign-ups + disclosure + links per §6 here.
GATE 2 — COMPLIANCE before publish: verify current policy from the platform's own docs → AI/synthetic disclosure only if visuals warrant it (when in doubt, disclose) → material variation (avoid "inauthentic") → cleared music. Then re-verify live prices.
Write findings and decisions into the vault (update the relevant note in place).