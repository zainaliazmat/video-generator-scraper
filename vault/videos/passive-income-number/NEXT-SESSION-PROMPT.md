---
summary: Handover prompt for resuming the passive-income-number run in a fresh session (written 2026-08-08). Session file — delete once folded into the milestone note.
updated: 2026-08-08
source: this run's run.json, stage logs and chapter reviews.
---

Resume the `passive-income-number` finance video run. Read
`vault/videos/passive-income-number/run.json` first — it is the authoritative state,
and it carries the creator's `constraints`, the `style_decision`, both measured hook
gates, the budget and the per-chapter records.

## Where it stands

**English cut — ready to build.** Script (restyled, 81 lines), audit (PASS), voice
(81 clips on Brian, 527.873s) and storyboard (81 scenes, 84 image slots) are all
marked `done`. `studio/videos/passive-income-number-en/assets/cues-tables.json` is
written. **Nothing is built yet.** Next action: `fin-assets` on en chapter 1, then
the chapter loop (assets → build → `hyperframes check` → draft render + sheet →
`fin-editor` → `fin-ceo` → lock) for all 6 chapters.

**Hindi cut — needs re-doing from the script.** Its script/audit/voice/storyboard
are marked `superseded`, because the creator changed both the register (style E) and
the voice (Harsh → Amrut Deshmukh, already switched in `tools/format.json`). Chapters
1 and 2 are built but obsolete. **Their photographs survive and must be reused** —
every image in both chapters is verified and passes the new gates, and three of them
took multiple rounds to land. Only script, voice, timing and layout get redone.

## What style E is

Creator-approved after a listening test. Reference scripts, chapters 1-2 of each cut,
in `studio/voice-tests/passive-income-number/`:
`style-E-teacher-curiosity.txt` (hi) and `style-E-en-teacher-curiosity.txt` (en).

1. The cold open is a **what-if**, not a statement, and the phone's silence is the
   promise while its single buzz is the payoff.
2. **Signposted teaching** — «यहाँ ध्यान दीजिए» / "Notice this", "Think of it this
   way", "Now watch what it buys", "Work it through".
3. **A tank analogy that pays off later**: "how much can you draw each year without
   emptying it" IS the safe-withdrawal question, so the mid-video yield-trap beat
   becomes a callback rather than a new idea.
4. **Stepped arithmetic** — yearly, then monthly, then the division, each its own line.

It measurably worked: the en hook gate is **9.571s** against the hi cut's 14.9-15.1s.

## Non-negotiables (from run.json `constraints`)

Every corpus figure speaks its rate in the SAME line AND shares its frame · derived
income figures too (`WHAT ₹2,500 BUYS` needed the rate or an ILLUSTRATIVE marker) ·
no return promise · no corpus converted to an age · the word "dividend" is banned in
the **hi** cut only, and en line 1.7 uses it on purpose because it is the phrase the
format ranks on · currency purity per cut · no Latin digits in a VO line · no first
person · no rail (nothing on screen may reveal the video is chapter-based).

## The traps this run has already paid for

Read `vault/knowledge/stock-photo-sourcing.md` before any fetch. In short:

- **`YHIGH ≥ 110`** on the source, enforced by `pipeline_check check assets --chapter <N>`
  — highlight ceiling predicts survival under the locked grade, average brightness does
  not. Measure the CONTACT SHEET CELLS, not the promoted file; it is a pre-fetch filter.
- **mean `R−B ≥ ~+40`** for warmth. No per-scene grade override exists under the
  chapter archetype, so the photograph is the only variable.
- **A gate can only reject, never approve.** Two candidates once cleared both gates and
  were a `PAST DUE` shoot saying the opposite of the line.
- **When a slot fails twice on brightness, change the MATERIAL** — matte paper has no
  specular return; enamel, glass, glazed ceramic, polished metal do.
- Pass `--chapter <N>` to the assets check or it reads the wrong directory and reports
  green over nothing.

Six tooling defects were fixed today and all share one shape: **a check reporting green
over the thing it existed to catch.** Invalid JS leaving a scene blank · a cue generator
parsing the wrong `<script>` block · a licence assertion pointed at a directory that did
not exist · another video's cue holds hardcoded in a shared tool · a foot struck through
by a comma at 11/11 WCAG AA · a photograph satisfying `image_per_scene` by loading a
file. Trust the encoded frames over the source, always.

## Budget

**ElevenLabs 209 / 350.** The hi restyle needs a full ~81 (voice AND text changed).
**vidIQ 13 credits** against a ~35-credit close-out packaging pass, resetting 2026-08-29
— that decision is still open: ration it, defer the title lock, or run one market only.

## Owed

A real study packet (`study.py --ids JiuVKaO2a6c Jn3N9OzSY1c`) once yt-dlp cookies exist
— `YTAUTO_COOKIES` / `YTAUTO_COOKIES_BROWSER` were added to `study.py` today. The
current study was built from two bought vidIQ transcripts, so its visual half is
recorded MISSING, not faked.
