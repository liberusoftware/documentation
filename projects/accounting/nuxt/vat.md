# Accounting: VAT Nuxt

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-vat-nuxt`
**Matching domain module:** `accounting-vat`
**Application:** Accounting
**Source feature:** [VAT](../features/vat.md)
**Architecture:** [NUXT.md](../ACCOUNTING.md) · [API.md](../ACCOUNTING.md) · [Matching API module](../api/vat.md) · [MODULES.md](../ACCOUNTING.md) · [TESTING.md](../ACCOUNTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-vat` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Input/output VAT:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reverse charge:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Partial exemption hooks:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Import/export:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Schemes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Boxes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Adjustments:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Digital records:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Audit trail:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-vat-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `input/output-vat`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `reverse-charge`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `partial-exemption-hooks`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `import/export`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `schemes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `boxes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `adjustments`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `digital-records`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `audit-trail`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-vat` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.
