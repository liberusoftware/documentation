# Accounting: Business Insights Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#business-insights). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-business-insights-nuxt`
**Matching domain module:** `accounting-business-insights`
**Application:** Accounting
**Source feature:** [Business Insights](../features/business-insights.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/business-insights.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-business-insights` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Trends:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Ratios:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Working capital:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Profitability:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Cash runway:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Anomalies:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Benchmarks adapters:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Explanations:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-business-insights-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `trends`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `ratios`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `working-capital`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `profitability`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `cash-runway`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `anomalies`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `benchmarks-adapters`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `explanations`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-business-insights` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/business-insights.md)) |
| Capability Nuxt module skeleton | [`module-accounting-business-insights-nuxt`](https://github.com/liberusoftware/module-accounting-business-insights-nuxt) (`@liberusoftware/module-accounting-business-insights-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Trends** | Expose composable and Vue 3 component for `trends` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/business-insights.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Ratios** | Expose composable and Vue 3 component for `ratios` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/business-insights.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Working capital** | Expose composable and Vue 3 component for `working capital` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/business-insights.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Profitability** | Expose composable and Vue 3 component for `profitability` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/business-insights.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Cash runway** | Expose composable and Vue 3 component for `cash runway` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/business-insights.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Anomalies** | Expose composable and Vue 3 component for `anomalies` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/business-insights.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Benchmarks adapters** | Expose composable and Vue 3 component for `benchmarks adapters` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/business-insights.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Explanations** | Expose composable and Vue 3 component for `explanations` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/business-insights.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [InsightQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-business-insights/src/Queries/InsightQuery.php) | `public function paginate(int $teamId, ?string $metric = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [RecordInsight.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-business-insights/src/Actions/RecordInsight.php) | `public function handle(array $attributes): InsightSnapshot` |
| [BusinessInsightsPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-business-insights-api/src/Policies/BusinessInsightsPolicy.php) | `public function viewAny(?object $user): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [InsightSnapshot.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-business-insights/src/Models/InsightSnapshot.php) | `team_id`, `metric`, `period_start`, `period_end`, `value`, `comparison_value`, `unit`, `explanation`, `metadata`, `refreshed_at` |

| Observed API controller | Handler signatures |
| --- | --- |
| [BusinessInsightsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-business-insights-api/src/Http/Controllers/BusinessInsightsController.php) | `public function index(Request $request, InsightQuery $query): mixed` |

**Observed route declarations:**

[modules/accounting-business-insights-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-business-insights-api/routes/api.php)

```php
Route::get('api/v1/accounting/business-insights', [BusinessInsightsController::class, 'index'])->middleware(['auth:sanctum', 'ability:accounting.business-insights.read', 'throttle:60,1']);
```
<!-- layer-implementation-plan:end -->
