# Accounting: Deposits and Clearing Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#deposits-and-clearing). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-deposits-and-clearing-nuxt`
**Matching domain module:** `accounting-deposits-and-clearing`
**Application:** Accounting
**Source feature:** [Deposits and Clearing](../features/deposits-and-clearing.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/deposits-and-clearing.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-deposits-and-clearing` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Undeposited funds:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Grouped deposits:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Payment-provider clearing:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Fees:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Payouts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Timing differences:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reconciliation:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-deposits-and-clearing-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `undeposited-funds`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `grouped-deposits`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `payment-provider-clearing`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `fees`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `payouts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `timing-differences`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
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

- Package identity, public exports, API dependency, and module dependency match `accounting-deposits-and-clearing` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/deposits-and-clearing.md)) |
| Capability Nuxt module skeleton | [`module-accounting-deposits-and-clearing-nuxt`](https://github.com/liberusoftware/module-accounting-deposits-and-clearing-nuxt) (`@liberusoftware/module-accounting-deposits-and-clearing-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Undeposited funds** | Expose composable and Vue 3 component for `undeposited funds` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/deposits-and-clearing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Grouped deposits** | Expose composable and Vue 3 component for `grouped deposits` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/deposits-and-clearing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Payment-provider clearing** | Expose composable and Vue 3 component for `payment-provider clearing` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/deposits-and-clearing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Fees** | Expose composable and Vue 3 component for `fees` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/deposits-and-clearing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Payouts** | Expose composable and Vue 3 component for `payouts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/deposits-and-clearing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Timing differences** | Expose composable and Vue 3 component for `timing differences` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/deposits-and-clearing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Reconciliation** | Expose composable and Vue 3 component for `reconciliation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/deposits-and-clearing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ClearingQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Queries/ClearingQuery.php) | `public function undeposited(int $teamId): Collection`<br>`public function deposits(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateGroupedDeposit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Actions/CreateGroupedDeposit.php) | `public function handle(array $attributes, array $fundIds): ClearingDeposit` |
| [ReconcileDeposit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Actions/ReconcileDeposit.php) | `public function handle(ClearingDeposit $deposit, float $payoutAmount, float $feeAmount = 0): ClearingDeposit` |
| [RecordUndepositedFund.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Actions/RecordUndepositedFund.php) | `public function handle(array $attributes): ClearingFund` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ClearingDeposit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Models/ClearingDeposit.php) | `team_id`, `deposit_ref`, `provider`, `account_ref`, `currency`, `gross_amount`, `fee_amount`, `payout_amount`, `deposit_date`, `status`, `metadata` |
| [ClearingFund.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Models/ClearingFund.php) | `team_id`, `deposit_id`, `source_type`, `source_id`, `amount`, `currency`, `received_on`, `status`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ClearingController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing-api/src/Http/Controllers/ClearingController.php) | `public function funds(ClearingQuery $query): JsonResponse`<br>`public function deposits(ClearingQuery $query): JsonResponse`<br>`public function recordFund(Request $request, RecordUndepositedFund $action): JsonResponse`<br>`public function createDeposit(Request $request, CreateGroupedDeposit $action): JsonResponse`<br>`public function reconcile(Request $request, string $deposit, ReconcileDeposit $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-deposits-and-clearing-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/deposits-and-clearing')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.deposits-and-clearing.read')->group(function (): void {
Route::get('/funds', [ClearingController::class, 'funds']);
Route::get('/deposits', [ClearingController::class, 'deposits']);
Route::middleware('ability:accounting.deposits-and-clearing.write')->group(function (): void {
Route::post('/funds', [ClearingController::class, 'recordFund']);
Route::post('/deposits', [ClearingController::class, 'createDeposit']);
Route::post('/deposits/{deposit}/reconcile', [ClearingController::class, 'reconcile']);
```
<!-- layer-implementation-plan:end -->
