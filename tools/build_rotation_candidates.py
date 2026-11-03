#!/usr/bin/env python3
"""Populate archived candidate spell/talent associations for all CR/CoA specs.

Run: python tools/build_rotation_candidates.py
No rotation priorities are inferred. This builds an evidence-backed candidate
index from existing local CoA-Research datasets.
"""
import gzip
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "datasets/relationships"
INPUT = ROOT / "datasets/rotations/coa-spec-rotation-guide-records-v1.json"
OUTPUT = ROOT / "datasets/rotations/coa-spec-mechanics-candidates-v1.json.gz"
REPORT = ROOT / "datasets/rotations/coverage-report.json"


def load_gz(path):
    with gzip.open(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)


def main():
    base = json.loads(INPUT.read_text(encoding="utf-8"))
    spells = load_gz(SRC / "spells-by-id.json.gz")
    talents = load_gz(SRC / "talent-nodes.json.gz")
    enriched = load_gz(SRC / "enriched-spells-by-id.json.gz")
    by_spec = {r["specId"]: {"classId": r["classId"], "className": r["className"],
                "specId": r["specId"], "specName": r["specName"],
                "candidateAbilities": [], "candidateTalentNodes": [],
                "status": "archived-source-candidates-not-live-verified"} for r in base["records"]}
    by_class = defaultdict(list)
    for spec in by_spec.values():
        by_class[spec["classId"]].append(spec)
    unmatched_classwide = defaultdict(list)
    seen = set()
    for sid, entry in spells.items():
        spell_id = int(sid)
        definition = enriched.get(sid, {})
        for evidence in entry.get("evidence", []):
            if evidence.get("type") != "ability-member":
                continue
            cls = evidence["classId"]
            candidate_ids = evidence.get("candidateSpecIds", [])
            if not candidate_ids:
                unmatched_classwide[cls].append(spell_id)
                continue
            for spec_id in candidate_ids:
                spec = by_spec.get(spec_id)
                if not spec or spec["classId"] != cls:
                    continue
                key = (spec_id, spell_id, evidence.get("source"))
                if key in seen:
                    continue
                seen.add(key)
                spec["candidateAbilities"].append({
                    "spellId": spell_id, "abilityName": evidence.get("abilityName"),
                    "spellName": evidence.get("spellName"),
                    "rank": evidence.get("rank"), "cadTabs": evidence.get("cadTabs", []),
                    "source": evidence.get("source"),
                    "mappingEvidence": "archived-CAD-tab-match",
                    "definition": definition if isinstance(definition, dict) else {},
                })
    for node in talents:
        for spec_id in node.get("candidateSpecIds", []):
            spec = by_spec.get(spec_id)
            if spec and spec["classId"] == node.get("classId"):
                spec["candidateTalentNodes"].append({
                    "nodeId": node.get("nodeId"), "name": node.get("nodeName"),
                    "spellIds": node.get("spellIds", []), "requiredNodeIds": node.get("requiredNodeIds", []),
                    "maxPoints": node.get("maxPoints"), "source": node.get("source"),
                    "mappingEvidence": node.get("mappingConfidence"),
                })
    for spec in by_spec.values():
        spec["candidateAbilities"].sort(key=lambda a: (a["spellId"], a["source"] or ""))
        spec["candidateTalentNodes"].sort(key=lambda n: n["nodeId"] or 0)
        spec["unassignedClassAbilitySpellIds"] = sorted(set(unmatched_classwide[spec["classId"]]))
        spec["priorityRules"] = []
        spec["priorityStatus"] = "awaiting-mechanics-and-combat-validation"
    rows = sorted(by_spec.values(), key=lambda x: x["specId"])
    report = {"schemaVersion": 1, "sourceStatus": "archived-candidate-only",
              "specs": len(rows), "classes": len(by_class),
              "specsWithAbilityCandidates": sum(bool(r["candidateAbilities"]) for r in rows),
              "specsWithTalentCandidates": sum(bool(r["candidateTalentNodes"]) for r in rows),
              "abilityCandidateEdges": sum(len(r["candidateAbilities"]) for r in rows),
              "talentCandidateNodes": sum(len(r["candidateTalentNodes"]) for r in rows),
              "specsWithVerifiedRotation": 0,
              "note": "No live-client ownership, cooldown units, spell effects, or rotation priority is inferred."}
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(OUTPUT, "wt", encoding="utf-8") as stream:
        json.dump({"schemaVersion": 1, "sourceFiles": [
            "datasets/relationships/spells-by-id.json.gz",
            "datasets/relationships/talent-nodes.json.gz",
            "datasets/relationships/enriched-spells-by-id.json.gz"],
            "records": rows}, stream, ensure_ascii=False, separators=(",", ":"))
    REPORT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
