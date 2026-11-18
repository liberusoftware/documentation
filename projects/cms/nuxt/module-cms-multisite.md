# CMS: Module Cms Multisite Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-multisite). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-cms-module-cms-multisite-nuxt`
**Matching domain module:** `module-cms-multisite`
**Application:** CMS
**Source feature:** [Module Cms Multisite](../features/module-cms-multisite.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/module-cms-multisite.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `module-cms-multisite` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Site network:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Shared/isolated content:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Domains:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Site admins:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Quotas:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Site lifecycle:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Network operations:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Safe cross-site references:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-cms-module-cms-multisite-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `site-network`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `shared-isolated-content`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `domains`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `site-admins`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `quotas`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `site-lifecycle`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `network-operations`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `safe-cross-site-references`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `module-cms-multisite` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-cms-nuxt-vue`](https://github.com/liberusoftware/project-cms-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/module-cms-multisite.md)) |
| Capability Nuxt module skeleton | [`module-cms-multisite-nuxt`](https://github.com/liberusoftware/module-cms-multisite-nuxt) (`@liberusoftware/module-cms-multisite-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Site network** | Expose composable and Vue 3 component for `site network` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-multisite.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Shared/isolated content** | Expose composable and Vue 3 component for `shared/isolated content` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-multisite.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Domains** | Expose composable and Vue 3 component for `domains` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-multisite.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Site admins** | Expose composable and Vue 3 component for `site admins` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-multisite.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Quotas** | Expose composable and Vue 3 component for `quotas` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-multisite.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Site lifecycle** | Expose composable and Vue 3 component for `site lifecycle` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-multisite.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Network operations** | Expose composable and Vue 3 component for `network operations` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-multisite.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Safe cross-site references** | Expose composable and Vue 3 component for `safe cross-site references` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-multisite.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [MultisiteService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-multisite/src/Services/MultisiteService.php) | `public function __construct(private SiteFactoryService $factory)`<br>`public function createSite(string $key, string $name, ?string $domain = null, ?int $teamId = null): Site`<br>`public function transition(Site $site, string $status): Site`<br>`public function setQuota(Site $site, array $limits): SiteQuota`<br>`public function recordUsage(SiteQuota $quota, array $delta): SiteQuota`<br>`public function assignAdmin(Site $site, int $userId, string $role = 'editor'): SiteAdmin`<br>`public function removeAdmin(SiteAdmin $admin): void`<br>`public function reference(Site $source, Site $target, string $contentType, string $contentId, string $mode = 'shared'): SiteReference`<br>`public function networkTransition(array $siteIds, string $status): int` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SiteAdmin.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-multisite/src/Models/SiteAdmin.php) | `site_id`, `user_id`, `role`, `active`, `team_id` |
| [SiteQuota.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-multisite/src/Models/SiteQuota.php) | `site_id`, `limits`, `usage`, `team_id` |
| [SiteReference.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-multisite/src/Models/SiteReference.php) | `source_site_id`, `target_site_id`, `content_type`, `content_id`, `mode`, `status`, `team_id` |
<!-- layer-implementation-plan:end -->
