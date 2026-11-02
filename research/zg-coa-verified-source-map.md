# Zul'Gurub: verified public source map (2026-11-02)

**Evidence level:** files verified present in the public Conquest-of-AzerothCore fork; **NOT** confirmed as the scripts deployed on Conquest Reborn.

## Important finding

The CoA raid-difficulty module contains a separate Ascension-specific implementation. For DBM research, prioritize its boss scripts and SQL mappings over the generic AzerothCore boss scripts, but verify live behavior.

- [CoA Venoxis AI](https://github.com/Conquest-of-AzerothCore/azerothcore-wotlk-coa/blob/main/modules/mod-coa-raid-difficulty/src/boss_venoxis_coa.cpp) — file inspected; comments describe troll-form Holy Nova, Renew, Holy Wrath, Holy Fire, transition near 50% via Avatar of Hethiss, and snake-form abilities. Comments cite combat-log and video-derived timing; **not live verified**.
- [ZG CoA SQL mappings](https://github.com/Conquest-of-AzerothCore/azerothcore-wotlk-coa/blob/main/modules/mod-coa-raid-difficulty/data/sql/db-world/base/14_zg.sql) — file inspected; maps Venoxis NPC 14507 to `boss_venoxis_coa`, Jeklik 14517 to `boss_jeklik_coa`, Mar'li 14510 to `boss_marli_coa`, Thekal 14509 to `boss_thekal_coa`, Arlokk 14515 to `boss_arlokk_coa`; additional mappings should be read from the complete SQL file.
- [Stock Venoxis AI](https://github.com/Conquest-of-AzerothCore/azerothcore-wotlk-coa/blob/main/src/server/scripts/EasternKingdoms/ZulGurub/boss_venoxis.cpp) — present but differs from CoA module implementation.
- [ZG instance script](https://github.com/Conquest-of-AzerothCore/azerothcore-wotlk-coa/blob/main/src/server/scripts/EasternKingdoms/ZulGurub/instance_zulgurub.cpp) — search-confirmed file.
- [ZG shared script](https://github.com/Conquest-of-AzerothCore/azerothcore-wotlk-coa/blob/main/src/server/scripts/EasternKingdoms/ZulGurub/zulgurub.cpp) — search-confirmed file.

## Collection caveat

The collector must include `modules/mod-coa-raid-difficulty/src/` and module SQL. These paths were missing in the initial collector and have now been added. The archive and full encounter index remain **unverified until workflow completion**.
