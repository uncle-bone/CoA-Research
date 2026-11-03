# Learner and SmartSync audit — DBM-CoA source snapshot

**DBM-CoA revision inspected:** `ba9d91fb44dbd26d2755682279962a5cfe407787` (default branch, fetched 2026-11-03).

## Learner flow observed in source

- `Classic19CastWarnings.lua` and `Classic19SourceTimers.lua` observe combat-log cast events; zone/instance transitions clear local state.
- `LiveLearning.lua` accepts hostile creature/vehicle sources, rejects player-pet GUIDs and non-hostile/player-controlled flags, keys records by zone/type/difficulty/NPC/spell, and only derives an interval after at least three clustered samples. Its boundaries/outlier checks are heuristics requiring regression coverage.
- `EncounterEngine.lua` records context from `GetInstanceInfo`; it is adaptive observation/diagnostics, not proof that it can name every encounter.
- `SourceTimerEngine.lua` reads source ability records, checks stock-timer ownership and uses native DBM bars. Its current reset/cancellation and opt-in behavior must be covered before adding more records.

## SmartSync v3 flow observed in source

- Prefix `DCOAS3`, channel `CoASync`; queue cap 160, packet-length guard 231 characters, duplicate queued-packet suppression, incremental index rebuild, and validated N/S records are visible in `SmartSync3.lua`.
- Legacy DCOAL31/DCOAR21 compatibility is explicitly retained. Do not change wire encoding or identity fields without a migration and mixed-version fixture.
- Existing `tests/smartsync3_identity_test.lua` is a starting regression fixture; it does not replace client peer tests.

## Required next audit/tests

1. Trace exact TOC load order for all learning, timer, sync, data, localization, and options files.
2. Test event argument layouts used by the 3.3.5a combat log and decorated CoASync channel names.
3. Replay out-of-order, repeated, identical-name/different-NPC, pet-controlled, hostile, phase-reset, wipe, map-transition, disconnect/reconnect and mixed-version traffic.
4. Assert one timer owner and cancellation on all lifecycle exits.
5. Measure combat event cost and SavedVariables growth on representative long sessions; set hard record/queue caps.

No protocol change or implementation patch is proposed by this research pass.
