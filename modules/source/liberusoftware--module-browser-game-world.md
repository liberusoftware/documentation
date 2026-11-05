# liberusoftware/module-browser-game-world: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Provider-neutral Browser Game world catalog, travel, weather, encounters, resources, NPCs, and unlocks.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [browser-game](../../projects/browser-game/SOURCE-MODULES.md) | [browser-game-world](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world/composer.json) | `790fdffebd3a` | [Variant 1](#variant-1) | 2 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-browser-game-laravel-filament, `browser-game-world`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-browser-game-world` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `browser-game-world` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\BrowserGame\\World\\WorldServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `false` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world/composer.json) · [module.json](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world/module.json).

**Declared capabilities:** browser-game.world

**Declared features:** Regions and locations, Maps and travel, Encounters and NPCs, Resources and weather, Unlocks

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/events` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\BrowserGame\\World\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Policies/WorldPolicy.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world/src/Policies/WorldPolicy.php) | `public function view(?string $tenantId, ?string $teamId, WorldEntity $entity): bool`<br>`public function manage(?string $actorId, ?string $tenantId, ?string $teamId, WorldEntity $entity): bool` |
| [src/Queries/WorldQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world/src/Queries/WorldQuery.php) | `public function visible(?string $tenantId, ?string $teamId, ?string $kind = null): Builder` |
| [src/Support/WorldManager.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world/src/Support/WorldManager.php) | `public function defineRegion(?string $tenantId, ?string $teamId, string $name, string $slug, array $attributes = [], ?string $worldId = null, ?string $unlockKey = null): WorldEntity`<br>`public function defineLocation(?string $tenantId, ?string $teamId, string $name, string $slug, array $attributes = [], ?string $worldId = null, ?string $unlockKey = null): WorldEntity`<br>`public function defineMap(?string $tenantId, ?string $teamId, string $name, string $slug, array $attributes = [], ?string $worldId = null, ?string $unlockKey = null): WorldEntity`<br>`public function defineEncounter(?string $tenantId, ?string $teamId, string $name, string $slug, array $attributes = [], ?string $worldId = null, ?string $unlockKey = null): WorldEntity`<br>`public function defineNpc(?string $tenantId, ?string $teamId, string $name, string $slug, array $attributes = [], ?string $worldId = null, ?string $unlockKey = null): WorldEntity`<br>`public function defineResource(?string $tenantId, ?string $teamId, string $name, string $slug, array $attributes = [], ?string $worldId = null, ?string $unlockKey = null): WorldEntity`<br>`public function defineWeather(?string $tenantId, ?string $teamId, string $name, string $slug, array $attributes = [], ?string $worldId = null, ?string $unlockKey = null): WorldEntity`<br>`public function defineUnlock(?string $tenantId, ?string $teamId, string $name, string $slug, array $attributes = [], ?string $worldId = null, ?string $unlockKey = null): WorldEntity`<br>`public function define(?string $tenantId, ?string $teamId, string $kind, string $name, string $slug, array $attributes = [], ?string $worldId = null, ?string $unlockKey = null): WorldEntity`<br>`public function travel(string $actorId, ?string $tenantId, ?string $teamId, ?WorldEntity $origin, WorldEntity $destination, ?string $idempotencyKey = null, array $metadata = []): WorldTravel`<br>`public function grantUnlock(string $actorId, WorldEntity\|string $entity, ?string $tenantId = null, ?string $teamId = null, ?string $idempotencyKey = null, array $metadata = []): WorldUnlock`<br>`public function revokeUnlock(string $actorId, WorldUnlock\|int\|string $unlock, ?string $tenantId = null, ?string $teamId = null): WorldUnlock`<br>`public function hasUnlock(string $actorId, string $unlockKey, ?string $tenantId = null, ?string $teamId = null): bool`<br>`public function update(WorldEntity $entity, ?string $tenantId, ?string $teamId, string $name, string $slug, string $status, array $attributes = [], ?array $coordinates = null, ?string $unlockKey = null): WorldEntity` |

Other non-legacy PHP sources: [src/Events/WorldEntityDefined.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world/src/Events/WorldEntityDefined.php) · [src/Events/WorldEntityUpdated.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world/src/Events/WorldEntityUpdated.php) · [src/Events/WorldTravelled.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world/src/Events/WorldTravelled.php) · [src/Events/WorldUnlockGranted.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world/src/Events/WorldUnlockGranted.php) · [src/Events/WorldUnlockRevoked.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world/src/Events/WorldUnlockRevoked.php) · [src/Models/WorldEntity.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world/src/Models/WorldEntity.php) · [src/Models/WorldTravel.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world/src/Models/WorldTravel.php) · [src/Models/WorldUnlock.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world/src/Models/WorldUnlock.php) · [src/WorldServiceProvider.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world/src/WorldServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_000200_create_browser_game_world_tables.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world/database/migrations/2026_08_24_000200_create_browser_game_world_tables.php)
- [database/migrations/2026_08_25_000300_create_browser_game_world_unlocks_table.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world/database/migrations/2026_08_25_000300_create_browser_game_world_unlocks_table.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **2**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Pest.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world/tests/Pest.php)
- [tests/Unit/WorldBoundaryTest.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-world/tests/Unit/WorldBoundaryTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
