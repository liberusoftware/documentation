# CRM: Crm Template Snapshots Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-template-snapshots). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-crm-template-snapshots-nuxt`
**Matching domain module:** `crm-template-snapshots`
**Application:** CRM
**Source feature:** [Crm Template Snapshots](../features/crm-template-snapshots.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-template-snapshots.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-template-snapshots` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

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

- Register a stable `module-crm-crm-template-snapshots-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
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

- Package identity, public exports, API dependency, and module dependency match `crm-template-snapshots` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-template-snapshots.md)) |
| Capability Nuxt module skeleton | [`module-crm-crm-template-snapshots-nuxt`](https://github.com/liberusoftware/module-crm-crm-template-snapshots-nuxt) (`@liberusoftware/module-crm-crm-template-snapshots-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Versioned bundles of fields** | Expose composable and Vue 3 component for `versioned bundles of fields` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-template-snapshots.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Pipelines** | Expose composable and Vue 3 component for `pipelines` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-template-snapshots.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Workflows** | Expose composable and Vue 3 component for `workflows` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-template-snapshots.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Forms** | Expose composable and Vue 3 component for `forms` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-template-snapshots.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Funnels** | Expose composable and Vue 3 component for `funnels` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-template-snapshots.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Calendars** | Expose composable and Vue 3 component for `calendars` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-template-snapshots.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Templates** | Expose composable and Vue 3 component for `templates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-template-snapshots.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Dashboards** | Expose composable and Vue 3 component for `dashboards` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-template-snapshots.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Settings with preview** | Expose composable and Vue 3 component for `settings with preview` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-template-snapshots.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Protected sharing** | Expose composable and Vue 3 component for `protected sharing` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-template-snapshots.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Install** | Expose composable and Vue 3 component for `install` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-template-snapshots.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Update** | Expose composable and Vue 3 component for `update` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-template-snapshots.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Rollback** | Expose composable and Vue 3 component for `rollback` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-template-snapshots.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

No dedicated source files were matched in the pinned module roots for this spelling. Consult the [project source map](../SOURCE-MAPPING.md) and owning domain/API plans before implementing new callables or routes.
<!-- layer-implementation-plan:end -->
