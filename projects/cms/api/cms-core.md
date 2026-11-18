# CMS: CMS Core API

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-core). Observed identity: [`liberusoftware/module-cms-core-api`](../../../modules/source/liberusoftware--module-cms-core-api.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one API module specification

**Proposed API design identifier:** `module-cms-core-api`
**Matching domain module:** `cms-core`
**Application:** CMS
**Source feature:** [CMS Core](../features/cms-core.md)
**Architecture:** [API.md](../../../architecture/API.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional API presentation package exposes approved HTTP operations for the CMS Core domain module. It presents exactly one independent module, delegates all authoritative behavior to that module's public actions/queries/policies, and contains no other module's API logic.

The domain capability includes:

- Sites
- Channels
- Content identity
- Aliases
- Ownership
- Shared terminology
- Settings
- Domain events

Installation does not expose every capability automatically. The host application selects this package, API version, audiences, route groups, and operations in its API manifest.

## 2. Contract design

- Publish an OpenAPI 3.1 fragment with stable operation IDs, schemas, examples, scopes, errors, pagination, rate limits, idempotency, and deprecation metadata.
- Choose the route namespace through the host's reviewed API contract; observed source prefixes below take precedence over repository/design-name guesses.
- Represent resources through explicit API DTOs/resources rather than automatic Eloquent serialization.
- Use lowercase kebab-case paths, snake_case JSON fields, opaque identifiers, ISO 8601 timestamps, explicit money objects, and RFC 9457 Problem Details errors.
- Compatible additions remain within the major version; removals or semantic breaks require a new major version or approved migration path.

## 3. Endpoint examples

**Contract status:** use the observed source below for current route/handler/schema evidence. The surrounding module scope is a target design; its feature labels are not request field names. Do not generate a create/update/delete payload or final URL by mechanically copying the design identifier.

### Product API backend and client integration

This module API adapter is composed into [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api), the shared Laravel HTTP backend for independent web, mobile, and desktop clients ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [repository map](../../REPOSITORIES.md#laravel-applications)).

| Consuming client surface | Host repository | Module adapter plan | Transport and auth contract |
| --- | --- | --- | --- |
| Next.js React | [`project-cms-next-react`](https://github.com/liberusoftware/project-cms-next-react) | [Next.js plan](../nextjs/cms-core.md) | Server Component / Route Handler / BFF or Sanctum SPA with `no-store` private reads |
| Nuxt 4 Vue | [`project-cms-nuxt-vue`](https://github.com/liberusoftware/project-cms-nuxt-vue) | [Nuxt plan](../nuxt/cms-core.md) | Nitro SSR / BFF or Sanctum SPA with actor/tenant-scoped `useFetch` keys |
| React Native Expo | [`project-cms-mobile-react`](https://github.com/liberusoftware/project-cms-mobile-react) | [React Native plan](../react-native/cms-core.md) | Typed client with Keychain/Keystore token storage, PKCE/Sanctum, and idempotent retries |
| Flutter mobile | [`project-cms-mobile-flutter`](https://github.com/liberusoftware/project-cms-mobile-flutter) | [Flutter plan](../flutter/cms-core.md) | Typed Dart DTOs and platform-secure credentials on iOS and Android |
| Dart mobile & desktop | [`project-cms-dart-mobile`](https://github.com/liberusoftware/project-cms-dart-mobile) · [`project-cms-dart-desktop`](https://github.com/liberusoftware/project-cms-dart-desktop) | [Flutter & Dart plan](../flutter/cms-core.md) | Separate mobile and desktop native hosts consuming the same versioned `/api/v1` contract |

### Feature-to-API capability and operation matrix

| Feature / aspect | HTTP query and command intent | DTO allowlist, concurrency, and error contract |
| --- | --- | --- |
| **Sites** | Expose authorized query/read projection and explicit domain transition command for `sites` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Channels** | Expose authorized query/read projection and explicit domain transition command for `channels` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Content identity** | Expose authorized query/read projection and explicit domain transition command for `content identity` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Aliases** | Expose authorized query/read projection and explicit domain transition command for `aliases` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Ownership** | Expose authorized query/read projection and explicit domain transition command for `ownership` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Shared terminology** | Expose authorized query/read projection and explicit domain transition command for `shared terminology` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Settings** | Expose authorized query/read projection and explicit domain transition command for `settings` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Domain events** | Expose authorized query/read projection and explicit domain transition command for `domain events` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |

| Boundary | Observed identity and implementation reference |
| --- | --- |
| Source package | [liberusoftware/module-cms-core-api](../../../modules/source/liberusoftware--module-cms-core-api.md) |
| Source package | [liberusoftware/module-cms-core](../../../modules/source/liberusoftware--module-cms-core.md) |

No route file was established under the matched module roots for this spelling. That is a source-location observation, not proof that the capability has no API or UI. Review application-owned routes and the public domain boundary before proposing HTTP commands.

### Observed controller entry points

The signatures identify request handlers to review; their argument names are not complete JSON schemas. Read their request validation, actor/tenant resolution, policy, serialization and error paths before writing a client.

| Controller source | Public handler signatures |
| --- | --- |
| [CoreApiController.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-core-api/src/Http/Controllers/CoreApiController.php) | `public function __construct( private CoreQueryService $queries, private CoreMutationService $mutations, )`<br>`public function createSite(Request $request): JsonResponse`<br>`public function createChannel(Request $request, string $site): JsonResponse`<br>`public function sites(): AnonymousResourceCollection`<br>`public function site(string $site): CoreSiteResource`<br>`public function channels(string $site): AnonymousResourceCollection`<br>`public function alias(string $site, string $alias): CoreAliasResource`<br>`public function aliases(string $site): AnonymousResourceCollection`<br>`public function identities(string $site): AnonymousResourceCollection`<br>`public function updateSite(Request $request, string $site): CoreSiteResource`<br>`public function destroySite(string $site): JsonResponse`<br>`public function updateChannel(Request $request, string $site, string $channel): CoreChannelResource`<br>`public function destroyChannel(string $site, string $channel): JsonResponse`<br>`public function createIdentity(Request $request, string $site): JsonResponse`<br>`public function createAlias(Request $request, string $site): JsonResponse`<br>`public function settings(string $site): AnonymousResourceCollection`<br>`public function putSetting(Request $request, string $site, string $key): CoreSettingResource` |

### Observed domain queries, actions, and storage models

API controllers delegate to these observed core domain entry points and serialize only allowlisted DTO fields rather than raw storage models.

| Core query source | Observed signatures |
| --- | --- |
| [CoreQueryService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Queries/CoreQueryService.php) | `public function sites(int $perPage = 15, string $search = ''): LengthAwarePaginator`<br>`public function site(string $key): ?Site`<br>`public function channels(string $siteKey, int $perPage = 15, string $search = ''): LengthAwarePaginator`<br>`public function alias(string $siteKey, string $alias): ?ContentAlias`<br>`public function aliases(string $siteKey, int $perPage = 15): LengthAwarePaginator`<br>`public function identities(string $siteKey, int $perPage = 15): LengthAwarePaginator`<br>`public function settings(string $siteKey, int $perPage = 15, string $environment = 'production'): LengthAwarePaginator` |

| Core action / service source | Observed signatures |
| --- | --- |
| [CoreMutationService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Actions/CoreMutationService.php) | `public function createSite(array $attributes): Site`<br>`public function createChannel(Site\|int\|string $site, array $attributes): Channel`<br>`public function updateSite(Site $site, array $attributes): Site`<br>`public function updateChannel(Channel $channel, array $attributes): Channel`<br>`public function deleteSite(Site $site): void`<br>`public function deleteChannel(Channel $channel): void`<br>`public function createIdentity(Site\|int\|string $site, array $attributes): ContentIdentity`<br>`public function createAlias(Site\|int\|string $site, array $attributes): ContentAlias`<br>`public function putSetting(?Site $site, string $key, array $value, string $environment = 'production'): Setting` |

| Core storage model | Observed fillable fields (review for DTO allowlist) |
| --- | --- |
| [Channel.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Models/Channel.php) | `site_id`, `key`, `name`, `type`, `settings`, `team_id` |
| [ContentAlias.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Models/ContentAlias.php) | `site_id`, `channel_id`, `alias`, `target_type`, `target_id`, `redirect_status`, `team_id` |
| [ContentIdentity.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Models/ContentIdentity.php) | `site_id`, `channel_id`, `content_type`, `content_id`, `canonical_path`, `status`, `owner_type`, `owner_id`, `metadata`, `team_id` |
| [Setting.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Models/Setting.php) | `site_id`, `key`, `value`, `environment` |
| [Site.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-core/src/Models/Site.php) | `key`, `name`, `domain`, `default_locale`, `timezone`, `status`, `settings`, `team_id` |

A client example is valid only after its exact request/response contract is established. Record required/nullable fields, business units, allowed values, operation identity/concurrency support, result/pagination envelope and recovery. An `Idempotency-Key` or `If-Match` example does not establish server support by itself.

## 4. OpenAPI schema

No machine-readable schema file was found in the indexed `openapi/` or `schemas/` roots of the matched packages. Define a reviewed fragment from the actual public operations; a capability list or unrestricted `attributes` object is not a complete request contract. Application-owned or differently located contracts may need separate mapping.

For the target contract, define stable operation IDs, explicit request/resource/collection/error schemas, allowed audiences/scopes, actor/tenant resolution, field sensitivity, pagination/filter limits, concurrency and retry semantics. Use the real manifest identity and actual route namespace, not a guessed repository-derived package or path.

Validate/bundle the fragment, check supported-version compatibility and generate clients only from the reviewed contract. Retain the source/schema commit or release in client compatibility notes. See the [API architecture](../../../architecture/API.md), [source mapping](../SOURCE-MAPPING.md#cms-core), and [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) guides.

## 5. Audience and operation matrix

| Audience                       | Default exposure                    | Required controls                                                                      |
| ------------------------------ | ----------------------------------- | -------------------------------------------------------------------------------------- |
| Public/anonymous               | Disabled unless explicitly required | Enumeration resistance, strict rate limits, field minimization, abuse controls         |
| Authenticated customer/partner | Explicit allowlist                  | Tenant/resource ownership, purpose-specific scopes, field policy                       |
| Staff/administrator            | Explicit allowlist                  | Role/permission policy, tenant context, recent authentication for risky actions, audit |
| Service/integration client     | Explicit allowlist                  | Service identity, least-privilege scopes, expiry/rotation, idempotency, quotas         |

Every exposed operation must map to one audience, domain query/action, permission/scope, request/response schema, rate limit, idempotency/concurrency policy, audit event, and test set. Unmapped operations fail CI.

## 6. Implementation strategy

- Keep routes, controllers/handlers, requests, API resources, OpenAPI fragments, and transport tests in this API package.
- Validate shape at the request boundary and enforce authoritative invariants again in the domain action.
- Resolve tenant and actor context from trusted authentication/application routing; never grant context from a caller-supplied tenant identifier alone.
- Authorize field visibility as well as record/action access, and return concealment-safe errors where enumeration is a risk.
- Use idempotency keys for retryable writes, ETags/`If-Match` for relevant concurrent updates, and asynchronous operation resources for slow/bulk/provider-dependent work.
- Compose cross-module workflows in the application layer; do not query or mutate another module's private storage from this API package.

## 7. Security, resilience, and observability

- Threat-model authentication, authorization, tenant isolation, mass assignment, object references, abusive queries, uploads/downloads, webhooks, and sensitive data.
- Bound pagination, filters, includes, payloads, batch sizes, timeouts, and retry budgets.
- Redact credentials and protected data from logs and errors while recording request, correlation, API/module/version, tenant, principal, operation, status, latency, rate-limit, and idempotency outcomes.
- Define availability, latency, error-rate and queued-operation objectives plus alerts and recovery/reconciliation runbooks.

## 8. Verification strategy

- Lint OpenAPI, validate examples, detect implementation drift and breaking changes, and reject path/schema/operation-ID collisions during application aggregation.
- Test every operation for allowed, unauthenticated, wrong-tenant, insufficient-scope, insufficient-permission, hidden-field, invalid, missing, duplicate, stale, concurrent, throttled, and failure/recovery paths as applicable.
- Test pagination, filtering, sorting, includes, dates, money, identifiers, enums, idempotency, ETags, async operations, bulk partial failure, and stable Problem Details.
- Add one-to-one architecture tests proving this package depends on and presents only `cms-core`.
- Run independent installation, minimum/current compatibility, security, performance, generated-client smoke, and representative host-composition tests.
- Run Pest 5 with meaningful owned PHP targeting 100% line coverage; coverage complements contract, mutation, security, and failure assertions.

## 9. Definition of done

- The package name, manifest, Composer dependency, namespace, route prefix, and OpenAPI ownership all match `cms-core`.
- The audience/operation matrix is complete, least-privilege, documented, and enforced in CI.
- Schemas, implementation, examples, errors, SDK/client evidence, and documentation agree.
- Authorization, tenant/field isolation, idempotency/concurrency, limits, audit, observability, compatibility, and recovery tests pass.
- The API fragment aggregates without collisions and the independent package can be installed, tested, versioned, upgraded, and removed safely.
