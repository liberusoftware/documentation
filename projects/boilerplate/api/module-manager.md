# Boilerplate: Module Manager API presentation packages

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-manager). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Design package identifier:** `module-module-manager-api`
**Matching core package:** [`module-module-manager`](../core/module-manager.md)
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Manifest discovery, dependency resolution, enablement, lifecycle, compatibility, registry caching, and diagnostics.

## Adapter implementation plan

This package presents the Module Manager core capability through API. It owns routes, resources, components, pages, hooks, forms, tables, or client state appropriate to this layer, but does not recreate domain rules, persistence, authorization, or provider integrations.

- Depend on the matching core package and call its typed actions, queries, policies, and resource DTOs through public contracts.
- Preserve tenant/team context, authorization, field visibility, validation, localization, timezone/currency behavior, accessibility, and safe error/recovery states.
- Publish versioned OpenAPI 3.1 schemas, operation IDs, scopes, pagination, rate limits, idempotency, concurrency, and RFC 9457 Problem Details.
- Add adapter contract tests for allowed and denied access, wrong tenant, validation, hidden fields, empty states, failures, retries, and compatibility with the core package.

## Scope

The package is optional and installable independently. Applications may omit it, replace it with another presentation adapter, or compose it with a custom theme while retaining the same Module Manager core boundary.

<!-- observed-api-contract:start -->
## 3. Endpoint examples

**Contract status:** use the observed source below for current route/handler/schema evidence. The surrounding module scope is a target design; its feature labels are not request field names. Do not generate a create/update/delete payload or final URL by mechanically copying the design identifier.

### Product API backend and client integration

This module API adapter is composed into [`project-boilerplate-laravel-api`](https://github.com/liberusoftware/project-boilerplate-laravel-api), the shared Laravel HTTP backend for independent web, mobile, and desktop clients ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [repository map](../../REPOSITORIES.md#laravel-applications)).

| Consuming client surface | Host repository | Module adapter plan | Transport and auth contract |
| --- | --- | --- | --- |
| Next.js React | [`project-boilerplate-next-react`](https://github.com/liberusoftware/project-boilerplate-next-react) | [Next.js plan](../nextjs/module-manager.md) | Server Component / Route Handler / BFF or Sanctum SPA with `no-store` private reads |
| Nuxt 4 Vue | [`project-boilerplate-nuxt-vue`](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) | [Nuxt plan](../nuxt/module-manager.md) | Nitro SSR / BFF or Sanctum SPA with actor/tenant-scoped `useFetch` keys |
| React Native Expo | [`project-boilerplate-mobile-react`](https://github.com/liberusoftware/project-boilerplate-mobile-react) | [React Native plan](../react-native/module-manager.md) | Typed client with Keychain/Keystore token storage, PKCE/Sanctum, and idempotent retries |
| Flutter mobile | [`project-boilerplate-mobile-flutter`](https://github.com/liberusoftware/project-boilerplate-mobile-flutter) | [Flutter plan](../flutter/module-manager.md) | Typed Dart DTOs and platform-secure credentials on iOS and Android |
| Dart mobile & desktop | [`project-boilerplate-dart-mobile`](https://github.com/liberusoftware/project-boilerplate-dart-mobile) · [`project-boilerplate-dart-desktop`](https://github.com/liberusoftware/project-boilerplate-dart-desktop) | [Flutter & Dart plan](../flutter/module-manager.md) | Separate mobile and desktop native hosts consuming the same versioned `/api/v1` contract |

### Feature-to-API capability and operation matrix

| Feature / aspect | HTTP query and command intent | DTO allowlist, concurrency, and error contract |
| --- | --- | --- |
| **Manifest discovery** | Expose authorized query/read projection and explicit domain transition command for `manifest discovery` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Dependency resolution** | Expose authorized query/read projection and explicit domain transition command for `dependency resolution` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Enablement** | Expose authorized query/read projection and explicit domain transition command for `enablement` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Lifecycle** | Expose authorized query/read projection and explicit domain transition command for `lifecycle` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Compatibility** | Expose authorized query/read projection and explicit domain transition command for `compatibility` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Registry caching** | Expose authorized query/read projection and explicit domain transition command for `registry caching` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Diagnostics** | Expose authorized query/read projection and explicit domain transition command for `diagnostics` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |

| Boundary | Observed identity and implementation reference |
| --- | --- |
| Source package | [liberusoftware/module-manager](../../../modules/source/liberusoftware--module-manager.md) |

### Observed route declarations

These are literal excerpts, not runnable standalone route files or expanded final URLs. Read group middleware/prefixes, provider loading and the host route configuration together. Authentication middleware alone does not establish the controller/domain permission policy.

[modules/module-manager-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/module-manager-api/routes/api.php)

```php
Route::prefix('api/v1/module-manager')->middleware('api')->group(function (): void {
Route::get('/status', StatusController::class)->name('module-manager-api.status');
```

A client example is valid only after its exact request/response contract is established. Record required/nullable fields, business units, allowed values, operation identity/concurrency support, result/pagination envelope and recovery. An `Idempotency-Key` or `If-Match` example does not establish server support by itself.

## 4. OpenAPI schema

No machine-readable schema file was found in the indexed `openapi/` or `schemas/` roots of the matched packages. Define a reviewed fragment from the actual public operations; a capability list or unrestricted `attributes` object is not a complete request contract. Application-owned or differently located contracts may need separate mapping.

For the target contract, define stable operation IDs, explicit request/resource/collection/error schemas, allowed audiences/scopes, actor/tenant resolution, field sensitivity, pagination/filter limits, concurrency and retry semantics. Use the real manifest identity and actual route namespace, not a guessed repository-derived package or path.

Validate/bundle the fragment, check supported-version compatibility and generate clients only from the reviewed contract. Retain the source/schema commit or release in client compatibility notes. See the [API architecture](../../../architecture/API.md), [source mapping](../SOURCE-MAPPING.md#module-manager), and [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) guides.

<!-- observed-api-contract:end -->
