# CRM: Crm Sales Engagement Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-sales-engagement). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-crm-sales-engagement-nuxt`
**Matching domain module:** `crm-sales-engagement`
**Application:** CRM
**Source feature:** [Crm Sales Engagement](../features/crm-sales-engagement.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-sales-engagement.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-sales-engagement` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Sequences/cadences:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Multi-channel steps:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Templates/snippets:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Task queues:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Enrollment/re-entry:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Throttles:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Timezone windows:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reply/meeting stop rules:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Experiments:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-crm-sales-engagement-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `sequences-cadences`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `multi-channel-steps`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `templates-snippets`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `task-queues`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `enrollment-re-entry`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `throttles`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `timezone-windows`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `reply-meeting-stop-rules`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `experiments`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-sales-engagement` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-sales-engagement.md)) |
| Capability Nuxt module skeleton | [`module-crm-sales-engagement-nuxt`](https://github.com/liberusoftware/module-crm-sales-engagement-nuxt) (`@liberusoftware/module-crm-sales-engagement-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Sequences/cadences** | Expose composable and Vue 3 component for `sequences/cadences` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-sales-engagement.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Multi-channel steps** | Expose composable and Vue 3 component for `multi-channel steps` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-sales-engagement.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Templates/snippets** | Expose composable and Vue 3 component for `templates/snippets` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-sales-engagement.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Task queues** | Expose composable and Vue 3 component for `task queues` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-sales-engagement.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Enrollment/re-entry** | Expose composable and Vue 3 component for `enrollment/re-entry` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-sales-engagement.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Throttles** | Expose composable and Vue 3 component for `throttles` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-sales-engagement.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Timezone windows** | Expose composable and Vue 3 component for `timezone windows` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-sales-engagement.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Reply/meeting stop rules** | Expose composable and Vue 3 component for `reply/meeting stop rules` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-sales-engagement.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Experiments** | Expose composable and Vue 3 component for `experiments` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-sales-engagement.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [EngagementQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Queries/EngagementQuery.php) | `public function sequences(int $teamId)`<br>`public function enrollments(int $teamId)`<br>`public function tasks(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddStep.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Actions/AddStep.php) | `public function execute(int $teamId, int $actorId, array $data): EngagementStep` |
| [CreateSequence.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Actions/CreateSequence.php) | `public function execute(int $teamId, int $actorId, array $data): EngagementSequence` |
| [EnrollContact.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Actions/EnrollContact.php) | `public function execute(int $teamId, int $actorId, array $data): Enrollment` |
| [RecordEngagementEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Actions/RecordEngagementEvent.php) | `public function execute(int $teamId, int $actorId, array $data): EngagementEvent` |
| [StopEnrollment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Actions/StopEnrollment.php) | `public function execute(int $teamId, int $actorId, int $id, string $reason): Enrollment` |
| [UpdateSequence.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Actions/UpdateSequence.php) | `public function execute(int $teamId, int $actorId, int $sequenceId, array $data): EngagementSequence` |
| [EngagementPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Services/EngagementPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [EngagementEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Models/EngagementEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [EngagementSequence.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Models/EngagementSequence.php) | No literal fillable array detected; inspect the model and API schema. |
| [EngagementStep.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Models/EngagementStep.php) | No literal fillable array detected; inspect the model and API schema. |
| [EngagementTask.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Models/EngagementTask.php) | No literal fillable array detected; inspect the model and API schema. |
| [Enrollment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Models/Enrollment.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [EngagementController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement-api/src/Http/Controllers/EngagementController.php) | `public function sequences(Request $r, EngagementQuery $q)`<br>`public function sequence(Request $r, CreateSequence $a)`<br>`public function step(Request $r, AddStep $a)`<br>`public function enrollments(Request $r, EngagementQuery $q)`<br>`public function enroll(Request $r, EnrollContact $a)`<br>`public function stop(Request $r, int $enrollment, string $reason, StopEnrollment $a)`<br>`public function tasks(Request $request, EngagementQuery $query)`<br>`public function complete(Request $request, int $task, CompleteEngagementTask $action)`<br>`public function event(Request $r, RecordEngagementEvent $a)` |

**Observed route declarations:**

[modules/crm-sales-engagement-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/sales-engagement')->group(function (): void {
Route::get('/sequences', [EngagementController::class, 'sequences']);
Route::post('/sequences', [EngagementController::class, 'sequence']);
Route::post('/steps', [EngagementController::class, 'step']);
Route::get('/enrollments', [EngagementController::class, 'enrollments']);
Route::post('/enrollments', [EngagementController::class, 'enroll']);
Route::post('/enrollments/{enrollment}/stop/{reason}', [EngagementController::class, 'stop']);
Route::get('/tasks', [EngagementController::class, 'tasks']);
Route::post('/tasks/{task}/complete', [EngagementController::class, 'complete']);
Route::post('/events', [EngagementController::class, 'event']);
```
<!-- layer-implementation-plan:end -->
