# DBM-CoA v6 research baseline

Generated 2026-11-03. This is an evidence-indexing baseline built from checked-in CoA-Research sources and the inspected DBM-CoA default-branch checkout. It is **not** a claim that v6 is complete or that source candidates match live Conquest Reborn.

## Inputs pinned for this pass

- CoA-Research: `acff72745a107407812e76ddea4efffbef844f71`.
- DBM-CoA: `ba9d91fb44dbd26d2755682279962a5cfe407787`. The fetched repository reports addon version 5.2.24 in `DBM-CoA-Learner/DBM-CoA-Learner.toc`; README text still describes stable v5.2.23, while `.release.json` marks v5.2.24 prerelease. Those are metadata states, not release verification.
- Priority instance source corpus: `datasets/instance-scripts/priority/coverage-report.json` (22 instance entries, source archives collected from six upstream repositories plus the then-current CoA-Research snapshot). It explicitly says findings are not live verified.

## Key finding

The assignment's priority seven are not seven equally evidenced dungeon modules. Road to De Other Side (source alias: “Road to De Other Side”, map candidate 937) and Vaults of the Inquisition (map candidate 936) have source-derived boss dossiers; Blackrock Caverns has five TrinityCore filename candidates and candidate IDs, not CoA-confirmed implementation. Shadowbone Depths has a dossier and explicit gaps. Manastorm evidence is primarily a reward/mode system and must not be modeled as a distinct instance without map/instance evidence. The inspected research pass did not find boss-script evidence for The Temple of Embers or The Radiant Spring; the latter appears in a user-provided content-scope list only.

## Seven-dungeon status

| Target | Research state | Live status | Safe DBM use now |
|---|---|---|---|
| Manastorm | mode-and-reward-system-evidence; do-not-model-as-a-distinct-instance-without-map-evidence | Unverified | Detection-only only after map/name confirmation; no speculative boss timers |
| Shadowbone Depths | quest-and-narrative-source-evidence; encounter identity unresolved | Unverified | Detection-only only after map/name confirmation; no speculative boss timers |
| The Temple of Embers | no-instance-script-evidence-indexed | Unverified | Detection-only only after map/name confirmation; no speculative boss timers |
| The Radiant Spring | name-only-content-scope-evidence; encounter evidence absent | Unverified | Detection-only only after map/name confirmation; no speculative boss timers |
| Road to the Other Side | source-candidates-found | Unverified | Detection-only only after map/name confirmation; no speculative boss timers |
| Vaults of Inquisition | source-candidates-found | Unverified | Detection-only only after map/name confirmation; no speculative boss timers |
| Blackrock Caverns | source-candidates-found | Unverified | Detection-only only after map/name confirmation; no speculative boss timers |

## Existing 22-instance source corpus

`INSTANCE-REGISTRY.json` carries all 22 entries from the checked-in priority archive. This is not the complete instance roster demanded by the assignment. `DBM-MODULE-COVERAGE.json` is a source-file inventory aid and must be reconciled against each module TOC, localization, `DBM:NewMod`, event registration, map ID and GUI category before claiming module coverage. The live-support state of every row is unresolved.

## DBM architecture observations (DBM-CoA ba9d91fb44dbd26d2755682279962a5cfe407787)

- Native instance modules use `DBM:NewMod(...)` inside existing module folders; the current Vanilla/TBC party modules already group instance encounters by native subcategory. v6 should follow this loader and GUI pathway, not introduce a parallel encounter UI.
- `DBM-CoA-Learner/DBM-CoA-Learner.toc` declares interface 30300, dependency `DBM-Core`, SavedVariables `DBMCoALearnerDB`, and explicitly lists each research/learning Lua file. A new data-driven module needs TOC inclusion and unique module IDs; folder creation alone is insufficient.
- `Classic19CastWarnings.lua` and `Classic19SourceTimers.lua` subscribe to `COMBAT_LOG_EVENT_UNFILTERED` and area/instance-change events. The source timers track NPC/spell observations and consult stock indexes; timings from public source should remain behind explicit evidence gates.
- `LiveLearning.lua` gates learning to hostile NPC GUID/flags, groups observations by zone/type/difficulty, and uses sample-count/outlier rules. This is discovery evidence, not a guarantee of encounter identity or timer accuracy.
- `SourceTimerEngine.lua` uses native `DBM.Bars:CreateBar`, skips NPC/spell entries already in the stock timer index, and checks the opt-in source-timer SavedVariable. Keep native bars and duplicate suppression. Audit its event scheduling and timer cancellation before expanding it.
- `SmartSync3.lua` is namespaced `DCOAS3`, targets `CoASync`, bounds pending packets, validates record shape and keeps legacy protocols separate. Preserve wire formats and SavedVariables; test peers with real WoW 3.3.5a event arguments.
- `DBM-Core/DBM-Core.lua` owns `DBM:StartCombat`, `DBM:EndCombat`, mod creation and difficulty helper behavior; encounter modules should invoke native APIs rather than create their own boss panel or tree.

## Timing policy

Use the priority chain in `DBM-V6-IMPLEMENTATION-SPEC.md`: verified existing DBM timer; timing from an identified server-source revision (experimental until deployment is established); repeated live combat observations; high-confidence learned estimate; otherwise no bar. Preserve ranges and conditions. Do not turn SQL fields or C++ schedule expressions into exact countdowns without matching semantics, cast completion behavior, phase, difficulty, and reset logic.

## Unresolved completeness

The full instance inventory, complete custom-instance rosters, CoA-specific spell mappings, deployed server revision, live combat evidence, exact difficulty behavior, and live compatibility/performance checks remain open. See `UNRESOLVED-RESEARCH-GAPS.md`.
