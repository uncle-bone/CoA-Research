#!/usr/bin/env python3
"""Collect the public CoA core's complete dungeon/raid script tree and source references.

Requires Python 3.9+ and network access to api.github.com. Optional GITHUB_TOKEN.
This does NOT claim these scripts are identical to Conquest Reborn's live server.
"""
import argparse
import io
import json
import os
import pathlib
import urllib.request
import zipfile

API = "https://api.github.com"
SOURCES = ("Conquest-of-AzerothCore/azerothcore-wotlk-coa", "azerothcore/azerothcore-wotlk", "TrinityCore/TrinityCore", "Zyth45/azerothcore-wotlk-coa", "cmangos/mangos-wotlk", "uncle-bone/CoA-Research")
REGIONS = ("EasternKingdoms/", "Kalimdor/", "Northrend/", "Outland/")
SCRIPT_PREFIX = "src/server/scripts/"
SQL_PREFIX = "data/sql/"
EXTENSIONS = (".cpp", ".h", ".sql")
INSTANCE_WORDS = ("instance_", "boss_", "dungeon", "raid", "creature", "smartai", "waypoint", "areatrigger", "gameobject")

def request(url):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "CoA-Research-instance-script-collector"}
    if os.getenv("GITHUB_TOKEN"):
        headers["Authorization"] = "Bearer " + os.environ["GITHUB_TOKEN"]
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=90) as r:
        return r.read()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ref", default=None, help="Override ref (single-source only)")
    ap.add_argument("--sources", nargs="+", default=list(SOURCES), help="owner/repo names")
    ap.add_argument("--output", default="coa-core-instance-scripts.zip")
    ap.add_argument("--include-sql", action="store_true", help="Include relevant SQL update files (can be large)")
    args = ap.parse_args()
    if args.ref and len(args.sources) != 1:
        ap.error("--ref requires exactly one --sources entry")
    output = pathlib.Path(args.output)
    manifest = {"schema": 2, "baseline": "assumed-coa-core",
                "verified_on_conquest_reborn": False, "sources": [], "files": [],
                "notes": ["This is a multi-source reference archive, not a verified Reborn script corpus.",
                          "SQL updates are included whole with --include-sql; database snapshots must be collected separately.",
                          "Multiple implementations of an encounter are alternatives, not merged behavior.",
                          "CoA-Research data is included as research evidence, not executable server AI."]}
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for source in args.sources:
            if "/" not in source or source.count("/") != 1:
                raise ValueError(f"Invalid owner/repo: {source}")
            revision = args.ref or json.loads(request(f"{API}/repos/{source}"))["default_branch"]
            sha = json.loads(request(f"{API}/repos/{source}/commits/{revision}"))["sha"]
            archive = request(f"https://codeload.github.com/{source}/zip/{sha}")
            count = 0
            with zipfile.ZipFile(io.BytesIO(archive)) as src:
                for info in src.infolist():
                    if info.is_dir():
                        continue
                    path = info.filename.split("/", 1)[-1]
                    lower = path.lower()
                    is_script = (
                        (path.startswith(SCRIPT_PREFIX) or "/scripts/" in lower or "/scriptdev2/" in lower)
                        and lower.endswith((".cpp", ".h", ".lua"))
                    )
                    is_research = source == "uncle-bone/CoA-Research" and (
                        path.startswith(("datasets/", "research/", "docs/"))
                        and lower.endswith((".json", ".jsonl", ".csv", ".md", ".txt", ".lua", ".sql"))
                    )
                    is_sql = args.include_sql and lower.endswith(".sql") and (
                        path.startswith(SQL_PREFIX) or "/sql/" in lower
                    )
                    if not (is_script or is_sql or is_research):
                        continue
                    raw = src.read(info)
                    dest = f"source/{source}/{path}"
                    z.writestr(dest, raw)
                    manifest["files"].append({"source": source, "revision": sha, "path": path,
                                              "bytes": len(raw), "kind": "research" if is_research else ("sql" if is_sql else "script")})
                    count += 1
            manifest["sources"].append({"repository": source, "revision": sha, "file_count": count})
            print(f"{source}: {count} files at {sha}", flush=True)
        if not manifest["files"]:
            raise RuntimeError("No matching scripts found")
        z.writestr("manifest.json", json.dumps(manifest, indent=2) + "\\n")
        z.writestr("README.txt", "Research reference archive. Scripts are not verified against Conquest Reborn. Each source retains its original copyright and license; consult upstream repositories before redistribution.\\n")
    print(f"Saved {output} with {len(manifest['files'])} files")

if __name__ == "__main__":
    main()
