#!/usr/bin/env python3
"""Reproducible v2 research package: explicit edges, gaps, browser index, Lua 5.1 exports."""
import json, re, hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"datasets/shared-reference"
OUT=BASE/"v2.0"
NAMES=("classes","specializations","spells","pets-and-summons","quests-and-npcs","items-and-loot","combat-attribution","client-compatibility")
def load(p): return json.loads(p.read_text(encoding="utf-8"))
def dump(p,v):
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
def lua(v):
    if v is None:return "nil"
    if isinstance(v,bool):return "true" if v else "false"
    if isinstance(v,(int,float)):return str(v)
    if isinstance(v,str):return json.dumps(v,ensure_ascii=True)
    if isinstance(v,list):return "{"+",".join(lua(x) for x in v)+"}"
    if isinstance(v,dict):return "{"+",".join("["+lua(str(k))+"]="+lua(x) for k,x in v.items())+"}"
    raise TypeError(type(v))
def main():
    OUT.mkdir(parents=True,exist_ok=True)
    # v1.2 is generated as a build prerequisite, never read a nonexistent committed output.
    docs={n:load(BASE/"v1.2"/(n+".json")) for n in NAMES}
    edges=[]; missing=[]; conflicts=[]
    classes={r["classId"]:r for r in docs["classes"]["records"]}
    specs={r["specId"]:r for r in docs["specializations"]["records"]}
    spells={r["spellId"]:r for r in docs["spells"]["records"]}
    def edge(kind,a,b,source,confidence="archived_source",detail=None):
        edges.append(dict(type=kind,fromNode=a,toNode=b,sourcePath=source,
                          sourceExtractionDate="unknown",confidence=confidence,
                          liveRebornVerified=False,detail=detail))
    for c in classes.values():
        for sid in c["specializationIds"]:
            if sid in specs and specs[sid]["classId"]==c["classId"]:
                edge("class-spec","class:"+str(c["classId"]),"spec:"+str(sid),c["sourcePath"])
            else: missing.append(dict(type="class-spec",classId=c["classId"],specId=sid))
    for s in spells.values():
        for cid in s["classIds"]:
            if cid in classes: edge("class-spell","class:"+str(cid),"spell:"+str(s["spellId"]),s["sourcePath"])
            else:missing.append(dict(type="class-spell",classId=cid,spellId=s["spellId"]))
        for sid in s["candidateSpecIds"]:
            if sid in specs: edge("candidate-spec-spell","spec:"+str(sid),"spell:"+str(s["spellId"]),s["sourcePath"],"archived_candidate")
            else:missing.append(dict(type="spec-spell",specId=sid,spellId=s["spellId"]))
    for t in docs["specializations"].get("archivedTalentNodes",[]):
        key="talent:"+str(t["classId"])+":"+str(t["nodeId"])
        for sid in t["candidateSpecIds"]:
            if sid in specs:edge("candidate-spec-talent","spec:"+str(sid),key,t["sourcePath"],"archived_candidate")
            else:missing.append(dict(type="spec-talent",specId=sid,nodeId=t["nodeId"]))
        for spellid in t["spellIds"]:
            if spellid in spells:edge("talent-spell",key,"spell:"+str(spellid),t["sourcePath"])
            else:missing.append(dict(type="talent-spell",nodeId=t["nodeId"],spellId=spellid))
        for dep in t["requiredNodeIds"]:
            edge("talent-prerequisite","talent:"+str(t["classId"])+":"+str(dep),key,t["sourcePath"])
    # Encounter overlay contains sourced instance credits; not automatically verified boss mechanics.
    encounter_source="research/encounters/base-plus-coa-encounter-overlay-2026-10-30.json"
    overlay=load(ROOT/encounter_source)
    encounters=[]
    for r in overlay.get("records",[]):
        if not isinstance(r,dict):continue
        encounters.append(dict(**r,sourcePath=encounter_source,sourceExtractionDate="2026-10-30",confidence="archived_sql_overlay",liveRebornVerified=False))
    # Raw positional Questie records retained: no guessed quest objectives, coordinates, loot or restrictions.
    for n,d in docs.items():
        d["datasetVersion"]="2.0.0"
        d["recordCount"]=len(d["records"])
        dump(OUT/(n+".json"),d)
    graph=dict(schemaVersion=1,version="2.0.0",edges=edges,missingReferences=missing,conflicts=conflicts,
               liveVerifiedEdges=0,limitations=["Archived relationships are not runtime ownership","No explicit summon effect->creature or pet ability edges verified"])
    dump(OUT/"relationship-graph.json",graph)
    dump(OUT/"encounter-evidence.json",dict(version="2.0.0",records=encounters,liveVerified=False,
         limitations=["Instance encounter credits do not establish phases, combat timers, trash AI or live difficulty behavior"]))
    report=dict(version="2.0.0",datasetCounts={n:len(docs[n]["records"]) for n in NAMES},
       edgeCounts={kind:sum(e["type"]==kind for e in edges) for kind in sorted({e["type"] for e in edges})},
       brokenReferenceCount=len(missing),conflictCount=len(conflicts),encounterOverlayRows=len(encounters),
       verifiedSummonOwnershipChains=0,verifiedQuestCoordinates=0,verifiedLootDrops=0,
       verifiedTrainerMappings=0,verifiedUiCompatibilityTests=0,
       unresolved=["Summon effect-to-creature owner and pet ability mapping","Questie positional Lua schema, objectives, giver, rewards, prerequisites and coordinates","Loot SQL joins, vendors, recipes and equipment restrictions","Trainer spell requirements and live roster","Charlga/trash AI runtime and combat GUID flags","Client API changes and UI addon runtime compatibility"])
    dump(OUT/"coverage-report.json",report)
    # Addon-specific projections are intentionally minimal and do not promote candidates.
    exports={
      "DBM-CoA":dict(version="2.0.0",encounterCredits=encounters,verifiedSummonOwnership={}),
      "Details-CoA":dict(version="2.0.0",verifiedPetOwnership={}),
      "pfQuest-CoA":dict(version="2.0.0",quests=[dict(id=r["id"],name=r.get("name")) for r in docs["quests-and-npcs"]["records"] if r["recordType"]=="quest"]),
      "LootCollector":dict(version="2.0.0",items=[r["id"] for r in docs["items-and-loot"]["records"]],verifiedDrops={}),
      "WhatsTraining-CoA":dict(version="2.0.0",specs=[dict(id=s["specId"],classId=s["classId"]) for s in specs.values()],verifiedTrainers={})
    }
    for name,data in exports.items():
        (OUT/"lua"/(name+".lua")).parent.mkdir(parents=True,exist_ok=True)
        (OUT/"lua"/(name+".lua")).write_text("-- Historical research candidates; no live verification.\nreturn "+lua(data)+"\n",encoding="utf-8")
    # Small browser index: do not download the full multi-MB research graph for each page load.
    browser=[]
    for c in classes.values():browser.append(dict(type="class",id=c["classId"],name=c["name"],source=c["sourcePath"],verified=False,addons=["WeakAuras-CoA","Details-CoA"]))
    for s in specs.values():browser.append(dict(type="spec",id=s["specId"],name=s["name"],source=s["sourcePath"],verified=False,addons=["WhatsTraining-CoA"]))
    for r in docs["quests-and-npcs"]["records"]:
        if r.get("name"):browser.append(dict(type=r["recordType"],id=r["id"],name=r["name"],source=r["sourcePath"],verified=False,addons=["pfQuest-CoA"]))
    dump(OUT/"explorer-index.json",browser)
    print(json.dumps(report,indent=2))
if __name__=="__main__":main()
