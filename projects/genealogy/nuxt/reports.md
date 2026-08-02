# Genealogy: Reports Nuxt\n\n## Canonical one-to-one Nuxt 4 implementation\n\n**Nuxt package:** `module-genealogy-reports-nuxt`\n**Matching domain module:** `genealogy-reports`\n**Application:** Genealogy\n**Source feature:** [Reports](../features/reports.md)\n**Architecture:** [NUXT.md](../GENEALOGY.md) · [API.md](../GENEALOGY.md) · [Matching API module](../api/reports.md) · [MODULES.md](../GENEALOGY.md) · [TESTING.md](../GENEALOGY.md)\n\n## 1. Purpose and ownership\n\nThis optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `genealogy-reports` public API boundary. It must not contain another module's UI or depend on application `App\` classes.\n\n## 2. Module-specific surfaces\n\n- **Family groups:** page/component/composable/API-action behavior for this module's authorized workflow.\n- **Pedigrees:** page/component/composable/API-action behavior for this module's authorized workflow.\n- **Descendants:** page/component/composable/API-action behavior for this module's authorized workflow.\n- **Timelines:** page/component/composable/API-action behavior for this module's authorized workflow.\n- **Research:** page/component/composable/API-action behavior for this module's authorized workflow.\n- **Sources:** page/component/composable/API-action behavior for this module's authorized workflow.\n- **Exportable charts:** page/component/composable/API-action behavior for this module's authorized workflow.\n\n## 3. Nuxt 4 implementation\n\n- Register a stable `module-genealogy-reports-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.\n- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.\n- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.\n- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.\n\n### Capability mapping\n\n- `family-groups`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.\n- `pedigrees`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.\n- `descendants`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.\n- `timelines`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.\n- `research`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.\n- `sources`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.\n- `exportable-charts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.\n\n## 4. API contract and Nuxt consumption\n\n- Consume only the matching API module linked above; use its documented OpenAPI schemas, routes, authentication, permissions, team context, pagination, errors, and operation semantics.\n- Keep a typed API client and module-local composables under the package boundary; use `useFetch` or `useAsyncData` for SSR-safe reads and `$fetch` for event-driven mutations.\n- Forward Sanctum cookies or approved authorization headers through a controlled client boundary; never persist long-lived tokens in browser storage or expose secrets in SSR payloads.\n- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.\n- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.\n\n## 5. Security and verification\n\n- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.\n- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, and minimal-host installation tests.\n- Test observable browser and SSR behavior with Vitest, Vue Test Utils, Playwright, TypeScript, and the supported Nuxt 4/Vue 3 stack; domain behavior remains covered by the owning module.\n\n## 6. Definition of done\n\n- Package identity, public exports, API dependency, and module dependency match `genealogy-reports` one-to-one.\n- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.\n- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-genealogy-reports-nuxt`
**Matching domain module:** `genealogy-reports`
**Application:** Genealogy
**Source feature:** [Reports](../features/reports.md)
**Architecture:** [NUXT.md](../GENEALOGY.md) · [API.md](../GENEALOGY.md) · [Matching API module](../api/reports.md) · [MODULES.md](../GENEALOGY.md) · [TESTING.md](../GENEALOGY.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `genealogy-reports` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Family groups:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Pedigrees:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Descendants:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Timelines:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Research:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Sources:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Exportable charts:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-genealogy-reports-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `family-groups`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `pedigrees`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `descendants`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `timelines`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `research`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `sources`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `exportable-charts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `genealogy-reports` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.
