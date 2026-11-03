# Bind My Soul + Ascension Data — consolidated research findings

**Research date:** 2026-11-03  
**Maintainer:** Uncle Bone  
**Status:** Source inventory and candidate evidence; **not** live Conquest Reborn/Vol'jin gameplay verification.

## Primary references

- Bind My Soul planner: https://bindmysoul.com/?realm=voljin
- Bind My Soul download: https://bindmysoul.com/download
- Preservation project: https://github.com/hertigservices/Ascension_preservation
- Importer guide: https://github.com/hertigservices/Ascension_preservation/blob/main/tools/character-importer/README.md
- Checkpoint parser: https://github.com/hertigservices/Ascension_preservation/blob/main/tools/character-importer/bms_parse.py
- Importer implementation: https://github.com/hertigservices/Ascension_preservation/blob/main/tools/character-importer/bms_import.py
- Provenance manifest: https://github.com/hertigservices/Ascension_preservation/blob/main/manifests/source-origins.json
- Recovered data catalog: https://github.com/hertigservices/ascension-data
- Data README: https://github.com/hertigservices/ascension-data/blob/main/README.md
- Earlier assessment: [bindmysoul-voljin-source-assessment-2026-11-03.md](bindmysoul-voljin-source-assessment-2026-11-03.md)

## Site observations (reported by user from signed-in live site; not independently reproduced)

- Build Forge: 21 CoA classes, role filters, target level.
- Planner: Ability Vault and Talent Trees.
- Ability Vault fields: ability name, description, active/passive, class/tree, level, essence cost. Observed Venomancer listing: 46 entries across 12 pages.
- Talent Trees: specializations, ranks, dependencies/locks, level-bounded essence totals.
- Starter-tree recommendations are explicitly heuristic/local theorycraft drafts, not live game verification.
- Characters and My Builds private records were **not** inspected.
- Download page offered v1.3.5 Windows installer (28.8 MB, unsigned / Unknown Publisher), addon-only v1.3.5 ZIP, and described Soul Bridge's local checkpoint storage and account-linked synchronization. Nothing downloaded or executed for this research.

## GitHub source findings (importer and parser inspected)

The Bind My Soul addon produces character preservation checkpoints. An offline AzerothCore importer supports dry-run preflight and requires explicit `--apply` for database writes while the target realm is stopped. It resolves normal spells/talents using the target DBCs and handles CoA custom advancement separately.

Documented restore scope: character identity, equipment/bags, known spells, talents, CoA advancement, skills, reputations, action bars, active/completed quests, completed achievements and homebind. Documented limitations include appearance, titles, pets/mounts/companions, glyph IDs, bank/guild, quest objective counters, and exact world position. Do not infer gameplay spell availability or universal class mechanics from a single checkpoint.

**Integrity distinctions:**

1. SavedVariables `BMSP1` / `BMSP2` envelopes contain no computed cryptographic hash. The `integrity.sealStatus` marker `pending-companion-hash` is not proof of tamper evidence.
2. The `.bmsr.zip` offline importer validates internal hash relationships / bundle consistency.
3. The importer documentation states it does **not** verify the Ed25519 signature against the service's public key. Offline consistency validation is **not** publisher-authenticity verification.

The source-origins manifest attributes the importer subtree to `hertigservices/BindMySoul-Ascension-Importer` at `e8bf002236eb2cfd2f34d8d61e97c19f6c66f875`. No authoritative public source repository for the BindMySoul.com frontend/backend was established.

## Ascension Data inventory (public repository README independently inspected)

`hertigservices/ascension-data` was previously named `ascension-cache-consolidator`; tooling moved to `Ascension_preservation/tools/cache-consolidator`.

| Dataset | Reported coverage | Potential research use | Verification needed |
|---|---|---|---|
| Captured WDB caches | Per-source/per-mode variants, SHA-256 manifests | Client-observed NPC, quest, item records | Capture build, realm, record format and trust |
| `supplemental/exiles-db/` | Mirrored CoA site; spell, item, NPC, quest, achievement and talent-tree records | Entity names/IDs and candidate relationships | Site version and schema interpretation |
| `supplemental/exiles-db-export/` | PostgreSQL SQL/CSV export; **97 gameplay tables, 6.19M rows**, loot and raw spawn coordinates, icon map and 80,721 images (README-reported) | High-value candidate loot, spawn, world, quest and spell joins | Table schema, provenance, exact IDs, realm/build, duplicates |
| `supplemental/coa-databank/` | Attributed CoA talent/skill/community build scrape, MPQ spell/asset indexes | Class/spec/spell/talent cross-reference | Historical/community status, licenses, ID collisions |
| `supplemental/worldforged/` | Attributed pickup locations and upgrade ladders | Candidate location and progression relationships | Realm/version matching |
| `supplemental/bisbeard/` | Planner export, catalog and comparison report | Historical build references | Community vs game-authored evidence |
| `supplemental/client-dbc-snapshots/` | Differing DBC members with hashes and record-level reports | Client compatibility and ID comparisons | Client build matching |

All dataset counts above are **repository-reported**, not independently counted from the full archives. None is proof of current Vol'jin realm behavior.

## Logs audit — what was actually found?

**No actual recorded combat-log archive was identified during this scan.** Do not equate game databases or character checkpoints with time-ordered combat events.

| Source | Observed record/log type | Not established |
|---|---|---|
| Bind My Soul | Character checkpoint payloads: progression, spells, talents, equipment, quests | Damage/healing event stream, encounter timeline |
| Soul Bridge | Described local checkpoints and account sync | Public combat-log archive or sync audit logs |
| Offline importer | Dry-run checks, warnings, skips and import reports | Live gameplay event telemetry |
| Ascension Data | WDB cache records, manifests, hashes, provenance | Timestamped boss fights or spell casts |
| Exiles database | Historical gameplay tables and entity relationships | Recorded combat sessions |
| CoA Databank | Extracted assets/spells, planner/community references | Live combat logs |

### Still missing for DBM-CoA / Details! / combat attribution

- Actual combat event streams with timestamps, source/destination GUIDs, event subtype and spell IDs.
- Boss cast cadence, cooldown intervals, phase boundaries, wipe/death timelines.
- Verified owner-pet-summon GUID mappings, damage attribution, healing and threat events.
- Live-client comparison against archived spell and encounter data.

## Integration priorities (no automatic promotion)

1. Inspect Exiles export table schema and manifests, identify exact version, realm and provenance of each table and field.
2. Build quarantined staging indexes for spells, talents, NPCs, quests, items, loot and spawn coordinates; use explicit stable IDs and preserve source hashes.
3. Compare to CoA-Research v2.0.1 and report coverage, conflicts, duplicate IDs and missing joins.
4. Capture public Bind My Soul planner entries only when permitted and technically available; preserve descriptions as site-authored catalog evidence.
5. For DBM and Details!, collect **actual** client combat logs before promoting timings, encounter phases or summon ownership.
6. Keep personal account checkpoints and saved builds out of the public research database without explicit consent and privacy review.

## Release status

This document updates the **research repository only**. It does not claim a new shared-database release, source ZIP, completed Exiles ingestion, or live gameplay verification. The last independently verified shared-database release remains v2.0.1.
