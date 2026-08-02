# CRM: Templates and Snapshots Nuxt

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-templates-and-snapshots-nuxt`
**Matching domain module:** `crm-templates-and-snapshots`
**Application:** CRM
**Source feature:** [Templates and Snapshots](../features/templates-and-snapshots.md)
**Architecture:** [NUXT.md](../CRM.md) · [API.md](../CRM.md) · [Matching API module](../api/templates-and-snapshots.md) · [MODULES.md](../CRM.md) · [TESTING.md](../CRM.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-templates-and-snapshots` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Versioned bundles of fields:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Pipelines:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Workflows:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Forms:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Funnels:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Calendars:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Templates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Dashboards:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Settings with preview:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Protected sharing:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Install:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Update:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Rollback:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-templates-and-snapshots-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `versioned-bundles-of-fields`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `pipelines`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `workflows`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `forms`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `funnels`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `calendars`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `templates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `dashboards`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `settings-with-preview`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `protected-sharing`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `install`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `update`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `rollback`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-templates-and-snapshots` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.
