#!/usr/bin/env python3
"""Generate v1.2 from existing v1.1 source graphs and Questie-X extracted records."""
import json, re, hashlib, gzip
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"datasets/shared-reference"
DEST=BASE/"v1.2"
EXTRACT=ROOT/"research/local-client-extracts/2026-10-31/Questie-X-Full-Extracted-Data"
NAMES=("classes","specializations","spells","pets-and-summons","quests-and-npcs","items-and-loot","combat-attribution","client-compatibility")
def read(p):
    return json.loads(p.read_text(encoding="utf-8"))
def evidence(path,date="2026-10-31",confidence="client_extracted_source_candidate"):
    return dict(sourcePath=path,sourceExtractionDate=date,confidence=confidence,liveRebornVerified=False)
def extract(name):
    path=EXTRACT/(name+".jsonl")
    source=path.relative_to(ROOT).as_posix()
    rows=[]
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip(): continue
        row=json.loads(line)
        if not isinstance(row.get("id"),int) or row["id"]<=0: continue
        raw=row.get("rawLuaRecord","")
        rows.append(dict(recordType=name[:-1] if name.endswith("s") else name,
                         id=row["id"],name=row.get("name"),
                         rawLuaRecord=raw,sourceFile=row.get("source"),
                         availability=row.get("availability"),
                         normalizedRelationshipsStatus="not_verified",
                         coordinates=None,**evidence(source)))
    return rows
def main():
    DEST.mkdir(parents=True,exist_ok=True)
    docs={n:read(BASE/"v1.1"/(n+".json")) for n in NAMES}
    extracted={n:extract(n) for n in ("quests","npcs","objects","items")}
    # Keep source records and raw Lua rather than assuming Questie positional field semantics.
    quests=docs["quests-and-npcs"]
    quests["records"]=extracted["quests"]+extracted["npcs"]+extracted["objects"]
    quests["limitations"]=["Raw CoA Questie-X Lua records preserved losslessly; positional fields have not been assigned semantics without matching database schema","No coordinates, objective/giver/precondition/reward joins promoted without verified schema","Client addon extraction is not proof of live availability"]
    items=docs["items-and-loot"]
    items["records"]=extracted["items"]
    items["limitations"]=["Raw Questie-X item records preserved; positional Lua fields not presumed to be loot or equipment restrictions","Creature/boss drop tables and class/spec restrictions require explicit schema and loot-table source","No item record alone establishes a live drop"]
    # Join only explicit NPC ID equality to historical candidate list. This is ID correspondence, NOT ownership.
    npc_ids={r["id"] for r in extracted["npcs"]}
    pets=docs["pets-and-summons"]
    for r in pets["records"]:
        key=next((k for k in ("npcId","creatureId","id") if isinstance(r.get(k),int)),None)
        r["clientExtractIdMatch"]=bool(key and r[key] in npc_ids)
        r["ownershipLinkVerified"]=False
        r["petAbilitySpellIds"]=[]
        r["summoningSpellId"]=None
    pets["limitations"].append("NPC ID equality across historical sources is not proof of player control, summon spell, or pet abilities")
    # Candidate client addon records are not evidence of live combat-log ownership.
    combat=docs["combat-attribution"]
    combat["records"].append(dict(recordType="unresolved_evidence",id="charlga-and-trash-ai",boss="Charlga Razorflank",classification="unresolved",evidenceNeeded=["reliable boss-AI script or verified SQL mapping","hostile trash ScriptName/SmartAI attribution","live GUID flags and source/destination event traces"],**evidence("research/priority-dungeon-source-coverage-gap-analysis-2026-11-02.md","2026-11-02","research_gap")))
    compat=docs["client-compatibility"]
    for addon,repo in (("Mapster-CoA","uncle-bone/Mapster-CoA"),("ElvUI-CoA","uncle-bone/ElvUI-CoA"),("ConquestWorldMapImprovement","uncle-bone/ConquestWorldMapImprovement"),("DragonUI-CoA","PentSec/DragonUI-CoA")):
        compat["records"].append(dict(recordType="integration_research_target",addon=addon,repository=repo,modifiedApis=[],mapBehavior="unverified",frameOwnership="unverified",conflicts=[],workarounds=[],liveTestStatus="not_tested",**evidence("datasets/shared-reference/v1/README.md","2026-11-02","research_target_only")))
    for name,doc in docs.items():
        doc["datasetVersion"]="1.2.0"
        doc["recordCount"]=len(doc["records"])
        (DEST/(name+".json")).write_text(json.dumps(doc,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    report={"version":"1.2.0","dataNature":"source candidates; no live Conquest Reborn validation",
      "counts":{n:len(docs[n]["records"]) for n in NAMES},
      "sourceExtractCounts":{n:len(v) for n,v in extracted.items()},
      "archivedSpellClassLinks":sum(len(s.get("classIds",[])) for s in docs["spells"]["records"]),
      "archivedTalentNodes":len(docs["specializations"].get("archivedTalentNodes",[])),
      "summonOwnershipChainsVerified":0,"questCoordinatesVerified":0,"lootDropsVerified":0,
      "trainerMappingsVerified":0,"combatRuntimeTracesVerified":0,"uiLiveTestsVerified":0,
      "unresolved":["Spell effect -> summon NPC -> owner -> pet abilities","Questie Lua positional field schema and coordinate semantics","Creature loot SQL, item eligibility","Trainer data and current class roster","Charlga trusted AI and hostile trash SQL","3.3.5a combat logs","UI addon source/API audits and live compatibility tests"]}
    (DEST/"coverage-report.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(report,indent=2))
if __name__=="__main__":main()
