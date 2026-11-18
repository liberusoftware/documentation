# Maintenance: Labor and Time Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#labor-and-time). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-maintenance-labor-and-time-nuxt`
**Matching domain module:** `maintenance-labor-and-time`
**Application:** Maintenance
**Source feature:** [Labor and Time](../features/labor-and-time.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/labor-and-time.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `maintenance-labor-and-time` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Engineer skills:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Attendance:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Time entries:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Rates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Expenses:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Approval:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-maintenance-labor-and-time-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `engineer-skills`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `attendance`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `time-entries`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `rates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `expenses`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `approval`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `maintenance-labor-and-time` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-maintenance-nuxt-vue`](https://github.com/liberusoftware/project-maintenance-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/labor-and-time.md)) |
| Capability Nuxt module skeleton | [`module-maintenance-labor-and-time-nuxt`](https://github.com/liberusoftware/module-maintenance-labor-and-time-nuxt) (`@liberusoftware/module-maintenance-labor-and-time-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Engineer skills** | Expose composable and Vue 3 component for `engineer skills` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/labor-and-time.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Attendance** | Expose composable and Vue 3 component for `attendance` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/labor-and-time.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Time entries** | Expose composable and Vue 3 component for `time entries` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/labor-and-time.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Rates** | Expose composable and Vue 3 component for `rates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/labor-and-time.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Expenses** | Expose composable and Vue 3 component for `expenses` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/labor-and-time.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Approval** | Expose composable and Vue 3 component for `approval` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/labor-and-time.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApproveTimeEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time/src/Actions/ApproveTimeEntry.php) | `public function handle(int $teamId, TimeEntry $entry, int $approverId): TimeEntry` |
| [CreateTimeEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time/src/Actions/CreateTimeEntry.php) | `public function handle(int $teamId, array $attributes): TimeEntry` |
| [DeleteTimeEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time/src/Actions/DeleteTimeEntry.php) | `public function handle(int $teamId, TimeEntry $entry): void` |
| [RejectTimeEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time/src/Actions/RejectTimeEntry.php) | `public function handle(int $teamId, TimeEntry $entry, int $approverId, ?string $reason = null): TimeEntry` |
| [UpdateTimeEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time/src/Actions/UpdateTimeEntry.php) | `public function handle(int $teamId, TimeEntry $entry, array $attributes): TimeEntry` |
| [TimeEntryPolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time/src/Policies/TimeEntryPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, TimeEntry $entry): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, TimeEntry $entry): bool`<br>`public function delete(object $user, TimeEntry $entry): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [TimeEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time/src/Models/TimeEntry.php) | `team_id`, `user_id`, `work_order_id`, `description`, `started_at`, `ended_at`, `minutes`, `rate`, `status`, `expense_amount`, `currency` |

| Observed API controller | Handler signatures |
| --- | --- |
| [TimeEntryController.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time-api/src/Http/Controllers/TimeEntryController.php) | `public function index(Request $r): JsonResponse`<br>`public function store(Request $r, CreateTimeEntry $create): JsonResponse`<br>`public function show(Request $r, TimeEntry $timeEntry): JsonResponse`<br>`public function approve(Request $r, TimeEntry $timeEntry, ApproveTimeEntry $approve): JsonResponse`<br>`public function reject(Request $r, TimeEntry $timeEntry, RejectTimeEntry $reject): JsonResponse`<br>`public function update(Request $r, TimeEntry $timeEntry, UpdateTimeEntry $update): JsonResponse`<br>`public function destroy(Request $r, TimeEntry $timeEntry, DeleteTimeEntry $delete): JsonResponse` |

**Observed route declarations:**

[modules/module-maintenance-labor-and-time-api/routes/api.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/maintenance/labor-and-time')->group(function (): void {
Route::get('/', [TimeEntryController::class, 'index']);
Route::post('/', [TimeEntryController::class, 'store']);
Route::get('/{timeEntry}', [TimeEntryController::class, 'show']);
Route::patch('/{timeEntry}', [TimeEntryController::class, 'update']);
Route::delete('/{timeEntry}', [TimeEntryController::class, 'destroy']);
Route::post('/{timeEntry}/approve', [TimeEntryController::class, 'approve']);
Route::post('/{timeEntry}/reject', [TimeEntryController::class, 'reject']);
```
<!-- layer-implementation-plan:end -->
