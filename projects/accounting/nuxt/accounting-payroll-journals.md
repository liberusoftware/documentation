# Accounting: Accounting Payroll Journals Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-payroll-journals). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-accounting-payroll-journals-nuxt`
**Matching domain module:** `accounting-payroll-journals`
**Application:** Accounting
**Source feature:** [Accounting Payroll Journals](../features/accounting-payroll-journals.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-payroll-journals.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-payroll-journals` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Gross pay:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Taxes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Deductions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Benefits:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Employer costs:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Net pay:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Liabilities:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Allocation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Posting:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reversal:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Corrections:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-accounting-payroll-journals-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `gross-pay`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `taxes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `deductions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `benefits`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `employer-costs`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `net-pay`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `liabilities`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `allocation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `posting`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `reversal`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `corrections`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-payroll-journals` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-payroll-journals.md)) |
| Capability Nuxt module skeleton | [`module-accounting-payroll-journals-nuxt`](https://github.com/liberusoftware/module-accounting-payroll-journals-nuxt) (`@liberusoftware/module-accounting-payroll-journals-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Gross pay** | Expose composable and Vue 3 component for `gross pay` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-payroll-journals.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Taxes** | Expose composable and Vue 3 component for `taxes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-payroll-journals.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Deductions** | Expose composable and Vue 3 component for `deductions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-payroll-journals.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Benefits** | Expose composable and Vue 3 component for `benefits` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-payroll-journals.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Employer costs** | Expose composable and Vue 3 component for `employer costs` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-payroll-journals.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Net pay** | Expose composable and Vue 3 component for `net pay` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-payroll-journals.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Liabilities** | Expose composable and Vue 3 component for `liabilities` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-payroll-journals.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Allocation** | Expose composable and Vue 3 component for `allocation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-payroll-journals.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Posting** | Expose composable and Vue 3 component for `posting` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-payroll-journals.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Reversal** | Expose composable and Vue 3 component for `reversal` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-payroll-journals.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Corrections** | Expose composable and Vue 3 component for `corrections` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-payroll-journals.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [PayrollJournalSummary.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-journals/src/Queries/PayrollJournalSummary.php) | `public function forTeam(?int $teamId = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreatePayrollJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-journals/src/Actions/CreatePayrollJournal.php) | `public function handle(array $attributes): PayrollJournal` |
| [PostPayrollJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-journals/src/Actions/PostPayrollJournal.php) | `public function handle(PayrollJournal $journal): PayrollJournal` |
| [ReversePayrollJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-journals/src/Actions/ReversePayrollJournal.php) | `public function handle(PayrollJournal $journal, string $reversalRef): PayrollJournal` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PayrollJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-journals/src/Models/PayrollJournal.php) | `team_id`, `journal_ref`, `payroll_period_start`, `payroll_period_end`, `currency`, `gross_pay`, `taxes`, `deductions`, `benefits`, `employer_costs`, `net_pay`, `liabilities`, `allocation`, `status`, `posted_at`, `reversed_at`, `reversal_ref`, `correction_ref`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [PayrollJournalsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-journals-api/src/Http/Controllers/PayrollJournalsController.php) | `public function index(Request $request): AnonymousResourceCollection`<br>`public function store(Request $request, CreatePayrollJournal $action): JsonResponse`<br>`public function show(Request $request, PayrollJournal $payrollJournal): PayrollJournalResource`<br>`public function post(Request $request, PayrollJournal $payrollJournal, PostPayrollJournal $action): PayrollJournalResource`<br>`public function reverse(Request $request, PayrollJournal $payrollJournal, ReversePayrollJournal $action): PayrollJournalResource`<br>`public function summary(Request $request, PayrollJournalSummary $query): array` |

**Observed route declarations:**

[modules/accounting-payroll-journals-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-journals-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/payroll-journals')->group(function (): void {
Route::middleware('ability:accounting.payroll-journals.read')->group(function (): void {
Route::get('/', [PayrollJournalsController::class, 'index']);
Route::get('/summary', [PayrollJournalsController::class, 'summary']);
Route::get('/{payrollJournal}', [PayrollJournalsController::class, 'show']);
Route::middleware('ability:accounting.payroll-journals.write')->group(function (): void {
Route::post('/', [PayrollJournalsController::class, 'store']);
Route::post('/{payrollJournal}/post', [PayrollJournalsController::class, 'post']);
Route::post('/{payrollJournal}/reverse', [PayrollJournalsController::class, 'reverse']);
```
<!-- layer-implementation-plan:end -->
