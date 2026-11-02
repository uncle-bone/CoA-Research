const PAGES_ORIGIN = "https://uncle-bone.github.io";
const PAGES_PREFIX = "/CoA-Research";
const ADDON_REPOS = new Set([
  "AtlasLoot-CoA",
  "BoneUI",
  "Cell-CoA",
  "CoA-Item-Search",
  "ConquestWorldMapImprovement",
  "DBM-CoA",
  "Details",
  "ElvUI-CoA",
  "LootCollector",
  "Mapster-CoA",
  "MRT-CoA",
  "Nameplates",
  "NovaInstanceTracker",
  "Questie-X",
  "Refactor-CoA",
  "SexyMap-CoA",
  "SilverDragon",
  "UnclePlus-CoA",
  "UncleTranslate-CoA",
  "VeilForge-CoA",
  "WeakAuras-CoA",
  "Zygor-CoA",
  "WhatsTraining-CoA",
  "RetailGuildPane-CoA",
  "RXPGuides-CoA",
  "BoneProfiler",
  "pfQuest-CoA"
]);

function messagePage(title, message, status) {
  return new Response(`<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>${title} · BoneArchive</title><body style="margin:0;background:#151a1c;color:#eee8df;font:16px/1.6 system-ui,sans-serif"><main style="max-width:640px;margin:12vh auto;padding:28px"><p style="color:#d5b477;font-size:12px;letter-spacing:.12em;text-transform:uppercase">BoneArchive · Addon downloads</p><h1>${title}</h1><p>${message}</p><p><a style="color:#f0bd74" href="https://github.com/uncle-bone?tab=repositories">Browse GitHub repositories ↗</a></p></main></body></html>`, {
    status,
    headers: { "Content-Type": "text/html; charset=utf-8", "Cache-Control": "no-store" }
  });
}

async function latestAddonDownload(repo) {
  if (!ADDON_REPOS.has(repo)) return messagePage("Addon not found", "This download link is not in the BoneArchive addon catalog.", 404);

  const apiUrl = `https://api.github.com/repos/uncle-bone/${repo}/releases/latest`;
  const releaseResponse = await fetch(apiUrl, {
    headers: { Accept: "application/vnd.github+json", "User-Agent": "BoneArchive-addon-downloads" },
    cf: { cacheEverything: true, cacheTtl: 30 }
  });

  if (releaseResponse.status === 404) {
    return messagePage("No release published yet", `${repo} does not have a published stable release yet. Check its GitHub repository for project updates.`, 404);
  }
  if (!releaseResponse.ok) {
    return messagePage("Release lookup unavailable", "GitHub could not provide the latest release right now. Please try again shortly or open the repository.", 502);
  }

  let release;
  try {
    release = await releaseResponse.json();
  } catch {
    return messagePage("Release lookup unavailable", "GitHub returned release data that could not be read. Please use the repository link.", 502);
  }

  const zipAssets = Array.isArray(release.assets)
    ? release.assets.filter(asset => typeof asset.name === "string" && asset.name.toLowerCase().endsWith(".zip"))
    : [];
  if (zipAssets.length !== 1) {
    return messagePage("Download not available", "This release does not contain exactly one ZIP package, so BoneArchive cannot choose the correct download safely. Please use the repository release page.", 503);
  }

  const assetUrl = new URL(zipAssets[0].browser_download_url || "");
  const allowedPrefix = `/uncle-bone/${repo}/releases/download/`;
  if (assetUrl.protocol !== "https:" || assetUrl.hostname !== "github.com" || !assetUrl.pathname.startsWith(allowedPrefix)) {
    return messagePage("Download not available", "The release asset link did not match this repository. Please use the repository page.", 502);
  }

  return new Response(null, {
    status: 302,
    headers: {
      Location: assetUrl.href,
      "Cache-Control": "no-store"
    }
  });
}

export default {
  async fetch(request) {
    const incoming = new URL(request.url);
    const pathname = incoming.pathname || "/";
    if (pathname.includes("\\\\") || pathname.split("/").includes("..")) {
      return new Response("Invalid path", { status: 400 });
    }

    const method = request.method.toUpperCase();
    if (method !== "GET" && method !== "HEAD") {
      return new Response("Method not allowed", {
        status: 405,
        headers: { Allow: "GET, HEAD" }
      });
    }

    const downloadMatch = pathname.match(/^\/download\/([^/]+)\/?$/);
    if (downloadMatch) return latestAddonDownload(downloadMatch[1]);
    if (pathname.startsWith("/download/")) {
      return messagePage("Addon not found", "This download link is not in the BoneArchive addon catalog.", 404);
    }

    const target = new URL(PAGES_PREFIX + (pathname === "/" ? "/" : pathname), PAGES_ORIGIN);
    target.search = incoming.search;
    if (pathname === "/" || pathname.endsWith(".html")) target.searchParams.set("_bonearchive_release", "20261030-24");

    const headers = new Headers(request.headers);
    headers.delete("host");

    let upstream = await fetch(new Request(target, { method, headers, redirect: "manual" }), {
      cf: { cacheEverything: true, cacheTtl: 300 }
    });

    if (upstream.status === 404 && method === "GET" &&
        (request.headers.get("accept") || "").includes("text/html")) {
      const fallback = new URL(PAGES_PREFIX + "/index.html", PAGES_ORIGIN);
      fallback.searchParams.set("_bonearchive_release", "20261030-24");
      upstream = await fetch(new Request(fallback, { method, headers, redirect: "manual" }), {
        cf: { cacheEverything: true, cacheTtl: 60 }
      });
    }

    const response = new Response(upstream.body, upstream);
    const location = response.headers.get("location");
    const pagesBase = PAGES_ORIGIN + PAGES_PREFIX;
    if (location && location.startsWith(pagesBase)) {
      response.headers.set("location", incoming.origin + location.slice(pagesBase.length));
    }
    response.headers.set("cache-control", "public, max-age=0, must-revalidate");
    return response;
  }
};
