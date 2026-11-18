# Accounting: Accounting Dashboards Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-dashboards). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-accounting-dashboards-nuxt`
**Matching domain module:** `accounting-dashboards`
**Application:** Accounting
**Source feature:** [Accounting Dashboards](../features/accounting-dashboards.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-dashboards.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-dashboards` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Role-specific KPIs:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Widgets:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Periods:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Dimensions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Targets:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Drill-through:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Refresh status:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Sharing:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-accounting-dashboards-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `role-specific-kpis`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `widgets`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `periods`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `dimensions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `targets`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `drill-through`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `refresh-status`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `sharing`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-dashboards` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-dashboards.md)) |
| Capability Nuxt module skeleton | [`module-accounting-dashboards-nuxt`](https://github.com/liberusoftware/module-accounting-dashboards-nuxt) (`@liberusoftware/module-accounting-dashboards-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Role-specific KPIs** | Expose composable and Vue 3 component for `role-specific kpis` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-dashboards.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Widgets** | Expose composable and Vue 3 component for `widgets` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-dashboards.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Periods** | Expose composable and Vue 3 component for `periods` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-dashboards.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Dimensions** | Expose composable and Vue 3 component for `dimensions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-dashboards.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Targets** | Expose composable and Vue 3 component for `targets` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-dashboards.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Drill-through** | Expose composable and Vue 3 component for `drill-through` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-dashboards.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Refresh status** | Expose composable and Vue 3 component for `refresh status` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-dashboards.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Sharing** | Expose composable and Vue 3 component for `sharing` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-dashboards.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [DashboardQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dashboards/src/Queries/DashboardQuery.php) | `public function forTeam(int $teamId): Collection`<br>`public function findForTeam(int $teamId, int\|string $id): Dashboard` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateDashboard.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dashboards/src/Actions/CreateDashboard.php) | `public function handle(array $attributes): Dashboard` |
| [ShareDashboard.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dashboards/src/Actions/ShareDashboard.php) | `public function handle(Dashboard $dashboard, array $attributes): DashboardShare` |
| [UpsertKpi.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dashboards/src/Actions/UpsertKpi.php) | `public function handle(Dashboard $dashboard, array $attributes): DashboardKpi` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Dashboard.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dashboards/src/Models/Dashboard.php) | `team_id`, `dashboard_ref`, `name`, `role`, `period`, `dimensions`, `metadata` |
| [DashboardKpi.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dashboards/src/Models/DashboardKpi.php) | `dashboard_id`, `team_id`, `kpi_ref`, `label`, `value`, `target`, `unit`, `refreshed_at`, `drill_through` |
| [DashboardShare.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dashboards/src/Models/DashboardShare.php) | `dashboard_id`, `team_id`, `shared_with_user_id`, `shared_with_role`, `token`, `expires_at` |

| Observed API controller | Handler signatures |
| --- | --- |
| [DashboardsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dashboards-api/src/Http/Controllers/DashboardsController.php) | `public function index(DashboardQuery $query): JsonResponse`<br>`public function store(Request $request, CreateDashboard $action): JsonResponse`<br>`public function kpi(Request $request, string $dashboard, UpsertKpi $action): JsonResponse`<br>`public function share(Request $request, string $dashboard, ShareDashboard $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-dashboards-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-dashboards-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/dashboards')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.dashboards.read')->get('/', [DashboardsController::class, 'index']);
Route::middleware('ability:accounting.dashboards.write')->group(function (): void {
Route::post('/', [DashboardsController::class, 'store']);
Route::post('/{dashboard}/kpis', [DashboardsController::class, 'kpi']);
Route::post('/{dashboard}/shares', [DashboardsController::class, 'share']);
```
<!-- layer-implementation-plan:end -->
