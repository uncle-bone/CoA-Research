#!/usr/bin/env python3
"""Validate v1.2 provenance, uniqueness, ID links, and coverage."""
import json
from pathlib import Path
P=Path(__file__).resolve().parents[1]/"datasets/shared-reference/v1.2"
NAMES=("classes","specializations","spells","pets-and-summons","quests-and-npcs","items-and-loot","combat-attribution","client-compatibility")
def main():
    d={}
    for name in NAMES:
        x=json.loads((P/(name+".json")).read_text(encoding="utf-8"))
        assert x["datasetVersion"]=="1.2.0" and x["recordCount"]==len(x["records"])
        for r in x["records"]:
            assert r.get("sourcePath") and r.get("sourceExtractionDate")
            assert r.get("confidence") and r.get("liveRebornVerified") is False
        d[name]=x
    classes=d["classes"]["records"]; specs=d["specializations"]["records"]; spells=d["spells"]["records"]
    ci={x["classId"] for x in classes}; si={x["specId"] for x in specs}; pi={x["spellId"] for x in spells}
    assert len(ci)==len(classes)==21 and len(si)==len(specs)==101 and len(pi)==len(spells)
    assert all(set(s["classIds"])<=ci and set(s["candidateSpecIds"])<=si for s in spells)
    assert all(set(c["archivedAssociatedSpellIds"])<=pi for c in classes)
    for name in ("quests-and-npcs","items-and-loot"):
        keys=[(r["recordType"],r["id"]) for r in d[name]["records"]]
        assert len(keys)==len(set(keys)),name
    nodes=d["specializations"]["archivedTalentNodes"]
    pairs={(n["classId"],n["nodeId"]) for n in nodes}
    assert len(pairs)==len(nodes)
    assert all(set(n["candidateSpecIds"])<=si and all((n["classId"],k) in pairs for k in n["requiredNodeIds"]) for n in nodes)
    report=json.loads((P/"coverage-report.json").read_text())
    assert report["counts"]=={n:len(d[n]["records"]) for n in NAMES}
    assert report["archivedTalentNodes"]==len(nodes)
    assert report["archivedSpellClassLinks"]==sum(len(s["classIds"]) for s in spells)
    assert report["summonOwnershipChainsVerified"]==0 and report["lootDropsVerified"]==0
    print("PASS",json.dumps(report["counts"],sort_keys=True))
if __name__=="__main__":main()
