# Priority dungeons + Zul'Gurub: public-source audit

Date: 2026-11-02. Source: [Conquest-of-AzerothCore/azerothcore-wotlk-coa](https://github.com/Conquest-of-AzerothCore/azerothcore-wotlk-coa). Paths below were returned by repository code search, not downloaded as a complete archive. **No live Conquest Reborn verification.** SQL examples are *not* necessarily deployed on the live realm. Manastorm files are an alternative gameplay mode and should not be conflated with default boss AI.

| Instance | Search-confirmed primary file (relative to `src/server/scripts/`) | Additional lead | Status |
|---|---|---|---|
| Ragefire Chasm | `Kalimdor/RagefireChasm/instance_ragefire_chasm.cpp` | `data/sql/updates/pending_db_world/rev_20260930_80_rfc_bosses.sql` | Source path found, full AI not audited |
| Wailing Caverns | `Kalimdor/WailingCaverns/instance_wailing_caverns.cpp` | `data/sql/updates/pending_db_world/rev_20261019_21_wailing_caverns_disciple_wing_gossip.sql` | Source path found, full AI not audited |
| The Deadmines | `EasternKingdoms/Deadmines/instance_deadmines.cpp` | `data/sql/updates/pending_db_world/rev_20260930_70_deadmines_bosses.sql` | Source path found, full AI not audited |
| Shadowfang Keep | `EasternKingdoms/ShadowfangKeep/instance_shadowfang_keep.cpp` | `data/sql/updates/pending_db_world/rev_20261009_80_shadowfang_ashcrombe_unattackable.sql` | Source path found, full AI not audited |
| Blackfathom Deeps | `Kalimdor/BlackfathomDeeps/instance_blackfathom_deeps.cpp` | `modules/mod-manastorm-endless/data/sql/db-world/base/119_manastorm_blackfathom_deeps_akumai.sql` | Source path found, full AI not audited |
| The Stockade | `EasternKingdoms/TheStockade/instance_the_stockade.cpp` | `data/sql/updates/pending_db_world/rev_20261002_30_stockade.sql` | Source path found, full AI not audited |
| Gnomeregan | `EasternKingdoms/Gnomeregan/instance_gnomeregan.cpp` | `data/sql/updates/pending_db_world/rev_20261002_10_gnomeregan_bombs.sql` | Source path found, full AI not audited |
| Razorfen Kraul | `Kalimdor/RazorfenKraul/instance_razorfen_kraul.cpp` | `modules/mod-manastorm-endless/data/sql/db-world/base/89_manastorm_razorfen_kraul_charlga_razorflank.sql` | Source path found, full AI not audited |
| Scarlet Monastery | `EasternKingdoms/ScarletMonastery/instance_scarlet_monastery.cpp` | `data/sql/updates/pending_db_world/rev_20261019_20_scarlet_monastery_graveyard_rares_normal.sql` | Source path found, full AI not audited |
| Razorfen Downs | `Kalimdor/RazorfenDowns/instance_razorfen_downs.cpp` | `modules/mod-manastorm-endless/data/sql/db-world/base/123_manastorm_razorfen_downs_amnennar_the_coldbringer.sql` | Source path found, full AI not audited |
| Uldaman | `EasternKingdoms/Uldaman/instance_uldaman.cpp` | `modules/mod-manastorm-endless/data/sql/db-world/base/128_manastorm_uldaman_archaedas.sql` | Source path found, full AI not audited |
| Zul'Farrak | `NOT FOUND IN FIRST RESULTS` | `modules/mod-manastorm-endless/src/ManastormZulFarrakCompat.cpp` | Unresolved primary script |
| Maraudon | `Kalimdor/Maraudon/instance_maraudon.cpp` | `data/sql/updates/pending_db_world/rev_20261003_10_dm_maraudon.sql` | Source path found, full AI not audited |
| The Temple of Atal'Hakkar | `EasternKingdoms/SunkenTemple/instance_sunken_temple.cpp` | `data/sql/updates/pending_db_world/rev_20261024_43_sunken_temple_hallway_trash.sql` | Source path found, full AI not audited |
| Blackrock Depths | `EasternKingdoms/BlackrockMountain/BlackrockDepths/instance_blackrock_depths.cpp` | `modules/mod-manastorm-endless/data/sql/db-world/base/150_manastorm_blackrock_depths_magmus.sql` | Source path found, full AI not audited |
| Lower Blackrock Spire | `EasternKingdoms/BlackrockMountain/BlackrockSpire/instance_blackrock_spire.cpp` | `boss_highlord_omokk.cpp` | Source path found, full AI not audited |
| Upper Blackrock Spire | `EasternKingdoms/BlackrockMountain/BlackrockSpire/instance_blackrock_spire.cpp` | `boss_drakkisath.cpp` | Source path found, full AI not audited |
| Dire Maul | `Kalimdor/DireMaul/dire_maul.h` | `data/sql/updates/pending_db_world/rev_20261009_83_dire_maul_west_fixes.sql` | Source path found, full AI not audited |
| Scholomance | `EasternKingdoms/Scholomance/instance_scholomance.cpp` | `boss_darkmaster_gandling.cpp` | Source path found, full AI not audited |
| Stratholme | `EasternKingdoms/Stratholme/instance_stratholme.cpp` | `data/sql/updates/pending_db_world/rev_20261008_20_stratholme_dathrohan.sql` | Source path found, full AI not audited |
| Blackrock Caverns | `NOT FOUND IN FIRST RESULTS` | `modules/mod-coa-mythic-plus/src/MythicPlus.cpp (mention only)` | Unresolved primary script |
| Zul'Gurub (raid) | `EasternKingdoms/ZulGurub/instance_zulgurub.cpp` | `modules/mod-coa-raid-difficulty/data/sql/db-world/base/14_zg.sql` | Source path found, full AI not audited |

## Priority findings

- Zul'Gurub has Ascension-specific boss AI in `modules/mod-coa-raid-difficulty/src/`, and SQL mappings in `modules/mod-coa-raid-difficulty/data/sql/db-world/base/14_zg.sql`. See `research/zg-coa-verified-source-map.md`.
- Blackrock Caverns is **in scope** because the maintainer confirms it is released. Searches found references but **not its actual encounter AI**. Do not mislabel Blackrock Depths or Blackrock Spire as Caverns.
- Stock dungeon script directories, CoA modules, and SQL updates must all be indexed, with provenance and revision recorded.
- A file found in public source is not proof that the live server uses it. Do not assert timings without confirming the script or a combat log.

## Next verification requirements

1. Complete the automated source archive and record its source commit hashes.
2. Generate per-instance manifest, boss/trash AI mapping and spell/event ID cross-reference from the archived files.
3. Resolve missing primary script locations for Blackrock Caverns and Zul'Farrak, including module and SQL references.
4. Verify whether the GitHub Actions workflow completed and produced downloadable artifacts.
