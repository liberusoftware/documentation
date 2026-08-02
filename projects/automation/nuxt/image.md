# Automation: Image Nuxt\n\n## Canonical one-to-one Nuxt 4 implementation\n\n**Nuxt package:** `module-automation-image-nuxt`\n**Matching domain module:** `automation-image`\n**Application:** Automation\n**Source feature:** [Image](../features/image.md)\n**Architecture:** [NUXT.md](../AUTOMATION.md) · [API.md](../AUTOMATION.md) · [Matching API module](../api/image.md) · [MODULES.md](../AUTOMATION.md) · [TESTING.md](../AUTOMATION.md)\n\n## 1. Purpose and ownership\n\nThis optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `automation-image` public API boundary. It must not contain another module's UI or depend on application `App\` classes.\n\n## 2. Module-specific surfaces\n\n- **Generation/editing requests:** page/component/composable/API-action behavior for this module's authorized workflow.\n- **Source assets:** page/component/composable/API-action behavior for this module's authorized workflow.\n- **Moderation:** page/component/composable/API-action behavior for this module's authorized workflow.\n- **Provenance:** page/component/composable/API-action behavior for this module's authorized workflow.\n- **Variants:** page/component/composable/API-action behavior for this module's authorized workflow.\n- **Delivery:** page/component/composable/API-action behavior for this module's authorized workflow.\n\n## 3. Nuxt 4 implementation\n\n- Register a stable `module-automation-image-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.\n- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.\n- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.\n- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.\n\n### Capability mapping\n\n- `generation/editing-requests`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.\n- `source-assets`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.\n- `moderation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.\n- `provenance`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.\n- `variants`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.\n- `delivery`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.\n\n## 4. API contract and Nuxt consumption\n\n- Consume only the matching API module linked above; use its documented OpenAPI schemas, routes, authentication, permissions, team context, pagination, errors, and operation semantics.\n- Keep a typed API client and module-local composables under the package boundary; use `useFetch` or `useAsyncData` for SSR-safe reads and `$fetch` for event-driven mutations.\n- Forward Sanctum cookies or approved authorization headers through a controlled client boundary; never persist long-lived tokens in browser storage or expose secrets in SSR payloads.\n- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.\n- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.\n\n## 5. Security and verification\n\n- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.\n- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, and minimal-host installation tests.\n- Test observable browser and SSR behavior with Vitest, Vue Test Utils, Playwright, TypeScript, and the supported Nuxt 4/Vue 3 stack; domain behavior remains covered by the owning module.\n\n## 6. Definition of done\n\n- Package identity, public exports, API dependency, and module dependency match `automation-image` one-to-one.\n- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.\n- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-automation-image-nuxt`
**Matching domain module:** `automation-image`
**Application:** Automation
**Source feature:** [Image](../features/image.md)
**Architecture:** [NUXT.md](../AUTOMATION.md) · [API.md](../AUTOMATION.md) · [Matching API module](../api/image.md) · [MODULES.md](../AUTOMATION.md) · [TESTING.md](../AUTOMATION.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `automation-image` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Generation/editing requests:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Source assets:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Moderation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Provenance:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Variants:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Delivery:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-automation-image-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `generation/editing-requests`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `source-assets`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `moderation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `provenance`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `variants`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `delivery`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `automation-image` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.
