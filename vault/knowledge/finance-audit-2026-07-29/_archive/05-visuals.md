# 05 — Imagery: what's in the frame, and where it comes from

Scope: image sourcing for @cashguruguides (₹/hi) + @moneymavens101 ($/en).
Every claim tagged `FACT` (verifiable from a file, a rendered artifact, a spec, a
cited source, or a reproduced code behaviour) or `UNVALIDATED` (belief about
audience response — untested, no analytics exist).

Read-only pass. Nothing in `/home/zain-ali/Documents/YoutubeScraper` was modified.
No paid image API was called. The two code bugs in §3 were proved offline using
the fetcher's own `FIN_FAKE_APIS=1` mode in the scratchpad.

---

## 1. Diagnosis — what a pair actually costs

### 1.1 How many distinct images a pair needs

`FACT` — counted from archived `.src` files and live manifests:

| Pair | hi slots | en slots | pair total | source |
|---|---|---|---|---|
| pay-yourself-first | 9 | 9 | **18** | `vault/videos/pay-yourself-first/src/{hi,en}/assets/img/*.src` |
| good-debt-vs-bad-debt | 16 | 16 | **32** | `vault/videos/good-debt-vs-bad-debt/src/{hi,en}/assets/img/*.src` |
| credit-history | 13 | 11 | **24** | `studio/videos/credit-history-{hi,en}/assets/img/manifest.json` |

So **18–32 distinct images per pair, median ~24–25**. Nine are backgrounds
(one per blockframe-9 scene, mandatory since the 2026-07-28 creator rule);
the rest are cut-ins, which may be dropped.

At **2 pairs/week ≈ 8.7 pairs/month**, that is **~210 accepted images/month**.

### 1.2 What it costs to get them

`FACT` — from the milestone notes:

- **credit-history** (`vault/videos/credit-history/index.md`): "Pixabay: **hi 34
  fetches over 4 rounds** (14 accepted, 3 cut-ins dropped), **en 41 fetches over
  6 rounds** (11 accepted, 6 cut-ins dropped) — the retry ladder, not the budget,
  is what this cost." → **75 fetches / 10 rounds per pair for 24 kept = 3.1
  fetches per accepted image.**
- **good-debt-vs-bad-debt** (`vault/videos/good-debt-vs-bad-debt/index.md`):
  "**144 Pixabay calls** (hi 48 + 30 frame-gate re-source, en 66)" for 32 kept
  = **4.5 calls per accepted image**, and the hi cut needed "a full 5-slot
  re-source" after the frame gate.

Extrapolated to 8.7 pairs/month: **~650–1,250 stock API calls and 40–85 retry
rounds per month.**

**The API calls are free. The cost is entirely agent time.** Pixabay and Pexels
are both free at this volume — 650–1,250 calls/month sits far under the Pexels
default ceiling of 200 requests/hour and 20,000/month
([Pexels API docs](https://www.pexels.com/api/documentation/)). What is being
spent is fin-assets vision passes and, when the frame gate fails, whole extra
`fin-build` + `fin-render` cycles. credit-history paid one of those
(`vault/videos/credit-history/index.md`: the car-fob re-frame "cost a full extra
build + render cycle"); good-debt paid another (both cuts landed on attempt 3).

**So the real per-pair imagery cost is ~10 retry rounds of agent time plus a
~1-in-2 chance of an extra render cycle — not money.** Any proposal that costs
money but removes rounds is trading the expensive resource for the cheap one.

### 1.3 The recorded failure modes, and what they have in common

From `vault/knowledge/stock-photo-sourcing.md`,
`vault/knowledge/design-finance-blockframe.md` §7, and the two milestone notes —
all `FACT`:

- India-people queries: **~20% first-try usable**. Pixabay's India library is
  "heritage- and tourist-heavy and almost empty of contemporary urban-professional
  life."
- One demonetised ₹500 pile is "the immovable #1 for every rupee query"; "~3 clean
  rupee images exist channel-wide."
- Homonym traps recur: "bill"→a bird, "coins"→a €1 coin.
- The frame gate caught an antique coin **depicting a Hindu deity** (revered-figure
  violation), German legal text, a Polish metallurgy book, and a US road in the ₹ cut.
- A phone-screen background has shipped **three times undetected** carrying `AT&T`,
  a legible Facebook login, and `MTN-SA`.
- One `s9.jpg` is **byte-identical in three shipped projects across both channels**.
- credit-history hit **seven hash collisions in one run**, none from adjacent slugs.

Every one of these is the same underlying fact: **a stock search returns whatever
the index returns, and the pipeline has no way to constrain it.** `#N` picks a
different wrong thing; a synonym picks a different index. There is no knob that
says "Indian, current-series, no deity, no brand, no Latin text, no faces."

### 1.4 The finding the vault has not written down: the retry ladder converges on generic

`FACT`. Compare the final accepted queries across three consecutive pairs
(`.src` files / manifests, listed in §1.1):

- **pay-yourself-first hi** — 3 India signifiers in 9 slots: `indian rupee coins
  scattered table#3`, `crowded indian market shopping bags`, `mumbai skyline sunrise`.
- **good-debt hi** — 2 India signifiers in 16 slots (`indian 2000 rupee note pink#2`,
  `hand giving indian rupee cash notes`), and the first of those is defective (§4.2).
- **credit-history hi** — **zero India signifiers in 13 slots**. The final accepted
  manifest is `rows of archive files on shelves dark`, `manila folder`, `old
  documents`, `accounting ledger`, `open desk diary`, `red rubber stamp`, `calendar`,
  `pocket watch`, `blueprint`, `document`, `pen ticking boxes`, `open door sunlight`.
  The en cut is the same family: `card index`, `cardboard boxes`, `manometer#2`,
  `hourglass#6`, `lamp`, `red pen`.

The credit-history note records the mechanism approvingly — "Short one-noun queries
beat descriptive phrases… landed 9 of 12 retries **and produced the best images in
the set**" — and it is true that one-noun queries have a higher hit rate. But the
reason is that **a one-noun query asks for less**, and what it gives up is exactly
the market specificity that distinguishes the ₹ channel from the $ channel. The
retry ladder is a ratchet: each round trades specificity for availability, and it
only turns one way.

Terminal state, reached in three pairs: **the India cut of an India-market finance
video contains no Indian imagery, and the two cuts of a pair are separated only by
the currency glyph in the type layer.**

`UNVALIDATED` — whether an Indian viewer notices or cares. No analytics exist.
But see §5.3: this is also a monetisation-policy exposure, which is not an
audience question.

### 1.5 A second undocumented convergence: one query, several slots

`FACT`. good-debt-vs-bad-debt **en** shipped these background queries
(`vault/videos/good-debt-vs-bad-debt/src/en/assets/img/*.src`):

```
s1.jpg.src   us dollar bills#5
s3.jpg.src   us dollar bills#6
s8.jpg.src   us dollar bills#7
s2.jpg.src   us dollar bills spread on table#4
s6.jpg.src   hundred dollar bills fanned out#4
s6-cut.jpg.src  hand giving a us dollar bill#2
```

**Three of nine backgrounds are the same query at three consecutive ranks**, and
six of sixteen slots in the video are a photograph of banknotes. Within-video
near-duplication is not covered by the md5 rule (the bytes differ) and is not
covered by the frame gate (each image is individually clean). Nobody owns it.

---

## 2. The deduplication gap (task item 4)

### 2.1 Does the ledger exist in code? No.

`FACT`. `vault/knowledge/design-finance-blockframe.md:261` prescribes:

> "Key an asset ledger by md5 and refuse a hash already used anywhere."

Grepping `tools/`, `.claude/` and the repo for `md5|ledger|dedup`:

- `tools/stock/pixabay_fetch.py` — `hashlib.md5` appears **once**, at line 227,
  used to pick a fake placeholder colour in `FIN_FAKE_APIS` mode. It is not a
  dedupe mechanism.
- `.claude/agents/fin-assets.md:22,54` — the only enforcement is an instruction to
  the agent to run `md5sum studio/videos/*/assets/img/*.jpg` by hand.
- No ledger file exists anywhere in the repo (`find -iname "*ledger*"` → nothing).

So the prescribed control is **documentation, executed manually, with no persistence.**

### 2.2 And the manual substitute is now blind to every published video

`FACT`, and this is the more serious half. `vault/CLAUDE.md` (finished-video rule)
states that `archive_cut.py` **drops `*.jpg`** and then **deletes
`studio/videos/<slug>*`**. So the glob `studio/videos/*/assets/img/*.jpg` only ever
matches work still in production.

Measured today:

```
$ ls studio/videos/*/assets/img/*.jpg | wc -l        → 46
$ ... | cut -d/ -f3 | sort | uniq -c
     17 credit-history-en      (finance, NOT yet uploaded)
     13 credit-history-hi      (finance, NOT yet uploaded)
      6 credit-history-thumbs
     10 dark-truth-social      (a history video, different channel)
$ find vault/videos -name "*.jpg" | wc -l            → 0
```

**Zero of the 46 belong to any of the five live finance pairs.** Their images were
deleted at archive and survive nowhere. The dedupe check that fin-assets is told to
run cannot see 50-30-20-rule, emergency-fund, needs-vs-wants, pay-yourself-first or
good-debt-vs-bad-debt — the entire published corpus of both channels.

This is the root cause of the two recorded symptoms. The byte-identical `s9.jpg`
across three shipped projects went undetected because by the time the third was
built, the first two were archived and invisible. credit-history's seven collisions
were caught only because they were against `pay-yourself-first`, `emergency-fund`
and `50-30-20-rule-en` **while those were still in studio** — all three are archived
now, so the same collisions would pass silently today. The check degrades with every
successful delivery, which is the worst possible failure curve.

### 2.3 Spec for the real ledger

One append-only TSV at **`vault/assets-ledger.tsv`**, columns
`md5 · slug · cut · slot · provider · page_url · date`. It lives in the vault, not
in studio, so it survives `archive_cut.py` and is git-tracked — which also makes it
the audit trail the vault's own conventions ask for. `tools/stock/pixabay_fetch.py`
grows ~20 stdlib lines: after every successful `download()` in both `fetch_one()`
and `cmd_pick()`, hash the bytes; if the hash is already a row, delete the file,
print `DUPE <slot> — already used in <slug>/<cut>`, and exit non-zero so fin-assets
must re-pick rather than choose to notice; otherwise append the row. Because the
hash is taken at download time, the ledger records images whose files are long gone,
which is precisely the property the current `md5sum` glob lacks. Two deliberate
ceilings worth naming in the code: it catches **byte identity only**, so the same
photo re-encoded by a second provider slips through (upgrade path: a perceptual hash
— do not build it until byte-identity is actually enforced); and it is a plain file
with no locking, which is correct because `.claude/commands/finance-video.md:138`
already guarantees "`fin-assets` never runs for both cuts at once." Backfill is
impossible for the five archived pairs — their bytes are gone — so the ledger starts
from credit-history forward and that limitation should be stated in its header line.

---

## 3. Two proven bugs in `tools/stock/pixabay_fetch.py`

Both reproduced offline with the tool's own `FIN_FAKE_APIS=1` mode (no API calls,
nothing written inside the repo). Both are `FACT`.

### 3.1 `#N` is silently ignored on the default path

`cmd_candidates()` parses the query and **discards the rank**:

```python
provider, query, _ = parse_query(raw)      # line ~287 — `want` thrown away
hits = provider_hits(provider, query, n)   # always starts at result 1
```

Reproduction:

```
sheet("rupee notes") == sheet("rupee notes#3")  →  True   (byte-identical)
cands[0] for "rupee notes#3"                    →  result #1
```

`fetch_one()` (the single-image path) *does* honour `#N`. The contact-sheet path —
which `.claude/agents/fin-assets.md` names as **the default** ("sheets are the
default") — does not.

Why this matters specifically: `vault/videos/good-debt-vs-bad-debt/index.md`
records that for rupee queries "one demonetised ₹500 pile is the immovable #1 …
**escape only via `#N`**". On the default path **that escape does not exist.** The
agent writes `#3`, believes it has stepped past the poisoned top hit, and is served
the poisoned top hit as cell 1 of six. This also explains a lesson the vault wrote
down as a search-behaviour insight — "`#N` on a bad long query only returns more of
the same wrong thing" — which is a reasonable inference from the observation, but
the actual cause is that `#N` was doing nothing at all.

Fix: pass `want` through and slice `hits[want:want+n]`, fetching `want + n`.

### 3.2 `.src` does not record which cell was picked — the archive cannot reproduce a cut

`cmd_pick()` writes the sidecar as:

```python
open(out + ".src", "w").write(meta["query"])     # line ~364 — `k` is dropped
```

The chosen cell index `k` is never persisted. Reproduction:

```
pick cell 4 → a.jpg ;  a.jpg.src == "rupee notes"
re-fetch from the archived .src → different bytes than shipped  (False)
```

This **falsifies a load-bearing claim in `vault/CLAUDE.md`**, which states that
archives keep "`assets/img/*.src` (the image prompts)" and that "Re-render is
reproducible, not free — … a rebuild re-pays image gens + ElevenLabs off the
archived prompts and lines." For every image promoted through the contact sheet —
the default path — the archived `.src` returns **result #1 of the query**, not the
image that shipped. The pick is unrecoverable.

Fix: write `f"{base_query}#{k}"` (with any existing `#N` stripped, since cells are
indexed from result 1 — and note this fix is only correct *after* 3.1 is fixed).

### 3.3 The two bugs have already poisoned a live video's archive

`FACT`, and this is the concrete consequence. In good-debt-vs-bad-debt (live on
YouTube since 2026-07-29):

- `vault/videos/good-debt-vs-bad-debt/src/hi/assets/img/s2.jpg.src` reads
  `indian 2000 rupee note pink#2`.
- `vault/videos/good-debt-vs-bad-debt/logs/fin-render-hi-2.md:18` records that s2
  was re-sourced after the frame gate flagged it **HIGH / revered-figure**, and the
  shipped pixels are "four rolled CURRENT legal-tender notes ₹10/₹20/₹50/₹100 …
  CLEAN."
- Line 42 of that same log: "manifest.json still records s2's query as 'indian 2000
  rupee note pink#2' — stale/misleading … **Flag for fin-assets to correct the
  ledger string**; does not block."

That correction was never made before `archive_cut.py` ran, and the studio copy is
now deleted. **Re-rendering the hi cut from its archive would re-fetch the query
that produced the revered-figure violation the frame gate caught.** The one
safeguard — the log — is a prose note in a different file that no tool reads.

Worth adding to the vault as a trap in its own right: the **₹2000 note was
withdrawn from circulation by the RBI on 2023-05-19** and 98.45% had returned as of
2026-03-31, though it remains legal tender
([RBI FAQ](https://www.rbi.org.in/commonman/english/scripts/FAQs.aspx?Id=3443)).
`vault/knowledge/stock-photo-sourcing.md` documents only the pre-2016 ₹500 trap.
A ₹2000 note on screen in 2026 reads as dated to an Indian viewer for the same
reason the old ₹500 does, and the vault does not warn about it anywhere except
inside one render log.

---

## 4. Options, with 2026 prices

### 4.1 AI generation

Per-image API prices, July 2026:

| Model | $/image | Notes |
|---|---|---|
| **Imagen 4 Fast** | **$0.02** | flat per image |
| **Imagen 4 Standard** | **$0.04** | flat |
| Imagen 4 Ultra | $0.06 | flat |
| Flux 2 Schnell / Dev / Pro | $0.015 / $0.025 / **$0.05** | Pro ≈ cinema-grade photoreal |
| **Nano Banana** (Gemini 3.1 Flash Image) | **$0.067** @1K | range $0.045–$0.151 by resolution |
| Gemini 3.1 Flash Lite Image | $0.0336 @1K | ~2.7× faster |
| **Nano Banana Pro** (Gemini 3 Pro Image) | **$0.134** @1K/2K | $0.24 @4K; GA June 2026 |
| Ideogram 3.0 | $0.03–$0.09 | best text-in-image |
| Recraft V4 | $0.04 raster | |

Sources: [Gemini pricing breakdown](https://developer.puter.com/tutorials/gemini-api-pricing/),
[Gemini image cost calculator](https://www.aifreeapi.com/en/posts/gemini-image-generation-api-pricing),
[Flux/Ideogram/Recraft comparison](https://apiscout.dev/guides/flux-vs-ideogram-vs-recraft-image-gen-api-2026),
[provider price comparison](https://www.digitalapplied.com/blog/ai-image-generation-api-pricing-comparison-2026).

Two multipliers: the **Batch API halves any Gemini price** if 24h latency is
acceptable (it is — assets are sourced long before render). And a **free tier**
exists: ~500 images/day via the API and 500–1,000/day via AI Studio, though API
free-tier quotas were cut by up to 92% on 2025-12-07 and should not be planned
around ([free tier guide](https://www.aifreeapi.com/en/posts/gemini-image-generation-free-api)).

**Suitability for this format.** Nano Banana Pro is reported strong on photoreal
lighting/texture, on hands and small objects, and on holding a consistent look
across a set — which is what a 9-image scene set needs
([review](https://designforonline.com/ai-models/google-nano-banana-pro-gemini-3-pro-image-preview/),
[DataStudios report](https://www.datastudios.org/post/nano-banana-pro-full-report-and-review-of-the-google-s-gemini-3-ai-image-generation-engine-compar)).
`UNVALIDATED` at the level that matters here: none of these benchmarks tested
Indian domestic interiors, Indian street furniture, or Indian financial paperwork,
and this project has no measurement of its own. The project *does* already have a
working convention for one-shot over-specified photoreal prompts — the history
channel's `vault/videos/video-hist-01-pompeii/image-prompts.md` pattern — so the
prompt craft is not new work.

**The one thing AI should not be asked to do: banknotes.** Photoshop and other
imaging software have refused currency images for years via the CBCDG Counterfeit
Deterrence System and the EURion constellation, and generative models inherit
similar restrictions; more importantly, a *plausible but wrong* ₹500 note is
strictly worse than a real photo of a withdrawn one, and it is exactly the defect
class this pipeline already ships. Currency slots must stay photographic.

This creates the apparent deadlock: the vault's object-led rule makes **₹ notes the
load-bearing India signifier** ("The ₹500 notes and Indian coins say 'India' more
reliably than any stock photo of an Indian person"), and ₹ notes are precisely the
~3 clean images that exist. The resolution is to **stop making currency carry the
market signal.** Indian *environments and objects* — a kitchen counter, a shop
QR-code standee, an EMI passbook, a scooter, a steel tiffin, a Mumbai local — carry
"India" at least as well, are what stock genuinely lacks, and are what AI renders
well and safely. That is a substrate change, not just a supplier change.

### 4.2 Stock — free

| Source | Cost | Rate limit | Monetised YouTube? | Attribution |
|---|---|---|---|---|
| **Pixabay** | free | generous | yes | not required |
| **Pexels** | free | 200/hr, 20k/mo default; unlimited free on approval | yes, explicitly | not required |
| **Unsplash** | free | **50/hr Demo**, 5,000/hr on Production approval | yes | **required when sourced via the API** |

Sources: [Pexels API](https://www.pexels.com/api/documentation/),
[Pexels rules](https://help.pexels.com/hc/en-us/articles/360042332714-What-are-the-rules-for-using-Pexels-photos-or-videos),
[Unsplash API Terms](https://unsplash.com/api-terms),
[Unsplash rate limits](https://help.unsplash.com/en/articles/3887917-when-should-i-apply-for-a-higher-rate-limit),
[Pixabay license analysis](https://picdefense.io/resources/source-intel/pixabay/).

**Is any free pool deeper for India-finance? No — and the headline counts lie.**
Measured directly:

- Pexels `indian rupee` → claims **68.5K**, but the visible first page is a mix of
  current notes, coins, and **vintage/demonetised** notes — the same contamination
  as Pixabay.
- Pexels `indian office worker` → claims **198.7K**, and the first twelve results
  are textile-factory workers and generic office workers of assorted ethnicities.
  The count is fuzzy-match noise; the India-specific depth is not there.
- Unsplash `indian rupee` → **550+**, and the first page already leaks US dollars
  and euros.

This is the important negative result: **`@pexels` is a different pool, not a
deeper one.** It works as a dedupe escape hatch (which is how
`.claude/agents/fin-assets.md` uses it, correctly) and it does not solve the India
problem. Adding `@unsplash` would add a third shallow pool plus an attribution
obligation (below) — not worth it.

### 4.3 Stock — paid

Adobe Stock ~$29.99/mo for **10 assets**, ~$49.99 for 25, ~$249.99 for 750.
Shutterstock from $29/mo for 10 images. Envato Elements $16.50/mo annual for
unlimited downloads. Freepik from $14.50/mo annual (rebranded to Magnific,
2026-04-28). Sources:
[Adobe Stock pricing](https://photutorial.com/adobe-stock-pricing/),
[Adobe vs Shutterstock 2026](https://josephnilo.com/blog/adobe-stock-vs-shutterstock/),
[Freepik pricing](https://photutorial.com/freepik-pricing/),
[Adobe Stock alternatives](https://photutorial.com/best-adobe-stock-alternatives/).
Both Adobe and Shutterstock expose REST APIs
([Adobe Stock API](https://developer.adobe.com/stock/docs/getting-started/),
[Shutterstock API](https://api-reference.shutterstock.com/)).

Adobe's India depth is genuinely better — **30,348 results for the exact phrase
"indian rupees"** vs 50,787 loose — and paid libraries carry indemnification the
free ones do not. But at ~210 images/month the only Adobe tier that fits is the
**$249.99/mo / 750-asset plan**, or Envato Elements at $16.50/mo unlimited.
Envato is the only paid option that is price-competitive, and it has no documented
public API, which means fin-assets would lose the scripted contact-sheet flow and
go back to manual downloads — trading away the one thing that made the asset stage
cheap. Not recommended.

### 4.4 Recommendation — hybrid, AI-first, at ~$11–19/month

At 8.7 pairs/month ≈ **210 accepted images**, assuming ~1.4 generations per
accepted image (the history channel's one-shot over-specified prompt doctrine
targets 1.0; 1.4 is a conservative allowance for the frame gate) ≈ **~295
generations/month**:

| Model | Monthly | With Batch API (24h) |
|---|---|---|
| Imagen 4 Fast $0.02 | **$5.90** | — |
| **Imagen 4 Standard $0.04** | **$11.80** | — |
| Flux 2 Pro $0.05 | $14.75 | — |
| **Nano Banana $0.067** | **$19.77** | ~$9.89 |
| Nano Banana Pro $0.134 | $39.53 | ~$19.77 |

**Recommended split, ~$15/month all-in:**

- **Currency, and only currency, stays photographic.** ~2–3 slots per pair.
  Free stock (Pixabay/Pexels) as today, with the frame gate unchanged. This is
  where the ₹500/₹2000 traps live and where fabrication is unacceptable.
- **Everything else generated** — ~21–22 slots per pair. Nano Banana (or Imagen 4
  Standard for the pure-texture plates, which do not need the better model).
  ~$15/mo at the blended rate; under $10 on the Batch API.
- **Keep Pexels wired** as the fallback when a generation is rejected twice — it
  already works and costs nothing to keep.

What this buys, and it is the point: **the retry ladder collapses.** A prompt can
say "current-series Indian ₹100 note, stone-grey ₹500 absent, no legible brand
marks, no human face, no Latin signage, no religious iconography, shallow depth of
field, dark" — a search box cannot say any of that. Homonym traps ("bill"→a bird),
cross-market bleed (a US road in the ₹ cut), foreign-language text (German legal
text, a Polish metallurgy book) and the revered-figure class all become
prompt-negatives rather than post-hoc rejections. **This is a trade of ~$15/month
of money for ~40–85 retry rounds/month of agent time plus roughly one avoided
build+render cycle per pair** — spending the cheap resource to save the expensive
one, which §1.2 established is the right direction.

It also, incidentally, makes §3.2 moot for generated slots: a prompt in `.src`
*is* fully reproducible in a way that "query + a lost cell index" never was.

---

## 5. Licensing and policy

### 5.1 Per-source terms

- **Pixabay** — free commercial use, no attribution. Prohibits depicting
  **identifiable persons in an offensive, pornographic, obscene, immoral,
  defamatory or libelous way**; model releases are the uploader's responsibility
  and the downstream user is expected to verify they exist, which is not practically
  possible at scale. Pixabay now also hosts AI-generated uploads, filterable in
  search. Documented supply-chain risk: stolen images have been downloaded
  >159,000 times before removal
  ([risk profile](https://picdefense.io/resources/source-intel/pixabay/)).
  The pipeline's existing rule — "no identifiable person as the subject of a
  negative money claim" (`.claude/agents/fin-assets.md:47`) — is the correct
  reading of this and is already enforced.
- **Pexels** — free personal and commercial, no attribution, explicitly usable in
  monetised YouTube. Cannot be sold standalone with no meaningful creative effort
  applied. **API terms prohibit data mining and using the API to train ML/AI models
  without explicit permission** — worth knowing before anyone proposes scraping
  Pexels to fine-tune anything.
- **Unsplash** — the download licence allows commercial use without attribution,
  **but the API Terms require attribution** for API-sourced images: photographer
  and Unsplash, with a clickable link to the photographer's profile. `FACT` and a
  real trap: if `@unsplash` were added the way `@pexels` was, the pipeline would
  silently inherit an obligation that a `CREDITS.txt` on disk does not discharge —
  it would have to appear in the video or description. Free tier is also only
  **50 requests/hour** in Demo status. Recommend **not** adding it.
- **Adobe Stock / Shutterstock** — paid, licensed for monetised commercial video,
  and indemnified. The reason to consider them is legal certainty, not depth.
- **Google (Gemini/Imagen)** — "Google does not assert any ownership rights in new
  intellectual property created in the Generated Output"; commercial use permitted;
  **rights are identical on free and paid tiers**; API data is not used for training
  ([output rights](https://terms.law/ai-output-rights/gemini/),
  [commercial use guide](https://banana-clean.app/blog/gemini-images-copyright-commercial-use)).
  Caveat worth stating once in the vault: AI-generated images are likely **not
  copyrightable** under current US/EU law, so nobody can stop a competitor reusing
  an identical-looking generation. Irrelevant at this scale; relevant if thumbnails
  ever become brand assets (another agent's scope).

### 5.2 Does AI imagery create a YouTube disclosure obligation in 2026? Yes — and it does not cost anything.

YouTube requires the altered-or-synthetic disclosure when content is realistic and
could be mistaken for a real person, place, scene or event — the policy's own
examples include "realistic scenes that never occurred" and "AI generated extra
footage of a real place." Exempt: clearly unrealistic content, colour/lighting
filters, special-effects filters, and **production assistance such as generating an
outline, script, thumbnail or title**
([YouTube Help](https://support.google.com/youtube/answer/14328491)).

Photoreal generated b-roll of an Indian kitchen that never existed sits on the
disclose side of that line. The scrim and the `brightness(0.62)` grade do not move
it — the grade is a filter applied to a synthetic scene, not a thing that makes the
scene unrealistic.

Two facts that make this cheap:

1. **Disclosure does not affect reach or monetisation.** YouTube states plainly:
   "Disclosing AI content won't limit a video's audience or impact its eligibility
   to earn money."
2. **It may happen automatically anyway.** YouTube began **auto-labelling**
   photorealistic AI content in **May 2026**, reading **C2PA metadata and SynthID
   watermarks**; Google embeds SynthID in Gemini/Imagen output by default
   ([TNW](https://thenextweb.com/news/youtube-will-now-automatically-label-ai-generated-videos-whether-creators-disclose-them-or-not),
   [detection guide](https://nerdleveltech.com/youtube-automatic-ai-labels-detection-c2pa)).

Non-disclosure, by contrast, is enforced: warning → 90-day monetisation suspension →
YPP removal. **Recommendation: tick the box. It is free, and the alternative is a
strike ladder.** `fin-package` writes the publish pack, so the disclosure line
belongs there.

### 5.3 The bigger policy risk is not AI imagery — it is duplicate assets as templating evidence

`FACT`. On 2025-07-15 YouTube renamed its "repetitious content" policy to
**"inauthentic content"**, defined as "mass-produced or repetitive content,"
including "content that looks like it was **made with a template with little to no
variation across videos**, or content that is easily replicable at scale." In
**January 2026** YouTube terminated **16 channels with a combined 35M subscribers
and 4.7B lifetime views** under it
([policy change](https://alternativeto.net/news/2025/7/youtube-updates-its-policy-to-demonetize-inauthentic-mass-produced-ai-generated-content),
[2026 enforcement](https://milx.app/en/news/why-youtube-just-suspended-thousands-of-ai-channels-and-how-to-protect-yours),
[repetitious content explainer](https://www.advertisingbusiness.org/ai-or-authentic-youtubes-repetitious-content-policy-explained/)).
Faceless is explicitly *not* the trigger; templating is.

Now line that up against what is already in the vault:

- **Six consecutive blockframe-9 cuts on both channels**, flagged three times,
  changed nothing (`vault/videos/credit-history/index.md` frontmatter).
- **One image byte-identical in three shipped projects across both channels.**
- **Three of nine backgrounds in a shipped cut from one query at consecutive ranks** (§1.5).
- **A ₹-market cut whose imagery contains nothing market-specific** (§1.4), making
  the pair's two cuts differ only in the currency glyph.
- **A dedupe check structurally blind to the entire published corpus** (§2.2).

`.claude/agents/fin-assets.md:59` already contains the right sentence —
"Byte-identical images across the grid are **mass-production evidence**" — but the
check that would catch it cannot see the evidence. Duplicate assets are the
machine-readable half of a templating case, and it is the half that is trivially
auditable from outside. This is the highest-severity item in my scope, and the
`vault/assets-ledger.tsv` fix in §2.3 is the cheapest available mitigation.

`UNVALIDATED`: whether either channel is actually near an enforcement threshold.
Nobody outside YouTube can know that, and no analytics exist here.

---

## 6. Is graded full-bleed stock even the right substrate?

### 6.1 What the grade actually leaves

`FACT`, from `vault/videos/good-debt-vs-bad-debt/src/en/index.html`:

```css
.bg    { filter: grayscale(0.32) brightness(0.62) contrast(1.05); }
       + linear-gradient(180deg, rgba(13,16,23,.40), rgba(13,16,23,.10) 46%, rgba(13,16,23,.52))
.grain { opacity: 0.05; mix-blend-mode: overlay; }
```

plus a slow Ken Burns push per scene and heavy type over the top. After 32%
desaturation, a 38% luminance cut, a four-layer scrim and grain, what survives is
luminance variation, edge texture and a vague silhouette. The vault says this
outright: photos "are **texture, not information**."

**The asymmetry is the finding.** The subject contributes almost nothing to
comprehension — proved by §1.4, where a `manometer` and a `pocket watch` sit under
credit-history's VO without anyone objecting. But the subject still contributes
liability: the frame gate caught a Hindu deity, German legal text, a Polish
metallurgy book and a US road *through the same grade*. **The substrate carries
downside risk without carrying upside value.** Anything that keeps the texture and
removes the uncontrolled subject is a strict improvement.

This also sharpens the 2026-07-28 creator rule. "Every scene must carry an image"
is what forces the retry ladder to run to exhaustion — fin-assets may no longer
drop a background, so it must accept *something*, and "something" is how a
`manometer` gets in. The rule is defensible; its cost is just currently paid in the
wrong currency.

### 6.2 Ranked alternatives for *this* format

1. **Generated photoreal plates (recommended).** Identical visual language, so no
   design-system change and no other agent's scope is touched. Removes homonym
   traps, brand marks, cross-market bleed, foreign text and the revered-figure class
   by construction, since every one becomes a prompt negative. ~$0.04–0.067/image.
   Costs a YouTube disclosure (free, §5.2). Cannot do banknotes.
2. **Data-viz as background.** An amortisation curve behind the amortisation number;
   a 36-month decay behind the CIBIL line. Zero licensing risk, zero sourcing cost,
   deterministic, fully re-labelable per market (₹/$ on one axis), and it is the one
   option that puts *information* on screen that survives the grade, because line art
   on dark reads at `brightness(0.62)` where a photograph does not. It satisfies
   "every frame has an image" without any sourcing at all. Two caveats: it belongs to
   `fin-build`, not `fin-assets`, so it crosses an agent boundary; and it cannot fill
   all nine scenes without becoming its own kind of sameness. Best used for the 2–3
   number-carrying scenes per cut.
3. **Abstract / macro texture.** Already the ladder's terminal rung, already
   sanctioned ("the densest scene gets the calmest background"). Safe and free — and
   it is exactly what produces the sameness in §5.3. Keep as fallback, not default.
4. **Motion texture** (drifting gradients, film grain, slow noise). Deterministic and
   free, but the format already runs a Ken Burns push and grain; more motion competes
   with the type, and motion is another agent's scope. Low.
5. **Illustration.** Would need its own consistency system and contradicts the
   photoreal dark aesthetic the design system is built on. Low.
6. **Real screen recordings of banking apps.** Highest information density and
   superficially the most attractive option for a finance channel — and it should be
   **ranked last**. It is a direct collision with the pipeline's single most-repeated
   defect: "**Never a phone-screen photo as a background** — the screen is someone
   else's brand, and it's the brightest thing in frame," which has "shipped three
   times undetected." A recording is a *deliberate* version of that, adds real
   trademark exposure for a monetised channel, and risks leaking personal financial
   data. Do not.

---

## 7. What contradicts the vault (and the brief)

1. **`vault/CLAUDE.md`: archived `.src` prompts make a re-render reproducible.**
   False for every contact-sheet-sourced image — the picked cell index is never
   written (§3.2, reproduced). One live video's archive additionally holds a query
   that reproduces a frame-gate violation (§3.3).
2. **`vault/videos/good-debt-vs-bad-debt/index.md`: "escape only via `#N`."**
   `#N` is a no-op on the default contact-sheet path (§3.1, reproduced).
3. **`vault/knowledge/design-finance-blockframe.md:261`: "Key an asset ledger by
   md5."** No ledger exists in code; the manual substitute is blind to all five
   published pairs and gets blinder with each delivery (§2).
4. **`vault/knowledge/stock-photo-sourcing.md`: "For the finance format, object-led
   Pixabay has been sufficient."** Written 2026-07-27, before good-debt's 144 calls
   and 5-slot re-source and before credit-history's 75 fetches over 10 rounds. The
   frontmatter's own basis ("~35 fetches") is now roughly half of what one pair
   costs. It is stale.
5. **The same note's escalation clause — "generate the image per
   scene-image-prompt-rules"** — points at `[[scene-image-prompt-rules]]`, which
   **does not exist in the vault**. It is only a Claude Code memory file
   (`~/.claude/projects/…/memory/scene-image-prompt-rules.md`), i.e. not in the
   single source of truth the vault claims to be, and not readable by the fin-*
   agents that are told to read the vault. The generation escape hatch is
   undocumented in practice.
6. **The task brief says "The current source is Pixabay."** Pexels has already been
   a first-class provider since the contact-sheet rewrite — `@pexels` in the query
   string, `PEXELS_API_KEY`, `pexels_hits()`. The brief is a version behind.
7. **The task brief describes `.src` files as AI image prompts.** They are stock
   search queries (`us dollar bills#5`). No finance cut has ever used a generated
   image; that convention exists only on the history channel.
8. **The vault documents the demonetised pre-2016 ₹500 trap but not the ₹2000
   note**, withdrawn 2023-05-19 and 98.45% returned by 2026-03-31. A ₹2000 query
   reached a live cut's manifest and is preserved in its archive (§3.3).

---

## 8. Sources

- [YouTube: altered or synthetic content disclosure](https://support.google.com/youtube/answer/14328491)
- [YouTube auto-labelling AI video, May 2026 (TNW)](https://thenextweb.com/news/youtube-will-now-automatically-label-ai-generated-videos-whether-creators-disclose-them-or-not)
- [YouTube automatic AI labels: C2PA / SynthID detection](https://nerdleveltech.com/youtube-automatic-ai-labels-detection-c2pa)
- [YouTube inauthentic-content policy change](https://alternativeto.net/news/2025/7/youtube-updates-its-policy-to-demonetize-inauthentic-mass-produced-ai-generated-content)
- [YouTube repetitious/inauthentic content explained](https://www.advertisingbusiness.org/ai-or-authentic-youtubes-repetitious-content-policy-explained/)
- [January 2026 AI-channel terminations](https://milx.app/en/news/why-youtube-just-suspended-thousands-of-ai-channels-and-how-to-protect-yours)
- [Gemini API pricing breakdown, Jul 2026](https://developer.puter.com/tutorials/gemini-api-pricing/)
- [Gemini image generation per-image prices](https://www.aifreeapi.com/en/posts/gemini-image-generation-api-pricing)
- [Gemini image free tier limits 2026](https://www.aifreeapi.com/en/posts/gemini-image-generation-free-api)
- [Flux vs Ideogram vs Recraft, 2026](https://apiscout.dev/guides/flux-vs-ideogram-vs-recraft-image-gen-api-2026)
- [AI image API pricing, 12 providers](https://www.digitalapplied.com/blog/ai-image-generation-api-pricing-comparison-2026)
- [Nano Banana Pro review / benchmarks](https://designforonline.com/ai-models/google-nano-banana-pro-gemini-3-pro-image-preview/)
- [Nano Banana Pro full report](https://www.datastudios.org/post/nano-banana-pro-full-report-and-review-of-the-google-s-gemini-3-ai-image-generation-engine-compar)
- [Gemini output ownership & commercial rights](https://terms.law/ai-output-rights/gemini/)
- [Gemini images: commercial use](https://banana-clean.app/blog/gemini-images-copyright-commercial-use)
- [Pexels API documentation](https://www.pexels.com/api/documentation/)
- [Pexels: rules for using photos/videos](https://help.pexels.com/hc/en-us/articles/360042332714-What-are-the-rules-for-using-Pexels-photos-or-videos)
- [Unsplash API Terms](https://unsplash.com/api-terms)
- [Unsplash rate limits](https://help.unsplash.com/en/articles/3887917-when-should-i-apply-for-a-higher-rate-limit)
- [Pixabay Content License risk profile](https://picdefense.io/resources/source-intel/pixabay/)
- [Adobe Stock pricing](https://photutorial.com/adobe-stock-pricing/) · [Adobe vs Shutterstock 2026](https://josephnilo.com/blog/adobe-stock-vs-shutterstock/) · [Freepik pricing](https://photutorial.com/freepik-pricing/) · [Adobe Stock alternatives](https://photutorial.com/best-adobe-stock-alternatives/)
- [Adobe Stock API](https://developer.adobe.com/stock/docs/getting-started/) · [Shutterstock API](https://api-reference.shutterstock.com/)
- [RBI: ₹2000 withdrawal FAQ](https://www.rbi.org.in/commonman/english/scripts/FAQs.aspx?Id=3443) · [98.45% returned, Mar 2026](https://www.businessupturn.com/sectors/banking/rs-2000-banknote-withdrawal-98-45-returned-rs-5501-crore-still-out-as-of-march-2026/)
- [Central Bank Counterfeit Deterrence Group](https://rulesforuse.org/en/index.html)
