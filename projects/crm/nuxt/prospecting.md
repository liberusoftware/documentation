# CRM: Prospecting Nuxt

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-prospecting-nuxt`
**Matching domain module:** `crm-prospecting`
**Application:** CRM
**Source feature:** [Prospecting](../features/prospecting.md)
**Architecture:** [NUXT.md](../CRM.md) · [API.md](../CRM.md) · [Matching API module](../api/prospecting.md) · [MODULES.md](../CRM.md) · [TESTING.md](../CRM.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-prospecting` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Ideal-customer profiles:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Prospect searches:** page/component/composable/API-action behavior for this module's authorized workflow.
- **List building:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Research queues:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Contact reveal/credits:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Provider provenance:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Compliant export/outreach handoff:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-prospecting-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `ideal-customer-profiles`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `prospect-searches`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `list-building`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `research-queues`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `contact-reveal/credits`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `provider-provenance`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `compliant-export/outreach-handoff`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-prospecting` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.
