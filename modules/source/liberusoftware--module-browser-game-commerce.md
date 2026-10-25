# liberusoftware/module-browser-game-commerce: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Provider-neutral Browser Game Commerce capability.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [browser-game](../../projects/browser-game/SOURCE-MODULES.md) | [browser-game-commerce](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/composer.json) | `790fdffebd3a` | [Variant 1](#variant-1) | 2 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: browser-game-laravel, `browser-game-commerce`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-browser-game-commerce` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `browser-game-commerce` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\BrowserGame\\Commerce\\CommerceServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `false` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/composer.json) · [module.json](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/module.json).

**Declared capabilities:** browser-game.commerce

**Declared features:** Products and game-store offers, Retry-safe checkout and orders, Entitlements and delivery, Refunds and inventory limits

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/events` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\BrowserGame\\Commerce\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Queries/CommerceQuery.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/src/Queries/CommerceQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |
| [src/Support/CommerceManager.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/src/Support/CommerceManager.php) | `public function define(string $name, array $data = [], ?string $tenantId = null, ?string $teamId = null): CommerceRecord`<br>`public function createProduct(string $sku, string $name, string $currencyCode, int $price, array $delivery = [], ?int $stock = null, ?int $maxPerActor = null, array $data = [], ?string $tenantId = null, ?string $teamId = null): CommerceProduct`<br>`public function checkout(string $actorId, array $lines, ?string $idempotencyKey = null, ?string $tenantId = null, ?string $teamId = null): CommerceOrder`<br>`public function complete(CommerceOrder $order, ?string $actorId = null, ?string $tenantId = null, ?string $teamId = null): CommerceOrder`<br>`public function refund(CommerceOrder $order, ?string $actorId = null, ?string $tenantId = null, ?string $teamId = null): CommerceOrder` |

Other non-legacy PHP sources: [src/CommerceServiceProvider.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/src/CommerceServiceProvider.php) · [src/Events/CommerceDefined.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/src/Events/CommerceDefined.php) · [src/Models/CommerceEntitlement.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/src/Models/CommerceEntitlement.php) · [src/Models/CommerceOrder.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/src/Models/CommerceOrder.php) · [src/Models/CommerceOrderLine.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/src/Models/CommerceOrderLine.php) · [src/Models/CommerceProduct.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/src/Models/CommerceProduct.php) · [src/Models/CommerceRecord.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/src/Models/CommerceRecord.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_000509_create_browser_game_commerce_tables.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/database/migrations/2026_08_24_000509_create_browser_game_commerce_tables.php)
- [database/migrations/2026_08_25_000100_add_scope_to_commerce_products_and_orders.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/database/migrations/2026_08_25_000100_add_scope_to_commerce_products_and_orders.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **2**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Pest.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/tests/Pest.php)
- [tests/Unit/CommerceBoundaryTest.php](https://github.com/liberusoftware/browser-game-laravel/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/tests/Unit/CommerceBoundaryTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
