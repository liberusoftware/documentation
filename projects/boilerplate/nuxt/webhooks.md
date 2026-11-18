# Boilerplate: Webhooks Nuxt presentation packages

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#webhooks). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Design package identifier:** `module-webhooks-nuxt`
**Matching core package:** [`module-webhooks`](../core/webhooks.md)
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Endpoint registration, signing, delivery attempts, retries, replay, event filtering, and logs.

## Adapter implementation plan

This package presents the Webhooks core capability through Nuxt 4. It owns routes, resources, components, pages, hooks, forms, tables, or client state appropriate to this layer, but does not recreate domain rules, persistence, authorization, or provider integrations.

- Depend on the matching core package and call its typed actions, queries, policies, and resource DTOs through public contracts.
- Preserve tenant/team context, authorization, field visibility, validation, localization, timezone/currency behavior, accessibility, and safe error/recovery states.
- Consume the versioned API contract or approved server boundary; keep client state and views replaceable, typed, accessible, and resilient to partial failure.
- Add adapter contract tests for allowed and denied access, wrong tenant, validation, hidden fields, empty states, failures, retries, and compatibility with the core package.

## Scope

The package is optional and installable independently. Applications may omit it, replace it with another presentation adapter, or compose it with a custom theme while retaining the same Webhooks core boundary.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-boilerplate-nuxt-vue`](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-boilerplate-laravel-api`](https://github.com/liberusoftware/project-boilerplate-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/webhooks.md)) |
| Capability Nuxt module skeleton | [`module-webhooks-nuxt`](https://github.com/liberusoftware/module-webhooks-nuxt) (`@liberusoftware/module-webhooks-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Endpoint registration** | Expose composable and Vue 3 component for `endpoint registration` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/webhooks.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Signing** | Expose composable and Vue 3 component for `signing` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/webhooks.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Delivery attempts** | Expose composable and Vue 3 component for `delivery attempts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/webhooks.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Retries** | Expose composable and Vue 3 component for `retries` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/webhooks.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Replay** | Expose composable and Vue 3 component for `replay` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/webhooks.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Event filtering** | Expose composable and Vue 3 component for `event filtering` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/webhooks.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Logs** | Expose composable and Vue 3 component for `logs` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/webhooks.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |

### Observed domain and transport source evidence

**Observed route declarations:**

[modules/webhooks-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/webhooks-api/routes/api.php)

```php
Route::prefix('api/v1/webhooks')->middleware('api')->group(function (): void {
Route::get('/status', StatusController::class)->name('webhooks-api.status');
```

[modules/webhooks-api/routes/api.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/webhooks-api/routes/api.php)

```php
Route::prefix('api/v1/webhooks')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [WebhooksController::class, 'index']);
Route::post('/', [WebhooksController::class, 'store']);
Route::post('/{endpoint}/rotate-secret', [WebhooksController::class, 'rotate']);
Route::get('/{endpoint}/deliveries', [WebhooksController::class, 'deliveries']);
Route::post('/{endpoint}/deliveries/{delivery}/replay', [WebhooksController::class, 'replay']);
```
<!-- layer-implementation-plan:end -->
