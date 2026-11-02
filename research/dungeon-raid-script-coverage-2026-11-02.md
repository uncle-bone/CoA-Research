# Dungeon and raid NPC / encounter script coverage audit — 2026-11-02

## Objective
Collect full, source-attributed scripts for every dungeon and raid: boss AI, trash AI, NPC interactions, triggers, spawns, phases, timers, dialogue, loot and instance progression. **Do not represent client encounter metadata as actual server-side scripts.**

## Verified source boundaries
- [srhinos/coa-datamine AGENT-GUIDE](https://github.com/srhinos/coa-datamine/blob/master/AGENT-GUIDE.md): client-derived `data/dungeons/index.json` and per-dungeon files cover 430 dungeon entries, including 109 raid entries, and 2,704 encounter entries. These are client metadata, not executable encounter AI. Of the 2,704 encounter entries, 84 have no resolved creature link (66 lack an extra row; 18 have an unresolved creature ID).
- `data/creatures/` holds 127,179 creature-template ID/name records; it does not supply AI scripts.
- The upstream guide explicitly states boss scripts, loot tables, runtime grants and proc internals are server-side and absent from the client extraction.
- [Conquest Reborn dungeon and raid page](https://conquestreborn.com/dungeons.html) describes classic dungeons at Normal/Heroic/Mythic and Mythic+; Outland/Northrend dungeons are closed. Its snapshot says raids have not yet opened; verify live status again before claiming availability.
- Blackrock Caverns is described as opened October 18; Shadowbone Depths is described as planned/in progress on the [official home page](https://conquestreborn.com/). Do not treat unshipped content as live.

## Source hierarchy and status flags
1. `verified-server-source`: actual server-side source, licensed for reuse, with path, revision, encounter and creature IDs.
2. `verified-runtime`: combat log, live observation, or reproducible test confirming behavior; not source code.
3. `client-metadata`: DBC/JSON creature, encounter, map, difficulty and spell references.
4. `upstream-reference`: stock TrinityCore/AzerothCore encounter scripts; **not** evidence that Conquest Reborn runs identical logic.
5. `candidate`: inferred match or unresolved identity.
6. `unavailable`: server implementation not publicly obtainable or not yet located.

## Collection requirements
For each instance, preserve map ID, LFG dungeon ID, difficulty, availability, encounter ID, boss creature IDs, alternate creature variants, trash creature IDs, spawn references, AI source path, source repository/commit/license, spell IDs, phases, casts, target selection, cooldown ranges, summon ownership, events, doors, gameobjects, gossip, scripts, and evidence type. Preserve unknown fields as unknown rather than filling from retail/stock assumptions.

## Next evidence collection
1. Enumerate all 430 client dungeon entries, group by map and difficulty, and identify the 109 raid entries without treating them as 109 distinct raid zones.
2. Resolve the 84 missing encounter creature links where evidence exists; do not infer unique IDs by name alone.
3. Search permitted public server-source projects for stock encounter implementations, retain upstream attribution and license, and label each as reference-only until verified in Conquest Reborn.
4. Obtain live combat logs or authorized server sources for Conquest-specific overrides, new Blackrock Caverns, and future Shadowbone Depths.
5. Export DBM-safe mechanics separately from uncertain candidates; never register player pets/summons as bosses based on NPC names alone.

## Explicit limitation
No complete proprietary Conquest Reborn server-side boss/trash/instance script corpus has been verified as publicly available. A complete client datamine cannot recover code that only exists on the server.
