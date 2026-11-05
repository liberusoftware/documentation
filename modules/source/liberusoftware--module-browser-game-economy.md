# liberusoftware/module-browser-game-economy: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Provider-neutral Browser Game Economy capability.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [browser-game](../../projects/browser-game/SOURCE-MODULES.md) | [browser-game-economy](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/composer.json) | `790fdffebd3a` | [Variant 1](#variant-1) | 3 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-browser-game-laravel-filament, `browser-game-economy`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-browser-game-economy` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `browser-game-economy` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\BrowserGame\\Economy\\EconomyServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `false` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/composer.json) · [module.json](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/module.json).

**Declared capabilities:** browser-game.economy

**Declared features:** Currency definitions and ledgers, Faucets and sinks, Vendor pricing and stock, Trading and marketplace listings, Fees, idempotency, and anti-abuse limits

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/events` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\BrowserGame\\Economy\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Queries/EconomyQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/src/Queries/EconomyQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |
| [src/Support/EconomyManager.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/src/Support/EconomyManager.php) | `public function define(string $name, array $data = [], ?string $tenantId = null, ?string $teamId = null): EconomyRecord`<br>`public function credit(string $actorId, string $currencyCode, int $amount, string $source = 'faucet', ?string $idempotencyKey = null, array $metadata = [], ?string $tenantId = null, ?string $teamId = null): EconomyLedgerEntry`<br>`public function debit(string $actorId, string $currencyCode, int $amount, string $source = 'sink', ?string $idempotencyKey = null, array $metadata = [], ?string $tenantId = null, ?string $teamId = null): EconomyLedgerEntry`<br>`public function transfer(string $senderId, string $recipientId, string $currencyCode, int $amount, ?string $idempotencyKey = null, ?string $tenantId = null, ?string $teamId = null): array`<br>`public function createVendor(string $name, array $data = [], ?string $tenantId = null, ?string $teamId = null): EconomyVendor`<br>`public function addOffer(EconomyVendor $vendor, string $itemKey, string $currencyCode, int $unitPrice, ?int $stock = null, ?int $maxPerActor = null, ?string $tenantId = null, ?string $teamId = null): EconomyVendorOffer`<br>`public function purchaseOffer(string $actorId, EconomyVendorOffer $offer, int $quantity = 1, ?string $tenantId = null, ?string $teamId = null): EconomyVendorOffer`<br>`public function createListing(string $sellerId, string $itemKey, string $currencyCode, int $quantity, int $unitPrice, array $assetReference = [], ?string $idempotencyKey = null, ?string $tenantId = null, ?string $teamId = null): EconomyListing`<br>`public function purchaseListing(string $buyerId, EconomyListing $listing, ?string $idempotencyKey = null, ?string $tenantId = null, ?string $teamId = null): EconomyListing`<br>`public function cancelListing(string $sellerId, EconomyListing $listing, ?string $tenantId = null, ?string $teamId = null): EconomyListing` |

Other non-legacy PHP sources: [src/EconomyServiceProvider.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/src/EconomyServiceProvider.php) · [src/Events/EconomyDefined.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/src/Events/EconomyDefined.php) · [src/Events/EconomyFeeCharged.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/src/Events/EconomyFeeCharged.php) · [src/Events/EconomyListingSold.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/src/Events/EconomyListingSold.php) · [src/Events/EconomyTransactionRecorded.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/src/Events/EconomyTransactionRecorded.php) · [src/Models/EconomyLedgerEntry.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/src/Models/EconomyLedgerEntry.php) · [src/Models/EconomyListing.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/src/Models/EconomyListing.php) · [src/Models/EconomyRecord.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/src/Models/EconomyRecord.php) · [src/Models/EconomyVendor.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/src/Models/EconomyVendor.php) · [src/Models/EconomyVendorOffer.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/src/Models/EconomyVendorOffer.php) · [src/Models/EconomyWallet.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/src/Models/EconomyWallet.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_000504_create_browser_game_economy_tables.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/database/migrations/2026_08_24_000504_create_browser_game_economy_tables.php)
- [database/migrations/2026_08_25_000200_add_scope_to_economy_marketplaces.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/database/migrations/2026_08_25_000200_add_scope_to_economy_marketplaces.php)
- [database/migrations/2026_08_25_000511_scope_economy_wallets_and_ledger.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/database/migrations/2026_08_25_000511_scope_economy_wallets_and_ledger.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **3**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Pest.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/tests/Pest.php)
- [tests/Unit/EconomyBehaviorTest.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/tests/Unit/EconomyBehaviorTest.php)
- [tests/Unit/EconomyBoundaryTest.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-economy/tests/Unit/EconomyBoundaryTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
