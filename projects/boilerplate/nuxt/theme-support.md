# Boilerplate: Theme Support Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#theme-support). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-boilerplate-theme-support-nuxt`
**Matching domain module:** `theme-support`
**Application:** Boilerplate
**Source feature:** [Theme Support](../features/theme-support.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/theme-support.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `theme-support` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Theme discovery:** page/component/composable/API-action behavior for this module's authorized workflow.
- **View overrides:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Safe asset directives:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Preferences:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Panel palettes:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-boilerplate-theme-support-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `theme-discovery`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `view-overrides`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `safe-asset-directives`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `preferences`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `panel-palettes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `theme-support` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-boilerplate-nuxt-vue`](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-boilerplate-laravel-api`](https://github.com/liberusoftware/project-boilerplate-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/theme-support.md)) |
| Capability Nuxt module skeleton | [`module-theme-support-nuxt`](https://github.com/liberusoftware/module-theme-support-nuxt) (`@liberusoftware/module-theme-support-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Theme discovery** | Expose composable and Vue 3 component for `theme discovery` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/theme-support.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **View overrides** | Expose composable and Vue 3 component for `view overrides` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/theme-support.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Safe asset directives** | Expose composable and Vue 3 component for `safe asset directives` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/theme-support.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Preferences** | Expose composable and Vue 3 component for `preferences` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/theme-support.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Panel palettes** | Expose composable and Vue 3 component for `panel palettes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/theme-support.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ThemeManager.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/theme-support/src/Services/ThemeManager.php) | `public function __construct(?string $themesPath = null)`<br>`public function setTheme(string $theme): void`<br>`public function persistTheme(string $theme): void`<br>`public function selectForSurface(string $surface, ?string $site = null, ?string $tenant = null): string`<br>`public function getActiveTheme(): string`<br>`public function getSiteTheme(): string`<br>`public function getThemes(): array`<br>`public function providers(): array`<br>`public function themeExists(string $theme): bool`<br>`public function themeIsCompatible(string $theme): bool`<br>`public function getThemePath(?string $theme = null): string`<br>`public function getThemeViewsPath(?string $theme = null): string`<br>`public function getThemeAssetPath(string $type, ?string $theme = null): ?string`<br>`public function inheritanceChain(?string $theme = null): array`<br>`public function registerThemePaths(): void`<br>`public function getThemeCss(?string $theme = null): ?string`<br>`public function getThemeJs(?string $theme = null): ?string`<br>`public function activeEntries(): array`<br>`public function assetUrl(string $path, ?string $theme = null): string`<br>`public function activeCssEntry(): string`<br>`public function viteHasAsset(string $path): bool`<br>`public function getThemeConfig(?string $theme = null): array`<br>`public function primaryColor(?string $theme = null): string`<br>`public function clearCache(): void`<br>`public function hasCustomLayout(string $layout, ?string $theme = null): bool`<br>`public function getLayout(string $layout, ?string $theme = null): string` |
<!-- layer-implementation-plan:end -->
