# Class/pet/summon ownership & DBM-CoA safe classification — first research milestone
Date: 2026-11-01. Client target: WoW 3.3.5a (Lua 5.1).

## Source inventory (repository main; 1,230 Git tree entries, not truncated)
- `datasets/catalog/`: 6 files including NPC, item, quest, spell and talent ID catalogs (gzipped).
- `datasets/collected/`: 5 files; selected captured creature/spell/quest examples, not comprehensive.
- `datasets/relationships/`: 15 pre-existing files including unified spell research index, enriched spells, talent nodes, quality reports. Existing `quality-report.json` documents 9,754 archived class ability edges, 3,618 talent nodes, 3,933 talent-spell edges; NOT verified current-game facts.
- `datasets/upstream/`: 12 files, including datamine class IDs/spec links and creature buckets.
- `datasets/bulk/`: upstream compressed spellbooks, creature buckets, ability tables, indexes. Bulk binaries have **not** been decompressed and exhaustively checked in this milestone.
- `research/local-client-extracts/2026-10-31/`: 89 files; Questie-X NPC JSONL among them. One class list there contains unresolved/null class IDs; prefer sourced datamine IDs while explicitly preserving archive status.
- `research/dbm/`: 120 files, primarily encounter research, not an authoritative current pet ownership matrix.
- `site/data/`: 39 files, including class and specialization presentation.
Existing datasets should be cross-joined, not replaced. Completeness and duplication remain unverified at record level.

## Class roster distinction
Archived `datasets/upstream/coa-datamine/data-classes-index.json` lists **21 custom classes** with IDs 12–32, alongside 11 standard/placeholder class records in `chrClasses`. This confirms archived custom-class enumeration, **not** present-day playable roster. Some internal filenames differ from display names (e.g. DEMONHUNTER/Felsworn, MONK/Templar, WILDWALKER/Primalist). Preserve both identifiers. Source `data-classes-specs.json` has class/spec identifiers and historical source labels, but specializations need current-runtime checking.

## Current verified extraction scope
See `datasets/relationships/class-pet-summon-investigation-v1.json` for 21 archived class IDs and 7 NPC + 4 spell user-reported candidates. Candidate names and IDs originate with user reports, **not a verified lookup against creature/spell indexes**. Zero authoritative summon ownership edges confirmed during this first pass. No exclusions or runtime addon changes are authorized by this dataset.

## 3.3.5a combat-log classification design (proposed, NOT game-tested)
WoW combat log exposes sourceGUID, sourceFlags, destGUID, destFlags and event payload. Use 3.3.5a direct varargs in the event handler (later clients changed API), and verify on the actual 3.3.5a client before deployment. Bitmask categories: AFFILIATION, REACTION, CONTROL, TYPE; constants include `COMBATLOG_OBJECT_AFFILIATION_MINE`, `_PARTY`, `_RAID`, `COMBATLOG_OBJECT_CONTROL_PLAYER`, `COMBATLOG_OBJECT_TYPE_PET`, `_GUARDIAN`, `_NPC`, `COMBATLOG_OBJECT_REACTION_HOSTILE`.
Source references:
- https://warcraft.wiki.gg/wiki/UnitFlag
- https://warcraft.wiki.gg/wiki/Patch_2.4.0/Consolidated_API_changes/Guide_to_the_New_Combat_Log
- https://warcraft.wiki.gg/wiki/API_COMBAT_LOG_EVENT_UNFILTERED (modern examples must not be copied unchanged to 3.3.5a).

Decision policy:
1. Check sourceFlags when present, not creature name or numeric NPC ID alone; a pet/guardian controlled by a player may have an NPC-like template ID.
2. If affiliation is MINE/PARTY/RAID and source is a player, pet, guardian, or player-controlled entity, label friendly-associated and **do not register as hostile dungeon mechanics**. Friendly reactions and player control strengthen evidence; retain anomalies for diagnostics.
3. For outsider player-controlled sources, exclude from hostile NPC learning when clearly player/pet/guardian. Do not universally exclude outsider-controlled guardians without checking flags and context.
4. For hostile, NPC-controlled source in an instance, label **candidate hostile encounter mechanic**, not automatically boss. Confirm map/instance, observed encounter association, boss roster, recurrence, and boss GUID. Hostile flags alone do not identify bosses.
5. On `SPELL_SUMMON`, associate source GUID -> summoned destination GUID in a time-bounded cache when event shape supports it; on `UNIT_DIED` remove with bounded TTL. Cross-check dynamic source flags and group GUIDs. GUIDs identify individual runtime instances, not stable universal ownership of a creature template.
6. For ambiguous flags, charm/mind-control changes, pets turned hostile, or missing GUIDs: quarantine with compact timestamps, map, sourceGUID, flags, spellId and reason; do not silently discard.
7. Never make the seven NPCs or four spells a universal blacklist. A single spell can be used by legitimate enemy NPCs and friendly summons.
8. Performance: avoid memory-heavy full-catalog loading; cache small GUID ownership maps only during combat, cap entries and retention, and batch/limit writes and network sharing. No per-event full-table scans.

### Suggested strict outcomes
- `player_friendly`, `player_owned_pet`, `player_owned_guardian`, `npc_hostile_candidate`, `boss_verified`, `unknown_quarantined`
- Carry `classificationReason`, `sourceFlags`, `sourceGuid`, `destFlags`, `spellId`, `instanceMapId`, `observedAt`, `evidenceLevel`.
- Only `boss_verified` should automatically create confident boss entries; `npc_hostile_candidate` requires evidence/thresholds.

## Remaining blockers
- Decompress and cross-index all source archives, especially full creature/spell tooltip and per-class spellbooks.
- Resolve 7 creature and 4 spell candidates with exact raw-record excerpts.
- Build class->spec->summon spell->creature->pet ability relationships with per-edge citations and conflicts.
- Verify actual in-game combat flag behavior for summons, charm, and guardian events on Conquest Reborn.
- Only after tests produce a DBM-CoA patch proposal; no changes to DBM-CoA have been made.
