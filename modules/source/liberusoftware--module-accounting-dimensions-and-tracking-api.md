# liberusoftware/module-accounting-dimensions-and-tracking-api: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Authenticated API adapter for accounting dimensions and tracking.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [accounting](../../projects/accounting/SOURCE-MODULES.md) | [accounting-dimensions-and-tracking-api](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dimensions-and-tracking-api/composer.json) | `39a49babafc0` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: accounting-erp-laravel, `accounting-dimensions-and-tracking-api`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-accounting-dimensions-and-tracking-api` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `accounting-dimensions-and-tracking-api` |
| Module version field | `1.0.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\Accounting\\DimensionsApi\\DimensionsApiServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\Accounting\\DimensionsApi\\DimensionsApiServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dimensions-and-tracking-api/composer.json) · [module.json](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dimensions-and-tracking-api/module.json).

**Declared capabilities:** accounting.dimensions-and-tracking.api

**Declared features:** Dimension CRUD, Value CRUD, Validation, Allocations, Balances

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `laravel/framework` | `^13.0` |
| `laravel/sanctum` | `^4.0` |
| `liberusoftware/module-accounting-dimensions-and-tracking` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Accounting\\DimensionsApi\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-accounting-dimensions-and-tracking": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Http/Controllers/DimensionsController.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dimensions-and-tracking-api/src/Http/Controllers/DimensionsController.php) | `public function index(Request $request)`<br>`public function show(string $dimension): DimensionResource`<br>`public function store(Request $request, SaveDimension $save)`<br>`public function update(Request $request, string $dimension, SaveDimension $save): DimensionResource`<br>`public function values(Request $request, string $dimension, SaveDimensionValue $save)`<br>`public function validateValues(Request $request, ValidateDimensions $validate)`<br>`public function allocate(Request $request, AllocateDimensions $allocate)`<br>`public function balances(Request $request, DimensionalBalances $balances)`<br>`public function destroy(string $dimension): Response` |
| [src/Policies/DimensionsPolicy.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dimensions-and-tracking-api/src/Policies/DimensionsPolicy.php) | `public function viewAny(?Authenticatable $u): bool`<br>`public function view(?Authenticatable $u, Dimension $d): bool`<br>`public function create(?Authenticatable $u): bool`<br>`public function update(?Authenticatable $u, Dimension $d): bool`<br>`public function delete(?Authenticatable $u, Dimension $d): bool` |

Other non-legacy PHP sources: [src/DimensionsApiServiceProvider.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dimensions-and-tracking-api/src/DimensionsApiServiceProvider.php) · [src/Http/Resources/DimensionResource.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dimensions-and-tracking-api/src/Http/Resources/DimensionResource.php).

### HTTP and schema sources

Read route groups, middleware, controller checks and the host route provider together. These source links do not resolve a final deployment URL or prove that the specification matches runtime behavior.

- [openapi/v1/accounting-dimensions-and-tracking.yaml](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dimensions-and-tracking-api/openapi/v1/accounting-dimensions-and-tracking.yaml)
- [routes/api.php](https://github.com/liberusoftware/accounting-erp-laravel/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dimensions-and-tracking-api/routes/api.php)

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
