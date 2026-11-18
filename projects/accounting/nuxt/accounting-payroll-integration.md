# Accounting: Accounting Payroll Integration Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-payroll-integration). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-accounting-payroll-integration-nuxt`
**Matching domain module:** `accounting-payroll-integration`
**Application:** Accounting
**Source feature:** [Accounting Payroll Integration](../features/accounting-payroll-integration.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-payroll-integration.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-payroll-integration` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Provider/period/run identity:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Employee/contractor references:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Import validation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Dimensions/projects:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Provider adapters:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-accounting-payroll-integration-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `provider-period-run-identity`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `employee-contractor-references`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `import-validation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `dimensions-projects`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `provider-adapters`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-payroll-integration` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-payroll-integration.md)) |
| Capability Nuxt module skeleton | [`module-accounting-payroll-integration-nuxt`](https://github.com/liberusoftware/module-accounting-payroll-integration-nuxt) (`@liberusoftware/module-accounting-payroll-integration-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Provider/period/run identity** | Expose composable and Vue 3 component for `provider/period/run identity` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-payroll-integration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Employee/contractor references** | Expose composable and Vue 3 component for `employee/contractor references` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-payroll-integration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Import validation** | Expose composable and Vue 3 component for `import validation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-payroll-integration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Dimensions/projects** | Expose composable and Vue 3 component for `dimensions/projects` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-payroll-integration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Provider adapters** | Expose composable and Vue 3 component for `provider adapters` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-payroll-integration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [PayrollImportSummary.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-integration/src/Queries/PayrollImportSummary.php) | `public function forTeam(?int $teamId = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ImportPayrollRun.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-integration/src/Actions/ImportPayrollRun.php) | `public function handle(array $attributes): PayrollImport` |
| [MarkPayrollImport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-integration/src/Actions/MarkPayrollImport.php) | `public function handle(PayrollImport $import, ImportStatus $status): PayrollImport` |
| [PayrollProviderAdapter.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-integration/src/Contracts/PayrollProviderAdapter.php) | `public function validateImport(array $payload): array`<br>`public function import(array $payload): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PayrollImport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-integration/src/Models/PayrollImport.php) | `team_id`, `provider`, `period_start`, `period_end`, `run_ref`, `currency`, `employee_refs`, `contractor_refs`, `dimensions`, `project_refs`, `payload_hash`, `validation_errors`, `adapter_ref`, `status`, `imported_at`, `reconciled_at`, `metadata` |
| [Payroll.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-integration-api/src/Models/Payroll.php) | `employee_id`, `base_salary`, `overtime_hours`, `overtime_rate`, `tax_deductions`, `other_deductions`, `net_salary`, `pay_period_start`, `pay_period_end`, `payment_date`, `payment_status` |

| Observed API controller | Handler signatures |
| --- | --- |
| [PayrollIntegrationController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-integration-api/src/Http/Controllers/PayrollIntegrationController.php) | `public function index(Request $request): AnonymousResourceCollection`<br>`public function store(Request $request, ImportPayrollRun $action): JsonResponse`<br>`public function show(Request $request, PayrollImport $payrollImport): PayrollImportResource`<br>`public function status(Request $request, PayrollImport $payrollImport, MarkPayrollImport $action): PayrollImportResource`<br>`public function summary(Request $request, PayrollImportSummary $query): array` |

**Observed route declarations:**

[modules/accounting-payroll-integration-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-integration-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/payroll-integration')->group(function (): void {
Route::middleware('ability:accounting.payroll-integration.read')->group(function (): void {
Route::get('/', [PayrollIntegrationController::class, 'index']);
Route::get('/summary', [PayrollIntegrationController::class, 'summary']);
Route::get('/{payrollImport}', [PayrollIntegrationController::class, 'show']);
Route::middleware('ability:accounting.payroll-integration.write')->group(function (): void {
Route::post('/', [PayrollIntegrationController::class, 'store']);
Route::post('/{payrollImport}/status', [PayrollIntegrationController::class, 'status']);
```
<!-- layer-implementation-plan:end -->
