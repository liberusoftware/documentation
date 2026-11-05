# liberusoftware/real-estate-properties-api: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Versioned API adapter for real-estate properties.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [real-estate](../../projects/real-estate/SOURCE-MODULES.md) | [real-estate-properties-api](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/composer.json) | `178d8015b601` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-real-estate-laravel-filament, `real-estate-properties-api`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/real-estate-properties-api` |
| Composer version field | `1.0.1` |
| Package type | `liberu-module` |
| Module manifest name | `real-estate-properties-api` |
| Module version field | `1.0.1` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\RealEstate\\PropertiesApi\\PropertiesApiServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/composer.json) · [module.json](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/module.json).

**Declared capabilities:** real-estate.properties.api

**Declared features:** Property list and detail transport, Validated property creation, Tenant-scoped property comparison, Property tax estimates, Walkability score refresh, Property QR-code data, Property sharing, Favorites and saved-property endpoints, Saved-search endpoints, Community event endpoints, Price alert endpoints

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/http` | `^13.0` |
| `illuminate/routing` | `^13.0` |
| `liberusoftware/organizations-teams` | `^1.0` |
| `liberusoftware/real-estate-properties` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\RealEstate\\PropertiesApi\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/organizations-teams": "^1.0", "liberusoftware/real-estate-properties": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Http/Controllers/CommunityEventController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/src/Http/Controllers/CommunityEventController.php) | `public function index(Request $request): JsonResponse`<br>`public function show(Request $request, CommunityEvent $event): JsonResponse` |
| [src/Http/Controllers/PropertyArTourController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/src/Http/Controllers/PropertyArTourController.php) | `public function config(Property $property, ConfigurePropertyArTour $arTour): JsonResponse`<br>`public function availability(Property $property, ConfigurePropertyArTour $arTour): JsonResponse`<br>`public function enable(Request $request, Property $property, ConfigurePropertyArTour $arTour): JsonResponse`<br>`public function disable(Request $request, Property $property, ConfigurePropertyArTour $arTour): JsonResponse`<br>`public function updateSettings(Request $request, Property $property, ConfigurePropertyArTour $arTour): JsonResponse` |
| [src/Http/Controllers/PropertyCategoryController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/src/Http/Controllers/PropertyCategoryController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request): JsonResponse`<br>`public function update(Request $request, PropertyCategory $category): JsonResponse`<br>`public function destroy(Request $request, PropertyCategory $category): Response` |
| [src/Http/Controllers/PropertyController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/src/Http/Controllers/PropertyController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateProperty $create): JsonResponse`<br>`public function favorite(Request $request, Property $property, TogglePropertyFavorite $toggle): JsonResponse`<br>`public function favorites(Request $request): JsonResponse`<br>`public function removeFavorite(Request $request, Property $property, RemovePropertyFavorite $remove): JsonResponse`<br>`public function similar(Request $request, Property $property): JsonResponse`<br>`public function walkability(Request $request, Property $property, FetchWalkabilityScores $fetch, UpdateProperty $update): JsonResponse`<br>`public function qrCode(Request $request, Property $property, GeneratePropertyQrCode $generate): JsonResponse`<br>`public function share(Request $request, Property $property, SendPropertyToFriend $send): JsonResponse`<br>`public function compare(Request $request): JsonResponse`<br>`public function taxEstimate(Request $request, EstimatePropertyTax $estimate): JsonResponse`<br>`public function show(Request $request, Property $property): JsonResponse`<br>`public function history(Request $request, Property $property): JsonResponse`<br>`public function update(Request $request, Property $property, UpdateProperty $update): JsonResponse`<br>`public function transition(Request $request, Property $property, string $status, TransitionProperty $transition): JsonResponse`<br>`public function unit(Request $request, Property $property, UpsertPropertyUnit $upsert): JsonResponse`<br>`public function key(Request $request, Property $property, RecordPropertyKey $record): JsonResponse`<br>`public function destroy(Request $request, Property $property, DeleteProperty $delete): Response` |
| [src/Http/Controllers/PropertyPriceAlertController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/src/Http/Controllers/PropertyPriceAlertController.php) | `public function index(Request $request, int\|string $property): JsonResponse`<br>`public function store(Request $request, int\|string $property, CreatePriceAlert $create): JsonResponse`<br>`public function update(Request $request, int\|string $alert, UpdatePriceAlert $update): JsonResponse`<br>`public function destroy(Request $request, int\|string $alert, DeletePriceAlert $delete): JsonResponse` |
| [src/Http/Controllers/PropertySavedSearchController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/src/Http/Controllers/PropertySavedSearchController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, SavePropertySearch $save): JsonResponse`<br>`public function destroy(Request $request, int $savedSearch, DeletePropertySearch $delete): JsonResponse` |
| [src/Http/Controllers/PropertyTemplateController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/src/Http/Controllers/PropertyTemplateController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request): JsonResponse`<br>`public function update(Request $request, PropertyTemplate $template): JsonResponse`<br>`public function destroy(Request $request, PropertyTemplate $template): Response` |
| [src/Http/Controllers/PublicPropertyController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/src/Http/Controllers/PublicPropertyController.php) | `public function index(Request $request): JsonResponse`<br>`public function show(Request $request, Property $property): JsonResponse` |

Other non-legacy PHP sources: [src/Http/Resources/CommunityEventResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/src/Http/Resources/CommunityEventResource.php) · [src/Http/Resources/PropertyCategoryResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/src/Http/Resources/PropertyCategoryResource.php) · [src/Http/Resources/PropertyHistoryResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/src/Http/Resources/PropertyHistoryResource.php) · [src/Http/Resources/PropertyKeyResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/src/Http/Resources/PropertyKeyResource.php) · [src/Http/Resources/PropertyPriceAlertResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/src/Http/Resources/PropertyPriceAlertResource.php) · [src/Http/Resources/PropertyQrCodeResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/src/Http/Resources/PropertyQrCodeResource.php) · [src/Http/Resources/PropertyResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/src/Http/Resources/PropertyResource.php) · [src/Http/Resources/PropertySavedSearchResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/src/Http/Resources/PropertySavedSearchResource.php) · [src/Http/Resources/PropertyShareResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/src/Http/Resources/PropertyShareResource.php) · [src/Http/Resources/PropertyTemplateResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/src/Http/Resources/PropertyTemplateResource.php) · [src/Http/Resources/PropertyUnitResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/src/Http/Resources/PropertyUnitResource.php) · [src/Http/Resources/PublicPropertyResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/src/Http/Resources/PublicPropertyResource.php) · [src/PropertiesApiServiceProvider.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/src/PropertiesApiServiceProvider.php).

### HTTP and schema sources

Read route groups, middleware, controller checks and the host route provider together. These source links do not resolve a final deployment URL or prove that the specification matches runtime behavior.

- [openapi/v1/real-estate-properties.yaml](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/openapi/v1/real-estate-properties.yaml)
- [routes/api.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-properties-api/routes/api.php)

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
