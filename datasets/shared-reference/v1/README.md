# Shared reference v1 — initial cross-addon export

This directory is a **partial, provenance-labeled export** of existing CoA-Research records, not a complete current Conquest Reborn database. Every record includes `sourcePath`, `sourceExtractionDate` (set to `unknown` when absent), `confidence`, and `liveRebornVerified`. False means **not independently live-verified**, not disproven.

## Contents
- `classes.json`: 21 archived custom class IDs and links to historical specialization IDs.
- `specializations.json`: 101 source-derived specialization rows (includes non-custom classes).
- `spells.json`: four quarantined, user-reported spell candidates.
- `pets-and-summons.json`: seven quarantined NPC ownership candidates; zero confirmed ownership edges.
- `quests-and-npcs.json`: client-extract inventory, not normalized coordinates.
- `items-and-loot.json`: client-extract item inventory, not verified loot tables.
- `combat-attribution.json`: proposed GUID/flags classification policy, not runtime tested.
- `client-compatibility.json`: 3.3.5a/Lua 5.1 target; no runtime verification imported.

Existing bulk catalogs, spell/talent graph, DBM encounter corpus and Questie-X extracted JSONL remain authoritative *source artifacts* and have not been overwritten or duplicated wholesale. Current export intentionally does not infer summon ownership from NPC names or item drops from generic creature presence.

## Validation
Run `python3 tools/validate_shared_reference.py` from the repository root. It checks file presence, JSON schema version, count consistency, provenance fields, class/spec links, and quarantined candidate status. It does **not** prove the source records match live gameplay.

## Next extraction stages
1. Decompress archived ability/spellbook/creature tables, join explicit summon-effect and creature IDs with citations; preserve unresolved and conflicting links.
2. Normalize Questie-X quest/NPC/object links and map coordinates where actually present.
3. Cross-join item catalog and encounter/creature drop evidence; distinguish guaranteed and candidate drops.
4. Join talent nodes and trainer records, retaining rank/prerequisite source and extraction dates.
5. Capture in-game 3.3.5a combat-log flags and map events to owner GUIDs; avoid static blacklists.
6. Record observed UI/API behavior for stock, Mapster, DragonUI and ElvUI; don't infer compatibility from filenames.
