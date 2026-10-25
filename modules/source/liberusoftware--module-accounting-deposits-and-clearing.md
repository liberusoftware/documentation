# liberusoftware/module-accounting-deposits-and-clearing: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Undeposited funds, grouped deposits, provider clearing, fees, payouts and reconciliation.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [accounting-deposits-and-clearing](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: accounting-erp-laravel, `accounting-deposits-and-clearing`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-accounting-deposits-and-clearing` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `accounting-deposits-and-clearing` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Accounting\\DepositsAndClearing\\DepositsAndClearingServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\Accounting\\DepositsAndClearing\\DepositsAndClearingServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/composer.json) · [module.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/module.json).

**Declared capabilities:** accounting.deposits-and-clearing

**Declared features:** Undeposited funds, Grouped deposits, Provider clearing and fees, Payouts and reconciliation

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Accounting\\DepositsAndClearing\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CreateGroupedDeposit.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Actions/CreateGroupedDeposit.php) | `public function handle(array $attributes, array $fundIds): ClearingDeposit` |
| [src/Actions/ReconcileDeposit.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Actions/ReconcileDeposit.php) | `public function handle(ClearingDeposit $deposit, float $payoutAmount, float $feeAmount = 0): ClearingDeposit` |
| [src/Actions/RecordUndepositedFund.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Actions/RecordUndepositedFund.php) | `public function handle(array $attributes): ClearingFund` |
| [src/Queries/ClearingQuery.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Queries/ClearingQuery.php) | `public function undeposited(int $teamId): Collection`<br>`public function deposits(int $teamId): Collection` |

Other non-legacy PHP sources: [src/DepositsAndClearingServiceProvider.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/DepositsAndClearingServiceProvider.php) · [src/Enums/ClearingDepositStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Enums/ClearingDepositStatus.php) · [src/Enums/ClearingFundStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Enums/ClearingFundStatus.php) · [src/Exceptions/InvalidClearing.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Exceptions/InvalidClearing.php) · [src/Models/ClearingDeposit.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Models/ClearingDeposit.php) · [src/Models/ClearingFund.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Models/ClearingFund.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_29_000011_create_accounting_deposits_and_clearing_tables.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/database/migrations/2026_08_29_000011_create_accounting_deposits_and_clearing_tables.php)

[src/Enums/ClearingDepositStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Enums/ClearingDepositStatus.php): `Open = 'open'`, `Reconciled = 'reconciled'`.

[src/Enums/ClearingFundStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Enums/ClearingFundStatus.php): `Undeposited = 'undeposited'`, `Grouped = 'grouped'`, `Reconciled = 'reconciled'`.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
