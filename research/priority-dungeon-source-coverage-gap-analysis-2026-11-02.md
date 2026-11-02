# Encounter source coverage gaps: 22 priority instances

Date: 2026-11-02. The first pass inspected the six-source ZIP; a follow-up located additional historical ScriptDev2 encounter scripts and adds `Lennix/scriptdev0` as a seventh source. **These are public reference implementations, not verified Conquest Reborn runtime scripts.**

## Why the previous coverage report undercounted

The database classified boss scripts only when the **filename** began with `boss_` and trash only when filenames contained `trash`, `mob_`, `npc_`, or `creature`. Most instance-wide scripts use names such as `wailing_caverns.cpp`, `razorfen_kraul.cpp`, and `sunken_templeScripts.cpp`. These were indexed as `shared` even where they define NPC AI. That is a **classifier limitation** for *shared creature AI*, but it does not prove that they contain dungeon boss or hostile trash combat AI.

The updated index records `creature_ai_source_candidate`, `boss_ai_source_candidate`, `nonboss_ai_source_candidate`, and symbol candidates separately. It deliberately does **not** upgrade escort/pet/quest NPC AI to trash combat AI.

## Boss-AI gaps and newly located references

| Instance | Exact source references found in collected archive | Evidence and disposition |
|---|---|---|
| Wailing Caverns | Existing TrinityCore/CMaNGOS event scripts, plus `Lennix/scriptdev0/scripts/kalimdor/wailing_caverns/boss_mutanus_the_devourer.cpp` | ScriptDev2 has individual Mutanus AI (NPC 3654), candidate spells 7967, 8150, 7399, and timer expressions. This closes the public-reference discovery gap for Mutanus; it remains a historical candidate, not confirmed Reborn behavior. |
| Razorfen Kraul | `TrinityCore/TrinityCore/src/server/scripts/Kalimdor/RazorfenKraul/razorfen_kraul.cpp`; `cmangos/mangos-wotlk/src/game/AI/ScriptDevAI/scripts/kalimdor/razorfen_kraul/razorfen_kraul.cpp`; `Conquest-of-AzerothCore/azerothcore-wotlk-coa/modules/mod-manastorm-endless/src/ManastormRazorfenKraulCompat.cpp` | Shared scripts include Snufflenose Gopher pet AI and Willix escort AI; the module is **Manastorm-specific**. A separate fork contains a Charlga script candidate, but its provenance and spell/creature references need validation, so it is not counted as a verified upstream reference. Charlga boss AI remains the unresolved public-source gap. |
| Sunken Temple | Existing TrinityCore/CMaNGOS event scripts, plus `Lennix/scriptdev0/scripts/eastern_kingdoms/sunken_temple/boss_jammalan_ogom.cpp` | ScriptDev2 includes candidate AI for Jammal'an the Prophet and Ogom the Wretched, spell IDs, timers, and instance-state signals. This closes the public-reference discovery gap for those two bosses; runtime behavior remains unverified. |

## Why trash coverage appeared as 2/22

The old field `trash_ai_explicitly_identified` is **filename-based only** and should never have been interpreted as complete trash coverage. The source archives contain NPC scripts in shared `.cpp` files, but many are escort, quest, pet, or event helpers. Classifying every `npc_` symbol as hostile trash would inflate coverage. The revised database reports separate nonboss/shared creature AI candidates and retains the original conservative filename count.

## Additional discovery: global CoA dungeon mechanics were omitted by the collector

The public CoA fork contains `src/server/coa/CoADungeonBossKit.cpp`, `src/server/coa/CoADungeonBossSpells.cpp`, and `src/server/coa/CoADungeonNormal.cpp`. These are **outside** the former `src/server/scripts/` path filter. For example, `data/sql/updates/pending_db_world/rev_20261002_40_wailing_caverns.sql` maps Skum's Overrun (spell 2102624) to `spell_coa_skum_overrun`, implemented in `CoADungeonBossSpells.cpp`. The generic kit SQL `data/sql/updates/pending_db_world/rev_20261001_10_boss_kits_scripted.sql` defines NPC/spell/timing rows for multiple dungeons.

**Disposition:** missing from collected source set because of the path filter (**category a**). Collector now includes the global dungeon C++ handlers and relevant global boss kit SQL, and the encounter database records them as **cross-instance sources**. They are not blindly assigned to a particular dungeon without NPC/SQL mapping. These source implementations are public reference candidates, not verified deployed Conquest Reborn behavior.

## Remaining evidence-based gaps

- Razorfen Kraul/Charlga remains without a sufficiently validated public boss-AI reference in the seven-source collection. This is a **source-coverage gap**, not a claim that live Conquest Reborn lacks the boss.
- A separate SQL SmartAI, EventAI, creature-template, and spell-script mapping pass is needed to attribute hostile trash abilities; filename and class-name heuristics alone are insufficient.
- Shared source paths, candidate NPC/spell IDs, and script-derived timing expressions do not establish actual deployed live mechanics.
- Blackrock Caverns five TrinityCore boss reference files are present, but remain unverified against the Conquest Reborn server.

## Reproduction

Run `tools/collect_coa_instance_scripts.py --priority-only --include-sql`, then `tools/build_encounter_database.py` and `tools/publish_encounter_coverage.py`. The collector includes the supplemental ScriptDev2 tree for Wailing Caverns and Sunken Temple. Inspect `datasets/instance-scripts/priority/coverage-report.json` for `shared_creature_ai_source_candidates` and `nonboss_ai_source_candidates`. Compare original `by_kind` counts to the new evidence fields. No metric should be treated as a live encounter verification.
