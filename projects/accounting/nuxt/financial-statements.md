# Accounting: Financial Statements Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#financial-statements). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-financial-statements-nuxt`
**Matching domain module:** `accounting-financial-statements`
**Application:** Accounting
**Source feature:** [Financial Statements](../features/financial-statements.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/financial-statements.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-financial-statements` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Profit and loss:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Balance sheet:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Cash flow:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Changes in equity:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Comparative periods:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Dimensions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Drill-through:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-financial-statements-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `profit-and-loss`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `balance-sheet`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `cash-flow`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `changes-in-equity`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `comparative-periods`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `dimensions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `drill-through`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-financial-statements` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/financial-statements.md)) |
| Capability Nuxt module skeleton | [`module-accounting-financial-statements-nuxt`](https://github.com/liberusoftware/module-accounting-financial-statements-nuxt) (`@liberusoftware/module-accounting-financial-statements-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Profit and loss** | Expose composable and Vue 3 component for `profit and loss` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/financial-statements.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Balance sheet** | Expose composable and Vue 3 component for `balance sheet` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/financial-statements.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Cash flow** | Expose composable and Vue 3 component for `cash flow` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/financial-statements.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Changes in equity** | Expose composable and Vue 3 component for `changes in equity` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/financial-statements.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Comparative periods** | Expose composable and Vue 3 component for `comparative periods` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/financial-statements.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Dimensions** | Expose composable and Vue 3 component for `dimensions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/financial-statements.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Drill-through** | Expose composable and Vue 3 component for `drill-through` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/financial-statements.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [StatementQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-statements/src/Queries/StatementQuery.php) | `public function profitAndLoss(int $bookId, string $start, string $end, ?array $dimensions = null): array`<br>`public function balanceSheet(int $bookId, string $asOf, ?array $dimensions = null): array`<br>`public function cashFlow(int $bookId, string $start, string $end, ?array $dimensions = null): array`<br>`public function changesInEquity(int $bookId, string $start, string $end, ?array $dimensions = null): array`<br>`public function comparative(int $bookId, string $start, string $end, string $compareStart, string $compareEnd, ?array $dimensions = null): array`<br>`public function drillThrough(int $bookId, int $accountId, string $start, string $end, ?array $dimensions = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [FinancialStatementsPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-statements-api/src/Policies/FinancialStatementsPolicy.php) | `public function view(?Authenticatable $user): bool` |

| Observed API controller | Handler signatures |
| --- | --- |
| [FinancialStatementsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-statements-api/src/Http/Controllers/FinancialStatementsController.php) | `public function profitAndLoss(Request $request, StatementQuery $query): JsonResponse`<br>`public function balanceSheet(Request $request, StatementQuery $query): JsonResponse`<br>`public function cashFlow(Request $request, StatementQuery $query): JsonResponse`<br>`public function equity(Request $request, StatementQuery $query): JsonResponse`<br>`public function comparative(Request $request, StatementQuery $query): JsonResponse`<br>`public function drillThrough(Request $request, StatementQuery $query): JsonResponse` |

**Observed route declarations:**

[modules/accounting-financial-statements-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-financial-statements-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api', 'ability:accounting.financial-statements.read'])
Route::get('/profit-and-loss', [FinancialStatementsController::class, 'profitAndLoss'])->name('accounting.financial-statements.profit-and-loss');
Route::get('/balance-sheet', [FinancialStatementsController::class, 'balanceSheet'])->name('accounting.financial-statements.balance-sheet');
Route::get('/cash-flow', [FinancialStatementsController::class, 'cashFlow'])->name('accounting.financial-statements.cash-flow');
Route::get('/changes-in-equity', [FinancialStatementsController::class, 'equity'])->name('accounting.financial-statements.changes-in-equity');
Route::get('/comparative', [FinancialStatementsController::class, 'comparative'])->name('accounting.financial-statements.comparative');
Route::get('/drill-through', [FinancialStatementsController::class, 'drillThrough'])->name('accounting.financial-statements.drill-through');
```
<!-- layer-implementation-plan:end -->
