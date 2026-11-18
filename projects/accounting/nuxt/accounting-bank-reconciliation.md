# Accounting: Accounting Bank Reconciliation Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-bank-reconciliation). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-accounting-bank-reconciliation-nuxt`
**Matching domain module:** `accounting-bank-reconciliation`
**Application:** Accounting
**Source feature:** [Accounting Bank Reconciliation](../features/accounting-bank-reconciliation.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-bank-reconciliation.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-bank-reconciliation` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Suggested/exact matches:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Transfers:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Grouped receipts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Fees/interest:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Adjustments:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Statement balance:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Exceptions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Sign-off:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-accounting-bank-reconciliation-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `suggested-exact-matches`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `transfers`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `grouped-receipts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `fees-interest`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `adjustments`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `statement-balance`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `exceptions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `sign-off`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-bank-reconciliation` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-bank-reconciliation.md)) |
| Capability Nuxt module skeleton | [`module-accounting-bank-reconciliation-nuxt`](https://github.com/liberusoftware/module-accounting-bank-reconciliation-nuxt) (`@liberusoftware/module-accounting-bank-reconciliation-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Suggested/exact matches** | Expose composable and Vue 3 component for `suggested/exact matches` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-bank-reconciliation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Transfers** | Expose composable and Vue 3 component for `transfers` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-bank-reconciliation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Grouped receipts** | Expose composable and Vue 3 component for `grouped receipts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-bank-reconciliation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Fees/interest** | Expose composable and Vue 3 component for `fees/interest` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-bank-reconciliation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Adjustments** | Expose composable and Vue 3 component for `adjustments` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-bank-reconciliation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Statement balance** | Expose composable and Vue 3 component for `statement balance` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-bank-reconciliation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Exceptions** | Expose composable and Vue 3 component for `exceptions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-bank-reconciliation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Sign-off** | Expose composable and Vue 3 component for `sign-off` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-bank-reconciliation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ReconciliationSummaryQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/src/Queries/ReconciliationSummaryQuery.php) | `public function handle(ReconciliationSession $session): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddReconciliationEntry.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/src/Actions/AddReconciliationEntry.php) | `public function handle(ReconciliationSession $session, array $attributes): ReconciliationEntry` |
| [ConfirmReconciliationEntry.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/src/Actions/ConfirmReconciliationEntry.php) | `public function handle(ReconciliationEntry $entry): ReconciliationEntry` |
| [CreateReconciliationSession.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/src/Actions/CreateReconciliationSession.php) | `public function handle(array $attributes): ReconciliationSession` |
| [SignOffReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/src/Actions/SignOffReconciliation.php) | `public function handle(ReconciliationSession $session): ReconciliationSession` |
| [BankReconciliationPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation-api/src/Policies/BankReconciliationPolicy.php) | `public function viewAny(?object $user = null): bool`<br>`public function view(?object $user, object $session): bool`<br>`public function create(?object $user = null): bool`<br>`public function update(?object $user, object $session): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ReconciliationEntry.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/src/Models/ReconciliationEntry.php) | `team_id`, `session_id`, `source_type`, `source_id`, `kind`, `status`, `amount`, `currency`, `confidence`, `description`, `metadata`, `exception_reason`, `confirmed_at`, `confirmed_by` |
| [ReconciliationSession.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/src/Models/ReconciliationSession.php) | `team_id`, `user_id`, `bank_account_id`, `period_start`, `period_end`, `opening_balance`, `statement_balance`, `status`, `signed_off_at`, `signed_off_by`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ReconciliationController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation-api/src/Http/Controllers/ReconciliationController.php) | `public function index(Request $request): mixed`<br>`public function store(Request $request, CreateReconciliationSession $action): ReconciliationResource`<br>`public function show(string $session): ReconciliationResource`<br>`public function entry(Request $request, string $session, AddReconciliationEntry $action): mixed`<br>`public function confirm(string $session, string $entry, ConfirmReconciliationEntry $action): mixed`<br>`public function signOff(string $session, SignOffReconciliation $action): ReconciliationResource`<br>`public function summary(string $session, ReconciliationSummaryQuery $query): mixed` |

**Observed route declarations:**

[modules/accounting-bank-reconciliation-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/bank-reconciliation')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [ReconciliationController::class, 'index'])->middleware('ability:accounting.bank-reconciliation.read');
Route::post('/', [ReconciliationController::class, 'store'])->middleware('ability:accounting.bank-reconciliation.write');
Route::get('/{session}', [ReconciliationController::class, 'show'])->middleware('ability:accounting.bank-reconciliation.read');
Route::get('/{session}/summary', [ReconciliationController::class, 'summary'])->middleware('ability:accounting.bank-reconciliation.read');
Route::post('/{session}/entries', [ReconciliationController::class, 'entry'])->middleware('ability:accounting.bank-reconciliation.write');
Route::post('/{session}/entries/{entry}/confirm', [ReconciliationController::class, 'confirm'])->middleware('ability:accounting.bank-reconciliation.write');
Route::post('/{session}/sign-off', [ReconciliationController::class, 'signOff'])->middleware('ability:accounting.bank-reconciliation.write');
```
<!-- layer-implementation-plan:end -->
