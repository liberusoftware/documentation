# liberusoftware/module-browser-game-crafting: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Provider-neutral Browser Game Crafting capability.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [browser-game](../../projects/browser-game/SOURCE-MODULES.md) | [browser-game-crafting](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/composer.json) | `790fdffebd3a` | [Variant 1](#variant-1) | 3 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: browser-game-laravel, `browser-game-crafting`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-browser-game-crafting` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `browser-game-crafting` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\BrowserGame\\Crafting\\CraftingServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `false` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/composer.json) · [module.json](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/module.json).

**Declared capabilities:** browser-game.crafting

**Declared features:** Recipe definitions and material rules, Profession progression, Resource consumption and quality, Transactional crafting queues, Discovery, salvage, and provenance outputs

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/events` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\BrowserGame\\Crafting\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Queries/CraftingQuery.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Queries/CraftingQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |
| [src/Support/CraftingManager.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Support/CraftingManager.php) | `public function define(string $name, array $data = [], ?string $tenantId = null, ?string $teamId = null): CraftingRecord`<br>`public function grantResource(string $actorId, string $resourceKey, int $quantity, ?string $tenantId = null, ?string $teamId = null): CraftingResource`<br>`public function setProfession(string $actorId, string $profession, int $level = 1, int $experience = 0, ?string $tenantId = null, ?string $teamId = null): CraftingProfession`<br>`public function gainProfessionExperience(string $actorId, string $profession, int $amount): CraftingProfession`<br>`public function discover(string $actorId, CraftingRecord $recipe, ?string $tenantId = null, ?string $teamId = null): CraftingDiscovery`<br>`public function queueCraft(string $actorId, CraftingRecord $recipe, int $quantity = 1, int $quality = 100, ?string $idempotencyKey = null, int $actorLevel = 1, ?string $tenantId = null, ?string $teamId = null): CraftingQueue`<br>`public function complete(CraftingQueue $queue): CraftingQueue`<br>`public function cancel(CraftingQueue $queue): CraftingQueue`<br>`public function salvage(CraftingQueue $queue): CraftingQueue` |

Other non-legacy PHP sources: [src/CraftingServiceProvider.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/CraftingServiceProvider.php) · [src/Events/CraftingCancelled.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Events/CraftingCancelled.php) · [src/Events/CraftingCompleted.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Events/CraftingCompleted.php) · [src/Events/CraftingDefined.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Events/CraftingDefined.php) · [src/Events/CraftingDiscovered.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Events/CraftingDiscovered.php) · [src/Events/CraftingFailed.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Events/CraftingFailed.php) · [src/Events/CraftingQueued.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Events/CraftingQueued.php) · [src/Events/CraftingSalvaged.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Events/CraftingSalvaged.php) · [src/Models/CraftingDiscovery.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Models/CraftingDiscovery.php) · [src/Models/CraftingOutput.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Models/CraftingOutput.php) · [src/Models/CraftingProfession.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Models/CraftingProfession.php) · [src/Models/CraftingQueue.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Models/CraftingQueue.php) · [src/Models/CraftingRecord.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Models/CraftingRecord.php) · [src/Models/CraftingResource.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/src/Models/CraftingResource.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_000503_create_browser_game_crafting_tables.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/database/migrations/2026_08_24_000503_create_browser_game_crafting_tables.php)
- [database/migrations/2026_08_25_000512_scope_crafting_player_state.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/database/migrations/2026_08_25_000512_scope_crafting_player_state.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **3**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Pest.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/tests/Pest.php)
- [tests/Unit/CraftingBehaviorTest.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/tests/Unit/CraftingBehaviorTest.php)
- [tests/Unit/CraftingBoundaryTest.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-crafting/tests/Unit/CraftingBoundaryTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
