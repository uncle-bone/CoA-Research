# CoA-Research — level-60 class stat discovery and migration comparison

**Research date:** 2026-11-05  
**Maintainer:** Uncle Bone  
**Scope:** Conquest Reborn / Conquest of Azeroth **research only**. No server or addon changes.

## Executive result

- **21/21 supplied class rows** preserved with all seven before/after fields in [machine-readable reference](../../datasets/normalized/coa-proposed-class-level60-stats-2026-11-05.json).
- **21/21 proposed after rows match the upstream SQL migration exactly** across BaseHP, BaseMana, Strength, Agility, Stamina, Intellect and Spirit.
- **210/210 race/class proposal rows** (10 race IDs × 21 classes) transcribed from the SQL, with class IDs and level 60 retained.
- The upstream [PR #11062](https://github.com/Conquest-of-AzerothCore/azerothcore-wotlk-coa/pull/11062) is **merged**, but its [server config](https://github.com/Conquest-of-AzerothCore/azerothcore-wotlk-coa/blob/main/src/server/coa/conf/coa.conf.dist) specifies `CoA.ClassLevelSixtyStats.Enable = 0` by default. **Nothing here proves CR's production realm has enabled this migration.**
- The upstream [SQL](https://github.com/Conquest-of-AzerothCore/azerothcore-wotlk-coa/blob/main/data/sql/updates/pending_db_world/rev_20261105_95_coa_class_level_sixty_stats.sql) explicitly describes the level-60 BaseHP and Stamina targets as **already adjusted ×1.2**. **Do not multiply these “after” rows again.**
- User-provided “before” values represent a **local `coa_world.player_class_stats`**, not measured CR live-client values. The report's “after” values are **migration targets**, not confirmed CR live stats.
- The attributed raw `coa.bisbeard.com` / `realmDataCoa` `coa-text` source rows **were not independently retrieved**. Neither their precise pre-scaling values nor rounding rules can be validated from this document.

## Source provenance

| Evidence | Origin | Confidence / limits |
|---|---|---|
| Before/after 21-class table | User-supplied `message(1).txt`, SHA-256 `473086208e9873a291934163a43243396c12e32d48657dab39df867d60efc397` | High confidence **as a transcription of this document**; “before” is not live CR |
| Proposed after values | Upstream SQL `rev_20261105_95_coa_class_level_sixty_stats.sql`; GitHub blob `63ade658315236f3038353f9849e25a7a67ba726` | Exact match across 21 rows; proposed server implementation |
| Race/class level-60 targets | Same upstream SQL `_coa_level_sixty_race_class` values | Exact 210 rows; not verified as live player attributes |
| Bisbeard original | Upstream PR / SQL attribution to `coa.bisbeard.com` / `realmDataCoa`, `coa-text` | **Attributed only**; original unscaled values not independently established |
| Active CR class names | `datasets/normalized/coa-conquest-reborn-character-creation-2026-10-30.json` | 21 class names from CR screenshots; no numeric level-60 stat observations |
| Historical class IDs / internal aliases | `datasets/normalized/coa-class-spec-id-registry.json` and `coa-custom-class-roster.json` | All class IDs 12–32 matched; internal aliases are intentionally distinct |
| Historical BisBeard gear snapshots | `datasets/gear/bisbeard-coverage.json` | Gear planner item records **not** class-base-stat records |

## Preserved original comparison (Human, level 60, no race offset)

`B → A` denotes **document-reported local coa_world before → proposed migration target after**. These are not a live realm benchmark.

| Class (ID) | Base HP | Base mana | Strength | Agility | Stamina | Intellect | Spirit |
|---|---|---|---|---|---|---|---|
| Barbarian (`12`) | 1572 → 3752 | 0 → 0 | 86 → 99 | 133 → 98 | 78 → 90 | 29 → 51 | 48 → 67 |
| Witch Doctor (`13`) | 1448 → 3128 | 1497 → 1538 | 79 → 54 | 57 → 82 | 97 → 86 | 90 → 79 | 106 → 106 |
| Felsworn (`14`) | 1563 → 3440 | 0 → 0 | 82 → 68 | 130 → 93 | 79 → 93 | 34 → 75 | 49 → 78 |
| Witch Hunter (`15`) | 1486 → 3440 | 1720 → 2064 | 55 → 75 | 127 → 94 | 93 → 91 | 64 → 71 | 69 → 75 |
| Stormbringer (`16`) | 1448 → 2925 | 1535 → 1456 | 79 → 55 | 50 → 57 | 93 → 73 | 101 → 119 | 106 → 103 |
| Knight of Xoroth (`17`) | 1734 → 4220 | 0 → 0 | 128 → 117 | 81 → 69 | 116 → 99 | 28 → 66 | 37 → 55 |
| Guardian (`18`) | 1734 → 3752 | 0 → 0 | 124 → 99 | 80 → 76 | 118 → 112 | 26 → 59 | 41 → 62 |
| Templar (`19`) | 1563 → 4220 | 0 → 0 | 81 → 83 | 132 → 92 | 79 → 96 | 32 → 63 | 49 → 72 |
| Bloodmage (`20`) | 1504 → 3385 | 0 → 0 | 63 → 71 | 60 → 75 | 78 → 102 | 98 → 73 | 111 → 87 |
| Ranger (`21`) | 1486 → 2972 | 0 → 0 | 61 → 80 | 130 → 110 | 94 → 91 | 62 → 65 | 64 → 60 |
| Chronomancer (`22`) | 1410 → 3307 | 1376 → 1651 | 33 → 54 | 35 → 61 | 49 → 74 | 125 → 105 | 132 → 115 |
| Necromancer (`23`) | 1456 → 3463 | 1373 → 1648 | 44 → 69 | 43 → 50 | 68 → 91 | 117 → 109 | 117 → 91 |
| Pyromancer (`24`) | 1403 → 2956 | 1213 → 1456 | 24 → 51 | 32 → 63 | 45 → 78 | 131 → 109 | 127 → 108 |
| Cultist (`25`) | 1418 → 3502 | 1512 → 1814 | 108 → 92 | 63 → 66 | 104 → 99 | 71 → 78 | 73 → 72 |
| Starcaller (`26`) | 1512 → 3151 | 1269 → 1824 | 71 → 82 | 56 → 71 | 75 → 92 | 105 → 104 | 102 → 57 |
| Sun Cleric (`27`) | 1410 → 3463 | 1363 → 1814 | 40 → 94 | 35 → 55 | 56 → 97 | 119 → 80 | 125 → 84 |
| Tinker (`28`) | 1486 → 3229 | 1740 → 1824 | 59 → 74 | 126 → 94 | 92 → 87 | 68 → 91 | 64 → 59 |
| Venomancer (`29`) | 1456 → 2995 | 1520 → 1824 | 85 → 63 | 53 → 78 | 98 → 86 | 93 → 91 | 100 → 90 |
| Reaper (`30`) | 1554 → 4196 | 0 → 0 | 84 → 95 | 126 → 70 | 80 → 100 | 33 → 67 | 50 → 76 |
| Primalist (`31`) | 1504 → 3697 | 1269 → 1824 | 73 → 89 | 57 → 73 | 75 → 90 | 100 → 86 | 105 → 67 |
| Runemaster (`32`) | 1448 → 2917 | 1480 → 1361 | 80 → 60 | 59 → 88 | 98 → 87 | 95 → 96 | 98 → 75 |

## 1.2× scaling — confirmed scope and unresolved raw values

The upstream migration's SQL comment says Stamina and BaseHP were multiplied by 1.2 **when constructing the target table**. It then inserts fixed final numbers into `_coa_level_sixty_class` and `_coa_level_sixty_race_class`, and computes the remaining class/race curves through levels 2–80. For example, its proposed **Human Barbarian** target is **3752 BaseHP and 90 Stamina**, while its proposed **Orc Barbarian** five attributes are **106 / 101 / 98 / 47 / 60**. Those values include the upstream author's scaling decision.

**Do not interpret `after / before` as the scaling factor.** “Before” comes from a different local donor/fallback curve, not the unscaled Bisbeard target. In the document, Barbarian BaseHP changes from 1572 to 3752 (≈2.3868×), and Stamina from 78 to 90 (≈1.1538×). Both are compatible with a new Bisbeard target followed by a separate 1.2 multiplier. Reversing rounded results with division by 1.2 would produce only rough *inferences*, not proven original Bisbeard records; therefore the raw unscaled data is `null` in the reference dataset.

## Quantitative discrepancies **within the two documented configurations**

- All 21 classes have increased **proposed BaseHP** relative to the supplied local-world baseline, with ratios from **2.000× (Ranger)** to **2.700× (Reaper)**.
- **11** classes have higher proposed Stamina and **10** lower proposed Stamina. Decreases: Witch Doctor (-11), Witch Hunter (-2), Stormbringer (-20), Knight of Xoroth (-17), Guardian (-6), Ranger (-3), Cultist (-5), Tinker (-5), Venomancer (-12), Runemaster (-11).
- **2** classes have lower proposed BaseMana: Stormbringer (-79), Runemaster (-119).
- **8 zero-mana classes** remain at BaseMana 0 in both document columns; the other 13 classes have nonzero proposed BaseMana.
- The original document notes an **Undead Necromancer level-60 health** example, 1956 → 4213. This is a separate full-character health illustration; **do not substitute it for the class BaseHP row** (1456 → 3463), or treat it as an independently observed CR live-client value.

These are **differences between two historical/proposed data configurations**, not demonstrated nerfs/buffs on Conquest Reborn.

## Cross-check against CoA-Research

- **21/21 IDs and class names** reconcile with the archived specialization registry and the CR character-creation names; zero class identity conflicts were found using those display names.
- The internal roster additionally uses **seven intentional aliases**, rather than user-visible display names: Witch Doctor = `WitchDoctor` (class 13); Felsworn = `DemonHunter` (class 14); Witch Hunter = `WitchHunter` (class 15); Knight of Xoroth = `KnightOfXoroth` (class 17); Templar = `Monk` (class 19); Bloodmage = `SonOfArugal` (class 20); Sun Cleric = `SunCleric` (class 27). These are **not data errors**.
- `coa-conquest-reborn-character-creation-2026-10-30.json` supports class-level resource/role descriptions but contains **no level-60 health, mana or five-attribute measurements** for numeric comparison.
- `bisbeard-coverage.json` covers a separately sourced gear planner, **not** raw class level-60 attribute rows. No Bisbeard-source numerical cross-confirmation is claimed.
- **Numeric live-client comparison count: 0** from the reviewed records. Therefore “matches current CR live stats” remains **unknown**, rather than failed or passed.

## What the merged upstream change does (not a CR balance recommendation)

1. Leaves original `player_class_stats` intact; creates alternative `ascension_class_stats` and `ascension_race_class_stats` tables.
2. Does not change level 1; the alternate level 2–59 curve interpolates a donor class's progression to the alternate level-60 target.
3. For levels 61–80, preserves donor **incremental gains** above 60, relative to the new level-60 baseline; final absolute stats at those levels can therefore differ.
4. Maintains base mana zero for classes without mana.
5. Uses per-race/class adjusted attributes for the 10 enumerated race IDs (1, 2, 3, 4, 5, 6, 7, 8, 10, 11).
6. Documents a Necromancer minion-health preservation mechanism; it is **not** evidence of live CR minion health measurements.
7. Reads `CoA.ClassLevelSixtyStats.Enable` at server startup; the public default is **0/off**. The pull request states its in-game check was **not done**, despite passing test-harness and scenario checks on the project's development environment.

See [upstream PR](https://github.com/Conquest-of-AzerothCore/azerothcore-wotlk-coa/pull/11062), [SQL migration](https://github.com/Conquest-of-AzerothCore/azerothcore-wotlk-coa/blob/main/data/sql/updates/pending_db_world/rev_20261105_95_coa_class_level_sixty_stats.sql), [test harness](https://github.com/Conquest-of-AzerothCore/azerothcore-wotlk-coa/blob/main/apps/test-framework/test_class_level_sixty_stats.py), and [config](https://github.com/Conquest-of-AzerothCore/azerothcore-wotlk-coa/blob/main/src/server/coa/conf/coa.conf.dist).

## Outstanding verification questions

1. Can an authorized public snapshot of `realmDataCoa` / `coa-text` be recovered to establish **unscaled** values and its rounding and per-race semantics?
2. Does the **production CR realm** use the migration's optional tables or an unrelated/custom stats implementation? The public config default does not establish deployed configuration.
3. Which actual level-60 naked-character **health, mana and primary attributes** are observed in the CR client for each class/race with known talents, buffs, passives and gear excluded? Collect source, build, realm, screenshot/log timestamp, and modifiers to compare like-for-like.
4. Do level-1 and level-61–80 interpolation results in a running realm match the documented donor/fallback curve? Requires server-side data access or controlled test fixture, not client assumption.
5. Do Necromancer minion-health preservation and race modifiers behave as expected in an **authorized running realm**?
6. Do any of the 21-class recorded values represent server BaseHP versus displayed character-sheet maximum HP with additional stamina? These must be compared using the correct definitions.

## Research-only guardrails

**No SQL applied, no server config changed, no balance patch, no addon modified, and no claim that CR adopted the migration.** This finding is a candidate stats-reference snapshot for future CR research and rotation/theorycraft caveats, not a new gameplay baseline.
