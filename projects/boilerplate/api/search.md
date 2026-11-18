# Boilerplate: Search API presentation packages

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#search). Observed identity: [`liberusoftware/search-api`](../../../modules/source/liberusoftware--search-api.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Design package identifier:** `module-search-api`
**Matching core package:** [`module-search`](../core/search.md)
**Foundation specification:** [BOILERPLATE.md](../BOILERPLATE.md)
**Capability:** Authorized indexing, search contracts, filters, pagination, reindexing, and provider adapters.

## Adapter implementation plan

This package presents the Search core capability through API. It owns routes, resources, components, pages, hooks, forms, tables, or client state appropriate to this layer, but does not recreate domain rules, persistence, authorization, or provider integrations.

- Depend on the matching core package and call its typed actions, queries, policies, and resource DTOs through public contracts.
- Preserve tenant/team context, authorization, field visibility, validation, localization, timezone/currency behavior, accessibility, and safe error/recovery states.
- Publish versioned OpenAPI 3.1 schemas, operation IDs, scopes, pagination, rate limits, idempotency, concurrency, and RFC 9457 Problem Details.
- Add adapter contract tests for allowed and denied access, wrong tenant, validation, hidden fields, empty states, failures, retries, and compatibility with the core package.

## Scope

The package is optional and installable independently. Applications may omit it, replace it with another presentation adapter, or compose it with a custom theme while retaining the same Search core boundary.

<!-- observed-api-contract:start -->
## 3. Endpoint examples

**Contract status:** use the observed source below for current route/handler/schema evidence. The surrounding module scope is a target design; its feature labels are not request field names. Do not generate a create/update/delete payload or final URL by mechanically copying the design identifier.

### Product API backend and client integration

This module API adapter is composed into [`project-boilerplate-laravel-api`](https://github.com/liberusoftware/project-boilerplate-laravel-api), the shared Laravel HTTP backend for independent web, mobile, and desktop clients ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [repository map](../../REPOSITORIES.md#laravel-applications)).

| Consuming client surface | Host repository | Module adapter plan | Transport and auth contract |
| --- | --- | --- | --- |
| Next.js React | [`project-boilerplate-next-react`](https://github.com/liberusoftware/project-boilerplate-next-react) | [Next.js plan](../nextjs/search.md) | Server Component / Route Handler / BFF or Sanctum SPA with `no-store` private reads |
| Nuxt 4 Vue | [`project-boilerplate-nuxt-vue`](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) | [Nuxt plan](../nuxt/search.md) | Nitro SSR / BFF or Sanctum SPA with actor/tenant-scoped `useFetch` keys |
| React Native Expo | [`project-boilerplate-mobile-react`](https://github.com/liberusoftware/project-boilerplate-mobile-react) | [React Native plan](../react-native/search.md) | Typed client with Keychain/Keystore token storage, PKCE/Sanctum, and idempotent retries |
| Flutter mobile | [`project-boilerplate-mobile-flutter`](https://github.com/liberusoftware/project-boilerplate-mobile-flutter) | [Flutter plan](../flutter/search.md) | Typed Dart DTOs and platform-secure credentials on iOS and Android |
| Dart mobile & desktop | [`project-boilerplate-dart-mobile`](https://github.com/liberusoftware/project-boilerplate-dart-mobile) · [`project-boilerplate-dart-desktop`](https://github.com/liberusoftware/project-boilerplate-dart-desktop) | [Flutter & Dart plan](../flutter/search.md) | Separate mobile and desktop native hosts consuming the same versioned `/api/v1` contract |

### Feature-to-API capability and operation matrix

| Feature / aspect | HTTP query and command intent | DTO allowlist, concurrency, and error contract |
| --- | --- | --- |
| **Authorized indexing** | Expose authorized query/read projection and explicit domain transition command for `authorized indexing` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Search contracts** | Expose authorized query/read projection and explicit domain transition command for `search contracts` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Filters** | Expose authorized query/read projection and explicit domain transition command for `filters` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Pagination** | Expose authorized query/read projection and explicit domain transition command for `pagination` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Reindexing** | Expose authorized query/read projection and explicit domain transition command for `reindexing` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Provider adapters** | Expose authorized query/read projection and explicit domain transition command for `provider adapters` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |

| Boundary | Observed identity and implementation reference |
| --- | --- |
| Source package | [liberusoftware/search-api](../../../modules/source/liberusoftware--search-api.md) |
| Source package | [liberusoftware/search](../../../modules/source/liberusoftware--search.md) |

### Observed route declarations

These are literal excerpts, not runnable standalone route files or expanded final URLs. Read group middleware/prefixes, provider loading and the host route configuration together. Authentication middleware alone does not establish the controller/domain permission policy.

[modules/search-api/routes/api.php](https://github.com/liberusoftware/project-boilerplate-laravel-filament/blob/3ade34046c3de1e2f0fc8e498a2451241c0584dc/modules/search-api/routes/api.php)

```php
Route::prefix('api/search')->name('search.')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function () {
Route::get('/users', [SearchController::class, 'users'])->name('users');
Route::get('/all', [SearchController::class, 'all'])->name('all');
```

### Observed controller entry points

The signatures identify request handlers to review; their argument names are not complete JSON schemas. Read their request validation, actor/tenant resolution, policy, serialization and error paths before writing a client.

| Controller source | Public handler signatures |
| --- | --- |
| [SearchController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/search-api/src/Http/Controllers/SearchController.php) | `public function __construct(SearchService $searchService, SearcherRegistry $searchers)`<br>`public function users(Request $request): JsonResponse`<br>`public function all(Request $request): JsonResponse` |

### Observed domain queries, actions, and storage models

API controllers delegate to these observed core domain entry points and serialize only allowlisted DTO fields rather than raw storage models.

| Core action / service source | Observed signatures |
| --- | --- |
| [SearchIndexer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/search/src/Contracts/SearchIndexer.php) | `public function index(string $type, Model $record): void`<br>`public function remove(string $type, string\|int $id): void`<br>`public function flush(string $type): void` |
| [LocalSearchIndexer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/search/src/Services/LocalSearchIndexer.php) | `public function index(string $type, Model $record): void`<br>`public function remove(string $type, string\|int $id): void`<br>`public function flush(string $type): void` |
| [SearchService.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/search/src/Services/SearchService.php) | `public function __construct(private readonly SearcherRegistry $searchers)`<br>`public function searchUsers(array $filters): LengthAwarePaginator`<br>`public function searchAll(array $filters): array` |

A client example is valid only after its exact request/response contract is established. Record required/nullable fields, business units, allowed values, operation identity/concurrency support, result/pagination envelope and recovery. An `Idempotency-Key` or `If-Match` example does not establish server support by itself.

## 4. OpenAPI schema

No machine-readable schema file was found in the indexed `openapi/` or `schemas/` roots of the matched packages. Define a reviewed fragment from the actual public operations; a capability list or unrestricted `attributes` object is not a complete request contract. Application-owned or differently located contracts may need separate mapping.

For the target contract, define stable operation IDs, explicit request/resource/collection/error schemas, allowed audiences/scopes, actor/tenant resolution, field sensitivity, pagination/filter limits, concurrency and retry semantics. Use the real manifest identity and actual route namespace, not a guessed repository-derived package or path.

Validate/bundle the fragment, check supported-version compatibility and generate clients only from the reviewed contract. Retain the source/schema commit or release in client compatibility notes. See the [API architecture](../../../architecture/API.md), [source mapping](../SOURCE-MAPPING.md#search), and [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) guides.

<!-- observed-api-contract:end -->
