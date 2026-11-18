# Maintenance: Scheduling Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#scheduling). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-maintenance-scheduling-nuxt`
**Matching domain module:** `maintenance-scheduling`
**Application:** Maintenance
**Source feature:** [Scheduling](../features/scheduling.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/scheduling.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `maintenance-scheduling` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Calendars:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Skills:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Territories:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Shifts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Availability:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Travel:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Dispatch:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Conflict handling:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-maintenance-scheduling-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `calendars`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `skills`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `territories`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `shifts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `availability`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `travel`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `dispatch`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `conflict-handling`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `maintenance-scheduling` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-maintenance-nuxt-vue`](https://github.com/liberusoftware/project-maintenance-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/scheduling.md)) |
| Capability Nuxt module skeleton | [`module-maintenance-scheduling-nuxt`](https://github.com/liberusoftware/module-maintenance-scheduling-nuxt) (`@liberusoftware/module-maintenance-scheduling-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Calendars** | Expose composable and Vue 3 component for `calendars` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/scheduling.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Skills** | Expose composable and Vue 3 component for `skills` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/scheduling.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Territories** | Expose composable and Vue 3 component for `territories` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/scheduling.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Shifts** | Expose composable and Vue 3 component for `shifts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/scheduling.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Availability** | Expose composable and Vue 3 component for `availability` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/scheduling.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Travel** | Expose composable and Vue 3 component for `travel` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/scheduling.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Dispatch** | Expose composable and Vue 3 component for `dispatch` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/scheduling.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Conflict handling** | Expose composable and Vue 3 component for `conflict handling` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/scheduling.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateScheduleEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-scheduling/src/Actions/CreateScheduleEntry.php) | `public function handle(int $teamId, array $attributes): ScheduleEntry` |
| [DeleteScheduleEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-scheduling/src/Actions/DeleteScheduleEntry.php) | `public function handle(int $teamId, ScheduleEntry $entry): void` |
| [TransitionScheduleEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-scheduling/src/Actions/TransitionScheduleEntry.php) | `public function handle(int $teamId, ScheduleEntry $entry, string $status): ScheduleEntry` |
| [UpdateScheduleEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-scheduling/src/Actions/UpdateScheduleEntry.php) | `public function handle(int $teamId, ScheduleEntry $entry, array $attributes): ScheduleEntry` |
| [ScheduleEntryPolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-scheduling/src/Policies/ScheduleEntryPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, ScheduleEntry $entry): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, ScheduleEntry $entry): bool`<br>`public function delete(object $user, ScheduleEntry $entry): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ScheduleEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-scheduling/src/Models/ScheduleEntry.php) | `team_id`, `title`, `description`, `resource_key`, `equipment_id`, `assigned_to`, `checklist_id`, `instructions`, `estimated_duration`, `starts_at`, `ends_at`, `status`, `territory`, `metadata`, `recurrence_type`, `recurrence_value`, `next_due_at`, `last_completed_at`, `priority` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ScheduleEntryController.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-scheduling-api/src/Http/Controllers/ScheduleEntryController.php) | `public function index(Request $r): JsonResponse`<br>`public function store(Request $r, CreateScheduleEntry $create): JsonResponse`<br>`public function transition(Request $r, ScheduleEntry $scheduleEntry, TransitionScheduleEntry $transition): JsonResponse`<br>`public function show(Request $r, ScheduleEntry $scheduleEntry): JsonResponse`<br>`public function update(Request $r, ScheduleEntry $scheduleEntry, UpdateScheduleEntry $update): JsonResponse`<br>`public function destroy(Request $r, ScheduleEntry $scheduleEntry, DeleteScheduleEntry $delete): JsonResponse` |

**Observed route declarations:**

[modules/module-maintenance-scheduling-api/routes/api.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-scheduling-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/maintenance/scheduling')->group(function (): void {
Route::get('/', [ScheduleEntryController::class, 'index']);
Route::post('/', [ScheduleEntryController::class, 'store']);
Route::get('/{scheduleEntry}', [ScheduleEntryController::class, 'show']);
Route::patch('/{scheduleEntry}', [ScheduleEntryController::class, 'update']);
Route::post('/{scheduleEntry}/transitions', [ScheduleEntryController::class, 'transition']);
Route::delete('/{scheduleEntry}', [ScheduleEntryController::class, 'destroy']);
```
<!-- layer-implementation-plan:end -->
