# Accounting: Cash-Flow Forecasting Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cash-flow-forecasting). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-cash-flow-forecasting-nuxt`
**Matching domain module:** `accounting-cash-flow-forecasting`
**Application:** Accounting
**Source feature:** [Cash-Flow Forecasting](../features/cash-flow-forecasting.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/cash-flow-forecasting.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-cash-flow-forecasting` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Direct forecast:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Opening cash:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Receivable/payable timing:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Recurring items:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Scenarios:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Manual assumptions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Variance:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Confidence:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-cash-flow-forecasting-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `direct-forecast`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `opening-cash`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `receivable-payable-timing`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `recurring-items`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `scenarios`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `manual-assumptions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `variance`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `confidence`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-cash-flow-forecasting` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/cash-flow-forecasting.md)) |
| Capability Nuxt module skeleton | [`module-accounting-cash-flow-forecasting-nuxt`](https://github.com/liberusoftware/module-accounting-cash-flow-forecasting-nuxt) (`@liberusoftware/module-accounting-cash-flow-forecasting-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Direct forecast** | Expose composable and Vue 3 component for `direct forecast` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cash-flow-forecasting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Opening cash** | Expose composable and Vue 3 component for `opening cash` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cash-flow-forecasting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Receivable/payable timing** | Expose composable and Vue 3 component for `receivable/payable timing` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cash-flow-forecasting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Recurring items** | Expose composable and Vue 3 component for `recurring items` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cash-flow-forecasting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Scenarios** | Expose composable and Vue 3 component for `scenarios` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cash-flow-forecasting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Manual assumptions** | Expose composable and Vue 3 component for `manual assumptions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cash-flow-forecasting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Variance** | Expose composable and Vue 3 component for `variance` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cash-flow-forecasting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Confidence** | Expose composable and Vue 3 component for `confidence` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cash-flow-forecasting.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CashFlowForecastQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-flow-forecasting/src/Queries/CashFlowForecastQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddForecastItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-flow-forecasting/src/Actions/AddForecastItem.php) | `public function receivable(CashFlowForecast $forecast, array $item): CashFlowForecast`<br>`public function payable(CashFlowForecast $forecast, array $item): CashFlowForecast`<br>`public function recurring(CashFlowForecast $forecast, array $item): CashFlowForecast` |
| [CreateCashFlowForecast.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-flow-forecasting/src/Actions/CreateCashFlowForecast.php) | `public function handle(array $attributes): CashFlowForecast` |
| [SetForecastScenario.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-flow-forecasting/src/Actions/SetForecastScenario.php) | `public function handle(CashFlowForecast $forecast, array $scenario): CashFlowForecast` |
| [UpdateCashFlowForecast.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-flow-forecasting/src/Actions/UpdateCashFlowForecast.php) | `public function handle(CashFlowForecast $forecast, array $data): CashFlowForecast` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CashFlowForecast.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-flow-forecasting/src/Models/CashFlowForecast.php) | `team_id`, `forecast_ref`, `currency`, `starts_on`, `ends_on`, `opening_cash`, `forecast_cash`, `variance`, `confidence`, `receivables`, `payables`, `recurring_items`, `scenarios`, `assumptions` |

| Observed API controller | Handler signatures |
| --- | --- |
| [CashFlowForecastsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-flow-forecasting-api/src/Http/Controllers/CashFlowForecastsController.php) | `public function index(CashFlowForecastQuery $query): JsonResponse`<br>`public function store(Request $request, CreateCashFlowForecast $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-cash-flow-forecasting-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-flow-forecasting-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/cash-flow-forecasting')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.cash-flow-forecasting.read')->get('/', [CashFlowForecastsController::class, 'index']);
Route::middleware('ability:accounting.cash-flow-forecasting.write')->post('/', [CashFlowForecastsController::class, 'store']);
```
<!-- layer-implementation-plan:end -->
