# CoA source index

Last cataloged: 2026-10-29. Dates/counts below describe prior inspections, not a live guarantee of completeness.

## Official and core adjacent
| Source | URL | Research use |
| --- | --- | --- |
| World0fWarcraft GitHub organization | https://github.com/World0fWarcraft | Broad historical Vanilla/TBC/Wrath emulator, 3.3.5a database, WoWDBDefs, packet and development tools catalog; [selected repositories](../research/sources/world0fwarcraft-github-repository-catalog-2026-10-31.json) |
| TrinityCore project | https://www.trinitycore.org/ | Official emulator project documentation and background; historical comparative reference, not CoA authoritative data |
| TrinityCore GitHub (3.3.5 branch) | https://github.com/TrinityCore/TrinityCore/tree/3.3.5 | Compare Vanilla/TBC/Wrath NPCs, spells, quests, instance scripts, world SQL and core APIs against CoA-specific code; [source registration](../research/sources/trinitycore-upstream-335-reference-2026-10-31.json) |
| CoA AzerothCore repository | https://github.com/Conquest-of-AzerothCore/azerothcore-wotlk-coa | C++ core, modules, world SQL, custom mechanics; contains `modules/mod-ascension`, `modules/mod-spellbook`, `data/coa-world`, `src/server` |
| CoA talents | https://coa-development.org/talents | Class/spec talent presentation; test-realm differences possible |
| Ascension DB website | https://ascension-db.ascension-archive.workers.dev/ | Item, spell, NPC and other archived Ascension reference material |
| CoA server manager | https://github.com/Corfirean/coa-server-manager | Server tooling and setup |
| CoA content scaling | https://github.com/Corfirean/mod-coa-content-scaling | Scaling reference |
| CoA playerbots | https://github.com/Corfirean/mod-coa-playerbots | AI classes, combat ability choices |
| Ascension offline source | https://github.com/Duff-SPP/AcensionOfflineDatabase | db.exil.es offline mirror source referenced by SQL converters |
| GitHub CoA discovery query | https://github.com/search?q=conquest+of+azeroth&type=repositories | Broader repository discovery; many forks |

| AzerothHub / Bronzebeard Maps | https://azerothhub.com/ | Bronzebeard-specific zone marker counts and map categories; not validated for CoA; [assessment](../research/sources/azerothhub-bronzebeard-source-assessment-2026-11-01.md) |

## Archived and structured databases
| Repository | URL | Research use |
| --- | --- | --- |
| Ascension SQL conversions | https://github.com/DealsBeam/ascension-db | Seven SQL files, spells/ranks, NPCs, items, quests; see limitations |
| Preserved CoA data | https://github.com/Bharph/coa-preservation-data | Changelogs, spell tooltips, class spellbooks, WDB/client cache records; may use external packs |
| CoA Databank | https://github.com/f3rr311/CoA-Databank | CoABuildHub scrape, DBC/MPQ palette, provenance |
| Ascension data archive | https://github.com/hertigservices/ascension-data | Independent archive / conversion, compare provenance |
| CoA datamine | https://github.com/srhinos/coa-datamine | Client data / DBC investigation; inspect before assuming availability |
| CoA DB tools | https://github.com/codesage24/ConquestOfAzerothDb | Tools for Ascension database |
| Ascension armory | https://github.com/IOUJared/ascension-armory | Gear planning and comparison |
| Ascension Score DB | https://github.com/DungeonV/AscensionScoreDB | Rating / scores |
| CoA Reborn class study | https://github.com/Shadowjp2026/coa-reborn-classes | Class research project; not an authoritative client export |
| CoA talent scrape tools | https://github.com/v1cferr/ascension-coa-scraper | Normalize talent trees into JSON |
| CoA ability extractor lead | https://github.com/johnayoung/coa-arena | Examine exact source and compatibility before accepting extracted ability mappings |

## Historic BisBeard / builds
| Source | URL | Notes |
| --- | --- | --- |
| Discontinued CoA BisBeard | https://coa.bisbeard.com/ | Historical endpoint; availability not guaranteed |
| BisBeard root | https://bisbeard.com/ | Parent website |
| CoA tier list raw captures | https://github.com/Ryansousa10/coa-tier-list/tree/main/tools/data/raw | `bisbeard-items-p1.json`, `bisbeard-items-p2.json`, `bisbeard-meta.json`, combat and rankings captures |
| BisBeard extraction script | https://github.com/Ryansousa10/coa-tier-list/blob/main/tools/scrape/bisbeard.mjs | Historical request/scraping logic |
| BisBeard glyph dataset | https://github.com/kevinvongmany/bisbeard-db | `glyphs_ascension.ts` (observed ~509 KB) |
| BisBuddy | https://github.com/Leemo94/BisBuddy | BisBeard-adjacent tool |
| CoA DPS sim | https://github.com/kaderos/coa-dps-sim | Felsworn Infernal example |

## Combat, raid and UI reference projects
| Project | URL |
| --- | --- |
| CoA Molten Core restoration notes (published evidence from a 54-log live CoA corpus; raw logs excluded from public repo) | https://github.com/Conquest-of-AzerothCore/azerothcore-wotlk-coa/blob/main/docs/coa/molten-core.md#evidence-live-combat-logs |
| Reddit CoA Mythic record-count snapshot (community transcription, Aug 2 2026; not raw reports) | https://www.reddit.com/r/ProjectAscension/comments/1vdlzds/class_statistics/ |
| Reddit Week 1 Molten Core Normal Lucifron class/spec parse counts (Aug 12 2026; source total mismatch is flagged on BoneArchive) | https://www.reddit.com/r/ProjectAscension/comments/1vm1c7o/week_1_molten_core_normal_class_statistics/ |
| Third-party CoA logs tier snapshot (Aug 12 2026; boss-only/AoE DPS, Mythic+, HPS, tank DPS, parse counts) | https://coa.zalidan.com/tier-list-logs/ |
| Reddit community DPS value/tier snapshot (Jul 25 2026; includes exact values, but filter/sample method omitted) | https://www.reddit.com/r/ProjectAscension/comments/1v6itd1/most_recent_dps_statistics_ranking/ |
| Reddit tank intake observations (Jul 25 2026; leveling/dungeon anecdotes) | https://www.reddit.com/r/ProjectAscension/comments/1v6j5ca/coa_tank_damage_intake_profiles/ |
| Reddit high-key tank ranking discussion (Aug 18 2026; self-reported claims) | https://www.reddit.com/r/ProjectAscension/comments/1vrgkde/how_would_you_rank_the_tanks/ |
| Reddit report-comparison discussion (Aug 16 2026; Reave/Wound damage source question) | https://www.reddit.com/r/ProjectAscension/comments/1vpmbqi/bloodmage_accursed_help/ |
| Reddit player rotation recollections (Sep 14 2026; post-shutdown memories, not parsed event sequences) | https://www.reddit.com/r/ProjectAscension/comments/1wgfo2x/what_coa_spec_did_you_play_how_did_it_work/ |
| FangYuanWoW Ascension Logs Uploader / Companion (upload and combatant-metadata tooling; not a public log dump) | https://github.com/FangYuanWoW/ascension-logs-uploader |
| CoA Build Hub community-vote meta announcement (37 builds reported Jul 17 2026; not log-derived) | https://www.reddit.com/r/ProjectAscension/comments/1uz0jox/coa_build_hub_update_meta_tier_list_is_live_37/ |
| Preserved CoA Build Hub scrape mirror (128 identity-stripped builds; captured Jul 31 2026) | https://github.com/hertigservices/ascension-data/tree/main/supplemental/coa-databank/166001399306e4fb022116fe1e3cfbbd7bd4bf37/coabuildhub/builds |
| Method Raid Tools (community CoA) | https://github.com/ArgonautCaptain/Method-Raid-Tools-Ascension-CoA |
| CoAAnalytics | https://github.com/265ada/CoAAnalytics |
| CoA Raid Tool | https://github.com/Voxikai/CoA-Raid-Tool |
| CoACooldownManager | https://github.com/WoloUI/CoACooldownManager |
| CoAInspectTree | https://github.com/WoloUI/CoAInspectTree |
| Tinker utility addon | https://github.com/Minnona/Minn-Tinkers |
| CoA WeakAuras | https://github.com/Zillas/coa-weakauras |
| CoA combat tool | https://github.com/HighOnGames/CoACombat |
| CoA LootCollector community fork | https://github.com/Trollmingo/CoA-LootCollector |
| Questie CoA community | https://github.com/Dandenas/coa-questie |
| CoA UI | https://github.com/Fanatiques/CoA-UI |
| Modern SpellBook CoA | https://github.com/Sleepywalker69/ModernSpellBook-CoA-Ascension |
| CoA Talent Preview | https://github.com/Allerias-Forge/CoATalentPreview |

## User's addon repositories
Maintainer: **Uncle Bone**, GitHub: https://github.com/downingwow

- [Details](https://github.com/downingwow/Details) — combat meter
- [BoneUI](https://github.com/downingwow/BoneUI) — standalone UI replacement
- [SilverDragon](https://github.com/downingwow/SilverDragon) — rare tracking
- [CoA-Research](https://github.com/downingwow/CoA-Research) — this research hub

Other named projects in development: DBM-CoA, MRT-CoA, Questie-X, LootCollector, Zygor-CoA, ElvUI-CoA, FojjiCore-CoA, Leatrix Plus CoA, UncleGPT. Link their exact repositories only after confirmed rather than guessing URLs.
## Community WeakAuras catalog

BoneArchive catalogs 91 public class and specialization pack exports from [JesterCharles/coa-weakauras](https://github.com/JesterCharles/coa-weakauras), last observed Aug 8, 2026. The site stores only the pack manifest and links to the author's export strings and guide pages; it does not mirror the import strings. A second listed project, [Zillas/coa-weakauras](https://github.com/Zillas/coa-weakauras), currently has no public pack files. Compatibility is author-reported and must be checked against the installed client/addon version.

