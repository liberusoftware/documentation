# Ecommerce: Promotions Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#promotions). Implementation also lives in the [application tree](../SOURCE-APPLICATION.md); preserve this documented module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-ecommerce-promotions-nuxt`
**Matching domain module:** `ecommerce-promotions`
**Application:** Ecommerce
**Source feature:** [Promotions](../features/promotions.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/promotions.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `ecommerce-promotions` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Codes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Automatic discounts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Buy-X-get-Y:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Bundles:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Free shipping/gifts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Customer/product eligibility:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Limits:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Attribution:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Fraud controls:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-ecommerce-promotions-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `codes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `automatic-discounts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `buy-x-get-y`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `bundles`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `free-shipping-gifts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `customer-product-eligibility`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `limits`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `attribution`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `fraud-controls`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `ecommerce-promotions` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-ecommerce-nuxt-vue`](https://github.com/liberusoftware/project-ecommerce-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-ecommerce-laravel-api`](https://github.com/liberusoftware/project-ecommerce-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/promotions.md)) |
| Capability Nuxt module skeleton | [`module-ecommerce-promotions-nuxt`](https://github.com/liberusoftware/module-ecommerce-promotions-nuxt) (`@liberusoftware/module-ecommerce-promotions-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Codes** | Expose composable and Vue 3 component for `codes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/promotions.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Automatic discounts** | Expose composable and Vue 3 component for `automatic discounts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/promotions.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Buy-X-get-Y** | Expose composable and Vue 3 component for `buy-x-get-y` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/promotions.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Bundles** | Expose composable and Vue 3 component for `bundles` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/promotions.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Free shipping/gifts** | Expose composable and Vue 3 component for `free shipping/gifts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/promotions.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Customer/product eligibility** | Expose composable and Vue 3 component for `customer/product eligibility` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/promotions.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Limits** | Expose composable and Vue 3 component for `limits` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/promotions.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Attribution** | Expose composable and Vue 3 component for `attribution` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/promotions.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Fraud controls** | Expose composable and Vue 3 component for `fraud controls` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/promotions.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
