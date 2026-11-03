# BindMySoul — Vol'jin realm source assessment

- Added: 2026-11-03
- User-provided URL: https://bindmysoul.com/?realm=voljin
- Realm query parameter: `voljin`
- Scope: candidate third-party realm-specific research source; exact database coverage and server/client affiliation **not established**.
- Access status: direct webpage fetch failed (disabled); indexed web search returned no results in this research pass. **No site content was retrieved or verified.**
- Evidence status: URL supplied by user, unverified site content.
- Confidence: source discovery only; **not** verified CoA/Conquest Reborn data.

## Intended research workflow

1. When reachable, identify site owner, realm identity, data provenance, license/robots and update dates.
2. Inventory available entities and stable IDs: classes/specs, spells, creatures, quests, objectives, items, loot, NPC spawns, trainers and locations. Do not assume any category exists.
3. Determine whether `realm=voljin` is a server-specific data filter, and whether that realm actually corresponds to the target Conquest Reborn build.
4. Compare records by explicit IDs and version/realm context against CoA-Research archived sources. Preserve original URLs, retrieval timestamps, raw source values, and conflicts.
5. Only promote links into normalized datasets when the source explicitly supports them; distinguish historical/third-party candidates from client-verified facts.

## Blockers

- Website content could not be fetched in this session.
- No supported schema, API, export, or record URLs identified.
- Realm/build compatibility and licensing not verified.

Do not fabricate data or silently treat this website as authoritative. No core dataset records were changed by this source-registration commit.

## Follow-up scan: GitHub evidence (2026-11-03)

### Relevant source discovered
- https://github.com/hertigservices/Ascension_preservation/tree/main/tools/character-importer
- https://github.com/hertigservices/Ascension_preservation/blob/main/tools/character-importer/README.md
- https://github.com/hertigservices/Ascension_preservation/blob/main/tools/character-importer/bms_parse.py
- https://github.com/hertigservices/Ascension_preservation/blob/main/tools/character-importer/bms_import.py
- https://github.com/hertigservices/Ascension_preservation/blob/main/manifests/source-origins.json

The importer documentation explicitly describes Bind My Soul as an **in-game character-checkpoint addon and website-provided checkpoint archive**, with an offline AzerothCore character importer. Documented data include equipment, known spells, talents, skills, reputations, action bars, quests, and CoA custom-class advancement. The source is evidence for **checkpoint structure and migration compatibility**, not a confirmed public quest/NPC/loot database.

The parser documents `BMSP1` and `BMSP2` envelopes and `BindMySoulDB.checkpointExport` / `checkpointQueueExport` SavedVariables. The parser states the addon's `integrity.sealStatus` is `pending-companion-hash` rather than a cryptographic digest: **do not treat captured checkpoint payloads as tamper-evident**. The importer uses DBC matching and dry-run preflight, and explicitly does not restore pets, mounts, glyphs, bank, guild, or quest objective progress. Its own documentation states no live trainer or creature-loot catalog is provided.

The migration manifest traces the character importer to `hertigservices/BindMySoul-Ascension-Importer` at commit `e8bf002236eb2cfd2f34d8d61e97c19f6c66f875`. This is source-code provenance; no proof that this project operates the currently linked website.

### Website and realm verification
- `https://bindmysoul.com/?realm=voljin` was not retrievable through the web reader (disabled fetch).
- Direct HTTPS attempts to both bare and `www` hosts failed DNS resolution from the execution environment.
- Searches for the domain, Vol'jin parameter, and site GitHub code did not locate a verified website deployment repository or public API.
- The `realm=voljin` parameter is **not verified** to identify Conquest Reborn or the same environment as the importer. Do not join realm-specific character data based on this parameter alone.

### Research opportunities and safeguards
1. Analyze parser schema and `bms_coa` / DBC resolver to map **explicit** captured character spells/talents and custom-class advancement fields; classify as historical snapshots, not universal class spellbooks.
2. Compare imported quest IDs and character state with CoA-Research only if consented, privacy-safe example checkpoints are available. Never ingest personal character checkpoints or account data by default.
3. Add deterministic schema validation for checkpoint parsing and explicitly document incomplete quest objective progress, pet state and trainer data.
4. Do not infer creature loot, NPC spawns, pet ownership or live spell availability from a character checkpoint.

### GitHub scan assessment
A public code-search hit for `bindmysoul.com` was found in the character importer and its tests. No authoritative BindMySoul site/backend repository was established. Generic repositories mentioning `Vol'jin` are unrelated realm-name collisions, not usable evidence.
