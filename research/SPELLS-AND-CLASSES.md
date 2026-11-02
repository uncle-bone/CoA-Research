# Spell, class, and specialization research

## Data hierarchy
1. **Observed Conquest Reborn client data and combat logs:** highest priority for actual spell IDs, class/spec behavior and combat-log encoding.
2. **Client DBC/WDB and verified extracts:** strong candidates; record client version, timestamp and source files.
3. **Preserved class spellbooks/tooltips:** broad historical coverage, not necessarily exact current spell effects.
4. **CoA AzerothCore and SQL mirrors:** useful names, ranks, NPCs, spell code and possible effect IDs. Do not assume exact parity with Ascension live realm.
5. **CoA talent calculators / BisBeard metadata:** cross-check names, roles, builds and relationships; cannot prove combat-log effects alone.

## Known corpus
- [DealsBeam/ascension-db](https://github.com/DealsBeam/ascension-db) README states **464,048 SQL rows across seven files**, derived from an August 2026 preservation snapshot. Spell-oriented SQL contains **222,456 rows** including `spell_dbc` + `spell_ranks`. This figure **is not 222,456 unique playable class abilities**.
- The same audit [missing.md](https://github.com/DealsBeam/ascension-db/blob/main/missing.md) documents lost raw DBC attributes, proc flags, numeric spell-effect fields, and other missing information. Never invent them.
- [CoA preservation](https://github.com/Bharph/coa-preservation-data) contains class spellbooks, spell tooltips, caches and changelogs; manifests can point to data packs not bundled in the base archive. Confirm pack acquisition before claiming the corpus is wholly imported.
- [CoA Databank](https://github.com/f3rr311/CoA-Databank), [talent scraper](https://github.com/v1cferr/ascension-coa-scraper), and [CoA talents site](https://coa-development.org/talents) provide complementary class/talent sources.
- [CoA AzerothCore](https://github.com/Conquest-of-AzerothCore/azerothcore-wotlk-coa) has `modules/mod-spellbook`, `modules/mod-ascension` and `data/coa-world`; the project's SQL and modules should be inspected selectively for relevant mappings.

## Important caveats
- A Tinker-related SQL completion patch was **reported missing** from the DealsBeam conversion baseline (`rev_20260910_15_tinker_completion.sql`). Consult upstream/release archives; do not assume Tinker coverage complete.
- Tinker specialization terminology includes **Mechanics, Invention, Demolition** in the user's development scope; IDs 49/50/51 are **candidate mappings requiring verification**, not an authoritative API guarantee.
- Vanilla, TBC and WotLK spell references are all in development scope, even when expansion gameplay is not currently accessible.
- Many effects arrive as separate aura/periodic/summon events rather than the player's direct attack. A spell-ID lookup is insufficient to identify ownership.

## Installed client and PTR source pass (2026-11-02)

The [Details-CoA class/spec/server-source audit](DETAILS-COA-CLASS-SPEC-SERVER-SOURCE-2026-11-02.md) and its [self-contained client package](local-client-extracts/2026-11-02/details-coa-class-spec-research/README.md) add local client counts, a 21-class/70-spec crosswalk, seven missing direct tab mappings, runtime API evidence, and a pinned PTR-source snapshot. The installed `CharacterAdvancementData.json` has 23,709 records and 21,063 unique linked spell IDs; `SpellRankData.json` has 13,311 rows. These counts describe files, not live availability.

The CoA core's [talent-system notes](https://github.com/Conquest-of-AzerothCore/azerothcore-wotlk-coa/blob/9f22d992e39410c6869d1efad6426f0fd2eef081/.agents/docs/systems/ascension-talents.md) distinguish internal specialization/tab tokens from display names and document active spec state and advancement packets. The [spell-twins notes](https://github.com/Conquest-of-AzerothCore/azerothcore-wotlk-coa/blob/9f22d992e39410c6869d1efad6426f0fd2eef081/.agents/docs/systems/warcraft-reborn-spell-twins.md) describe an ID offset for particular Reborn spell twins; retain explicit per-spell aliases and never treat the offset as universal. These server-source findings remain unverified against a particular deployed PTR realm.

## Future import format
Create an extracted, versioned `CSV/JSON` manifest with `spell_id, name, rank, source, source_version, class, specialization, category, confidence`, separate from small runtime Lua lookup tables. Annotate uncertain fields. Preserve third-party licenses and provenance.

Avoid forcing hundreds of thousands of rows into a game addon at startup. Use minimal tables for exceptions and rely on client `GetSpellInfo` when available.
