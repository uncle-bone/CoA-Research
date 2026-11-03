# Conquest Reborn local class, spell, pet, and summon research

Scanned on 2026-11-01 from `C:\Games\Conquest Reborn`. This package contains derived JSON/JSONL records from the installed client and installed addons. It does not include MPQ archives or personal SavedVariables.

## Contents

- `class-ability-talent-index.jsonl.gz`: compact 23,705-row index of class/tab/node/spell/prerequisite links.
- `class-summon-entity-candidates.jsonl.gz`: 977 name-matched class-node candidate rows across 18 class keys; candidate labels do not establish entity ownership.
- `missing-data-report.json`: per-registry-class coverage and unresolved blockers.
- `whats-training-local-research/`: existing installed addon trainer research and audit files; retained with its no-trainer-mappings caveat.
- `class-roster-and-coverage.json`: roster evidence from the installed WhatsTraining class registry and CharacterAdvancementData, including their mismatch.
- `character-advancement-records.jsonl.gz`: all 23,709 rows from `Data/Content/CharacterAdvancementData.json`, retaining raw fields for class, ability/talent type, tab, linked spell IDs, prerequisites, and node metadata.
- `spell-rank-data.json`: all 13,311 local spell rank rows.
- `skill-card-spell-links.jsonl.gz`: all 49,670 local skill-card-to-spell links; no class ownership is inferred from these links.
- `necro-minion-crosswalk.json`: structured extraction of NecroMinions' summon/aura/species mappings, joined to class advancement and name-reference rows.
- `false-discovery-candidate-review.json`: focused review of requested suspect NPC/spell IDs with exact local evidence and uncertainty.
- `entity-name-candidates.jsonl.gz`: name-based summon/pet/guardian/totem candidates for review only.
- `npc-name-reference.jsonl.gz` and `spell-name-reference.jsonl.gz`: local name maps. Their upstream metadata says they are preserved Exiles DB snapshots and unverified for Conquest Reborn.
- `source-inventory.json`: source paths, sizes, record counts, and caveats.
- `ownership-filtering.md`: evidence-backed runtime filtering recommendation for DBM-CoA.

## Key findings

The installed advancement JSON has 23,709 records, 44 distinct `Class` values (including `None`, base classes, `Reborn*` namespaces, and custom classes), and types including Ability, Talent, TalentAbility, Trait, and None. The separate installed WhatsTraining registry lists 21 CoA class tokens. The two sources disagree: registry-only names include Felsworn, Templar, and Bloodmage; advancement-only custom names include DemonHunter, Monk, and SonOfArugal. This package preserves both views and does not claim either is the definitive currently playable roster. Tabs are retained as client node labels; they are not silently recast as specializations.

NecroMinions contains explicit Necromancer summon spell and entity-kind mappings. Examples: spell 500969 is called `Raise: Skeletal Rogue` in the local spell-name reference, is mapped as kind `rogue` by NecroMinions, and appears in CharacterAdvancementData under the name `Raise: Crypt Leaper`; NPC reference ID 50078 is named Skeletal Rogue. This is strong cross-source evidence for a species/ability link, but the NPC reference metadata itself is unverified for CR and static data cannot prove a live entity was player-owned. Similar alias conflict exists for spell 500335 (`Raise: Abomination` vs advancement node `Raise: Flesh Golem`).

Candidate NPC 1374 is locally named Rejold Barleybrew, not Devilsaur. The client reference has Devilsaur NPC entries 6498, 6499, and 6500; CharacterAdvancementData links ability 801585 (`Call Avatar: Devilsaur`) to WitchDoctor / Shadowhunting. Do not blacklist 1374 as a Devilsaur.

DBM-CoA-Learner's installed `ResearchIndex.lua` associates NPC 50068 with spell 578319 (Disease Cloud), 50078 with spell 805024 (Decaying Poison), and 50119 with spell 504909 (Shadow Effigy). Its own header says the index is derived observation research and not confirmed encounter mechanics. Preserve these as candidate associations only.

The package includes 30 NecroMinions summon-spell-to-kind mappings and 11 aura-spell-to-kind mappings. It also includes 977 label-matched class-node candidate rows; those are leads, not confirmed summon ownership.

## Local sources and limitations

The local `Data\Content` JSON files were parsed directly. The game `Data` folder also contains many large MPQ archives. The Data folder contains 72 MPQ archives totaling 43,354,546,252 bytes. No MPQ extraction utility/library was available in the local environment, so MPQs were inventoried but not extracted. No archives were copied. No combat logs or live character session were inspected. `CoA-Research-Offline` metadata labels its NPC/spell maps as preserved Exiles DB snapshots, unverified for Conquest Reborn. No relationship based only on a creature name is treated as confirmed ownership.
