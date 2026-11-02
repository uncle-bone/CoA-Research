#!/usr/bin/env python3
"""Build provenance-labeled v1.1 from committed archival relationship artifacts."""
import gzip
import json
from pathlib import Path
from collections import Counter

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"datasets/shared-reference"
SOURCE=BASE/"v1"
DEST=BASE/"v1.1"
REL=ROOT/"datasets/relationships"
NAMES=("classes","specializations","spells","pets-and-summons","quests-and-npcs","items-and-loot","combat-attribution","client-compatibility")

def read(path):
    if path.suffix==".gz":
        with gzip.open(path,"rt",encoding="utf-8") as f: return json.load(f)
    return json.loads(path.read_text(encoding="utf-8"))

def write(name,doc):
    doc["schemaVersion"]=1
    doc["datasetVersion"]="1.1.0"
    doc["recordCount"]=len(doc["records"])
    (DEST/(name+".json")).write_text(json.dumps(doc,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

def evidence(source,confidence="archived_source"):
    return dict(sourcePath=source,sourceExtractionDate="unknown",confidence=confidence,liveRebornVerified=False)

def main():
    DEST.mkdir(parents=True,exist_ok=True)
    docs={name:read(SOURCE/(name+".json")) for name in NAMES}
    graph=read(REL/"spells-by-id.json.gz")
    nodes=read(REL/"talent-nodes.json.gz")
    ids={c["classId"] for c in docs["classes"]["records"]}
    specids={s["specId"] for s in docs["specializations"]["records"]}
    src="datasets/relationships/spells-by-id.json.gz"
    spells=[]
    class_spells={c:set() for c in ids}
    for key,g in sorted(graph.items(),key=lambda kv:int(kv[0])):
        sid=int(key)
        classes=sorted(set(g.get("classIds",[]))&ids)
        specs=sorted(set(g.get("candidateSpecIds",[]))&specids)
        for cid in classes: class_spells[cid].add(sid)
        spells.append(dict(spellId=sid,classIds=classes,candidateSpecIds=specs,
                           ownershipEvidence=g.get("evidence",[]),
                           ownershipStatus="archived_class_association_not_runtime_owner",
                           summonCreatureId=None,**evidence(src)))
    docs["spells"]["records"]=spells
    for c in docs["classes"]["records"]:
        c["archivedAssociatedSpellIds"]=sorted(class_spells[c["classId"]])
    talent_by_spec={s:set() for s in specids}
    talents=[]
    for n in nodes:
        cid=n.get("classId")
        if cid not in ids: continue
        specs=[x for x in n.get("candidateSpecIds",[]) if x in specids]
        for s in specs: talent_by_spec[s].add((cid,n["nodeId"]))
        talents.append(dict(classId=cid,nodeId=n["nodeId"],candidateSpecIds=specs,
                            requiredNodeIds=n.get("requiredNodeIds",[]),maxPoints=n.get("maxPoints"),
                            spellIds=n.get("spellIds",[]),sourceTab=n.get("archivedTabName"),
                            **evidence("datasets/relationships/talent-nodes.json.gz")))
    for s in docs["specializations"]["records"]:
        s["archivedTalentNodeIds"]=sorted(n for cid,n in talent_by_spec[s["specId"]] if cid==s["classId"])
        s["trainerMappingsVerified"]=False
        s["currentPlayableVerified"]=False
    docs["specializations"]["archivedTalentNodes"]=talents
    docs["spells"]["limitations"].append("Spell-class associations are archived source evidence, not verified casts, ownership, or summon effects")
    docs["pets-and-summons"]["limitations"].append("No explicit summon-spell-to-creature mapping inferred from names; needs effect/aura evidence and runtime validation")
    docs["quests-and-npcs"]["limitations"].append("Source inventory only; Questie Lua/JSONL relationships and map coordinates not normalized in this release")
    docs["items-and-loot"]["limitations"].append("No source-verified creature-loot SQL join or equipment restriction mapping available in this export")
    docs["combat-attribution"]["limitations"].append("Charlga AI remains insufficiently sourced; hostile trash attribution and live GUID tests pending")
    docs["client-compatibility"]["limitations"].append("Mapster, ElvUI, CWMI and DragonUI behavior not live-tested; do not assert compatibility")
    for name,doc in docs.items(): write(name,doc)
    report={"version":"1.1.0","sourceStatus":"archived candidates, not live verified",
      "counts":{name:len(doc["records"]) for name,doc in docs.items()},
      "archivedTalentNodes":len(talents),"spellClassLinks":sum(len(s["classIds"]) for s in spells),
      "verifiedSummonChains":0,"verifiedQuestLocationLinks":0,"verifiedLootLinks":0,
      "verifiedTrainerMappings":0,"verifiedClientCompatibilityFindings":0,
      "unresolved":["summon creature ownership","quest/object coordinates","loot table joins","trainer spells","runtime combat flags","UI compatibility tests","Charlga reliable boss AI"]}
    (DEST/"coverage-report.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,indent=2))

if __name__=="__main__": main()
