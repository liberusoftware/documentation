# Maintenance: Preventative Maintenance Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#preventative-maintenance). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-maintenance-preventative-maintenance-nuxt`
**Matching domain module:** `maintenance-preventative-maintenance`
**Application:** Maintenance
**Source feature:** [Preventative Maintenance](../features/preventative-maintenance.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/preventative-maintenance.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `maintenance-preventative-maintenance` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Plans:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Triggers:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Frequencies:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Meter rules:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Forecasts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Generation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Optimization:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-maintenance-preventative-maintenance-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `plans`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `triggers`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `frequencies`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `meter-rules`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `forecasts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `generation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `optimization`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `maintenance-preventative-maintenance` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-maintenance-nuxt-vue`](https://github.com/liberusoftware/project-maintenance-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/preventative-maintenance.md)) |
| Capability Nuxt module skeleton | [`module-maintenance-preventative-maintenance-nuxt`](https://github.com/liberusoftware/module-maintenance-preventative-maintenance-nuxt) (`@liberusoftware/module-maintenance-preventative-maintenance-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Plans** | Expose composable and Vue 3 component for `plans` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/preventative-maintenance.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Triggers** | Expose composable and Vue 3 component for `triggers` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/preventative-maintenance.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Frequencies** | Expose composable and Vue 3 component for `frequencies` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/preventative-maintenance.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Meter rules** | Expose composable and Vue 3 component for `meter rules` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/preventative-maintenance.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Forecasts** | Expose composable and Vue 3 component for `forecasts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/preventative-maintenance.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Generation** | Expose composable and Vue 3 component for `generation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/preventative-maintenance.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Optimization** | Expose composable and Vue 3 component for `optimization` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/preventative-maintenance.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CompleteMaintenancePlan.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-preventative-maintenance/src/Actions/CompleteMaintenancePlan.php) | `public function handle(int $teamId, MaintenancePlan $plan, ?CarbonInterface $completedAt = null): MaintenancePlan` |
| [CreateMaintenancePlan.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-preventative-maintenance/src/Actions/CreateMaintenancePlan.php) | `public function handle(int $teamId, array $attributes): MaintenancePlan` |
| [DeleteMaintenancePlan.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-preventative-maintenance/src/Actions/DeleteMaintenancePlan.php) | `public function handle(int $teamId, MaintenancePlan $plan): void` |
| [UpdateMaintenancePlan.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-preventative-maintenance/src/Actions/UpdateMaintenancePlan.php) | `public function handle(int $teamId, MaintenancePlan $plan, array $attributes): MaintenancePlan` |
| [MaintenancePlanPolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-preventative-maintenance/src/Policies/MaintenancePlanPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, MaintenancePlan $plan): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, MaintenancePlan $plan): bool`<br>`public function delete(object $user, MaintenancePlan $plan): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MaintenancePlan.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-preventative-maintenance/src/Models/MaintenancePlan.php) | `team_id`, `name`, `code`, `description`, `equipment_id`, `assigned_to`, `checklist_id`, `instructions`, `estimated_duration`, `frequency_unit`, `frequency_value`, `next_due_at`, `last_completed_at`, `is_active`, `rules` |

| Observed API controller | Handler signatures |
| --- | --- |
| [MaintenancePlanController.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-preventative-maintenance-api/src/Http/Controllers/MaintenancePlanController.php) | `public function index(Request $r): JsonResponse`<br>`public function complete(Request $r, MaintenancePlan $maintenancePlan, CompleteMaintenancePlan $complete): JsonResponse`<br>`public function store(Request $r, CreateMaintenancePlan $create): JsonResponse`<br>`public function show(Request $r, MaintenancePlan $maintenancePlan): JsonResponse`<br>`public function update(Request $r, MaintenancePlan $maintenancePlan, UpdateMaintenancePlan $update): JsonResponse`<br>`public function destroy(Request $r, MaintenancePlan $maintenancePlan, DeleteMaintenancePlan $delete): JsonResponse` |

**Observed route declarations:**

[modules/module-maintenance-preventative-maintenance-api/routes/api.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-preventative-maintenance-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/maintenance/preventative-maintenance')->group(function (): void {
Route::get('/', [MaintenancePlanController::class, 'index']);
Route::post('/', [MaintenancePlanController::class, 'store']);
Route::get('/{maintenancePlan}', [MaintenancePlanController::class, 'show']);
Route::patch('/{maintenancePlan}', [MaintenancePlanController::class, 'update']);
Route::post('/{maintenancePlan}/complete', [MaintenancePlanController::class, 'complete']);
Route::delete('/{maintenancePlan}', [MaintenancePlanController::class, 'destroy']);
```
<!-- layer-implementation-plan:end -->
