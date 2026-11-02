# Installed client runtime evidence

All line numbers refer to files under `C:\Games\Conquest Reborn` and are 1-based. These files show the API calls used by shipped UI code; they do not prove that a third-party addon can access every undocumented API in every build.

- `Interface/AddOns/Ascension_CoATalents/CoASpecViewMixin.lua:4` obtains the player class token with `UnitClass("player")`. Lines 8-15 call `C_ClassInfo.GetAllSpecs(class)` and `C_ClassInfo.GetSpecInfo(class, spec)` to populate the spec selector. Line 26 reads active specialization via `C_CharacterAdvancement.GetActiveChrSpec()`.
- `Interface/AddOns/Ascension_CoATalents/CoATalentFrame.lua:160` obtains the class token. Lines 187-204 read active spec and resolve spec metadata; lines 290-294 do so again for portrait/context.
- `Interface/AddOns/Ascension_CoATalents/CoATreeViewMixin.lua:60-63` maps current class token to the client class DBC. Lines 230-243 resolve spec metadata by ID, get class/spec DBCs, and render the selected tree.
- `Interface/AddOns/WhatsTraining-CoA/ClassRegistry.lua:2-21` contains an explicit 21-token display-name registry; `GetCoAClass()` at lines 11-14 returns `UnitClass` token and display fallback.
- `Data/Content/CharacterAdvancementData.json` is the direct installed static ability/talent/trait source. `Data/Content/SpellRankData.json` is the direct installed spell-rank source.

## Addon-facing recommendation

At runtime, use `select(2, UnitClass("player"))` for the installed class token. Feature-detect `C_CharacterAdvancement.GetActiveChrSpec` and `C_ClassInfo.GetSpecInfoByID`; protect lookups with nil checks and retain unknown IDs. Treat `CharacterAdvancementData` tab labels as build/tree data, not guaranteed specialization IDs. Keep archival spell links as research candidates until a live client or observed log confirms current availability.

## Second installation: `C:\CoA`

`C:\CoA\CLIENT-RELEASE.json` identifies this client as `descension-names-20260924`, revision 8, with `inGameTested: false`. SHA-256 comparison of loose `CharacterAdvancementData.json`, `SpellRankData.json`, `SkillCardData.json`, `WorldMapAreaData.json`, `HandOfFateQuestData.json`, and `LFGData.json` against `C:\Games\Conquest Reborn` found all six byte-identical. The bundle records the hashes in `client-install-comparison.json`; it does not double-count those data.

Additional shipped client event evidence from `C:\CoA\Interface\AddOns\Ascension_CharacterAdvancement\CharacterAdvancement.lua:74,2717` registers and handles `ASCENSION_CA_SPECIALIZATION_ACTIVE_ID_CHANGED`. `C:\CoA\Interface\AddOns\Ascension_CoATalents\CoATalentFrame.lua:173-187,246-247` registers the event and refreshes its active specialization view; the frame handler does not consume the event argument. This is a useful event to feature-detect/observe, alongside reading `C_CharacterAdvancement.GetActiveChrSpec()`.

`C:\CoA` is an installed client folder, not a server-core source checkout: it contains the client executable, interface addons, and MPQ archives. Its release manifest mentions a server prerequisite commit but does not contain those server scripts. No MPQs were extracted.
