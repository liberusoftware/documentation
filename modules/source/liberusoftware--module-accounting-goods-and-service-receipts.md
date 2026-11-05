# liberusoftware/module-accounting-goods-and-service-receipts: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Goods and service receipts, quantities, variance, returns, attachments and accruals.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [accounting-goods-and-service-receipts](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-accounting-erp-laravel-filament, `accounting-goods-and-service-receipts`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-accounting-goods-and-service-receipts` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `accounting-goods-and-service-receipts` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Accounting\\GoodsAndServiceReceipts\\GoodsAndServiceReceiptsServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\Accounting\\GoodsAndServiceReceipts\\GoodsAndServiceReceiptsServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/composer.json) · [module.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/module.json).

**Declared capabilities:** accounting.goods-and-service-receipts

**Declared features:** Goods and service receipts, Quantities and variance, Returns and attachments, Inventory/project references, Accrual events

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Accounting\\GoodsAndServiceReceipts\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/AddReceiptAttachment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Actions/AddReceiptAttachment.php) | `public function handle(Receipt $receipt, array $a): ReceiptAttachment` |
| [src/Actions/AddReceiptLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Actions/AddReceiptLine.php) | `public function handle(Receipt $receipt, array $a): ReceiptLine` |
| [src/Actions/ConfirmService.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Actions/ConfirmService.php) | `public function handle(Receipt $receipt, array $a): ServiceConfirmation` |
| [src/Actions/CreateReceipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Actions/CreateReceipt.php) | `public function handle(array $a): Receipt` |
| [src/Actions/PostAccrual.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Actions/PostAccrual.php) | `public function handle(Receipt $receipt, array $a): ReceiptAccrual` |
| [src/Actions/ReturnReceipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Actions/ReturnReceipt.php) | `public function handle(Receipt $receipt, array $a): ReceiptReturn` |
| [src/Queries/ReceiptQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Queries/ReceiptQuery.php) | `public function paginate(?int $teamId = null, ?ReceiptStatus $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function variance(Receipt $receipt): array` |

Other non-legacy PHP sources: [src/Enums/ReceiptStatus.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Enums/ReceiptStatus.php) · [src/Enums/ReceiptType.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Enums/ReceiptType.php) · [src/Events/ReceiptAccrualPosted.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Events/ReceiptAccrualPosted.php) · [src/Exceptions/InvalidReceipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Exceptions/InvalidReceipt.php) · [src/GoodsAndServiceReceiptsServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/GoodsAndServiceReceiptsServiceProvider.php) · [src/Models/Receipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Models/Receipt.php) · [src/Models/ReceiptAccrual.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Models/ReceiptAccrual.php) · [src/Models/ReceiptAttachment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Models/ReceiptAttachment.php) · [src/Models/ReceiptLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Models/ReceiptLine.php) · [src/Models/ReceiptReturn.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Models/ReceiptReturn.php) · [src/Models/ServiceConfirmation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Models/ServiceConfirmation.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_26_020000_create_accounting_receipt_tables.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/database/migrations/2026_08_26_020000_create_accounting_receipt_tables.php)

[src/Enums/ReceiptStatus.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Enums/ReceiptStatus.php): `Draft = 'draft'`, `Received = 'received'`, `Confirmed = 'confirmed'`, `PartiallyReturned = 'partially_returned'`, `Closed = 'closed'`.

[src/Enums/ReceiptType.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Enums/ReceiptType.php): `Goods = 'goods'`, `Service = 'service'`.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
