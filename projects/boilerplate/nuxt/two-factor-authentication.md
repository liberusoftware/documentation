# Boilerplate: Two-Factor Authentication Nuxt presentation packages

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#two-factor-authentication). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Design package identifier:** `module-two-factor-authentication-nuxt`
**Matching core package:** [`module-two-factor-authentication`](../core/two-factor-authentication.md)
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** TOTP enrollment, recovery codes, enforcement, trusted devices, recovery, and audit.

## Adapter implementation plan

This package presents the Two-Factor Authentication core capability through Nuxt 4. It owns routes, resources, components, pages, hooks, forms, tables, or client state appropriate to this layer, but does not recreate domain rules, persistence, authorization, or provider integrations.

- Depend on the matching core package and call its typed actions, queries, policies, and resource DTOs through public contracts.
- Preserve tenant/team context, authorization, field visibility, validation, localization, timezone/currency behavior, accessibility, and safe error/recovery states.
- Consume the versioned API contract or approved server boundary; keep client state and views replaceable, typed, accessible, and resilient to partial failure.
- Add adapter contract tests for allowed and denied access, wrong tenant, validation, hidden fields, empty states, failures, retries, and compatibility with the core package.

## Scope

The package is optional and installable independently. Applications may omit it, replace it with another presentation adapter, or compose it with a custom theme while retaining the same Two-Factor Authentication core boundary.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-boilerplate-nuxt-vue`](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-boilerplate-laravel-api`](https://github.com/liberusoftware/project-boilerplate-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/two-factor-authentication.md)) |
| Capability Nuxt module skeleton | [`module-two-factor-authentication-nuxt`](https://github.com/liberusoftware/module-two-factor-authentication-nuxt) (`@liberusoftware/module-two-factor-authentication-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **TOTP enrollment** | Expose composable and Vue 3 component for `totp enrollment` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/two-factor-authentication.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Recovery codes** | Expose composable and Vue 3 component for `recovery codes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/two-factor-authentication.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Enforcement** | Expose composable and Vue 3 component for `enforcement` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/two-factor-authentication.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Trusted devices** | Expose composable and Vue 3 component for `trusted devices` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/two-factor-authentication.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Recovery** | Expose composable and Vue 3 component for `recovery` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/two-factor-authentication.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Audit** | Expose composable and Vue 3 component for `audit` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/two-factor-authentication.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [TwoFactorRecovery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/two-factor-authentication/src/Contracts/TwoFactorRecovery.php) | `public function recover(Authenticatable $subject, Authenticatable $administrator, string $reason): void` |

**Observed route declarations:**

[modules/two-factor-authentication-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/two-factor-authentication-api/routes/api.php)

```php
Route::prefix('api/v1/two-factor-authentication')->middleware('api')->group(function (): void {
Route::get('/status', StatusController::class)->name('two-factor-authentication-api.status');
```
<!-- layer-implementation-plan:end -->
