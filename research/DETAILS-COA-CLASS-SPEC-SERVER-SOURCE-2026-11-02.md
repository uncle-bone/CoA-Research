# Details-CoA class, specialization, and server-source research

Date: 2026-11-02. Target: Conquest Reborn, WoW 3.3.5a / Lua 5.1.

## Added research package

The linked package is a source-labeled companion to existing CoA-Research class, talent, spellbook, and summon datasets. It captures a scan of `C:\Games\Conquest Reborn`, the second client at `C:\CoA`, and a targeted pass over the public CoA AzerothCore/PTR source. It does not inspect or modify the Details addon.

- [Self-contained research ZIP](local-client-extracts/2026-11-02/details-coa-class-spec-research/details-coa-class-spec-research.zip)
- [Class/spec crosswalk](local-client-extracts/2026-11-02/details-coa-class-spec-research/class-spec-coverage.json)
- [Coverage gaps](local-client-extracts/2026-11-02/details-coa-class-spec-research/class-spec-coverage-gaps.json)
- [Client install comparison](local-client-extracts/2026-11-02/details-coa-class-spec-research/client-install-comparison.json)
- [Runtime API evidence](local-client-extracts/2026-11-02/details-coa-class-spec-research/runtime-api-evidence.md)
- [PTR server-source findings](local-client-extracts/2026-11-02/details-coa-class-spec-research/ptr-server-source-findings.md) and [JSON](local-client-extracts/2026-11-02/details-coa-class-spec-research/ptr-server-source-findings.json)

## Key findings

1. CoA-Research's archived roster contains 21 custom class identities and 70 specialization records. The installed client `CharacterAdvancementData.json` contains 23,709 records, 44 distinct raw `Class` strings (including base classes, `Reborn*` namespaces, and sentinels), 28,199 spell links across 21,063 unique spell IDs, and record types Ability, Talent, TalentAbility, Trait, and None. Installed `SpellRankData.json` contains 13,311 rows. These are local static-file counts, not live-server availability counts.
2. Do not report Felsworn, Templar, and Bloodmage as roster conflicts with internal keys DemonHunter, Monk, and SonOfArugal. The existing class identity audit explicitly crosswalks them. Keep display names, client tokens, internal class keys, specialization display names, and internal tab tokens as separate fields.
3. Sixty-three archived specialization rows have an `archivedCadTab` value matching an installed client tab label. Seven have no direct tab mapping in the archived registry: Fleshweaver (25), Warden (45), Valkyrie (47), Mountain King (60), Dreadnought (96), Black Knight (97), and Vizier (101). These are mapping gaps, not proof that the specs are absent. Resolve live state via the client APIs where possible.
4. Shipped CoA client UI code uses `UnitClass("player")`, `C_ClassInfo.GetAllSpecs`, `GetSpecInfo`, `GetSpecInfoByID`, and `C_CharacterAdvancement.GetActiveChrSpec`. The client UI also registers `ASCENSION_CA_SPECIALIZATION_ACTIVE_ID_CHANGED`; read active spec again after the event instead of assuming the event argument is present.
5. The second client folder `C:\CoA` is a client installation (revision 8, `descension-names-20260924`), not the server source checkout. Six checked loose data files are byte-identical to `C:\Games\Conquest Reborn`; see the hash report. MPQs were not extracted.
6. The public [Conquest-of-AzerothCore repository](https://github.com/Conquest-of-AzerothCore/azerothcore-wotlk-coa) contains server-side evidence useful for Details. At inspected commit `9f22d992e39410c6869d1efad6426f0fd2eef081`, its [talent-system notes](https://github.com/Conquest-of-AzerothCore/azerothcore-wotlk-coa/blob/9f22d992e39410c6869d1efad6426f0fd2eef081/.agents/docs/systems/ascension-talents.md) document active-spec storage in `core.ascension_active_spec`, spellbook-derived known talent ranks, internal-token joins, and character-advancement packets. Its [spell-twins notes](https://github.com/Conquest-of-AzerothCore/azerothcore-wotlk-coa/blob/9f22d992e39410c6869d1efad6426f0fd2eef081/.agents/docs/systems/warcraft-reborn-spell-twins.md) describe a stock/Reborn spell-ID offset pattern (+1,100,000) for the spell family under discussion. Treat that as an explicit alias lead, never as a universal arithmetic transform.
7. The repo's [AscensionTinker.h](https://github.com/Conquest-of-AzerothCore/azerothcore-wotlk-coa/blob/9f22d992e39410c6869d1efad6426f0fd2eef081/src/server/coa/AscensionTinker.h) declares GUID-tracked summons, owner/owned checks, pet casts, summon helpers, and device events. It provides server-side ownership leads, but does not establish client combat-log flags, event ordering, or deployment to a particular PTR realm.

## Details integration guidance

- Discover the player's current class from `UnitClass`; feature-detect the CoA specialization APIs and refresh after the specialization-change event.
- Store class identity and spell aliases as provenance-bearing relations. Preserve display and internal tokens separately; do not infer specializations from tree position or IDs alone.
- Do not apply the +1,100,000 spell-ID offset blindly. Add aliases only where the repository's twin criteria or current-client evidence supports a specific pair.
- For summons, track source/owner GUID associations separately from creature template IDs. Keep ambiguous and early-arriving combat events unassigned until ownership evidence exists.
- Mark local client static data as client-derived; CoA-AzerothCore material as server-source-derived; preservation/datamine sources as archived; and name-based candidates as inferred. Source presence does not prove a live PTR deployment or observed combat-log behavior.

## Remaining gaps

- No complete class-by-class/server-script spell or summon extraction has been performed in this addendum.
- No runtime `C_ClassInfo` dump, live PTR build/deployment confirmation, combat-log sample, or summon flag observation was collected.
- The historical unified spell index has 9,656 linked IDs, but its own audit warns archive evidence does not prove current-client behavior.
- MPQ archives were not extracted, and personal SavedVariables were not included.
