# liberusoftware/module-browser-game-collections: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Provider-neutral Browser Game Collections capability.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [browser-game](../../projects/browser-game/SOURCE-MODULES.md) | [browser-game-collections](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-collections/composer.json) | `790fdffebd3a` | [Variant 1](#variant-1) | 2 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: browser-game-laravel, `browser-game-collections`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-browser-game-collections` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `browser-game-collections` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\BrowserGame\\Collections\\CollectionsServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `false` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-collections/composer.json) · [module.json](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-collections/module.json).

**Declared capabilities:** browser-game.collections

**Declared features:** Achievements and titles, Reputation, pets, and mounts, Housing and cosmetics, Collection progress

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/events` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\BrowserGame\\Collections\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Queries/CollectionsQuery.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-collections/src/Queries/CollectionsQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder`<br>`public function availableAchievements(?string $tenantId, ?string $teamId): Builder`<br>`public function forActor(string $actorId, ?string $tenantId, ?string $teamId): Builder`<br>`public function unlockedForActor(string $actorId, ?string $tenantId, ?string $teamId): Builder` |
| [src/Support/CollectionsManager.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-collections/src/Support/CollectionsManager.php) | `public function define(string $name, array $data = [], ?string $tenantId = null, ?string $teamId = null): CollectionsRecord`<br>`public function addEntry(CollectionsRecord $collection, string $entryKey, string $name, int $requiredQuantity = 1, array $reward = [], array $data = [], ?string $tenantId = null, ?string $teamId = null): mixed`<br>`public function defineCollection(string $name, string $kind = 'achievement', array $data = [], bool $repeatable = false, ?string $tenantId = null, ?string $teamId = null): CollectionsRecord`<br>`public function defineAchievement(string $name, array $data = [], bool $repeatable = false, ?string $tenantId = null, ?string $teamId = null): CollectionsRecord`<br>`public function defineTitle(string $name, array $data = [], ?string $tenantId = null, ?string $teamId = null): CollectionsRecord`<br>`public function defineReputation(string $name, array $data = [], ?string $tenantId = null, ?string $teamId = null): CollectionsRecord`<br>`public function definePet(string $name, array $data = [], ?string $tenantId = null, ?string $teamId = null): CollectionsRecord`<br>`public function defineMount(string $name, array $data = [], ?string $tenantId = null, ?string $teamId = null): CollectionsRecord`<br>`public function defineHousing(string $name, array $data = [], ?string $tenantId = null, ?string $teamId = null): CollectionsRecord`<br>`public function defineCosmetic(string $name, array $data = [], ?string $tenantId = null, ?string $teamId = null): CollectionsRecord`<br>`public function record(string $actorId, CollectionsRecord $collection, string $entryKey, int $quantity = 1, ?string $idempotencyKey = null, ?string $tenantId = null, ?string $teamId = null): CollectionProgress` |

Other non-legacy PHP sources: [src/CollectionsServiceProvider.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-collections/src/CollectionsServiceProvider.php) · [src/Events/CollectionProgressRecorded.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-collections/src/Events/CollectionProgressRecorded.php) · [src/Events/CollectionRewardGranted.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-collections/src/Events/CollectionRewardGranted.php) · [src/Events/CollectionsDefined.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-collections/src/Events/CollectionsDefined.php) · [src/Models/CollectionEntry.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-collections/src/Models/CollectionEntry.php) · [src/Models/CollectionProgress.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-collections/src/Models/CollectionProgress.php) · [src/Models/CollectionsRecord.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-collections/src/Models/CollectionsRecord.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_000507_create_browser_game_collections_tables.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-collections/database/migrations/2026_08_24_000507_create_browser_game_collections_tables.php)
- [database/migrations/2026_08_24_001000_add_collection_progress_lifecycle_fields.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-collections/database/migrations/2026_08_24_001000_add_collection_progress_lifecycle_fields.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **2**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Pest.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-collections/tests/Pest.php)
- [tests/Unit/CollectionsBoundaryTest.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-collections/tests/Unit/CollectionsBoundaryTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
