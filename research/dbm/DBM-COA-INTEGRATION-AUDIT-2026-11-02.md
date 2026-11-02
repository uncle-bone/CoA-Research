# DBM-CoA research integration audit — 2026-11-02

**Target:** Conquest Reborn / WoW 3.3.5a. **Repository:** uncle-bone/CoA-Research.

## Existing machine-readable evidence inspected

1. `research/dbm/classic-all-19-dungeon-dbm-integration-rosters-timers-and-confidence-2026-10-30.json` — reports **19 dungeon maps**, **190 encounter NPCs**, **6 maps with timer candidates**, **1 repeat-only map**, **4 spell-only maps**, and **8 roster-only maps**. Its own availability statement says live Conquest Reborn availability is **not independently verified**.
2. `research/dbm/dbm-coa-vanilla-19-plus-zulgurub-consolidated-source-handoff-2026-10-30.json` — reports **113 exact** and **15 provisional** dungeon mechanic rows; **23 Zul'Gurub script files**, **8 custom boss files**, **145 spell definitions**, and **212 mechanic-signal lines**. These are **source-reported totals**, not independently recounted in this audit.
3. `research/encounters/coa-vanilla-and-raid-full-encounter-overrides-2026-10-30.json` — existing encounter-overlay candidate source (identified, not fully validated in this pass).
4. `research/dbm/coa-dungeon-boss-kit-timers-2026-10-30.json` — existing timer candidate source (identified, not fully validated in this pass).

## Integration policy

- **Tier A / live verified:** boss NPC and spell ID confirmed by Conquest Reborn combat-log evidence; predictive timers require repeated observed timing or independently verified deployed script.
- **Tier B / source verified:** spell/cast/phase relationship verified in cited upstream source; keep experimental until live confirmed.
- **Tier C / provisional:** incomplete or inferred mapping; log and inspect only, no predictive timers.
- **Tier D / roster only:** detect encounters and record combat events; no unsupported warnings.

## Implementation order

1. Import encounter NPC and map identifiers from the 19-map handoff; retain source and confidence per row.
2. Enable raw combat-log capture with timestamp, map/difficulty, source/destination GUID and NPC IDs, event type, spell ID, and encounter lifecycle; filter player/pet noise only in derived boss analysis, not raw evidence.
3. Enable cast-triggered warnings for independently confirmed hostile boss spell IDs.
4. Add predictive timers only where source initial/repeat timing and runtime conditions are documented; never derive initial timer from repeat interval.
5. Validate live Conquest Reborn logs against upstream data and promote records to Tier A individually.
6. Keep BBLC25C protocol namespaced, bounded, and independent of chat-channel numbering. Never share raw full logs through the chat channel.

## Source separation

- Conquest Reborn official website: https://conquestreborn.com/ — current public realm scope, not encounter scripts.
- Conquest of AzerothCore: https://github.com/Conquest-of-AzerothCore/azerothcore-wotlk-coa — separate public implementation, **not** the deployed Conquest Reborn server.
- TrinityCore 3.3.5: https://github.com/TrinityCore/TrinityCore/tree/3.3.5 — stock baseline.
- Historical preservation: https://github.com/Bharph/coa-preservation-data — historical reference, not live encounter proof.

## Next extraction task

Normalize existing `maps[].encounters[]`, `timedCandidates[]`, and `otherMechanics[]` into a stable CSV/JSON crosswalk keyed by map ID + NPC ID + spell ID + difficulty, with source file, confidence, initial/repeat interval semantics, and live-verification flag. Do not silently collapse conflicting upstream mappings.

**Status:** repository inventory and two source files directly inspected; this document is an audit and implementation gate, not a claim that all source data has been extracted or tested in game.
