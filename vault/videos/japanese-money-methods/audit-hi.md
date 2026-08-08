---
summary: Gate-one adversarial audit of script-hi.md for japanese-money-methods (LONG, hi). Every load-bearing number re-fetched from its recorded source; three violations fixed by direct edit, one borderline tightened. Verdict PASS after edits.
updated: 2026-08-01
source: Re-fetched primaries — Horioka NBER WP 33181, Statistics Bureau FIES 2024 summary, BOJ Flow of Funds overview (all read as PDF, not via search index); Fujin no Tomo Sha publisher page; DEA small-savings notification Q2 FY2026-27; AMFI Chhoti SIP; Wikipedia Tsukubai.
stage: fin-audit, cut hi, attempt 1
---

# audit-hi — japanese-money-methods

PASS

Passing **after four direct edits**. The script as submitted would have failed checks 3
and 1. Downstream voice work must re-run against the edited file — the VO strings for
**1.2, 3.8, 3.9 and 6.14** have changed and the pipeline hash-checks this.

---

## 1. Independence re-fetch — every load-bearing number

`facts-staging.md` was written by this same run, so nothing below was graded against the
claim text. Each figure was confirmed inside the fetched source itself. The three primary
PDFs returned raw binary through the fetch tool and were read directly as PDFs instead —
so these are the actual documents, not a search-index rendering of them.

| Figure | Script line | Re-fetched source | Verdict |
|---|---|---|---|
| **37.8%** FIES surplus rate | 2.3, 2.5 | FIES 2024 summary **p.11**: 黒字率 **37.8**; independently Horioka **p.7** "37.8 percent according to the Family Income and Expenditure Survey" | ✅ two independent, one is the issuing agency |
| **about 1%** SNA rate | 2.6 | Horioka **p.2**: "The most recently available figure is for 2024, when it was a mere **1.1%**" | ✅ VO correctly says "क़रीब एक परसेंट" |
| **more than 30 times** | 2.7 | Horioka **p.7** verbatim: "is more than 30 times as high as the figure from the National Accounts!" | ✅ |
| Who each survey counts | 2.9 | Horioka **p.7** verbatim: "only for salaried worker households whereas the National Accounts include everyone including the self-employed, the unemployed, the retired, and private unincorporated enterprises" | ✅ |
| ¥636,155 · ¥522,569 · ¥325,137 · ¥197,432 | 2.5 foot | FIES **p.11** 表I-2-2, all four exact | ✅ stays in yen |
| **~90% deposits · ~3% securities** | 3.2 | FIES **p.11**: 預貯金純増 **175,241**, 有価証券純購入 **6,705**, 黒字 **197,432** → 88.8% / 3.4% | ✅ ratio is COMPUTED and the frame carries `ILLUSTRATIVE` |
| **51.0%** Japan cash · **11.5%** US cash · **41.5%** US equity | 3.4, 3.5 | BOJ Flow of Funds overview, **Chart 2** (p.3 of PDF), data as of **end-March 2025**, ¥2,195tn / $128.8tn | ✅ one table states both markets — not a cross-market conversion |
| **23.2%** mid-1970s peak | 3.9 | Horioka **p.2**: "peaked at 23.2%" | ✅ |
| **1961–1986** above 15% | 3.8 | Horioka **p.3** — **but only "if we confine ourselves to the postwar period"** | ⚠️ **KILLED AS WRITTEN — see §2** |
| never above 5% since 2002 | 3.9 | Horioka **p.2** — **"except for a temporary blip in 2020 due to the Covid-19 pandemic"** | ⚠️ **KILLED AS WRITTEN — see §2** |
| Culture not a major determinant | 3.10, 3.11 | Horioka **p.3 §3** verbatim: "culture, tradition, and national character are not a major determinant of Japan's household saving rate"; drivers in §9–10 | ✅ premise correction holds |
| **62.2%** avg propensity to consume | 5.7 | FIES **p.11**: 平均消費性向 **62.2%** | ✅ Japan's own figure, uncompared |
| **₹500 / ₹250** SIP minimum | 5.10 | AMFI/SEBI Chhoti SIP — ₹500 conventional minimum, ₹250 Chhoti SIP | ✅ price evidence, no platform named |
| **7.1%** PPF | 6.14 | DEA notification, rates unchanged for **Jul–Sep 2026 (Q2 FY27)**, announced 30 Jun 2026 | ✅ number good — **framing rewritten, see §2** |
| **1904** · Hani Motoko · 4 wartime years · budget-first | 6.2, 6.3, 6.5, 6.6 | Fujin no Tomo Sha publisher primary: "『羽仁もと子案家計簿』が初めて発行されたのは、明治37（1904）年末"; "戦中戦後の4年間は紙の統制により発行できませんでした"; 年間の予算を立てて | ✅ and the script correctly never says "121 years" |
| Ryōan-ji tsukubai · four characters · shared 口 | 7.2–7.5 | Tsukubai article: each character "is read in combination with 口 (kuchi), the shape of the central bowl" → 吾唯足知 | ✅ Mitsukuni donor attribution correctly NOT used |
| ₹30,000 → ₹6,000 (20%) · ₹24,000 · ₹1,500 (5%) | 2.11, 4.11, 5.5, 5.9 | Channel convention, arithmetic re-checked | ✅ all four correct and labelled on screen |

**Nothing was untraceable.** No number in the script lacked a staging line, and no staging
line collapsed under re-fetch — but two *sentences* asserted more than their cited page
supports. Those are §2.

---

## 2. What was killed or rewritten, and why

### 2.1 — 1.2 rewritten · **check 3, the 15-second promise gate** · the reason this was not a pass

The submitted cut carried **no payoff promise until line 2.1 at 0:54**. Inside the first
fifteen seconds the viewer got rent, a power bill and nothing else. The script argued this
from study conclusion 1 ("TOP spends 40s before its first promise"). **A competitor's
retention curve does not override a gate.** This was the single largest defect in the file
and it was deliberate, which is worse than an oversight.

- was: `फ़ोन पर वो नोटिफिकेशन देखकर दो सेकंड अच्छा लगता है।` (50 ch)
- now: `फ़ोन पर वो नोटिफिकेशन दो सेकंड अच्छा लगता है — और बाक़ी महीने के लिए जापान के तीन तरीक़े हैं।` (~94 ch)

Promise clause opens ≈7.9s, closes ≈11.6s. Chapter 1 still carries **zero statistics** and
stays entirely in second person, so the pain-mirror survives intact; only the roadmap moved.
2.1 now reads as the expansion of a promise already made, which is stronger structure anyway.

### 2.2 — 3.8 rewritten · **check 1, source does not back the claim**

- was: "**सिर्फ़** उन्नीस सौ इकसठ से छियासी तक …" — *only* 1961–1986 was the rate above 15%.
- Horioka **p.3** actually says: "**if we confine ourselves to the postwar period**, the only
  period during which Japan's household saving rate exceeded 15% was the 25-year period from
  1961 until 1986."
- Horioka **p.2** says the rate "reached **44%** in the waning years of the Second World War."

The unqualified sentence is therefore **false against its own citation**. `facts-staging.md`
J6 dropped the qualifier and the script inherited the drop — exactly the failure mode the
independence rule exists to catch. Fixed by prefixing **युद्ध के बाद** and rewriting the
screen `foot:` to name the postwar restriction and the wartime forced-saving context.

### 2.3 — 3.9 softened · **check 1, source does not back the claim**

- was: "दो हज़ार दो के बाद **कभी** पाँच परसेंट से ऊपर **नहीं** गई" — *never* above 5% since 2002.
- Horioka **p.2**: "has been no higher than 5% during the past two decades (since 2002)
  **except for a temporary blip in 2020 due to the Covid-19 pandemic**."

An absolute the source explicitly carves an exception out of. Softened to **शायद ही कभी**
("hardly ever") and the Covid exception added to the `foot:`. Kept short deliberately —
the full caveat in VO would have pushed the line past the 105-char scene ceiling.

### 2.4 — 6.14 rewritten · **checks 4 and 7, monetisation gate**

- was: "और **जिस हिस्से को सबसे पहले अलग रखा जाता है**, उस पर आज पी-पी-एफ़ में सात दशमलव एक परसेंट सालाना मिलता है।"

The number is fine and re-verified. The *sentence* routed the kakeibo set-aside into a named
scheme — that is a placement recommendation regardless of a `foot:` reading "price evidence,
not a recommendation". A disclaimer under a recommendation is still a recommendation.

- now: `पैसा कहाँ रखा जाए यह इस वीडियो का विषय नहीं, पर आज पी-पी-एफ़ की दर सात दशमलव एक परसेंट सालाना है।`

The rate now stands as scale, the VO disclaims placement out loud, and the `head:` changed
from `THE SET-ASIDE BUCKET` to `TODAY'S RATE, FOR SCALE`. 5.10 was checked the same way and
needed no change — it was already neutrally worded.

---

## 3. Checks that passed without edit

2. **Char budget.** `(660 − 92 × 0.8) × 13.03 = 7,640`. Draft 7,544 (−1.3%); post-edit
   **7,598 (−0.5%)**. Inside ±10% both ways. Budget formula is the corrected one that takes
   padding out of the target *before* applying the rate — the `cuts.en._chars_per_second_trap`
   is not repeated here.
5. **Currency purity.** Zero `$` in the file (grep, whole file, including claim IDs and
   comments). ₹ present as required. No ¥ glyph anywhere — yen written `JPY 197,432`, which
   also dodges the 97-codepoint font subset.
6. **TTS silent-killers.** No `(28:4)`-style cite refs. **No bare Latin digit in any VO
   line** — every figure spelled out in Devanagari (सैंतीस दशमलव आठ, इक्यावन, बासठ, तेईस).
   Verified by grep across all `> ` lines.
7. **Persona.** No `मैं` / `हम` / `हमारा` / `मुझे` anywhere in VO (grep). No host persona,
   no first-person expertise, no fund/stock/AMC/app/bank named. After §2.4, no scheme is
   recommended either.
8. **Layout lints.** One focal element per scene — no scene carries both `stmt:` and `num:`
   (all 92 cues checked). Three cues per scene (head/stmt-or-num/foot) inside 4.4–8.3s scenes
   clears `cue_min_gap_seconds` 0.8 and `first_cue_by_seconds` 0.5 with room. No scene exceeds
   `max_scene_seconds` 9.0 post-edit (longest 103 ch → 8.7s). Colour table does **not** argue
   against the thesis: `--warn` sits on leaks and on numbers used wrongly, `--fund` on
   behaviour that works, `--target` on figures under examination; 3.12 — "the methods work,
   they were never the reason" — is `--fund`, which is thesis-consistent.

Also verified and correct: no Japan-vs-India / Japan-vs-US saving-rate comparison anywhere,
spoken or adjacent (India's 7.0%/34.2% are used nowhere at all); no ¥→₹ conversion; no number
attached to mottainai, hara hachi bu or taru wo shiru; the four kakeibo pillars explicitly
**not** attributed to Hani Motoko (6.7, 6.8).

---

## 4. Two things the build stage must not get wrong (not script defects)

1. **Extraction hazard.** The warning box above `# THE SCRIPT` is a `>` blockquote and
   contains English text and Latin digits. A naive `^> ` slicer would sweep it into the VO
   set. Extraction must key off the `**N.N**` markers and land exactly **92** entries
   `1.1…8.8`; the byte-for-byte reconstruction gate in build handoff §1 will catch it if not.
2. **`·`-separated statements are not chip rows.** 3.11 (five items) and 6.10 (four items)
   would breach `max_chips_per_row` 3 and, at 6.10, `max_chip_chars` 22 **if built as chips**.
   They are `stmt:` strings at 44px and must render as wrapped statement lines, per the
   ledger-rail two-type-sizes rule. Do not promote them to chips.
