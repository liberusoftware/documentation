# liberusoftware/real-estate-property-management-api: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Versioned HTTP API adapter for real-estate property management.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [real-estate](../../projects/real-estate/SOURCE-MODULES.md) | [real-estate-property-management-api](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-api/composer.json) | `178d8015b601` | [Variant 1](#variant-1) | 0 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-real-estate-laravel-filament, `real-estate-property-management-api`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/real-estate-property-management-api` |
| Composer version field | `1.0.0` |
| Package type | `liberu-module` |
| Module manifest name | `real-estate-property-management-api` |
| Module version field | `1.0.0` |
| Category / layers | `"adapter"` |
| Manifest provider(s) | `"Liberu\\RealEstate\\PropertyManagementApi\\PropertyManagementApiServiceProvider"` |
| Composer Laravel provider registration | `["Liberu\\RealEstate\\PropertyManagementApi\\PropertyManagementApiServiceProvider"]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-api/composer.json) · [module.json](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-api/module.json).

**Declared capabilities:** real-estate.property-management.api

**Declared features:** Validated management record creation, Team-scoped listing and detail transport, Lifecycle transitions, Inspection scheduling and reporting, Vendor quote CRUD and decisions, Work-order CRUD and progress updates

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/http` | `^13.0` |
| `illuminate/routing` | `^13.0` |
| `liberusoftware/real-estate-property-management` | `^1.0` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\RealEstate\\PropertyManagementApi\\": "src/"}`.

Module resolver requirements: `{"packages": {"liberusoftware/real-estate-property-management": "^1.0"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Http/Controllers/InspectionController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-api/src/Http/Controllers/InspectionController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateInspection $create): JsonResponse`<br>`public function show(Request $request, Inspection $inspection): JsonResponse`<br>`public function update(Request $request, Inspection $inspection, UpdateInspection $update): JsonResponse` |
| [src/Http/Controllers/MaintenanceRequestController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-api/src/Http/Controllers/MaintenanceRequestController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateMaintenanceRequest $create): JsonResponse`<br>`public function show(Request $request, MaintenanceRequest $maintenance): JsonResponse`<br>`public function update(Request $request, MaintenanceRequest $maintenance, UpdateMaintenanceRequest $update): JsonResponse` |
| [src/Http/Controllers/ManagementRecordController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-api/src/Http/Controllers/ManagementRecordController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateManagementRecord $create): JsonResponse`<br>`public function show(Request $request, ManagementRecord $record): JsonResponse`<br>`public function update(Request $request, ManagementRecord $record, TransitionManagementRecord $transition): JsonResponse`<br>`public function updateDetails(Request $request, ManagementRecord $record, UpdateManagementDetails $update): JsonResponse`<br>`public function recordFailure(Request $request, ManagementRecord $record, RecordManagementFailure $failure): JsonResponse` |
| [src/Http/Controllers/VendorQuoteController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-api/src/Http/Controllers/VendorQuoteController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateVendorQuote $create): JsonResponse`<br>`public function show(Request $request, VendorQuote $contractorQuote): JsonResponse`<br>`public function update(Request $request, VendorQuote $contractorQuote): JsonResponse`<br>`public function decide(Request $request, VendorQuote $contractorQuote, DecideVendorQuote $decide): JsonResponse` |
| [src/Http/Controllers/WorkOrderController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-api/src/Http/Controllers/WorkOrderController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateWorkOrder $create): JsonResponse`<br>`public function show(Request $request, WorkOrder $workOrder): JsonResponse`<br>`public function update(Request $request, WorkOrder $workOrder): JsonResponse`<br>`public function updates(Request $request, WorkOrder $workOrder): JsonResponse`<br>`public function storeUpdate(Request $request, WorkOrder $workOrder, RecordWorkOrderUpdate $record): JsonResponse` |

Other non-legacy PHP sources: [src/Http/Resources/InspectionResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-api/src/Http/Resources/InspectionResource.php) · [src/Http/Resources/MaintenanceRequestResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-api/src/Http/Resources/MaintenanceRequestResource.php) · [src/Http/Resources/ManagementRecordResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-api/src/Http/Resources/ManagementRecordResource.php) · [src/Http/Resources/VendorQuoteResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-api/src/Http/Resources/VendorQuoteResource.php) · [src/Http/Resources/WorkOrderResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-api/src/Http/Resources/WorkOrderResource.php) · [src/Http/Resources/WorkOrderUpdateResource.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-api/src/Http/Resources/WorkOrderUpdateResource.php) · [src/PropertyManagementApiServiceProvider.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-api/src/PropertyManagementApiServiceProvider.php).

### HTTP and schema sources

Read route groups, middleware, controller checks and the host route provider together. These source links do not resolve a final deployment URL or prove that the specification matches runtime behavior.

- [openapi/v1/real-estate-property-management.yaml](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-api/openapi/v1/real-estate-property-management.yaml)
- [routes/api.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-api/routes/api.php)

### Persistence and lifecycle evidence

No migrations/settings files were observed in the indexed roots. Inspect model/provider behavior and upstream dependencies before concluding that the package is stateless.

### Verification and consumer use

Declared Composer scripts: `{"test": "pest"}`.

No tracked files under `tests/` were observed in this source location. Do not describe this as a verified independent suite.

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
