# Maintenance: Procurement Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#procurement). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-maintenance-procurement-nuxt`
**Matching domain module:** `maintenance-procurement`
**Application:** Maintenance
**Source feature:** [Procurement](../features/procurement.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/procurement.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `maintenance-procurement` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Suppliers:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Requests:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Approvals:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Purchase orders:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Receipts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Returns:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Cost allocation:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-maintenance-procurement-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `suppliers`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `requests`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `approvals`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `purchase-orders`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `receipts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `returns`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `cost-allocation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `maintenance-procurement` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-maintenance-nuxt-vue`](https://github.com/liberusoftware/project-maintenance-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/procurement.md)) |
| Capability Nuxt module skeleton | [`module-maintenance-procurement-nuxt`](https://github.com/liberusoftware/module-maintenance-procurement-nuxt) (`@liberusoftware/module-maintenance-procurement-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Suppliers** | Expose composable and Vue 3 component for `suppliers` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/procurement.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Requests** | Expose composable and Vue 3 component for `requests` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/procurement.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Approvals** | Expose composable and Vue 3 component for `approvals` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/procurement.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Purchase orders** | Expose composable and Vue 3 component for `purchase orders` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/procurement.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Receipts** | Expose composable and Vue 3 component for `receipts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/procurement.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Returns** | Expose composable and Vue 3 component for `returns` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/procurement.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Cost allocation** | Expose composable and Vue 3 component for `cost allocation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/procurement.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApprovePurchaseRequest.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/ApprovePurchaseRequest.php) | `public function handle(int $teamId, PurchaseRequest $request, int $approverId): PurchaseRequest` |
| [CreatePurchaseRequest.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/CreatePurchaseRequest.php) | `public function handle(int $teamId, array $attributes): PurchaseRequest` |
| [CreateVendorContract.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/CreateVendorContract.php) | `public function handle(int $teamId, array $attributes): VendorContract` |
| [CreateVendorPerformanceEvaluation.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/CreateVendorPerformanceEvaluation.php) | `public function handle(int $teamId, array $attributes): VendorPerformanceEvaluation` |
| [DeletePurchaseRequest.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/DeletePurchaseRequest.php) | `public function handle(int $teamId, PurchaseRequest $request): void` |
| [DeleteVendorContract.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/DeleteVendorContract.php) | `public function handle(int $teamId, VendorContract $contract): void` |
| [DeleteVendorPerformanceEvaluation.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/DeleteVendorPerformanceEvaluation.php) | `public function handle(int $teamId, VendorPerformanceEvaluation $evaluation): void` |
| [RejectPurchaseRequest.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/RejectPurchaseRequest.php) | `public function handle(int $teamId, PurchaseRequest $request, int $approverId, ?string $reason = null): PurchaseRequest` |
| [TransitionPurchaseRequest.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/TransitionPurchaseRequest.php) | `public function handle(int $teamId, PurchaseRequest $request, string $status, ?int $actorId = null): PurchaseRequest` |
| [TransitionVendorContract.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Actions/TransitionVendorContract.php) | `public function handle(int $teamId, VendorContract $contract, string $status): VendorContract` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PurchaseRequest.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Models/PurchaseRequest.php) | `team_id`, `supplier_name`, `title`, `description`, `amount`, `currency`, `status`, `requested_by`, `approved_by`, `metadata` |
| [VendorContract.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Models/VendorContract.php) | `team_id`, `vendor_name`, `contract_number`, `title`, `description`, `contract_type`, `start_date`, `end_date`, `contract_value`, `currency`, `status`, `auto_renewal`, `renewal_date`, `notes`, `metadata` |
| [VendorPerformanceEvaluation.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement/src/Models/VendorPerformanceEvaluation.php) | `team_id`, `vendor_contract_id`, `vendor_name`, `evaluation_date`, `evaluated_by`, `quality_rating`, `timeliness_rating`, `communication_rating`, `cost_effectiveness_rating`, `professionalism_rating`, `overall_rating`, `strengths`, `areas_for_improvement`, `comments`, `would_recommend` |

| Observed API controller | Handler signatures |
| --- | --- |
| [PurchaseRequestController.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement-api/src/Http/Controllers/PurchaseRequestController.php) | `public function index(Request $r): JsonResponse`<br>`public function store(Request $r, CreatePurchaseRequest $create): JsonResponse`<br>`public function show(Request $r, PurchaseRequest $purchaseRequest): JsonResponse`<br>`public function approve(Request $r, PurchaseRequest $purchaseRequest, ApprovePurchaseRequest $approve): JsonResponse`<br>`public function reject(Request $r, PurchaseRequest $purchaseRequest, RejectPurchaseRequest $reject): JsonResponse`<br>`public function transition(Request $r, PurchaseRequest $purchaseRequest, TransitionPurchaseRequest $transition): JsonResponse`<br>`public function update(Request $r, PurchaseRequest $purchaseRequest, UpdatePurchaseRequest $update): JsonResponse`<br>`public function destroy(Request $r, PurchaseRequest $purchaseRequest, DeletePurchaseRequest $delete): JsonResponse` |
| [VendorContractController.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement-api/src/Http/Controllers/VendorContractController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateVendorContract $create): JsonResponse`<br>`public function show(Request $request, VendorContract $vendorContract): JsonResponse`<br>`public function transition(Request $request, VendorContract $vendorContract, TransitionVendorContract $transition): JsonResponse`<br>`public function update(Request $request, VendorContract $vendorContract, UpdateVendorContract $update): JsonResponse`<br>`public function destroy(Request $request, VendorContract $vendorContract, DeleteVendorContract $delete): JsonResponse` |
| [VendorPerformanceEvaluationController.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement-api/src/Http/Controllers/VendorPerformanceEvaluationController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateVendorPerformanceEvaluation $create): JsonResponse`<br>`public function show(Request $request, VendorPerformanceEvaluation $vendorPerformanceEvaluation): JsonResponse`<br>`public function update(Request $request, VendorPerformanceEvaluation $vendorPerformanceEvaluation, UpdateVendorPerformanceEvaluation $update): JsonResponse`<br>`public function destroy(Request $request, VendorPerformanceEvaluation $vendorPerformanceEvaluation, DeleteVendorPerformanceEvaluation $delete): JsonResponse` |

**Observed route declarations:**

[modules/module-maintenance-procurement-api/routes/api.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-procurement-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/maintenance/procurement')->group(function (): void {
Route::get('/contracts', [VendorContractController::class, 'index']);
Route::post('/contracts', [VendorContractController::class, 'store']);
Route::get('/contracts/{vendorContract}', [VendorContractController::class, 'show']);
Route::patch('/contracts/{vendorContract}', [VendorContractController::class, 'update']);
Route::post('/contracts/{vendorContract}/transition', [VendorContractController::class, 'transition']);
Route::delete('/contracts/{vendorContract}', [VendorContractController::class, 'destroy']);
Route::get('/evaluations', [VendorPerformanceEvaluationController::class, 'index']);
Route::post('/evaluations', [VendorPerformanceEvaluationController::class, 'store']);
Route::get('/evaluations/{vendorPerformanceEvaluation}', [VendorPerformanceEvaluationController::class, 'show']);
Route::patch('/evaluations/{vendorPerformanceEvaluation}', [VendorPerformanceEvaluationController::class, 'update']);
Route::delete('/evaluations/{vendorPerformanceEvaluation}', [VendorPerformanceEvaluationController::class, 'destroy']);
Route::get('/', [PurchaseRequestController::class, 'index']);
Route::post('/', [PurchaseRequestController::class, 'store']);
Route::get('/{purchaseRequest}', [PurchaseRequestController::class, 'show']);
Route::patch('/{purchaseRequest}', [PurchaseRequestController::class, 'update']);
Route::delete('/{purchaseRequest}', [PurchaseRequestController::class, 'destroy']);
Route::post('/{purchaseRequest}/approve', [PurchaseRequestController::class, 'approve']);
Route::post('/{purchaseRequest}/reject', [PurchaseRequestController::class, 'reject']);
Route::post('/{purchaseRequest}/transitions', [PurchaseRequestController::class, 'transition']);
```
<!-- layer-implementation-plan:end -->
