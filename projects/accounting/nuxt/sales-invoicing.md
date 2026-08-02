# Accounting: Sales Invoicing Nuxt

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-sales-invoicing-nuxt`
**Matching domain module:** `accounting-sales-invoicing`
**Application:** Accounting
**Source feature:** [Sales Invoicing](../features/sales-invoicing.md)
**Architecture:** [NUXT.md](../ACCOUNTING.md) · [API.md](../ACCOUNTING.md) · [Matching API module](../api/sales-invoicing.md) · [MODULES.md](../ACCOUNTING.md) · [TESTING.md](../ACCOUNTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-sales-invoicing` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Draft/approved/final invoices:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Line items:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Tax:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Discounts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Deposits:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Recurring sources:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Branding:** page/component/composable/API-action behavior for this module's authorized workflow.
- **PDFs:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Delivery:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Immutability:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-sales-invoicing-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `draft/approved/final-invoices`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `line-items`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `tax`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `discounts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `deposits`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `recurring-sources`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `branding`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `pdfs`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `delivery`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `immutability`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-sales-invoicing` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.
