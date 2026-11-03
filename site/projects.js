(() => {
  'use strict';
  const focus = [
    {
      name: 'BoneArchive & CoA Research',
      status: 'Ongoing · research + website',
      repo: 'https://github.com/uncle-bone/CoA-Research',
      text: 'Expand the CoA source archive and turn it into useful, searchable class/spec, spell, talent, gear, loot, performance, build, and addon research—keeping archived candidates separate from facts verified in the live client.'
    },
    {
      name: 'DBM-CoA',
      status: 'Performance · test work',
      repo: 'https://github.com/uncle-bone/DBM-CoA',
      text: 'Keep AutoLearner useful without making the game work harder than needed. Review memory, stutter, and module loading while preserving encounter timers, learning, and community sharing.'
    },
    {
      name: 'WeakAuras-CoA',
      status: 'v1.0.7 · memory work ongoing',
      repo: 'https://github.com/uncle-bone/WeakAuras-CoA',
      text: 'Reduce memory retained by the options editor safely. Test clearing temporary editor caches while preserving saved auras, imports, triggers, animations, and supported UI setups.'
    },
    {
      name: 'Zygor-CoA',
      status: 'Guide audit · CoA integration',
      repo: 'https://github.com/uncle-bone/Zygor-CoA',
      text: 'Connect the guide viewer more deeply with Conquest Reborn’s custom classes and quest data. Audit bundled guides and build verified custom routes, starting with Pale Reach.'
    },
    {
      name: 'pfQuest-CoA',
      status: 'Active replacement · quest discovery + sharing',
      repo: 'https://github.com/uncle-bone/pfQuest-CoA',
      text: 'Maintain pfQuest-CoA as the replacement for discontinued Questie-X, with CoA quest discovery, shared-channel compatibility, and accessible in-game sync controls.'
    },
    {
      name: 'LootCollector',
      status: 'Map stability · compatibility',
      repo: 'https://github.com/uncle-bone/LootCollector',
      text: 'Keep Worldforged, rare, treasure, and loot discoveries useful while checking map-marker stability, UI compatibility, and a possible performance interaction with DBM sharing.'
    },
    {
      name: 'VeilForge-CoA',
      status: 'Client graphics mod · compatibility test pending',
      repo: 'https://github.com/uncle-bone/VeilForge-CoA',
      text: 'Package Lumenveil atmospheric effects and DXVK for Ascension.exe with a local data-generation helper. v1.0.1 is a direct-extract release; back up game graphics files first. Windows and in-game compatibility still need independent testing.'
    }
  ];
  const more = [
    ['Raid tools', [
      ['Details', 'Resolve CoA class/spec attribution and combat-history details; the latest release still needs full live-client validation.', 'https://github.com/uncle-bone/Details', 'v1.1.7 · validation ongoing'],
      ['MRT-CoA', 'Experiment with CoA spellbook scanning and cooldown displays using observed/scanned spells, not guessed full class coverage.', 'https://github.com/uncle-bone/MRT-CoA', 'v0.20 · experimental']
    ]],
    ['Loot and research tools', [
      ['AtlasLoot-CoA', 'Build the phase-based BiS browser and item tooltips. Phase 1/2 controls exist; verified gear lists still need to be populated.', 'https://github.com/uncle-bone/AtlasLoot-CoA', 'v8.1.6 · data work'],
      ['CoA Item Search', 'Use adjustable item scanning and saved progress to expand the research archive; 1,353 extracted item records have been backed up.', 'https://github.com/uncle-bone/CoA-Item-Search', 'v1.0.1 · research tool']
    ]],
    ['Interface and player tools', [
      ['ElvUI-CoA', 'Maintain the CoA interface package and its custom resource bars and helper components.', 'https://github.com/uncle-bone/ElvUI-CoA', 'v1.0.1 · maintenance'],
      ['Cell-CoA', 'Adapt the Cell raid-frame addon for the Conquest Reborn 3.3.5a client.', 'https://github.com/uncle-bone/Cell-CoA', 'v1.0.2 · client checks'],
      ['Nameplates', 'Keep custom CoA nameplates and threat support moving; the latest custom/summon package is a prerelease.', 'https://github.com/uncle-bone/Nameplates', 'v1.4.0 · prerelease'],
      ['BoneUI', 'Develop a standalone early UI build with movable unit frames and a player cast/channel timer.', 'https://github.com/uncle-bone/BoneUI', 'v1.1.0 · alpha'],
      ['SexyMap-CoA', 'Add minimap looks and a combined addon-button collector, with compatibility polish for common CoA UI setups.', 'https://github.com/uncle-bone/SexyMap-CoA', 'v1.1.5 · continued polish']
    ]],
    ['Map and compatibility addons', [
      ['Mapster-CoA', 'Customize the world map with scaling, coordinates, group icons, fog-of-war, instance maps, and integrated zoom. Review README compatibility notes for your UI setup.', 'https://github.com/uncle-bone/Mapster-CoA', 'v1.1.1 · ElvUI compatibility update'],
      ['ConquestWorldMapImprovement', 'Compatibility layer for world-map zoom and marker rendering alongside Mapster, Magnify, pfQuest-CoA, LootCollector, and map overlays. Check release notes for addon combinations.', 'https://github.com/uncle-bone/ConquestWorldMapImprovement', 'v0.15.1 · compatibility update']
    ]],
    ['Tracking, utilities, and experiments', [
      ['NecroMinions-CoA', 'Necromancer minion HUD, current-minion tracking, and combat-log estimates. v0.8.6 is stable; generic per-minion dismissal remains unavailable until the client exposes a verified targeted operation.', 'https://github.com/uncle-bone/NecroMinions-CoA', 'v0.8.6 · stable'],
      ['SilverDragon', 'Adapt rare alerts and sighting history for Conquest Reborn, including optional map integrations.', 'https://github.com/uncle-bone/SilverDragon', 'v1.0.1-CoA · testing'],
      ['UnclePlus-CoA', 'A separate Conquest Reborn utility-addon package, tracked independently from the larger UI ports.', 'https://github.com/uncle-bone/UnclePlus-CoA', 'CR test build'],
      ['Refactor-CoA', 'Keep addon refactor and packaging experiments in their own repository.', 'https://github.com/uncle-bone/Refactor-CoA', 'Separate workstream'],
      ['UncleTranslate-CoA', 'Paused at v1.3.0 after tests exposed missed Chinese and romanized chat; the next step needs real unseen-message translation.', 'https://github.com/uncle-bone/UncleTranslate-CoA', 'Paused · v1.3.0'],
      ['NovaInstanceTracker', 'Repository scaffold is present; public source and project notes have not been added yet.', 'https://github.com/uncle-bone/NovaInstanceTracker', 'Scaffold · details pending'],
      ['Questie-X', 'Discontinued: Uncle Bone no longer provides service or support. Direct questing users to pfQuest-CoA; the old repository is retained for reference.', 'https://github.com/uncle-bone/Questie-X', 'Discontinued · pfQuest-CoA recommended'],
      ['WhatsTraining-CoA', 'Trainer tracker with a spellbook-attached page and a catalog built from services actually observed at trainers. Historical spell-rank data is not treated as proof of trainer availability; current UI compatibility still needs in-game checks.', 'https://github.com/uncle-bone/WhatsTraining-CoA', 'Current release · trainer evidence only'],
      ['RetailGuildPane-CoA', 'Retail-inspired guild window in visual-preview stage. Roster, chat, custom-class behavior, and UI compatibility are not yet validated in game.', 'https://github.com/uncle-bone/RetailGuildPane-CoA', 'v1.2.0 · visual preview'],
      ['RXPGuides-CoA', 'Leveling-guide engine and CoA route research, beginning with Pale Reach. No playable, fully tested addon release is published yet.', 'https://github.com/uncle-bone/RXPGuides-CoA', 'Research · no tested release'],
      ['BoneProfiler', 'Standalone diagnostic for FPS drops, stutter, addon memory and CPU sampling, with copyable reports. Read its current release notes; CPU profiling adds overhead.', 'https://github.com/uncle-bone/BoneProfiler', 'Performance diagnostics']
    ]]
  ];

  const esc = value => String(value || '').replace(/[&<>"']/g, ch => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
  })[ch]);

  function renderCard(item) {
    return '<article class="work-card"><div class="work-card-meta"><span class="work-status">' + esc(item.status) + '</span></div>' +
      '<h3>' + esc(item.name) + '</h3><p>' + esc(item.text) + '</p>' +
      '<a href="' + esc(item.repo) + '" target="_blank" rel="noopener noreferrer">Project repository ↗</a></article>';
  }

  function renderMore([group, entries]) {
    return '<section class="work-group"><h4>' + esc(group) + '</h4><div class="work-mini-grid">' +
      entries.map(([name, text, repo, status]) => '<article class="work-mini"><div><strong>' + esc(name) +
        '</strong><span class="work-status">' + esc(status) + '</span></div><p>' + esc(text) +
        '</p><a href="' + esc(repo) + '" target="_blank" rel="noopener noreferrer">Repository ↗</a></article>').join('') +
      '</div></section>';
  }

  function mount() {
    const app = document.querySelector('#app');
    const updates = app && app.querySelector('.home-updates');
    if (!updates || app.querySelector('.home-projects')) return;
    const section = document.createElement('section');
    section.className = 'home-projects';
    section.innerHTML =
      '<div class="sectionline"><div><span class="eyebrow">THE WORKSHOP · 27 ADDONS · 1 GAME ENHANCEMENT · COA RESEARCH HUB</span><h2>What I’m working on</h2></div><span class="archive-wordmark">CoA addons · research · experiments</span></div>' +
      '<p class="work-intro">A snapshot of the bigger efforts and the wider addon lineup. Test builds and research are labeled honestly; a repository or release does not mean every feature has been validated in game.</p>' +
      '<div class="work-focus-grid">' + focus.map(renderCard).join('') + '</div>' +
      '<details class="work-more"><summary><span>Browse the rest of the workshop</span><b>22 more repositories · one discontinued · one scaffold</b></summary>' +
      '<div class="work-more-body">' + more.map(renderMore).join('') +
      '<aside class="work-research"><strong>Client modernization research</strong><p>Separately comparing newer Wrath client paths, including 3.4.3, as research. This is exploratory work—not a claim that Conquest Reborn runs on a newer client.</p><a href="https://github.com/uncle-bone/CoA-Research" target="_blank" rel="noopener noreferrer">Research hub ↗</a></aside>' +
      '<p class="work-footnote">Project notes checked against the public repositories and recent development chats on November 3, 2026. For current downloads and exact release status, open each repository.</p></div></details>';
    updates.insertAdjacentElement('afterend', section);
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', mount, { once: true });
  else mount();
  new MutationObserver(mount).observe(document.documentElement, { childList: true, subtree: true });
})();