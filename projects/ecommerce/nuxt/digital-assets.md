# Ecommerce: Digital Assets Nuxt

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-ecommerce-digital-assets-nuxt`
**Matching domain module:** `ecommerce-digital-assets`
**Application:** Ecommerce
**Source feature:** [Digital Assets](../features/digital-assets.md)
**Architecture:** [NUXT.md](../ECOMMERCE.md) · [API.md](../ECOMMERCE.md) · [Matching API module](../api/digital-assets.md) · [MODULES.md](../ECOMMERCE.md) · [TESTING.md](../ECOMMERCE.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `ecommerce-digital-assets` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Commerce media:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Swatches:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Documents:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Manuals:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Rights:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Ordering:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Transformations:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Videos:** page/component/composable/API-action behavior for this module's authorized workflow.
- **CMS/DAM references:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-ecommerce-digital-assets-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `commerce-media`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `swatches`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `documents`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `manuals`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `rights`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `ordering`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `transformations`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `videos`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `cms/dam-references`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `ecommerce-digital-assets` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.
