# fin-assets · japanese-money-methods · en · chapters 3–5 · attempt 3

Targeted re-source of chapters 3, 4, 5 only, against the three editor logs
(`editor-en-ch3-2.md`, `editor-en-ch4-2.md`, `editor-en-ch5-2.md`).
Fetched only rows whose fix says `source new`. Every `reuse hi:`-only row was
left untouched (file copies are the caller's).

Manifest: `studio/videos/japanese-money-methods-en/assets/img/manifest-fix-345.json`
(`manifest-fix.json` already existed — another agent has ch1–2 — and was not touched).
No existing `sN.jpg` was overwritten; every new file is `<slot>-fix.jpg`.

## Landed — 15 files, all read at FULL resolution before acceptance

| slot | file | what it is | note |
|---|---|---|---|
| s24 | `s24-fix.jpg` | corridor of shut lockboxes, receding, cold ceiling light | not literally steel; reads "hundreds of locked boxes", kills the plastic-padlock/gym read |
| s25 **and** s26 | `s25-fix.jpg` | printed *Consolidated Statements of Functional Expenses*, two year-columns (2018 / 2017), dark wood desk | one file, two framings — the 2018/2017 pair IS "same table, next column". ⚠ small angled header reads "FIND AID FOR THE AGED, INC." — keep the s25 wide framing off the top-left |
| s27 | `s27-fix.jpg` | five clip-top glass jars of rice/buckwheat/peas/oats, dark slate | no dipper, no flower, no text, dark ground |
| s28 | `s28-fix.jpg` | Higashi Chaya, Kanazawa — aged wooden machiya street, red lanterns | see "s28 compromise" below |
| s34 | `s34-fix.jpg` | kintsugi bowl, gold lacquer repair seams, 4400 px | Commons, CC0 (Daderot). Object is a 16thC Korean buncheong tea bowl repaired *in the Japanese kintsugi manner* — the technique is right, the provenance is Korean; invisible on screen, flagged for honesty |
| s36b | `s36b-fix.jpg` | spinning frame, receding row of yarn packages, no faces | the missing MILL link in the s36 chain |
| s38 | `s38-fix.jpg` | blank white swing tag with twine on linen, hard shadow | see "s38 trade" below |
| s39 | `s39-fix.jpg` | hands on a phone in a dark room, screen turned away | see "s39 trade" below |
| s40 | `s40-fix.jpg` | used lidded takeout containers, disposable glasses, dark table | no person, no brand; "this all goes in the bin" |
| s41 | `s41-fix.jpg` | five taped, sealed cardboard boxes on a shelf | optional (editor note-level). ⚠ white brick wall — bright; take it or leave it |
| s42 | `s42-fix.jpg` | hand lifting a boxed cake off a chilled retail shelf | ⚠ Cyrillic price tags at right/bottom edges — frame left-of-centre |
| s44 | `s44-fix.jpg` | checkout belt mid-transaction, vegetables, red basket | live purchase, not a derelict cart; keypad in frame is generic/unbranded |
| s50 | `s50-fix.jpg` | kraft envelope with a folded stack of $50s, dark grey ground | one serial only (no prop-money repeat); empty space right/bottom for the ten-cell art |
| s53 | `s53-fix.jpg` | laptop glowing in a very dark room, city bokeh, mug | a screen with no brand and no card — the editor's SVG carries "separation + recurrence" |
| s56 | `s56-fix.jpg` | single folded US bill on a pale desk, lots of empty space | see "s56 trade" below |

md5 dedupe: hashed all 262 images across the `-en` and `-hi` master dirs; **zero
collisions** involving any `-fix` file. (The per-chapter dirs mirror the master
dir, so a naive `studio/videos/*/assets/img/*.jpg` sweep reports every file 9×
and is useless — restrict to the two master dirs.)

CREDITS.txt: verified — one line for each of the 15.

Resolution: every Pexels pick lands at ~1880 px (`dpr=2&w=940`); s34 (Commons)
is 4400 px. All clear the ≥1600 px zoom bar.

## Compromises the caller must know about

**s28 — no archival Showa street exists in reach.** Eight Commons query rounds
(`postwar Tokyo 1950s`, `Ginza 1946`, `Shōwa era Japan street`, `Tokyo commuters
1960s`, `Japanese village 1950s`, …). The enwiki file search is not era-aware:
era words returned either modern colour Tokyo, WWII firebombing aerials, imperial
family portraits, or (for "Japan 1955 photograph people") Abraham Lincoln and
Ansel Adams. Two real candidates were fetched and **rejected at full res**:
- `Ginza, Tokyo, 1971` — correct era, but SONY / 三菱電機 / 森永 / Mazda neon
  everywhere and portrait 1817×2754.
- an "old Japanese street" first pick — empty and timeless, but carrying a **German
  flag and a "GERMAN RESTAURANT" sign**, i.e. the wrong-country defect this fix
  exists to remove.

What landed instead is Japanese architecture rather than a Japanese *date*: a
Kanazawa machiya street. It fixes the blocker (the frame no longer asserts
Europe) and is unmistakably old-fashioned Japan. Costs: present-day tourists
mid-frame (small, faces not legible) and it is colour, not b/w. **Desaturate and
lift the grade**, and push the ken framing to the left/upper wooden facades to
keep the modern figures out. If that is not good enough, the editor's fallback
(`reuse hi:.../hi-ch3/assets/img/s28.jpg`) still stands and is a file copy.

**s38 — the tag or the clothes, not both.** Three query rounds. Everything with
garments *and* a legible tag carried a defect: a "ROUTINE / DIVIDE 78 MENSWEAR"
brand tag, or a Turkish tag reading `Taksitli Fiyat 122,21₺ / Peşin Fiyat 109,99₺`
(wrong currency, in a $ cut — rejected on sight at full res). What landed makes
the *tag* the subject with zero text risk, but it is one tag on cloth, not "two
or three garments". The editor's alternative — tighten the ken framing onto the
tag on the existing `s38.jpg` closet — is still the cleaner fix if you want
garments. Both are now available; your call.

**s39 — every legible phone screen was a defect.** The contact-sheet cell that
read as a "settings list" turned out at full res to be an **"All countries"
picker** (Albania, Argentina, Australia… with flags) — a textbook grid-size miss.
The rest of the pool: PayPal, Cash App, NatWest, Apple Wallet, a bank fraud-alert
notification, a crypto portfolio. Script 4.6 itself asks for "screen text
illegible, hand only", so what landed is hands + phone in the dark with the screen
turned away: no brand, no wrong content, doesn't contradict. It also does not
fully *assert* "the subscriptions screen" — let the on-screen type carry that.

**s56 — the contrast pair does not exist.** "One $20 beside a much thicker
folded stack" returned nothing on either pool across four queries; what came back
was abundance shots, mixed denominations, or **prop money** (`MB77999921K`
repeated across every note in two separate photos, and the `LB45440078L` family
again). Landed frame is a single folded bill alone in a large empty field —
"start smaller" by composition rather than by comparison. Denomination is not
legible, so no friction with the $200 on screen.

**s25/s26 is deliberately ONE file.** Two framings of one document is the literal
claim the scene makes ("SAME TABLE, NEXT COLUMN"), not an image repeat. Point
both scenes at `s25-fix.jpg`.

## What the contact sheets missed (all caught by the full-res read)
Six picks were promoted, viewed at full resolution, and thrown away: the
"SALES VOLUME DURING THE WEEK" chart and an options-pricing printout on s25;
a Ginza neon wall of brand marks and a German flag on s28; a "ROUTINE" brand tag
and a Turkish-lira price tag on s38; an "All countries" picker on s39; a
"GRAB & GO"-labelled deli case on s40; a "Mia" bottle wall on s42; an Italian
supermarket with euro shelf-edge prices on s44. Not one of those was legible at
contact-sheet size. The rule holds: the grid picks the candidate, the full-res
read decides.

## Not touched (out of scope, as instructed)
All `reuse hi:`-only rows — ch3 #4 s31, #8 s23; ch4 #4 s45, #6 s37, #12 s35;
ch5 #2 s52, #3 s55, #8 s48, #9 s49, #10 s57, #11 s58. Also every Lottie/SVG,
markup, timing and framing finding (ch3 #5/#6, ch4 #11/#14, ch5 #6/#7), and
ch5 #13 s51 (marked optional).
