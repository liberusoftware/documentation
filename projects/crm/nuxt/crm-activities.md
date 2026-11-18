# CRM: Crm Activities Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-activities). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-crm-activities-nuxt`
**Matching domain module:** `crm-activities`
**Application:** CRM
**Source feature:** [Crm Activities](../features/crm-activities.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-activities.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-activities` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Tasks:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Calls:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Meetings:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Emails:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Deadlines:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Recurrence:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Queues:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Bulk completion:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reminders:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Outcomes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Goals:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Activity reporting:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-crm-activities-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `tasks`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `calls`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `meetings`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `emails`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `deadlines`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `recurrence`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `queues`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `bulk-completion`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `reminders`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `outcomes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `goals`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `activity-reporting`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-activities` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-activities.md)) |
| Capability Nuxt module skeleton | [`module-crm-activities-nuxt`](https://github.com/liberusoftware/module-crm-activities-nuxt) (`@liberusoftware/module-crm-activities-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Tasks** | Expose composable and Vue 3 component for `tasks` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-activities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Calls** | Expose composable and Vue 3 component for `calls` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-activities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Meetings** | Expose composable and Vue 3 component for `meetings` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-activities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Emails** | Expose composable and Vue 3 component for `emails` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-activities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Deadlines** | Expose composable and Vue 3 component for `deadlines` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-activities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Recurrence** | Expose composable and Vue 3 component for `recurrence` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-activities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Queues** | Expose composable and Vue 3 component for `queues` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-activities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Bulk completion** | Expose composable and Vue 3 component for `bulk completion` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-activities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Reminders** | Expose composable and Vue 3 component for `reminders` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-activities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Outcomes** | Expose composable and Vue 3 component for `outcomes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-activities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Goals** | Expose composable and Vue 3 component for `goals` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-activities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Activity reporting** | Expose composable and Vue 3 component for `activity reporting` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-activities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CancelActivity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities/src/Actions/CancelActivity.php) | `public function execute(Activity $activity): Activity` |
| [CompleteActivities.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities/src/Actions/CompleteActivities.php) | `public function execute(int $teamId, array $activityIds, ?string $outcome = null, ?string $notes = null): int` |
| [CreateActivity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities/src/Actions/CreateActivity.php) | `public function execute(int $teamId, ?int $actorId, array $attributes): Activity` |
| [CreateActivityGoal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities/src/Actions/CreateActivityGoal.php) | `public function execute(int $teamId, array $attributes): ActivityGoal` |
| [ActivityReport.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities/src/Services/ActivityReport.php) | `public function summarize(int $teamId, Carbon $from, Carbon $until): array` |
| [ActivityScheduler.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities/src/Services/ActivityScheduler.php) | `public function nextOccurrence(Activity $activity): ?Activity`<br>`public function dueReminders(int $teamId, ?Carbon $at = null): Collection` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Activity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities/src/Models/Activity.php) | `team_id`, `actor_id`, `assigned_to`, `kind`, `status`, `title`, `description`, `subject_type`, `subject_id`, `starts_at`, `due_at`, `ends_at`, `recurrence`, `recurrence_until`, `reminder_at`, `queue`, `outcome`, `outcome_notes`, `metadata`, `completed_at` |
| [ActivityEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities/src/Models/ActivityEvent.php) | `team_id`, `activity_id`, `actor_id`, `event`, `details` |
| [ActivityGoal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities/src/Models/ActivityGoal.php) | `team_id`, `owner_id`, `name`, `kind`, `target`, `progress`, `starts_at`, `ends_at`, `status`, `criteria` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ActivityController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities-api/src/Http/Controllers/ActivityController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateActivity $create): JsonResponse`<br>`public function show(Request $request, int $activity): JsonResponse`<br>`public function update(Request $request, int $activity): JsonResponse`<br>`public function complete(Request $request, CompleteActivities $complete): JsonResponse`<br>`public function cancel(Request $request, int $activity, CancelActivity $cancel): JsonResponse`<br>`public function report(Request $request, ActivityReport $report): JsonResponse` |

**Observed route declarations:**

[modules/crm-activities-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities-api/routes/api.php)

```php
Route::middleware(['auth:sanctum', 'throttle:api'])->prefix('api/v1/crm/activities')->group(function (): void {
Route::get('/', [ActivityController::class, 'index']);
Route::post('/', [ActivityController::class, 'store']);
Route::get('/report', [ActivityController::class, 'report']);
Route::post('/complete', [ActivityController::class, 'complete']);
Route::get('/{activity}', [ActivityController::class, 'show']);
Route::patch('/{activity}', [ActivityController::class, 'update']);
Route::post('/{activity}/cancel', [ActivityController::class, 'cancel']);
```
<!-- layer-implementation-plan:end -->
