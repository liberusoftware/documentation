# Accounting: Debt and Loans Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#debt-and-loans). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-debt-and-loans-nuxt`
**Matching domain module:** `accounting-debt-and-loans`
**Application:** Accounting
**Source feature:** [Debt and Loans](../features/debt-and-loans.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/debt-and-loans.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-debt-and-loans` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Facilities:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Drawdowns:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Repayments:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Interest/fees:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Schedules:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Covenants:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Current/non-current split:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reconciliation:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-debt-and-loans-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `facilities`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `drawdowns`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `repayments`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `interest-fees`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `schedules`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `covenants`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `current-non-current-split`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
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

- Package identity, public exports, API dependency, and module dependency match `accounting-debt-and-loans` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/debt-and-loans.md)) |
| Capability Nuxt module skeleton | [`module-accounting-debt-and-loans-nuxt`](https://github.com/liberusoftware/module-accounting-debt-and-loans-nuxt) (`@liberusoftware/module-accounting-debt-and-loans-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Facilities** | Expose composable and Vue 3 component for `facilities` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/debt-and-loans.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Drawdowns** | Expose composable and Vue 3 component for `drawdowns` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/debt-and-loans.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Repayments** | Expose composable and Vue 3 component for `repayments` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/debt-and-loans.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Interest/fees** | Expose composable and Vue 3 component for `interest/fees` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/debt-and-loans.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Schedules** | Expose composable and Vue 3 component for `schedules` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/debt-and-loans.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Covenants** | Expose composable and Vue 3 component for `covenants` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/debt-and-loans.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Current/non-current split** | Expose composable and Vue 3 component for `current/non-current split` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/debt-and-loans.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Reconciliation** | Expose composable and Vue 3 component for `reconciliation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/debt-and-loans.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [DebtQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Queries/DebtQuery.php) | `public function facilities(int $teamId): Collection`<br>`public function position(int $teamId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateDebtFacility.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Actions/CreateDebtFacility.php) | `public function handle(array $attributes): DebtFacility` |
| [ReconcileDebtMovement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Actions/ReconcileDebtMovement.php) | `public function handle(DebtMovement $movement, string $journalReference): DebtMovement` |
| [RecordDebtMovement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Actions/RecordDebtMovement.php) | `public function handle(DebtFacility $facility, string\|DebtMovementKind $kind, array $attributes): DebtMovement` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DebtCovenant.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Models/DebtCovenant.php) | `facility_id`, `team_id`, `covenant_ref`, `metric`, `threshold`, `operator`, `last_value`, `status`, `metadata` |
| [DebtFacility.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Models/DebtFacility.php) | `team_id`, `facility_ref`, `lender_ref`, `currency`, `limit_amount`, `drawn_amount`, `interest_rate`, `start_date`, `maturity_date`, `status`, `metadata` |
| [DebtMovement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Models/DebtMovement.php) | `facility_id`, `team_id`, `kind`, `principal_amount`, `interest_amount`, `fee_amount`, `movement_date`, `due_date`, `status`, `journal_ref`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [DebtAndLoansController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans-api/src/Http/Controllers/DebtAndLoansController.php) | `public function index(Request $request): JsonResponse`<br>`public function position(DebtQuery $query): JsonResponse`<br>`public function store(Request $request, CreateDebtFacility $action): JsonResponse`<br>`public function movement(Request $request, string $facility, RecordDebtMovement $action): JsonResponse`<br>`public function reconcile(Request $request, string $movement, ReconcileDebtMovement $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-debt-and-loans-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/debt-and-loans')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.debt-and-loans.read')->group(function (): void {
Route::get('/facilities', [DebtAndLoansController::class, 'index']);
Route::get('/position', [DebtAndLoansController::class, 'position']);
Route::middleware('ability:accounting.debt-and-loans.write')->group(function (): void {
Route::post('/facilities', [DebtAndLoansController::class, 'store']);
Route::post('/facilities/{facility}/movements', [DebtAndLoansController::class, 'movement']);
Route::post('/movements/{movement}/reconcile', [DebtAndLoansController::class, 'reconcile']);
```
<!-- layer-implementation-plan:end -->
