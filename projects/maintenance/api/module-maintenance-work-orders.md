# Maintenance: Module Maintenance Work Orders API

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-maintenance-work-orders). Observed identity: [`liberusoftware/module-maintenance-work-orders-api`](../../../modules/source/liberusoftware--module-maintenance-work-orders-api.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one API module specification

**Proposed API design identifier:** `module-maintenance-module-maintenance-work-orders-api`<br>
**Matching domain module:** `module-maintenance-work-orders`  
**Application:** Maintenance  
**Source feature:** [Module Maintenance Work Orders](../features/module-maintenance-work-orders.md)  
**Architecture:** [API.md](../../../architecture/API.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional API presentation package exposes approved HTTP operations for the Module Maintenance Work Orders domain module. It presents exactly one independent module, delegates all authoritative behavior to that module's public actions/queries/policies, and contains no other module's API logic.

The domain capability includes:

- Requests
- Triage
- Jobs
- Tasks
- Status machine
- Dependencies
- Notes
- Evidence
- Completion

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

This module API adapter is composed into [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api), the shared Laravel HTTP backend for independent web, mobile, and desktop clients ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [repository map](../../REPOSITORIES.md#laravel-applications)).

| Consuming client surface | Host repository | Module adapter plan | Transport and auth contract |
| --- | --- | --- | --- |
| Next.js React | [`project-maintenance-next-react`](https://github.com/liberusoftware/project-maintenance-next-react) | [Next.js plan](../nextjs/module-maintenance-work-orders.md) | Server Component / Route Handler / BFF or Sanctum SPA with `no-store` private reads |
| Nuxt 4 Vue | [`project-maintenance-nuxt-vue`](https://github.com/liberusoftware/project-maintenance-nuxt-vue) | [Nuxt plan](../nuxt/module-maintenance-work-orders.md) | Nitro SSR / BFF or Sanctum SPA with actor/tenant-scoped `useFetch` keys |
| React Native Expo | [`project-maintenance-mobile-react`](https://github.com/liberusoftware/project-maintenance-mobile-react) | [React Native plan](../react-native/module-maintenance-work-orders.md) | Typed client with Keychain/Keystore token storage, PKCE/Sanctum, and idempotent retries |
| Flutter mobile | [`project-maintenance-mobile-flutter`](https://github.com/liberusoftware/project-maintenance-mobile-flutter) | [Flutter plan](../flutter/module-maintenance-work-orders.md) | Typed Dart DTOs and platform-secure credentials on iOS and Android |
| Dart mobile & desktop | [`project-maintenance-dart-mobile`](https://github.com/liberusoftware/project-maintenance-dart-mobile) · [`project-maintenance-dart-desktop`](https://github.com/liberusoftware/project-maintenance-dart-desktop) | [Flutter & Dart plan](../flutter/module-maintenance-work-orders.md) | Separate mobile and desktop native hosts consuming the same versioned `/api/v1` contract |

### Feature-to-API capability and operation matrix

| Feature / aspect | HTTP query and command intent | DTO allowlist, concurrency, and error contract |
| --- | --- | --- |
| **Requests** | Expose authorized query/read projection and explicit domain transition command for `requests` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Triage** | Expose authorized query/read projection and explicit domain transition command for `triage` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Jobs** | Expose authorized query/read projection and explicit domain transition command for `jobs` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Tasks** | Expose authorized query/read projection and explicit domain transition command for `tasks` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Status machine** | Expose authorized query/read projection and explicit domain transition command for `status machine` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Dependencies** | Expose authorized query/read projection and explicit domain transition command for `dependencies` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Notes** | Expose authorized query/read projection and explicit domain transition command for `notes` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Evidence** | Expose authorized query/read projection and explicit domain transition command for `evidence` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Completion** | Expose authorized query/read projection and explicit domain transition command for `completion` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |

| Boundary | Observed identity and implementation reference |
| --- | --- |
| Source package | [liberusoftware/module-maintenance-work-orders-api](../../../modules/source/liberusoftware--module-maintenance-work-orders-api.md) |
| Source package | [liberusoftware/module-maintenance-work-orders](../../../modules/source/liberusoftware--module-maintenance-work-orders.md) |

### Observed route declarations

These are literal excerpts, not runnable standalone route files or expanded final URLs. Read group middleware/prefixes, provider loading and the host route configuration together. Authentication middleware alone does not establish the controller/domain permission policy.

[modules/module-maintenance-work-orders-api/routes/api.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/maintenance/work-orders')->group(function (): void {
Route::get('/', [WorkOrderController::class, 'index']);
Route::post('/', [WorkOrderController::class, 'store']);
Route::get('/{workOrder}', [WorkOrderController::class, 'show']);
Route::patch('/{workOrder}', [WorkOrderController::class, 'update']);
Route::delete('/{workOrder}', [WorkOrderController::class, 'destroy']);
Route::post('/{workOrder}/transitions', [WorkOrderController::class, 'transition']);
Route::get('/{workOrder}/comments', [WorkOrderController::class, 'comments']);
Route::post('/{workOrder}/comments', [WorkOrderController::class, 'comment']);
Route::get('/{workOrder}/dependencies', [WorkOrderController::class, 'dependencies']);
Route::post('/{workOrder}/dependencies', [WorkOrderController::class, 'addDependency']);
Route::delete('/{workOrder}/dependencies/{dependency}', [WorkOrderController::class, 'removeDependency']);
Route::get('/{workOrder}/evidence', [WorkOrderController::class, 'evidence']);
Route::post('/{workOrder}/evidence', [WorkOrderController::class, 'addEvidence']);
Route::delete('/{workOrder}/evidence/{evidence}', [WorkOrderController::class, 'removeEvidence']);
```

### Observed controller entry points

The signatures identify request handlers to review; their argument names are not complete JSON schemas. Read their request validation, actor/tenant resolution, policy, serialization and error paths before writing a client.

| Controller source | Public handler signatures |
| --- | --- |
| [WorkOrderController.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders-api/src/Http/Controllers/WorkOrderController.php) | `public function index(Request $r): JsonResponse`<br>`public function store(Request $r, CreateWorkOrder $create): JsonResponse`<br>`public function show(Request $r, WorkOrder $workOrder): JsonResponse`<br>`public function update(Request $r, WorkOrder $workOrder, UpdateWorkOrder $update): JsonResponse`<br>`public function destroy(Request $r, WorkOrder $workOrder, DeleteWorkOrder $delete): JsonResponse`<br>`public function transition(Request $r, WorkOrder $workOrder, TransitionWorkOrder $transition): JsonResponse`<br>`public function comments(Request $r, WorkOrder $workOrder): JsonResponse`<br>`public function comment(Request $r, WorkOrder $workOrder, AddWorkOrderComment $add): JsonResponse`<br>`public function dependencies(Request $r, WorkOrder $workOrder): JsonResponse`<br>`public function addDependency(Request $r, WorkOrder $workOrder, AddWorkOrderDependency $add): JsonResponse`<br>`public function removeDependency(Request $r, WorkOrder $workOrder, WorkOrderDependency $dependency, RemoveWorkOrderDependency $remove): JsonResponse`<br>`public function evidence(Request $r, WorkOrder $workOrder): JsonResponse`<br>`public function addEvidence(Request $r, WorkOrder $workOrder, AddWorkOrderEvidence $add): JsonResponse`<br>`public function removeEvidence(Request $r, WorkOrder $workOrder, WorkOrderEvidence $evidence, RemoveWorkOrderEvidence $remove): JsonResponse` |

### Observed domain queries, actions, and storage models

API controllers delegate to these observed core domain entry points and serialize only allowlisted DTO fields rather than raw storage models.

| Core action / service source | Observed signatures |
| --- | --- |
| [AddWorkOrderComment.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Actions/AddWorkOrderComment.php) | `public function handle(int $teamId, WorkOrder $workOrder, int $userId, string $comment, bool $internal = false): WorkOrderComment` |
| [AddWorkOrderDependency.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Actions/AddWorkOrderDependency.php) | `public function handle(int $teamId, WorkOrder $workOrder, WorkOrder $dependsOn): WorkOrderDependency` |
| [AddWorkOrderEvidence.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Actions/AddWorkOrderEvidence.php) | `public function handle(int $teamId, WorkOrder $workOrder, array $attributes): WorkOrderEvidence` |
| [CreateWorkOrder.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Actions/CreateWorkOrder.php) | `public function handle(int $teamId, array $attributes): WorkOrder` |
| [DeleteWorkOrder.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Actions/DeleteWorkOrder.php) | `public function handle(int $teamId, WorkOrder $workOrder): void` |
| [RemoveWorkOrderDependency.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Actions/RemoveWorkOrderDependency.php) | `public function handle(int $teamId, WorkOrderDependency $dependency): void` |
| [RemoveWorkOrderEvidence.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Actions/RemoveWorkOrderEvidence.php) | `public function handle(int $teamId, WorkOrderEvidence $evidence): void` |
| [TransitionWorkOrder.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Actions/TransitionWorkOrder.php) | `public function handle(int $teamId, WorkOrder $workOrder, string $status, ?int $actorId = null): WorkOrder` |
| [UpdateWorkOrder.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Actions/UpdateWorkOrder.php) | `public function handle(int $teamId, WorkOrder $workOrder, array $attributes): WorkOrder` |
| [WorkOrderPolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Policies/WorkOrderPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, WorkOrder $order): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, WorkOrder $order): bool`<br>`public function delete(object $user, WorkOrder $order): bool` |

| Core storage model | Observed fillable fields (review for DTO allowlist) |
| --- | --- |
| [WorkOrder.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Models/WorkOrder.php) | `team_id`, `number`, `title`, `description`, `location`, `equipment_id`, `customer_id`, `vendor_id`, `assigned_to`, `due_date`, `started_at`, `estimated_minutes`, `actual_minutes`, `maintenance_plan_id`, `checklist_id`, `priority`, `status`, `requested_by`, `guest_name`, `guest_email`, `guest_phone`, `submitted_at`, `reviewed_by`, `reviewed_at`, `completed_at`, `notes`, `metadata` |
| [WorkOrderComment.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Models/WorkOrderComment.php) | `team_id`, `work_order_id`, `user_id`, `comment`, `is_internal` |
| [WorkOrderDependency.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Models/WorkOrderDependency.php) | `team_id`, `work_order_id`, `depends_on_work_order_id` |
| [WorkOrderEvidence.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Models/WorkOrderEvidence.php) | `team_id`, `work_order_id`, `added_by`, `kind`, `label`, `reference`, `metadata` |

A client example is valid only after its exact request/response contract is established. Record required/nullable fields, business units, allowed values, operation identity/concurrency support, result/pagination envelope and recovery. An `Idempotency-Key` or `If-Match` example does not establish server support by itself.

## 4. OpenAPI schema

The matched source contains these machine-readable contract/schema files. Verify their version and parity with handlers; file presence does not prove deployed compatibility or a passing validation run.

- [openapi/v1/maintenance-work-orders.yaml](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders-api/openapi/v1/maintenance-work-orders.yaml)

For the target contract, define stable operation IDs, explicit request/resource/collection/error schemas, allowed audiences/scopes, actor/tenant resolution, field sensitivity, pagination/filter limits, concurrency and retry semantics. Use the real manifest identity and actual route namespace, not a guessed repository-derived package or path.

Validate/bundle the fragment, check supported-version compatibility and generate clients only from the reviewed contract. Retain the source/schema commit or release in client compatibility notes. See the [API architecture](../../../architecture/API.md), [source mapping](../SOURCE-MAPPING.md#module-maintenance-work-orders), and [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) guides.

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
- Add one-to-one architecture tests proving this package depends on and presents only `module-maintenance-work-orders`.
- Run independent installation, minimum/current compatibility, security, performance, generated-client smoke, and representative host-composition tests.
- Run Pest 5 with meaningful owned PHP targeting 100% line coverage; coverage complements contract, mutation, security, and failure assertions.

## 9. Definition of done

- The package name, manifest, Composer dependency, namespace, route prefix, and OpenAPI ownership all match `module-maintenance-work-orders`.
- The audience/operation matrix is complete, least-privilege, documented, and enforced in CI.
- Schemas, implementation, examples, errors, SDK/client evidence, and documentation agree.
- Authorization, tenant/field isolation, idempotency/concurrency, limits, audit, observability, compatibility, and recovery tests pass.
- The API fragment aggregates without collisions and the independent package can be installed, tested, versioned, upgraded, and removed safely.
