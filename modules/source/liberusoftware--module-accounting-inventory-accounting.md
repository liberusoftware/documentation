# liberusoftware/module-accounting-inventory-accounting: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Inventory valuation, cost layers, cost of sales, landed costs, adjustments, write-downs and reconciliation.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [accounting-inventory-accounting](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: accounting-erp-laravel, `accounting-inventory-accounting`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-accounting-inventory-accounting` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `accounting-inventory-accounting` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Accounting\\InventoryAccounting\\InventoryAccountingServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\Accounting\\InventoryAccounting\\InventoryAccountingServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/composer.json) · [module.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/module.json).

**Declared capabilities:** accounting.inventory-accounting

**Declared features:** Perpetual and periodic methods, Valuation and cost layers, Cost of sales and landed cost, Adjustments and write-downs, Subledger reconciliation

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Accounting\\InventoryAccounting\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/AdjustInventory.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Actions/AdjustInventory.php) | `public function handle(InventoryItem $item, array $attributes): InventoryAdjustment` |
| [src/Actions/ApplyLandedCost.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Actions/ApplyLandedCost.php) | `public function handle(InventoryItem $item, array $attributes): LandedCost` |
| [src/Actions/CreateInventoryItem.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Actions/CreateInventoryItem.php) | `public function handle(array $attributes): InventoryItem` |
| [src/Actions/IssueInventory.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Actions/IssueInventory.php) | `public function handle(InventoryItem $item, array $attributes): float` |
| [src/Actions/ReceiveInventory.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Actions/ReceiveInventory.php) | `public function handle(InventoryItem $item, array $attributes): CostLayer` |
| [src/Actions/ReconcileInventory.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Actions/ReconcileInventory.php) | `public function handle(array $attributes, ?InventoryItem $item = null): InventoryReconciliation` |
| [src/Actions/WriteDownInventory.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Actions/WriteDownInventory.php) | `public function handle(InventoryItem $item, array $attributes): InventoryWriteDown` |
| [src/Queries/InventoryQuery.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Queries/InventoryQuery.php) | `public function paginate(?int $teamId = null, ?InventoryStatus $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function valuation(InventoryItem $item): array` |

Other non-legacy PHP sources: [src/Enums/InventoryStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Enums/InventoryStatus.php) · [src/Enums/MovementType.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Enums/MovementType.php) · [src/Enums/ValuationMethod.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Enums/ValuationMethod.php) · [src/Events/InventoryReconciled.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Events/InventoryReconciled.php) · [src/Exceptions/InvalidInventory.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Exceptions/InvalidInventory.php) · [src/InventoryAccountingServiceProvider.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/InventoryAccountingServiceProvider.php) · [src/Models/CostLayer.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Models/CostLayer.php) · [src/Models/InventoryAdjustment.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Models/InventoryAdjustment.php) · [src/Models/InventoryItem.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Models/InventoryItem.php) · [src/Models/InventoryMovement.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Models/InventoryMovement.php) · [src/Models/InventoryReconciliation.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Models/InventoryReconciliation.php) · [src/Models/InventoryWriteDown.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Models/InventoryWriteDown.php) · [src/Models/LandedCost.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Models/LandedCost.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_26_018000_create_accounting_inventory_tables.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/database/migrations/2026_08_26_018000_create_accounting_inventory_tables.php)

[src/Enums/InventoryStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Enums/InventoryStatus.php): `Active = 'active'`, `Closed = 'closed'`.

[src/Enums/MovementType.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Enums/MovementType.php): `Receipt = 'receipt'`, `Issue = 'issue'`, `Adjustment = 'adjustment'`, `LandedCost = 'landed_cost'`, `WriteDown = 'write_down'`.

[src/Enums/ValuationMethod.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Enums/ValuationMethod.php): `Perpetual = 'perpetual'`, `Periodic = 'periodic'`, `FIFO = 'fifo'`, `WeightedAverage = 'weighted_average'`.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
