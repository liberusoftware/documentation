# Accounting: Projects and Jobs Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#projects-and-jobs). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-projects-and-jobs-nuxt`
**Matching domain module:** `accounting-projects-and-jobs`
**Application:** Accounting
**Source feature:** [Projects and Jobs](../features/projects-and-jobs.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/projects-and-jobs.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-projects-and-jobs` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Customers:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Project/job hierarchy:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Status:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Dates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Managers:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Budgets:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Dimensions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Source links:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Lifecycle:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-projects-and-jobs-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `customers`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `project-job-hierarchy`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `status`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `dates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `managers`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `budgets`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `dimensions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `source-links`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `lifecycle`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-projects-and-jobs` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/projects-and-jobs.md)) |
| Capability Nuxt module skeleton | [`module-accounting-projects-and-jobs-nuxt`](https://github.com/liberusoftware/module-accounting-projects-and-jobs-nuxt) (`@liberusoftware/module-accounting-projects-and-jobs-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Customers** | Expose composable and Vue 3 component for `customers` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/projects-and-jobs.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Project/job hierarchy** | Expose composable and Vue 3 component for `project/job hierarchy` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/projects-and-jobs.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Status** | Expose composable and Vue 3 component for `status` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/projects-and-jobs.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Dates** | Expose composable and Vue 3 component for `dates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/projects-and-jobs.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Managers** | Expose composable and Vue 3 component for `managers` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/projects-and-jobs.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Budgets** | Expose composable and Vue 3 component for `budgets` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/projects-and-jobs.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Dimensions** | Expose composable and Vue 3 component for `dimensions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/projects-and-jobs.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Source links** | Expose composable and Vue 3 component for `source links` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/projects-and-jobs.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Lifecycle** | Expose composable and Vue 3 component for `lifecycle` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/projects-and-jobs.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateProjectJob.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-projects-and-jobs/src/Actions/CreateProjectJob.php) | `public function handle(array $attributes): ProjectJob` |
| [TransitionProject.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-projects-and-jobs/src/Actions/TransitionProject.php) | `public function handle(ProjectJob $project, ProjectStatus $status): ProjectJob` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ProjectCustomer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-projects-and-jobs/src/Models/ProjectCustomer.php) | `team_id`, `customer_ref`, `name`, `status`, `metadata` |
| [ProjectJob.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-projects-and-jobs/src/Models/ProjectJob.php) | `team_id`, `customer_id`, `parent_id`, `name`, `code`, `description`, `start_date`, `end_date`, `status`, `manager_ref`, `budget_amount`, `budget_currency`, `dimensions`, `source_links`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ProjectsAndJobsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-projects-and-jobs-api/src/Http/Controllers/ProjectsAndJobsController.php) | `public function index(Request $request): mixed`<br>`public function store(Request $request, CreateProjectJob $action): mixed`<br>`public function show(Request $request, ProjectJob $project): ProjectJob`<br>`public function transition(Request $request, ProjectJob $project, TransitionProject $action): ProjectJob` |

**Observed route declarations:**

[modules/accounting-projects-and-jobs-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-projects-and-jobs-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/projects-and-jobs')->group(function (): void {
Route::middleware('ability:accounting.projects-and-jobs.read')->group(function (): void {
Route::get('/', [ProjectsAndJobsController::class, 'index']);
Route::get('/{project}', [ProjectsAndJobsController::class, 'show']);
Route::middleware('ability:accounting.projects-and-jobs.write')->group(function (): void {
Route::post('/', [ProjectsAndJobsController::class, 'store']);
Route::post('/{project}/transition', [ProjectsAndJobsController::class, 'transition']);
```
<!-- layer-implementation-plan:end -->
