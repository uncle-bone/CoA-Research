# DBM-CoA v6 implementation handoff — grounded status

Use this as the implementation starting point; do not treat unresolved research as a request to fabricate modules.

## Inputs

- `PRIORITY-SEVEN-DUNGEONS.json`: normalized state for the seven named targets.
- `INSTANCE-REGISTRY.json`: the 22 source-corpus instances plus named custom targets; explicitly incomplete as a live inventory.
- `BOSS-REGISTRY.json`, `SPELL-MECHANICS.json`, `ENCOUNTER-TIMINGS.json`: source-index candidates only. These are not production warning/timer tables.
- `INSTANCE-SOURCE-MAP.json`, `SOURCE-PROVENANCE.json`: source lineage and revision references.
- `DBM-MODULE-COVERAGE.json`: module source-file inventory needing TOC/localization/map reconciliation.
- `DBM-V6-IMPLEMENTATION-SPEC.md`: native architecture, evidence gates and timer arbitration.

## First safe engineering slice

1. Build an automated native module inventory from the current DBM-CoA default branch: parse each package TOC, locale, `DBM:NewMod`, registered map/NPC IDs, and start/end signals; emit a stable diffable coverage file.
2. Validate data cross-references and the priority datasets in CI. Keep source-only candidates out of live-warning/timer exports.
3. Add deterministic regression fixtures for existing Learner and SmartSync v3 behavior before any protocol or runtime changes.
4. Implement only records that pass the evidence gates; start with native module coverage gaps backed by live logs or exact deployed source.
5. Maintain one source record per fact, keep conflicts side-by-side, and add explicit promotion history when evidence changes status.

## Hard prohibitions

Do not copy Cataclysm mechanics into Blackrock Caverns as if verified, do not infer Manastorm as a map, do not create boss IDs/spell IDs/timers from names, do not overwrite existing DBM modules, and do not publish v6 until the tests and in-game acceptance criteria pass.
