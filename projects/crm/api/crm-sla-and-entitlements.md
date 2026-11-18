# CRM: Crm Sla And Entitlements API

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-sla-and-entitlements). Observed identity: [`liberusoftware/module-crm-sla-and-entitlements-api`](../../../modules/source/liberusoftware--module-crm-sla-and-entitlements-api.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one API module specification

**Proposed API design identifier:** `module-crm-crm-sla-and-entitlements-api`<br>
**Matching domain module:** `crm-sla-and-entitlements`  
**Application:** CRM  
**Source feature:** [Crm Sla And Entitlements](../features/crm-sla-and-entitlements.md)  
**Architecture:** [API.md](../../../architecture/API.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional API presentation package exposes approved HTTP operations for the Crm Sla And Entitlements domain module. It presents exactly one independent module, delegates all authoritative behavior to that module's public actions/queries/policies, and contains no other module's API logic.

The domain capability includes:

- Service contracts
- Coverage
- Business calendars
- Response/resolution targets
- Milestones
- Pauses
- Warnings
- Breaches
- Escalations
- Exceptions

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
| Next.js React | [`project-crm-next-react`](https://github.com/liberusoftware/project-crm-next-react) | [Next.js plan](../nextjs/crm-sla-and-entitlements.md) | Server Component / Route Handler / BFF or Sanctum SPA with `no-store` private reads |
| Nuxt 4 Vue | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | [Nuxt plan](../nuxt/crm-sla-and-entitlements.md) | Nitro SSR / BFF or Sanctum SPA with actor/tenant-scoped `useFetch` keys |
| React Native Expo | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | [React Native plan](../react-native/crm-sla-and-entitlements.md) | Typed client with Keychain/Keystore token storage, PKCE/Sanctum, and idempotent retries |
| Flutter mobile | [`project-crm-mobile-flutter`](https://github.com/liberusoftware/project-crm-mobile-flutter) | [Flutter plan](../flutter/crm-sla-and-entitlements.md) | Typed Dart DTOs and platform-secure credentials on iOS and Android |
| Dart mobile & desktop | [`project-crm-dart-mobile`](https://github.com/liberusoftware/project-crm-dart-mobile) · [`project-crm-dart-desktop`](https://github.com/liberusoftware/project-crm-dart-desktop) | [Flutter & Dart plan](../flutter/crm-sla-and-entitlements.md) | Separate mobile and desktop native hosts consuming the same versioned `/api/v1` contract |

### Feature-to-API capability and operation matrix

| Feature / aspect | HTTP query and command intent | DTO allowlist, concurrency, and error contract |
| --- | --- | --- |
| **Service contracts** | Expose authorized query/read projection and explicit domain transition command for `service contracts` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Coverage** | Expose authorized query/read projection and explicit domain transition command for `coverage` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Business calendars** | Expose authorized query/read projection and explicit domain transition command for `business calendars` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Response/resolution targets** | Expose authorized query/read projection and explicit domain transition command for `response/resolution targets` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Milestones** | Expose authorized query/read projection and explicit domain transition command for `milestones` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Pauses** | Expose authorized query/read projection and explicit domain transition command for `pauses` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Warnings** | Expose authorized query/read projection and explicit domain transition command for `warnings` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Breaches** | Expose authorized query/read projection and explicit domain transition command for `breaches` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Escalations** | Expose authorized query/read projection and explicit domain transition command for `escalations` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Exceptions** | Expose authorized query/read projection and explicit domain transition command for `exceptions` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |

| Boundary | Observed identity and implementation reference |
| --- | --- |
| Source package | [liberusoftware/module-crm-sla-and-entitlements-api](../../../modules/source/liberusoftware--module-crm-sla-and-entitlements-api.md) |
| Source package | [liberusoftware/module-crm-sla-and-entitlements](../../../modules/source/liberusoftware--module-crm-sla-and-entitlements.md) |

### Observed route declarations

These are literal excerpts, not runnable standalone route files or expanded final URLs. Read group middleware/prefixes, provider loading and the host route configuration together. Authentication middleware alone does not establish the controller/domain permission policy.

[modules/crm-sla-and-entitlements-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements-api/routes/api.php)

```php
Route::middleware(['auth:sanctum', 'throttle:api'])->prefix('api/v1/crm/sla-and-entitlements')->group(function (): void {
Route::get('/contracts', [SlaController::class, 'contracts']);
Route::post('/contracts', [SlaController::class, 'storeContract']);
Route::get('/calendars', [SlaController::class, 'calendars']);
Route::post('/calendars', [SlaController::class, 'storeCalendar']);
Route::get('/entitlements', [SlaController::class, 'entitlements']);
Route::post('/entitlements', [SlaController::class, 'storeEntitlement']);
Route::get('/cases', [SlaController::class, 'cases']);
Route::post('/cases', [SlaController::class, 'storeCase']);
Route::post('/cases/{case}/{transition}', [SlaController::class, 'transition'])->whereIn('transition', ['responded', 'pause', 'resume', 'resolve', 'close']);
Route::post('/cases/{case}/evaluate', [SlaController::class, 'evaluate']);
Route::post('/exceptions', [SlaController::class, 'exception']);
```

### Observed controller entry points

The signatures identify request handlers to review; their argument names are not complete JSON schemas. Read their request validation, actor/tenant resolution, policy, serialization and error paths before writing a client.

| Controller source | Public handler signatures |
| --- | --- |
| [SlaController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements-api/src/Http/Controllers/SlaController.php) | `public function contracts(Request $r, SlaQuery $q): JsonResponse`<br>`public function calendars(Request $r, SlaQuery $q): JsonResponse`<br>`public function entitlements(Request $r, SlaQuery $q): JsonResponse`<br>`public function cases(Request $r, SlaQuery $q): JsonResponse`<br>`public function storeContract(Request $r, CreateContract $a): JsonResponse`<br>`public function storeCalendar(Request $r, CreateCalendar $a): JsonResponse`<br>`public function storeEntitlement(Request $r, SetEntitlement $a): JsonResponse`<br>`public function storeCase(Request $r, OpenCase $a): JsonResponse`<br>`public function transition(Request $r, int $case, string $transition, TransitionCase $a): JsonResponse`<br>`public function evaluate(Request $r, int $case, EvaluateCase $a): JsonResponse`<br>`public function exception(Request $r, RequestException $a): JsonResponse` |

### Observed domain queries, actions, and storage models

API controllers delegate to these observed core domain entry points and serialize only allowlisted DTO fields rather than raw storage models.

| Core query source | Observed signatures |
| --- | --- |
| [SlaQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Queries/SlaQuery.php) | `public function contracts(int $teamId)`<br>`public function calendars(int $teamId)`<br>`public function entitlements(int $teamId)`<br>`public function cases(int $teamId)`<br>`public function escalations(int $teamId)`<br>`public function exceptions(int $teamId)` |

| Core action / service source | Observed signatures |
| --- | --- |
| [CreateCalendar.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Actions/CreateCalendar.php) | `public function execute(int $teamId, int $actorId, array $data): SlaCalendar` |
| [CreateContract.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Actions/CreateContract.php) | `public function execute(int $teamId, int $actorId, array $data): SlaContract` |
| [EvaluateCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Actions/EvaluateCase.php) | `public function execute(int $teamId, int $actorId, int $caseId): array` |
| [OpenCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Actions/OpenCase.php) | `public function execute(int $teamId, int $actorId, array $data): SlaCase` |
| [RequestException.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Actions/RequestException.php) | `public function execute(int $teamId, int $actorId, array $data): SlaException` |
| [SetEntitlement.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Actions/SetEntitlement.php) | `public function execute(int $teamId, int $actorId, array $data): SlaEntitlement` |
| [TransitionCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Actions/TransitionCase.php) | `public function execute(int $teamId, int $actorId, int $caseId, string $transition, array $data = []): SlaCase` |
| [SlaAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Services/SlaAudit.php) | `public function record(int $teamId, ?int $actorId, int $caseId, string $type, array $payload = []): SlaCaseEvent` |
| [SlaPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Services/SlaPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Core storage model | Observed fillable fields (review for DTO allowlist) |
| --- | --- |
| [SlaCalendar.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Models/SlaCalendar.php) | No literal fillable array detected; inspect the model and API schema. |
| [SlaCase.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Models/SlaCase.php) | No literal fillable array detected; inspect the model and API schema. |
| [SlaCaseEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Models/SlaCaseEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [SlaContract.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Models/SlaContract.php) | No literal fillable array detected; inspect the model and API schema. |
| [SlaEntitlement.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Models/SlaEntitlement.php) | No literal fillable array detected; inspect the model and API schema. |
| [SlaEscalation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Models/SlaEscalation.php) | No literal fillable array detected; inspect the model and API schema. |
| [SlaException.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements/src/Models/SlaException.php) | No literal fillable array detected; inspect the model and API schema. |

A client example is valid only after its exact request/response contract is established. Record required/nullable fields, business units, allowed values, operation identity/concurrency support, result/pagination envelope and recovery. An `Idempotency-Key` or `If-Match` example does not establish server support by itself.

## 4. OpenAPI schema

The matched source contains these machine-readable contract/schema files. Verify their version and parity with handlers; file presence does not prove deployed compatibility or a passing validation run.

- [openapi/v1/crm-sla-and-entitlements.yaml](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sla-and-entitlements-api/openapi/v1/crm-sla-and-entitlements.yaml)

For the target contract, define stable operation IDs, explicit request/resource/collection/error schemas, allowed audiences/scopes, actor/tenant resolution, field sensitivity, pagination/filter limits, concurrency and retry semantics. Use the real manifest identity and actual route namespace, not a guessed repository-derived package or path.

Validate/bundle the fragment, check supported-version compatibility and generate clients only from the reviewed contract. Retain the source/schema commit or release in client compatibility notes. See the [API architecture](../../../architecture/API.md), [source mapping](../SOURCE-MAPPING.md#crm-sla-and-entitlements), and [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) guides.

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
- Add one-to-one architecture tests proving this package depends on and presents only `crm-sla-and-entitlements`.
- Run independent installation, minimum/current compatibility, security, performance, generated-client smoke, and representative host-composition tests.
- Run Pest 5 with meaningful owned PHP targeting 100% line coverage; coverage complements contract, mutation, security, and failure assertions.

## 9. Definition of done

- The package name, manifest, Composer dependency, namespace, route prefix, and OpenAPI ownership all match `crm-sla-and-entitlements`.
- The audience/operation matrix is complete, least-privilege, documented, and enforced in CI.
- Schemas, implementation, examples, errors, SDK/client evidence, and documentation agree.
- Authorization, tenant/field isolation, idempotency/concurrency, limits, audit, observability, compatibility, and recovery tests pass.
- The API fragment aggregates without collisions and the independent package can be installed, tested, versioned, upgraded, and removed safely.
