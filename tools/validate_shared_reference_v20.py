#!/usr/bin/env python3
"""Validate v2 source traceability, graph references, Lua projections and reports."""
import json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P=ROOT/"datasets/shared-reference/v2.0"
NAMES=("classes","specializations","spells","pets-and-summons","quests-and-npcs","items-and-loot","combat-attribution","client-compatibility")
def load(n):return json.loads((P/n).read_text(encoding="utf-8"))
def main():
    docs={n:load(n+".json") for n in NAMES}
    for n,d in docs.items():
        assert d["datasetVersion"]=="2.0.0" and d["recordCount"]==len(d["records"])
        for r in d["records"]:
            assert r.get("sourcePath") and r.get("sourceExtractionDate") and r.get("confidence")
            assert r["liveRebornVerified"] is False
    graph=load("relationship-graph.json")
    edges=graph["edges"]
    assert edges
    keys=set()
    for e in edges:
        assert e["sourcePath"] and e["sourceExtractionDate"] and e["confidence"] and e["liveRebornVerified"] is False
        key=(e["type"],e["fromNode"],e["toNode"])
        assert key not in keys,("duplicate edge",key)
        keys.add(key)
    classes={r["classId"] for r in docs["classes"]["records"]}
    specs={r["specId"] for r in docs["specializations"]["records"]}
    spells={r["spellId"] for r in docs["spells"]["records"]}
    talents={(r["classId"],r["nodeId"]) for r in docs["specializations"]["archivedTalentNodes"]}
    for e in edges:
        for v in (e["fromNode"],e["toNode"]):
            p=v.split(":")
            if p[0]=="class":assert int(p[1]) in classes
            if p[0]=="spec":assert int(p[1]) in specs
            if p[0]=="spell":assert int(p[1]) in spells
            if p[0]=="talent":assert (int(p[1]),int(p[2])) in talents
    report=load("coverage-report.json")
    assert report["brokenReferenceCount"]==len(graph["missingReferences"])
    assert report["conflictCount"]==len(graph["conflicts"])
    assert report["datasetCounts"]=={n:len(docs[n]["records"]) for n in NAMES}
    for p in (P/"lua").glob("*.lua"):
        text=p.read_text()
        assert text.startswith("-- Historical") and "\nreturn {" in text
        assert not re.search(r"\b(?:function|goto|continue)\b",text)
    assert len(list((P/"lua").glob("*.lua")))==5
    assert isinstance(load("explorer-index.json"),list)
    print("PASS v2",len(edges),"edges",len(graph["missingReferences"]),"missing",len(load("encounter-evidence.json")["records"]),"encounter credits")
if __name__=="__main__":main()
