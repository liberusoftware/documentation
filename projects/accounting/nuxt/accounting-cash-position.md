# Accounting: Accounting Cash Position Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-cash-position). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-accounting-cash-position-nuxt`
**Matching domain module:** `accounting-cash-position`
**Application:** Accounting
**Source feature:** [Accounting Cash Position](../features/accounting-cash-position.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-cash-position.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-cash-position` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Available/ledger balances:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Outstanding receipts/payments:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Committed cash:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Entity/currency views:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Freshness:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-accounting-cash-position-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `available-ledger-balances`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `outstanding-receipts-payments`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `committed-cash`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `entity-currency-views`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `freshness`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-cash-position` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-cash-position.md)) |
| Capability Nuxt module skeleton | [`module-accounting-cash-position-nuxt`](https://github.com/liberusoftware/module-accounting-cash-position-nuxt) (`@liberusoftware/module-accounting-cash-position-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Available/ledger balances** | Expose composable and Vue 3 component for `available/ledger balances` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-cash-position.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Outstanding receipts/payments** | Expose composable and Vue 3 component for `outstanding receipts/payments` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-cash-position.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Committed cash** | Expose composable and Vue 3 component for `committed cash` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-cash-position.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Entity/currency views** | Expose composable and Vue 3 component for `entity/currency views` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-cash-position.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Freshness** | Expose composable and Vue 3 component for `freshness` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-cash-position.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CashPositionQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-position/src/Queries/CashPositionQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCashPosition.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-position/src/Actions/CreateCashPosition.php) | `public function handle(array $attributes): CashPosition` |
| [RefreshCashPosition.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-position/src/Actions/RefreshCashPosition.php) | `public function handle(CashPosition $position, array $balances): CashPosition` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CashPosition.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-position/src/Models/CashPosition.php) | `team_id`, `view_ref`, `entity_ref`, `currency`, `ledger_balance`, `available_balance`, `outstanding_receipts`, `outstanding_payments`, `committed_cash`, `refreshed_at` |

| Observed API controller | Handler signatures |
| --- | --- |
| [CashPositionsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-position-api/src/Http/Controllers/CashPositionsController.php) | `public function index(CashPositionQuery $query): JsonResponse`<br>`public function store(Request $request, CreateCashPosition $action): JsonResponse`<br>`public function refresh(Request $request, string $position, RefreshCashPosition $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-cash-position-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-cash-position-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/cash-position')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.cash-position.read')->get('/', [CashPositionsController::class, 'index']);
Route::middleware('ability:accounting.cash-position.write')->group(function (): void {
Route::post('/', [CashPositionsController::class, 'store']);
Route::post('/{position}/refresh', [CashPositionsController::class, 'refresh']);
```
<!-- layer-implementation-plan:end -->
