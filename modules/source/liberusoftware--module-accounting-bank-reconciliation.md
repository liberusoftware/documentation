# liberusoftware/module-accounting-bank-reconciliation: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Provider-neutral bank reconciliation domain module.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [accounting-bank-reconciliation](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-accounting-erp-laravel-filament, `accounting-bank-reconciliation`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-accounting-bank-reconciliation` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `accounting-bank-reconciliation` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Accounting\\BankReconciliation\\BankReconciliationServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\Accounting\\BankReconciliation\\BankReconciliationServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/composer.json) · [module.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/module.json).

**Declared capabilities:** accounting.bank-reconciliation

**Declared features:** Matches, Transfers, Grouped receipts, Fees and interest, Adjustments, Exceptions, Sign-off

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Accounting\\BankReconciliation\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/AddReconciliationEntry.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/src/Actions/AddReconciliationEntry.php) | `public function handle(ReconciliationSession $session, array $attributes): ReconciliationEntry` |
| [src/Actions/ConfirmReconciliationEntry.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/src/Actions/ConfirmReconciliationEntry.php) | `public function handle(ReconciliationEntry $entry): ReconciliationEntry` |
| [src/Actions/CreateReconciliationSession.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/src/Actions/CreateReconciliationSession.php) | `public function handle(array $attributes): ReconciliationSession` |
| [src/Actions/SignOffReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/src/Actions/SignOffReconciliation.php) | `public function handle(ReconciliationSession $session): ReconciliationSession` |
| [src/Queries/ReconciliationSummaryQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/src/Queries/ReconciliationSummaryQuery.php) | `public function handle(ReconciliationSession $session): array` |

Other non-legacy PHP sources: [src/BankReconciliationServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/src/BankReconciliationServiceProvider.php) · [src/Enums/ReconciliationEntryKind.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/src/Enums/ReconciliationEntryKind.php) · [src/Enums/ReconciliationEntryStatus.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/src/Enums/ReconciliationEntryStatus.php) · [src/Enums/ReconciliationStatus.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/src/Enums/ReconciliationStatus.php) · [src/Events/ReconciliationEntryConfirmed.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/src/Events/ReconciliationEntryConfirmed.php) · [src/Events/ReconciliationSignedOff.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/src/Events/ReconciliationSignedOff.php) · [src/Exceptions/InvalidReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/src/Exceptions/InvalidReconciliation.php) · [src/Models/ReconciliationEntry.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/src/Models/ReconciliationEntry.php) · [src/Models/ReconciliationSession.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/src/Models/ReconciliationSession.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_30_120000_create_accounting_bank_reconciliation_tables.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/database/migrations/2026_08_30_120000_create_accounting_bank_reconciliation_tables.php)

[src/Enums/ReconciliationEntryKind.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/src/Enums/ReconciliationEntryKind.php): `Match = 'match'`, `Transfer = 'transfer'`, `GroupedReceipt = 'grouped_receipt'`, `Fee = 'fee'`, `Interest = 'interest'`, `Adjustment = 'adjustment'`.

[src/Enums/ReconciliationEntryStatus.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/src/Enums/ReconciliationEntryStatus.php): `Suggested = 'suggested'`, `Confirmed = 'confirmed'`, `Exception = 'exception'`.

[src/Enums/ReconciliationStatus.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/src/Enums/ReconciliationStatus.php): `Draft = 'draft'`, `InReview = 'in_review'`, `SignedOff = 'signed_off'`.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
