# CMS: Hook and Event SDK Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#hook-and-event-sdk). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-cms-hook-and-event-sdk-nuxt`
**Matching domain module:** `cms-hook-and-event-sdk`
**Application:** CMS
**Source feature:** [Hook and Event SDK](../features/hook-and-event-sdk.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/hook-and-event-sdk.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `cms-hook-and-event-sdk` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Stable content/editor/render/admin/CLI events:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Typed extension points:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Priorities:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Isolation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Diagnostics:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Deprecation:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-cms-hook-and-event-sdk-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `stable-content-editor-render-admin-cli-events`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `typed-extension-points`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `priorities`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `isolation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `diagnostics`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `deprecation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `cms-hook-and-event-sdk` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-cms-nuxt-vue`](https://github.com/liberusoftware/project-cms-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/hook-and-event-sdk.md)) |
| Capability Nuxt module skeleton | [`module-cms-hook-and-event-sdk-nuxt`](https://github.com/liberusoftware/module-cms-hook-and-event-sdk-nuxt) (`@liberusoftware/module-cms-hook-and-event-sdk-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Stable content/editor/render/admin/CLI events** | Expose composable and Vue 3 component for `stable content/editor/render/admin/cli events` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/hook-and-event-sdk.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Typed extension points** | Expose composable and Vue 3 component for `typed extension points` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/hook-and-event-sdk.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Priorities** | Expose composable and Vue 3 component for `priorities` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/hook-and-event-sdk.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Isolation** | Expose composable and Vue 3 component for `isolation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/hook-and-event-sdk.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Diagnostics** | Expose composable and Vue 3 component for `diagnostics` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/hook-and-event-sdk.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Deprecation** | Expose composable and Vue 3 component for `deprecation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/hook-and-event-sdk.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
