# Maintenance: Module Maintenance Work Orders Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-maintenance-work-orders). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-maintenance-module-maintenance-work-orders-nuxt`
**Matching domain module:** `module-maintenance-work-orders`
**Application:** Maintenance
**Source feature:** [Module Maintenance Work Orders](../features/module-maintenance-work-orders.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/module-maintenance-work-orders.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `module-maintenance-work-orders` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Requests:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Triage:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Jobs:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Tasks:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Status machine:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Dependencies:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Notes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Evidence:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Completion:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-maintenance-module-maintenance-work-orders-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `requests`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `triage`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `jobs`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `tasks`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `status-machine`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `dependencies`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `notes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `evidence`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `completion`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `module-maintenance-work-orders` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-maintenance-nuxt-vue`](https://github.com/liberusoftware/project-maintenance-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/module-maintenance-work-orders.md)) |
| Capability Nuxt module skeleton | [`module-maintenance-work-orders-nuxt`](https://github.com/liberusoftware/module-maintenance-work-orders-nuxt) (`@liberusoftware/module-maintenance-work-orders-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Requests** | Expose composable and Vue 3 component for `requests` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-maintenance-work-orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Triage** | Expose composable and Vue 3 component for `triage` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-maintenance-work-orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Jobs** | Expose composable and Vue 3 component for `jobs` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-maintenance-work-orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Tasks** | Expose composable and Vue 3 component for `tasks` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-maintenance-work-orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Status machine** | Expose composable and Vue 3 component for `status machine` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-maintenance-work-orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Dependencies** | Expose composable and Vue 3 component for `dependencies` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-maintenance-work-orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Notes** | Expose composable and Vue 3 component for `notes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-maintenance-work-orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Evidence** | Expose composable and Vue 3 component for `evidence` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-maintenance-work-orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Completion** | Expose composable and Vue 3 component for `completion` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-maintenance-work-orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddWorkOrderComment.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Actions/AddWorkOrderComment.php) | `public function handle(int $teamId, WorkOrder $workOrder, int $userId, string $comment, bool $internal = false): WorkOrderComment` |
| [AddWorkOrderDependency.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Actions/AddWorkOrderDependency.php) | `public function handle(int $teamId, WorkOrder $workOrder, WorkOrder $dependsOn): WorkOrderDependency` |
| [AddWorkOrderEvidence.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Actions/AddWorkOrderEvidence.php) | `public function handle(int $teamId, WorkOrder $workOrder, array $attributes): WorkOrderEvidence` |
| [CreateWorkOrder.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Actions/CreateWorkOrder.php) | `public function handle(int $teamId, array $attributes): WorkOrder` |
| [DeleteWorkOrder.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Actions/DeleteWorkOrder.php) | `public function handle(int $teamId, WorkOrder $workOrder): void` |
| [RemoveWorkOrderDependency.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Actions/RemoveWorkOrderDependency.php) | `public function handle(int $teamId, WorkOrderDependency $dependency): void` |
| [RemoveWorkOrderEvidence.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Actions/RemoveWorkOrderEvidence.php) | `public function handle(int $teamId, WorkOrderEvidence $evidence): void` |
| [TransitionWorkOrder.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Actions/TransitionWorkOrder.php) | `public function handle(int $teamId, WorkOrder $workOrder, string $status, ?int $actorId = null): WorkOrder` |
| [UpdateWorkOrder.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Actions/UpdateWorkOrder.php) | `public function handle(int $teamId, WorkOrder $workOrder, array $attributes): WorkOrder` |
| [WorkOrderPolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Policies/WorkOrderPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, WorkOrder $order): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, WorkOrder $order): bool`<br>`public function delete(object $user, WorkOrder $order): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [WorkOrder.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Models/WorkOrder.php) | `team_id`, `number`, `title`, `description`, `location`, `equipment_id`, `customer_id`, `vendor_id`, `assigned_to`, `due_date`, `started_at`, `estimated_minutes`, `actual_minutes`, `maintenance_plan_id`, `checklist_id`, `priority`, `status`, `requested_by`, `guest_name`, `guest_email`, `guest_phone`, `submitted_at`, `reviewed_by`, `reviewed_at`, `completed_at`, `notes`, `metadata` |
| [WorkOrderComment.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Models/WorkOrderComment.php) | `team_id`, `work_order_id`, `user_id`, `comment`, `is_internal` |
| [WorkOrderDependency.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Models/WorkOrderDependency.php) | `team_id`, `work_order_id`, `depends_on_work_order_id` |
| [WorkOrderEvidence.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Models/WorkOrderEvidence.php) | `team_id`, `work_order_id`, `added_by`, `kind`, `label`, `reference`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [WorkOrderController.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders-api/src/Http/Controllers/WorkOrderController.php) | `public function index(Request $r): JsonResponse`<br>`public function store(Request $r, CreateWorkOrder $create): JsonResponse`<br>`public function show(Request $r, WorkOrder $workOrder): JsonResponse`<br>`public function update(Request $r, WorkOrder $workOrder, UpdateWorkOrder $update): JsonResponse`<br>`public function destroy(Request $r, WorkOrder $workOrder, DeleteWorkOrder $delete): JsonResponse`<br>`public function transition(Request $r, WorkOrder $workOrder, TransitionWorkOrder $transition): JsonResponse`<br>`public function comments(Request $r, WorkOrder $workOrder): JsonResponse`<br>`public function comment(Request $r, WorkOrder $workOrder, AddWorkOrderComment $add): JsonResponse`<br>`public function dependencies(Request $r, WorkOrder $workOrder): JsonResponse`<br>`public function addDependency(Request $r, WorkOrder $workOrder, AddWorkOrderDependency $add): JsonResponse`<br>`public function removeDependency(Request $r, WorkOrder $workOrder, WorkOrderDependency $dependency, RemoveWorkOrderDependency $remove): JsonResponse`<br>`public function evidence(Request $r, WorkOrder $workOrder): JsonResponse`<br>`public function addEvidence(Request $r, WorkOrder $workOrder, AddWorkOrderEvidence $add): JsonResponse`<br>`public function removeEvidence(Request $r, WorkOrder $workOrder, WorkOrderEvidence $evidence, RemoveWorkOrderEvidence $remove): JsonResponse` |

**Observed route declarations:**

[modules/module-maintenance-work-orders-api/routes/api.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/maintenance/work-orders')->group(function (): void {
Route::get('/', [WorkOrderController::class, 'index']);
Route::post('/', [WorkOrderController::class, 'store']);
Route::get('/{workOrder}', [WorkOrderController::class, 'show']);
Route::patch('/{workOrder}', [WorkOrderController::class, 'update']);
Route::delete('/{workOrder}', [WorkOrderController::class, 'destroy']);
Route::post('/{workOrder}/transitions', [WorkOrderController::class, 'transition']);
Route::get('/{workOrder}/comments', [WorkOrderController::class, 'comments']);
Route::post('/{workOrder}/comments', [WorkOrderController::class, 'comment']);
Route::get('/{workOrder}/dependencies', [WorkOrderController::class, 'dependencies']);
Route::post('/{workOrder}/dependencies', [WorkOrderController::class, 'addDependency']);
Route::delete('/{workOrder}/dependencies/{dependency}', [WorkOrderController::class, 'removeDependency']);
Route::get('/{workOrder}/evidence', [WorkOrderController::class, 'evidence']);
Route::post('/{workOrder}/evidence', [WorkOrderController::class, 'addEvidence']);
Route::delete('/{workOrder}/evidence/{evidence}', [WorkOrderController::class, 'removeEvidence']);
```
<!-- layer-implementation-plan:end -->
