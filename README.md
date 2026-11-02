# CoA Research — Conquest Reborn Addon & Data Hub

**Maintainer:** Uncle Bone · [@uncle-bone](https://github.com/uncle-bone)

A searchable collection of research, reference data, and engineering notes supporting addons for Ascension's **Conquest of Azeroth / Conquest Reborn**. It brings together the sources and compatibility findings used to build, update, and maintain the CoA addon lineup, alongside preservation work for useful community data and older projects.

This repository is the research and reference hub. Installable addon builds are published in their individual repositories under [uncle-bone](https://github.com/uncle-bone?tab=repositories); use each addon's README or Releases page for its current download. Research files here are not packaged addon releases, and external data is not assumed to be complete or validated against the live client.

## What this project does

- **Builds and maintains CoA addons.** Research client compatibility, game APIs, class and spell behavior, combat events, UI frameworks, and integrations that support the separately released addon projects.
- **Collects and cross-references game data.** Index public CoA and Ascension sources, preserved spellbooks and tooltips, client data extracts, talent trees, item records, and related archives.
- **Preserves provenance.** Record where information came from, which snapshot or revision it represents, what has been checked, what is missing, and whether it can be redistributed.
- **Turns research into useful tools.** The companion BoneArchive site presents browsable references, planners, audits, and local analysis tools built from selected, attributed datasets.

## Current addon releases

The CoA addons are maintained in separate repositories so each project can publish its own source, release notes, and easy-to-download ZIP. Browse the [addon repositories](https://github.com/uncle-bone?tab=repositories) and use the **Download** link at the top of an addon's README or its [Releases](https://github.com/uncle-bone?tab=repositories) page to get the current build.

Projects in the lineup include [DBM-CoA](https://github.com/uncle-bone/DBM-CoA), [pfQuest-CoA](https://github.com/uncle-bone/pfQuest-CoA) (replacement for discontinued Questie-X), [Details](https://github.com/uncle-bone/Details), [MRT-CoA](https://github.com/uncle-bone/MRT-CoA), [WeakAuras-CoA](https://github.com/uncle-bone/WeakAuras-CoA), [LootCollector](https://github.com/uncle-bone/LootCollector), [AtlasLoot-CoA](https://github.com/uncle-bone/AtlasLoot-CoA), [Cell-CoA](https://github.com/uncle-bone/Cell-CoA), [CoA-Item-Search](https://github.com/uncle-bone/CoA-Item-Search), [Nameplates](https://github.com/uncle-bone/Nameplates), [ElvUI-CoA](https://github.com/uncle-bone/ElvUI-CoA), [Zygor-CoA](https://github.com/uncle-bone/Zygor-CoA), [SilverDragon](https://github.com/uncle-bone/SilverDragon), [UnclePlus-CoA](https://github.com/uncle-bone/UnclePlus-CoA), [Refactor-CoA](https://github.com/uncle-bone/Refactor-CoA), and [BoneUI](https://github.com/uncle-bone/BoneUI). Availability and release status are tracked in each project's own repository.

## What we've gathered

### Classes, spells, talents, and abilities

- A roster covering **21 classes and 70 specialization trees**, with archived talent-tree data containing **3,618 talent nodes** from an identified CoA capture.
- Spell and talent snapshots, specialization references, spell-to-talent relationships, unresolved-spell triage, weapon proficiency checks, and source-priority notes.
- Cross-references between preserved class spellbooks, spell tooltips, CoA talent sources, client DBC/WDB material, public SQL conversions, and the CoA server source.
- Research on custom CoA abilities and Tinker specializations, with candidate mappings clearly marked until supported by client evidence.
- Details-CoA now has a [local client and PTR server-source class/spec research pass](research/DETAILS-COA-CLASS-SPEC-SERVER-SOURCE-2026-11-02.md), including runtime specialization APIs, spell-alias cautions, and source-derived summon ownership leads.

Start with [spell and class research](research/SPELLS-AND-CLASSES.md), the [dataset catalog](research/DATASET-CATALOG.md), and the [spell/talent graph methodology](research/SPELL-TALENT-GRAPH-METHODOLOGY.md).

### Gear, loot, builds, and historical BisBeard data

- Indexed historical BisBeard item and glyph references, phase-specific gear candidates, and class/spec weight profiles.
- Gear and item relationships, eligibility checks, weapon and armor constraints, and audits across phase/spec lists.
- Documentation that distinguishes recovered historical recommendations from verified current best-in-slot results.

See [BisBeard preservation](research/BISBEARD.md), the [data provenance notes](research/BISBEARD-DATA-PROVENANCE.md), and the [latest eligibility audit](research/BIS-ELIGIBILITY-AUDIT-2026-10-30.md).

### Combat logs, raid encounters, and addon engineering

- Research on 3.3.5a combat events, spell ownership, pets and guardians, damage and healing attribution, encounter identification, and DBM timer evidence.
- A generated [22-instance encounter database](datasets/instance-scripts/priority/) and [coverage report](datasets/instance-scripts/priority/coverage-report.json), including source-linked boss-kit candidates and supplemental ScriptDev2 references for Mutanus, Jammal'an, and Ogom. These are public-source candidates, not verified Conquest Reborn mechanics; known source gaps are reported explicitly.
- Details! investigations covering combat-history retention, pet ownership, periodic effects, summons, and accurate DPS/HPS reporting.
- Public Ascension Logs capabilities and permissible API use, plus references to published CoA raid-log findings. Raw logs and bulk third-party history are not presented as downloadable when they are not public or licensed for redistribution.
- Compatibility notes for the default UI, DragonUI, ElvUI, and standalone full UI replacements.

See [combat and addon engineering](research/COMBAT-AND-ADDONS.md), [Ascension Logs research](research/ASCENSIONLOGS.md), and [log archive status](research/LOGS-ARCHIVE-STATUS.md).

### Sources, archives, and collection tools

The [source index](sources/INDEX.md) catalogs official and community repositories, server and client references, converted databases, class research, combat tools, and historic projects. The [archive inventory](archives/INVENTORY.md) records what was supplied, what is only linked, and why large or private files are not mirrored here.

The `tools/` directory contains scripts for collecting and auditing CoA data, building spell catalogs and graphs, resolving source relationships, cross-referencing preserved spellbooks, and importing talent or gear references. The `datasets/` directory separates upstream, collected, normalized, relationship, catalog, and gear data so their origins and transformations remain clear.

## BoneArchive

[BoneArchive](https://coa-research.unclebone.workers.dev/) is the companion research website published from this repository. It turns selected data into a browsable archive and practical research tools, including:

- Class and specialization references, talent-tree browsing, and a build planner with dependency and point-budget checks.
- Spell database and research views linking abilities, talents, sources, and unresolved questions.
- Gear and build references, historical phase candidates, eligibility checks, and provenance notes.
- A local combat-log exploration tool and preserved public performance snapshots, with limitations stated on the site.
- Searchable research documents and source links.

The site is a research companion, not an authoritative live-game database. Archived captures retain their original dates and source attribution; planner output is not automatically verified in-game.

## Start here

| Guide | Contents |
| --- | --- |
| [Source index](sources/INDEX.md) | Public sources, datasets, archives, tools, and addon projects |
| [Dataset catalog](research/DATASET-CATALOG.md) | Indexed datasets, their contents, provenance, and verification status |
| [Spell and class data](research/SPELLS-AND-CLASSES.md) | Spellbook, talents, specializations, and known data gaps |
| [Spell/talent graph methodology](research/SPELL-TALENT-GRAPH-METHODOLOGY.md) | How spell, talent, and specialization relationships are assembled |
| [Combat and addon engineering](research/COMBAT-AND-ADDONS.md) | Details!, MRT, DBM, pets and summons, combat history, and client compatibility |
| [Ascension Logs research](research/ASCENSIONLOGS.md) | Public reports, API capabilities, derived captures, and usage limits |
| [BisBeard preservation](research/BISBEARD.md) | Recovered item, build, and glyph references |
| [Gear eligibility audit](research/BIS-ELIGIBILITY-AUDIT-2026-10-30.md) | Phase/spec candidate validation and constraints |
| [BoneArchive website notes](research/BONEARCHIVE-WEBSITE.md) | Integrated datasets, planner behavior, and site coverage |
| [Archive inventory](archives/INVENTORY.md) | User-provided archives, provenance, and storage constraints |
| [Research rules](research/PROVENANCE.md) | Source conflicts, confidence, licensing, and update workflow |

## Starting sources

[CoA AzerothCore](https://github.com/Conquest-of-AzerothCore/azerothcore-wotlk-coa) · [DealsBeam Ascension DB](https://github.com/DealsBeam/ascension-db) · [CoA preservation data](https://github.com/Bharph/coa-preservation-data) · [CoA Databank](https://github.com/f3rr311/CoA-Databank) · [CoA talents](https://coa-development.org/talents) · [Ascension DB site](https://ascension-db.ascension-archive.workers.dev/) · [Ascension Logs](https://coa.ascensionlogs.gg/).

## Scope, validation, and reuse

- Vanilla, TBC, and Wrath references are in scope, alongside Ascension custom spells, creatures, systems, and class mechanics.
- Addons target Conquest Reborn's **3.3.5a-based** client. Consider the default Blizzard UI, DragonUI, and ElvUI where relevant; independent complete UI replacements are not expected to coexist.
- Prefer observed live-client behavior and combat logs, then verified client data; use historical spellbooks, calculators, server SQL, and archived pages as reference until corroborated.
- A listed or indexed dataset is not necessarily mirrored, complete, current, or validated in-game. Each source has its own caveats and licensing.
- Keep research separate from distributable addon payloads. Preserve third-party license notices and attribution; check source terms before copying or republishing data or code.
- Do not commit credentials, local account details, character data, or private logs.

This is an openly maintained knowledge base for developing, preserving, and improving Conquest Reborn addons and tools. External links can disappear; see the [archive inventory](archives/INVENTORY.md) for preservation status and the [provenance guide](research/PROVENANCE.md) for how findings are tracked.
