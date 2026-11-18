# CRM: CRM Analytics Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-analytics). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-analytics-nuxt`
**Matching domain module:** `crm-analytics`
**Application:** CRM
**Source feature:** [CRM Analytics](../features/crm-analytics.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-analytics.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-analytics` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Governed datasets:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Dashboards:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reports:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Pivots:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Funnels:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Cohorts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Goals:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Schedules:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Exports:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Row-level access:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Metric lineage:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-analytics-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `governed-datasets`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `dashboards`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `reports`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `pivots`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `funnels`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `cohorts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `goals`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `schedules`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `exports`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `row-level-access`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `metric-lineage`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-analytics` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-analytics.md)) |
| Capability Nuxt module skeleton | [`module-crm-analytics-nuxt`](https://github.com/liberusoftware/module-crm-analytics-nuxt) (`@liberusoftware/module-crm-analytics-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Governed datasets** | Expose composable and Vue 3 component for `governed datasets` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Dashboards** | Expose composable and Vue 3 component for `dashboards` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Reports** | Expose composable and Vue 3 component for `reports` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Pivots** | Expose composable and Vue 3 component for `pivots` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Funnels** | Expose composable and Vue 3 component for `funnels` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Cohorts** | Expose composable and Vue 3 component for `cohorts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Goals** | Expose composable and Vue 3 component for `goals` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Schedules** | Expose composable and Vue 3 component for `schedules` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Exports** | Expose composable and Vue 3 component for `exports` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Row-level access** | Expose composable and Vue 3 component for `row-level access` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Metric lineage** | Expose composable and Vue 3 component for `metric lineage` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-analytics.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [AnalyticsQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-analytics/src/Queries/AnalyticsQuery.php) | `public function assets(int $teamId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateAnalyticsAsset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-analytics/src/Actions/CreateAnalyticsAsset.php) | `public function execute(int $teamId, int $userId, array $input): AnalyticsAsset` |
| [ExecuteAnalyticsAsset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-analytics/src/Actions/ExecuteAnalyticsAsset.php) | `public function execute(int $teamId, int $userId, AnalyticsAsset $asset, array $parameters = [], string $kind = 'preview'): AnalyticsExecution` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AnalyticsAsset.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-analytics/src/Models/AnalyticsAsset.php) | No literal fillable array detected; inspect the model and API schema. |
| [AnalyticsExecution.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-analytics/src/Models/AnalyticsExecution.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [AnalyticsController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-analytics-api/src/Http/Controllers/AnalyticsController.php) | `public function __construct(private readonly AnalyticsQuery $query)`<br>`public function index(): JsonResponse`<br>`public function store(CreateAnalyticsAsset $action): JsonResponse`<br>`public function execute(AnalyticsAsset $asset, ExecuteAnalyticsAsset $action): JsonResponse` |

**Observed route declarations:**

[modules/crm-analytics-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-analytics-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/analytics')->group(function (): void {
Route::get('assets', [AnalyticsController::class, 'index']);
Route::post('assets', [AnalyticsController::class, 'store']);
Route::post('assets/{asset}/execute', [AnalyticsController::class, 'execute']);
```
<!-- layer-implementation-plan:end -->
