# CMS: Module Cms Content Intelligence Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-content-intelligence). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-cms-module-cms-content-intelligence-nuxt`
**Matching domain module:** `module-cms-content-intelligence`
**Application:** CMS
**Source feature:** [Module Cms Content Intelligence](../features/module-cms-content-intelligence.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/module-cms-content-intelligence.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `module-cms-content-intelligence` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Inventory:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Quality:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Readability:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Accessibility:** page/component/composable/API-action behavior for this module's authorized workflow.
- **SEO:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Freshness:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Duplication:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Gaps:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Performance:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Improvement queues:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-cms-module-cms-content-intelligence-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `inventory`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `quality`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `readability`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `accessibility`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `seo`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `freshness`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `duplication`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `gaps`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `performance`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `improvement-queues`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `module-cms-content-intelligence` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-cms-nuxt-vue`](https://github.com/liberusoftware/project-cms-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/module-cms-content-intelligence.md)) |
| Capability Nuxt module skeleton | [`module-cms-content-intelligence-nuxt`](https://github.com/liberusoftware/module-cms-content-intelligence-nuxt) (`@liberusoftware/module-cms-content-intelligence-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Inventory** | Expose composable and Vue 3 component for `inventory` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-content-intelligence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Quality** | Expose composable and Vue 3 component for `quality` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-content-intelligence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Readability** | Expose composable and Vue 3 component for `readability` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-content-intelligence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Accessibility** | Expose composable and Vue 3 component for `accessibility` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-content-intelligence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **SEO** | Expose composable and Vue 3 component for `seo` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-content-intelligence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Freshness** | Expose composable and Vue 3 component for `freshness` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-content-intelligence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Duplication** | Expose composable and Vue 3 component for `duplication` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-content-intelligence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Gaps** | Expose composable and Vue 3 component for `gaps` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-content-intelligence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Performance** | Expose composable and Vue 3 component for `performance` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-content-intelligence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Improvement queues** | Expose composable and Vue 3 component for `improvement queues` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-content-intelligence.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ContentIntelligenceService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-intelligence/src/Services/ContentIntelligenceService.php) | `public function insights(?int $teamId, ?string $metric = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function analyze(array $data, ?int $teamId = null): ContentInsight`<br>`public function review(ContentInsight $insight, string $status): ContentInsight` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ContentInsight.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-intelligence/src/Models/ContentInsight.php) | `team_id`, `subject_type`, `subject_key`, `metric`, `score`, `severity`, `summary`, `rationale`, `context`, `status`, `reviewed_at` |
<!-- layer-implementation-plan:end -->
