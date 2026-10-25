# liberusoftware/module-accounting-revenue-recognition: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Accounting revenue recognition domain module

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [accounting-revenue-recognition](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: accounting-erp-laravel, `accounting-revenue-recognition`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-accounting-revenue-recognition` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `accounting-revenue-recognition` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Accounting\\RevenueRecognition\\RevenueRecognitionServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\Accounting\\RevenueRecognition\\RevenueRecognitionServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/composer.json) · [module.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/module.json).

**Declared capabilities:** accounting.revenue-recognition

**Declared features:** Obligations and schedules, Allocation references, Deferred and accrued revenue, Recognition runs, Modifications, Reconciliation

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Accounting\\RevenueRecognition\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CreateRevenueSchedule.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Actions/CreateRevenueSchedule.php) | `public function handle(array $attributes): RevenueSchedule` |
| [src/Actions/ModifyRevenueSchedule.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Actions/ModifyRevenueSchedule.php) | `public function handle(RevenueSchedule $schedule, array $attributes): RevenueModification` |
| [src/Actions/RecognizeDueRevenue.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Actions/RecognizeDueRevenue.php) | `public function handle(RevenueSchedule $schedule, string $asOfDate, ?int $teamId = null): RevenueRecognitionRun` |
| [src/Actions/ReconcileRevenueRun.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Actions/ReconcileRevenueRun.php) | `public function handle(RevenueRecognitionRun $run, array $references = []): RevenueRecognitionRun` |

Other non-legacy PHP sources: [src/Enums/RecognitionRunStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Enums/RecognitionRunStatus.php) · [src/Enums/RecognitionStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Enums/RecognitionStatus.php) · [src/Exceptions/InvalidRecognition.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Exceptions/InvalidRecognition.php) · [src/Models/RevenueAllocationReference.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Models/RevenueAllocationReference.php) · [src/Models/RevenueModification.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Models/RevenueModification.php) · [src/Models/RevenueObligation.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Models/RevenueObligation.php) · [src/Models/RevenueRecognitionRun.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Models/RevenueRecognitionRun.php) · [src/Models/RevenueReconciliation.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Models/RevenueReconciliation.php) · [src/Models/RevenueSchedule.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Models/RevenueSchedule.php) · [src/Models/RevenueScheduleEntry.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Models/RevenueScheduleEntry.php) · [src/RevenueRecognitionServiceProvider.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/RevenueRecognitionServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_25_160000_create_accounting_revenue_recognition_tables.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/database/migrations/2026_08_25_160000_create_accounting_revenue_recognition_tables.php)

[src/Enums/RecognitionRunStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Enums/RecognitionRunStatus.php): `Pending = 'pending'`, `Running = 'running'`, `Completed = 'completed'`, `Failed = 'failed'`, `Reconciled = 'reconciled'`.

[src/Enums/RecognitionStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Enums/RecognitionStatus.php): `Draft = 'draft'`, `Active = 'active'`, `Completed = 'completed'`, `Cancelled = 'cancelled'`, `Failed = 'failed'`.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
