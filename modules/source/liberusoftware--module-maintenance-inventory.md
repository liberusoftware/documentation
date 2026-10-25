# liberusoftware/module-maintenance-inventory: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Inventory domain module for Liberu Maintenance

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [maintenance](../../projects/maintenance/SOURCE-MODULES.md) | [module-maintenance-inventory](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/composer.json) | `c267d625e264` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: maintenance-laravel, `module-maintenance-inventory`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-maintenance-inventory` |
| Composer version field | `0.1.0` |
| Package type | `liberu-module` |
| Module manifest name | `module-maintenance-inventory` |
| Module version field | `0.1.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Modules\\Maintenance\\Inventory\\InventoryServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/composer.json) · [module.json](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/module.json).

**Declared capabilities:** maintenance.inventory

**Declared features:** Parts, Warehouses and vans, Stock ledger, Reservations, Issues and returns, Transfers, Reorder, Counts

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `liberusoftware/organizations-teams` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Modules\\Maintenance\\Inventory\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0", "liberusoftware/organizations-teams": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/AdjustStock.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/AdjustStock.php) | `public function handle(int $teamId, StockItem $item, int $delta, string $reason = 'adjustment', ?int $userId = null, ?string $notes = null): StockItem` |
| [src/Actions/CreateStockItem.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/CreateStockItem.php) | `public function handle(int $teamId, array $attributes): StockItem` |
| [src/Actions/DeleteStockItem.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/DeleteStockItem.php) | `public function handle(int $teamId, StockItem $item): void` |
| [src/Actions/IssueStock.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/IssueStock.php) | `public function __construct(private readonly AdjustStock $adjustStock)`<br>`public function handle(int $teamId, StockItem $item, int $quantity, ?int $userId = null, ?string $notes = null): StockItem` |
| [src/Actions/ReleaseReservedStock.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/ReleaseReservedStock.php) | `public function handle(int $teamId, StockItem $item, int $quantity): StockItem` |
| [src/Actions/ReserveStock.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/ReserveStock.php) | `public function handle(int $teamId, StockItem $item, int $quantity): StockItem` |
| [src/Actions/ReturnStock.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/ReturnStock.php) | `public function __construct(private readonly AdjustStock $adjustStock)`<br>`public function handle(int $teamId, StockItem $item, int $quantity, ?int $userId = null, ?string $notes = null): StockItem` |
| [src/Actions/UpdateStockItem.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/UpdateStockItem.php) | `public function handle(int $teamId, StockItem $item, array $attributes): StockItem` |
| [src/Policies/StockItemPolicy.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Policies/StockItemPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, StockItem $item): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, StockItem $item): bool`<br>`public function delete(object $user, StockItem $item): bool` |

Other non-legacy PHP sources: [src/InventoryServiceProvider.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/InventoryServiceProvider.php) · [src/Models/StockItem.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Models/StockItem.php) · [src/Models/StockMovement.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Models/StockMovement.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_25_070000_create_maintenance_stock_items_table.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/database/migrations/2026_08_25_070000_create_maintenance_stock_items_table.php)
- [database/migrations/2026_08_29_060000_create_maintenance_stock_movements_table.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/database/migrations/2026_08_29_060000_create_maintenance_stock_movements_table.php)
- [database/migrations/2026_08_29_080000_add_reserved_quantity_to_maintenance_stock_items.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/database/migrations/2026_08_29_080000_add_reserved_quantity_to_maintenance_stock_items.php)
- [database/migrations/2026_08_29_202000_add_legacy_part_details_to_maintenance_stock_items.php](https://github.com/liberusoftware/maintenance-laravel/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/database/migrations/2026_08_29_202000_add_legacy_part_details_to_maintenance_stock_items.php)

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
