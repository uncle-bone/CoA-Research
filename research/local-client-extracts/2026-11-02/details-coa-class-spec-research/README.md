# Details-CoA class, specialization, spell, and summon research

Research package prepared from the installed Conquest Reborn client and the local `uncle-bone/CoA-Research` checkout. It does not inspect or modify Details source.

## Key inventory

- 21 class identities and 70 archived specialization records from CoA-Research.
- Installed `CharacterAdvancementData.json`: 23,709 records, 44 raw `Class` values (this includes base/`Reborn*` namespaces and sentinels, not 44 playable classes), 6,953 Ability, 4,522 Talent, 573 TalentAbility, 11,657 Trait, 4 None; 28,199 spell links across 21,063 distinct spell IDs.
- Installed `SpellRankData.json`: 13,311 spell-rank rows.
- Historical unified spell index: 9,656 spell IDs; its audit reports 8,776 archived spell DBC definitions, 516 historical tooltips, 364 additional archive evidence, and 217 cross-source name conflicts. Its own warning says historical evidence does not prove current-client behavior.
- Preserved pre-shutdown class spellbook snapshots exist for 21 classes.
- Existing client-derived summon, NecroMinions crosswalk, entity-name candidates, and ownership caveats are included.

## Second client install (`C:\CoA`)

Scanned the second installation as well. It is an installed WoW client, not a source checkout of the server core. Its release manifest identifies revision 8 (`descension-names-20260924`, not in-game-tested). The six checked loose files—CharacterAdvancementData, SpellRankData, SkillCardData, WorldMapAreaData, HandOfFateQuestData, and LFGData—are byte-identical to the first installation. The bundle includes the release manifest and relevant shipped class/spec UI code; MPQ archives were inventoried but not extracted.

## Read first

- `class-spec-coverage.json`: merged 21-class / 70-spec identity crosswalk and installed tab-match checks.
- `class-spec-coverage-gaps.json`: seven spec records without direct archived client-tab mappings and runtime blockers.
- `references/runtime-api-evidence.md`: installed UI source paths, line references, and safe integration guidance.
- `client/ownership-filtering.md`: guidance and evidence limits for pet/summon attribution.
- `client/CharacterAdvancementData.json` and `client/SpellRankData.json`: copied installed client data.
- `coa-research/relationships/unified-spell-research-index.json.gz`: historical spell cross-reference.
- `coa-research/snapshots/class-spellbooks-by-class.json.gz`: preserved in-game snapshot dated 2026-09-02.

## Identity correction

The raw installed client `Class` field values and the user-facing class names are different namespaces. CoA-Research explicitly crosswalks Felsworn to internal/client key `DemonHunter`, Templar to `Monk`, and Bloodmage to `SonOfArugal`. Do not treat those as roster conflicts. The 44 raw strings also include base classes, `Reborn*`, `ConquestOfAzeroth`, and sentinel values.

## Confidence and limits

- **Client-derived:** static content copied from installed `Data/Content` and installed addon/UI scripts. This confirms local file content, not live server behavior.
- **Archived-research-derived:** CoA-Research roster, identity audit, talent-node graph, spell index, and saved spellbook snapshot. These have historical/version caveats.
- **Candidate/inferred:** tab-name associations, spell-to-class links beyond explicit client data, and name-matched summon candidates. Keep labeled and do not treat as verified.
- **Unknown:** live active spec API output, current spell availability, observed combat-log ownership/event timing, and pet GUID lifecycle.

No MPQ archives were extracted or copied. No personal SavedVariables or combat logs are included. The package is research data, not a runtime addon module.

## PTR server source

The package now includes a targeted research addendum for the [public Conquest-of-AzerothCore PTR repository](https://github.com/Conquest-of-AzerothCore/azerothcore-wotlk-coa). Read `ptr-server-source-findings.md` and `.json` for active-spec storage, advancement protocol, spell-alias leads, Tinker ownership hooks, source paths, confidence, and remaining class-coverage work. Repository source does not prove deployment or observed combat-log behavior.
