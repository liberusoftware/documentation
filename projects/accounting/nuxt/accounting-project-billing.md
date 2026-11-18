# Accounting: Accounting Project Billing Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-project-billing). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-accounting-project-billing-nuxt`
**Matching domain module:** `accounting-project-billing`
**Application:** Accounting
**Source feature:** [Accounting Project Billing](../features/accounting-project-billing.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-project-billing.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-project-billing` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Fixed fee:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Time/material:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Milestone:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Progress:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Retainer:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Billable time/expense:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Write-up/down:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Invoice handoff:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-accounting-project-billing-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `fixed-fee`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `time-material`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `milestone`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `progress`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `retainer`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `billable-time-expense`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `write-up-down`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `invoice-handoff`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-project-billing` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-project-billing.md)) |
| Capability Nuxt module skeleton | [`module-accounting-project-billing-nuxt`](https://github.com/liberusoftware/module-accounting-project-billing-nuxt) (`@liberusoftware/module-accounting-project-billing-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Fixed fee** | Expose composable and Vue 3 component for `fixed fee` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-project-billing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Time/material** | Expose composable and Vue 3 component for `time/material` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-project-billing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Milestone** | Expose composable and Vue 3 component for `milestone` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-project-billing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Progress** | Expose composable and Vue 3 component for `progress` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-project-billing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Retainer** | Expose composable and Vue 3 component for `retainer` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-project-billing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Billable time/expense** | Expose composable and Vue 3 component for `billable time/expense` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-project-billing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Write-up/down** | Expose composable and Vue 3 component for `write-up/down` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-project-billing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Invoice handoff** | Expose composable and Vue 3 component for `invoice handoff` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-project-billing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ProjectBillingSummary.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-billing/src/Queries/ProjectBillingSummary.php) | `public function forProject(int $projectJobId, ?int $teamId = null): array`<br>`public function summarize(Collection $rows): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [HandoffProjectBilling.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-billing/src/Actions/HandoffProjectBilling.php) | `public function handle(ProjectBilling $billing, ?string $invoiceRef = null): ProjectBilling` |
| [RecordProjectBilling.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-billing/src/Actions/RecordProjectBilling.php) | `public function handle(array $attributes): ProjectBilling` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ProjectBilling.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-billing/src/Models/ProjectBilling.php) | `team_id`, `project_job_id`, `method`, `status`, `period_start`, `period_end`, `currency`, `quantity`, `rate`, `amount`, `progress_percent`, `billable_time_amount`, `billable_expense_amount`, `retainer_amount`, `write_up_down_amount`, `source_ref`, `invoice_ref`, `metadata` |
| [Project.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-billing-api/src/Models/Project.php) | `name`, `code`, `description`, `start_date`, `end_date`, `status`, `allocation_percentage` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ProjectBillingController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-billing-api/src/Http/Controllers/ProjectBillingController.php) | `public function index(Request $request): mixed`<br>`public function store(Request $request, RecordProjectBilling $action): mixed`<br>`public function show(Request $request, ProjectBilling $projectBilling): ProjectBilling`<br>`public function handoff(Request $request, ProjectBilling $projectBilling, HandoffProjectBilling $action): ProjectBilling`<br>`public function summary(Request $request, int $projectJobId, ProjectBillingSummary $query): array` |

**Observed route declarations:**

[modules/accounting-project-billing-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-billing-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/project-billing')->group(function (): void {
Route::middleware('ability:accounting.project-billing.read')->group(function (): void {
Route::get('/', [ProjectBillingController::class, 'index']);
Route::get('/{projectBilling}', [ProjectBillingController::class, 'show']);
Route::get('/project/{projectJobId}/summary', [ProjectBillingController::class, 'summary']);
Route::middleware('ability:accounting.project-billing.write')->group(function (): void {
Route::post('/', [ProjectBillingController::class, 'store']);
Route::post('/{projectBilling}/handoff', [ProjectBillingController::class, 'handoff']);
```
<!-- layer-implementation-plan:end -->
