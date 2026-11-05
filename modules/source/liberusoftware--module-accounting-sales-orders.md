# liberusoftware/module-accounting-sales-orders: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Accounting sales orders domain module.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [accounting-sales-orders](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-accounting-erp-laravel-filament, `accounting-sales-orders`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-accounting-sales-orders` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `accounting-sales-orders` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Accounting\\SalesOrders\\SalesOrdersServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\Accounting\\SalesOrders\\SalesOrdersServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/composer.json) · [module.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/module.json).

**Declared capabilities:** accounting.sales-orders

**Declared features:** Accepted demand, Allocation/fulfillment references, Deposits, Partial invoicing, Status, Cancellation, Billing/Ecommerce integration

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Accounting\\SalesOrders\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/AddFulfillmentReference.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/src/Actions/AddFulfillmentReference.php) | `public function handle(SalesOrder $order, array $attributes): SalesOrderAllocation` |
| [src/Actions/AddSalesOrderDeposit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/src/Actions/AddSalesOrderDeposit.php) | `public function handle(SalesOrder $order, array $attributes): SalesOrderDeposit` |
| [src/Actions/CreateSalesOrder.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/src/Actions/CreateSalesOrder.php) | `public function handle(array $attributes, array $lines): SalesOrder` |
| [src/Actions/RecordPartialInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/src/Actions/RecordPartialInvoice.php) | `public function handle(SalesOrder $order, float $amount, string $invoiceReference): SalesOrder` |
| [src/Actions/TransitionSalesOrder.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/src/Actions/TransitionSalesOrder.php) | `public function handle(SalesOrder $order, OrderStatus\|string $status): SalesOrder` |
| [src/Queries/SalesOrderQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/src/Queries/SalesOrderQuery.php) | `public function paginate(?string $customer = null, ?string $status = null, int $perPage = 25, ?int $teamId = null): LengthAwarePaginator` |

Other non-legacy PHP sources: [src/Enums/OrderStatus.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/src/Enums/OrderStatus.php) · [src/Exceptions/InvalidSalesOrder.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/src/Exceptions/InvalidSalesOrder.php) · [src/Models/SalesOrder.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/src/Models/SalesOrder.php) · [src/Models/SalesOrderAllocation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/src/Models/SalesOrderAllocation.php) · [src/Models/SalesOrderDeposit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/src/Models/SalesOrderDeposit.php) · [src/Models/SalesOrderItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/src/Models/SalesOrderItem.php) · [src/SalesOrdersServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/src/SalesOrdersServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_25_160000_create_accounting_sales_order_tables.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/database/migrations/2026_08_25_160000_create_accounting_sales_order_tables.php)
- [database/migrations/2026_08_29_000001_add_team_id_to_accounting_sales_orders.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/database/migrations/2026_08_29_000001_add_team_id_to_accounting_sales_orders.php)

[src/Enums/OrderStatus.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/src/Enums/OrderStatus.php): `Draft = 'draft'`, `Confirmed = 'confirmed'`, `PartiallyInvoiced = 'partially_invoiced'`, `Invoiced = 'invoiced'`, `Cancelled = 'cancelled'`.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
