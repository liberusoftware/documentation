# Accounting: Payroll Liabilities Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#payroll-liabilities). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-payroll-liabilities-nuxt`
**Matching domain module:** `accounting-payroll-liabilities`
**Application:** Accounting
**Source feature:** [Payroll Liabilities](../features/payroll-liabilities.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/payroll-liabilities.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-payroll-liabilities` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Agency/payee balances:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Due dates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Payments:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Allocations:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Exceptions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reconciliation:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-payroll-liabilities-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `agency-payee-balances`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `due-dates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `payments`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `allocations`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `exceptions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
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

- Package identity, public exports, API dependency, and module dependency match `accounting-payroll-liabilities` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/payroll-liabilities.md)) |
| Capability Nuxt module skeleton | [`module-accounting-payroll-liabilities-nuxt`](https://github.com/liberusoftware/module-accounting-payroll-liabilities-nuxt) (`@liberusoftware/module-accounting-payroll-liabilities-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Agency/payee balances** | Expose composable and Vue 3 component for `agency/payee balances` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/payroll-liabilities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Due dates** | Expose composable and Vue 3 component for `due dates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/payroll-liabilities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Payments** | Expose composable and Vue 3 component for `payments` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/payroll-liabilities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Allocations** | Expose composable and Vue 3 component for `allocations` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/payroll-liabilities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Exceptions** | Expose composable and Vue 3 component for `exceptions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/payroll-liabilities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Reconciliation** | Expose composable and Vue 3 component for `reconciliation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/payroll-liabilities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [PayrollLiabilitySummary.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-liabilities/src/Queries/PayrollLiabilitySummary.php) | `public function forTeam(?int $teamId = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AllocatePayrollLiability.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-liabilities/src/Actions/AllocatePayrollLiability.php) | `public function handle(PayrollLiability $liability, float $amount, string $allocationRef): PayrollLiability` |
| [RecordPayrollLiability.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-liabilities/src/Actions/RecordPayrollLiability.php) | `public function handle(array $attributes): PayrollLiability` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PayrollLiability.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-liabilities/src/Models/PayrollLiability.php) | `team_id`, `agency_ref`, `payee_ref`, `liability_ref`, `currency`, `amount`, `paid_amount`, `due_on`, `status`, `payment_ref`, `allocation_ref`, `exception_code`, `exception_message`, `reconciliation_ref`, `reconciled_at`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [PayrollLiabilitiesController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-liabilities-api/src/Http/Controllers/PayrollLiabilitiesController.php) | `public function index(Request $request): AnonymousResourceCollection`<br>`public function store(Request $request, RecordPayrollLiability $action): JsonResponse`<br>`public function show(Request $request, PayrollLiability $payrollLiability): PayrollLiabilityResource`<br>`public function allocate(Request $request, PayrollLiability $payrollLiability, AllocatePayrollLiability $action): PayrollLiabilityResource`<br>`public function summary(Request $request, PayrollLiabilitySummary $query): array` |

**Observed route declarations:**

[modules/accounting-payroll-liabilities-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-liabilities-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/payroll-liabilities')->group(function (): void {
Route::middleware('ability:accounting.payroll-liabilities.read')->group(function (): void {
Route::get('/', [PayrollLiabilitiesController::class, 'index']);
Route::get('/summary', [PayrollLiabilitiesController::class, 'summary']);
Route::get('/{payrollLiability}', [PayrollLiabilitiesController::class, 'show']);
Route::middleware('ability:accounting.payroll-liabilities.write')->group(function (): void {
Route::post('/', [PayrollLiabilitiesController::class, 'store']);
Route::post('/{payrollLiability}/allocate', [PayrollLiabilitiesController::class, 'allocate']);
```
<!-- layer-implementation-plan:end -->
