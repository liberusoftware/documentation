# CMS: Site Factory Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#site-factory). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-cms-site-factory-nuxt`
**Matching domain module:** `cms-site-factory`
**Application:** CMS
**Source feature:** [Site Factory](../features/site-factory.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/site-factory.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `cms-site-factory` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Site templates/recipes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Provisioning:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Domain verification:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Initial content/configuration:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Cloning:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Suspension:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Archival:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Teardown:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-cms-site-factory-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `site-templates-recipes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `provisioning`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `domain-verification`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `initial-content-configuration`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `cloning`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `suspension`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `archival`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `teardown`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `cms-site-factory` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-cms-nuxt-vue`](https://github.com/liberusoftware/project-cms-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/site-factory.md)) |
| Capability Nuxt module skeleton | [`module-cms-site-factory-nuxt`](https://github.com/liberusoftware/module-cms-site-factory-nuxt) (`@liberusoftware/module-cms-site-factory-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Site templates/recipes** | Expose composable and Vue 3 component for `site templates/recipes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/site-factory.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Provisioning** | Expose composable and Vue 3 component for `provisioning` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/site-factory.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Domain verification** | Expose composable and Vue 3 component for `domain verification` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/site-factory.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Initial content/configuration** | Expose composable and Vue 3 component for `initial content/configuration` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/site-factory.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Cloning** | Expose composable and Vue 3 component for `cloning` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/site-factory.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Suspension** | Expose composable and Vue 3 component for `suspension` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/site-factory.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Archival** | Expose composable and Vue 3 component for `archival` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/site-factory.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Teardown** | Expose composable and Vue 3 component for `teardown` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/site-factory.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [SiteFactoryService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-site-factory/src/Services/SiteFactoryService.php) | `public function templates(): Collection`<br>`public function template(string $key, string $name, array $configuration = [], array $initialContent = [], ?int $teamId = null): SiteTemplate`<br>`public function updateTemplate(SiteTemplate $template, string $name, array $configuration, array $initialContent): SiteTemplate`<br>`public function activateTemplate(SiteTemplate $template): SiteTemplate`<br>`public function deactivateTemplate(SiteTemplate $template): SiteTemplate`<br>`public function provision(string $key, string $name, ?string $templateKey = null, ?string $domain = null, ?int $teamId = null): Site`<br>`public function addDomain(Site $site, string $domain): SiteDomain`<br>`public function verifyDomain(SiteDomain $domain, string $token): SiteDomain`<br>`public function clone(Site $source, string $key, string $name): Site`<br>`public function suspend(Site $site): Site`<br>`public function archive(Site $site): Site`<br>`public function transition(Site $site, string $status): Site`<br>`public function teardown(Site $site, bool $confirm = false): void`<br>`public function operations(?Site $site = null): Collection` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SiteDomain.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-site-factory/src/Models/SiteDomain.php) | `site_id`, `domain`, `verification_token`, `verified_at`, `team_id` |
| [SiteFactoryOperation.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-site-factory/src/Models/SiteFactoryOperation.php) | `site_id`, `team_id`, `operation`, `status`, `payload`, `error`, `completed_at` |
| [SiteTemplate.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-site-factory/src/Models/SiteTemplate.php) | `key`, `name`, `configuration`, `initial_content`, `active`, `team_id` |
<!-- layer-implementation-plan:end -->
