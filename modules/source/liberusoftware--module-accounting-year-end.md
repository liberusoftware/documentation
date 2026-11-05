# liberusoftware/module-accounting-year-end: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Accounting year end domain module.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [accounting-year-end](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-accounting-erp-laravel-filament, `accounting-year-end`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-accounting-year-end` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `accounting-year-end` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Accounting\\YearEnd\\YearEndServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\Accounting\\YearEnd\\YearEndServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/composer.json) · [module.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/module.json).

**Declared capabilities:** accounting.year-end

**Declared features:** Final adjustments, Retained earnings, Opening balances, Statutory handoff, Lock, Archive, Evidence

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Accounting\\YearEnd\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/AddYearEndAdjustment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Actions/AddYearEndAdjustment.php) | `public function handle(YearEndPeriod $period, array $attributes): YearEndAdjustment` |
| [src/Actions/ArchiveYearEnd.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Actions/ArchiveYearEnd.php) | `public function handle(YearEndPeriod $period): YearEndPeriod` |
| [src/Actions/CloseYearEnd.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Actions/CloseYearEnd.php) | `public function handle(YearEndClose $close, string $closingEntryRef): YearEndClose` |
| [src/Actions/CreateYearEndClose.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Actions/CreateYearEndClose.php) | `public function handle(array $attributes): YearEndClose` |
| [src/Actions/CreateYearEndPeriod.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Actions/CreateYearEndPeriod.php) | `public function handle(array $attributes): YearEndPeriod` |
| [src/Actions/LockYearEnd.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Actions/LockYearEnd.php) | `public function handle(YearEndPeriod $period, int $actor): YearEndPeriod` |
| [src/Actions/ReopenYearEnd.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Actions/ReopenYearEnd.php) | `public function handle(YearEndClose $close): YearEndClose` |
| [src/Queries/YearEndQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Queries/YearEndQuery.php) | `public function forTeam(int $teamId): Collection` |

Other non-legacy PHP sources: [src/Enums/YearEndAdjustmentStatus.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Enums/YearEndAdjustmentStatus.php) · [src/Enums/YearEndStatus.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Enums/YearEndStatus.php) · [src/Exceptions/InvalidYearEnd.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Exceptions/InvalidYearEnd.php) · [src/Models/YearEndAdjustment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Models/YearEndAdjustment.php) · [src/Models/YearEndClose.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Models/YearEndClose.php) · [src/Models/YearEndPeriod.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Models/YearEndPeriod.php) · [src/YearEndServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/YearEndServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_29_000005_create_accounting_year_end_tables.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/database/migrations/2026_08_29_000005_create_accounting_year_end_tables.php)
- [database/migrations/2026_08_29_000014_create_accounting_year_end_tables.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/database/migrations/2026_08_29_000014_create_accounting_year_end_tables.php)

[src/Enums/YearEndAdjustmentStatus.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Enums/YearEndAdjustmentStatus.php): `Draft = 'draft'`, `Posted = 'posted'`.

[src/Enums/YearEndStatus.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Enums/YearEndStatus.php): `Open = 'open'`, `Adjusted = 'adjusted'`, `Locked = 'locked'`, `Archived = 'archived'`.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
