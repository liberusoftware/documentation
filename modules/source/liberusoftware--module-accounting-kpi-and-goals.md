# liberusoftware/module-accounting-kpi-and-goals: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Governed accounting metrics, goals, targets, thresholds, alerts, commentary and history.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [accounting-kpi-and-goals](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: accounting-erp-laravel, `accounting-kpi-and-goals`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-accounting-kpi-and-goals` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `accounting-kpi-and-goals` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Accounting\\KpiAndGoals\\KpiAndGoalsServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\Accounting\\KpiAndGoals\\KpiAndGoalsServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/composer.json) · [module.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/module.json).

**Declared capabilities:** accounting.kpi-and-goals

**Declared features:** Governed metrics and goals, Targets and periods, Threshold alerts, Commentary and history

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Accounting\\KpiAndGoals\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/AddCommentary.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Actions/AddCommentary.php) | `public function handle(KpiGoal $goal, string $actor, string $body, ?string $period = null): KpiCommentary` |
| [src/Actions/CreateGoal.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Actions/CreateGoal.php) | `public function handle(KpiMetric $metric, array $attributes): KpiGoal` |
| [src/Actions/CreateMetric.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Actions/CreateMetric.php) | `public function handle(array $attributes): KpiMetric` |
| [src/Actions/RecordMeasurement.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Actions/RecordMeasurement.php) | `public function handle(KpiGoal $goal, array $attributes): KpiMeasurement` |
| [src/Queries/KpiQuery.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Queries/KpiQuery.php) | `public function goals(?int $teamId = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function progress(KpiGoal $goal): array` |

Other non-legacy PHP sources: [src/Enums/AlertStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Enums/AlertStatus.php) · [src/Enums/GoalStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Enums/GoalStatus.php) · [src/Events/KpiMeasurementRecorded.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Events/KpiMeasurementRecorded.php) · [src/Exceptions/InvalidKpi.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Exceptions/InvalidKpi.php) · [src/KpiAndGoalsServiceProvider.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/KpiAndGoalsServiceProvider.php) · [src/Models/KpiAlert.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Models/KpiAlert.php) · [src/Models/KpiCommentary.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Models/KpiCommentary.php) · [src/Models/KpiGoal.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Models/KpiGoal.php) · [src/Models/KpiMeasurement.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Models/KpiMeasurement.php) · [src/Models/KpiMetric.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Models/KpiMetric.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_26_015000_create_accounting_kpi_tables.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/database/migrations/2026_08_26_015000_create_accounting_kpi_tables.php)

[src/Enums/AlertStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Enums/AlertStatus.php): `Open = 'open'`, `Acknowledged = 'acknowledged'`, `Resolved = 'resolved'`.

[src/Enums/GoalStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Enums/GoalStatus.php): `Draft = 'draft'`, `Active = 'active'`, `Achieved = 'achieved'`, `AtRisk = 'at_risk'`, `Closed = 'closed'`.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
