# Boilerplate: Feature Flags Nuxt presentation packages

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#feature-flags). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Design package identifier:** `module-feature-flags-nuxt`
**Matching core package:** [`module-feature-flags`](../core/feature-flags.md)
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Typed flags, environment/tenant/user targeting, rollout, telemetry, ownership, and cleanup.

## Adapter implementation plan

This package presents the Feature Flags core capability through Nuxt 4. It owns routes, resources, components, pages, hooks, forms, tables, or client state appropriate to this layer, but does not recreate domain rules, persistence, authorization, or provider integrations.

- Depend on the matching core package and call its typed actions, queries, policies, and resource DTOs through public contracts.
- Preserve tenant/team context, authorization, field visibility, validation, localization, timezone/currency behavior, accessibility, and safe error/recovery states.
- Consume the versioned API contract or approved server boundary; keep client state and views replaceable, typed, accessible, and resilient to partial failure.
- Add adapter contract tests for allowed and denied access, wrong tenant, validation, hidden fields, empty states, failures, retries, and compatibility with the core package.

## Scope

The package is optional and installable independently. Applications may omit it, replace it with another presentation adapter, or compose it with a custom theme while retaining the same Feature Flags core boundary.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-boilerplate-nuxt-vue`](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-boilerplate-laravel-api`](https://github.com/liberusoftware/project-boilerplate-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/feature-flags.md)) |
| Capability Nuxt module skeleton | [`module-feature-flags-nuxt`](https://github.com/liberusoftware/module-feature-flags-nuxt) (`@liberusoftware/module-feature-flags-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Typed flags** | Expose composable and Vue 3 component for `typed flags` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/feature-flags.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Environment/tenant/user targeting** | Expose composable and Vue 3 component for `environment/tenant/user targeting` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/feature-flags.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Rollout** | Expose composable and Vue 3 component for `rollout` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/feature-flags.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Telemetry** | Expose composable and Vue 3 component for `telemetry` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/feature-flags.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Ownership** | Expose composable and Vue 3 component for `ownership` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/feature-flags.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Cleanup** | Expose composable and Vue 3 component for `cleanup` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/feature-flags.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |

### Observed domain and transport source evidence

**Observed route declarations:**

[modules/feature-flags-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/feature-flags-api/routes/api.php)

```php
Route::prefix('api/v1/feature-flags')->middleware('api')->group(function (): void {
Route::get('/status', StatusController::class)->name('feature-flags-api.status');
```
<!-- layer-implementation-plan:end -->
