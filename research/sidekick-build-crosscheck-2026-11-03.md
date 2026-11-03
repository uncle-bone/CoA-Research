# Ascension Sidekick build and data cross-check

Date: 2026-11-03.

## What was compared

All 70 Ascension Sidekick leveling allocations were matched to BoneArchive class and specialization IDs, then restored through the current talent calculator. The calculator check includes the current node IDs, specialization tab, rank limits, essence limits, and prerequisites. The cross-check also recorded Sidekick’s community ratings, popularity, role, and difficulty as dated third-party reference fields; these fields are not promoted to current CoA facts.

## Findings

- 62 of Sidekick’s 70 allocations restore under the current calculator rules.
- Eight Sidekick paths do not restore cleanly: Templar Crusader has six blocked picks; Necromancer Rime has a rank mismatch on Frozen Power; Pyromancer Draconic has a rank mismatch on Timed Attacks; Cultist Godblade, Corruption, Dreadnought, and Heretic have rank mismatches on Dark Infusion; Venomancer Vizier has a rank mismatch on Advisor’s Perfidy.
- For the seven rank-mismatch cases, an embedded talent allocation from the matching Kami Labs guide was checked against the current calculator. For Templar Crusader, a saved CoA Build Hub community allocation was used instead. All seven alternates and the Crusader fallback restore successfully.
- The resulting site data contains one loadable, source-linked path for every one of the 70 current specializations. These are leveling/community paths, not top-performance claims.
- Sidekick’s public data.js response reports Last-Modified: Thu, 23 Jul 2026 15:43:01 GMT. Its tier, popularity, and difficulty fields are therefore labeled as a historical snapshot. Sidekick describes its own site as a fan-made planning companion and says CoA is pre-meta.
- No Sidekick stat weights or tier values are used to generate gear priorities or performance rankings. Build paths are distinct from gear-stat priorities and measured logs.

## Sources

- [Ascension Sidekick tiers](https://ascensionsidekick.com/tiers) and [specialization build guides](https://ascensionsidekick.com/).
- [Sidekick public data file](https://ascensionsidekick.com/data.js), checked 2026-11-03; Last-Modified header 2026-07-23.
- [Kami Labs Conquest guides](https://kami-labs.fr/en/ascension/), including the seven alternative allocations linked from the site build cards.
- [Preserved CoA Build Hub data](https://github.com/hertigservices/ascension-data/tree/main/supplemental/coa-databank/166001399306e4fb022116fe1e3cfbbd7bd4bf37/coabuildhub/builds).
- Current BoneArchive class trees and calculator in this repository.
