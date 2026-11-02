# PTR server repository findings for Details-CoA

Repository: [Conquest-of-AzerothCore/azerothcore-wotlk-coa](https://github.com/Conquest-of-AzerothCore/azerothcore-wotlk-coa)
Inspected branch snapshot: `main` at `9f22d992e39410c6869d1efad6426f0fd2eef081` (2026-11-02 UTC). Source presence does not prove deployment to a live or PTR realm.

## Useful findings

- The repository's [CoA talent-system notes](https://github.com/Conquest-of-AzerothCore/azerothcore-wotlk-coa/blob/9f22d992e39410c6869d1efad6426f0fd2eef081/.agents/docs/systems/ascension-talents.md) describe active spec storage in `core.ascension_active_spec`, learned ranks derived from `character_spell`, and specialization catalog joins through internal tokens rather than display names.
- The notes describe the client deriving active specialization from specialization identity entries in the build; active-slot packet state is separate from the specialization itself. They document `SMSG 0x0725` for active slot/capacity, `SMSG 0x0726` for complete known-entry state, and `ASCENSION_CA_SPECIALIZATION_ACTIVE_ID_CHANGED` as a client refresh signal. These are valuable design leads; an addon should query the client API after the event rather than parse network packets.
- The [spell-twins notes](https://github.com/Conquest-of-AzerothCore/azerothcore-wotlk-coa/blob/9f22d992e39410c6869d1efad6426f0fd2eef081/.agents/docs/systems/warcraft-reborn-spell-twins.md) document a stock/Reborn spell alias pattern of stock ID + 1,100,000 for the described family. Do not apply this arithmetically to all spells; retain explicit alias rows and evidence.
- [AscensionTinker.h](https://github.com/Conquest-of-AzerothCore/azerothcore-wotlk-coa/blob/9f22d992e39410c6869d1efad6426f0fd2eef081/src/server/coa/AscensionTinker.h) has server-side ownership/summon state (`Owner`, `Owned`, GUID-tracked summons, `PetCast`, `Summon`, `DeviceEvent`). That can guide summon-attribution logic, but source declarations do not establish client combat-log flags or deployed behavior.
- [Tinker source reconstruction](https://github.com/Conquest-of-AzerothCore/azerothcore-wotlk-coa/blob/9f22d992e39410c6869d1efad6426f0fd2eef081/docs/coa/tinker-completion.md) explicitly distinguishes source changes and bounded offline checks from in-game acceptance.

## What remains

This was a targeted PTR source pass, not a complete inventory of every class file. The full class/spec spell and summon matrix still needs systematic extraction from `src/server/coa`, client DBC/catalog data, and SQL migrations. Confirm whether the inspected commit is deployed to the target PTR realm before labeling anything runtime-verified. Do not infer combat-log flags from server ownership code alone.

Machine-readable records and confidence labels are in `ptr-server-source-findings.json`.
