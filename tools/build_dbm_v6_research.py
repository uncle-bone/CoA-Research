#!/usr/bin/env python3
"""Build the DBM-CoA v6 evidence-first research package from checked-in sources.

This generator deliberately preserves candidate/unknown states. It does not
promote upstream scripts or database rows to live Conquest Reborn facts.
Run from the CoA-Research repository root:
  python tools/build_dbm_v6_research.py
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "dbm" / "v6"
DBM_HEAD = "ba9d91fb44dbd26d2755682279962a5cfe407787"
RESEARCH_HEAD = "acff72745a107407812e76ddea4efffbef844f71"
RETRIEVED = "2026-11-03"


def read(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def write_json(name: str, data):
    (OUT / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    coverage = read("datasets/instance-scripts/priority/coverage-report.json")
    inventory = read("datasets/instance-scripts/source-inventory.json")
    custom = read("research/dbm/custom-dungeons-canonical-v1-2026-10-30.json")
    seven = [
        ("manastorm", "Manastorm", "mode-or-progression-system", None),
        ("shadowbone-depths", "Shadowbone Depths", "custom-instance", None),
        ("temple-of-embers", "The Temple of Embers", "custom-instance", None),
        ("radiant-spring", "The Radiant Spring", "custom-instance", None),
        ("road-to-the-other-side", "Road to the Other Side", "custom-instance", 937),
        ("vaults-of-inquisition", "Vaults of Inquisition", "custom-instance", 936),
        ("blackrock-caverns", "Blackrock Caverns", "custom-instance", None),
    ]
    references = {
        "manastorm": ["research/dungeons/manastorm-dungeon-cache-mappings-all-modes-2026-10-30.json", "research/dbm/dungeon-research-consolidation-2026-10-30.md"],
        "shadowbone-depths": ["research/dbm/shadowbone-depths-source-dossier-2026-10-30.md", "research/dbm/shadowbone-depths-consolidated-gap-analysis-2026-10-30.md", "research/dbm/shadowbone-depths-quest-chain-evidence-audit-2026-10-30.md"],
        "temple-of-embers": [],
        "radiant-spring": ["research/dbm/atlasloot-coa-authoritative-content-scope-2026-10-30.json"],
        "road-to-the-other-side": ["research/dbm/road-to-de-other-side-three-boss-source-audit-2026-10-30.md", "research/dbm/road-to-de-other-side-phase-timelines-v1-2026-10-30.json", "research/dbm/road-to-de-other-side-sql-difficulty-fixes-2026-10-30.md", "research/dbm/road-boss-complete-scheduling-and-spell-index-2026-10-30.json"],
        "vaults-of-inquisition": ["research/dbm/vaults-of-the-inquisition-three-boss-source-audit-2026-10-30.md", "research/dbm/vaults-complete-mechanics-source-evidence-2026-10-30.json", "research/dbm/vaults-instance-difficulty-sql-index-2026-10-30.json"],
        "blackrock-caverns": ["datasets/instance-scripts/priority/blackrock-caverns.json"],
    }
    seven_records = []
    for slug, name, kind, map_id in seven:
        cov = coverage["instances"].get(slug, {})
        boss_records = []
        source_paths = []
        extra_evidence = {}
        source_revs = {}
        if slug == "blackrock-caverns":
            data = read("datasets/instance-scripts/priority/blackrock-caverns.json")
            for encounter in data.get("encounters", {}).values():
                boss_records.append({"key": encounter["name"], "name": encounter["name"].replace("boss_", "").replace("_", " ").title(), "npc_id": None, "evidence": encounter.get("evidence"), "live_verified": False, "source_paths": encounter.get("source_paths", [])})
            for source in data.get("source_files", []):
                source_paths.append({"repository": source.get("repository"), "revision": source.get("revision"), "path": source.get("path"), "kind": source.get("kind"), "evidence": source.get("evidence"), "live_verified": False})
        elif slug == "road-to-the-other-side":
            entry = next(x for x in custom["dungeons"] if x["mapId"] == 937)
            boss_records = [{"name": b["name"], "npc_id": b.get("npcId"), "difficulty_npc_ids": {"heroic": b.get("heroicNpcId"), "mythic": b.get("mythicNpcId")}, "mechanics_source": b.get("source"), "timing_record": b.get("timeline"), "evidence": "historical-upstream-source-derived", "live_verified": False} for b in entry.get("bosses", [])]
            schedule = read("research/dbm/road-boss-complete-scheduling-and-spell-index-2026-10-30.json")
            extra_evidence = {"source_schedule_index": schedule, "warning": "NPC/spell constants are source-index evidence; do not assume every defined constant is cast in every difficulty."}
        elif slug == "vaults-of-inquisition":
            entry = next((x for x in custom["dungeons"] if x.get("mapId") == 936), None)
            if entry:
                boss_records = [{"name": b["name"], "npc_id": b.get("npcId"), "difficulty_npc_ids": {"heroic": b.get("heroicNpcId"), "mythic": b.get("mythicNpcId")}, "mechanics_source": b.get("source"), "mechanics": b.get("mechanics", []), "evidence": "historical-upstream-source-derived", "live_verified": False} for b in entry.get("bosses", [])]
            extra_evidence = {"mechanics_source_index": read("research/dbm/vaults-complete-mechanics-source-evidence-2026-10-30.json"), "spell_binding_index": read("research/dbm/vaults-full-spell-sql-and-cpp-index-2026-10-30.json"), "warning": "Constants and SQL bindings are candidates; verify exact runtime cast paths, difficulty and deployment before DBM use."}
        elif slug == "shadowbone-depths":
            extra_evidence = {"quest_id_candidate": 175126, "quest_name": "Shadowbone Depths", "quest_target_name": "Morgwena", "quest_target_npc_id": None, "quest_giver": {"name": "Deirdre", "npc_id": 164355, "role": "quest giver/ender; not a verified boss"}, "boss_roster": "unknown", "map_id": None, "availability": "public roadmap snapshot said coming/in progress on 2026-10-30; current launch state not verified", "source_note": "Quest SQL and narrative establish a dungeon quest target, not a boss creature ID or mechanics."}
        elif slug == "radiant-spring":
            extra_evidence = {"source_note": "Name appears in an AtlasLoot content-scope record based on user-provided screenshot; no boss/instance data in inspected source corpus."}
        # Preserve the exact source inventory lineages for this instance when available.
        for rec in inventory.get("files", []):
            p = rec.get("path", "")
            tokens = [slug.replace("-", "_")]
            if slug == "blackrock-caverns":
                tokens.append("blackrockcaverns")
            if any(token in p.lower() for token in tokens):
                source_paths.append({"repository": rec.get("source"), "revision": rec.get("revision"), "path": p, "kind": rec.get("kind"), "live_verified": False})
        status = "source-candidates-found" if cov.get("source_files", 0) or boss_records else "no-instance-script-evidence-indexed"
        if slug == "shadowbone-depths":
            status = "quest-and-narrative-source-evidence; encounter identity unresolved"
        if slug == "radiant-spring":
            status = "name-only-content-scope-evidence; encounter evidence absent"
        if slug == "manastorm":
            status = "mode-and-reward-system-evidence; do-not-model-as-a-distinct-instance-without-map-evidence"
        seven_records.append({
            "id": slug, "name": name, "kind": kind, "map_id_candidate": map_id,
            "map_id_status": "candidate-needs-client-or-server-map-confirmation" if map_id else "unknown",
            "release_status": "unverified-in-live-client", "live_verified": False,
            "source_status": status, "coverage": cov, "bosses": boss_records,
            "additional_evidence": extra_evidence,
            "source_references": references[slug], "source_files": source_paths,
            "spell_ids": "not normalized into verified per-boss spell links",
            "difficulty_ids": "not independently reconciled for live Conquest Reborn",
            "timers_verified": False,
            "limitations": ["Historical/public source is not proof of current deployment.", "Do not enable predictive timers until the exact boss/spell/difficulty is corroborated by live logs or a verified deployed revision."]
        })
    write_json("PRIORITY-SEVEN-DUNGEONS.json", {"schema": "dbm-coa-v6-priority-seven-v1", "generated": RETRIEVED, "evidence_policy": "source-derived candidates remain distinct from live verification", "dungeons": seven_records})

    registry = []
    for slug, c in coverage["instances"].items():
        file_path = f"datasets/instance-scripts/priority/{slug}.json"
        data = read(file_path) if (ROOT / file_path).exists() else {}
        registry.append({"id": slug, "name": data.get("instance", slug.replace("-", " ").title()), "kind": "dungeon-or-raid-source-corpus-entry", "map_id": None, "module_status": "inspect-native-module-before-claiming-coverage", "source_evidence": c, "source_dataset": file_path, "live_verified": False, "availability": "unverified"})
    # Add custom entries not represented by the 22-instance source-corpus slice.
    known = {x["id"] for x in registry}
    for slug, name, kind, map_id in seven:
        if slug not in known:
            registry.append({"id": slug, "name": name, "kind": kind, "map_id": map_id, "module_status": "unknown", "source_evidence": {}, "source_dataset": None, "live_verified": False, "availability": "unverified"})
    write_json("INSTANCE-REGISTRY.json", {"schema": "dbm-coa-v6-instance-registry-v1", "generated": RETRIEVED, "scope_note": "22 rows derive from the priority source archive; this is not a complete supported-instance census", "instances": registry})

    bosses = []
    mechanics = []
    timings = []
    source_map = []
    for slug, c in coverage["instances"].items():
        path = ROOT / f"datasets/instance-scripts/priority/{slug}.json"
        if not path.exists():
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        for source in data.get("source_files", []):
            source_map.append({"instance": slug, "repository": source.get("repository"), "revision": source.get("revision"), "path": source.get("path"), "kind": source.get("kind"), "evidence": source.get("evidence"), "live_verified": False})
        for key, boss in data.get("encounters", {}).items():
            bosses.append({"record_id": f"{slug}:{key}", "instance": slug, "name": boss.get("name"), "npc_id": boss.get("npc_id_candidate"), "npc_ids_candidate": boss.get("npc_ids_candidate", []), "evidence": boss.get("evidence"), "source_paths": boss.get("source_paths", []), "live_verified": False})
            for sid in boss.get("spell_ids_candidate", []):
                mechanics.append({"record_id": f"{slug}:{key}:{sid}", "instance": slug, "boss_key": key, "npc_id": None, "spell_id": sid, "mechanic": None, "evidence": "candidate-id-from-source-index", "live_verified": False, "warning_eligible": False})
        for sf in data.get("source_files", []):
            source_path = sf.get("path")
            filename = Path(source_path or "").stem
            boss_key = filename if filename.startswith("boss_") else None
            for sid in sf.get("spell_ids_candidate", []):
                mechanics.append({"record_id": f"{slug}:{source_path}:{sid}", "instance": slug, "boss_key": boss_key, "npc_id": None, "spell_id": sid, "mechanic": None, "source_repository": sf.get("repository"), "source_revision": sf.get("revision"), "source_path": source_path, "evidence": "candidate-id-extracted-from-source-file; spell effect/cast/instance-use unresolved", "live_verified": False, "warning_eligible": False})
            for sig in sf.get("timer_expression_candidates", []):
                timings.append({"instance": slug, "source_path": source_path, "repository": sf.get("repository"), "revision": sf.get("revision"), "expression": sig.get("expression") if isinstance(sig, dict) else sig, "semantics": "unclassified-source-expression", "live_verified": False, "prediction_eligible": False})
    # Road to the Other Side has per-boss source indexes in the custom dossier.
    road = read("research/dbm/road-boss-complete-scheduling-and-spell-index-2026-10-30.json")
    for boss in road.get("bosses", []):
        npc_ids = [v for k, v in boss.get("npcConstants", {}).items() if k.startswith("NPC_") and isinstance(v, int)]
        for symbol, sid in boss.get("spellConstants", {}).items():
            if isinstance(sid, int):
                mechanics.append({"record_id": f"road-to-the-other-side:{boss['boss']}:{sid}:{symbol}", "instance": "road-to-the-other-side", "boss_name": boss["boss"], "npc_id_candidates": npc_ids, "spell_id": sid, "source_symbol": symbol, "mechanic": None, "evidence": "historical-source-index-constant; exact runtime use/difficulty requires review", "live_verified": False, "warning_eligible": False})
        for expr in boss.get("schedulingCalls", []):
            timings.append({"instance": "road-to-the-other-side", "boss_name": boss["boss"], "source_path": boss.get("source"), "expression": expr, "semantics": "source-scheduling-expression-not-normalized", "live_verified": False, "prediction_eligible": False})
    vault = read("research/dbm/vaults-complete-mechanics-source-evidence-2026-10-30.json")
    for symbol, sid in vault.get("spellConstants", {}).items():
        if isinstance(sid, int):
            mechanics.append({"record_id": f"vaults-of-inquisition:{sid}:{symbol}", "instance": "vaults-of-inquisition", "spell_id": sid, "source_symbol": symbol, "npc_id_candidates": [], "mechanic": None, "evidence": "historical-source-constant; per-boss association and runtime use unresolved", "live_verified": False, "warning_eligible": False})
    vault_dossier = next(x for x in custom["dungeons"] if x.get("mapId") == 936)
    for boss in vault_dossier.get("bosses", []):
        for ability in boss.get("mechanics", []):
            sid = ability.get("spellId")
            if sid:
                mechanics.append({"record_id": f"vaults-of-inquisition:{boss['name']}:{sid}", "instance": "vaults-of-inquisition", "boss_name": boss["name"], "npc_id": boss.get("npcId"), "spell_id": sid, "mechanic": ability.get("name"), "source_timing_fields": {k: v for k, v in ability.items() if k.endswith("Ms") or k.endswith("Pct")}, "evidence": "historical-source-derived-dossier; verify against exact source/deployment", "live_verified": False, "warning_eligible": False})
            timings.append({"instance": "vaults-of-inquisition", "boss_name": boss["name"], "npc_id": boss.get("npcId"), "spell_id": sid, "mechanic": ability.get("name"), "source_timing_fields": {k: v for k, v in ability.items() if k.endswith("Ms") or k.endswith("Pct")}, "semantics": "source-dossier-field-semantics-not-independently-replayed", "live_verified": False, "prediction_eligible": False})
    write_json("BOSS-REGISTRY.json", {"schema": "dbm-coa-v6-boss-registry-v1", "generated": RETRIEVED, "records": bosses})
    write_json("SPELL-MECHANICS.json", {"schema": "dbm-coa-v6-spell-mechanics-v1", "generated": RETRIEVED, "warning": "IDs are source candidates; no inferred spell-to-boss certainty", "records": mechanics})
    write_json("ENCOUNTER-TIMINGS.json", {"schema": "dbm-coa-v6-timing-evidence-v1", "generated": RETRIEVED, "warning": "Raw expressions are not normalized timer values; never create timers from this file", "records": timings})
    write_json("INSTANCE-SOURCE-MAP.json", {"schema": "dbm-coa-v6-source-map-v1", "generated": RETRIEVED, "records": source_map})
    difficulty_rows = []
    for row in seven_records:
        for boss in row.get("bosses", []):
            for label, npc_id in (boss.get("difficulty_npc_ids") or {}).items():
                if npc_id:
                    difficulty_rows.append({"instance": row["id"], "boss": boss.get("name"), "difficulty_label_candidate": label, "difficulty_id": None, "npc_id_candidate": npc_id, "evidence": "historical-source-dossier", "live_verified": False})
        if row["id"] == "road-to-the-other-side":
            # Map-level supported mode labels have not been converted to client difficulty IDs.
            difficulty_rows.extend({"instance": row["id"], "difficulty_label_candidate": label, "difficulty_id": None, "evidence": "source dossiers mention mode-specific NPC/spell variants", "live_verified": False} for label in ["normal", "heroic", "mythic"])
    write_json("DIFFICULTY-MATRIX.json", {"schema": "dbm-coa-v6-difficulty-matrix-v1", "generated": RETRIEVED, "policy": "difficulty IDs and variants require instance-specific evidence; generic 0-3 labels are not accepted as proof", "instances": [{"instance": r["id"], "map_id": r.get("map_id"), "difficulty_rows": [x for x in difficulty_rows if x["instance"] == r["id"]], "status": "source-label-candidates-only" if any(x["instance"] == r["id"] for x in difficulty_rows) else "unresolved", "live_verified": False} for r in registry]})

    module_files = []
    for folder in ("DBM-Party-Vanilla", "DBM-Party-BC", "DBM-ZG", "DBM-CoA-Learner"):
        base = ROOT.parent / "work" / "DBM-CoA-current" / folder
        if base.exists():
            for f in base.rglob("*.lua"):
                text = f.read_text(encoding="utf-8", errors="replace")
                if "DBM:NewMod" in text:
                    module_files.append(str(f.relative_to(ROOT.parent / "work" / "DBM-CoA-current")).replace("\\", "/"))
    write_json("DBM-MODULE-COVERAGE.json", {"schema": "dbm-coa-v6-native-module-inventory-v1", "dbm_repository": "https://github.com/uncle-bone/DBM-CoA", "dbm_head": DBM_HEAD, "files_with_newmod_in_party_zg_learner_scopes": len(module_files), "inventory_scope": ["DBM-Party-Vanilla", "DBM-Party-BC", "DBM-ZG", "DBM-CoA-Learner"], "module_source_files": module_files, "custom_priority_status": {x[0]: "no_verified_native_boss_module_established_by_this_research_pass" for x in seven}, "note": "File-level NewMod scan is an inventory aid, not a proof that every registration, localization, TOC inclusion, or GUI category is correct. Re-running the generator requires the pinned DBM-CoA checkout at ../work/DBM-CoA-current; otherwise this inventory will be empty."})

    provenance = {
        "schema": "dbm-coa-v6-provenance-v1", "generated": RETRIEVED,
        "repositories": [
            {"repository": "uncle-bone/CoA-Research", "url": "https://github.com/uncle-bone/CoA-Research", "revision": RESEARCH_HEAD, "retrieval_date": RETRIEVED, "status": "checked-in research baseline"},
            {"repository": "uncle-bone/DBM-CoA", "url": "https://github.com/uncle-bone/DBM-CoA", "revision": DBM_HEAD, "retrieval_date": RETRIEVED, "status": "default-branch source checkout; no production files changed"},
            *coverage.get("source_statuses", [])
        ],
        "evidence_classes": ["live-verified", "source-verified", "historical", "inferred", "unresolved"],
        "rule": "Repository source revisions identify where evidence was found; they do not establish deployment in the live Conquest Reborn realm."
    }
    write_json("SOURCE-PROVENANCE.json", provenance)
    write_json("DBM-MODULE-COVERAGE.json", {**json.loads((OUT / "DBM-MODULE-COVERAGE.json").read_text()), "module_source_files": module_files})

    (OUT / "MASTER-RESEARCH-REPORT.md").write_text(f"""# DBM-CoA v6 research baseline\n\nGenerated {RETRIEVED}. This is an evidence-indexing baseline built from checked-in CoA-Research sources and the inspected DBM-CoA default-branch checkout. It is **not** a claim that v6 is complete or that source candidates match live Conquest Reborn.\n\n## Inputs pinned for this pass\n\n- CoA-Research: `{RESEARCH_HEAD}`.\n- DBM-CoA: `{DBM_HEAD}`. The fetched repository reports addon version 5.2.24 in `DBM-CoA-Learner/DBM-CoA-Learner.toc`; README text still describes stable v5.2.23, while `.release.json` marks v5.2.24 prerelease. Those are metadata states, not release verification.\n- Priority instance source corpus: `datasets/instance-scripts/priority/coverage-report.json` (22 instance entries, source archives collected from six upstream repositories plus the then-current CoA-Research snapshot). It explicitly says findings are not live verified.\n\n## Key finding\n\nThe assignment's priority seven are not seven equally evidenced dungeon modules. Road to De Other Side (source alias: “Road to De Other Side”, map candidate 937) and Vaults of the Inquisition (map candidate 936) have source-derived boss dossiers; Blackrock Caverns has five TrinityCore filename candidates and candidate IDs, not CoA-confirmed implementation. Shadowbone Depths has a dossier and explicit gaps. Manastorm evidence is primarily a reward/mode system and must not be modeled as a distinct instance without map/instance evidence. The inspected research pass did not find boss-script evidence for The Temple of Embers or The Radiant Spring; the latter appears in a user-provided content-scope list only.\n\n## Seven-dungeon status\n\n| Target | Research state | Live status | Safe DBM use now |\n|---|---|---|---|\n""" + "\n".join(f"| {x['name']} | {x['source_status']} | Unverified | Detection-only only after map/name confirmation; no speculative boss timers |" for x in seven_records) + f"""\n\n## Existing 22-instance source corpus\n\n`INSTANCE-REGISTRY.json` carries all 22 entries from the checked-in priority archive. This is not the complete instance roster demanded by the assignment. `DBM-MODULE-COVERAGE.json` is a source-file inventory aid and must be reconciled against each module TOC, localization, `DBM:NewMod`, event registration, map ID and GUI category before claiming module coverage. The live-support state of every row is unresolved.\n\n## DBM architecture observations (DBM-CoA {DBM_HEAD})\n\n- Native instance modules use `DBM:NewMod(...)` inside existing module folders; the current Vanilla/TBC party modules already group instance encounters by native subcategory. v6 should follow this loader and GUI pathway, not introduce a parallel encounter UI.\n- `DBM-CoA-Learner/DBM-CoA-Learner.toc` declares interface 30300, dependency `DBM-Core`, SavedVariables `DBMCoALearnerDB`, and explicitly lists each research/learning Lua file. A new data-driven module needs TOC inclusion and unique module IDs; folder creation alone is insufficient.\n- `Classic19CastWarnings.lua` and `Classic19SourceTimers.lua` subscribe to `COMBAT_LOG_EVENT_UNFILTERED` and area/instance-change events. The source timers track NPC/spell observations and consult stock indexes; timings from public source should remain behind explicit evidence gates.\n- `LiveLearning.lua` gates learning to hostile NPC GUID/flags, groups observations by zone/type/difficulty, and uses sample-count/outlier rules. This is discovery evidence, not a guarantee of encounter identity or timer accuracy.\n- `SourceTimerEngine.lua` uses native `DBM.Bars:CreateBar`, skips NPC/spell entries already in the stock timer index, and checks the opt-in source-timer SavedVariable. Keep native bars and duplicate suppression. Audit its event scheduling and timer cancellation before expanding it.\n- `SmartSync3.lua` is namespaced `DCOAS3`, targets `CoASync`, bounds pending packets, validates record shape and keeps legacy protocols separate. Preserve wire formats and SavedVariables; test peers with real WoW 3.3.5a event arguments.\n- `DBM-Core/DBM-Core.lua` owns `DBM:StartCombat`, `DBM:EndCombat`, mod creation and difficulty helper behavior; encounter modules should invoke native APIs rather than create their own boss panel or tree.\n\n## Timing policy\n\nUse the priority chain in `DBM-V6-IMPLEMENTATION-SPEC.md`: verified existing DBM timer; timing from an identified server-source revision (experimental until deployment is established); repeated live combat observations; high-confidence learned estimate; otherwise no bar. Preserve ranges and conditions. Do not turn SQL fields or C++ schedule expressions into exact countdowns without matching semantics, cast completion behavior, phase, difficulty, and reset logic.\n\n## Unresolved completeness\n\nThe full instance inventory, complete custom-instance rosters, CoA-specific spell mappings, deployed server revision, live combat evidence, exact difficulty behavior, and live compatibility/performance checks remain open. See `UNRESOLVED-RESEARCH-GAPS.md`.\n""", encoding="utf-8")

    (OUT / "DBM-V6-IMPLEMENTATION-SPEC.md").write_text("""# DBM-CoA v6 native implementation specification\n\n## Non-negotiable integration rules\n\n1. Use `DBM:NewMod` in existing native module packages and subcategories. Do not add a second encounter UI, tree, profile/settings layer, or timer anchor.\n2. Keep one authoritative module per encounter/difficulty identity. New modules must have unique IDs, localization entries, TOC inclusion, correct map IDs, and explicit NPC start/death/combat-end signals.\n3. Reconcile difficulty from the actual CoA client/server data for each instance. Never map generic raid difficulty integers to custom modes by assumption.\n4. Preserve existing modules and SavedVariables. Add migrations only when a schema change is required and tested.\n5. Native DBM bars/warnings only. Event-driven parsing, bounded per-encounter state, clear cancellation on wipe/zone exit, and no periodic world scans.\n\n## Module file contract\n\nFor each encounter: `DBM:NewMod(stableUniqueId, packageId, nativeSubcategory)`; localization for display name and warning/timer options; `mod:SetCreatureID(...)`; `mod:RegisterEventsInCombat(...)`; `mod:StartCombat(...)` through native combat detection; `mod:EndCombat(...)` through death/encounter signals; warning and timer calls through core APIs. Add file paths to the package TOC in load-safe order. Confirm the DBM GUI enumerates the native mod category after loading.\n\n## Evidence-gated warnings\n\n- Cast warning requires a spell ID tied to the exact hostile boss NPC and a specific source/live evidence record.\n- Target warning additionally requires verified target selection semantics.\n- Interrupt/dispel/movement advice requires a verified effect and actionable response.\n- Trash mechanics are opt-in research until source attribution and live encounter relevance are confirmed.\n\n## Timer arbitration\n\nKey timer ownership by `(instance/map, encounter/module, boss NPC, spell, phase, difficulty)`. Precedence: existing verified native module > live-verified fixed/ranged mechanic > source-verified candidate explicitly marked experimental > high-confidence learner estimate > none. Never schedule a duplicate bar for the same key. On cast, correct/cancel the prior prediction and schedule only if timing semantics establish the next occurrence. Cancel on phase transition, reset, death, wipe, leaving instance, or difficulty change. Variable source ranges remain ranges; if DBM bar APIs cannot represent uncertainty honestly, use cast-based warning without a countdown.\n\n## Learning fallback\n\nLearning records raw source/destination GUID, flags, NPC, spell, event subtype, map, difficulty, timestamp and encounter context. Keep source observations separate from normalized encounter records. Require hostile NPC classification, exclude player-controlled pets/guardians, cap state and sample history, use robust statistics and outlier rejection, and show no timer until threshold/confidence is met. Do not use synthetic fixtures as encounter truth.\n\n## SmartSync v3\n\nKeep DCOAS3 and legacy handlers/wire formats compatible. Validate channel number and both plain/decorated CoASync names using WoW 3.3.5a event arguments. Bound queues, packet size and processing per frame; deduplicate records without conflating identity; reject malformed data; preserve old SavedVariables; and keep chat quiet. Never synchronize code or raw combat logs.\n\n## Implementation gate per module\n\nA boss module can be marked production-ready only when: exact map and difficulty; source-backed or live boss identity; localized native module registration; verified event lifecycle; spell-to-boss ties; warning semantics; timer semantics/cancellation; duplicate arbitration; test fixtures; TOC validation; Lua 5.1 parse; install ZIP check; and in-game confirmation are recorded. Otherwise ship detection/research-only behavior or leave it out.\n""", encoding="utf-8")

    (OUT / "LEARNER-AND-SMARTSYNC-AUDIT.md").write_text("""# Learner and SmartSync audit — DBM-CoA source snapshot\n\n**DBM-CoA revision inspected:** `ba9d91fb44dbd26d2755682279962a5cfe407787` (default branch, fetched 2026-11-03).\n\n## Learner flow observed in source\n\n- `Classic19CastWarnings.lua` and `Classic19SourceTimers.lua` observe combat-log cast events; zone/instance transitions clear local state.\n- `LiveLearning.lua` accepts hostile creature/vehicle sources, rejects player-pet GUIDs and non-hostile/player-controlled flags, keys records by zone/type/difficulty/NPC/spell, and only derives an interval after at least three clustered samples. Its boundaries/outlier checks are heuristics requiring regression coverage.\n- `EncounterEngine.lua` records context from `GetInstanceInfo`; it is adaptive observation/diagnostics, not proof that it can name every encounter.\n- `SourceTimerEngine.lua` reads source ability records, checks stock-timer ownership and uses native DBM bars. Its current reset/cancellation and opt-in behavior must be covered before adding more records.\n\n## SmartSync v3 flow observed in source\n\n- Prefix `DCOAS3`, channel `CoASync`; queue cap 160, packet-length guard 231 characters, duplicate queued-packet suppression, incremental index rebuild, and validated N/S records are visible in `SmartSync3.lua`.\n- Legacy DCOAL31/DCOAR21 compatibility is explicitly retained. Do not change wire encoding or identity fields without a migration and mixed-version fixture.\n- Existing `tests/smartsync3_identity_test.lua` is a starting regression fixture; it does not replace client peer tests.\n\n## Required next audit/tests\n\n1. Trace exact TOC load order for all learning, timer, sync, data, localization, and options files.\n2. Test event argument layouts used by the 3.3.5a combat log and decorated CoASync channel names.\n3. Replay out-of-order, repeated, identical-name/different-NPC, pet-controlled, hostile, phase-reset, wipe, map-transition, disconnect/reconnect and mixed-version traffic.\n4. Assert one timer owner and cancellation on all lifecycle exits.\n5. Measure combat event cost and SavedVariables growth on representative long sessions; set hard record/queue caps.\n\nNo protocol change or implementation patch is proposed by this research pass.\n""", encoding="utf-8")
    (OUT / "TEST-AND-VALIDATION-PLAN.md").write_text("""# DBM-CoA v6 test and validation plan\n\n## Offline deterministic checks\n\n- Parse all addon Lua as Lua 5.1; reject 5.2+ syntax/APIs.\n- Parse all research JSON; validate schemas, stable IDs, unique `(moduleId, mapId, NPC, difficulty)` tuples, source paths/revisions, and all foreign references.\n- Parse `.toc` files; ensure every listed path exists and every encounter module is listed exactly once.\n- Scan for duplicate `DBM:NewMod` IDs, duplicate NPC ownership, missing localization keys, absent map/creature registrations, invalid spell IDs, and module category collisions.\n- Simulate module load and native registration under a stub DBM core; validate GUI category visibility without creating a replacement UI.\n- Replay fixture combat events for start/end, cast warnings, target warnings, phase changes, interval timer scheduling, timer correction/cancellation, duplicate bars and difficulty transitions. Label generated fixture events synthetic.\n- Learner tests: hostile gate, pet/player exclusion, sample thresholds, median/outlier behavior, identical NPC display names, bounded storage and zone reset.\n- SmartSync v3 tests: plain/decorated channel names, channel number, malformed packet, duplicate, collision, bounded queue, mixed legacy/v3 records, disconnect/rejoin, and per-tick work cap.\n- SavedVariables tests: old schema loads unchanged, migration idempotence, user preferences preserved, data cap behavior.\n- Package test: expected folder layout, TOC paths, no development-only files/secrets, ZIP integrity, checksums.\n\n## In-game acceptance\n\nFor each instance and difficulty: enter/leave/reload; confirm native category and module appears; observe exact boss start/end; compare every warning/timer to combat log; test wipe/reset and phase cancellation; verify no duplicate stock/source/learned bars; test with other addons enabled; and record client build, date, map/difficulty, DBM commit and evidence artifact.\n\n## Evidence limits\n\nOffline stubs validate code logic only. They do not validate live boss identity, deployed mechanics, spell effects, difficulty behavior, encounter availability, client performance, or peer interoperability. Synthetic fixtures must never be promoted as live encounter evidence.\n""", encoding="utf-8")
    (OUT / "UNRESOLVED-RESEARCH-GAPS.md").write_text("""# DBM-CoA v6 unresolved research gaps\n\n## Blocking encounter evidence\n\n- No live Conquest Reborn logs or authorized deployed-server revision were available in this pass. All public/archive source candidates remain non-live evidence.\n- The complete live instance/mode/difficulty inventory and instance IDs have not been established. The 22-row priority source corpus is not a full inventory.\n- The Temple of Embers and The Radiant Spring do not have boss/AI dossiers in the inspected DBM source corpus. The Radiant Spring appears in an AtlasLoot content-scope record, which is not instance or encounter proof.\n- Manastorm sources describe cache/reward and progression/mode behavior. Whether it is an instance, a run mode over other maps, or a combination must be grounded in actual map/instance runtime evidence. Do not invent a standalone map.\n- Shadowbone Depths has historical/user-provided dossiers and gap analysis, but boss IDs, deployed scripts, spells, difficulty and availability still need verification.\n- Blackrock Caverns has five TrinityCore boss filename candidates (Rom'ogg Bonecrusher, Corla, Karsh Steelbender, Beauty, Ascendant Lord Obsidius) and candidate spell IDs in the archive; it is a Cataclysm reference, not proof of CoA content or mechanics.\n- Road to the Other Side and Vaults have source-derived dossiers, including candidate map/boss/timing data; source branch provenance and exact implementation semantics need verification against the deployed CoA revision.\n\n## Data-quality and implementation gaps\n\n- Spell IDs in source inventories can be shared, unused, difficulty-overridden or bound to other NPCs; source inventory identifiers are not normalized spell-to-boss links.\n- Script timing expressions may be randomized, conditional, cast-start, cast-success, delayed, reset, or phase-local; automatic expression capture does not identify timer semantics.\n- Boss/trash attribution and map/difficulty reconciliation require source and live evidence.\n- Native module coverage needs a full crosswalk of TOCs, localizations, module IDs, map IDs, creature IDs, GUI categories, native module event wiring and stock timer duplication.\n- No full performance benchmark, in-game test matrix, module ZIP or v6 release was produced in this assignment.\n\n## Evidence needed to close these gaps\n\nVersion-pinned authorized server source and world/instance SQL; client-confirmed instance names/map IDs/difficulty behavior; reproducible combat logs with full source flags and casts per difficulty; screenshots or recordings for availability only as supplementary evidence; and in-game tests against the intended DBM-CoA package.\n""", encoding="utf-8")
    (OUT / "V6-DEVELOPMENT-HANDOFF.md").write_text("""# DBM-CoA v6 implementation handoff — grounded status\n\nUse this as the implementation starting point; do not treat unresolved research as a request to fabricate modules.\n\n## Inputs\n\n- `PRIORITY-SEVEN-DUNGEONS.json`: normalized state for the seven named targets.\n- `INSTANCE-REGISTRY.json`: the 22 source-corpus instances plus named custom targets; explicitly incomplete as a live inventory.\n- `BOSS-REGISTRY.json`, `SPELL-MECHANICS.json`, `ENCOUNTER-TIMINGS.json`: source-index candidates only. These are not production warning/timer tables.\n- `INSTANCE-SOURCE-MAP.json`, `SOURCE-PROVENANCE.json`: source lineage and revision references.\n- `DBM-MODULE-COVERAGE.json`: module source-file inventory needing TOC/localization/map reconciliation.\n- `DBM-V6-IMPLEMENTATION-SPEC.md`: native architecture, evidence gates and timer arbitration.\n\n## First safe engineering slice\n\n1. Build an automated native module inventory from the current DBM-CoA default branch: parse each package TOC, locale, `DBM:NewMod`, registered map/NPC IDs, and start/end signals; emit a stable diffable coverage file.\n2. Validate data cross-references and the priority datasets in CI. Keep source-only candidates out of live-warning/timer exports.\n3. Add deterministic regression fixtures for existing Learner and SmartSync v3 behavior before any protocol or runtime changes.\n4. Implement only records that pass the evidence gates; start with native module coverage gaps backed by live logs or exact deployed source.\n5. Maintain one source record per fact, keep conflicts side-by-side, and add explicit promotion history when evidence changes status.\n\n## Hard prohibitions\n\nDo not copy Cataclysm mechanics into Blackrock Caverns as if verified, do not infer Manastorm as a map, do not create boss IDs/spell IDs/timers from names, do not overwrite existing DBM modules, and do not publish v6 until the tests and in-game acceptance criteria pass.\n""", encoding="utf-8")


if __name__ == "__main__":
    main()
