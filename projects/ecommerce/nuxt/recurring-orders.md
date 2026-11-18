# Ecommerce: Recurring Orders Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#recurring-orders). Implementation also lives in the [application tree](../SOURCE-APPLICATION.md); preserve this documented module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-ecommerce-recurring-orders-nuxt`
**Matching domain module:** `ecommerce-recurring-orders`
**Application:** Ecommerce
**Source feature:** [Recurring Orders](../features/recurring-orders.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/recurring-orders.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `ecommerce-recurring-orders` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Repeat schedules:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Editable upcoming orders:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Cutoff:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Skips:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Substitutions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Payment references:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Fulfillment generation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Failures:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-ecommerce-recurring-orders-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `repeat-schedules`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `editable-upcoming-orders`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `cutoff`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `skips`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `substitutions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `payment-references`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `fulfillment-generation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `failures`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `ecommerce-recurring-orders` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-ecommerce-nuxt-vue`](https://github.com/liberusoftware/project-ecommerce-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-ecommerce-laravel-api`](https://github.com/liberusoftware/project-ecommerce-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/recurring-orders.md)) |
| Capability Nuxt module skeleton | [`module-ecommerce-recurring-orders-nuxt`](https://github.com/liberusoftware/module-ecommerce-recurring-orders-nuxt) (`@liberusoftware/module-ecommerce-recurring-orders-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Repeat schedules** | Expose composable and Vue 3 component for `repeat schedules` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/recurring-orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Editable upcoming orders** | Expose composable and Vue 3 component for `editable upcoming orders` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/recurring-orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Cutoff** | Expose composable and Vue 3 component for `cutoff` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/recurring-orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Skips** | Expose composable and Vue 3 component for `skips` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/recurring-orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Substitutions** | Expose composable and Vue 3 component for `substitutions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/recurring-orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Payment references** | Expose composable and Vue 3 component for `payment references` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/recurring-orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Fulfillment generation** | Expose composable and Vue 3 component for `fulfillment generation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/recurring-orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |
| **Failures** | Expose composable and Vue 3 component for `failures` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/recurring-orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-ecommerce-laravel-api`. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
