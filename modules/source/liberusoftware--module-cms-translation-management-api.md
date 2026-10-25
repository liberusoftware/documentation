# liberusoftware/module-cms-translation-management-api: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

API adapter for CMS Translation Management.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [cms](../../projects/cms/SOURCE-MODULES.md) | [module-cms-translation-management-api](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-translation-management-api/composer.json) | `5d91aa9c0a3d` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: cms-laravel, `module-cms-translation-management-api`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-cms-translation-management-api` |
| Composer version field | `0.1.0` |
| Package type | `liberu-module` |
| Module manifest name | `module-cms-translation-management-api` |
| Module version field | `0.1.0` |
| Category / layers | `"not declared"` |
| Manifest provider(s) | `"not declared"` |
| Composer Laravel provider registration | `["Liberu\\Cms\\TranslationManagementApi\\TranslationManagementApiServiceProvider"]` |
| default_enabled field | `"not declared"` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-translation-management-api/composer.json) · [module.json](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-translation-management-api/module.json).

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `laravel/framework` | `^13.0` |
| `liberusoftware/module-cms-api` | `^0.1` |
| `liberusoftware/module-cms-translation-management` | `^0.1` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\Cms\\TranslationManagementApi\\": "src/"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Http/Controllers/TranslationManagementController.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-translation-management-api/src/Http/Controllers/TranslationManagementController.php) | `public function __construct(private TranslationJobQuery $jobs, private TranslationManagementService $service)`<br>`public function index(Request $request): AnonymousResourceCollection`<br>`public function show(string $publicId): TranslationJobResource`<br>`public function create(Request $request): TranslationJobResource`<br>`public function sourceChange(Request $request, string $publicId): TranslationSourceChangeResource`<br>`public function translate(Request $request, int $sourceChange): TranslationSourceChangeResource`<br>`public function review(Request $request, int $sourceChange): TranslationSourceChangeResource`<br>`public function reconcile(string $publicId): TranslationJobResource`<br>`public function queue(string $publicId): TranslationJobResource`<br>`public function cancel(string $publicId): TranslationJobResource`<br>`public function assign(Request $request, int $sourceChange): mixed`<br>`public function vendor(Request $request): TranslationVendorResource`<br>`public function memory(Request $request): TranslationMemoryResource`<br>`public function glossary(Request $request): TranslationGlossaryResource` |

Other non-legacy PHP sources: [src/Http/Resources/TranslationGlossaryResource.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-translation-management-api/src/Http/Resources/TranslationGlossaryResource.php) · [src/Http/Resources/TranslationJobResource.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-translation-management-api/src/Http/Resources/TranslationJobResource.php) · [src/Http/Resources/TranslationMemoryResource.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-translation-management-api/src/Http/Resources/TranslationMemoryResource.php) · [src/Http/Resources/TranslationSourceChangeResource.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-translation-management-api/src/Http/Resources/TranslationSourceChangeResource.php) · [src/Http/Resources/TranslationVendorResource.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-translation-management-api/src/Http/Resources/TranslationVendorResource.php) · [src/TranslationManagementApiServiceProvider.php](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-translation-management-api/src/TranslationManagementApiServiceProvider.php).

### HTTP and schema sources

Read route groups, middleware, controller checks and the host route provider together. These source links do not resolve a final deployment URL or prove that the specification matches runtime behavior.

- [openapi/v1/cms-translation-management.yaml](https://github.com/liberusoftware/cms-laravel/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-translation-management-api/openapi/v1/cms-translation-management.yaml)

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
