#!/usr/bin/env python3
"""Produce durable compact per-instance research and explicit gap reports."""
import argparse
import json
from pathlib import Path

def main():
    p=argparse.ArgumentParser()
    p.add_argument("database")
    p.add_argument("--outdir",default="datasets/instance-scripts/priority")
    args=p.parse_args()
    db=json.loads(Path(args.database).read_text(encoding="utf-8"))
    dest=Path(args.outdir)
    dest.mkdir(parents=True,exist_ok=True)
    coverage={}
    for slug,record in db["instances"].items():
        # Full source reference data (including candidate IDs) is persisted per instance.
        (dest/(slug+".json")).write_text(json.dumps({
            "schema":db["schema"],"warning":db["warning"],**record
        },indent=2)+"\n",encoding="utf-8")
        coverage[slug]=record["coverage"]
    report={"schema":"coa-dbm-priority-coverage-v1",
        "archive_integrity":db["archive_integrity"],
        "source_statuses":db["sources"],
        "instance_count":len(coverage),
        "covered_source_instances":sum(x["source_files"]>0 for x in coverage.values()),
        "instances":coverage,
        "not_live_verified":True,
        "limitations":["Script candidates are not live-server validation.",
            "Phase and timer coverage remains unverified until reviewed against scripts and combat logs.",
            "Trash and boss AI may be implemented in SQL or shared scripts and require additional mapping.",
            "Source archives are alternatives and not proof of active server deployment."]}
    (dest/"coverage-report.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
    gaps=[slug for slug,v in coverage.items() if not v["source_files"] or not v["boss_ai_present"] or not v["trash_ai_explicitly_identified"]]
    print("Instances:",len(coverage),"with source:",report["covered_source_instances"],"gaps:",len(gaps))
    for slug in gaps:
        v=coverage[slug]
        print("GAP",slug,"source",v["source_files"],"boss",v["boss_ai_present"],"trash",v["trash_ai_explicitly_identified"])
    if not coverage:
        raise SystemExit("No instances indexed")

if __name__=="__main__":
    main()
