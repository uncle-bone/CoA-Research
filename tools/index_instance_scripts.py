#!/usr/bin/env python3
"""Create searchable per-script symbol and spell-ID index from the source archive."""
import argparse
import json
import re
import zipfile
from collections import Counter

SYMBOL = re.compile(r"\b(?:struct|class)\s+([A-Za-z_]\w*)|\b(?:AddSC_|Register[A-Za-z]*|GetAI|On[A-Za-z]+)\w*\s*\(")
SPELL = re.compile(r"\b(?:SPELL_[A-Z0-9_]+|spellId|SpellId|SPELLID)\b|\b(?:DoCast|CastSpell|ScheduleEvent|EVENT_)\b")
ID = re.compile(r"\b(?:NPC|BOSS|DATA|GO|SPELL|EVENT)_[A-Z0-9_]+\b")

def build(archive):
    rows = []
    with zipfile.ZipFile(archive) as z:
        for entry in z.namelist():
            if not entry.startswith("source/") or not entry.endswith((".cpp", ".h", ".lua", ".sql")):
                continue
            data = z.read(entry).decode("utf-8", errors="replace")
            names = sorted(set(m.group(1) for m in SYMBOL.finditer(data) if m.group(1)))
            ids = sorted(set(ID.findall(data)))
            signals = dict(Counter(SPELL.findall(data)))
            rows.append({"path": entry, "classes": names, "identifiers": ids,
                         "mechanic_signals": signals, "lines": data.count("\n") + 1})
    return {"schema": 1, "verified_reborn": False, "entries": rows}

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("archive")
    p.add_argument("--output", default="instance-script-symbol-index.json")
    args = p.parse_args()
    result = build(args.archive)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(result, f, separators=(",", ":"))
    print(f"Indexed {len(result['entries'])} source files")
