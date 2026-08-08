# fin-assets — japanese-money-methods / en / attempt 4

Single-slot job: replace scene s7's background so the drawn `calendar-20th-circled`
Lottie is not sitting on a photographed calendar (rule-8 depictive defect).
No other slot touched; `manifest.json` and the other `manifest-fix*.json` untouched.

## Manifest
`assets/img/manifest-fix-s7.json` → `{"s7-fix.jpg": "warm evening sunlight shaft across an empty room wall and floor@pexels"}`

## Sheets

**Sheet A** — `late afternoon sunlight shadow on empty kitchen wall@pexels`, 6/6 cells.
All six rejected:
- 1 — café interior, `Café` legible on the wall + posters (readable text).
- 2 — sunlit exterior/industrial wall, hanging canopy; no hour-of-day read as a room.
- 3 — kitchen sink with dishes and faucet, blazing window in the upper band
  (violates the "nothing bright upper-right" framing constraint; surface not empty).
- 4 — balcony with an empty chair (collides with s10's empty chair).
- 5 — dining table + chairs (same collision).
- 6 — chair, table, mug and thermos (same collision + objects on the surface).

**Sheet B** — the manifest query above. Tiled only **2 of 6** (the known lossy-sheet
failure); read `_cand/s7-fix.json` for the full six.
- 5 — dark derelict room, murky, no clear shaft. Reject.
- 6 — Kolmanskop sand-filled abandoned house. Wrong place, wrong story. Reject.
- 2 — "shadow of a window frame on the wood flooring of an empty room". Promoted.
- 3 — fetched separately to `_cand/` and read: institutional washroom, a row of
  taps on the wall, and the shaft enters from the **top right** — straight through
  the calendar's zone. Reject.

## Accepted

`s7-fix.jpg` — cell 2, Pexels, sanket mahind, 1880×991.
An empty room corner: pale grey plaster walls, dark wood plank floor, one hard low
shaft throwing a window-frame patch on the wall and across the boards. Nothing else
in frame.

Full-resolution read (not the sheet): no calendar, clock, date, planner; no phone,
laptop or monitor; no envelope, bill, receipt or paper; no money; no readable text
anywhere; no people; no chair, no table, no sink, no running water. Clean on both
the intra-chapter collisions (s9 water, s10 empty chair).

- Framing: the right third (x≈1140–1880, where the calendar Lottie lives) is
  uniform mid-grey wall — nothing bright or strong there. The lit wedge sits
  centre/lower-centre.
- Resolution 1880 px ≥ the 1600 px zoom floor (Pexels `dpr=2&w=940`).
- Mean luminance 122/255 — mid-grade. **No `filter:` override needed**; the video's
  one override budget stays unspent by this slot.
- md5 `f003a826b78dc033121bd4bc397acac2` — unique across all `studio/videos/*`.
  (It appears under `…-ch1..ch8/assets/img/`, but those paths are a **symlink** to
  this same dir — same inode, not a collision.)
- CREDITS.txt line 129 written by the tool.
- Prompt recorded at `assets/img/s7-fix.jpg.src`.

Counts: 1 accepted, 11 rejected across two sheets + 1 side-fetch. Nothing dropped.
