# Accounting: Project Profitability Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#project-profitability). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-project-profitability-nuxt`
**Matching domain module:** `accounting-project-profitability`
**Application:** Accounting
**Source feature:** [Project Profitability](../features/project-profitability.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/project-profitability.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-project-profitability` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Revenue:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Cost:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Margin:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Estimates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Committed/actual:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Unbilled WIP:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Realization:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Dashboards:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Drill-through:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-project-profitability-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `revenue`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `cost`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `margin`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `estimates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `committed-actual`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `unbilled-wip`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `realization`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `dashboards`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
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

- Package identity, public exports, API dependency, and module dependency match `accounting-project-profitability` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/project-profitability.md)) |
| Capability Nuxt module skeleton | [`module-accounting-project-profitability-nuxt`](https://github.com/liberusoftware/module-accounting-project-profitability-nuxt) (`@liberusoftware/module-accounting-project-profitability-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Revenue** | Expose composable and Vue 3 component for `revenue` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/project-profitability.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Cost** | Expose composable and Vue 3 component for `cost` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/project-profitability.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Margin** | Expose composable and Vue 3 component for `margin` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/project-profitability.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Estimates** | Expose composable and Vue 3 component for `estimates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/project-profitability.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Committed/actual** | Expose composable and Vue 3 component for `committed/actual` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/project-profitability.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Unbilled WIP** | Expose composable and Vue 3 component for `unbilled wip` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/project-profitability.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Realization** | Expose composable and Vue 3 component for `realization` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/project-profitability.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Dashboards** | Expose composable and Vue 3 component for `dashboards` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/project-profitability.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Drill-through** | Expose composable and Vue 3 component for `drill-through` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/project-profitability.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ProjectProfitabilityDashboard.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-profitability/src/Queries/ProjectProfitabilityDashboard.php) | `public function forProject(int $projectJobId, ?int $teamId = null): array`<br>`public function summarize(Collection $rows): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [FinalizeProjectProfitability.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-profitability/src/Actions/FinalizeProjectProfitability.php) | `public function handle(ProjectProfitability $record): ProjectProfitability` |
| [RecordProjectProfitability.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-profitability/src/Actions/RecordProjectProfitability.php) | `public function handle(array $attributes): ProjectProfitability` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ProjectProfitability.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-profitability/src/Models/ProjectProfitability.php) | `team_id`, `project_job_id`, `period_start`, `period_end`, `currency`, `revenue_amount`, `cost_amount`, `estimate_amount`, `committed_amount`, `actual_amount`, `unbilled_wip_amount`, `billed_amount`, `status`, `dimensions`, `source_links`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ProjectProfitabilityController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-profitability-api/src/Http/Controllers/ProjectProfitabilityController.php) | `public function index(Request $request): mixed`<br>`public function store(Request $request, RecordProjectProfitability $action): mixed`<br>`public function show(Request $request, ProjectProfitability $projectProfitability): ProjectProfitability`<br>`public function finalize(Request $request, ProjectProfitability $projectProfitability, FinalizeProjectProfitability $action): ProjectProfitability`<br>`public function dashboard(Request $request, int $projectJobId, ProjectProfitabilityDashboard $query): array` |

**Observed route declarations:**

[modules/accounting-project-profitability-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-profitability-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/project-profitability')->group(function (): void {
Route::middleware('ability:accounting.project-profitability.read')->group(function (): void {
Route::get('/', [ProjectProfitabilityController::class, 'index']);
Route::get('/{projectProfitability}', [ProjectProfitabilityController::class, 'show']);
Route::get('/project/{projectJobId}/dashboard', [ProjectProfitabilityController::class, 'dashboard']);
Route::middleware('ability:accounting.project-profitability.write')->group(function (): void {
Route::post('/', [ProjectProfitabilityController::class, 'store']);
Route::post('/{projectProfitability}/finalize', [ProjectProfitabilityController::class, 'finalize']);
```
<!-- layer-implementation-plan:end -->
