# CRM: Case Management API

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#case-management). Observed identity: [`liberusoftware/module-crm-case-management-api`](../../../modules/source/liberusoftware--module-crm-case-management-api.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one API module specification

**Proposed API design identifier:** `module-crm-case-management-api`
**Matching domain module:** `crm-case-management`
**Application:** CRM
**Source feature:** [Case Management](../features/case-management.md)
**Architecture:** [API.md](../../../architecture/API.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional API presentation package exposes approved HTTP operations for the Case Management domain module. It presents exactly one independent module, delegates all authoritative behavior to that module's public actions/queries/policies, and contains no other module's API logic.

The domain capability includes:

- Tickets/cases
- Types
- Pipelines
- Statuses
- Priorities
- Ownership
- Parent/child cases
- Related assets/orders
- Entitlements
- Escalation
- Audit

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

This module API adapter is composed into [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api), the shared Laravel HTTP backend for independent web, mobile, and desktop clients ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [repository map](../../REPOSITORIES.md#laravel-applications)).

| Consuming client surface | Host repository | Module adapter plan | Transport and auth contract |
| --- | --- | --- | --- |
| Next.js React | [`project-crm-next-react`](https://github.com/liberusoftware/project-crm-next-react) | [Next.js plan](../nextjs/case-management.md) | Server Component / Route Handler / BFF or Sanctum SPA with `no-store` private reads |
| Nuxt 4 Vue | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | [Nuxt plan](../nuxt/case-management.md) | Nitro SSR / BFF or Sanctum SPA with actor/tenant-scoped `useFetch` keys |
| React Native Expo | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | [React Native plan](../react-native/case-management.md) | Typed client with Keychain/Keystore token storage, PKCE/Sanctum, and idempotent retries |
| Flutter mobile | [`project-crm-mobile-flutter`](https://github.com/liberusoftware/project-crm-mobile-flutter) | [Flutter plan](../flutter/case-management.md) | Typed Dart DTOs and platform-secure credentials on iOS and Android |
| Dart mobile & desktop | [`project-crm-dart-mobile`](https://github.com/liberusoftware/project-crm-dart-mobile) · [`project-crm-dart-desktop`](https://github.com/liberusoftware/project-crm-dart-desktop) | [Flutter & Dart plan](../flutter/case-management.md) | Separate mobile and desktop native hosts consuming the same versioned `/api/v1` contract |

### Feature-to-API capability and operation matrix

| Feature / aspect | HTTP query and command intent | DTO allowlist, concurrency, and error contract |
| --- | --- | --- |
| **Tickets/cases** | Expose authorized query/read projection and explicit domain transition command for `tickets/cases` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Types** | Expose authorized query/read projection and explicit domain transition command for `types` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Pipelines** | Expose authorized query/read projection and explicit domain transition command for `pipelines` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Statuses** | Expose authorized query/read projection and explicit domain transition command for `statuses` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Priorities** | Expose authorized query/read projection and explicit domain transition command for `priorities` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Ownership** | Expose authorized query/read projection and explicit domain transition command for `ownership` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Parent/child cases** | Expose authorized query/read projection and explicit domain transition command for `parent/child cases` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Related assets/orders** | Expose authorized query/read projection and explicit domain transition command for `related assets/orders` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Entitlements** | Expose authorized query/read projection and explicit domain transition command for `entitlements` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Escalation** | Expose authorized query/read projection and explicit domain transition command for `escalation` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Audit** | Expose authorized query/read projection and explicit domain transition command for `audit` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |

| Boundary | Observed identity and implementation reference |
| --- | --- |
| Source package | [liberusoftware/module-crm-case-management-api](../../../modules/source/liberusoftware--module-crm-case-management-api.md) |
| Source package | [liberusoftware/module-crm-case-management](../../../modules/source/liberusoftware--module-crm-case-management.md) |

### Observed route declarations

These are literal excerpts, not runnable standalone route files or expanded final URLs. Read group middleware/prefixes, provider loading and the host route configuration together. Authentication middleware alone does not establish the controller/domain permission policy.

[modules/crm-case-management-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-case-management-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/case-management')->group(function (): void {
Route::get('cases', [CaseManagementController::class, 'index']);
Route::post('cases', [CaseManagementController::class, 'store']);
Route::post('cases/{case}/transition', [CaseManagementController::class, 'transition']);
Route::get('queue', [CaseManagementController::class, 'queue']);
```

### Observed controller entry points

The signatures identify request handlers to review; their argument names are not complete JSON schemas. Read their request validation, actor/tenant resolution, policy, serialization and error paths before writing a client.

| Controller source | Public handler signatures |
| --- | --- |
| [CaseManagementController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-case-management-api/src/Http/Controllers/CaseManagementController.php) | `public function __construct(private readonly CaseQuery $query)`<br>`public function index(Request $request): JsonResponse`<br>`public function store(Request $request, OpenCase $a): JsonResponse`<br>`public function transition(Request $request, CaseRecord $case, TransitionCase $a): JsonResponse`<br>`public function queue(Request $request): JsonResponse` |

### Observed domain queries, actions, and storage models

API controllers delegate to these observed core domain entry points and serialize only allowlisted DTO fields rather than raw storage models.

| Core query source | Observed signatures |
| --- | --- |
| [CaseQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-case-management/src/Queries/CaseQuery.php) | `public function cases(int $teamId): Builder`<br>`public function queue(int $teamId, string $status = 'open'): Builder` |

| Core action / service source | Observed signatures |
| --- | --- |
| [OpenCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-case-management/src/Actions/OpenCase.php) | `public function execute(int $teamId, int $ownerId, array $input): CaseRecord` |
| [TransitionCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-case-management/src/Actions/TransitionCase.php) | `public function execute(int $teamId, int $actorId, CaseRecord $case, string $status, ?int $ownerId = null): CaseRecord` |

| Core storage model | Observed fillable fields (review for DTO allowlist) |
| --- | --- |
| [CaseAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-case-management/src/Models/CaseAudit.php) | No literal fillable array detected; inspect the model and API schema. |
| [CaseRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-case-management/src/Models/CaseRecord.php) | No literal fillable array detected; inspect the model and API schema. |

A client example is valid only after its exact request/response contract is established. Record required/nullable fields, business units, allowed values, operation identity/concurrency support, result/pagination envelope and recovery. An `Idempotency-Key` or `If-Match` example does not establish server support by itself.

## 4. OpenAPI schema

No machine-readable schema file was found in the indexed `openapi/` or `schemas/` roots of the matched packages. Define a reviewed fragment from the actual public operations; a capability list or unrestricted `attributes` object is not a complete request contract. Application-owned or differently located contracts may need separate mapping.

For the target contract, define stable operation IDs, explicit request/resource/collection/error schemas, allowed audiences/scopes, actor/tenant resolution, field sensitivity, pagination/filter limits, concurrency and retry semantics. Use the real manifest identity and actual route namespace, not a guessed repository-derived package or path.

Validate/bundle the fragment, check supported-version compatibility and generate clients only from the reviewed contract. Retain the source/schema commit or release in client compatibility notes. See the [API architecture](../../../architecture/API.md), [source mapping](../SOURCE-MAPPING.md#case-management), and [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) guides.

## 5. Audience and operation matrix

Expose only explicitly selected operations. Anonymous access is disabled unless the owning capability requires it; customer/partner reads and commands use record/tenant scope, staff actions use the relevant policy, and integrations use a narrow service identity. UI visibility and authentication alone do not establish authorization.

## 6. Implementation strategy

Resolve trusted actor/tenant context, validate the reviewed request and delegate to the public owning action/query. Serialize explicit authorized DTOs; preserve documented operation identity, concurrency and error semantics. Reuse existing owner APIs instead of copying their records or private model access.

## 7. Security, resilience, and observability

Apply record/field policy to lists, relationships, commands, bulk work, jobs and downloads. Use bounded retries/timeouts, durable operation/source references and explicit partial-failure recovery. Redact credentials/protected data while retaining safe request/correlation diagnostics.

## 8. Verification strategy

Verify actual route/schema parity, required input, allowed/denied/wrong-tenant requests, stale/duplicate commands, uncertain outcomes, pagination/field policy and affected owner integrations. Check the declared package/host scripts and supported versions; source/test presence is not a passing-run claim.

## 9. Definition of done

Release only after the complete reviewed request/response/error contract, version compatibility, security and owner invariants, consumer integration, migrations where owned, and operational recovery are verified. Document the actual package identity and source/release evidence in its README and changelog.
