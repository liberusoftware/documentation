# Accounting: Liberu Executive Insights Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#liberu-executive-insights). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-liberu-executive-insights-nuxt`
**Matching domain module:** `liberu-executive-insights`
**Application:** Accounting
**Source feature:** [Liberu Executive Insights](../features/liberu-executive-insights.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/liberu-executive-insights.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `liberu-executive-insights` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Metric registry:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Cross-product projections:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Evidence drill-through:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Decision snapshots:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Data-quality operations:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-liberu-executive-insights-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `metric-registry`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `cross-product-projections`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `evidence-drill-through`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `decision-snapshots`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `data-quality-operations`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `liberu-executive-insights` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/liberu-executive-insights.md)) |
| Capability Nuxt module skeleton | [`module-module-liberu-executive-insights-5279400e-nuxt`](https://github.com/liberusoftware/module-module-liberu-executive-insights-5279400e-nuxt) (`@liberusoftware/module-module-liberu-executive-insights-5279400e-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Metric registry** | Expose composable and Vue 3 component for `metric registry` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/liberu-executive-insights.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Cross-product projections** | Expose composable and Vue 3 component for `cross-product projections` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/liberu-executive-insights.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Evidence drill-through** | Expose composable and Vue 3 component for `evidence drill-through` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/liberu-executive-insights.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Decision snapshots** | Expose composable and Vue 3 component for `decision snapshots` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/liberu-executive-insights.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Data-quality operations** | Expose composable and Vue 3 component for `data-quality operations` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/liberu-executive-insights.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [RegisterMetric.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/liberu-executive-insights/src/Actions/RegisterMetric.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(array $attributes): MetricDefinition` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MetricDefinition.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/liberu-executive-insights/src/Models/MetricDefinition.php) | `team_id`, `key`, `name`, `formula`, `version`, `dimensions`, `currency`, `timezone`, `freshness_seconds`, `is_active` |
<!-- layer-implementation-plan:end -->
