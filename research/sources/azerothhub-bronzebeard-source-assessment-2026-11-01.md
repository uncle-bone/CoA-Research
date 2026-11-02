# AzerothHub / Bronzebeard Maps — source assessment (2026-11-01)

Source: https://azerothhub.com/ ; https://azerothhub.com/about ; https://azerothhub.com/zones
Observed site identity: "Bronzebeard Atlas v1.0" / "Bronzebeard Maps", an unofficial fan-made interactive Ascension WoW map companion for the **Bronzebeard realm**.

## Confirmed accessible material (SOURCE-DERIVED; NOT VERIFIED LIVE IN COA)
- Public zone directory for Kalimdor and Eastern Kingdoms; each zone has displayed aggregate counts by marker category.
- Marker types: quest/quest hub, vendor, point of interest, artifact/legendary/epic/rare Mystic Enchant, Worldforge.
- Home/about advertise quest chains, mystic altars, world bosses and rare spawns, but this audit did not obtain verified underlying marker coordinates or detailed quest/NPC/item IDs.
- Selected examples from /zones: The Barrens 298 markers (189 mystic enchants, 109 worldforges); Stranglethorn Vale 295 (2 vendors, 1 POI, 194 mystic enchants, 98 worldforges); Eastern Plaguelands 249 (1 POI, 175 mystic enchants, 73 worldforges); Durotar Valley of Trials 48 (8 quests, 1 vendor, 2 POI, 14 mystic enchants, 23 worldforges); Elwynn Forest Northshire Valley 10 (7 quests, 1 vendor, 2 POI).
- Zone links redirect to /map?zone=...; in text-only inspection, map reports 'Loading Atlas...' and exposes no marker details. **No individual markers, coordinates, NPC IDs, spell IDs, or item IDs were extracted.**

## Compatibility / provenance warning
The site explicitly focuses on **Ascension Bronzebeard**, including classless Mystic Enchants and Worldforge. This is **not evidence that those systems, quests, spawns, or positions exist in Conquest Reborn / Conquest of Azeroth**. Do not import into live CoA Questie-X, LootCollector, DBM-CoA or other runtime databases without independent validation. Zone-count summaries are site statistics, not unique-object guarantees.

## Recommended follow-up
1. Check whether the site offers permitted machine-readable exports, an API, or openly licensed datasets.
2. For any retrieved markers, store source URL, capture date, zone, marker type, coordinates, source-reported ID/name, and verification state; deduplicate by stable identity.
3. Cross-reference against CoA client extracts and in-game observations; label mismatches and realm-specific features.
4. Avoid redistributing bulk third-party content without checking permissions.

Status: **SOURCE-DERIVED website reconnaissance; INCOMPLETE marker-level extraction; UNKNOWN CoA applicability.**
