# liberusoftware/module-accounting-sage-accounting-migration: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Sage Accounting migration domain module

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [accounting-sage-accounting-migration](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sage-accounting-migration/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: accounting-erp-laravel, `accounting-sage-accounting-migration`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-accounting-sage-accounting-migration` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `accounting-sage-accounting-migration` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Accounting\\SageAccountingMigration\\SageAccountingMigrationServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\Accounting\\SageAccountingMigration\\SageAccountingMigrationServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sage-accounting-migration/composer.json) · [module.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sage-accounting-migration/module.json).

**Declared capabilities:** accounting.sage-accounting-migration

**Declared features:** Chart and analysis types, Contacts and products, Sales and purchases, Payments and bank, VAT and CIS evidence, Currencies and budgets, Attachments and source IDs, Idempotent migration and reconciliation

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Accounting\\SageAccountingMigration\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CreateMigrationRun.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sage-accounting-migration/src/Actions/CreateMigrationRun.php) | `public function handle(?int $connectionId, array $metadata = []): SageMigrationRun` |
| [src/Actions/ImportMigrationRecords.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sage-accounting-migration/src/Actions/ImportMigrationRecords.php) | `public function handle(SageMigrationRun $run, array $records): SageMigrationRun` |
| [src/Actions/ReconcileMigration.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sage-accounting-migration/src/Actions/ReconcileMigration.php) | `public function handle(SageMigrationRun $run): SageMigrationRun` |

Other non-legacy PHP sources: [src/Enums/MigrationRecordStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sage-accounting-migration/src/Enums/MigrationRecordStatus.php) · [src/Enums/MigrationRunStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sage-accounting-migration/src/Enums/MigrationRunStatus.php) · [src/Exceptions/InvalidMigration.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sage-accounting-migration/src/Exceptions/InvalidMigration.php) · [src/Models/SageMigrationConnection.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sage-accounting-migration/src/Models/SageMigrationConnection.php) · [src/Models/SageMigrationRecord.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sage-accounting-migration/src/Models/SageMigrationRecord.php) · [src/Models/SageMigrationRun.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sage-accounting-migration/src/Models/SageMigrationRun.php) · [src/SageAccountingMigrationServiceProvider.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sage-accounting-migration/src/SageAccountingMigrationServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_25_150000_create_accounting_sage_migration_tables.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sage-accounting-migration/database/migrations/2026_08_25_150000_create_accounting_sage_migration_tables.php)

[src/Enums/MigrationRecordStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sage-accounting-migration/src/Enums/MigrationRecordStatus.php): `Pending = 'pending'`, `Imported = 'imported'`, `Failed = 'failed'`, `Skipped = 'skipped'`.

[src/Enums/MigrationRunStatus.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sage-accounting-migration/src/Enums/MigrationRunStatus.php): `Draft = 'draft'`, `Running = 'running'`, `Completed = 'completed'`, `Failed = 'failed'`, `Reconciled = 'reconciled'`.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
