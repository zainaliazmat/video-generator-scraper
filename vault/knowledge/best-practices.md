---
summary: The LIVING synthesis of what our own video studies prove about hooks, structure, and failure modes. Evidence accumulates here; patterns confirmed ~3× get promoted into the skills.
updated: 2026-07-27
source: video studies under knowledge/video-studies/ + publish-pack research under videos/*/youtube-metadata* (evidence lines carry their study + date)
---

# Best practices — earned from our own studies

**Charter:** the skills ([[../skills/long_form_scripting]]) hold researched
*hypotheses*; this note holds what OUR studies of real videos in OUR niche
actually show. Every claim = a dated evidence line pointing at a study note.
~3 independent confirmations → promote into the skill and mark it promoted here.
Contradictions are findings too — log them, don't delete the hypothesis.

## Hooks (what the winners actually do in 0–30s)
Baseline hypotheses to test (from the skill, unproven on our own data yet):
payoff promise by ~0:15 · open loop ≠ announcement · result-first works ·
no greeting/bumper.
- Self-demonstrating hook: the video shows the tool's output ON ITSELF while the
  VO narrates (capability montage, 0:00–0:12) — study:[[video-studies/claude-video-editing-launch]] (Nate, 363k) — 2026-07-04
- Identity-twist + roadmap hook: pattern interrupt ("what you're watching isn't
  me") then a time-boxed roadmap of exactly what you'll learn — study:[[video-studies/claude-video-editing-launch]] (Simon, 19× views/sub) — 2026-07-04
- Quantify the manual pain early ("this 23-second clip = ~2 hours by hand") —
  study:[[video-studies/claude-video-editing-launch]] (Nate) — 2026-07-04
- Ordinary-life cold open + dramatic irony ("in about 4 hours, every one of
  these people…") — five human vignettes before any spectacle; promise by 1:19 —
  study:[[video-studies/pompeii-last-day]] (Fading Lore, 10.7× views/sub) — 2026-07-07

## Structure & retention
Baseline: value delivered fast (no withholding in action formats) · mid-video
(~55–65%) opens on tension · a teased reward pays ~70% · but/therefore bridges.
- Winners in the AI-video lane are LONG: 31:57 / 18:08 top performers (3rd
  confirmation of 18–32 min pattern) — study:[[video-studies/claude-video-editing-launch]] — 2026-07-04
- Give the starter away free (repo/template/prompts) and say so in the hook —
  study:[[video-studies/claude-video-editing-launch]] (Nate) — 2026-07-04
- End by opening the NEXT tutorial explicitly ("watch that now") — session-time
  play — study:[[video-studies/claude-video-editing-launch]] (Simon) — 2026-07-04
- History-lane breakouts are also long-form: 31:37 / 22:25 (4th+5th confirmation
  of the 18–32 min pattern, second niche) — study:[[video-studies/pompeii-last-day]] — 2026-07-07
- Parchment/period-texture infographic cards (myth-vs-reality tables, numbered
  process diagrams) = motion graphics that don't break immersion in history
  content — study:[[video-studies/pompeii-last-day]] (Fading Lore) — 2026-07-07

## Packaging (title/thumbnail seen in the wild)
Baseline: keyword-front-loaded titles for small channels · thumbnail = second
hook, not the title repeated.
- **Anchor the title to a HIGH-SEARCH term (brand or "Claude"), never to an
  unknown tool name** — Simon rode "HeyGen" to 140k on 7.4k subs; MSG led with
  "HyperFrames" (zero search) and died at 139 views —
  study:[[video-studies/claude-video-editing-launch]] — 2026-07-04
- The reframe-title move: "Not X. The thing before X." differentiates inside a
  saturated topic ("The Last Morning | A Day in the Life of a Doomed City") —
  study:[[video-studies/pompeii-last-day]] (Fading Lore) — 2026-07-07
- **Title research is 20 minutes of REAL data, not brainstorming** (method, proven on Pompeii):
  (1) YouTube autocomplete (`suggestqueries.google.com/complete/search?client=firefox&ds=yt&q=…`)
  across seed queries → the literal strings people type, ranked by appearing early for short
  seeds; (2) scrape competitor titles + view counts (`curl -A <browser-UA> youtube.com/watch?v=…`,
  grep `"viewCount"`) → which formula actually won. Pompeii result: "pompeii city history in urdu"
  autocompletes for bare "pompeii"; "Lost City + URDU HINDI + curiosity" title = 5.46M views vs
  40× less for a plain "documentary" label; Roman-Urdu phrases have zero Latin-script volume —
  full data:[[../videos/video-hist-01-pompeii/youtube-metadata]] — 2026-07-18
- **US personal-finance title formula: a specific dollar number + a time bound + an
  objection-killer** — "How to Build an Emergency Fund in 60 Days (**Even If You're Broke**)" 65k ·
  "How to Build an Emergency Fund **from $0**" 15k · "How Much Emergency Cash You **Actually** Need
  Saved" 30k; the contrarian variant works too ("Your Emergency Fund **Isn't Big Enough** in 2026").
  Biggest title on the board (199k) was the **first-$1,000** angle, and `2026` in the title is
  common across the performers. A bare "Emergency Fund Guide" label sits in the hundreds — the same
  plain-label penalty Pompeii showed —
  full data:[[../videos/emergency-fund/youtube-metadata-en]] — 2026-07-27
- **Method upgrade:** step (2) of the title-research method no longer needs hand-rolled curl —
  `PYTHONPATH=backend venv/bin/python` → `youtube_scraper.build_search_url(kw)` +
  `scrape_url(url, N)` returns titles, view counts, durations and channels for a whole search page
  (default `sp=` filter = last 12 months, which is what you want for "who is winning *now*").
  Reuse the project's own engine — 2026-07-27
- **Split the market's demand between the cuts, don't merge it.** Bare "emergency fund"
  autocompletes into a mostly Hindi/Hinglish cluster (`…kaise banaye`, `…kaha rakhe`, `…warikoo`);
  the US strings sit under different seeds (`emergency fund how much`, `where to put…`,
  `high yield savings account…`, `save $1000`). Tag each cut to its own cluster — mixing them
  dilutes the signal on both — 2026-07-27
- **Urdu/Hindi market searches in ENGLISH keywords + "in urdu/hindi"** — tags/titles must ride
  English search strings; Roman-Urdu phrases don't autocomplete ("pompeii ka…" → karaoke) —
  our research:[[../videos/video-hist-01-pompeii/youtube-metadata]] — 2026-07-18

## Thumbnails (the ~50% lever — the click gate)
The thumbnail decides whether anyone sees the content at all. Creator's rule: it's ~50% of
whether a video goes viral. Rules from research + real competitor teardown + our builds
(updated 2026-07-10; sources: ampifire/thumbmagic/bananathumbnail 2026 + the 6 top "Claude
video editing" thumbnails we downloaded & analyzed — Nate Herk 363k, "IS INSANE", "Edited By Claude").

**⚠️ Hard-won correction (2026-07-10):** ENERGY BEATS AUTHENTICITY. Our first video-02 pass used
real B&W footage from the video — it was authentic and DULL, and the creator rejected it outright.
Winning thumbnails are LOUD: saturated punchy color, glow, fire, glossy 3D, drama, crisp sharpness.
Real muted footage (esp. B&W history) is scroll-past. Juice everything. AI-designed drama (Canva) is
fine and usually better than a literal screenshot.

- **Energy first:** vivid saturated color, dramatic glow/fire/lightning, glossy, sharp, high contrast.
- **Brand-logo battle (the niche formula that wins in AI-tools):** the tool's REAL logo is the
  glowing hero; the competitors it beats are shown DEFEATED — cracked, shattered, or on fire
  (Premiere/DaVinci/After Effects). Uses the actual recognizable app icons. This is THE pattern in
  every top "Claude video editing" thumbnail. Use the **pixel-accurate real logo**, not an AI approximation.
- **One idea, ≤3 elements** (>3 ≈ 23% lower CTR); hero fills 30–50% of frame.
- **≤3–5 words, huge bold font (700+)**; put the punch word in a **colored keyword box** (red/orange)
  or a contrasting color — "It's over.", "IS INSANE" (red box), "EDITED BY **CLAUDE**".
- **Text upper area** (bottom-right = timestamp zone); high contrast on its background.
- **Face lifts CTR ~25–30%** if you have one (pointing/reacting). We're faceless → lean on the
  logo-battle + drama instead (Nate's 363k is faceless: crowned Claude + cracked editors).
- **Don't over-bait:** CTR with weak retention gets punished (watch-time share is weighted).
- **Specs:** 1280×720, < 2 MB. Text in English per [[english-titles-descriptions]].
- **Build:** Canva `generate-design` (design_type youtube_thumbnail) for the polished vibrant scene;
  composite the exact real logo locally (ImageMagick) if the AI's version is off. Study the top
  competitors first: `curl https://img.youtube.com/vi/<VIDEO_ID>/maxresdefault.jpg` → view → copy the pattern.
- **Anti-pattern:** literal real screenshots / muted archival photos as the whole thumbnail = dull = no clicks.
- **Thumbnail aesthetic is DECOUPLED from the video's aesthetic** — optimize the thumb for the CLICK, the film for RETENTION. Our shipped HIST-01 "A Century of Travel" is a deliberately muted vintage B&W parallax film, yet its thumbnail is a loud saturated liner-vs-jet lightning split. 2nd confirmation of energy>authenticity (video-02 was 1st) — our own build:[[../videos/video-hist-01-travel/index]] — 2026-07-10
- **The thumbnail must state the SUBJECT, not just the payoff.** HIST-01's first pass said only "WEEKS→HOURS" (the payoff) — it never told a scroller *what the video is*. Adding a top line "180 YEARS OF TRAVEL" fixed it. Rule: small top line = subject + scale, huge main line = payoff — our own build:[[../videos/video-hist-01-travel/index]] — 2026-07-10
- **⚠️ Scoping correction (2026-07-18, Pompeii): energy lives in the IMAGE, not in clickbait text
  furniture.** Creator rejected 4 Pompeii thumbs styled with the red keyword box + heavy outlined
  sans ("the main issue is the style") — but kept the LOUD dramatic base image (distressed face +
  erupting volcano). Final thumb = dramatic saturated imagery + typography from the video's own
  design system (Playfair serif, ember accent). So: energy>authenticity still holds for the
  *picture*; the *type* must match the channel's design language — the red-box/MrBeast text grammar
  is an AI-tools-niche pattern, not universal. Recipe: [[design-cinematic-history]] → Thumbnails —
  our own build:[[../videos/video-hist-01-pompeii/index]] — 2026-07-18

## Failure modes (low-performer autopsies)
What demonstrably kills videos in this niche — each entry names the mechanism,
not just "low views".
- Zero-search title anchor + no audience = no distribution path at all (the
  script's quality never got a chance) — study:[[video-studies/claude-video-editing-launch]] (MSG, 139 views) — 2026-07-04
- Jargon word-salad + "subscribe" CTA at 0:18, before any value — the skill's
  #1 hook mistake observed killing a real video — study:[[video-studies/claude-video-editing-launch]] — 2026-07-04
- Me-centric framing (creator as hero, viewer's payoff late) — StoryBrand
  inversion in the wild — study:[[video-studies/claude-video-editing-launch]] — 2026-07-04

## Promoted to skills
- *(none yet — first promotion after ~3 confirming studies)*
