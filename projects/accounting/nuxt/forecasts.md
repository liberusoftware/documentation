# Accounting: Forecasts Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#forecasts). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-forecasts-nuxt`
**Matching domain module:** `accounting-forecasts`
**Application:** Accounting
**Source feature:** [Forecasts](../features/forecasts.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/forecasts.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-forecasts` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Driver/manual forecasts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Scenarios:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Rolling periods:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Actual replacement:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Assumptions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Approvals:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Variance:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-forecasts-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `driver-manual-forecasts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `scenarios`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `rolling-periods`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `actual-replacement`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `assumptions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `approvals`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `variance`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-forecasts` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/forecasts.md)) |
| Capability Nuxt module skeleton | [`module-accounting-forecasts-nuxt`](https://github.com/liberusoftware/module-accounting-forecasts-nuxt) (`@liberusoftware/module-accounting-forecasts-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Driver/manual forecasts** | Expose composable and Vue 3 component for `driver/manual forecasts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/forecasts.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Scenarios** | Expose composable and Vue 3 component for `scenarios` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/forecasts.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Rolling periods** | Expose composable and Vue 3 component for `rolling periods` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/forecasts.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Actual replacement** | Expose composable and Vue 3 component for `actual replacement` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/forecasts.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Assumptions** | Expose composable and Vue 3 component for `assumptions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/forecasts.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Approvals** | Expose composable and Vue 3 component for `approvals` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/forecasts.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Variance** | Expose composable and Vue 3 component for `variance` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/forecasts.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ForecastQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Queries/ForecastQuery.php) | `public function paginate(?int $teamId = null, ?ForecastStatus $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function variance(Forecast $forecast): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddForecastAssumption.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Actions/AddForecastAssumption.php) | `public function handle(Forecast $forecast, array $attributes): ForecastAssumption` |
| [AddForecastLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Actions/AddForecastLine.php) | `public function handle(Forecast $forecast, array $a): ForecastLine` |
| [CreateForecast.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Actions/CreateForecast.php) | `public function handle(array $a): Forecast` |
| [CreateForecastPeriods.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Actions/CreateForecastPeriods.php) | `public function handle(Forecast $forecast, ?string $startsOn = null): array` |
| [DecideForecast.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Actions/DecideForecast.php) | `public function handle(Forecast $forecast, string $actor, bool $approved, ?string $comment = null): Forecast` |
| [ReplaceActual.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Actions/ReplaceActual.php) | `public function handle(Forecast $forecast, array $a): ForecastActual` |
| [SubmitForecast.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Actions/SubmitForecast.php) | `public function handle(Forecast $forecast): Forecast` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Forecast.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Models/Forecast.php) | `team_id`, `forecast_ref`, `name`, `currency`, `method`, `status`, `base_period`, `horizon_periods`, `scenario_ref`, `metadata` |
| [ForecastActual.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Models/ForecastActual.php) | `forecast_id`, `line_id`, `period_ref`, `actual_value`, `source_ref`, `replaced_at`, `metadata` |
| [ForecastApproval.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Models/ForecastApproval.php) | `forecast_id`, `actor_ref`, `approved`, `comment`, `decided_at`, `metadata` |
| [ForecastAssumption.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Models/ForecastAssumption.php) | `forecast_id`, `assumption_ref`, `name`, `value`, `unit`, `source`, `effective_from`, `effective_to`, `metadata` |
| [ForecastLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Models/ForecastLine.php) | `forecast_id`, `period_ref`, `account_ref`, `dimension_ref`, `description`, `driver_ref`, `forecast_value`, `actual_value`, `variance_value`, `metadata` |
| [ForecastPeriod.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts/src/Models/ForecastPeriod.php) | `forecast_id`, `period_ref`, `starts_on`, `ends_on`, `status`, `is_rolling`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ForecastsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts-api/src/Http/Controllers/ForecastsController.php) | `public function __construct(private readonly ForecastQuery $query)`<br>`public function index(Request $request): ForecastResource`<br>`public function store(Request $request, CreateForecast $action): ForecastResource`<br>`public function show(Forecast $forecast): ForecastResource`<br>`public function line(Request $request, Forecast $forecast, AddForecastLine $action): ForecastResource`<br>`public function assumption(Request $request, Forecast $forecast, AddForecastAssumption $action): ForecastResource`<br>`public function periods(Request $request, Forecast $forecast, CreateForecastPeriods $action): ForecastResource`<br>`public function submit(Forecast $forecast, SubmitForecast $action): ForecastResource`<br>`public function decide(Request $request, Forecast $forecast, DecideForecast $action): ForecastResource`<br>`public function actual(Request $request, Forecast $forecast, ReplaceActual $action): ForecastResource`<br>`public function variance(Forecast $forecast): JsonResponse` |

**Observed route declarations:**

[modules/accounting-forecasts-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-forecasts-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/forecasts')->group(function (): void {
Route::middleware('ability:accounting.forecasts.read')->group(function (): void {
Route::get('/', [ForecastsController::class, 'index'])->name('accounting.forecasts.list');
Route::get('/{forecast}', [ForecastsController::class, 'show'])->name('accounting.forecasts.show');
Route::get('/{forecast}/variance', [ForecastsController::class, 'variance'])->name('accounting.forecasts.variance');
Route::middleware('ability:accounting.forecasts.write')->group(function (): void {
Route::post('/', [ForecastsController::class, 'store'])->name('accounting.forecasts.create');
Route::post('/{forecast}/lines', [ForecastsController::class, 'line'])->name('accounting.forecasts.line');
Route::post('/{forecast}/assumptions', [ForecastsController::class, 'assumption'])->name('accounting.forecasts.assumption');
Route::post('/{forecast}/periods', [ForecastsController::class, 'periods'])->name('accounting.forecasts.periods');
Route::post('/{forecast}/submit', [ForecastsController::class, 'submit'])->name('accounting.forecasts.submit');
Route::post('/{forecast}/decide', [ForecastsController::class, 'decide'])->name('accounting.forecasts.decide');
Route::post('/{forecast}/actuals', [ForecastsController::class, 'actual'])->name('accounting.forecasts.actual');
```
<!-- layer-implementation-plan:end -->
