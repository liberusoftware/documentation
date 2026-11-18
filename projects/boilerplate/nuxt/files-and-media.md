# Boilerplate: Files and Media Nuxt presentation packages

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#files-and-media). No dedicated package name match was found for this layer in the scanned module manifests. This retained spelling maps to `files-media`; it is not another independent module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Design package identifier:** `module-files-and-media-nuxt`
**Matching core package:** [`module-files-and-media`](../core/files-and-media.md)
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Storage contracts, uploads, validation, scanning, metadata, access, transformations, and retention.

## Adapter implementation plan

This package presents the Files and Media core capability through Nuxt 4. It owns routes, resources, components, pages, hooks, forms, tables, or client state appropriate to this layer, but does not recreate domain rules, persistence, authorization, or provider integrations.

- Depend on the matching core package and call its typed actions, queries, policies, and resource DTOs through public contracts.
- Preserve tenant/team context, authorization, field visibility, validation, localization, timezone/currency behavior, accessibility, and safe error/recovery states.
- Consume the versioned API contract or approved server boundary; keep client state and views replaceable, typed, accessible, and resilient to partial failure.
- Add adapter contract tests for allowed and denied access, wrong tenant, validation, hidden fields, empty states, failures, retries, and compatibility with the core package.

## Scope

The package is optional and installable independently. Applications may omit it, replace it with another presentation adapter, or compose it with a custom theme while retaining the same Files and Media core boundary.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-boilerplate-nuxt-vue`](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-boilerplate-laravel-api`](https://github.com/liberusoftware/project-boilerplate-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/files-and-media.md)) |
| Capability Nuxt module skeleton | [`module-files-media-nuxt`](https://github.com/liberusoftware/module-files-media-nuxt) (`@liberusoftware/module-files-media-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Storage contracts** | Expose composable and Vue 3 component for `storage contracts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/files-and-media.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Uploads** | Expose composable and Vue 3 component for `uploads` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/files-and-media.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Validation** | Expose composable and Vue 3 component for `validation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/files-and-media.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Scanning** | Expose composable and Vue 3 component for `scanning` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/files-and-media.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Metadata** | Expose composable and Vue 3 component for `metadata` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/files-and-media.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Access** | Expose composable and Vue 3 component for `access` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/files-and-media.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Transformations** | Expose composable and Vue 3 component for `transformations` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/files-and-media.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |
| **Retention** | Expose composable and Vue 3 component for `retention` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/files-and-media.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-boilerplate-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [MalwareScanner.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/files-media/src/Contracts/MalwareScanner.php) | `public function clean(string $path): bool` |
| [MediaAccess.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/files-media/src/Contracts/MediaAccess.php) | `public function authorized(string\|int\|null $actorId, string $mediaId, string $operation): bool` |
| [MediaTransformer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/files-media/src/Contracts/MediaTransformer.php) | `public function transform(string $source, string $operation, array $parameters = []): string` |

**Observed route declarations:**

[modules/files-media-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/files-media-api/routes/api.php)

```php
Route::prefix('api/v1/files-media')->middleware('api')->group(function (): void {
Route::get('/status', StatusController::class)->name('files-media-api.status');
```
<!-- layer-implementation-plan:end -->
