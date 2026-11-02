#!/usr/bin/env python3
"""Validate shared-reference v1 files using Python standard library only."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "datasets" / "shared-reference" / "v1"
NAMES = ("classes", "specializations", "spells", "pets-and-summons",
         "quests-and-npcs", "items-and-loot", "combat-attribution", "client-compatibility")

def validate(root=ROOT):
    documents = {}
    for name in NAMES:
        path = root / (name + ".json")
        doc = json.loads(path.read_text(encoding="utf-8"))
        assert doc["schemaVersion"] == 1, path
        assert doc["recordCount"] == len(doc["records"]), path
        assert isinstance(doc["limitations"], list) and doc["limitations"], path
        for record in doc["records"]:
            assert record["sourcePath"] and record["sourceExtractionDate"], (path, record)
            assert record["confidence"] and record["liveRebornVerified"] is False, (path, record)
        documents[name] = doc
    classes = documents["classes"]["records"]
    specs = documents["specializations"]["records"]
    ids = {c["classId"] for c in classes}
    assert len(ids) == len(classes) == 21
    spec_ids = {s["specId"] for s in specs}
    assert len(spec_ids) == len(specs) == 101
    assert all(s["classId"] in ids or s["classId"] < 12 for s in specs)
    for c in classes:
        assert set(c["specializationIds"]) == {s["specId"] for s in specs if s["classId"] == c["classId"]}
    assert all(r["classification"] == "quarantine" for r in documents["pets-and-summons"]["records"])
    assert all(r["classification"] == "quarantine" for r in documents["spells"]["records"])
    return {name: doc["recordCount"] for name, doc in documents.items()}

if __name__ == "__main__":
    print(json.dumps({"result": "pass", "counts": validate()}, sort_keys=True))
