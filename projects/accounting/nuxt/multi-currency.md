# Accounting: Multi-Currency Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#multi-currency). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-multi-currency-nuxt`
**Matching domain module:** `accounting-multi-currency`
**Application:** Accounting
**Source feature:** [Multi-Currency](../features/multi-currency.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/multi-currency.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-multi-currency` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Transaction/functional/reporting currencies:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Rates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Revaluation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Realized/unrealized gains:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Historical rates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reconciliation:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-multi-currency-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `transaction-functional-reporting-currencies`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `rates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `revaluation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `realized-unrealized-gains`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `historical-rates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `reconciliation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-multi-currency` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/multi-currency.md)) |
| Capability Nuxt module skeleton | [`module-accounting-multi-currency-nuxt`](https://github.com/liberusoftware/module-accounting-multi-currency-nuxt) (`@liberusoftware/module-accounting-multi-currency-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Transaction/functional/reporting currencies** | Expose composable and Vue 3 component for `transaction/functional/reporting currencies` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/multi-currency.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Rates** | Expose composable and Vue 3 component for `rates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/multi-currency.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Revaluation** | Expose composable and Vue 3 component for `revaluation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/multi-currency.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Realized/unrealized gains** | Expose composable and Vue 3 component for `realized/unrealized gains` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/multi-currency.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Historical rates** | Expose composable and Vue 3 component for `historical rates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/multi-currency.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Reconciliation** | Expose composable and Vue 3 component for `reconciliation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/multi-currency.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CurrencyQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency/src/Queries/CurrencyQuery.php) | `public function rates(?int $teamId = null, ?string $from = null, ?string $to = null, int $perPage = 25): LengthAwarePaginator`<br>`public function revaluations(?int $teamId = null): LengthAwarePaginator`<br>`public function report(RevaluationRun $run): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ConfigureCurrency.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency/src/Actions/ConfigureCurrency.php) | `public function handle(array $attributes): CurrencyProfile` |
| [CreateRevaluation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency/src/Actions/CreateRevaluation.php) | `public function handle(array $attributes, array $positions): RevaluationRun` |
| [RecordExchangeRate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency/src/Actions/RecordExchangeRate.php) | `public function handle(array $attributes): ExchangeRate` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CurrencyProfile.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency/src/Models/CurrencyProfile.php) | `team_id`, `scope_ref`, `currency`, `role`, `is_active`, `metadata` |
| [CurrencyReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency/src/Models/CurrencyReconciliation.php) | `run_id`, `reference_type`, `reference_id`, `expected_gain_loss`, `actual_gain_loss`, `variance`, `status`, `external_ref`, `notes`, `metadata` |
| [ExchangeRate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency/src/Models/ExchangeRate.php) | `team_id`, `from_currency`, `to_currency`, `rate_date`, `rate`, `source`, `rate_type`, `is_historical`, `metadata` |
| [RevaluationPosition.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency/src/Models/RevaluationPosition.php) | `run_id`, `reference_type`, `reference_id`, `currency`, `foreign_amount`, `book_rate`, `closing_rate`, `book_value`, `closing_value`, `gain_loss`, `gain_status`, `metadata` |
| [RevaluationRun.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency/src/Models/RevaluationRun.php) | `team_id`, `run_ref`, `scope_ref`, `as_of_date`, `functional_currency`, `status`, `source_hash`, `realized_gain`, `realized_loss`, `unrealized_gain`, `unrealized_loss`, `summary`, `failure_message`, `requested_by`, `posted_by`, `posted_at`, `metadata` |
| [Currency.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency-api/src/Models/Currency.php) | `code`, `name`, `symbol`, `is_default` |

| Observed API controller | Handler signatures |
| --- | --- |
| [MultiCurrencyController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency-api/src/Http/Controllers/MultiCurrencyController.php) | `public function rates(Request $request, CurrencyQuery $query): mixed`<br>`public function profile(Request $request, ConfigureCurrency $action): JsonResponse`<br>`public function rate(Request $request, RecordExchangeRate $action): JsonResponse`<br>`public function revaluation(Request $request, CreateRevaluation $action): JsonResponse`<br>`public function show(RevaluationRun $revaluationRun): RevaluationResource`<br>`public function report(RevaluationRun $revaluationRun, CurrencyQuery $query): array` |

**Observed route declarations:**

[modules/accounting-multi-currency-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-multi-currency-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/multi-currency')->group(function (): void {
Route::get('/rates', [MultiCurrencyController::class, 'rates'])->name('accounting.multi-currency.rates');
Route::post('/profiles', [MultiCurrencyController::class, 'profile'])->name('accounting.multi-currency.profile');
Route::post('/rates', [MultiCurrencyController::class, 'rate'])->name('accounting.multi-currency.rate');
Route::post('/revaluations', [MultiCurrencyController::class, 'revaluation'])->name('accounting.multi-currency.revaluation');
Route::get('/revaluations/{revaluationRun}', [MultiCurrencyController::class, 'show'])->name('accounting.multi-currency.show');
Route::get('/revaluations/{revaluationRun}/report', [MultiCurrencyController::class, 'report'])->name('accounting.multi-currency.report');
```
<!-- layer-implementation-plan:end -->
