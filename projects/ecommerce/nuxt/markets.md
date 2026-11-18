# Ecommerce: Markets Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#markets). Implementation also lives in the [application tree](../SOURCE-APPLICATION.md); preserve this documented module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-ecommerce-markets-nuxt`
**Matching domain module:** `ecommerce-markets`
**Application:** Ecommerce
**Source feature:** [Markets](../features/markets.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/markets.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `ecommerce-markets` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Customer/region/channel market definitions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Domains:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Locale:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Currency:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Pricing:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Availability:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Tax/duty:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Content/theme references:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Fallback:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-ecommerce-markets-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `customer-region-channel-market-definitions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `domains`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `locale`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `currency`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `pricing`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `availability`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `tax-duty`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `content-theme-references`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `fallback`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `ecommerce-markets` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-ecommerce-nuxt-vue`](https://github.com/liberusoftware/project-ecommerce-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-ecommerce-laravel-api`](https://github.com/liberusoftware/project-ecommerce-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/markets.md)) |
| Capability Nuxt module skeleton | [`module-ecommerce-markets-nuxt`](https://github.com/liberusoftware/module-ecommerce-markets-nuxt) (`@liberusoftware/module-ecommerce-markets-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Customer/region/channel market definitions** | Expose composable and Vue 3 component for `customer/region/channel market definitions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/markets.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Domains** | Expose composable and Vue 3 component for `domains` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/markets.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Locale** | Expose composable and Vue 3 component for `locale` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/markets.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Currency** | Expose composable and Vue 3 component for `currency` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/markets.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Pricing** | Expose composable and Vue 3 component for `pricing` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/markets.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Availability** | Expose composable and Vue 3 component for `availability` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/markets.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Tax/duty** | Expose composable and Vue 3 component for `tax/duty` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/markets.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Content/theme references** | Expose composable and Vue 3 component for `content/theme references` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/markets.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Fallback** | Expose composable and Vue 3 component for `fallback` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/markets.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
