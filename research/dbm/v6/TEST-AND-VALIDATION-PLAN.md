# DBM-CoA v6 test and validation plan

## Offline deterministic checks

- Parse all addon Lua as Lua 5.1; reject 5.2+ syntax/APIs.
- Parse all research JSON; validate schemas, stable IDs, unique `(moduleId, mapId, NPC, difficulty)` tuples, source paths/revisions, and all foreign references.
- Parse `.toc` files; ensure every listed path exists and every encounter module is listed exactly once.
- Scan for duplicate `DBM:NewMod` IDs, duplicate NPC ownership, missing localization keys, absent map/creature registrations, invalid spell IDs, and module category collisions.
- Simulate module load and native registration under a stub DBM core; validate GUI category visibility without creating a replacement UI.
- Replay fixture combat events for start/end, cast warnings, target warnings, phase changes, interval timer scheduling, timer correction/cancellation, duplicate bars and difficulty transitions. Label generated fixture events synthetic.
- Learner tests: hostile gate, pet/player exclusion, sample thresholds, median/outlier behavior, identical NPC display names, bounded storage and zone reset.
- SmartSync v3 tests: plain/decorated channel names, channel number, malformed packet, duplicate, collision, bounded queue, mixed legacy/v3 records, disconnect/rejoin, and per-tick work cap.
- SavedVariables tests: old schema loads unchanged, migration idempotence, user preferences preserved, data cap behavior.
- Package test: expected folder layout, TOC paths, no development-only files/secrets, ZIP integrity, checksums.

## In-game acceptance

For each instance and difficulty: enter/leave/reload; confirm native category and module appears; observe exact boss start/end; compare every warning/timer to combat log; test wipe/reset and phase cancellation; verify no duplicate stock/source/learned bars; test with other addons enabled; and record client build, date, map/difficulty, DBM commit and evidence artifact.

## Evidence limits

Offline stubs validate code logic only. They do not validate live boss identity, deployed mechanics, spell effects, difficulty behavior, encounter availability, client performance, or peer interoperability. Synthetic fixtures must never be promoted as live encounter evidence.
