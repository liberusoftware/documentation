# liberusoftware/real-estate-core-api: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Versioned API adapter for real-estate branches.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [real-estate](../../projects/real-estate/SOURCE-MODULES.md) | [real-estate-core-api](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/composer.json) | `178d8015b601` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-real-estate-laravel-filament, `real-estate-core-api`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/real-estate-core-api` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `real-estate-core-api` |
| Module version field | `1.0.0` |
| Category / layers | `"presentation"` |
| Manifest provider(s) | `"Liberu\\RealEstate\\CoreApi\\RealEstateCoreApiServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/composer.json) · [module.json](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/module.json).

**Declared capabilities:** real-estate.core.api

**Declared features:** Branch list and detail transport, Validated branch mutations

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/http` | `^13.0` |
| `illuminate/routing` | `^13.0` |
| `liberusoftware/api-access` | `^1.0` |
| `liberusoftware/organizations-teams` | `^1.0` |
| `liberusoftware/real-estate-core` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\RealEstate\\CoreApi\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/api-access": "^1.0", "liberusoftware/organizations-teams": "^1.0", "liberusoftware/real-estate-core": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Http/Controllers/AgencyController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/Http/Controllers/AgencyController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateAgency $create): JsonResponse`<br>`public function show(Request $request, Agency $agency): JsonResponse`<br>`public function update(Request $request, Agency $agency, UpdateAgency $update): JsonResponse`<br>`public function destroy(Request $request, Agency $agency, DeleteAgency $delete): Response` |
| [src/Http/Controllers/BranchController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/Http/Controllers/BranchController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateBranch $create): JsonResponse`<br>`public function show(Request $request, Branch $branch): JsonResponse`<br>`public function update(Request $request, Branch $branch, UpdateBranch $update): JsonResponse`<br>`public function destroy(Request $request, Branch $branch, DeleteBranch $delete): Response` |
| [src/Http/Controllers/CalendarEntryController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/Http/Controllers/CalendarEntryController.php) | `public function store(Request $request, CreateCalendarEntry $create): JsonResponse`<br>`public function update(Request $request, CalendarEntry $calendarEntry): JsonResponse`<br>`public function destroy(Request $request, CalendarEntry $calendarEntry): Response` |
| [src/Http/Controllers/CommunicationController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/Http/Controllers/CommunicationController.php) | `public function store(Request $request, RecordCommunication $record): JsonResponse`<br>`public function update(Request $request, Communication $communication): JsonResponse`<br>`public function destroy(Request $request, Communication $communication): Response` |
| [src/Http/Controllers/CoreConfigurationController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/Http/Controllers/CoreConfigurationController.php) | `public function terminology(Request $request, string $key, SetTerminology $set): JsonResponse`<br>`public function status(Request $request, DefineStatus $define): JsonResponse`<br>`public function audit(Request $request, RecordAuditEntry $record): JsonResponse`<br>`public function list(Request $request, string $kind): JsonResponse` |
| [src/Http/Controllers/NumberingController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/Http/Controllers/NumberingController.php) | `public function next(Request $request, string $key, NextNumber $nextNumber): JsonResponse` |
| [src/Http/Controllers/PublicTerritoryController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/Http/Controllers/PublicTerritoryController.php) | `public function index(): JsonResponse` |
| [src/Http/Controllers/TerritoryController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/Http/Controllers/TerritoryController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateTerritory $create): JsonResponse`<br>`public function show(Request $request, Territory $territory): JsonResponse`<br>`public function update(Request $request, Territory $territory, UpdateTerritory $update): JsonResponse`<br>`public function destroy(Request $request, Territory $territory, DeleteTerritory $delete): Response` |

Other non-legacy PHP sources: [src/Http/Resources/AgencyResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/Http/Resources/AgencyResource.php) · [src/Http/Resources/BranchResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/Http/Resources/BranchResource.php) · [src/Http/Resources/CalendarEntryResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/Http/Resources/CalendarEntryResource.php) · [src/Http/Resources/CommunicationResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/Http/Resources/CommunicationResource.php) · [src/Http/Resources/CoreConfigurationResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/Http/Resources/CoreConfigurationResource.php) · [src/Http/Resources/NumberingResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/Http/Resources/NumberingResource.php) · [src/Http/Resources/TerritoryResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/Http/Resources/TerritoryResource.php) · [src/RealEstateCoreApiServiceProvider.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/RealEstateCoreApiServiceProvider.php).

### HTTP and schema sources

Read route groups, middleware, controller checks and the host route provider together. These source links do not resolve a final deployment URL or prove that the specification matches runtime behavior.

- [openapi/v1/real-estate-core.yaml](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/openapi/v1/real-estate-core.yaml)
- [routes/api.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/routes/api.php)

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
