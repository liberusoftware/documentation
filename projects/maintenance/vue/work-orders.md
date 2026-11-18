# Maintenance: Work Orders Vue + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#work-orders). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-maintenance-work-orders-vue-inertia`
**Matching domain module:** `maintenance-work-orders`
**Application:** Maintenance
**Source feature:** [Work Orders](../features/work-orders.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/work-orders.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Requests:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Triage:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Jobs:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Tasks:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Status machine:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Dependencies:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Notes:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Evidence:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Completion:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-maintenance-work-orders-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `requests`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `triage`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `jobs`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `tasks`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `status-machine`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `dependencies`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `notes`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `evidence`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `completion`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `maintenance-work-orders` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia Vue host skeleton | [`project-maintenance-laravel-inertia-vue`](https://github.com/liberusoftware/project-maintenance-laravel-inertia-vue) | Laravel 13 + Inertia 3 + Vue 3 host shell, web/session/CSRF routes, and `vue-tsc` Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-vue) · [wayfinder](../../wayfinders/laravel-inertia-vue.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability Vue Inertia module skeleton | [`module-maintenance-work-orders-vue-inertia`](https://github.com/liberusoftware/module-maintenance-work-orders-vue-inertia) (`@liberusoftware/module-maintenance-work-orders-vue-inertia`) | Reusable Inertia Vue SFC pages, composables, forms, and framework-independent Vue UI ([foundation](https://github.com/liberusoftware/module-boilerplate-vue-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-vue.md)) |
| Shared Vue reuse | [Nuxt plan](../nuxt/work-orders.md) · [Core plan](../core/work-orders.md) · [API plan](../api/work-orders.md) | Share presentational Vue SFCs and DTO types with Nuxt 4 while keeping Inertia navigation/forms in this adapter |

### Vue 3 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia Vue SFC page, shared component & composable contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Requests** | Render `requests` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Triage** | Render `triage` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Jobs** | Render `jobs` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Tasks** | Render `tasks` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Status machine** | Render `status machine` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Dependencies** | Render `dependencies` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Notes** | Render `notes` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Evidence** | Render `evidence` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |
| **Completion** | Render `completion` with `<script setup lang="ts">` Inertia page props (`resources/js/Pages`) and reusable Vue primitives (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; preserve drafts, focus invalid fields, and surface conflicts clearly. |

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
