#!/usr/bin/env python3
import json
from pathlib import Path
P=Path(__file__).resolve().parents[1]/"datasets/shared-reference/v2.0"
def read(n):return json.loads((P/n).read_text(encoding="utf-8"))
def main():
    d=read("items-and-loot.json");rows=d["sourcedCreatureLootRows"]
    assert len(rows)==d["sourcedCreatureLootRowCount"]==239
    keys=set()
    for r in rows:
        assert r["sourcePath"] and r["underlyingSqlSource"] and r["sourceExtractionDate"]
        assert r["liveRebornVerified"] is False and r["confidence"]=="archived_sql_row"
        assert r["npcId"]>0 and r["itemId"]>0
        k=(r["npcId"],r["itemId"],r["lootMode"],r["groupId"])
        assert k not in keys,("duplicate",k)
        keys.add(k)
    report=read("coverage-report.json")
    assert report["sourcedCreatureLootRows"]==len(rows)
    assert report["sourcedCreatureLootNpcs"]==len({r["npcId"] for r in rows})
    assert report["confirmedTrainerNpcAssignments"]==0
    assert read("unresolved-evidence.json")["loot"]["runtimeVerified"]==0
    print("PASS SQL-backed loot rows",len(rows))
if __name__=="__main__":main()
