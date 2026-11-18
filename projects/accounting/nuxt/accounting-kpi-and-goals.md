# Accounting: Accounting Kpi And Goals Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-kpi-and-goals). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-accounting-kpi-and-goals-nuxt`
**Matching domain module:** `accounting-kpi-and-goals`
**Application:** Accounting
**Source feature:** [Accounting Kpi And Goals](../features/accounting-kpi-and-goals.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-kpi-and-goals.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-kpi-and-goals` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Governed metrics:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Targets:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Owners:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Thresholds:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Periods:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Alerts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Commentary:** page/component/composable/API-action behavior for this module's authorized workflow.
- **History:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-accounting-kpi-and-goals-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `governed-metrics`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `targets`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `owners`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `thresholds`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `periods`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `alerts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `commentary`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `history`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-kpi-and-goals` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-kpi-and-goals.md)) |
| Capability Nuxt module skeleton | [`module-accounting-kpi-and-goals-nuxt`](https://github.com/liberusoftware/module-accounting-kpi-and-goals-nuxt) (`@liberusoftware/module-accounting-kpi-and-goals-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Governed metrics** | Expose composable and Vue 3 component for `governed metrics` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-kpi-and-goals.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Targets** | Expose composable and Vue 3 component for `targets` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-kpi-and-goals.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Owners** | Expose composable and Vue 3 component for `owners` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-kpi-and-goals.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Thresholds** | Expose composable and Vue 3 component for `thresholds` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-kpi-and-goals.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Periods** | Expose composable and Vue 3 component for `periods` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-kpi-and-goals.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Alerts** | Expose composable and Vue 3 component for `alerts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-kpi-and-goals.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Commentary** | Expose composable and Vue 3 component for `commentary` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-kpi-and-goals.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **History** | Expose composable and Vue 3 component for `history` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-kpi-and-goals.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [KpiQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Queries/KpiQuery.php) | `public function goals(?int $teamId = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function progress(KpiGoal $goal): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddCommentary.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Actions/AddCommentary.php) | `public function handle(KpiGoal $goal, string $actor, string $body, ?string $period = null): KpiCommentary` |
| [CreateGoal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Actions/CreateGoal.php) | `public function handle(KpiMetric $metric, array $attributes): KpiGoal` |
| [CreateMetric.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Actions/CreateMetric.php) | `public function handle(array $attributes): KpiMetric` |
| [RecordMeasurement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Actions/RecordMeasurement.php) | `public function handle(KpiGoal $goal, array $attributes): KpiMeasurement` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [KpiAlert.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Models/KpiAlert.php) | `team_id`, `goal_id`, `measurement_id`, `severity`, `status`, `message`, `triggered_at`, `acknowledged_by`, `resolved_at`, `metadata` |
| [KpiCommentary.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Models/KpiCommentary.php) | `goal_id`, `actor_ref`, `body`, `period_ref`, `metadata` |
| [KpiGoal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Models/KpiGoal.php) | `team_id`, `metric_id`, `goal_ref`, `name`, `owner_ref`, `period_start`, `period_end`, `baseline`, `target`, `warning_threshold`, `critical_threshold`, `status`, `metadata` |
| [KpiMeasurement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Models/KpiMeasurement.php) | `team_id`, `metric_id`, `goal_id`, `period_ref`, `measured_on`, `value`, `progress`, `source_ref`, `metadata` |
| [KpiMetric.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Models/KpiMetric.php) | `team_id`, `metric_ref`, `name`, `description`, `unit`, `direction`, `source_contract`, `formula`, `owner_ref`, `active`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [KpiController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals-api/src/Http/Controllers/KpiController.php) | `public function index(Request $request, KpiQuery $query): mixed`<br>`public function metric(Request $request, CreateMetric $action): JsonResponse`<br>`public function goal(Request $request, KpiMetric $metric, CreateGoal $action): KpiGoalResource`<br>`public function show(KpiGoal $goal, KpiQuery $query): array`<br>`public function measurement(Request $request, KpiGoal $goal, RecordMeasurement $action): JsonResponse`<br>`public function commentary(Request $request, KpiGoal $goal, AddCommentary $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-kpi-and-goals-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/kpi-and-goals')->group(function (): void {
Route::get('/goals', [KpiController::class, 'index'])->name('accounting.kpi-and-goals.list');
Route::post('/metrics', [KpiController::class, 'metric'])->name('accounting.kpi-and-goals.metric');
Route::post('/metrics/{metric}/goals', [KpiController::class, 'goal'])->name('accounting.kpi-and-goals.goal');
Route::get('/goals/{goal}', [KpiController::class, 'show'])->name('accounting.kpi-and-goals.show');
Route::post('/goals/{goal}/measurements', [KpiController::class, 'measurement'])->name('accounting.kpi-and-goals.measurement');
Route::post('/goals/{goal}/commentary', [KpiController::class, 'commentary'])->name('accounting.kpi-and-goals.commentary');
```
<!-- layer-implementation-plan:end -->
