# liberusoftware/module-accounting-account-reconciliations: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Account reconciliation workpapers, review, certification, and carry-forward.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [accounting-account-reconciliations](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-accounting-erp-laravel-filament, `accounting-account-reconciliations`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-accounting-account-reconciliations` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `accounting-account-reconciliations` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Accounting\\AccountReconciliations\\AccountReconciliationsServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\Accounting\\AccountReconciliations\\AccountReconciliationsServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/composer.json) · [module.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/module.json).

**Declared capabilities:** accounting.account-reconciliations

**Declared features:** Templates, Source balances, Supporting items, Preparer and reviewer, Aging, Certification, Carry-forward

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Accounting\\AccountReconciliations\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CarryForwardAccountReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/src/Actions/CarryForwardAccountReconciliation.php) | `public function handle(AccountReconciliation $reconciliation, array $carryForward): AccountReconciliation` |
| [src/Actions/CertifyAccountReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/src/Actions/CertifyAccountReconciliation.php) | `public function handle(AccountReconciliation $reconciliation, array $certification): AccountReconciliation` |
| [src/Actions/CreateAccountReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/src/Actions/CreateAccountReconciliation.php) | `public function handle(array $attributes): AccountReconciliation` |
| [src/Actions/PrepareAccountReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/src/Actions/PrepareAccountReconciliation.php) | `public function handle(AccountReconciliation $reconciliation, array $preparer, array $sourceBalance, array $supportingItems = []): AccountReconciliation` |
| [src/Actions/ReviewAccountReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/src/Actions/ReviewAccountReconciliation.php) | `public function handle(AccountReconciliation $reconciliation, array $reviewer): AccountReconciliation` |
| [src/Queries/AccountReconciliationQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/src/Queries/AccountReconciliationQuery.php) | `public function paginate(?int $teamId, ?string $status = null, int $perPage = 25): LengthAwarePaginator` |

Other non-legacy PHP sources: [src/AccountReconciliationsServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/src/AccountReconciliationsServiceProvider.php) · [src/Enums/ReconciliationStatus.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/src/Enums/ReconciliationStatus.php) · [src/Exceptions/InvalidAccountReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/src/Exceptions/InvalidAccountReconciliation.php) · [src/Models/AccountReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/src/Models/AccountReconciliation.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_31_100000_create_accounting_account_reconciliations_table.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/database/migrations/2026_08_31_100000_create_accounting_account_reconciliations_table.php)

[src/Enums/ReconciliationStatus.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/src/Enums/ReconciliationStatus.php): `Draft = 'draft'`, `Prepared = 'prepared'`, `InReview = 'in_review'`, `Certified = 'certified'`, `CarriedForward = 'carried_forward'`.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
