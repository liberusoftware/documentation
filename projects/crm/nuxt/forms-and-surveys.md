# CRM: Forms and Surveys Nuxt

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-forms-and-surveys-nuxt`
**Matching domain module:** `crm-forms-and-surveys`
**Application:** CRM
**Source feature:** [Forms and Surveys](../features/forms-and-surveys.md)
**Architecture:** [NUXT.md](../CRM.md) · [API.md](../CRM.md) · [Matching API module](../api/forms-and-surveys.md) · [MODULES.md](../CRM.md) · [TESTING.md](../CRM.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-forms-and-surveys` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Drag-and-drop schemas:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Conditional fields:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Progressive profiling:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Validation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Spam controls:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Consent:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Hidden attribution:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Embedding:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Submissions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Follow-up:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-forms-and-surveys-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `drag-and-drop-schemas`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `conditional-fields`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `progressive-profiling`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `validation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `spam-controls`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `consent`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `hidden-attribution`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `embedding`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `submissions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `follow-up`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-forms-and-surveys` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.
