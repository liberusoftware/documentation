# liberusoftware/module-accounting-customer-payments: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Accounting customer payments domain module.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [accounting-customer-payments](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-payments/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-accounting-erp-laravel-filament, `accounting-customer-payments`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-accounting-customer-payments` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `accounting-customer-payments` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Accounting\\CustomerPayments\\CustomerPaymentsServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\Accounting\\CustomerPayments\\CustomerPaymentsServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-payments/composer.json) · [module.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-payments/module.json).

**Declared capabilities:** accounting.customer-payments

**Declared features:** Receipts, Payment links, Gateway references, Deposits, Undeposited funds, Allocations, Partial/overpayments, Refunds, Reconciliation

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Accounting\\CustomerPayments\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/AllocateCustomerPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-payments/src/Actions/AllocateCustomerPayment.php) | `public function handle(CustomerPayment $payment, string $documentRef, float $amount): CustomerPaymentAllocation` |
| [src/Actions/ReconcileCustomerPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-payments/src/Actions/ReconcileCustomerPayment.php) | `public function handle(CustomerPayment $payment, string $depositReference): CustomerPayment` |
| [src/Actions/RecordCustomerPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-payments/src/Actions/RecordCustomerPayment.php) | `public function handle(array $attributes): CustomerPayment` |
| [src/Actions/RefundCustomerPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-payments/src/Actions/RefundCustomerPayment.php) | `public function handle(CustomerPayment $payment, float $amount): CustomerPayment` |
| [src/Queries/CustomerPaymentQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-payments/src/Queries/CustomerPaymentQuery.php) | `public function forTeam(int $teamId): Collection`<br>`public function forCustomer(int $teamId, string $customerId): Collection` |

Other non-legacy PHP sources: [src/CustomerPaymentsServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-payments/src/CustomerPaymentsServiceProvider.php) · [src/Enums/CustomerPaymentKind.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-payments/src/Enums/CustomerPaymentKind.php) · [src/Enums/CustomerPaymentStatus.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-payments/src/Enums/CustomerPaymentStatus.php) · [src/Exceptions/InvalidCustomerPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-payments/src/Exceptions/InvalidCustomerPayment.php) · [src/Models/CustomerPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-payments/src/Models/CustomerPayment.php) · [src/Models/CustomerPaymentAllocation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-payments/src/Models/CustomerPaymentAllocation.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_29_000016_create_accounting_customer_payments_tables.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-payments/database/migrations/2026_08_29_000016_create_accounting_customer_payments_tables.php)

[src/Enums/CustomerPaymentKind.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-payments/src/Enums/CustomerPaymentKind.php): `Receipt = 'receipt'`, `PaymentLink = 'payment_link'`, `Deposit = 'deposit'`, `Refund = 'refund'`.

[src/Enums/CustomerPaymentStatus.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-payments/src/Enums/CustomerPaymentStatus.php): `Unreconciled = 'unreconciled'`, `PartiallyAllocated = 'partially_allocated'`, `Allocated = 'allocated'`, `Reconciled = 'reconciled'`.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
