# Boilerplate: Sessions and Devices Nuxt presentation packages

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#sessions-and-devices). No dedicated package name match was found for this layer in the scanned module manifests. This retained spelling maps to `sessions-devices`; it is not another independent module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Design package identifier:** `module-sessions-and-devices-nuxt`
**Matching core package:** [`module-sessions-and-devices`](../core/sessions-and-devices.md)
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Active sessions, device metadata, revocation, timeout policy, suspicious access, and retention.

## Adapter implementation plan

This package presents the Sessions and Devices core capability through Nuxt 4. It owns routes, resources, components, pages, hooks, forms, tables, or client state appropriate to this layer, but does not recreate domain rules, persistence, authorization, or provider integrations.

- Depend on the matching core package and call its typed actions, queries, policies, and resource DTOs through public contracts.
- Preserve tenant/team context, authorization, field visibility, validation, localization, timezone/currency behavior, accessibility, and safe error/recovery states.
- Consume the versioned API contract or approved server boundary; keep client state and views replaceable, typed, accessible, and resilient to partial failure.
- Add adapter contract tests for allowed and denied access, wrong tenant, validation, hidden fields, empty states, failures, retries, and compatibility with the core package.

## Scope

The package is optional and installable independently. Applications may omit it, replace it with another presentation adapter, or compose it with a custom theme while retaining the same Sessions and Devices core boundary.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-boilerplate-nuxt-vue`](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-boilerplate-laravel-api`](https://github.com/liberusoftware/project-boilerplate-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/sessions-and-devices.md)) |
| Capability Nuxt module skeleton | [`module-sessions-devices-nuxt`](https://github.com/liberusoftware/module-sessions-devices-nuxt) (`@liberusoftware/module-sessions-devices-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Active sessions** | Expose composable and Vue 3 component for `active sessions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/sessions-and-devices.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Device metadata** | Expose composable and Vue 3 component for `device metadata` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/sessions-and-devices.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Revocation** | Expose composable and Vue 3 component for `revocation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/sessions-and-devices.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Timeout policy** | Expose composable and Vue 3 component for `timeout policy` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/sessions-and-devices.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Suspicious access** | Expose composable and Vue 3 component for `suspicious access` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/sessions-and-devices.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Retention** | Expose composable and Vue 3 component for `retention` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/sessions-and-devices.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [SessionReader.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/sessions-devices/src/Queries/SessionReader.php) | `public function forActor(string\|int $actorId, ?string $currentId = null): Collection`<br>`public function revoke(string\|int $actorId, string $sessionId, ?string $currentId = null): bool`<br>`public function revokeOthers(string\|int $actorId, string $currentId): int` |

**Observed route declarations:**

[modules/sessions-devices-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/sessions-devices-api/routes/api.php)

```php
Route::prefix('api/v1/sessions-devices')->middleware('api')->group(function (): void {
Route::get('/status', StatusController::class)->name('sessions-devices-api.status');
```
<!-- layer-implementation-plan:end -->
