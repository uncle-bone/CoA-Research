#!/usr/bin/env python3
"""Strict v1.1 cross-reference and provenance validation."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/"datasets/shared-reference/v1.1"
NAMES=("classes","specializations","spells","pets-and-summons","quests-and-npcs","items-and-loot","combat-attribution","client-compatibility")
def main():
    docs={}
    for name in NAMES:
        d=json.loads((P/(name+".json")).read_text())
        assert d["datasetVersion"]=="1.1.0" and d["schemaVersion"]==1
        assert d["recordCount"]==len(d["records"])
        for r in d["records"]:
            assert r.get("sourcePath") and r.get("sourceExtractionDate")
            assert r.get("confidence") and r.get("liveRebornVerified") is False
        docs[name]=d
    classes=docs["classes"]["records"]
    specs=docs["specializations"]["records"]
    spells=docs["spells"]["records"]
    classids={c["classId"] for c in classes}
    specids={s["specId"] for s in specs}
    spellids={s["spellId"] for s in spells}
    assert len(classids)==len(classes)==21
    assert len(specids)==len(specs)==101
    assert len(spellids)==len(spells)
    assert all(set(s["classIds"])<=classids and set(s["candidateSpecIds"])<=specids for s in spells)
    assert all(set(c["archivedAssociatedSpellIds"])<=spellids for c in classes)
    assert all(set(c["specializationIds"])<=specids for c in classes)
    nodes=docs["specializations"]["archivedTalentNodes"]
    pairs={(n["classId"],n["nodeId"]) for n in nodes}
    assert len(pairs)==len(nodes)
    for n in nodes:
        assert n["classId"] in classids
        assert set(n["candidateSpecIds"])<=specids
        assert all((n["classId"],i) in pairs for i in n["requiredNodeIds"])
    report=json.loads((P/"coverage-report.json").read_text())
    assert report["counts"]=={n:len(docs[n]["records"]) for n in NAMES}
    assert report["archivedTalentNodes"]==len(nodes)
    assert report["spellClassLinks"]==sum(len(s["classIds"]) for s in spells)
    assert report["verifiedSummonChains"]==0
    print("PASS",report["counts"],"talentNodes",len(nodes))
if __name__=="__main__":main()
