# liberusoftware/import-export: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Versioned transfer schemas, mapping, dry runs, validation, queued progress, reports, and retention.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [import-export](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/import-export/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 1 |
| [automation](../../projects/automation/SOURCE-MODULES.md) | [import-export](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/import-export/composer.json) | `68e5f07a6704` | [Variant 1](#variant-1) | 1 |
| [billing](../../projects/billing/SOURCE-MODULES.md) | [import-export](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/import-export/composer.json) | `4743bdfebd1c` | [Variant 1](#variant-1) | 1 |
| [boilerplate](../../projects/boilerplate/SOURCE-MODULES.md) | [import-export](https://github.com/liberusoftware/project-boilerplate-laravel-filament/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/import-export/composer.json) | `3ade34046c3d` | [Variant 1](#variant-1) | 1 |
| [browser-game](../../projects/browser-game/SOURCE-MODULES.md) | [import-export](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/import-export/composer.json) | `790fdffebd3a` | [Variant 1](#variant-1) | 1 |
| [control-panel](../../projects/control-panel/SOURCE-MODULES.md) | [import-export](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/import-export/composer.json) | `1797f25d705f` | [Variant 1](#variant-1) | 1 |
| [crm](../../projects/crm/SOURCE-MODULES.md) | [import-export](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/import-export/composer.json) | `63aad94e94c0` | [Variant 2](#variant-2) | 1 |
| [sap](../../projects/sap/SOURCE-MODULES.md) | [import-export](https://github.com/liberusoftware/project-enterprise-sap-laravel-filament/blob/b12a8c841c6a9054e52cac99d9ac1f233924a041/modules/import-export/composer.json) | `b12a8c841c6a` | [Variant 1](#variant-1) | 1 |
| [genealogy](../../projects/genealogy/SOURCE-MODULES.md) | [import-export](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/import-export/composer.json) | `577e93db23cc` | [Variant 1](#variant-1) | 1 |
| [maintenance](../../projects/maintenance/SOURCE-MODULES.md) | [import-export](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/import-export/composer.json) | `c267d625e264` | [Variant 1](#variant-1) | 1 |
| [real-estate](../../projects/real-estate/SOURCE-MODULES.md) | [import-export](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/import-export/composer.json) | `178d8015b601` | [Variant 1](#variant-1) | 1 |
| [social-network](../../projects/social-network/SOURCE-MODULES.md) | [import-export](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/import-export/composer.json) | `08bbc484b50f` | [Variant 1](#variant-1) | 1 |

Physical source locations: **12**. Reference variants: **2**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-accounting-erp-laravel-filament, `import-export`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/import-export` |
| Composer version field | `1.4.1` |
| Package type | `liberu-module` |
| Module manifest name | `import-export` |
| Module version field | `1.4.1` |
| Category / layers | `"foundation"` |
| Manifest provider(s) | `"Liberu\\Foundation\\ImportExport\\ImportExportServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/import-export/composer.json) · [module.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/import-export/module.json).

**Declared capabilities:** foundation.import-export

**Declared features:** Schemas, Mapping, Dry runs, Validation, Queued execution, Progress, Error reports, Authorization, Retention

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Foundation\\ImportExport\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Contracts/TransferAuthorizer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/import-export/src/Contracts/TransferAuthorizer.php) | `public function allowed(string\|int $actorId, string $schema, string $direction): bool` |
| [src/Support/RowValidator.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/import-export/src/Support/RowValidator.php) | `public function validate(TransferSchema $schema, array $row): array` |

Other non-legacy PHP sources: [src/Data/TransferSchema.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/import-export/src/Data/TransferSchema.php) · [src/ImportExportServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/import-export/src/ImportExportServiceProvider.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_01_050000_create_data_transfers_table.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/import-export/database/migrations/2026_08_01_050000_create_data_transfers_table.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/import-export/tests/.gitkeep)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.


## Variant 2

Representative: project-crm-laravel-filament, `import-export`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/import-export` |
| Composer version field | `1.4.1` |
| Package type | `liberu-module` |
| Module manifest name | `import-export` |
| Module version field | `1.4.1` |
| Category / layers | `"foundation"` |
| Manifest provider(s) | `"Liberu\\Foundation\\ImportExport\\ImportExportServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/import-export/composer.json) · [module.json](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/import-export/module.json).

**Declared capabilities:** foundation.import-export

**Declared features:** Schemas, Mapping, Dry runs, Validation, Queued execution, Progress, Error reports, Authorization, Retention

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Foundation\\ImportExport\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Contracts/TransferAuthorizer.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/import-export/src/Contracts/TransferAuthorizer.php) | `public function allowed(string\|int $actorId, string $schema, string $direction): bool` |
| [src/Support/RowValidator.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/import-export/src/Support/RowValidator.php) | `public function validate(TransferSchema $schema, array $row): array` |

Other non-legacy PHP sources: [src/Data/TransferSchema.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/import-export/src/Data/TransferSchema.php) · [src/ImportExportServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/import-export/src/ImportExportServiceProvider.php).

**Legacy review:** 8 files are under `src/Legacy/`. Their location does not prove they are unused. Review registration, host imports and migrations before moving or removing them.

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_07_08_000004_create_exports_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/import-export/database/migrations/2026_07_08_000004_create_exports_table.php)
- [database/migrations/2026_08_01_050000_create_data_transfers_table.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/import-export/database/migrations/2026_08_01_050000_create_data_transfers_table.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

Tracked files under `tests/`: **1**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/.gitkeep](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/import-export/tests/.gitkeep)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
