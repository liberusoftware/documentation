# liberusoftware/module-accounting-migration-framework: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Accounting migration sources, mappings, dry runs, batches, resume, errors and reconciliation.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [accounting-migration-framework](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: accounting-erp-laravel, `accounting-migration-framework`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-accounting-migration-framework` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `accounting-migration-framework` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Accounting\\MigrationFramework\\MigrationFrameworkServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\Accounting\\MigrationFramework\\MigrationFrameworkServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/composer.json) · [module.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/module.json).

**Declared capabilities:** accounting.migration-framework

**Declared features:** Source inventory and mappings, Dry runs and validation, Resumable batches, Attachments and errors, Counts and reconciliation

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Accounting\\MigrationFramework\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CreateBatch.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Actions/CreateBatch.php) | `public function handle(MigrationSource $source, MigrationMapping $mapping, array $attributes, array $rows = []): MigrationBatch` |
| [src/Actions/CreateMapping.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Actions/CreateMapping.php) | `public function handle(MigrationSource $source, array $attributes): MigrationMapping` |
| [src/Actions/ReconcileBatch.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Actions/ReconcileBatch.php) | `public function handle(MigrationBatch $batch, array $attributes = []): MigrationReconciliation` |
| [src/Actions/RegisterSource.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Actions/RegisterSource.php) | `public function handle(array $attributes): MigrationSource` |
| [src/Actions/RunBatch.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Actions/RunBatch.php) | `public function handle(MigrationBatch $batch, bool $dryRun = false, int $limit = 100): MigrationBatch` |
| [src/Queries/MigrationQuery.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Queries/MigrationQuery.php) | `public function sources(?int $teamId = null, int $perPage = 25): LengthAwarePaginator`<br>`public function batches(?int $teamId = null, int $perPage = 25): LengthAwarePaginator`<br>`public function counts(MigrationBatch $batch): array` |

Other non-legacy PHP sources: [src/Enums/MigrationStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Enums/MigrationStatus.php) · [src/Enums/RowStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Enums/RowStatus.php) · [src/Events/MigrationBatchCompleted.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Events/MigrationBatchCompleted.php) · [src/Exceptions/InvalidMigration.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Exceptions/InvalidMigration.php) · [src/MigrationFrameworkServiceProvider.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/MigrationFrameworkServiceProvider.php) · [src/Models/MigrationAttachment.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Models/MigrationAttachment.php) · [src/Models/MigrationBatch.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Models/MigrationBatch.php) · [src/Models/MigrationMapping.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Models/MigrationMapping.php) · [src/Models/MigrationReconciliation.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Models/MigrationReconciliation.php) · [src/Models/MigrationRow.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Models/MigrationRow.php) · [src/Models/MigrationSource.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Models/MigrationSource.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_26_011000_create_accounting_migration_framework_tables.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/database/migrations/2026_08_26_011000_create_accounting_migration_framework_tables.php)

[src/Enums/MigrationStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Enums/MigrationStatus.php): `Draft = 'draft'`, `DryRun = 'dry_run'`, `Running = 'running'`, `Paused = 'paused'`, `Completed = 'completed'`, `Failed = 'failed'`, `Reconciled = 'reconciled'`.

[src/Enums/RowStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-migration-framework/src/Enums/RowStatus.php): `Pending = 'pending'`, `Valid = 'valid'`, `Imported = 'imported'`, `Skipped = 'skipped'`, `Failed = 'failed'`.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
