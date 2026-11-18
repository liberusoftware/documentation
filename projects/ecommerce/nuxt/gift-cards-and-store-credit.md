# Ecommerce: Gift Cards and Store Credit Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#gift-cards-and-store-credit). Implementation also lives in the [application tree](../SOURCE-APPLICATION.md); preserve this documented module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-ecommerce-gift-cards-and-store-credit-nuxt`
**Matching domain module:** `ecommerce-gift-cards-and-store-credit`
**Application:** Ecommerce
**Source feature:** [Gift Cards and Store Credit](../features/gift-cards-and-store-credit.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/gift-cards-and-store-credit.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `ecommerce-gift-cards-and-store-credit` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Issue:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Activate:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Send:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Redeem:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Partial use:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Balances:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Expiry:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Refund:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Transfer policy:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Liabilities:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Immutable ledger:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-ecommerce-gift-cards-and-store-credit-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `issue`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `activate`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `send`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `redeem`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `partial-use`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `balances`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `expiry`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `refund`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `transfer-policy`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `liabilities`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `immutable-ledger`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `ecommerce-gift-cards-and-store-credit` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-ecommerce-nuxt-vue`](https://github.com/liberusoftware/project-ecommerce-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-ecommerce-laravel-api`](https://github.com/liberusoftware/project-ecommerce-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/gift-cards-and-store-credit.md)) |
| Capability Nuxt module skeleton | [`module-ecommerce-gift-cards-and-store-credit-nuxt`](https://github.com/liberusoftware/module-ecommerce-gift-cards-and-store-credit-nuxt) (`@liberusoftware/module-ecommerce-gift-cards-and-store-credit-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Issue** | Expose composable and Vue 3 component for `issue` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/gift-cards-and-store-credit.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Activate** | Expose composable and Vue 3 component for `activate` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/gift-cards-and-store-credit.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Send** | Expose composable and Vue 3 component for `send` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/gift-cards-and-store-credit.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Redeem** | Expose composable and Vue 3 component for `redeem` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/gift-cards-and-store-credit.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Partial use** | Expose composable and Vue 3 component for `partial use` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/gift-cards-and-store-credit.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Balances** | Expose composable and Vue 3 component for `balances` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/gift-cards-and-store-credit.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Expiry** | Expose composable and Vue 3 component for `expiry` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/gift-cards-and-store-credit.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Refund** | Expose composable and Vue 3 component for `refund` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/gift-cards-and-store-credit.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Transfer policy** | Expose composable and Vue 3 component for `transfer policy` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/gift-cards-and-store-credit.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Liabilities** | Expose composable and Vue 3 component for `liabilities` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/gift-cards-and-store-credit.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Immutable ledger** | Expose composable and Vue 3 component for `immutable ledger` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/gift-cards-and-store-credit.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
