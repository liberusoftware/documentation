# Ecommerce: Point of Sale Nuxt

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-ecommerce-point-of-sale-nuxt`
**Matching domain module:** `ecommerce-point-of-sale`
**Application:** Ecommerce
**Source feature:** [Point of Sale](../../features/ecommerce/point-of-sale.md)
**Architecture:** [NUXT.md](../../NUXT.md) · [API.md](../../API.md) · [Matching API module](../../api/ecommerce/point-of-sale.md) · [MODULES.md](../../MODULES.md) · [TESTING.md](../../TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `ecommerce-point-of-sale` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Registers:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Carts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Customers:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Products:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Taxes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Discounts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Tenders:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Receipts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Returns/exchanges:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Holds:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Staff actions:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-ecommerce-point-of-sale-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `registers`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `carts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `customers`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `products`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `taxes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `discounts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `tenders`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `receipts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `returns/exchanges`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `holds`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `staff-actions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `ecommerce-point-of-sale` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.
