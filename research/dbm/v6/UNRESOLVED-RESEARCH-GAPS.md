# DBM-CoA v6 unresolved research gaps

## Blocking encounter evidence

- No live Conquest Reborn logs or authorized deployed-server revision were available in this pass. All public/archive source candidates remain non-live evidence.
- The complete live instance/mode/difficulty inventory and instance IDs have not been established. The 22-row priority source corpus is not a full inventory.
- The Temple of Embers and The Radiant Spring do not have boss/AI dossiers in the inspected DBM source corpus. The Radiant Spring appears in an AtlasLoot content-scope record, which is not instance or encounter proof.
- Manastorm sources describe cache/reward and progression/mode behavior. Whether it is an instance, a run mode over other maps, or a combination must be grounded in actual map/instance runtime evidence. Do not invent a standalone map.
- Shadowbone Depths has historical/user-provided dossiers and gap analysis, but boss IDs, deployed scripts, spells, difficulty and availability still need verification.
- Blackrock Caverns has five TrinityCore boss filename candidates (Rom'ogg Bonecrusher, Corla, Karsh Steelbender, Beauty, Ascendant Lord Obsidius) and candidate spell IDs in the archive; it is a Cataclysm reference, not proof of CoA content or mechanics.
- Road to the Other Side and Vaults have source-derived dossiers, including candidate map/boss/timing data; source branch provenance and exact implementation semantics need verification against the deployed CoA revision.

## Data-quality and implementation gaps

- Spell IDs in source inventories can be shared, unused, difficulty-overridden or bound to other NPCs; source inventory identifiers are not normalized spell-to-boss links.
- Script timing expressions may be randomized, conditional, cast-start, cast-success, delayed, reset, or phase-local; automatic expression capture does not identify timer semantics.
- Boss/trash attribution and map/difficulty reconciliation require source and live evidence.
- Native module coverage needs a full crosswalk of TOCs, localizations, module IDs, map IDs, creature IDs, GUI categories, native module event wiring and stock timer duplication.
- No full performance benchmark, in-game test matrix, module ZIP or v6 release was produced in this assignment.

## Evidence needed to close these gaps

Version-pinned authorized server source and world/instance SQL; client-confirmed instance names/map IDs/difficulty behavior; reproducible combat logs with full source flags and casts per difficulty; screenshots or recordings for availability only as supplementary evidence; and in-game tests against the intended DBM-CoA package.
