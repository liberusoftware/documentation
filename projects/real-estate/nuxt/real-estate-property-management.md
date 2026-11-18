# Real Estate: Real Estate Property Management Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#real-estate-property-management). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-real-estate-real-estate-property-management-nuxt`
**Matching domain module:** `real-estate-property-management`
**Application:** Real Estate
**Source feature:** [Real Estate Property Management](../features/real-estate-property-management.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/real-estate-property-management.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `real-estate-property-management` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Rent schedule:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Statements:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Inspections:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Compliance:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Maintenance:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Contractors:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Owner approvals:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-real-estate-real-estate-property-management-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `rent-schedule`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `statements`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `inspections`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `compliance`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `maintenance`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `contractors`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `owner-approvals`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

## 4. API contract and Nuxt consumption

- Consume only the matching API module linked above; use its documented OpenAPI schemas, routes, authentication, permissions, team context, pagination, errors, and operation semantics.
- Keep a typed API client and module-local composables under the package boundary; use `useFetch` or `useAsyncData` for SSR-safe reads and `$fetch` for event-driven mutations.
- Forward Sanctum cookies or approved authorization headers through a controlled client boundary; never persist long-lived tokens in browser storage or expose secrets in SSR payloads.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, and minimal-host installation tests.
- Test observable browser and SSR behavior with Vitest, Vue Test Utils, Playwright, TypeScript, and the supported Nuxt 4/Vue 3 stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `real-estate-property-management` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-real-estate-nuxt-vue`](https://github.com/liberusoftware/project-real-estate-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/real-estate-property-management.md)) |
| Capability Nuxt module skeleton | [`module-real-estate-property-management-nuxt`](https://github.com/liberusoftware/module-real-estate-property-management-nuxt) (`@liberusoftware/module-real-estate-property-management-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Rent schedule** | Expose composable and Vue 3 component for `rent schedule` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-property-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Statements** | Expose composable and Vue 3 component for `statements` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-property-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Inspections** | Expose composable and Vue 3 component for `inspections` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-property-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Compliance** | Expose composable and Vue 3 component for `compliance` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-property-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Maintenance** | Expose composable and Vue 3 component for `maintenance` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-property-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Contractors** | Expose composable and Vue 3 component for `contractors` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-property-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Owner approvals** | Expose composable and Vue 3 component for `owner approvals` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-property-management.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListManagementRecords.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Queries/ListManagementRecords.php) | `public function handle(int\|string $teamId, ?string $capability = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ManagementRecordPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Policies/ManagementRecordPolicy.php) | `public function view($user, ManagementRecord $record): bool`<br>`public function update($user, ManagementRecord $record): bool`<br>`public function delete($user, ManagementRecord $record): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Inspection.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Models/Inspection.php) | No literal fillable array detected; inspect the model and API schema. |
| [MaintenanceRequest.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Models/MaintenanceRequest.php) | No literal fillable array detected; inspect the model and API schema. |
| [ManagementRecord.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Models/ManagementRecord.php) | No literal fillable array detected; inspect the model and API schema. |
| [VendorQuote.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Models/VendorQuote.php) | No literal fillable array detected; inspect the model and API schema. |
| [WorkOrder.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Models/WorkOrder.php) | No literal fillable array detected; inspect the model and API schema. |
| [WorkOrderUpdate.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Models/WorkOrderUpdate.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [InspectionController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-api/src/Http/Controllers/InspectionController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateInspection $create): JsonResponse`<br>`public function show(Request $request, Inspection $inspection): JsonResponse`<br>`public function update(Request $request, Inspection $inspection, UpdateInspection $update): JsonResponse` |
| [MaintenanceRequestController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-api/src/Http/Controllers/MaintenanceRequestController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateMaintenanceRequest $create): JsonResponse`<br>`public function show(Request $request, MaintenanceRequest $maintenance): JsonResponse`<br>`public function update(Request $request, MaintenanceRequest $maintenance, UpdateMaintenanceRequest $update): JsonResponse` |
| [ManagementRecordController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-api/src/Http/Controllers/ManagementRecordController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateManagementRecord $create): JsonResponse`<br>`public function show(Request $request, ManagementRecord $record): JsonResponse`<br>`public function update(Request $request, ManagementRecord $record, TransitionManagementRecord $transition): JsonResponse`<br>`public function updateDetails(Request $request, ManagementRecord $record, UpdateManagementDetails $update): JsonResponse`<br>`public function recordFailure(Request $request, ManagementRecord $record, RecordManagementFailure $failure): JsonResponse` |
| [VendorQuoteController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-api/src/Http/Controllers/VendorQuoteController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateVendorQuote $create): JsonResponse`<br>`public function show(Request $request, VendorQuote $contractorQuote): JsonResponse`<br>`public function update(Request $request, VendorQuote $contractorQuote): JsonResponse`<br>`public function decide(Request $request, VendorQuote $contractorQuote, DecideVendorQuote $decide): JsonResponse` |
| [WorkOrderController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-api/src/Http/Controllers/WorkOrderController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateWorkOrder $create): JsonResponse`<br>`public function show(Request $request, WorkOrder $workOrder): JsonResponse`<br>`public function update(Request $request, WorkOrder $workOrder): JsonResponse`<br>`public function updates(Request $request, WorkOrder $workOrder): JsonResponse`<br>`public function storeUpdate(Request $request, WorkOrder $workOrder, RecordWorkOrderUpdate $record): JsonResponse` |

**Observed route declarations:**

[modules/real-estate-property-management-api/routes/api.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->prefix('api/v1/real-estate/property-management')->group(function (): void {
Route::get('/', [ManagementRecordController::class, 'index']);
Route::post('/', [ManagementRecordController::class, 'store']);
Route::get('/{record}', [ManagementRecordController::class, 'show']);
Route::patch('/{record}', [ManagementRecordController::class, 'update']);
Route::patch('/{record}/details', [ManagementRecordController::class, 'updateDetails']);
Route::post('/{record}/failure', [ManagementRecordController::class, 'recordFailure']);
Route::middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->prefix('api/v1/real-estate/work-orders')->group(function (): void {
Route::get('/', [WorkOrderController::class, 'index']);
Route::post('/', [WorkOrderController::class, 'store']);
Route::get('/{workOrder}', [WorkOrderController::class, 'show']);
Route::patch('/{workOrder}', [WorkOrderController::class, 'update']);
Route::get('/{workOrder}/updates', [WorkOrderController::class, 'updates']);
Route::post('/{workOrder}/updates', [WorkOrderController::class, 'storeUpdate']);
Route::middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->prefix('api/v1/real-estate/contractor-quotes')->group(function (): void {
Route::get('/', [VendorQuoteController::class, 'index']);
Route::post('/', [VendorQuoteController::class, 'store']);
Route::get('/{contractorQuote}', [VendorQuoteController::class, 'show']);
Route::patch('/{contractorQuote}', [VendorQuoteController::class, 'update']);
Route::post('/{contractorQuote}/decision', [VendorQuoteController::class, 'decide']);
Route::middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->prefix('api/v1/real-estate/maintenance')->group(function (): void {
Route::get('/', [MaintenanceRequestController::class, 'index']);
Route::post('/', [MaintenanceRequestController::class, 'store']);
Route::get('/{maintenance}', [MaintenanceRequestController::class, 'show']);
Route::patch('/{maintenance}', [MaintenanceRequestController::class, 'update']);
Route::middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->prefix('api/v1/real-estate/inspections')->group(function (): void {
Route::get('/', [InspectionController::class, 'index']);
Route::post('/', [InspectionController::class, 'store']);
Route::get('/{inspection}', [InspectionController::class, 'show']);
Route::patch('/{inspection}', [InspectionController::class, 'update']);
```
<!-- layer-implementation-plan:end -->
