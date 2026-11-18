# CRM: Crm Forecasting Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-forecasting). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-crm-forecasting-nuxt`
**Matching domain module:** `crm-forecasting`
**Application:** CRM
**Source feature:** [Crm Forecasting](../features/crm-forecasting.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-forecasting.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-forecasting` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Forecast categories:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Rollups:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Manager adjustments:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Commit/best-case/pipeline views:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Coverage:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Trend:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Scenario:** page/component/composable/API-action behavior for this module's authorized workflow.
- **History:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Accuracy:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Submission workflow:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-crm-forecasting-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `forecast-categories`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `rollups`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `manager-adjustments`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `commit-best-case-pipeline-views`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `coverage`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `trend`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `scenario`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `history`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `accuracy`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `submission-workflow`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-forecasting` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-forecasting.md)) |
| Capability Nuxt module skeleton | [`module-crm-forecasting-nuxt`](https://github.com/liberusoftware/module-crm-forecasting-nuxt) (`@liberusoftware/module-crm-forecasting-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Forecast categories** | Expose composable and Vue 3 component for `forecast categories` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-forecasting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Rollups** | Expose composable and Vue 3 component for `rollups` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-forecasting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Manager adjustments** | Expose composable and Vue 3 component for `manager adjustments` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-forecasting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Commit/best-case/pipeline views** | Expose composable and Vue 3 component for `commit/best-case/pipeline views` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-forecasting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Coverage** | Expose composable and Vue 3 component for `coverage` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-forecasting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Trend** | Expose composable and Vue 3 component for `trend` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-forecasting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Scenario** | Expose composable and Vue 3 component for `scenario` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-forecasting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **History** | Expose composable and Vue 3 component for `history` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-forecasting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Accuracy** | Expose composable and Vue 3 component for `accuracy` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-forecasting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Submission workflow** | Expose composable and Vue 3 component for `submission workflow` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-forecasting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ForecastingQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forecasting/src/Queries/ForecastingQuery.php) | `public function categories(int $teamId)`<br>`public function forecasts(int $teamId, string $period)`<br>`public function summary(int $teamId, string $period): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCategory.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forecasting/src/Actions/CreateCategory.php) | `public function __construct(private readonly ForecastingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ForecastCategory` |
| [RecordForecast.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forecasting/src/Actions/RecordForecast.php) | `public function __construct(private readonly ForecastingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): Forecast` |
| [SubmitForecast.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forecasting/src/Actions/SubmitForecast.php) | `public function __construct(private readonly ForecastingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, Forecast $forecast): ForecastSubmission` |
| [ForecastingPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forecasting/src/Services/ForecastingPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Forecast.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forecasting/src/Models/Forecast.php) | No literal fillable array detected; inspect the model and API schema. |
| [ForecastAdjustment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forecasting/src/Models/ForecastAdjustment.php) | No literal fillable array detected; inspect the model and API schema. |
| [ForecastCategory.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forecasting/src/Models/ForecastCategory.php) | No literal fillable array detected; inspect the model and API schema. |
| [ForecastSubmission.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forecasting/src/Models/ForecastSubmission.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ForecastingController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forecasting-api/src/Http/Controllers/ForecastingController.php) | `public function __construct(private readonly ForecastingQuery $query)`<br>`public function categories(): JsonResponse`<br>`public function index(string $period): JsonResponse`<br>`public function storeCategory(CreateCategory $action): JsonResponse`<br>`public function store(RecordForecast $action): JsonResponse`<br>`public function submit(int $forecast, SubmitForecast $action): JsonResponse`<br>`public function adjust(int $forecast, AdjustForecast $action): JsonResponse` |

**Observed route declarations:**

[modules/crm-forecasting-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forecasting-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/forecasting')->group(function (): void {
Route::get('categories', [ForecastingController::class, 'categories']);
Route::get('forecasts/{period}', [ForecastingController::class, 'index']);
Route::post('categories', [ForecastingController::class, 'storeCategory']);
Route::post('forecasts', [ForecastingController::class, 'store']);
Route::post('forecasts/{forecast}/submit', [ForecastingController::class, 'submit']);
Route::post('forecasts/{forecast}/adjustments', [ForecastingController::class, 'adjust']);
```
<!-- layer-implementation-plan:end -->
