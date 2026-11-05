# liberusoftware/module-browser-game-items: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Provider-neutral Browser Game Items capability.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [browser-game](../../projects/browser-game/SOURCE-MODULES.md) | [browser-game-items](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-items/composer.json) | `790fdffebd3a` | [Variant 1](#variant-1) | 2 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-browser-game-laravel-filament, `browser-game-items`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-browser-game-items` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `browser-game-items` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\BrowserGame\\Items\\ItemsServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `false` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-items/composer.json) · [module.json](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-items/module.json).

**Declared capabilities:** browser-game.items

**Declared features:** Item catalogue lifecycle, Typed item properties and stat bonuses, Transactional player inventory, Inventory queries and mutations, Items audit events

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/events` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\BrowserGame\\Items\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Queries/ItemsQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-items/src/Queries/ItemsQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |
| [src/Support/ItemsManager.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-items/src/Support/ItemsManager.php) | `public function define(string $name, array $data = [], ?string $tenantId = null, ?string $teamId = null): ItemsRecord`<br>`public function addToInventory(string\|int $playerId, ItemsRecord\|string $item, int $quantity = 1, array $provenance = [], ?string $tenantId = null, ?string $teamId = null): InventoryEntry`<br>`public function removeFromInventory(string\|int $playerId, ItemsRecord\|string $item, int $quantity = 1, ?string $tenantId = null, ?string $teamId = null): bool`<br>`public function inventory(string\|int $playerId, ?string $tenantId = null, ?string $teamId = null): Collection`<br>`public function equip(string\|int $playerId, InventoryEntry\|int $entry, ?string $slot = null, ?string $tenantId = null, ?string $teamId = null): InventoryEntry`<br>`public function unequip(string\|int $playerId, InventoryEntry\|int $entry, ?string $tenantId = null, ?string $teamId = null): InventoryEntry`<br>`public function bind(string\|int $playerId, InventoryEntry\|int $entry, ?string $tenantId = null, ?string $teamId = null): InventoryEntry`<br>`public function setProvenance(string\|int $playerId, InventoryEntry\|int $entry, array $provenance, ?string $tenantId = null, ?string $teamId = null): InventoryEntry`<br>`public function adjustDurability(string\|int $playerId, InventoryEntry\|int $entry, int $delta, ?string $tenantId = null, ?string $teamId = null): InventoryEntry`<br>`public function putInContainer(string\|int $playerId, InventoryEntry\|int $entry, InventoryEntry\|int $container, ?string $tenantId = null, ?string $teamId = null): InventoryEntry` |

Other non-legacy PHP sources: [src/Events/ItemsDefined.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-items/src/Events/ItemsDefined.php) · [src/ItemsServiceProvider.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-items/src/ItemsServiceProvider.php) · [src/Models/InventoryEntry.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-items/src/Models/InventoryEntry.php) · [src/Models/ItemsRecord.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-items/src/Models/ItemsRecord.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_000502_create_browser_game_items_tables.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-items/database/migrations/2026_08_24_000502_create_browser_game_items_tables.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **2**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Pest.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-items/tests/Pest.php)
- [tests/Unit/ItemsBoundaryTest.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-items/tests/Unit/ItemsBoundaryTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
