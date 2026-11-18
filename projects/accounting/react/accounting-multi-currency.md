# Accounting: Accounting Multi Currency React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-multi-currency). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-accounting-accounting-multi-currency-react-inertia`
**Matching domain module:** `accounting-multi-currency`
**Application:** Accounting
**Source feature:** [Accounting Multi Currency](../features/accounting-multi-currency.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-multi-currency.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Transaction/functional/reporting currencies:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Rates:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Revaluation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Realized/unrealized gains:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Historical rates:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Reconciliation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-accounting-accounting-multi-currency-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `transaction-functional-reporting-currencies`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `rates`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `revaluation`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `realized-unrealized-gains`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `historical-rates`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `reconciliation`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

## 4. API contract and Inertia consumption

<!-- inertia-transport:start -->
### Inertia transport boundary

Use Laravel-owned Inertia page/command routes for visits and forms. The controller can invoke the module's public application actions in the same host or use a deliberate API adapter, then return an Inertia page/redirect response. A bare REST JSON resource response is not an Inertia page. Keep authoritative domain authorization and validation in the owning boundary for either path.

Independent API consumers and Next.js use their reviewed HTTP/session integration. Share DTOs and framework-independent UI primitives; keep Inertia page props, visits, form errors and redirects in the Inertia wrapper. Do not introduce loopback HTTP solely to reuse a public action inside the same Laravel host.

See the [Inertia standard](../../../standards/INERTIA.md), [request lifecycle](https://inertiajs.com/docs/v3/core-concepts/how-it-works) and [redirect behavior](https://inertiajs.com/docs/v3/the-basics/redirects).
<!-- inertia-transport:end -->

- Reuse the matching public application/API contracts. For HTTP consumption, use its documented schemas, routes, authentication, permissions, tenant context, errors and operation semantics; Inertia visits still require an Inertia response.
- Keep a typed module-local API client and hooks boundary; use Inertia visits for page transitions and `useForm`/`router` for mutations, preserving server validation and redirect semantics.
- Forward Sanctum cookies or approved authorization headers through a controlled first-party boundary; never persist long-lived tokens in browser storage or expose secrets in page props.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, SSR hydration where enabled, and minimal-host installation tests.
- Test observable behavior with TypeScript, ESLint, Vitest, React Testing Library, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `accounting-multi-currency` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-accounting-erp-laravel-inertia-react`](https://github.com/liberusoftware/project-accounting-erp-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-accounting-multi-currency-react-inertia`](https://github.com/liberusoftware/module-accounting-multi-currency-react-inertia) (`@liberusoftware/module-accounting-multi-currency-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/accounting-multi-currency.md) · [Core plan](../core/accounting-multi-currency.md) · [API plan](../api/accounting-multi-currency.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Transaction/functional/reporting currencies** | Render `transaction/functional/reporting currencies` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Rates** | Render `rates` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Revaluation** | Render `revaluation` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Realized/unrealized gains** | Render `realized/unrealized gains` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Historical rates** | Render `historical rates` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Reconciliation** | Render `reconciliation` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

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
