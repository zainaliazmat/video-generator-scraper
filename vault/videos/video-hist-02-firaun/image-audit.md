---
summary: Gate ③ vision audit of the 141 generated scene stills for «فرعون کا انجام» (2026-07-19). Files renamed to scene IDs, 3 byte-dupes quarantined, 8 scenes missing, 6 depiction violations found. This note is the re-generation worklist.
updated: 2026-07-19
source: Claude vision pass over studio/videos/firaun-ka-anjaam/assets/images/ vs [[image-prompts]] + [[DESIGN]] §DEPICTION
---

# IMAGE AUDIT — فرعون کا انجام (Gate ③)

**Method:** 9 parallel chapter agents, each viewing only its own scenes, checked against the
prompt text + [[DESIGN]] §DEPICTION (binding), §era grades, §Realism rules, and Ken Burns safety.

## Reconciliation (exact)
| | |
|---|---|
| prompts | 143 |
| files generated | 141 |
| − byte-identical duplicates | −3 → 138 unique |
| − alternate takes (P14a, P34b, P38c) | −3 → **135 scenes covered** |
| **missing** | **8** |

⚠️ **The initial "5 missing" estimate was wrong** — it assumed every unique file covered a new
scene. Three files are second takes of a scene that already had one, so the real gap is 8.
Lesson: reconcile by *scene coverage*, never by file count.

## Filing convention (applied 2026-07-19)
Files are now named by scene ID: `P16c2.jpeg`. Second takes of the same scene: `P16c2-alt1.jpeg`.
Byte-identical extras moved to `assets/images/_dupes/` — **nothing deleted**, creator to review.
Undo script exists at the session scratchpad (`undo-rename.sh`) until the creator confirms.

Dupes quarantined: `Ancient_Egypt_village_flooded_storm_…0454` (=P26a) ·
`Shaft_mouth_in_rock_face_…0455` (=P42b) · `War_crown_falling_underwater_…0458` (=P38b).

## ❌ DEPICTION VIOLATIONS — regenerate before edit (6)
| Scene | Fault |
|---|---|
| **P10c** | Glow is an offset hard-edged blob — mother's hair/brow/face-edge visible left of it, infant's head/ear/cheek right of it |
| **P14a-alt1** | A woman's face (eyes, nose, lips) readable **inside** the glow. Discard take; P14a proper is compliant |
| **P16d2** | Glow semi-transparent — eyes, nose, mouth readable through it |
| **P16e1** | Old man of Madyan given a glow he is **not cleared for** (creator confirmation still open in [[DESIGN]]) + head in frame vs the hands-only directive + modern Gulf ghutra/agal/thobe and machine-woven rug |
| **P16c2** | Glow rendered as an offset lens-flare rather than a veil; jaw/cheek contour may read |
| **P19c** | **Fired-brick error recurred** — tower is pale grey sun-dried mudbrick, no kilns, no smoke (face lock itself is correct) |

### What passed — the rules that held
- **Tuwa is clean.** P16g1/P16h1/P16h2 contain fire, tree, light and rock only — zero figure,
  zero form. The no-divine-depiction rule survived generation intact.
- **P35c and P36e glows are textbook** — featureless veil, no halo ring, no rays.
- **The صندوق correction held 100%:** every P11–P13 frame shows a plank-built pitch-sealed wooden
  chest. Not one reed basket. The 2026-07-19 fact-row rewrite worked.
- P19a/P19b/P19d are correctly fired brick — only P19c regressed, so the fix was ~75% effective.

## ⚠️ QUALITY — nice to fix
- **Anachronism:** P16f2 modern black jacket w/ ribbed knit cuff · P38b crown is medieval/fantasy
  not the khepresh · P41c collar is Sutton-Hoo cloisonné not Egyptian inlay · P16c3 camels ·
  P12a metal corner brackets
- **Legible text (breaks the no-text rule):** P46c licence plate "1932 1559" · P45b ship name on
  hull · P50b Mercedes badge + number plates
- **Era-grade mismatch:** **P46b is in COLOUR but must be 1976 B&W** · P42a neutral daylight,
  breaking its own sepia match-cut with P42b · P07b near-monochrome · P37b cold storm vs warm morning
- **Face leakage on ordinary characters** (permitted, but weakens the "anonymous labour" read):
  P06b, P07a, P07c, P19b, P34a, P36c, P33b
- **Ken Burns unsafe:** P45a (head 7% from top) · P50c · P16f3 · P03d
- **Baked-in bars — crop before animating:** P30a, P35b, P11b letterboxed · P37b pillarboxed
- **Prop continuity:** the staff drifts — straight in P16b1/P16d2, a hooked crook in P16d1/P17b;
  absent in P16b3. [[DESIGN]] §Realism rule 2 names the staff as a lock-prop; it did not hold.

## FIRAUN FACE LOCK — verdict
| Scene | Status |
|---|---|
| P31a | ✅ **cleanest reference** — ~50, clean-shaven, striped nemes + cobra |
| P41b | ✅ intact, calm, eyes closed, no decay (shoreline exception honoured); skin reads pale European, not bronzed |
| P08a | ⚠️ **drifts** — long striped false beard vs "clean-shaven", rounder softer face, CGI look |
| P19c | ✅ face matches (but the scene fails on brick) |
| P08b, P31c | ⚠️ king rendered too small/soft to verify |
| P38a | ❌ **never generated** |
Until P38a exists the sinking↔shoreline continuity cannot be checked — the two beats the
match depends on. Regenerate P38a against P31a, not P08a.

## MISSING — 8 scenes, no image
`P13b` · `P20c` · `P20d` · `P22a` · `P22b` · `P38a` · `P41a` · `P50a`

⚠️ **P20c + P20d + P22a + P22b is the entire swallow-and-sujood beat** (segs 20–22) — the
chapter's scripted pattern interrupt and the «silence frame» have **zero coverage**. Highest
re-generation priority; the edit cannot carry seg 20-21 without them.
`P38a` = the drowning close-up (face-lock scene). `P41a` = shoreline wide. `P50a` = museum
thesis wide. `P13b` = the chest alone on the palace steps.

Prompts for all 8 are already in [[image-prompts]] — paste verbatim, they are one-shot ready.
