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
import re
import urllib.request
import zipfile

API = "https://api.github.com"
SOURCE = "Conquest-of-AzerothCore/azerothcore-wotlk-coa"
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
    ap.add_argument("--ref", default="main", help="CoA core branch, tag, or commit")
    ap.add_argument("--output", default="coa-core-instance-scripts.zip")
    ap.add_argument("--include-sql", action="store_true", help="Include relevant SQL update files (can be large)")
    args = ap.parse_args()
    ref = json.loads(request(f"{API}/repos/{SOURCE}/commits/{args.ref}"))
    sha = ref["sha"]
    tree = json.loads(request(f"{API}/repos/{SOURCE}/git/trees/{sha}?recursive=1"))
    if tree.get("truncated"):
        raise RuntimeError("GitHub tree was truncated; refusing to produce an incomplete archive")
    entries = []
    for node in tree["tree"]:
        if node["type"] != "blob":
            continue
        path = node["path"]
        if path.startswith(SCRIPT_PREFIX + REGIONS) and path.endswith((".cpp", ".h")):
            entries.append(path)
        elif args.include_sql and path.startswith(SQL_PREFIX) and path.endswith(".sql"):
            if any(word in path.lower() for word in INSTANCE_WORDS):
                entries.append(path)
    if not entries:
        raise RuntimeError("No matching files: check source tree or ref")
    output = pathlib.Path(args.output)
    manifest = {"source": f"https://github.com/{SOURCE}", "revision": sha,
                "evidence": "assumed-coa-core", "verified_on_conquest_reborn": False,
                "scripts": [], "sql_filter": "filename-based only; not exhaustive" if args.include_sql else "not included"}
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as z:
        for i, path in enumerate(entries, 1):
            data = request(f"{API}/repos/{SOURCE}/contents/{path}?ref={sha}")
            # Contents API defaults to base64; prefer the raw download URL via the blob API.
            obj = json.loads(data)
            import base64
            if obj.get("encoding") != "base64":
                raise RuntimeError(f"Unexpected content encoding for {path}")
            raw = base64.b64decode(obj["content"])
            z.writestr("source/" + path, raw)
            manifest["scripts"].append({"path": path, "blob_sha": obj["sha"], "bytes": len(raw)})
            if i % 100 == 0:
                print(f"Collected {i}/{len(entries)} files", flush=True)
        z.writestr("manifest.json", json.dumps(manifest, indent=2) + "\n")
        z.writestr("README.txt", "Public CoA/AzerothCore reference scripts, NOT verified Conquest Reborn scripts. Original licensing applies; see source repository LICENSE (GPL-2.0).\n")
    print(f"Saved {output} with {len(entries)} files at {sha}")

if __name__ == "__main__":
    main()
