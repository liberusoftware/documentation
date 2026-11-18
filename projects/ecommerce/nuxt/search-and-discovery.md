# Ecommerce: Search and Discovery Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#search-and-discovery). Implementation also lives in the [application tree](../SOURCE-APPLICATION.md); preserve this documented module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-ecommerce-search-and-discovery-nuxt`
**Matching domain module:** `ecommerce-search-and-discovery`
**Application:** Ecommerce
**Source feature:** [Search and Discovery](../features/search-and-discovery.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/search-and-discovery.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `ecommerce-search-and-discovery` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Full-text search:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Facets:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Autocomplete:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Synonyms:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Redirects:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Ranking rules:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Typo tolerance:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Query analytics:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Provider adapters:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-ecommerce-search-and-discovery-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `full-text-search`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `facets`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `autocomplete`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `synonyms`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `redirects`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `ranking-rules`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `typo-tolerance`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `query-analytics`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
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

- Package identity, public exports, API dependency, and module dependency match `ecommerce-search-and-discovery` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-ecommerce-nuxt-vue`](https://github.com/liberusoftware/project-ecommerce-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-ecommerce-laravel-api`](https://github.com/liberusoftware/project-ecommerce-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/search-and-discovery.md)) |
| Capability Nuxt module skeleton | [`module-ecommerce-search-and-discovery-nuxt`](https://github.com/liberusoftware/module-ecommerce-search-and-discovery-nuxt) (`@liberusoftware/module-ecommerce-search-and-discovery-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Full-text search** | Expose composable and Vue 3 component for `full-text search` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/search-and-discovery.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Facets** | Expose composable and Vue 3 component for `facets` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/search-and-discovery.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Autocomplete** | Expose composable and Vue 3 component for `autocomplete` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/search-and-discovery.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Synonyms** | Expose composable and Vue 3 component for `synonyms` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/search-and-discovery.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Redirects** | Expose composable and Vue 3 component for `redirects` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/search-and-discovery.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Ranking rules** | Expose composable and Vue 3 component for `ranking rules` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/search-and-discovery.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Typo tolerance** | Expose composable and Vue 3 component for `typo tolerance` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/search-and-discovery.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Query analytics** | Expose composable and Vue 3 component for `query analytics` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/search-and-discovery.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Provider adapters** | Expose composable and Vue 3 component for `provider adapters` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/search-and-discovery.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
