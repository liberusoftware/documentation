# Control Panel: Control Panel Control Core API

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#control-panel-control-core). Observed identity: [`liberusoftware/module-control-panel-control-core-api`](../../../modules/source/liberusoftware--module-control-panel-control-core-api.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one API module specification

**Proposed API design identifier:** `module-control-panel-control-panel-control-core-api`<br>
**Matching domain module:** `control-panel-control-core`  
**Application:** Control Panel  
**Source feature:** [Control Panel Control Core](../features/control-panel-control-core.md)  
**Architecture:** [API.md](../../../architecture/API.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional API presentation package exposes approved HTTP operations for the Control Panel Control Core domain module. It presents exactly one independent module, delegates all authoritative behavior to that module's public actions/queries/policies, and contains no other module's API logic.

The domain capability includes:

- Control Panel Control Core domain entities, lifecycle, validation, permissions, and audit
- Stable contracts, typed DTOs, and past-tense domain events

Installation does not expose every capability automatically. The host application selects this package, API version, audiences, route groups, and operations in its API manifest.

## 2. Contract design

- Publish an OpenAPI 3.1 fragment with stable operation IDs, schemas, examples, scopes, errors, pagination, rate limits, idempotency, and deprecation metadata.
- Choose the route namespace through the host's reviewed API contract; observed source prefixes below take precedence over repository/design-name guesses.
- Represent resources through explicit API DTOs/resources rather than automatic Eloquent serialization.
- Use lowercase kebab-case paths, snake_case JSON fields, opaque identifiers, ISO 8601 timestamps, explicit money objects, and RFC 9457 Problem Details errors.
- Compatible additions remain within the major version; removals or semantic breaks require a new major version or approved migration path.

## 3. Endpoint examples

**Contract status:** use the observed source below for current route/handler/schema evidence. The surrounding module scope is a target design; its feature labels are not request field names. Do not generate a create/update/delete payload or final URL by mechanically copying the design identifier.

| Boundary | Observed identity and implementation reference |
| --- | --- |
| Source package | [liberusoftware/module-control-panel-control-core-api](../../../modules/source/liberusoftware--module-control-panel-control-core-api.md) |
| Source package | [liberusoftware/module-control-panel-control-core](../../../modules/source/liberusoftware--module-control-panel-control-core.md) |

### Observed route declarations

These are literal excerpts, not runnable standalone route files or expanded final URLs. Read group middleware/prefixes, provider loading and the host route configuration together. Authentication middleware alone does not establish the controller/domain permission policy.

[modules/control-panel-control-core-api/routes/api.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core-api/routes/api.php)

```php
Route::prefix('api/v1/control-panel/control-core')
Route::get('nodes', [NodeController::class, 'index'])->name('control-panel.control-core.nodes.index');
Route::post('nodes', [NodeController::class, 'store'])->name('control-panel.control-core.nodes.store');
Route::get('nodes/{node}', [NodeController::class, 'show'])->name('control-panel.control-core.nodes.show');
Route::patch('nodes/{node}/desired-state', [NodeController::class, 'updateDesiredState'])->name('control-panel.control-core.nodes.desired-state');
Route::patch('nodes/{node}/status', [NodeController::class, 'updateStatus'])->name('control-panel.control-core.nodes.status');
Route::post('nodes/{node}/decommission', [NodeController::class, 'decommission'])->name('control-panel.control-core.nodes.decommission');
Route::put('nodes/{node}/capabilities', [NodeController::class, 'capabilities'])->name('control-panel.control-core.nodes.capabilities');
Route::post('nodes/{node}/credentials', [NodeController::class, 'credential'])->name('control-panel.control-core.nodes.credentials.store');
Route::post('nodes/{node}/ssh/deploy-key', [NodeController::class, 'deploySshKey'])->name('control-panel.control-core.nodes.ssh.deploy-key');
Route::post('nodes/{node}/ssh/test-connection', [NodeController::class, 'testSshConnection'])->name('control-panel.control-core.nodes.ssh.test-connection');
Route::post('credentials/generate-key-pair', [NodeController::class, 'generateKeyPair'])->name('control-panel.control-core.credentials.generate-key-pair');
Route::post('credentials/{credential}/revoke', [NodeController::class, 'revokeCredential'])->name('control-panel.control-core.credentials.revoke');
Route::patch('credentials/{credential}', [NodeController::class, 'updateCredential'])->name('control-panel.control-core.credentials.update');
Route::post('credentials/{credential}/expire', [NodeController::class, 'expireCredential'])->name('control-panel.control-core.credentials.expire');
Route::get('tasks', [OperationTaskController::class, 'index'])->name('control-panel.control-core.tasks.index');
Route::post('tasks', [OperationTaskController::class, 'store'])->name('control-panel.control-core.tasks.store');
Route::post('tasks/{task}/transition', [OperationTaskController::class, 'transition'])->name('control-panel.control-core.tasks.transition');
Route::post('tasks/{task}/cancel', [OperationTaskController::class, 'cancel'])->name('control-panel.control-core.tasks.cancel');
Route::post('tasks/{task}/timeout', [OperationTaskController::class, 'timeout'])->name('control-panel.control-core.tasks.timeout');
Route::post('tasks/{task}/compensation', [OperationTaskController::class, 'compensation'])->name('control-panel.control-core.tasks.compensation');
Route::get('tasks/{task}/steps', [OperationTaskController::class, 'steps'])->name('control-panel.control-core.tasks.steps.index');
Route::post('tasks/{task}/steps', [OperationTaskController::class, 'recordStep'])->name('control-panel.control-core.tasks.steps.store');
Route::post('tasks/{task}/retry', [OperationTaskController::class, 'retry'])->name('control-panel.control-core.tasks.retry');
Route::get('inventory', [InventoryController::class, 'index'])->name('control-panel.control-core.inventory.index');
Route::post('inventory', [InventoryController::class, 'store'])->name('control-panel.control-core.inventory.store');
Route::get('audit', [AuditController::class, 'index'])->name('control-panel.control-core.audit.index');
Route::get('locks', [OperationLockController::class, 'index'])->name('control-panel.control-core.locks.index');
Route::post('locks', [OperationLockController::class, 'store'])->name('control-panel.control-core.locks.store');
Route::delete('locks/{lock}', [OperationLockController::class, 'destroy'])->name('control-panel.control-core.locks.destroy');
```

### Observed controller entry points

The signatures identify request handlers to review; their argument names are not complete JSON schemas. Read their request validation, actor/tenant resolution, policy, serialization and error paths before writing a client.

| Controller source | Public handler signatures |
| --- | --- |
| [AuditController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core-api/src/Http/Controllers/AuditController.php) | `public function index(Request $request, ListAuditEntries $entries): JsonResponse` |
| [InventoryController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core-api/src/Http/Controllers/InventoryController.php) | `public function index(Request $request, ListInventory $inventory): JsonResponse`<br>`public function store(Request $request, RecordInventory $record): JsonResponse` |
| [NodeController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core-api/src/Http/Controllers/NodeController.php) | `public function show(Request $request, string $node): JsonResponse`<br>`public function index(Request $request, ListNodes $nodes): JsonResponse`<br>`public function store(Request $request, RegisterNode $register): JsonResponse`<br>`public function updateDesiredState(Request $request, string $node, UpdateDesiredState $update): JsonResponse`<br>`public function updateStatus(Request $request, string $node, ChangeNodeStatus $change): JsonResponse`<br>`public function decommission(Request $request, string $node, DecommissionNode $decommission): JsonResponse`<br>`public function capabilities(Request $request, string $node, SyncNodeCapabilities $sync): JsonResponse`<br>`public function credential(Request $request, string $node, RegisterNodeCredential $register): JsonResponse`<br>`public function generateKeyPair(Request $request, GenerateSshKeyPair $generate): JsonResponse`<br>`public function deploySshKey(Request $request, string $node, RequestSshOperation $requestOperation): JsonResponse`<br>`public function testSshConnection(Request $request, string $node, RequestSshOperation $requestOperation): JsonResponse`<br>`public function revokeCredential(Request $request, string $credential, RevokeNodeCredential $revoke): JsonResponse`<br>`public function updateCredential(Request $request, string $credential, UpdateNodeCredential $update): JsonResponse`<br>`public function expireCredential(Request $request, string $credential, ExpireNodeCredential $expire): JsonResponse` |
| [OperationLockController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core-api/src/Http/Controllers/OperationLockController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, AcquireOperationLock $acquire): JsonResponse`<br>`public function destroy(Request $request, string $lock, ReleaseOperationLock $release): JsonResponse` |
| [OperationTaskController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core-api/src/Http/Controllers/OperationTaskController.php) | `public function index(Request $request, ListOperationTasks $tasks): JsonResponse`<br>`public function store(Request $request, CreateOperationTask $create): JsonResponse`<br>`public function transition(Request $request, string $task, TransitionOperationTask $transition): JsonResponse`<br>`public function retry(Request $request, string $task, RetryOperationTask $retry): JsonResponse`<br>`public function cancel(Request $request, string $task, CancelOperationTask $cancel): JsonResponse`<br>`public function timeout(Request $request, string $task, TimeoutOperationTask $timeout): JsonResponse`<br>`public function compensation(Request $request, string $task, RecordOperationTaskCompensation $record): JsonResponse`<br>`public function steps(Request $request, string $task): JsonResponse`<br>`public function recordStep(Request $request, string $task, RecordOperationTaskStep $record): JsonResponse` |

A client example is valid only after its exact request/response contract is established. Record required/nullable fields, business units, allowed values, operation identity/concurrency support, result/pagination envelope and recovery. An `Idempotency-Key` or `If-Match` example does not establish server support by itself.

## 4. OpenAPI schema

The matched source contains these machine-readable contract/schema files. Verify their version and parity with handlers; file presence does not prove deployed compatibility or a passing validation run.

- [modules/control-panel-control-core-api/openapi/v1/control-panel-control-core.yaml](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-control-core-api/openapi/v1/control-panel-control-core.yaml)

For the target contract, define stable operation IDs, explicit request/resource/collection/error schemas, allowed audiences/scopes, actor/tenant resolution, field sensitivity, pagination/filter limits, concurrency and retry semantics. Use the real manifest identity and actual route namespace, not a guessed repository-derived package or path.

Validate/bundle the fragment, check supported-version compatibility and generate clients only from the reviewed contract. Retain the source/schema commit or release in client compatibility notes. See the [API architecture](../../../architecture/API.md), [source mapping](../SOURCE-MAPPING.md#control-panel-control-core), and [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) guides.

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
- Add one-to-one architecture tests proving this package depends on and presents only `control-panel-control-core`.
- Run independent installation, minimum/current compatibility, security, performance, generated-client smoke, and representative host-composition tests.
- Run Pest 5 with meaningful owned PHP targeting 100% line coverage; coverage complements contract, mutation, security, and failure assertions.

## 9. Definition of done

- The package name, manifest, Composer dependency, namespace, route prefix, and OpenAPI ownership all match `control-panel-control-core`.
- The audience/operation matrix is complete, least-privilege, documented, and enforced in CI.
- Schemas, implementation, examples, errors, SDK/client evidence, and documentation agree.
- Authorization, tenant/field isolation, idempotency/concurrency, limits, audit, observability, compatibility, and recovery tests pass.
- The API fragment aggregates without collisions and the independent package can be installed, tested, versioned, upgraded, and removed safely.
