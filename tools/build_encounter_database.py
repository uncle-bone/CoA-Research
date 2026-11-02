#!/usr/bin/env python3
"""Build a provenance-aware, searchable DBM research index from collected source files.

This is a static candidate index, NOT a claim of live-server behavior.
"""
import argparse
import json
import re
import zipfile
from collections import defaultdict

INSTANCE_TERMS = {
 "ragefire-chasm": ["ragefire"], "wailing-caverns": ["wailing"],
 "deadmines": ["deadmines"], "shadowfang-keep": ["shadowfang"],
 "blackfathom-deeps": ["blackfathom"], "stockade": ["stockade"],
 "gnomeregan": ["gnomeregan"], "razorfen-kraul": ["razorfenkraul"],
 "scarlet-monastery": ["scarletmonastery"], "razorfen-downs": ["razorfendowns"],
 "uldaman": ["uldaman"], "zulfarrak": ["zulfarrak"],
 "maraudon": ["maraudon"], "sunken-temple": ["sunkentemple", "atalhakkar"],
 "blackrock-depths": ["blackrockdepths"], "lower-blackrock-spire": ["blackrockspire"],
 "upper-blackrock-spire": ["blackrockspire"], "dire-maul": ["diremaul"],
 "scholomance": ["scholomance"], "stratholme": ["stratholme"],
 "blackrock-caverns": ["blackrockcaverns"], "zulgurub": ["zulgurub", "raid-difficulty"]
}
CATEGORIES = ("boss", "trash", "instance", "sql", "shared", "other")
IDENT = re.compile(r"\b(?:NPC|BOSS|SPELL|EVENT|DATA|GO)_[A-Z0-9_]+\b")
NPC = re.compile(r"\b(?:NPC|BOSS)_[A-Z0-9_]+\s*=\s*(\d{3,9})\b")
SPELL = re.compile(r"\bSPELL_[A-Z0-9_]+\s*=\s*(\d{3,9})\b")
CAST = re.compile(r"\b(?:DoCast|CastSpell|CastCustomSpell|DoCastVictim|DoCastAOE|ScheduleEvent|RescheduleEvent|AddEvent|events.ScheduleEvent)\s*\(")
TIMING = re.compile(r"\b(?:Seconds|Milliseconds|MINUTE|SECOND|urand|randtime|EVENT_|TIMER_|PHASE_|SetPhase|GetPhase|HealthBelowPct|HealthAbovePct|HealthPct|HealthPctBelow|HealthPctAbove)\b")
SQL_ENTRY = re.compile(r"(?:\bentry\b|\`entry\`)\s*=\s*(\d{3,9})", re.I)
SQL_SCRIPT = re.compile(r"ScriptName.{0,90}?['\"]([a-zA-Z_][a-zA-Z_0-9]+)['\"]", re.I)
COA_SQL = re.compile(r"mod-manastorm-endless|mod-coa-raid-difficulty", re.I)

def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())

def parse(archive):
    db = {k: {"instance":k, "source_files":[], "encounters":{}, "coverage":{}} for k in INSTANCE_TERMS}
    manifest = {}
    with zipfile.ZipFile(archive) as z:
        bad = z.testzip()
        if bad:
            raise RuntimeError("ZIP integrity error at "+bad)
        manifest = json.loads(z.read("manifest.json"))
        for item in manifest.get("files", []):
            name = "source/"+item["source"]+"/"+item["path"]
            if name not in z.namelist():
                raise RuntimeError("Manifest file absent from archive: "+name)
            path = item["path"]
            key = norm(path)
            matches = [slug for slug,terms in INSTANCE_TERMS.items() if any(norm(term) in key for term in terms)]
            if not matches:
                continue
            data = z.read(name).decode("utf-8", errors="replace")
            basename = path.rsplit("/",1)[-1].lower()
            category = ("boss" if basename.startswith("boss_") else
                        "instance" if basename.startswith("instance_") else
                        "sql" if path.lower().endswith(".sql") else
                        "trash" if any(t in basename for t in ("trash","mob_","npc_","creature")) else "shared")
            source = {"repository":item["source"],"revision":item["revision"],"path":path,
                      "kind":category,"bytes":item["bytes"],"evidence":"source-file-read",
                      "live_reborn_verified":False,
                      "npc_ids_candidate":sorted(set(map(int,NPC.findall(data)))),
                      "spell_ids_candidate":sorted(set(map(int,SPELL.findall(data)))),
                      "sql_entry_ids_candidate":sorted(set(map(int,SQL_ENTRY.findall(data)))) if category=="sql" else [],
                      "sql_script_names_candidate":sorted(set(SQL_SCRIPT.findall(data))) if category=="sql" else [],
                      "identifiers":sorted(set(IDENT.findall(data))),
                      "cast_calls":len(CAST.findall(data)),
                      "timing_or_phase_signals":len(TIMING.findall(data)),
                      "timers_verified":[],
                      "phases_verified":[]}
            # CoA Manastorm is a distinct mode, never silently merge with ordinary dungeon mechanics.
            source["variant"] = ("manastorm" if "mod-manastorm-endless" in path else
                                 "coa-raid-difficulty" if "mod-coa-raid-difficulty" in path else "baseline-candidate")
            for slug in matches:
                db[slug]["source_files"].append(source)
                if category=="boss":
                    boss_name=basename.rsplit(".",1)[0]
                    db[slug]["encounters"].setdefault(boss_name,{"name":boss_name,"evidence":"candidate-from-filename",
                         "source_paths":[],"live_reborn_verified":False})["source_paths"].append(path)
    for slug,entry in db.items():
        files=entry["source_files"]
        counts={k:sum(x["kind"]==k for x in files) for k in CATEGORIES}
        entry["coverage"]={"source_files":len(files),"by_kind":counts,
          "npc_ids_candidate":len(set(i for f in files for i in f["npc_ids_candidate"])),
          "spell_ids_candidate":len(set(i for f in files for i in f["spell_ids_candidate"])),
          "encounter_filename_candidates":len(entry["encounters"]),
          "boss_ai_present":counts["boss"]>0,
          "trash_ai_explicitly_identified":counts["trash"]>0,
          "script_timers_verified":False,"live_reborn_verified":False,
          "status":"source-candidates-found" if files else "no-matching-source-found"}
    return {"schema":"coa-dbm-encounter-research-v1",
      "warning":"Candidate source data only. Numeric IDs may be unrelated to runtime use; timings and phases are NOT verified. Review script behavior and live combat logs.",
      "archive_integrity":"zip-testzip-passed",
      "sources":manifest.get("sources",[]),"instances":db}

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("archive")
    p.add_argument("--output",default="dbm-priority-encounters.json")
    a=p.parse_args()
    db=parse(a.archive)
    with open(a.output,"w",encoding="utf-8") as f:
        json.dump(db,f,indent=2)
        f.write("\n")
    for slug,entry in db["instances"].items():
        print(slug,entry["coverage"]["source_files"],entry["coverage"]["status"])
