# CoA historical dataset catalog
Maintainer: Uncle Bone. Updated 2026-11-02.

| Dataset | Source | Contents | Verification |
|---|---|---|---|
| BisBeard comprehensive | https://github.com/hertigservices/ascension-data/tree/main/supplemental/bisbeard | Publisher reports 70,838 item rows / 75 phase-category tables / 37,557 variants; original Dexie and SQLite | Manifest checked, not game validated |
| BisBeard stat weights | https://github.com/Nalhan/Bestow | 70 class/spec profiles and pinned source metadata | Documentation checked; numeric profiles require parsing |
| BisBeard P1/P2 | https://github.com/Ryansousa10/coa-tier-list/tree/main/tools/data/raw | Phase-specific item JSON, metadata | GitHub files listed; coverage unknown |
| Ascension Logs aggregates | https://github.com/Ryansousa10/coa-tier-list/tree/main/tools/data/raw | Stats, rankings, boss metrics, Mythic+ | GitHub files listed; report coverage unknown |
| CoA client datamine | https://github.com/srhinos/coa-datamine | 368 DBC tables, 7,467,710 rows claimed by publisher | Check CoA base-chain vs Free-Pick overlay before joining |
| Late-era spellbooks and balance | https://github.com/Bharph/coa-preservation-data | 21 class spellbooks, ~180,282 tooltips, 70,437 changelog rows | Publisher-described, client snapshot/version caveats |
| CoA tier calculations | https://github.com/Ryansousa10/coa-tier-list | Reproducible community tier formula and data-processing code | Community-derived, not official |

| Armory planner | https://github.com/IOUJared/ascension-armory | Item EP calculations and WDB ingestion | Independent model; not BisBeard canonical BiS |
| Dynamic BiS prototype | https://github.com/lintukellin/chronoforge | Combat/gear recommendation project | Evaluate code and data provenance |

Do not mirror Ascension Logs' bulk data without permission. Preserve source URLs, hashes, phase labels, retrieval dates, methods and permissible derived summaries. Third-party datasets are not automatically licensed for copying.

## Local client and Details research additions

| Dataset | Source | Contents | Verification |
|---|---|---|---|
| [Details-CoA class/spec/server-source package](local-client-extracts/2026-11-02/details-coa-class-spec-research/README.md) | Local Conquest Reborn client installs `C:\Games\Conquest Reborn` and `C:\CoA`; CoA-Research preserved sources; CoA AzerothCore PTR repository at pinned commit | 21-class/70-specialization crosswalk, installed CA and spell-rank data, candidate/summon references, runtime API evidence, second-install hash comparison, PTR active-spec/protocol/spell-alias/Tinker ownership leads | Client files parsed and hashes compared; server notes source-derived, not proof of realm deployment; no MPQs or live combat logs |

## Audits

| BiS eligibility audit | [BIS-ELIGIBILITY-AUDIT-2026-10-30.md](BIS-ELIGIBILITY-AUDIT-2026-10-30.md) | 140 phase/spec lists checked against preserved armor, weapon, shield, dual-wield rules, and local weights | 65 ineligible rows filtered; 1 talent-gated item labeled |
