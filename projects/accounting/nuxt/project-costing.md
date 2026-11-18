# Accounting: Project Costing Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#project-costing). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-project-costing-nuxt`
**Matching domain module:** `accounting-project-costing`
**Application:** Accounting
**Source feature:** [Project Costing](../features/project-costing.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/project-costing.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-project-costing` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Labor:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Expense:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Bill:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Inventory:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Subcontractor:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Overhead:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Commitments:** page/component/composable/API-action behavior for this module's authorized workflow.
- **WIP:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Cost-to-complete:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Variance:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-project-costing-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `labor`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `expense`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `bill`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `inventory`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `subcontractor`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `overhead`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `commitments`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `wip`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `cost-to-complete`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `variance`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-project-costing` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/project-costing.md)) |
| Capability Nuxt module skeleton | [`module-accounting-project-costing-nuxt`](https://github.com/liberusoftware/module-accounting-project-costing-nuxt) (`@liberusoftware/module-accounting-project-costing-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Labor** | Expose composable and Vue 3 component for `labor` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/project-costing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Expense** | Expose composable and Vue 3 component for `expense` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/project-costing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Bill** | Expose composable and Vue 3 component for `bill` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/project-costing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Inventory** | Expose composable and Vue 3 component for `inventory` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/project-costing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Subcontractor** | Expose composable and Vue 3 component for `subcontractor` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/project-costing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Overhead** | Expose composable and Vue 3 component for `overhead` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/project-costing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Commitments** | Expose composable and Vue 3 component for `commitments` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/project-costing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **WIP** | Expose composable and Vue 3 component for `wip` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/project-costing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Cost-to-complete** | Expose composable and Vue 3 component for `cost-to-complete` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/project-costing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Variance** | Expose composable and Vue 3 component for `variance` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/project-costing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ProjectCostSummary.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-costing/src/Queries/ProjectCostSummary.php) | `public function forProject(int $projectJobId, ?int $teamId = null): array`<br>`public function summarize(Collection $rows): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [RecordProjectCost.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-costing/src/Actions/RecordProjectCost.php) | `public function handle(array $attributes): ProjectCost` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ProjectCost.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-costing/src/Models/ProjectCost.php) | `team_id`, `project_job_id`, `type`, `occurred_on`, `amount`, `currency`, `committed`, `actual`, `wip_amount`, `source_ref`, `dimensions`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ProjectCostingController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-costing-api/src/Http/Controllers/ProjectCostingController.php) | `public function index(Request $request): mixed`<br>`public function store(Request $request, RecordProjectCost $action): mixed`<br>`public function show(Request $request, ProjectCost $projectCost): ProjectCost`<br>`public function summary(Request $request, int $projectJobId, ProjectCostSummary $query): array` |

**Observed route declarations:**

[modules/accounting-project-costing-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-costing-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/project-costing')->group(function (): void {
Route::middleware('ability:accounting.project-costing.read')->group(function (): void {
Route::get('/', [ProjectCostingController::class, 'index']);
Route::get('/{projectCost}', [ProjectCostingController::class, 'show']);
Route::get('/project/{projectJobId}/summary', [ProjectCostingController::class, 'summary']);
Route::middleware('ability:accounting.project-costing.write')->group(function (): void {
Route::post('/', [ProjectCostingController::class, 'store']);
```
<!-- layer-implementation-plan:end -->
