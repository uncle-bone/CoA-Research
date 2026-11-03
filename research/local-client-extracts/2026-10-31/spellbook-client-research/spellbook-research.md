# Conquest Reborn spellbook research

## Scope and evidence
Static scan of `C:\Games\Conquest Reborn\Interface\AddOns` on 2026-11-01. No game runtime inspection was performed. The loose FrameXML implementation for the base client was not found in the AddOns folder; it may be packed in MPQ archives. The installed APIDocumentation files document API names, but do not prove runtime behavior.

## Ascension spellbook pane
The client exposes an Ascension-specific panel named `AscensionSpellbookFrame`, referenced directly by ElvUI and the other installed UI addon code. The panel includes three top tabs, sidebar skill tabs, spell buttons, profession content, pet spell content, page controls, a search edit box, and a show-all-ranks checkbox.

## DragonUI
DragonUI has a 15-file spellbook module loaded from `modules/modules.xml` through `modules/spellbook/spellbook.xml`. The XML loads trainerdata and modules for core, catalog, layout, frame, slots, professions, bars, secure handling, ranks, flyouts, controls, access, and Clique integration.

- `modules/spellbook/book_frame.lua:223` creates `DragonUI_SpellbookFrame`.
- `modules/spellbook/book_access.lua:108-110` detects the Blizzard spellbook and hides `SpellBookFrame`; line 182 hooks `SpellBookFrame.OnShow`.
- `modules/spellbook/book_catalog.lua:117,489-562` enumerates spell tabs and builds catalog sections.
- `modules/spellbook/book_core.lua:255` refreshes on `SPELLS_CHANGED`.
- `modules/spellbook/book_profession.lua:36-48,158` integrates profession spell data and notes that profession learning may not always trigger `SPELLS_CHANGED`.

## ElvUI
ElvUI is present with companion folders `ElvUI_AddOnSkins`, `ElvUI_CoACXtra`, `ElvUI_CoAResources`, `ElvUI_OptionsUI`, and `ElvUI_ProfileInstaller`.

- `ElvUI/Modules/Skins/Blizzard/Spellbook.lua:12-14` conditionally applies the skin based on Blizzard skin settings.
- Lines 15-60 style `AscensionSpellbookFrame`, its tabs, page buttons, close button, rank filter, search edit box, spell icons and cooldowns.
- Lines 69-112 style Ascension sidebar tabs and profession controls; lines 115-126 style pet spell buttons.
- `ElvUI/Modules/Blizzard/WindowMover.lua:16` lists `SpellBookFrame`; line 67 lists `AscensionSpellbookFrame`, making both eligible for repositioning.
- `ElvUI/Libraries/LibSpellRange-1.0/LibSpellRange-1.0.lua:85-101` enumerates skill tabs, reads spell names/ranks, and maps spellbook entries.
- `ElvUI_AddOnSkins/Modules/SkillToast.lua:194-221,271` scans spell tabs and tracks learned spells with `SPELLS_CHANGED` fallback.
- `ElvUI/Modules/Maps/Minimap.lua:46` toggles `AscensionSpellbookFrame`.

## Spellbook APIs/events seen in local code
`GetNumSpellTabs`, `GetSpellTabInfo`, `GetSpellName`, `GetSpellLink`, `GetSpellInfo`, `GetSpellTexture`, `PickupSpell`, `GetSpellCooldown`, `BOOKTYPE_SPELL`, `BOOKTYPE_PET`, and `SPELLS_CHANGED` appear in installed API documentation or addon source. These are source/documentation findings; runtime signatures and return values still need an in-game probe.

## Interaction risk
DragonUI contains a custom book panel and intercepts/hides the standard `SpellBookFrame`; ElvUI styles and moves `AscensionSpellbookFrame` and also knows the standard frame. This establishes overlapping spellbook touchpoints, but not a proven bug. Confirm which frame opens with DragonUI enabled, ElvUI Blizzard skins on/off, and each addon disabled in turn. Record frame visibility, anchors, tab clicks, spell drag/cast, profession and pet pages, rank filtering, search, and spellbook keybind behavior.

## Files scanned
- `DragonUI/modules/spellbook/*.lua`, `spellbook.xml`, `modules/modules.xml`
- `ElvUI/Modules/Skins/Blizzard/Spellbook.lua`
- `ElvUI/Modules/Blizzard/WindowMover.lua`
- `ElvUI/Libraries/LibSpellRange-1.0/LibSpellRange-1.0.lua`
- `ElvUI/Modules/Maps/Minimap.lua`
- `ElvUI_AddOnSkins/Modules/SkillToast.lua`
- `APIDocumentation/Documentation/SpellDocumentation.lua`

## Runtime test status
UNVERIFIED. No actual client UI was opened or instrumented during this scan.
