# CMS: Module Cms Theme Integration Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-theme-integration). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-cms-module-cms-theme-integration-nuxt`
**Matching domain module:** `module-cms-theme-integration`
**Application:** CMS
**Source feature:** [Module Cms Theme Integration](../features/module-cms-theme-integration.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/module-cms-theme-integration.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `module-cms-theme-integration` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Theme selection by site/channel:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Regions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **View contracts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Component registry:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Inheritance:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Preview:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Safe fallback:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-cms-module-cms-theme-integration-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `theme-selection-by-site-channel`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `regions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `view-contracts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `component-registry`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `inheritance`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `preview`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `safe-fallback`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `module-cms-theme-integration` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-cms-nuxt-vue`](https://github.com/liberusoftware/project-cms-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/module-cms-theme-integration.md)) |
| Capability Nuxt module skeleton | [`module-cms-theme-integration-nuxt`](https://github.com/liberusoftware/module-cms-theme-integration-nuxt) (`@liberusoftware/module-cms-theme-integration-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Theme selection by site/channel** | Expose composable and Vue 3 component for `theme selection by site/channel` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-theme-integration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Regions** | Expose composable and Vue 3 component for `regions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-theme-integration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **View contracts** | Expose composable and Vue 3 component for `view contracts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-theme-integration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Component registry** | Expose composable and Vue 3 component for `component registry` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-theme-integration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Inheritance** | Expose composable and Vue 3 component for `inheritance` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-theme-integration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Preview** | Expose composable and Vue 3 component for `preview` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-theme-integration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Safe fallback** | Expose composable and Vue 3 component for `safe fallback` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-theme-integration.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ThemeIntegrationQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-theme-integration/src/Queries/ThemeIntegrationQuery.php) | `public function __construct(private TenantContextInterface $tenant)`<br>`public function bindings(int $perPage = 15, ?int $teamId = null): LengthAwarePaginator`<br>`public function binding(string $siteKey, ?string $channelKey = null, ?int $teamId = null): ?ThemeBinding`<br>`public function bindingById(int\|string $id, ?int $teamId = null): ?ThemeBinding`<br>`public function components(string $themeKey, ?string $region = null, ?int $teamId = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ThemeIntegrationService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-theme-integration/src/Services/ThemeIntegrationService.php) | `public function __construct(private ThemeIntegrationQuery $query)`<br>`public function bind(string $siteKey, ?string $channelKey, string $themeKey, string $fallbackThemeKey = 'default', ?int $teamId = null): ThemeBinding`<br>`public function updateBinding(ThemeBinding $binding, array $attributes): ThemeBinding`<br>`public function removeBinding(ThemeBinding $binding): void`<br>`public function select(?string $siteKey, ?string $channelKey = null, ?int $teamId = null): ?ThemeBinding`<br>`public function effectiveTheme(?string $siteKey, ?string $channelKey = null, ?int $teamId = null): string`<br>`public function registerComponent(string $themeKey, string $region, string $componentKey, array $viewContract = [], array $configuration = [], ?int $teamId = null): ThemeComponent`<br>`public function components(string $themeKey, ?string $region = null, ?int $teamId = null): array`<br>`public function previewToken(ThemeBinding $binding): string`<br>`public function preview(ThemeBinding $binding, string $token): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ThemeBinding.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-theme-integration/src/Models/ThemeBinding.php) | `site_key`, `channel_key`, `theme_key`, `fallback_theme_key`, `preview_token`, `preview_expires_at`, `active`, `team_id` |
| [ThemeComponent.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-theme-integration/src/Models/ThemeComponent.php) | `theme_key`, `region`, `component_key`, `view_contract`, `configuration`, `team_id` |
<!-- layer-implementation-plan:end -->
