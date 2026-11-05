# liberusoftware/module-accounting-fixed-assets: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Fixed asset register, categories, acquisition, capitalization, components, locations, books and documents.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [accounting-fixed-assets](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-accounting-erp-laravel-filament, `accounting-fixed-assets`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-accounting-fixed-assets` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `accounting-fixed-assets` |
| Module version field | `1.0.0` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Accounting\\FixedAssets\\FixedAssetsServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\Accounting\\FixedAssets\\FixedAssetsServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/composer.json) · [module.json](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/module.json).

**Declared capabilities:** accounting.fixed-assets

**Declared features:** Asset register and categories, Acquisition and capitalization, Components and custodians, Asset books and documents

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Accounting\\FixedAssets\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/AcquireAsset.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/AcquireAsset.php) | `public function handle(AssetCategory $category, array $attributes): Asset` |
| [src/Actions/AddAssetComponent.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/AddAssetComponent.php) | `public function handle(Asset $asset, array $attributes): AssetComponent` |
| [src/Actions/AddAssetDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/AddAssetDocument.php) | `public function handle(Asset $asset, array $attributes): AssetDocument` |
| [src/Actions/ArchiveAsset.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/ArchiveAsset.php) | `public function handle(Asset $asset): Asset` |
| [src/Actions/AssignAssetCustodian.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/AssignAssetCustodian.php) | `public function handle(Asset $asset, AssetCustodian $custodian): Asset` |
| [src/Actions/AssignAssetLocation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/AssignAssetLocation.php) | `public function handle(Asset $asset, AssetLocation $location): Asset` |
| [src/Actions/CapitalizeAsset.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/CapitalizeAsset.php) | `public function handle(Asset $asset, string $bookReference): Asset` |
| [src/Actions/CreateCategory.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/CreateCategory.php) | `public function handle(array $attributes): AssetCategory` |
| [src/Actions/CreateCustodian.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/CreateCustodian.php) | `public function handle(array $attributes): AssetCustodian` |
| [src/Actions/CreateLocation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/CreateLocation.php) | `public function handle(array $attributes): AssetLocation` |
| [src/Actions/DisposeAsset.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/DisposeAsset.php) | `public function handle(Asset $asset, string $reason): Asset` |
| [src/Actions/UpdateAsset.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Actions/UpdateAsset.php) | `public function handle(Asset $asset, array $attributes): Asset` |
| [src/Policies/AssetPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Policies/AssetPolicy.php) | `public function view(mixed $user, Asset $asset): bool`<br>`public function create(mixed $user): bool`<br>`public function update(mixed $user, Asset $asset): bool`<br>`public function capitalize(mixed $user, Asset $asset): bool`<br>`public function dispose(mixed $user, Asset $asset): bool` |
| [src/Queries/AssetQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Queries/AssetQuery.php) | `public function paginate(?int $teamId = null, ?AssetStatus $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function registerSummary(Asset $asset): array` |

Other non-legacy PHP sources: [src/Enums/AssetStatus.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Enums/AssetStatus.php) · [src/Events/AssetAcquired.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Events/AssetAcquired.php) · [src/Events/AssetArchived.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Events/AssetArchived.php) · [src/Events/AssetCapitalized.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Events/AssetCapitalized.php) · [src/Events/AssetComponentAdded.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Events/AssetComponentAdded.php) · [src/Events/AssetCustodianAssigned.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Events/AssetCustodianAssigned.php) · [src/Events/AssetDisposed.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Events/AssetDisposed.php) · [src/Events/AssetDocumentAdded.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Events/AssetDocumentAdded.php) · [src/Events/AssetLocationAssigned.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Events/AssetLocationAssigned.php) · [src/Exceptions/AssetNotFound.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Exceptions/AssetNotFound.php) · [src/Exceptions/InvalidAsset.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Exceptions/InvalidAsset.php) · [src/FixedAssetsServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/FixedAssetsServiceProvider.php) · [src/Models/Asset.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Models/Asset.php) · [src/Models/AssetBook.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Models/AssetBook.php) · [src/Models/AssetCategory.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Models/AssetCategory.php) · [src/Models/AssetComponent.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Models/AssetComponent.php) · [src/Models/AssetCustodian.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Models/AssetCustodian.php) · [src/Models/AssetDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Models/AssetDocument.php) · [src/Models/AssetLocation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Models/AssetLocation.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_26_022000_create_accounting_fixed_asset_tables.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/database/migrations/2026_08_26_022000_create_accounting_fixed_asset_tables.php)

[src/Enums/AssetStatus.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-fixed-assets/src/Enums/AssetStatus.php): `Draft = 'draft'`, `Acquired = 'acquired'`, `Capitalized = 'capitalized'`, `Disposed = 'disposed'`, `Archived = 'archived'`.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
