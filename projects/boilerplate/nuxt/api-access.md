# Boilerplate: API Access Nuxt presentation packages

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#api-access). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Design package identifier:** `module-api-access-nuxt`
**Matching core package:** [`module-api-access`](../core/api-access.md)
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Tokens, service identities, scopes, rate limits, versioning, idempotency, and revocation.

## Adapter implementation plan

This package presents the API Access core capability through Nuxt 4. It owns routes, resources, components, pages, hooks, forms, tables, or client state appropriate to this layer, but does not recreate domain rules, persistence, authorization, or provider integrations.

- Depend on the matching core package and call its typed actions, queries, policies, and resource DTOs through public contracts.
- Preserve tenant/team context, authorization, field visibility, validation, localization, timezone/currency behavior, accessibility, and safe error/recovery states.
- Consume the versioned API contract or approved server boundary; keep client state and views replaceable, typed, accessible, and resilient to partial failure.
- Add adapter contract tests for allowed and denied access, wrong tenant, validation, hidden fields, empty states, failures, retries, and compatibility with the core package.

## Scope

The package is optional and installable independently. Applications may omit it, replace it with another presentation adapter, or compose it with a custom theme while retaining the same API Access core boundary.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-boilerplate-nuxt-vue`](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-boilerplate-laravel-api`](https://github.com/liberusoftware/project-boilerplate-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/api-access.md)) |
| Capability Nuxt module skeleton | [`module-api-access-nuxt`](https://github.com/liberusoftware/module-api-access-nuxt) (`@liberusoftware/module-api-access-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Tokens** | Expose composable and Vue 3 component for `tokens` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/api-access.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Service identities** | Expose composable and Vue 3 component for `service identities` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/api-access.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Scopes** | Expose composable and Vue 3 component for `scopes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/api-access.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Rate limits** | Expose composable and Vue 3 component for `rate limits` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/api-access.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Versioning** | Expose composable and Vue 3 component for `versioning` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/api-access.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Idempotency** | Expose composable and Vue 3 component for `idempotency` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/api-access.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Revocation** | Expose composable and Vue 3 component for `revocation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/api-access.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |

### Observed domain and transport source evidence

**Observed route declarations:**

[modules/api-access-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/api-access-api/routes/api.php)

```php
Route::prefix('api/v1/api-access')->middleware('api')->group(function (): void {
Route::get('/status', StatusController::class)->name('api-access-api.status');
```
<!-- layer-implementation-plan:end -->
