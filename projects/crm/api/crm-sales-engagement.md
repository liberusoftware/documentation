# CRM: Crm Sales Engagement API

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-sales-engagement). Observed identity: [`liberusoftware/module-crm-sales-engagement-api`](../../../modules/source/liberusoftware--module-crm-sales-engagement-api.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one API module specification

**Proposed API design identifier:** `module-crm-crm-sales-engagement-api`<br>
**Matching domain module:** `crm-sales-engagement`  
**Application:** CRM  
**Source feature:** [Crm Sales Engagement](../features/crm-sales-engagement.md)  
**Architecture:** [API.md](../../../architecture/API.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional API presentation package exposes approved HTTP operations for the Crm Sales Engagement domain module. It presents exactly one independent module, delegates all authoritative behavior to that module's public actions/queries/policies, and contains no other module's API logic.

The domain capability includes:

- Sequences/cadences
- Multi-channel steps
- Templates/snippets
- Task queues
- Enrollment/re-entry
- Throttles
- Timezone windows
- Reply/meeting stop rules
- Experiments

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
| Next.js React | [`project-crm-next-react`](https://github.com/liberusoftware/project-crm-next-react) | [Next.js plan](../nextjs/crm-sales-engagement.md) | Server Component / Route Handler / BFF or Sanctum SPA with `no-store` private reads |
| Nuxt 4 Vue | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | [Nuxt plan](../nuxt/crm-sales-engagement.md) | Nitro SSR / BFF or Sanctum SPA with actor/tenant-scoped `useFetch` keys |
| React Native Expo | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | [React Native plan](../react-native/crm-sales-engagement.md) | Typed client with Keychain/Keystore token storage, PKCE/Sanctum, and idempotent retries |
| Flutter mobile | [`project-crm-mobile-flutter`](https://github.com/liberusoftware/project-crm-mobile-flutter) | [Flutter plan](../flutter/crm-sales-engagement.md) | Typed Dart DTOs and platform-secure credentials on iOS and Android |
| Dart mobile & desktop | [`project-crm-dart-mobile`](https://github.com/liberusoftware/project-crm-dart-mobile) · [`project-crm-dart-desktop`](https://github.com/liberusoftware/project-crm-dart-desktop) | [Flutter & Dart plan](../flutter/crm-sales-engagement.md) | Separate mobile and desktop native hosts consuming the same versioned `/api/v1` contract |

### Feature-to-API capability and operation matrix

| Feature / aspect | HTTP query and command intent | DTO allowlist, concurrency, and error contract |
| --- | --- | --- |
| **Sequences/cadences** | Expose authorized query/read projection and explicit domain transition command for `sequences/cadences` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Multi-channel steps** | Expose authorized query/read projection and explicit domain transition command for `multi-channel steps` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Templates/snippets** | Expose authorized query/read projection and explicit domain transition command for `templates/snippets` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Task queues** | Expose authorized query/read projection and explicit domain transition command for `task queues` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Enrollment/re-entry** | Expose authorized query/read projection and explicit domain transition command for `enrollment/re-entry` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Throttles** | Expose authorized query/read projection and explicit domain transition command for `throttles` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Timezone windows** | Expose authorized query/read projection and explicit domain transition command for `timezone windows` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Reply/meeting stop rules** | Expose authorized query/read projection and explicit domain transition command for `reply/meeting stop rules` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Experiments** | Expose authorized query/read projection and explicit domain transition command for `experiments` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |

| Boundary | Observed identity and implementation reference |
| --- | --- |
| Source package | [liberusoftware/module-crm-sales-engagement-api](../../../modules/source/liberusoftware--module-crm-sales-engagement-api.md) |
| Source package | [liberusoftware/module-crm-sales-engagement](../../../modules/source/liberusoftware--module-crm-sales-engagement.md) |

### Observed route declarations

These are literal excerpts, not runnable standalone route files or expanded final URLs. Read group middleware/prefixes, provider loading and the host route configuration together. Authentication middleware alone does not establish the controller/domain permission policy.

[modules/crm-sales-engagement-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/sales-engagement')->group(function (): void {
Route::get('/sequences', [EngagementController::class, 'sequences']);
Route::post('/sequences', [EngagementController::class, 'sequence']);
Route::post('/steps', [EngagementController::class, 'step']);
Route::get('/enrollments', [EngagementController::class, 'enrollments']);
Route::post('/enrollments', [EngagementController::class, 'enroll']);
Route::post('/enrollments/{enrollment}/stop/{reason}', [EngagementController::class, 'stop']);
Route::get('/tasks', [EngagementController::class, 'tasks']);
Route::post('/tasks/{task}/complete', [EngagementController::class, 'complete']);
Route::post('/events', [EngagementController::class, 'event']);
```

### Observed controller entry points

The signatures identify request handlers to review; their argument names are not complete JSON schemas. Read their request validation, actor/tenant resolution, policy, serialization and error paths before writing a client.

| Controller source | Public handler signatures |
| --- | --- |
| [EngagementController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement-api/src/Http/Controllers/EngagementController.php) | `public function sequences(Request $r, EngagementQuery $q)`<br>`public function sequence(Request $r, CreateSequence $a)`<br>`public function step(Request $r, AddStep $a)`<br>`public function enrollments(Request $r, EngagementQuery $q)`<br>`public function enroll(Request $r, EnrollContact $a)`<br>`public function stop(Request $r, int $enrollment, string $reason, StopEnrollment $a)`<br>`public function tasks(Request $request, EngagementQuery $query)`<br>`public function complete(Request $request, int $task, CompleteEngagementTask $action)`<br>`public function event(Request $r, RecordEngagementEvent $a)` |

### Observed domain queries, actions, and storage models

API controllers delegate to these observed core domain entry points and serialize only allowlisted DTO fields rather than raw storage models.

| Core query source | Observed signatures |
| --- | --- |
| [EngagementQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Queries/EngagementQuery.php) | `public function sequences(int $teamId)`<br>`public function enrollments(int $teamId)`<br>`public function tasks(int $teamId)` |

| Core action / service source | Observed signatures |
| --- | --- |
| [AddStep.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Actions/AddStep.php) | `public function execute(int $teamId, int $actorId, array $data): EngagementStep` |
| [CreateSequence.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Actions/CreateSequence.php) | `public function execute(int $teamId, int $actorId, array $data): EngagementSequence` |
| [EnrollContact.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Actions/EnrollContact.php) | `public function execute(int $teamId, int $actorId, array $data): Enrollment` |
| [RecordEngagementEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Actions/RecordEngagementEvent.php) | `public function execute(int $teamId, int $actorId, array $data): EngagementEvent` |
| [StopEnrollment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Actions/StopEnrollment.php) | `public function execute(int $teamId, int $actorId, int $id, string $reason): Enrollment` |
| [UpdateSequence.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Actions/UpdateSequence.php) | `public function execute(int $teamId, int $actorId, int $sequenceId, array $data): EngagementSequence` |
| [EngagementPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Services/EngagementPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Core storage model | Observed fillable fields (review for DTO allowlist) |
| --- | --- |
| [EngagementEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Models/EngagementEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [EngagementSequence.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Models/EngagementSequence.php) | No literal fillable array detected; inspect the model and API schema. |
| [EngagementStep.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Models/EngagementStep.php) | No literal fillable array detected; inspect the model and API schema. |
| [EngagementTask.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Models/EngagementTask.php) | No literal fillable array detected; inspect the model and API schema. |
| [Enrollment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Models/Enrollment.php) | No literal fillable array detected; inspect the model and API schema. |

A client example is valid only after its exact request/response contract is established. Record required/nullable fields, business units, allowed values, operation identity/concurrency support, result/pagination envelope and recovery. An `Idempotency-Key` or `If-Match` example does not establish server support by itself.

## 4. OpenAPI schema

The matched source contains these machine-readable contract/schema files. Verify their version and parity with handlers; file presence does not prove deployed compatibility or a passing validation run.

- [openapi/v1/crm-sales-engagement.yaml](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement-api/openapi/v1/crm-sales-engagement.yaml)

For the target contract, define stable operation IDs, explicit request/resource/collection/error schemas, allowed audiences/scopes, actor/tenant resolution, field sensitivity, pagination/filter limits, concurrency and retry semantics. Use the real manifest identity and actual route namespace, not a guessed repository-derived package or path.

Validate/bundle the fragment, check supported-version compatibility and generate clients only from the reviewed contract. Retain the source/schema commit or release in client compatibility notes. See the [API architecture](../../../architecture/API.md), [source mapping](../SOURCE-MAPPING.md#crm-sales-engagement), and [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) guides.

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
- Add one-to-one architecture tests proving this package depends on and presents only `crm-sales-engagement`.
- Run independent installation, minimum/current compatibility, security, performance, generated-client smoke, and representative host-composition tests.
- Run Pest 5 with meaningful owned PHP targeting 100% line coverage; coverage complements contract, mutation, security, and failure assertions.

## 9. Definition of done

- The package name, manifest, Composer dependency, namespace, route prefix, and OpenAPI ownership all match `crm-sales-engagement`.
- The audience/operation matrix is complete, least-privilege, documented, and enforced in CI.
- Schemas, implementation, examples, errors, SDK/client evidence, and documentation agree.
- Authorization, tenant/field isolation, idempotency/concurrency, limits, audit, observability, compatibility, and recovery tests pass.
- The API fragment aggregates without collisions and the independent package can be installed, tested, versioned, upgraded, and removed safely.
