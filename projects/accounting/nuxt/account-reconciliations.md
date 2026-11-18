# Accounting: Account Reconciliations Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#account-reconciliations). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-account-reconciliations-nuxt`
**Matching domain module:** `accounting-account-reconciliations`
**Application:** Accounting
**Source feature:** [Account Reconciliations](../features/account-reconciliations.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/account-reconciliations.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-account-reconciliations` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **GL account templates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Source balances:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Supporting items:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Preparer/reviewer:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Aging:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Certification:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Carry-forward:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-account-reconciliations-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `gl-account-templates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `source-balances`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `supporting-items`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `preparer-reviewer`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `aging`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `certification`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `carry-forward`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-account-reconciliations` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/account-reconciliations.md)) |
| Capability Nuxt module skeleton | [`module-accounting-account-reconciliations-nuxt`](https://github.com/liberusoftware/module-accounting-account-reconciliations-nuxt) (`@liberusoftware/module-accounting-account-reconciliations-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **GL account templates** | Expose composable and Vue 3 component for `gl account templates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/account-reconciliations.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Source balances** | Expose composable and Vue 3 component for `source balances` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/account-reconciliations.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Supporting items** | Expose composable and Vue 3 component for `supporting items` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/account-reconciliations.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Preparer/reviewer** | Expose composable and Vue 3 component for `preparer/reviewer` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/account-reconciliations.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Aging** | Expose composable and Vue 3 component for `aging` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/account-reconciliations.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Certification** | Expose composable and Vue 3 component for `certification` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/account-reconciliations.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Carry-forward** | Expose composable and Vue 3 component for `carry-forward` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/account-reconciliations.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [AccountReconciliationQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/src/Queries/AccountReconciliationQuery.php) | `public function paginate(?int $teamId, ?string $status = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CarryForwardAccountReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/src/Actions/CarryForwardAccountReconciliation.php) | `public function handle(AccountReconciliation $reconciliation, array $carryForward): AccountReconciliation` |
| [CertifyAccountReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/src/Actions/CertifyAccountReconciliation.php) | `public function handle(AccountReconciliation $reconciliation, array $certification): AccountReconciliation` |
| [CreateAccountReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/src/Actions/CreateAccountReconciliation.php) | `public function handle(array $attributes): AccountReconciliation` |
| [PrepareAccountReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/src/Actions/PrepareAccountReconciliation.php) | `public function handle(AccountReconciliation $reconciliation, array $preparer, array $sourceBalance, array $supportingItems = []): AccountReconciliation` |
| [ReviewAccountReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/src/Actions/ReviewAccountReconciliation.php) | `public function handle(AccountReconciliation $reconciliation, array $reviewer): AccountReconciliation` |
| [AccountReconciliationsPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations-api/src/Policies/AccountReconciliationsPolicy.php) | `public function viewAny(?object $user): bool`<br>`public function view(?object $user, object $record): bool`<br>`public function create(?object $user): bool`<br>`public function update(?object $user, object $record): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AccountReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/src/Models/AccountReconciliation.php) | `team_id`, `book_id`, `account_id`, `period_start`, `period_end`, `status`, `template`, `source_balance`, `supporting_items`, `preparer`, `reviewer`, `aging`, `certification`, `carry_forward` |
| [Account.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations-api/src/Models/Account.php) | `account_number`, `account_name`, `account_type`, `normal_balance`, `balance`, `opening_balance`, `description`, `currency_id`, `parent_id`, `industry_type`, `is_active`, `allow_manual_entry`, `user_id`, `team_id`, `qbo_id`, `qbo_sync_token`, `xero_id`, `sage_id` |

| Observed API controller | Handler signatures |
| --- | --- |
| [AccountReconciliationController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations-api/src/Http/Controllers/AccountReconciliationController.php) | `public function index(Request $request, AccountReconciliationQuery $query): mixed`<br>`public function show(AccountReconciliation $reconciliation): AccountReconciliationResource`<br>`public function store(Request $request, CreateAccountReconciliation $action): AccountReconciliationResource`<br>`public function prepare(Request $request, AccountReconciliation $reconciliation, PrepareAccountReconciliation $action): AccountReconciliationResource`<br>`public function review(Request $request, AccountReconciliation $reconciliation, ReviewAccountReconciliation $action): AccountReconciliationResource`<br>`public function certify(Request $request, AccountReconciliation $reconciliation, CertifyAccountReconciliation $action): AccountReconciliationResource`<br>`public function carryForward(Request $request, AccountReconciliation $reconciliation, CarryForwardAccountReconciliation $action): AccountReconciliationResource` |

**Observed route declarations:**

[modules/accounting-account-reconciliations-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/account-reconciliations')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [AccountReconciliationController::class, 'index'])->middleware('ability:accounting.account-reconciliations.read');
Route::post('/', [AccountReconciliationController::class, 'store'])->middleware('ability:accounting.account-reconciliations.write');
Route::post('/{reconciliation}/prepare', [AccountReconciliationController::class, 'prepare'])->middleware('ability:accounting.account-reconciliations.write');
Route::post('/{reconciliation}/review', [AccountReconciliationController::class, 'review'])->middleware('ability:accounting.account-reconciliations.write');
Route::post('/{reconciliation}/certify', [AccountReconciliationController::class, 'certify'])->middleware('ability:accounting.account-reconciliations.write');
Route::post('/{reconciliation}/carry-forward', [AccountReconciliationController::class, 'carryForward'])->middleware('ability:accounting.account-reconciliations.write');
Route::get('/{reconciliation}', [AccountReconciliationController::class, 'show'])->middleware('ability:accounting.account-reconciliations.read');
```
<!-- layer-implementation-plan:end -->
