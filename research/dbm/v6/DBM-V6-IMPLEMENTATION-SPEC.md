# DBM-CoA v6 native implementation specification

## Non-negotiable integration rules

1. Use `DBM:NewMod` in existing native module packages and subcategories. Do not add a second encounter UI, tree, profile/settings layer, or timer anchor.
2. Keep one authoritative module per encounter/difficulty identity. New modules must have unique IDs, localization entries, TOC inclusion, correct map IDs, and explicit NPC start/death/combat-end signals.
3. Reconcile difficulty from the actual CoA client/server data for each instance. Never map generic raid difficulty integers to custom modes by assumption.
4. Preserve existing modules and SavedVariables. Add migrations only when a schema change is required and tested.
5. Native DBM bars/warnings only. Event-driven parsing, bounded per-encounter state, clear cancellation on wipe/zone exit, and no periodic world scans.

## Module file contract

For each encounter: `DBM:NewMod(stableUniqueId, packageId, nativeSubcategory)`; localization for display name and warning/timer options; `mod:SetCreatureID(...)`; `mod:RegisterEventsInCombat(...)`; `mod:StartCombat(...)` through native combat detection; `mod:EndCombat(...)` through death/encounter signals; warning and timer calls through core APIs. Add file paths to the package TOC in load-safe order. Confirm the DBM GUI enumerates the native mod category after loading.

## Evidence-gated warnings

- Cast warning requires a spell ID tied to the exact hostile boss NPC and a specific source/live evidence record.
- Target warning additionally requires verified target selection semantics.
- Interrupt/dispel/movement advice requires a verified effect and actionable response.
- Trash mechanics are opt-in research until source attribution and live encounter relevance are confirmed.

## Timer arbitration

Key timer ownership by `(instance/map, encounter/module, boss NPC, spell, phase, difficulty)`. Precedence: existing verified native module > live-verified fixed/ranged mechanic > source-verified candidate explicitly marked experimental > high-confidence learner estimate > none. Never schedule a duplicate bar for the same key. On cast, correct/cancel the prior prediction and schedule only if timing semantics establish the next occurrence. Cancel on phase transition, reset, death, wipe, leaving instance, or difficulty change. Variable source ranges remain ranges; if DBM bar APIs cannot represent uncertainty honestly, use cast-based warning without a countdown.

## Learning fallback

Learning records raw source/destination GUID, flags, NPC, spell, event subtype, map, difficulty, timestamp and encounter context. Keep source observations separate from normalized encounter records. Require hostile NPC classification, exclude player-controlled pets/guardians, cap state and sample history, use robust statistics and outlier rejection, and show no timer until threshold/confidence is met. Do not use synthetic fixtures as encounter truth.

## SmartSync v3

Keep DCOAS3 and legacy handlers/wire formats compatible. Validate channel number and both plain/decorated CoASync names using WoW 3.3.5a event arguments. Bound queues, packet size and processing per frame; deduplicate records without conflating identity; reject malformed data; preserve old SavedVariables; and keep chat quiet. Never synchronize code or raw combat logs.

## Implementation gate per module

A boss module can be marked production-ready only when: exact map and difficulty; source-backed or live boss identity; localized native module registration; verified event lifecycle; spell-to-boss ties; warning semantics; timer semantics/cancellation; duplicate arbitration; test fixtures; TOC validation; Lua 5.1 parse; install ZIP check; and in-game confirmation are recorded. Otherwise ship detection/research-only behavior or leave it out.
