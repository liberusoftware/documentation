# liberusoftware/real-estate-valuations-api: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Versioned API adapter for real-estate valuations.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [real-estate](../../projects/real-estate/SOURCE-MODULES.md) | [real-estate-valuations-api](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations-api/composer.json) | `178d8015b601` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-real-estate-laravel-filament, `real-estate-valuations-api`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/real-estate-valuations-api` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `real-estate-valuations-api` |
| Module version field | `1.0.0` |
| Category / layers | `"adapter"` |
| Manifest provider(s) | `"Liberu\\RealEstate\\ValuationsApi\\ValuationsApiServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations-api/composer.json) · [module.json](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations-api/module.json).

**Declared capabilities:** real-estate.valuations.api

**Declared features:** Team-scoped valuation endpoints, Bounded pagination and validation, Property valuation estimates, Mortgage estimates, Rental yield estimates

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/http` | `^13.0` |
| `illuminate/routing` | `^13.0` |
| `liberusoftware/api-access` | `^1.0` |
| `liberusoftware/real-estate-properties` | `^1.0` |
| `liberusoftware/real-estate-valuations` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\RealEstate\\ValuationsApi\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/api-access": "^1.0", "liberusoftware/real-estate-properties": "^1.0", "liberusoftware/real-estate-valuations": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Http/Controllers/ValuationController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations-api/src/Http/Controllers/ValuationController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateValuation $create): JsonResponse`<br>`public function calculateNeuralProperty(Request $request, GenerateNeuralPropertyValuation $generate): JsonResponse`<br>`public function show(Request $request, Valuation $valuation): JsonResponse`<br>`public function update(Request $request, Valuation $valuation, UpdateValuation $update): JsonResponse`<br>`public function destroy(Request $request, Valuation $valuation, DeleteValuation $delete): Response`<br>`public function schedule(Request $request, Valuation $valuation, ScheduleValuation $schedule): JsonResponse`<br>`public function complete(Request $request, Valuation $valuation, CompleteValuation $complete): JsonResponse`<br>`public function convert(Request $request, Valuation $valuation, ConvertValuation $convert): JsonResponse`<br>`public function comparables(Request $request, Valuation $valuation, CalculateComparables $calculate): JsonResponse`<br>`public function calculateHome(Request $request, CalculateHomeValuation $calculate): JsonResponse`<br>`public function calculateProperty(Request $request, GeneratePropertyValuation $calculate): JsonResponse`<br>`public function calculateMortgage(Request $request, CalculateMortgage $calculate): JsonResponse`<br>`public function calculateRentalYield(Request $request, CalculateRentalYield $calculate): JsonResponse` |

Other non-legacy PHP sources: [src/Http/Resources/ValuationCalculationResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations-api/src/Http/Resources/ValuationCalculationResource.php) · [src/Http/Resources/ValuationResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations-api/src/Http/Resources/ValuationResource.php) · [src/ValuationsApiServiceProvider.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations-api/src/ValuationsApiServiceProvider.php).

### HTTP and schema sources

Read route groups, middleware, controller checks and the host route provider together. These source links do not resolve a final deployment URL or prove that the specification matches runtime behavior.

- [openapi/v1/real-estate-valuations.yaml](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations-api/openapi/v1/real-estate-valuations.yaml)
- [routes/api.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-valuations-api/routes/api.php)

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
