#!/usr/bin/env python3
"""Evidence-only v2.0.1 enrichment from existing SQL-derived loot and trainer audits."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"datasets/shared-reference/v2.0"
LOOT=ROOT/"research/loot/vaults-complete-creature-loot-2026-10-30.json"
TRAIN=ROOT/"research/local-client-extracts/2026-10-31/whats-training/coa-trainer-npcs.json"
def read(p):return json.loads(p.read_text(encoding="utf-8"))
def write(p,d):p.write_text(json.dumps(d,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
def main():
    loot=read(LOOT)
    assert loot["rowCount"]==sum(len(n["rows"]) for n in loot["byNpc"])
    rows=[]
    for npc in loot["byNpc"]:
        for row in npc["rows"]:
            assert row["npcId"]==npc["npcId"]
            assert isinstance(row["itemId"],int) and row["itemId"]>0
            rows.append(dict(npcId=row["npcId"],itemId=row["itemId"],bossCandidate=npc.get("boss"),
                lootMode=row.get("lootMode"),chance=row.get("chance"),groupId=row.get("groupId"),
                minCount=row.get("min"),maxCount=row.get("max"),reference=row.get("reference"),
                evidenceType="SQL-derived creature loot row; runtime drop unverified",
                sourcePath=LOOT.relative_to(ROOT).as_posix(),
                underlyingSqlSource=loot["source"],sourceExtractionDate=loot["date"],
                confidence="archived_sql_row",liveRebornVerified=False))
    doc=read(OUT/"items-and-loot.json")
    doc["sourcedCreatureLootRows"]=rows
    doc["sourcedCreatureLootRowCount"]=len(rows)
    doc["limitations"].append("Vaults SQL creature-loot rows are concrete source-backed candidate drops; chance=0 and loot mode do not imply guaranteed drops")
    write(OUT/"items-and-loot.json",doc)
    report=read(OUT/"coverage-report.json")
    report["sourcedCreatureLootRows"]=len(rows)
    report["sourcedCreatureLootNpcs"]=len({r["npcId"] for r in rows})
    report["sourcedCreatureLootItems"]=len({r["itemId"] for r in rows})
    report["verifiedLootDrops"]=0
    trainer=read(TRAIN)
    report["confirmedTrainerNpcAssignments"]=len(trainer["records"])
    report["trainerEvidence"]="research/local-client-extracts/2026-10-31/whats-training/coa-trainer-research-audit.md"
    report["trainerRankRowsInLocalAudit"]=13311
    report["trainerRankRowsImported"]=0
    report["runtimeValidation"]="not_run"
    write(OUT/"coverage-report.json",report)
    audit={"release":"2.0.1","petSummon":{"status":"unresolved","required":"explicit spell effect summon creature ID, controller GUID and pet ability table; class spell associations alone insufficient"},
      "quests":{"status":"partially_extracted","required":"verified Questie positional schema, NPC/object spawn map data, quest relationships and client conflicts"},
      "loot":{"status":"source_backed_candidate","source":LOOT.relative_to(ROOT).as_posix(),"rows":len(rows),"runtimeVerified":0},
      "trainers":{"status":"source_audited","rankRowsReported":13311,"confirmedTrainerAssignments":0,"required":"parse rank dataset and capture live trainer NPC/service"},
      "combat":{"status":"unverified","required":"client combat GUID and flags; trusted Charlga/trash script mappings"},
      "ui":{"status":"unverified","required":"inspect exact addon commits and live 3.3.5a frame ownership"},
      "explorer":{"status":"code_and_index_in_repository","required":"HTTP verification of GitHub Pages deployment and browser interaction"}}
    write(OUT/"unresolved-evidence.json",audit)
    print(json.dumps({"lootRows":len(rows),"npcCount":report["sourcedCreatureLootNpcs"],"items":report["sourcedCreatureLootItems"],"trainerAssignments":0}))
if __name__=="__main__":main()
