---
summary: Editable timeline of the v3 synced draft (pompeii-full-draft-v3-synced-1080p.mp4) — every segment's actual start/end as computed by build.py's VO relock. Creator marks corrections in the FIX column; build.py gets updated from those.
updated: 2026-07-17
source: generated from studio build.py (ClaudeHyperFrame/videos/pompeii-ka-akhri-din/build.py) — the EDL source of truth
---

# Pompeii — timeline v3 (mark your fixes here)

These are the REAL times in `pompeii-full-draft-v3-synced-1080p.mp4` (19:55.8).

**How to fix:** watch the draft, and wherever a visual is early/late vs the voice,
write the correct time in the **FIX → new start** column (video time where that
segment's visual should begin). Anything else (wrong scene order, hold longer,
etc.) — note it in the same cell in words. Send the file back and I'll re-lock
build.py to your times and re-render.

**Reading the times:**
- A segment's start = when its FIRST visual begins on screen.
- Dissolve transitions overlap 1.0s, so most segments fade in ~1s before the
  previous one ends — the ~1s overlap between rows is intentional, not an error.
- Chapter rows show which VO clip is playing; chapter starts are exact
  (audio and visuals locked within ±4ms there).

scenes: 104  ·  duration: 1195.75s  (~19:55.8)  ·  fps 30  ·  frames ~35872
## Segment timeline (the thing to fix)

| Seg | Starts at | Ends at | Dur (s) | Scenes | First visual | FIX → new start |
|---|---|---|---|---|---|---|
| **— CH1** (`pompeii-hook-01-07-v3.mp3`) | | | | | | |
| 01 | 0:00.0 | 0:07 | 7 | s00–s01 | S1-01A_bread-man-bakery | |
| 02 | 0:07 | 0:14 | 7 | s02–s03 | S1-02A_thermopolium-argument | |
| 03 | 0:14.5 | 0:25 | 11.5 | s04–s05 | S1-03A_horse-groomed | |
| 04 | 0:25.5 | 0:37 | 12.5 | s06–s07 | S1-04A_gladiator | |
| 05 | 0:37.5 | 0:48.5 | 12 | s08–s09 | S1-05A_street-ordinary | |
| 06 | 0:49.0 | 1:01.3 | 12.3 | s10–s10 | S1-06A_epic-establishing | |
| 07 | 1:01.5 | 1:31.2 | 29.7 | s11–s13 | C-07 | |
| **— CH2** (`pompeii-ch2-08-12-v3.mp3`) | | | | | | |
| 08 | 1:31.2 | 1:45.8 | 14.6 | s14–s14 | C-08 | |
| 09 | 1:44.8 | 1:57.8 | 13.0 | s15–s17 | S2-09A_harbour | |
| 10 | 1:56.8 | 2:12.6 | 20.8 | s18–s19 | S2-10A_vesuvius-over-city | |
| 11 | 2:12.6 | 2:32.5 | 17.9 | s20–s20 | S2-11A_vesuvius-single-cone | |
| 12 | 2:32.5 | 2:50.4 | 18.9 | s21–s22 | S2-12A_earthquake-repairs | |
| **— CH3** (`pompeii-ch3-13-18-v3.mp3`) | | | | | | |
| 13 | 2:50.4 | 2:57.6 | 7.2 | s23–s23 | S3-13A_street-waking | |
| 14 | 2:57.6 | 3:19.5 | 21.9 | s24–s26 | S3-14A_baker-oven | |
| 15 | 3:18.5 | 3:34.6 | 16.1 | s27–s28 | S3-15A_thermopolium-lively | |
| 16 | 3:33.6 | 3:56.6 | 23.0 | s29–s29 | S3-16A_wall-graffiti | |
| 17 | 3:55.6 | 4:09.8 | 14.2 | s30–s30 | S3-17A_school-boy | |
| 18 | 4:08.8 | 4:30.1 | 21.3 | s31–s32 | S3-18A_roman-baths | |
| **— CH4** (`pompeii-ch4-19-22-B-v3.mp3`) | | | | | | |
| 19 | 4:29.1 | 4:48.5 | 19.4 | s33–s35 | S3-19A_dry-well | |
| 20 | 4:47.5 | 5:06.3 | 18.8 | s36–s36 | S3-20A_street-vesuvius-refrain | |
| 21 | 5:05.3 | 5:18.2 | 12.9 | s37–s37 | S3-21A_street-bread-vesuvius | |
| 22 | 5:17.2 | 5:33.8 | 16.6 | s38–s38 | S3-22A_noon-street | |
| **— CH5** (`pompeii-ch5-23-30-B-v3.mp3`) | | | | | | |
| 23 | 5:33.8 | 5:39.1 | 5.3 | s39–s40 | S4-23A_blast-over-city | |
| 24 | 5:38.1 | 5:53.9 | 15.8 | s41–s41 | S4-24A_umbrella-column | |
| 25 | 5:52.9 | 6:12.8 | 19.9 | s42–s42 | S4-25A_pliny-terrace | |
| 26 | 6:11.8 | 6:30.4 | 18.6 | s43–s44 | EV-26A_pliny-letters-manuscript | |
| 27 | 6:29.4 | 6:47.6 | 18.2 | s45–s46 | S4-27A_ashfall-street | |
| 28 | 6:46.6 | 6:57.8 | 11.2 | s47–s47 | S4-28A_family-doorway | |
| 29 | 6:56.8 | 7:20.8 | 24.0 | s48–s49 | S4-29A_refugees-road | |
| 30 | 7:19.8 | 7:37.6 | 17.8 | s50–s50 | S4-30A_lamplit-home | |
| **— CH6** (`pompeii-ch6-31-39-B-v3.mp3`) | | | | | | |
| 31 | 7:36.6 | 7:52.3 | 12.7 | s51–s52 | S5-31A_street-buried | |
| 32 | 7:52.3 | 8:06.6 | 15.3 | s53–s53 | S5-32A_harbour-pumice | |
| 33 | 8:06.6 | 8:27.1 | 19.5 | s54–s54 | S5-33A_rescue-fleet | |
| 34 | 8:27.1 | 8:43.0 | 18.9 | s55–s55 | S5-34A_admiral-beach | |
| 35 | 8:43.0 | 8:55.1 | 16.1 | s56–s56 | S5-35A_roof-collapse | |
| 36 | 8:55.1 | 9:13.8 | 17.7 | s57–s57 | C-36 | |
| 37 | 9:13.8 | 9:41.6 | 28.8 | s58–s58 | S5-37A_pyroclastic-night | |
| 38 | 9:41.6 | 10:03.2 | 26.6 | s59–s61 | C-38 | |
| 39 | 10:03.2 | 10:19.7 | 15.5 | s62–s62 | EV-39A_herculaneum-skeletons | |
| **— CH7** (`pompeii-ch7-40-46-B-v3.mp3`) | | | | | | |
| 40 | 10:18.7 | 10:37.3 | 18.6 | s63–s64 | S6-40A_family-vigil | |
| 41+42 | 10:37.3 | 10:51.2 | 13.9 | s65–s65 | S6-41A_silent-buried-street | |
| 43 | 10:50.2 | 11:05.3 | 15.1 | s66–s67 | S6-43A_survivors-emerge | |
| 44 | 11:04.3 | 11:21.4 | 17.1 | s68–s68 | S6-44A_column-collapse | |
| 45 | 11:20.4 | 11:39.4 | 19.0 | s69–s69 | S6-45A_surge-crests-wall | |
| 46 | 11:39.4 | 12:03.5 | 24.1 | s70–s70 | S6-46A_grey-plain | |
| **— CH8** (`pompeii-ch8-47-53-B-v3.mp3`) | | | | | | |
| 47 | 12:02.5 | 12:20.5 | 16.0 | s71–s73 | S7-47A_shepherd-plain | |
| 48 | 12:20.5 | 12:41.9 | 18.4 | s74–s75 | S7-48A_excavation-1748 | |
| 49 | 12:41.9 | 12:52.1 | 14.2 | s76–s76 | EV-51A_garden-fugitives-casts | |
| 50 | 12:52.1 | 13:11.7 | 23.6 | s77–s77 | C-50 | |
| 51 | 13:10.7 | 13:31.1 | 16.4 | s78–s78 | EV-51A-boxer_man-covering-face | |
| 52 | 13:31.1 | 13:58.7 | 32.6 | s79–s80 | S1-03A_horse-groomed | |
| 53 | 13:57.7 | 14:18.9 | 21.2 | s81–s81 | S7-48A_excavation-1748 | |
| **— CH9** (`pompeii-ch9-54-61-B-v3.mp3`) | | | | | | |
| 54 | 14:19.9 | 14:36.4 | 15.5 | s82–s82 | EV-54A_regio-ix-blueroom-1 | |
| 55 | 14:36.4 | 14:55.8 | 24.4 | s83–s84 | S8-55A_regio-ix-room | |
| 56 | 14:55.8 | 15:06.8 | 11.0 | s85–s85 | EV-57A_golden-bracelet-child | |
| 57 | 15:06.8 | 15:24.5 | 17.7 | s86–s86 | C-57 | |
| 58 | 15:23.5 | 15:33.7 | 10.2 | s87–s87 | C-58 | |
| 59 | 15:32.7 | 16:01.1 | 28.4 | s88–s88 | EV-59A_carbonised-figs | |
| 60 | 16:00.1 | 16:25.0 | 24.9 | s89–s89 | EV-60A_charcoal-inscription | |
| 61 | 16:24.0 | 16:40.6 | 16.6 | s90–s90 | EV-61A_victim-skeleton | |
| **— CH10** (`pompeii-ch10-61a-65-B-v3.mp3`) | | | | | | |
| 61a | 16:39.6 | 17:16.7 | 37.1 | s91–s91 | S9-61a_lupanar-empty | |
| 61b | 17:15.7 | 17:47.2 | 31.5 | s92–s92 | C-61b | |
| 61c | 17:46.2 | 18:11.3 | 25.1 | s93–s93 | S9-61c_overturned-ruin | |
| 61d | 18:10.3 | 18:40.9 | 30.6 | s94–s94 | C-61d | |
| 62 | 18:39.9 | 18:52.2 | 12.3 | s95–s95 | S1-07B_golden-lane | |
| 63 | 18:51.2 | 19:07.6 | 16.4 | s96–s98 | S1-01A_bread-man-bakery | |
| 64 | 19:06.6 | 19:40.2 | 33.6 | s99–s102 | S1-04B_school-boy | |
| 65 | 19:39.2 | 19:55.8 | 16.6 | s103–s103 | C-65 | |

Total: **19:55.8**

## Scene-level detail

| Scene | Seg | Start | Dur (s) | Kind | Ref | Chip | Trans out |
|---|---|---|---|---|---|---|---|
| s00 | 01 | 0:00.0 | 5.2 | R | S1-01A_bread-man-bakery |  | NONE |
| s01 | 01 | 0:04.2 | 3.5 | R | S1-01B_bread-hands |  | XD |
| s02 | 02 | 0:06.8 | 7.0 | R | S1-02A_thermopolium-argument |  | XD |
| s03 | 02 | 0:12.8 | 5.5 | R | S1-02B_stew-ladle |  | XD |
| s04 | 03 | 0:17.3 | 8.1 | R | S1-03A_horse-groomed |  | XD |
| s05 | 03 | 0:24.3 | 5.7 | R | S1-03B_horse-head |  | XD |
| s06 | 04 | 0:29.1 | 7.2 | R | S1-04A_gladiator |  | XD |
| s07 | 04 | 0:35.2 | 7.2 | R | S1-04B_school-boy |  | XD |
| s08 | 05 | 0:41.4 | 5.8 | R | S1-05A_street-ordinary |  | XD |
| s09 | 05 | 0:46.2 | 6.8 | R | S1-05B_street-vesuvius-first |  | XD |
| s10 | 06 | 0:52.0 | 10.3 | R | S1-06A_epic-establishing |  | XD |
| s11 | 07 | 1:01.3 | 9.5 | C | C-07 | 6:00 AM | XD |
| s12 | 07 | 1:09.8 | 11.7 | R | S1-07A_fountain-corner |  | XD |
| s13 | 07 | 1:20.5 | 11.7 | R | S1-07B_golden-lane |  | XD |
| s14 | 08 | 1:31.2 | 14.7 | C | C-08 | HIDE | XD |
| s15 | 09 | 1:44.8 | 5.0 | R | S2-09A_harbour |  | XD |
| s16 | 09 | 1:48.8 | 5.0 | R | S2-09B_seaside-villas |  | XD |
| s17 | 09 | 1:52.8 | 5.0 | R | S2-09C_commercial-street |  | XD |
| s18 | 10 | 1:56.8 | 10.9 | R | S2-10A_vesuvius-over-city |  | XD |
| s19 | 10 | 2:06.7 | 10.9 | R | S2-10B_vineyards |  | XD |
| s20 | 11 | 2:16.6 | 17.9 | R | S2-11A_vesuvius-single-cone |  | XD |
| s21 | 12 | 2:33.5 | 10.9 | R | S2-12A_earthquake-repairs |  | XD |
| s22 | 12 | 2:43.4 | 8.9 | E | EV-12B_earthquake-relief |  | XD |
| s23 | 13 | 2:51.4 | 7.3 | R | S3-13A_street-waking | 6:00 AM | XD |
| s24 | 14 | 2:57.6 | 9.7 | R | S3-14A_baker-oven |  | XD |
| s25 | 14 | 3:06.3 | 6.2 | R | S3-14B_loaves-cooling |  | XD |
| s26 | 14 | 3:11.5 | 7.9 | E | EV-14C_carbonised-bread |  | XD |
| s27 | 15 | 3:18.5 | 9.6 | R | S3-15A_thermopolium-lively | 7:00 AM | XD |
| s28 | 15 | 3:27.1 | 7.5 | R | S3-15B_thermopolium-counter |  | XD |
| s29 | 16 | 3:33.6 | 23.0 | R | S3-16A_wall-graffiti |  | XD |
| s30 | 17 | 3:55.6 | 14.2 | R | S3-17A_school-boy | 8:00 AM | XD |
| s31 | 18 | 4:08.8 | 11.2 | R | S3-18A_roman-baths | 9:00 AM | XD |
| s32 | 18 | 4:18.9 | 11.2 | R | S3-18B_amphitheatre | 10:00 AM | XD |
| s33 | 19 | 4:29.1 | 7.7 | R | S3-19A_dry-well |  | XD |
| s34 | 19 | 4:35.8 | 7.7 | R | S3-19B_horse-uneasy |  | XD |
| s35 | 19 | 4:42.5 | 6.0 | R | S3-19C_cracked-fresco |  | XD |
| s36 | 20 | 4:47.5 | 18.8 | R | S3-20A_street-vesuvius-refrain |  | XD |
| s37 | 21 | 5:05.3 | 13.0 | R | S3-21A_street-bread-vesuvius |  | XD |
| s38 | 22 | 5:17.2 | 16.6 | R | S3-22A_noon-street | 12:00 PM | XD |
| s39 | 23 | 5:33.8 | 2.9 | R | S4-23A_blast-over-city |  | BLK |
| s40 | 23 | 5:36.7 | 2.4 | R | S4-23B_summit-blast |  | CUT |
| s41 | 24 | 5:38.1 | 15.7 | R | S4-24A_umbrella-column |  | XD |
| s42 | 25 | 5:52.9 | 19.9 | R | S4-25A_pliny-terrace |  | XD |
| s43 | 26 | 6:11.8 | 12.8 | E | EV-26A_pliny-letters-manuscript |  | XD |
| s44 | 26 | 6:23.5 | 6.9 | R | S4-26B_pliny-writing |  | XD |
| s45 | 27 | 6:29.4 | 12.5 | R | S4-27A_ashfall-street |  | XD |
| s46 | 27 | 6:40.9 | 6.7 | R | S4-27B_pumice-hand |  | EMB |
| s47 | 28 | 6:46.6 | 11.2 | R | S4-28A_family-doorway |  | XD |
| s48 | 29 | 6:56.8 | 12.5 | R | S4-29A_refugees-road |  | XD |
| s49 | 29 | 7:08.3 | 12.5 | R | S4-29B_barring-door |  | XD |
| s50 | 30 | 7:19.8 | 17.8 | R | S4-30A_lamplit-home |  | XD |
| s51 | 31 | 7:36.6 | 8.4 | R | S5-31A_street-buried | ['2:00 PM', '3:00 PM', '4:00 PM'] | XD |
| s52 | 31 | 7:44.0 | 5.2 | R | S5-31B_door-blocked |  | XD |
| s53 | 32 | 7:48.3 | 15.3 | R | S5-32A_harbour-pumice |  | XD |
| s54 | 33 | 8:02.6 | 19.6 | R | S5-33A_rescue-fleet |  | XD |
| s55 | 34 | 8:21.1 | 18.9 | R | S5-34A_admiral-beach |  | XD |
| s56 | 35 | 8:39.0 | 16.1 | R | S5-35A_roof-collapse | 7:00 PM | XD |
| s57 | 36 | 8:54.1 | 17.7 | C | C-36 |  | XD |
| s58 | 37 | 9:10.8 | 28.8 | R | S5-37A_pyroclastic-night |  | XD |
| s59 | 38 | 9:38.6 | 7.8 | C | C-38 |  | EMB |
| s60 | 38 | 9:45.5 | 11.2 | R | S5-38A_boathouses-night |  | XD |
| s61 | 38 | 9:55.7 | 9.5 | E | EV-38B_herculaneum-boathouses |  | XD |
| s62 | 39 | 10:04.2 | 15.5 | E | EV-39A_herculaneum-skeletons |  | XD |
| s63 | 40 | 10:18.7 | 11.6 | R | S6-40A_family-vigil | 3:00 AM | XD |
| s64 | 40 | 10:29.3 | 8.0 | R | S6-40B_wall-night-surge |  | XD |
| s65 | 41+42 | 10:37.3 | 13.9 | R | S6-41A_silent-buried-street |  | BLK |
| s66 | 43 | 10:50.2 | 10.0 | R | S6-43A_survivors-emerge | 6:30 AM | XD |
| s67 | 43 | 10:59.2 | 6.1 | R | S6-43B_child-shoulders |  | XD |
| s68 | 44 | 11:04.3 | 17.0 | R | S6-44A_column-collapse |  | XD |
| s69 | 45 | 11:20.4 | 19.0 | R | S6-45A_surge-crests-wall |  | XD |
| s70 | 46 | 11:39.4 | 24.1 | R | S6-46A_grey-plain |  | WHITE |
| s71 | 47 | 12:02.5 | 6.0 | R | S7-47A_shepherd-plain | HIDE | XD |
| s72 | 47 | 12:07.5 | 6.0 | R | S7-47B_medieval-farmers |  | XD |
| s73 | 47 | 12:12.5 | 6.0 | R | S7-47C_1600s-farmers |  | XD |
| s74 | 48 | 12:17.5 | 11.2 | R | S7-48A_excavation-1748 |  | XD |
| s75 | 48 | 12:27.7 | 8.3 | E | EV-48B_villa-misteri-fresco |  | XD |
| s76 | 49 | 12:34.9 | 14.2 | E | EV-51A_garden-fugitives-casts |  | XD |
| s77 | 50 | 12:48.1 | 23.6 | C | C-50 |  | XD |
| s78 | 51 | 13:10.7 | 16.4 | E | EV-51A-boxer_man-covering-face |  | XD |
| s79 | 52 | 13:26.1 | 16.8 | R | S1-03A_horse-groomed |  | XD |
| s80 | 52 | 13:41.9 | 16.8 | E | EV-52B_horse-cast |  | XD |
| s81 | 53 | 13:57.7 | 21.2 | R | S7-48A_excavation-1748 |  | XD |
| s82 | 54 | 14:17.9 | 15.5 | E | EV-54A_regio-ix-blueroom-1 | AUG 2024 | XD |
| s83 | 55 | 14:32.4 | 16.6 | R | S8-55A_regio-ix-room |  | XD |
| s84 | 55 | 14:48.0 | 8.8 | R | S8-55B_hand-key |  | XD |
| s85 | 56 | 14:55.8 | 11.0 | E | EV-57A_golden-bracelet-child | NOV 2024 | XD |
| s86 | 57 | 15:06.8 | 17.7 | C | C-57 |  | BLK |
| s87 | 58 | 15:23.5 | 10.2 | C | C-58 |  | XD |
| s88 | 59 | 15:32.7 | 28.4 | E | EV-59A_carbonised-figs |  | XD |
| s89 | 60 | 16:00.1 | 24.9 | E | EV-60A_charcoal-inscription |  | XD |
| s90 | 61 | 16:24.0 | 16.6 | E | EV-61A_victim-skeleton | APR 2026 | XD |
| s91 | 61a | 16:39.6 | 37.1 | R | S9-61a_lupanar-empty | HIDE | XD |
| s92 | 61b | 17:15.7 | 31.5 | C | C-61b |  | XD |
| s93 | 61c | 17:46.2 | 25.1 | R | S9-61c_overturned-ruin |  | XD |
| s94 | 61d | 18:10.3 | 30.7 | C | C-61d |  | XD |
| s95 | 62 | 18:39.9 | 12.3 | R | S1-07B_golden-lane |  | XD |
| s96 | 63 | 18:51.2 | 6.1 | R | S1-01A_bread-man-bakery |  | XD |
| s97 | 63 | 18:56.3 | 6.1 | R | S1-02A_thermopolium-argument |  | XD |
| s98 | 63 | 19:01.5 | 6.1 | R | S1-04A_gladiator |  | XD |
| s99 | 64 | 19:06.6 | 4.4 | R | S1-04B_school-boy |  | XD |
| s100 | 64 | 19:10.0 | 4.4 | R | S1-03A_horse-groomed |  | XD |
| s101 | 64 | 19:13.5 | 13.9 | E | EV-52B_horse-cast |  | XD |
| s102 | 64 | 19:26.3 | 13.9 | R | S1-03A_horse-groomed |  | XD |
| s103 | 65 | 19:39.2 | 16.6 | C | C-65 |  | XD |
