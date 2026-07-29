# fin-script log — good-debt-vs-bad-debt / hi / attempt 1

- **Date:** 2026-07-28 · **Tier:** short (blockframe-9) · **Target:** 165s
- **Read:** vault/CLAUDE.md, tools/format.json, run.json, facts-staging.md,
  vault/skills/long_form_scripting.md, vault/knowledge/niches/india-finance-market.md,
  design-finance-blockframe.md, reference vault/videos/pay-yourself-first/script-hi.md
  + needs-vs-wants/script-hi.md.
- **Study note missing:** vault/knowledge/video-studies/good-debt-vs-bad-debt.md does
  not exist — fin-research rescued for exactly this (run.json). Proceeded on the
  creator brief + facts-staging + vault knowledge; scrape debt already in `owed`.

- **ORTHOGRAPHY CONFLICT (flagged, not followed):** the task called this a
  "Nastaliq-script hi cut." Written in **Devanagari Standard Hindi** instead —
  `format.json cuts.hi` locks voice **Harsh** (standard `hi`), the contract says
  Standard Hindi, and both shipped hi scripts are Devanagari. Nastaliq is the
  separate Urdu story lane (MEMORY note is scoped to "Urdu scripts", different
  voice); no Urdu finance channel exists in format.json. A Nastaliq/Urdu script
  read by Harsh = hard TTS failure. No config changed. Surfaced in the script
  header + return line for the orchestrator.

- **Wrote:** vault/videos/good-debt-vs-bad-debt/script-hi.md — 9 segments,
  ~2,070 Hindi chars ≈ ~2:46 at 12.5 c/s (format.json rate) vs 165s target
  (on-target; char counts are estimates, build ffprobe-measures + adds 0.4/1.0
  lead-in/tail per scene).
- **Brief compliance:** hook = "minimum payment is a trap, here's the actual math"
  rendered as the month-1 split (₹2,583 / ₹1,667 interest / ₹916 principal), payoff
  promised by ~15s; all four core beats mapped — debt=renting money (s3),
  good vs bad debt (s4), how the minimum works (s5), compounding against you (s5);
  action step "minimum + ₹1,000" (s6/s8); loop closes s9.

- **Hero-math discipline:** VO speaks only floor-independent robust anchors —
  month-1 split, "a year barely moves it (~₹40,000)", payoff as a round range
  (17+ years / nearly ₹90,000 / more than borrowed). The false-precise integers
  (208 months · ₹88,614) sit **on screen only**, tagged build-calculator-locked;
  build-handoff #5 requires they be regenerated from the ₹100-floor model, not
  hand-typed. No single-bank APR on screen (used "~40%, illustrative range").
  No fabricated "+₹1,000 saves ₹X" — kept qualitative (no build-locked figure).

- **Numbers:** all traced in the script's fact-trace table to facts-staging lines
  (₹50,000 hero, month-1 COMPUTED split, Claim ₹-1 APR, Claim ₹-2 5%+₹100 floor,
  Month-12 closed form, payoff range, action ₹1,000). No SOFT row on screen; no
  untraceable number. Pure-5%-no-floor asymptote available but omitted (too
  technical for a short).

- **Rules honoured:** digits spelled out in VO (no bare numerals), on-screen
  numerals exact with en-IN grouping; on-screen text English/Hinglish; Standard
  Hindi for Harsh (no Haryanvi/Urdu markers); ₹ only, zero `$`/US content (forbidden
  for hi); no host persona / no first-person expertise / no card/fund pick (card =
  generic instrument, APR+minimum as issuer/RBI price evidence only); every scene
  carries a keyword-matched bg (photo_free_scene_ratio 0, creator rule 2026-07-28);
  colour intent set red=interest trap per design §2; timing table included.

- **Did NOT:** read .env, read haryanvi-hindi-script-style.md, write to .claude/ or
  tools/, run Bash/git.
