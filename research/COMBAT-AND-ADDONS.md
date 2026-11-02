# Combat meter and addon development notes

## Target
Ascension Conquest Reborn, WoW 3.3.5a-based client. All classes and specs; vanilla/TBC/WotLK/custom content. Respect base UI, DragonUI and ElvUI. Full UI replacements such as BoneUI can be standalone.

## Details! CoA — priority bugs
- **Combat history loss:** Segments reportedly vanished when zoning, leaving instances (e.g. Headless Horseman), reloading, or fighting a new trash/boss segment. Check segment cleanup, instance transitions, `IsTrash()` filtering, saved segment limit and SavedVariables load path. Do not claim reliable persistence without in-game validation.
- **Pet names / ownership:** Unknown pet names and damage credited incorrectly. Handle `SPELL_SUMMON` source+destination GUID pairs, `UNIT_PET` when possible, guardian/turret events, nil GUIDs, a cached GUID->name->owner relationship, and noisy combat-log name fallbacks. Preserve actual pet ownership rather than reassigning unknowns to an arbitrary actor.
- **Tinker:** Mechanics, Invention and Demolition plus engineering guardians, constructs and periodic effects. Spell mapping requires client evidence.
- **Server ownership leads:** the pinned CoA AzerothCore PTR source declares Tinker owner/owned checks, GUID-tracked summons, pet-cast/summon helpers and device events (`src/server/coa/AscensionTinker.h`). These are useful for designing owner-GUID correlation, but do not prove the combat-log flags or event order delivered to the client. See the [2026-11-02 class/spec/server-source audit](DETAILS-COA-CLASS-SPEC-SERVER-SOURCE-2026-11-02.md).
- **DPS/HPS correctness:** Separate direct damage, pet damage, heals, absorbs and periodic damage. Avoid double-counting or phantom owner attribution.
- **Version:** Earlier local build `Details-CoA-v1.0.3-TEST.zip` was archive integrity checked but **not in-game validated**. That ZIP was a ChatGPT conversation artifact, **not stored in this repo**. The user's [Details repository](https://github.com/downingwow/Details) previously had documentation but not the entire source.

## Client limitations and known errors
- 3.3.5a APIs differ from Retail. Modern `GetCurrentEnvironment`, `CreateVector2D` and libraries relying on them may be unavailable.
- Do not assume stock 3.3.5a spellbook frame/UI when DragonUI or ElvUI changes the visual layer. Scan client spell APIs where supported; use event-driven discovery for truly custom abilities.
- A reliable sharing channel architecture: Questie-X, LootCollector and DBM-CoA share LootCollector's existing default global channel, distinguish messages with separate addon prefixes/protocols, and should not each create or join new channels.
- Keep code modular and memory efficient. Lazy-load optional reference data; avoid full SQL/DBC dumps in Lua.
- Preserve third-party license notices; maintainer branding is **Uncle Bone**, contact https://github.com/downingwow.
- Create Discord-ready release notes for addon updates (under 2,000 characters) ending exactly `:dragon: Uncle Bone :dragon:`.

## Source leads
- [Details repository](https://github.com/downingwow/Details)
- [CoA AzerothCore](https://github.com/Conquest-of-AzerothCore/azerothcore-wotlk-coa)
- [CoAAnalytics](https://github.com/265ada/CoAAnalytics)
- [Community MRT](https://github.com/ArgonautCaptain/Method-Raid-Tools-Ascension-CoA)
- [CoA preservation](https://github.com/Bharph/coa-preservation-data)
