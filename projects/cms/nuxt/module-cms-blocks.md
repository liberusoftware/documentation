# CMS: Module Cms Blocks Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-blocks). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-cms-module-cms-blocks-nuxt`
**Matching domain module:** `module-cms-blocks`
**Application:** CMS
**Source feature:** [Module Cms Blocks](../features/module-cms-blocks.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/module-cms-blocks.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `module-cms-blocks` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Typed content blocks:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Nesting rules:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Patterns:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reusable/global blocks:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Locking:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Transforms:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Previews:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Revision-safe data:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-cms-module-cms-blocks-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `typed-content-blocks`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `nesting-rules`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `patterns`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `reusable-global-blocks`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `locking`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `transforms`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `previews`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `revision-safe-data`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `module-cms-blocks` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-cms-nuxt-vue`](https://github.com/liberusoftware/project-cms-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/module-cms-blocks.md)) |
| Capability Nuxt module skeleton | [`module-cms-blocks-nuxt`](https://github.com/liberusoftware/module-cms-blocks-nuxt) (`@liberusoftware/module-cms-blocks-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Typed content blocks** | Expose composable and Vue 3 component for `typed content blocks` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-blocks.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Nesting rules** | Expose composable and Vue 3 component for `nesting rules` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-blocks.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Patterns** | Expose composable and Vue 3 component for `patterns` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-blocks.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Reusable/global blocks** | Expose composable and Vue 3 component for `reusable/global blocks` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-blocks.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Locking** | Expose composable and Vue 3 component for `locking` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-blocks.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Transforms** | Expose composable and Vue 3 component for `transforms` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-blocks.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Previews** | Expose composable and Vue 3 component for `previews` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-blocks.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Revision-safe data** | Expose composable and Vue 3 component for `revision-safe data` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-blocks.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
