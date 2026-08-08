# fin-assets — japanese-money-methods / en / attempt 5 — single slot: s39-fix.jpg

(Logged under `fin-assets-s39-5.md`, not `fin-assets-en-5.md`, because that filename
already holds an unrelated 2026-08-01 run. Same precedent as `fin-assets-s65-4.md`.)

Scene s39 line: **"The subscriptions screen. All of it."** — middle of the three-checks
sequence. Prior file was a hand + phone in near-darkness, screen edge-on and unlit,
mean luminance 32.7 against 110–171 for the chapter. CEO rejected it.

Manifest: `assets/img/manifest-fix-s39.json` (new file; `manifest.json` and the other
`manifest-fix*.json` untouched).

## Accepted

`s39-fix.jpg` — Pixabay, page `photos/business-smartphone-hands-7304257/`, IqbalStock,
Pixabay Content License. Query `subscription payment plan smartphone`, cell 1.
1280×853, **mean luminance 107.8** (was 32.7). md5 `6b86a134…` — unique across all
`studio/videos/*/assets/img/*.jpg` (the eight `-ch*` hits are symlinks to this same
`img/` dir, not copies).

Two hands hold a phone upright, screen lit and square to camera, warm defocused
interior behind. The screen shows a dark-blue app with **~10 stacked rows**, each row
a label on the left, a tiny sparkline in the middle and a figure on the right. Nothing
on it is legible at full resolution — no app name, no logo, no OS chrome, no currency
symbol, no readable figures. No face. Hands and phone are an object in a scene, not a
full-bleed screenshot.

Honest caveat for the record: the underlying app is a markets watchlist, so the rows
carry sparklines. They are illegible and read as line items, but this is a *rows-list*
photo, not literally a subscriptions settings screen — after 14 contact sheets neither
pool has the latter without brands. Also 1280 px, below the 1600 px zoom guidance;
the Pexels 1880 px path was tried repeatedly and returned nothing usable.

## Rejected — 14 sheets, ~78 cells, why

| Query | Verdict |
|---|---|
| `smartphone screen showing bank transaction list on wooden table@pexels` | 4/6 one lock-screen series with a legible "My Bank" fraud alert + AT&T carrier mark; rest a distant social feed and an article wall |
| same `#7` | Deutsche Bank + VISA card, a €10 note, dark screens |
| `hand holding smartphone showing mobile banking app transactions list screen@pexels` | WhatsApp/Facebook icons, a legible "Make Paying Easier With Wallet." mockup, "Super Internet eCommerce Market", a BLOCKCHAIN logo, two faces |
| `personal finance budget app smartphone screen list of expenses on desk@pexels` | six calculator apps; cell 6 also rubles |
| `smartphone screen showing app list of payments` (pixabay) | the known Facebook + Scrabble shot, GPS, home screens |
| `close up smartphone screen app interface rows of text list on desk@pexels` | sheet came back **1 of 6** (previews failed); that one cell a code editor |
| `smartphone lying on table screen showing settings menu list close up@pexels` | brand icon grids, an OpenAI page, a Russian Samsung settings list (OS chrome + wrong language) |
| `smartphone screen showing digital invoice with list of items and prices on table@pexels` | promoted cell 5, **killed at full res**: the phone is showing pexels.com itself (legible URL bar, photo grid not a list) plus a Canon lens with legible "IMAGE STABILIZER NANO USM" |
| same `#7` | 3/6 tiled, all calculators/dark |
| `expense tracker app on smartphone screen showing list of transactions@pexels` | best-structured cell was a crypto marketplace (Ethereum/Tether/Binance Coin, € amounts) — refused on the consistency rule; promoted cell 2 instead and **killed at full res**: a menstrual-cycle tracker with legible "Sex and Sex Drive" / "Vaginal Discharge" |
| `mobile banking app screen@pexels` | same recycled set as sheet 1 |
| `subscription payment plan smartphone` (pixabay) | **cell 1 accepted**; rest generic |
| `phone on desk screen showing list of monthly bills to pay@pexels` | six calculators again |
| `close up smartphone screen list of items with prices in hand@pexels` | promoted cell 4, **killed at full res**: Russian Google Play update list — Gmail, Google, Brave, Yandex, MTS, Mi Home logos all legible |
| same `#7` | crypto and calculators |
| `woman holding smartphone in cafe screen showing app list of rows blurred background@pexels` | six home screens, logo grids |

## What this run re-proves

1. **Full-resolution read is the whole defence.** Three separate picks passed the
   contact sheet and died only at full res — pexels.com's own URL bar, a
   menstrual-cycle tracker's intimate labels, and a Play Store list of logos. Each was
   an unreadable smudge at grid size.
2. **"Phone screen" queries are a brand minefield in both pools**, exactly as
   `stock-photo-sourcing.md` says. Roughly four in five cells across 14 sheets carried
   a legible brand, an OS chrome, a fabricated mockup brand, or a crypto prop.
3. **Naming the app category does not work the way naming a denomination does.**
   "subscriptions", "expense tracker", "bills", "invoice", "banking" all resolve to the
   same three stock clusters: calculator flatlays, crypto watchlists, and brand-logo
   home screens. Worth recording in the sourcing note if this recurs.
4. If s39 must be exact, the honest route is the third rung: **draw it** — a Lottie or
   a vector list of rows with blurred amounts. No photograph of a brand-free US
   subscriptions settings screen exists in either free pool.

CREDITS.txt line 129 carries the accepted image; no stale s39-fix lines (the tool
replaces rather than appends). `_cand/s39-fix.*` left in place as throwaway.
