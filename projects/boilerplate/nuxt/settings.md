# Boilerplate: Settings Nuxt presentation packages

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#settings). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Design package identifier:** `module-settings-nuxt`
**Matching core package:** [`module-settings`](../core/settings.md)
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Typed application/organization/team/user settings, precedence, validation, secrets, audit, and cache invalidation.

## Adapter implementation plan

This package presents the Settings core capability through Nuxt 4. It owns routes, resources, components, pages, hooks, forms, tables, or client state appropriate to this layer, but does not recreate domain rules, persistence, authorization, or provider integrations.

- Depend on the matching core package and call its typed actions, queries, policies, and resource DTOs through public contracts.
- Preserve tenant/team context, authorization, field visibility, validation, localization, timezone/currency behavior, accessibility, and safe error/recovery states.
- Consume the versioned API contract or approved server boundary; keep client state and views replaceable, typed, accessible, and resilient to partial failure.
- Add adapter contract tests for allowed and denied access, wrong tenant, validation, hidden fields, empty states, failures, retries, and compatibility with the core package.

## Scope

The package is optional and installable independently. Applications may omit it, replace it with another presentation adapter, or compose it with a custom theme while retaining the same Settings core boundary.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-boilerplate-nuxt-vue`](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-boilerplate-laravel-api`](https://github.com/liberusoftware/project-boilerplate-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/settings.md)) |
| Capability Nuxt module skeleton | [`module-settings-nuxt`](https://github.com/liberusoftware/module-settings-nuxt) (`@liberusoftware/module-settings-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Typed application/organization/team/user settings** | Expose composable and Vue 3 component for `typed application/organization/team/user settings` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/settings.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Precedence** | Expose composable and Vue 3 component for `precedence` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/settings.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Validation** | Expose composable and Vue 3 component for `validation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/settings.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Secrets** | Expose composable and Vue 3 component for `secrets` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/settings.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Audit** | Expose composable and Vue 3 component for `audit` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/settings.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Cache invalidation** | Expose composable and Vue 3 component for `cache invalidation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/settings.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [SettingDefinition.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/settings/src/Contracts/SettingDefinition.php) | `public function key(): string`<br>`public function validate(mixed $value): bool`<br>`public function secret(): bool` |
| [ScopedSettings.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/settings/src/Services/ScopedSettings.php) | `public function put(SettingDefinition $definition, string $scopeType, string $scopeId, mixed $value): void`<br>`public function resolve(string $key, array $scopes, mixed $fallback = null): mixed` |

**Observed route declarations:**

[modules/settings-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/settings-api/routes/api.php)

```php
Route::prefix('api/v1/settings')->middleware('api')->group(function (): void {
Route::get('/status', StatusController::class)->name('settings-api.status');
```
<!-- layer-implementation-plan:end -->
