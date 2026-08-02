# Ecommerce: Rentals Nuxt

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-ecommerce-rentals-nuxt`
**Matching domain module:** `ecommerce-rentals`
**Application:** Ecommerce
**Source feature:** [Rentals](../features/rentals.md)
**Architecture:** [NUXT.md](../ECOMMERCE.md) · [API.md](../ECOMMERCE.md) · [Matching API module](../api/rentals.md) · [MODULES.md](../ECOMMERCE.md) · [TESTING.md](../ECOMMERCE.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `ecommerce-rentals` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Inventory units:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Availability:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reservation periods:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Deposits:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Pickup/return:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Late/damage charges:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Inspection:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Maintenance blocks:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-ecommerce-rentals-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `inventory-units`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `availability`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `reservation-periods`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `deposits`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `pickup/return`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `late/damage-charges`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `inspection`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `maintenance-blocks`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `ecommerce-rentals` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.
