#!/usr/bin/env python3
"""Validate structural integrity of the DBM-CoA v6 research package."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "dbm" / "v6"
EXPECTED = {
    "MASTER-RESEARCH-REPORT.md", "INSTANCE-REGISTRY.json", "PRIORITY-SEVEN-DUNGEONS.json",
    "BOSS-REGISTRY.json", "SPELL-MECHANICS.json", "ENCOUNTER-TIMINGS.json",
    "DIFFICULTY-MATRIX.json", "INSTANCE-SOURCE-MAP.json", "DBM-MODULE-COVERAGE.json",
    "DBM-V6-IMPLEMENTATION-SPEC.md", "LEARNER-AND-SMARTSYNC-AUDIT.md",
    "TEST-AND-VALIDATION-PLAN.md", "UNRESOLVED-RESEARCH-GAPS.md",
    "SOURCE-PROVENANCE.json", "V6-DEVELOPMENT-HANDOFF.md",
}
EXPECTED_SEVEN = {"manastorm", "shadowbone-depths", "temple-of-embers", "radiant-spring", "road-to-the-other-side", "vaults-of-inquisition", "blackrock-caverns"}


def main():
    missing = EXPECTED - {p.name for p in OUT.iterdir()}
    assert not missing, f"Missing deliverables: {sorted(missing)}"
    parsed = {}
    for p in OUT.glob("*.json"):
        parsed[p.name] = json.loads(p.read_text(encoding="utf-8"))
    seven = parsed["PRIORITY-SEVEN-DUNGEONS.json"]["dungeons"]
    ids = [row["id"] for row in seven]
    assert len(ids) == 7 and set(ids) == EXPECTED_SEVEN and len(set(ids)) == 7
    for row in seven:
        assert row["live_verified"] is False, f"Unsubstantiated live promotion: {row['id']}"
        for ref in row["source_references"]:
            assert (ROOT / ref).is_file(), f"Broken research reference: {row['id']} -> {ref}"
    registry = parsed["INSTANCE-REGISTRY.json"]["instances"]
    assert len(registry) >= 22
    for doc in ("MASTER-RESEARCH-REPORT.md", "DBM-V6-IMPLEMENTATION-SPEC.md", "UNRESOLVED-RESEARCH-GAPS.md"):
        assert (OUT / doc).stat().st_size > 300
    print(f"PASS: {len(EXPECTED)} required deliverables present")
    print(f"PASS: {len(parsed)} JSON files parse")
    print(f"PASS: seven named priority targets present; all explicitly not live-verified")
    print(f"PASS: {len(registry)} instance registry entries; 22+ corpus rows retained")


if __name__ == "__main__":
    main()
