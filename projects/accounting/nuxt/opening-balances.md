# Accounting: Opening Balances Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#opening-balances). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-opening-balances-nuxt`
**Matching domain module:** `accounting-opening-balances`
**Application:** Accounting
**Source feature:** [Opening Balances](../features/opening-balances.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/opening-balances.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-opening-balances` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Migration date:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Account/customer/supplier/bank/item balances:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Outstanding documents:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Validation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Approval:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reconciliation:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-opening-balances-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `migration-date`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `account-customer-supplier-bank-item-balances`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `outstanding-documents`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `validation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `approval`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
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

- Package identity, public exports, API dependency, and module dependency match `accounting-opening-balances` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/opening-balances.md)) |
| Capability Nuxt module skeleton | [`module-accounting-opening-balances-nuxt`](https://github.com/liberusoftware/module-accounting-opening-balances-nuxt) (`@liberusoftware/module-accounting-opening-balances-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Migration date** | Expose composable and Vue 3 component for `migration date` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/opening-balances.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Account/customer/supplier/bank/item balances** | Expose composable and Vue 3 component for `account/customer/supplier/bank/item balances` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/opening-balances.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Outstanding documents** | Expose composable and Vue 3 component for `outstanding documents` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/opening-balances.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Validation** | Expose composable and Vue 3 component for `validation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/opening-balances.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Approval** | Expose composable and Vue 3 component for `approval` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/opening-balances.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Reconciliation** | Expose composable and Vue 3 component for `reconciliation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/opening-balances.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [OpeningBalanceQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-opening-balances/src/Queries/OpeningBalanceQuery.php) | `public function paginate(?int $teamId = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApproveOpeningBalances.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-opening-balances/src/Actions/ApproveOpeningBalances.php) | `public function handle(OpeningBalanceBatch $batch, int $actorId): OpeningBalanceBatch` |
| [CreateOpeningBalanceBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-opening-balances/src/Actions/CreateOpeningBalanceBatch.php) | `public function handle(array $attributes, array $entries): OpeningBalanceBatch` |
| [ReconcileOpeningBalances.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-opening-balances/src/Actions/ReconcileOpeningBalances.php) | `public function handle(OpeningBalanceBatch $batch, array $actuals): OpeningBalanceBatch` |
| [ValidateOpeningBalances.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-opening-balances/src/Actions/ValidateOpeningBalances.php) | `public function handle(OpeningBalanceBatch $batch): OpeningBalanceBatch` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [OpeningBalanceAudit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-opening-balances/src/Models/OpeningBalanceAudit.php) | `batch_id`, `event_type`, `actor_id`, `payload`, `payload_hash`, `created_at` |
| [OpeningBalanceBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-opening-balances/src/Models/OpeningBalanceBatch.php) | `team_id`, `batch_ref`, `migration_date`, `currency`, `status`, `source_hash`, `idempotency_key`, `summary`, `failure_message`, `requested_by`, `approved_by`, `approved_at`, `metadata` |
| [OpeningBalanceEntry.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-opening-balances/src/Models/OpeningBalanceEntry.php) | `batch_id`, `balance_type`, `reference_type`, `reference_id`, `document_ref`, `document_date`, `due_date`, `currency`, `debit_amount`, `credit_amount`, `status`, `description`, `metadata` |
| [OpeningBalanceReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-opening-balances/src/Models/OpeningBalanceReconciliation.php) | `batch_id`, `entry_id`, `expected_amount`, `actual_amount`, `variance`, `status`, `external_ref`, `notes`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [OpeningBalancesController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-opening-balances-api/src/Http/Controllers/OpeningBalancesController.php) | `public function index(Request $request, OpeningBalanceQuery $query): mixed`<br>`public function store(Request $request, CreateOpeningBalanceBatch $action): JsonResponse`<br>`public function show(OpeningBalanceBatch $openingBalance): OpeningBalanceResource`<br>`public function validateBatch(OpeningBalanceBatch $openingBalance, ValidateOpeningBalances $action): OpeningBalanceResource`<br>`public function approve(Request $request, OpeningBalanceBatch $openingBalance, ApproveOpeningBalances $action): OpeningBalanceResource`<br>`public function reconcile(Request $request, OpeningBalanceBatch $openingBalance, ReconcileOpeningBalances $action): OpeningBalanceResource` |

**Observed route declarations:**

[modules/accounting-opening-balances-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-opening-balances-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/opening-balances')->group(function (): void {
Route::get('/', [OpeningBalancesController::class, 'index'])->name('accounting.opening-balances.list');
Route::post('/', [OpeningBalancesController::class, 'store'])->name('accounting.opening-balances.create');
Route::get('/{openingBalance}', [OpeningBalancesController::class, 'show'])->name('accounting.opening-balances.show');
Route::post('/{openingBalance}/validate', [OpeningBalancesController::class, 'validateBatch'])->name('accounting.opening-balances.validate');
Route::post('/{openingBalance}/approve', [OpeningBalancesController::class, 'approve'])->name('accounting.opening-balances.approve');
Route::post('/{openingBalance}/reconcile', [OpeningBalancesController::class, 'reconcile'])->name('accounting.opening-balances.reconcile');
```
<!-- layer-implementation-plan:end -->
