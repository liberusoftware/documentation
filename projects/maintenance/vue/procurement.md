# Maintenance: Procurement Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#procurement). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-maintenance-procurement-vue-inertia`
**Matching domain module:** `maintenance-procurement`
**Application:** Maintenance
**Source feature:** [Procurement](../features/procurement.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/procurement.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Suppliers:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Requests:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Approvals:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Purchase orders:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Receipts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Returns:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Cost allocation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-maintenance-procurement-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `suppliers`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `requests`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `approvals`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `purchase-orders`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `receipts`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `returns`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `cost-allocation`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

## 4. API contract and Inertia consumption

<!-- inertia-transport:start -->
### Inertia transport boundary

Use Laravel-owned Inertia page/command routes for visits and forms. The controller can invoke the module's public application actions in the same host or use a deliberate API adapter, then return an Inertia page/redirect response. A bare REST JSON resource response is not an Inertia page. Keep authoritative domain authorization and validation in the owning boundary for either path.

Independent API consumers and Next.js use their reviewed HTTP/session integration. Share DTOs and framework-independent UI primitives; keep Inertia page props, visits, form errors and redirects in the Inertia wrapper. Do not introduce loopback HTTP solely to reuse a public action inside the same Laravel host.

See the [Inertia standard](../../../standards/INERTIA.md), [request lifecycle](https://inertiajs.com/docs/v3/core-concepts/how-it-works) and [redirect behavior](https://inertiajs.com/docs/v3/the-basics/redirects).
<!-- inertia-transport:end -->

- Reuse the matching public application/API contracts. For HTTP consumption, use its documented schemas, routes, authentication, permissions, tenant context, errors and operation semantics; Inertia visits still require an Inertia response.
- Keep a typed module-local API client and hooks boundary; use Inertia visits for page transitions and `useForm`/`router` for mutations, preserving server validation and redirect semantics.
- Forward Sanctum cookies or approved authorization headers through a controlled first-party boundary; never persist long-lived tokens in browser storage or expose secrets in page props.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, SSR hydration where enabled, and minimal-host installation tests.
- Test observable behavior with TypeScript, ESLint, Vitest, Vue Test Utils, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `maintenance-procurement` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-maintenance-laravel-inertia-vue`](https://github.com/liberusoftware/project-maintenance-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-maintenance-procurement-vue-inertia`](https://github.com/liberusoftware/module-maintenance-procurement-vue-inertia) (`@liberusoftware/module-maintenance-procurement-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/procurement.md) · [Core plan](../core/procurement.md) · [API plan](../api/procurement.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Suppliers** | Render `suppliers` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Requests** | Render `requests` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Approvals** | Render `approvals` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Purchase orders** | Render `purchase orders` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Receipts** | Render `receipts` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Returns** | Render `returns` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Cost allocation** | Render `cost allocation` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

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
