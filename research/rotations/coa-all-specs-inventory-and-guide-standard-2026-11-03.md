# CR/CoA rotation guide project — Phase 1 verified inventory

Date: 2026-11-03  
Maintainer: Uncle Bone  
Game: Conquest Reborn / Conquest of Azeroth (WoW 3.3.5a, Lua 5.1)

## Verification scope

Parsed `datasets/normalized/coa-class-spec-id-registry.json` from this repository. Registry reports **21 classes, 70 spec records, 70 distinct spec IDs, no missing classes**. This validates consistency of the **archived datamine registry**, not current live realm presence or ability availability. Source registry: `datasets/upstream/coa-datamine/data-classes-specs.json`. Historical naming, talents and spec aliases may differ by patch.

**Seven classes have four recorded specs:** Witch Hunter, Bloodmage, Cultist, Starcaller, Sun Cleric, Venomancer, Primalist. Fourteen classes have three. External community sources disagree between 69 and 70; do not silently delete or invent specs to force a count.

## Complete archived spec inventory

| Class | Archived specs (spec ID) |
|---|---|
| Barbarian | Headhunting (`1`); Brutality (`2`); Ancestry (`3`) |
| Witch Doctor | Shadowhunting (`4`); Voodoo (`5`); Brewing (`6`) |
| Felsworn | Infernal (`7`); Slayer (`8`); Tyrant (`9`) |
| Witch Hunter | Boltslinger (`10`); Houndmaster (`11`); Inquisition (`12`); Black Knight (`97`) |
| Stormbringer | Wind (`13`); Maelstrom (`14`); Lightning (`15`) |
| Knight of Xoroth | Hellfire (`16`); Defiance (`17`); War (`18`) |
| Guardian | Gladiator (`19`); Inspiration (`20`); Vanguard (`21`) |
| Templar | Oathkeeper (`22`); Zealot (`23`); Crusader (`24`) |
| Bloodmage | Fleshweaver (`25`); Sanguine (`26`); Accursed (`27`); Eternal (`99`) |
| Ranger | Archery (`28`); Farstrider (`29`); Brigand (`30`) |
| Chronomancer | Time (`31`); Infinite (`32`); Artificer (`33`) |
| Necromancer | Death (`34`); Animation (`35`); Rime (`36`) |
| Pyromancer | Flameweaving (`37`); Incineration (`38`); Draconic (`39`) |
| Cultist | Heretic (`40`); Corruption (`41`); Godblade (`42`); Dreadnought (`96`) |
| Starcaller | Moon Priest (`43`); Sentinel (`44`); Warden (`45`); Moon Guard (`100`) |
| Sun Cleric | Piety (`46`); Valkyrie (`47`); Seraphim (`48`); Blessings (`98`) |
| Tinker | Demolition (`49`); Mechanics (`50`); Invention (`51`) |
| Venomancer | Fortitude (`52`); Stalking (`53`); Rot (`54`); Vizier (`101`) |
| Reaper | Soul (`55`); Harvest (`56`); Domination (`57`) |
| Primalist | Grovekeeper (`58`); Wildwalker (`59`); Mountain King (`60`); Geomancy (`95`) |
| Runemaster | Engravement (`61`); Glyphic (`62`); Riftblade (`63`) |

## Rotation guide evidence policy

A **rotation** requires more than a list of available abilities. For each specialization verify: source spell ID and localized name; spell effects and coefficients; cast/channel time; GCD; cooldown/charges; resource generation/spend; DoT/HoT duration and pandemic/refresh behavior if supported; procs, talent modifiers, summon interactions; target-count breakpoints; execute thresholds; and role context. Never infer priority from names alone.

### Guide record required fields

- Class ID, spec ID, canonical name, aliases and patch/build scope.
- Role: DPS, tank, healer or support; evidence for role assignment.
- Level range, talent configuration, ability availability and unlock conditions.
- Single-target opener and sustained **conditional priority**.
- 2-target cleave, 3+ AoE, execute and movement adaptations, when supported.
- Burst and defensive cooldown alignment; utility, interrupt and crowd-control use.
- Resource pooling, proc handling, buff/debuff upkeep, summon ownership where applicable.
- Source links, extraction date, confidence and **live-tested status** for each priority rule.
- Outstanding validation questions and recorded test/combat-log evidence.

### Confidence levels

1. **Registry confirmed:** archived class/spec identity only; no gameplay recommendation.
2. **Source candidate:** specific ability/talent mechanics derived from dated client/site/database evidence; not verified live.
3. **Theorycrafted:** proposed priority based on explicit documented mechanics; not benchmarked.
4. **Combat-tested:** observed in current target client with reproducible logs and conditions.
5. **Optimized:** tested comparative performance with talent/gear context and sample limitations.

## Research inputs and limitations

- CoA-Research archived spec registry and spell/talent edges: identity and candidate links, not optimal rotations.
- Bind My Soul Build Forge/Ability Vault/Talent Trees: user-observed site-authored catalog; starter trees labeled heuristic, not live proof. https://bindmysoul.com/?realm=voljin
- Ascension Data / Exiles mirror and DBC snapshots: candidate spell, item, talent and ability details; confirm provenance, patch and realm before joining. https://github.com/hertigservices/ascension-data
- Client-extracted spell data reference: https://github.com/johnayoung/coa-arena ; inspect actual data and build provenance before use.
- Community class/spec atlas: https://github.com/BlakeDonn/coa_classes ; reference only, distinguish heuristic ratings and unverified rotation advice.
- **No combat-log archive confirmed** from Bind My Soul / Ascension Data. Do not fabricate cast cadence, DPS ranking, or optimal priorities.

## Work queue

1. Compare all 70 registry spec IDs/names to fresh in-game/client sources; mark absent, renamed, alias or active. Keep all archived rows for traceability.
2. Build spec-specific ability and talent candidate lists with explicit ID joins and source hashes.
3. Capture actual effect, cooldown, resource and proc data, resolve conflicts.
4. Draft priority rules only for evidence-supported mechanics; mark gaps as unknown rather than guessing.
5. Validate in-game with reproducible single-target and AoE combat logs and relevant gear/talents.
6. Publish 70 independent guides and a versioned machine-readable guide dataset only as each guide meets minimum evidence requirements.

## Current completion

- Archived roster inventory: **complete and internally verified (70/70)**.
- Published-source roster cross-check: **21 classes corroborated by user-observed Bind My Soul live planner; 70 spec IDs confirmed in archived registry**. Individual live-client spec verification: **not established by reviewed evidence**.
- Mechanics/rotation verification: **pending**.
- Combat-tested or optimized guides: **0 claimed**.

This is a research inventory and guide specification, **not** a claim that 70 rotations have been authored or validated.
