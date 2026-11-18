# CMS: Editorial Content Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#editorial-content). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-cms-editorial-content-nuxt`
**Matching domain module:** `cms-editorial-content`
**Application:** CMS
**Source feature:** [Editorial Content](../features/editorial-content.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/editorial-content.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `cms-editorial-content` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Posts/articles:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Authors:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Excerpts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Series:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Categories:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Tags:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Featured content:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Related content:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Archives:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-cms-editorial-content-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `posts-articles`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `authors`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `excerpts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `series`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `categories`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `tags`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `featured-content`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `related-content`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `archives`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `cms-editorial-content` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-cms-nuxt-vue`](https://github.com/liberusoftware/project-cms-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/editorial-content.md)) |
| Capability Nuxt module skeleton | [`module-cms-editorial-content-nuxt`](https://github.com/liberusoftware/module-cms-editorial-content-nuxt) (`@liberusoftware/module-cms-editorial-content-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Posts/articles** | Expose composable and Vue 3 component for `posts/articles` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/editorial-content.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Authors** | Expose composable and Vue 3 component for `authors` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/editorial-content.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Excerpts** | Expose composable and Vue 3 component for `excerpts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/editorial-content.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Series** | Expose composable and Vue 3 component for `series` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/editorial-content.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Categories** | Expose composable and Vue 3 component for `categories` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/editorial-content.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Tags** | Expose composable and Vue 3 component for `tags` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/editorial-content.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Featured content** | Expose composable and Vue 3 component for `featured content` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/editorial-content.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Related content** | Expose composable and Vue 3 component for `related content` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/editorial-content.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Archives** | Expose composable and Vue 3 component for `archives` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/editorial-content.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
