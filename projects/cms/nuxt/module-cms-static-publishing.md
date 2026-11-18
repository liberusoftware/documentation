# CMS: Module Cms Static Publishing Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-static-publishing). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-cms-module-cms-static-publishing-nuxt`
**Matching domain module:** `module-cms-static-publishing`
**Application:** CMS
**Source feature:** [Module Cms Static Publishing](../features/module-cms-static-publishing.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/module-cms-static-publishing.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `module-cms-static-publishing` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Full/incremental builds:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Route manifests:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Cache invalidation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Deployment adapters:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Preview builds:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Rollback:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Build diagnostics:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-cms-module-cms-static-publishing-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `full-incremental-builds`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `route-manifests`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `cache-invalidation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `deployment-adapters`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `preview-builds`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `rollback`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `build-diagnostics`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `module-cms-static-publishing` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-cms-nuxt-vue`](https://github.com/liberusoftware/project-cms-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/module-cms-static-publishing.md)) |
| Capability Nuxt module skeleton | [`module-cms-static-publishing-nuxt`](https://github.com/liberusoftware/module-cms-static-publishing-nuxt) (`@liberusoftware/module-cms-static-publishing-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Full/incremental builds** | Expose composable and Vue 3 component for `full/incremental builds` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-static-publishing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Route manifests** | Expose composable and Vue 3 component for `route manifests` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-static-publishing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Cache invalidation** | Expose composable and Vue 3 component for `cache invalidation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-static-publishing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Deployment adapters** | Expose composable and Vue 3 component for `deployment adapters` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-static-publishing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Preview builds** | Expose composable and Vue 3 component for `preview builds` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-static-publishing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Rollback** | Expose composable and Vue 3 component for `rollback` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-static-publishing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Build diagnostics** | Expose composable and Vue 3 component for `build diagnostics` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-static-publishing.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [StaticPublishingQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-static-publishing/src/Queries/StaticPublishingQuery.php) | `public function builds(int $perPage = 15): LengthAwarePaginator`<br>`public function build(int\|string $id): ?StaticBuild` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [DeploymentAdapterInterface.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-static-publishing/src/Contracts/DeploymentAdapterInterface.php) | `public function key(): string`<br>`public function deploy(StaticBuild $build): array` |
| [StaticPublishingService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-static-publishing/src/Services/StaticPublishingService.php) | `public function __construct(private DeploymentAdapterRegistry $deployments)`<br>`public function build(array $routes, ?string $siteKey = null, string $kind = 'full', string $deployment = 'local', ?StaticBuild $parent = null): StaticBuild`<br>`public function invalidate(StaticBuild $build, string $path, string $reason = 'content-changed'): StaticInvalidation`<br>`public function rollback(StaticBuild $build): StaticBuild`<br>`public function diagnostics(StaticBuild $build): array`<br>`public function deploy(StaticBuild $build, string $adapter): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [StaticBuild.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-static-publishing/src/Models/StaticBuild.php) | `site_key`, `state`, `kind`, `deployment`, `manifest`, `diagnostics`, `parent_build_id`, `checksum`, `started_at`, `finished_at`, `team_id` |
| [StaticInvalidation.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-static-publishing/src/Models/StaticInvalidation.php) | `build_id`, `path`, `reason`, `created_at` |
<!-- layer-implementation-plan:end -->
