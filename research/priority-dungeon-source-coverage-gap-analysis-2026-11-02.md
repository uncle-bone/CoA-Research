# Encounter source coverage gaps: 22 priority instances

Date: 2026-11-02. Evidence: inspected contents of the published six-source ZIP from the successful GitHub Actions collection. **These are public reference implementations, not verified Conquest Reborn runtime scripts.**

## Why the previous coverage report undercounted

The database classified boss scripts only when the **filename** began with `boss_` and trash only when filenames contained `trash`, `mob_`, `npc_`, or `creature`. Most instance-wide scripts use names such as `wailing_caverns.cpp`, `razorfen_kraul.cpp`, and `sunken_templeScripts.cpp`. These were indexed as `shared` even where they define NPC AI. That is a **classifier limitation** for *shared creature AI*, but it does not prove that they contain dungeon boss or hostile trash combat AI.

The updated index records `creature_ai_source_candidate`, `boss_ai_source_candidate`, `nonboss_ai_source_candidate`, and symbol candidates separately. It deliberately does **not** upgrade escort/pet/quest NPC AI to trash combat AI.

## The three boss-AI filename gaps

| Instance | Exact source references found in collected archive | Evidence and disposition |
|---|---|---|
| Wailing Caverns | `TrinityCore/TrinityCore/src/server/scripts/Kalimdor/WailingCaverns/wailing_caverns.cpp`; `cmangos/mangos-wotlk/src/game/AI/ScriptDevAI/scripts/kalimdor/wailing_caverns/wailing_cavernsScripts.cpp` | The TrinityCore file defines `npc_disciple_of_naralex` scripted AI. The CMaNGOS file defines `npc_disciple_of_naralexAI`, summons Mutanus (NPC 3654), and spawns deviate creatures. **Encounter event/support script found; individual Wailing Caverns boss combat AI still not found in these files.** |
| Razorfen Kraul | `TrinityCore/TrinityCore/src/server/scripts/Kalimdor/RazorfenKraul/razorfen_kraul.cpp`; `cmangos/mangos-wotlk/src/game/AI/ScriptDevAI/scripts/kalimdor/razorfen_kraul/razorfen_kraul.cpp`; `Conquest-of-AzerothCore/azerothcore-wotlk-coa/modules/mod-manastorm-endless/src/ManastormRazorfenKraulCompat.cpp` | Shared scripts include Snufflenose Gopher pet AI and Willix escort AI; the module is **Manastorm-specific**. **No Charlga or other boss combat AI implementation confirmed** in the collected reference set. |
| Sunken Temple | `TrinityCore/TrinityCore/src/server/scripts/EasternKingdoms/SunkenTemple/sunken_temple.cpp`; `cmangos/mangos-wotlk/src/game/AI/ScriptDevAI/scripts/eastern_kingdoms/sunken_temple/sunken_templeScripts.cpp`; `Conquest-of-AzerothCore/azerothcore-wotlk-coa/modules/mod-manastorm-endless/src/ManastormSunkenTempleCompat.cpp` | Shared scripts include Atal'ai statue gameobject AI, Malfurion NPC AI, avatar-of-Hakkar event, and associated spell/area-trigger handlers. **Boss combat AI remains unconfirmed** in these reference scripts. |

## Why trash coverage appeared as 2/22

The old field `trash_ai_explicitly_identified` is **filename-based only** and should never have been interpreted as complete trash coverage. The source archives contain NPC scripts in shared `.cpp` files, but many are escort, quest, pet, or event helpers. Classifying every `npc_` symbol as hostile trash would inflate coverage. The revised database reports separate nonboss/shared creature AI candidates and retains the original conservative filename count.

## Additional discovery: global CoA dungeon mechanics were omitted by the collector

The public CoA fork contains `src/server/coa/CoADungeonBossKit.cpp`, `src/server/coa/CoADungeonBossSpells.cpp`, and `src/server/coa/CoADungeonNormal.cpp`. These are **outside** the former `src/server/scripts/` path filter. For example, `data/sql/updates/pending_db_world/rev_20261002_40_wailing_caverns.sql` maps Skum's Overrun (spell 2102624) to `spell_coa_skum_overrun`, implemented in `CoADungeonBossSpells.cpp`. The generic kit SQL `data/sql/updates/pending_db_world/rev_20261001_10_boss_kits_scripted.sql` defines NPC/spell/timing rows for multiple dungeons.

**Disposition:** missing from collected source set because of the path filter (**category a**). Collector now includes the global dungeon C++ handlers and relevant global boss kit SQL, and the encounter database records them as **cross-instance sources**. They are not blindly assigned to a particular dungeon without NPC/SQL mapping. These source implementations are public reference candidates, not verified deployed Conquest Reborn behavior.

## Remaining evidence-based gaps

- Three instances still lack independently identified boss combat AI in the inspected six-source collection. This is a **source-coverage gap**, not a claim that live Conquest Reborn lacks those bosses.
- A separate SQL SmartAI, EventAI, creature-template, and spell-script mapping pass is needed to attribute hostile trash abilities; filename and class-name heuristics alone are insufficient.
- Shared source paths, candidate NPC/spell IDs, and script-derived timing expressions do not establish actual deployed live mechanics.
- Blackrock Caverns five TrinityCore boss reference files are present, but remain unverified against the Conquest Reborn server.

## Reproduction

Run `tools/collect_coa_instance_scripts.py --priority-only --include-sql`, then `tools/build_encounter_database.py` and `tools/publish_encounter_coverage.py`. Inspect `datasets/instance-scripts/priority/coverage-report.json` for `shared_creature_ai_source_candidates` and `nonboss_ai_source_candidates`. Compare original `by_kind` counts to the new evidence fields. No metric should be treated as a live encounter verification.
