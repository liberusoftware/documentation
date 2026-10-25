# liberusoftware/module-billing-catalog: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Provider-neutral catalog products and lifecycle for Liberu Billing.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [billing](../../projects/billing/SOURCE-MODULES.md) | [module-billing-catalog](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/composer.json) | `4743bdfebd1c` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: billing-laravel, `module-billing-catalog`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-billing-catalog` |
| Composer version field | `0.1.1` |
| Package type | `liberu-module` |
| Module manifest name | `module-billing-catalog` |
| Module version field | `0.1.1` |
| Category / layers | `"capability"` |
| Manifest provider(s) | `"Liberu\\Billing\\Catalog\\CatalogServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/composer.json) · [module.json](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/module.json).

**Declared capabilities:** billing.catalog

**Declared features:** Products, Product lifecycle, Team-scoped catalog

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-manager` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Billing\\Catalog\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-manager": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/CreateCatalogRecord.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Actions/CreateCatalogRecord.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(string $model, array $attributes): CatalogRecord` |
| [src/Actions/CreateProduct.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Actions/CreateProduct.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): Product` |
| [src/Actions/TransitionCatalogLifecycle.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Actions/TransitionCatalogLifecycle.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(CatalogRecord $record, CatalogStatus $status): CatalogRecord` |
| [src/Actions/TransitionProductLifecycle.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Actions/TransitionProductLifecycle.php) | `public function execute(Product $product, ProductStatus $status): Product` |
| [src/Policies/CatalogRecordPolicy.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Policies/CatalogRecordPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, CatalogRecord $record): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, CatalogRecord $record): bool` |
| [src/Policies/ProductPolicy.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Policies/ProductPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, Product $product): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, Product $product): bool` |
| [src/Queries/ListCatalogRecords.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Queries/ListCatalogRecords.php) | `public function execute(string $model, ?int $teamId, int $perPage = 25): LengthAwarePaginator` |
| [src/Queries/ListProducts.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Queries/ListProducts.php) | `public function execute(?int $teamId, int $perPage = 25): LengthAwarePaginator` |

Other non-legacy PHP sources: [src/CatalogServiceProvider.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/CatalogServiceProvider.php) · [src/Enums/CatalogStatus.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Enums/CatalogStatus.php) · [src/Enums/ProductStatus.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Enums/ProductStatus.php) · [src/Events/CatalogRecordCreated.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Events/CatalogRecordCreated.php) · [src/Events/CatalogRecordStatusChanged.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Events/CatalogRecordStatusChanged.php) · [src/Events/ProductCreated.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Events/ProductCreated.php) · [src/Events/ProductStatusChanged.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Events/ProductStatusChanged.php) · [src/Models/Addon.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Models/Addon.php) · [src/Models/Bundle.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Models/Bundle.php) · [src/Models/CatalogRecord.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Models/CatalogRecord.php) · [src/Models/Channel.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Models/Channel.php) · [src/Models/ConfigurableOption.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Models/ConfigurableOption.php) · [src/Models/Eligibility.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Models/Eligibility.php) · [src/Models/Plan.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Models/Plan.php) · [src/Models/Product.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Models/Product.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_23_010000_create_billing_catalog_products_table.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/database/migrations/2026_08_23_010000_create_billing_catalog_products_table.php)
- [database/migrations/2026_08_24_150000_create_billing_catalog_capabilities_tables.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/database/migrations/2026_08_24_150000_create_billing_catalog_capabilities_tables.php)

[src/Enums/CatalogStatus.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Enums/CatalogStatus.php): `Draft = 'draft'`, `Active = 'active'`, `Archived = 'archived'`.

[src/Enums/ProductStatus.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-catalog/src/Enums/ProductStatus.php): `Draft = 'draft'`, `Active = 'active'`, `Archived = 'archived'`.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
