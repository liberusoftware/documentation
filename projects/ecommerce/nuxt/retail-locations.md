# Ecommerce: Retail Locations Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#retail-locations). Implementation also lives in the [application tree](../SOURCE-APPLICATION.md); preserve this documented module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-ecommerce-retail-locations-nuxt`
**Matching domain module:** `ecommerce-retail-locations`
**Application:** Ecommerce
**Source feature:** [Retail Locations](../features/retail-locations.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/retail-locations.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `ecommerce-retail-locations` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Store hierarchy:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Hours:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Market:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Stock source:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Pickup:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Registers:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Staff assignments:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Fulfillment:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Location reporting:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-ecommerce-retail-locations-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `store-hierarchy`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `hours`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `market`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `stock-source`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `pickup`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `registers`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `staff-assignments`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `fulfillment`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `location-reporting`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `ecommerce-retail-locations` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-ecommerce-nuxt-vue`](https://github.com/liberusoftware/project-ecommerce-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-ecommerce-laravel-api`](https://github.com/liberusoftware/project-ecommerce-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/retail-locations.md)) |
| Capability Nuxt module skeleton | [`module-ecommerce-retail-locations-nuxt`](https://github.com/liberusoftware/module-ecommerce-retail-locations-nuxt) (`@liberusoftware/module-ecommerce-retail-locations-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Store hierarchy** | Expose composable and Vue 3 component for `store hierarchy` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/retail-locations.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Hours** | Expose composable and Vue 3 component for `hours` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/retail-locations.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Market** | Expose composable and Vue 3 component for `market` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/retail-locations.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Stock source** | Expose composable and Vue 3 component for `stock source` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/retail-locations.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Pickup** | Expose composable and Vue 3 component for `pickup` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/retail-locations.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Registers** | Expose composable and Vue 3 component for `registers` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/retail-locations.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Staff assignments** | Expose composable and Vue 3 component for `staff assignments` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/retail-locations.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Fulfillment** | Expose composable and Vue 3 component for `fulfillment` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/retail-locations.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Location reporting** | Expose composable and Vue 3 component for `location reporting` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/retail-locations.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
