# liberusoftware/module-accounting-debt-and-loans: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Debt facilities, drawdowns, repayments, interest, covenants, schedules and reconciliation.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [accounting-debt-and-loans](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: accounting-erp-laravel, `accounting-debt-and-loans`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-accounting-debt-and-loans` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `accounting-debt-and-loans` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Accounting\\DebtAndLoans\\DebtAndLoansServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\Accounting\\DebtAndLoans\\DebtAndLoansServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/composer.json) · [module.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/module.json).

**Declared capabilities:** accounting.debt-and-loans

**Declared features:** Facilities and drawdowns, Repayments and interest, Schedules and covenants, Current/non-current split and reconciliation

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Accounting\\DebtAndLoans\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CreateDebtFacility.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Actions/CreateDebtFacility.php) | `public function handle(array $attributes): DebtFacility` |
| [src/Actions/ReconcileDebtMovement.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Actions/ReconcileDebtMovement.php) | `public function handle(DebtMovement $movement, string $journalReference): DebtMovement` |
| [src/Actions/RecordDebtMovement.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Actions/RecordDebtMovement.php) | `public function handle(DebtFacility $facility, string\|DebtMovementKind $kind, array $attributes): DebtMovement` |
| [src/Queries/DebtQuery.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Queries/DebtQuery.php) | `public function facilities(int $teamId): Collection`<br>`public function position(int $teamId): array` |

Other non-legacy PHP sources: [src/DebtAndLoansServiceProvider.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/DebtAndLoansServiceProvider.php) · [src/Enums/DebtFacilityStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Enums/DebtFacilityStatus.php) · [src/Enums/DebtMovementKind.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Enums/DebtMovementKind.php) · [src/Enums/DebtMovementStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Enums/DebtMovementStatus.php) · [src/Exceptions/InvalidDebt.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Exceptions/InvalidDebt.php) · [src/Models/DebtCovenant.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Models/DebtCovenant.php) · [src/Models/DebtFacility.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Models/DebtFacility.php) · [src/Models/DebtMovement.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Models/DebtMovement.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_29_000012_create_accounting_debt_and_loans_tables.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/database/migrations/2026_08_29_000012_create_accounting_debt_and_loans_tables.php)

[src/Enums/DebtFacilityStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Enums/DebtFacilityStatus.php): `Active = 'active'`, `Closed = 'closed'`.

[src/Enums/DebtMovementKind.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Enums/DebtMovementKind.php): `Drawdown = 'drawdown'`, `Repayment = 'repayment'`, `Interest = 'interest'`, `Fee = 'fee'`.

[src/Enums/DebtMovementStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Enums/DebtMovementStatus.php): `Scheduled = 'scheduled'`, `Posted = 'posted'`, `Reconciled = 'reconciled'`.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
