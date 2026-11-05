# Control Panel: OS Adapters API

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#os-adapters). Observed identity: [`liberusoftware/module-control-panel-os-adapters-api`](../../../modules/source/liberusoftware--module-control-panel-os-adapters-api.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one API module specification

**Proposed API design identifier:** `module-control-panel-os-adapters-api`
**Matching domain module:** `control-panel-os-adapters`
**Application:** Control Panel
**Source feature:** [OS Adapters](../features/os-adapters.md)
**Architecture:** [API.md](../../../architecture/API.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional API presentation package exposes approved HTTP operations for the OS Adapters domain module. It presents exactly one independent module, delegates all authoritative behavior to that module's public actions/queries/policies, and contains no other module's API logic.

The domain capability includes:

- Detection
- packages
- services
- firewall
- users
- filesystems
- repositories
- support matrix

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
| Source package | [liberusoftware/module-control-panel-os-adapters-api](../../../modules/source/liberusoftware--module-control-panel-os-adapters-api.md) |
| Source package | [liberusoftware/module-control-panel-os-adapters](../../../modules/source/liberusoftware--module-control-panel-os-adapters.md) |

### Observed route declarations

These are literal excerpts, not runnable standalone route files or expanded final URLs. Read group middleware/prefixes, provider loading and the host route configuration together. Authentication middleware alone does not establish the controller/domain permission policy.

[modules/control-panel-os-adapters-api/routes/api.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-api/routes/api.php)

```php
Route::prefix('api/v1/control-panel/os-adapters')->middleware(['api', 'auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [OsAdapterController::class, 'index'])->name('control-panel.os-adapters.index');
Route::post('/', [OsAdapterController::class, 'store'])->name('control-panel.os-adapters.store');
Route::get('services/status', [OsAdapterController::class, 'serviceStatuses'])->name('control-panel.os-adapters.services.status');
Route::get('services/missing', [OsAdapterController::class, 'missingServices'])->name('control-panel.os-adapters.services.missing');
Route::get('services/stopped', [OsAdapterController::class, 'stoppedServices'])->name('control-panel.os-adapters.services.stopped');
Route::get('services/install-commands', [OsAdapterController::class, 'installationCommands'])->name('control-panel.os-adapters.services.install-commands');
Route::get('services/{service}/check', [OsAdapterController::class, 'checkService'])->name('control-panel.os-adapters.services.check');
Route::post('packages', [OsAdapterController::class, 'package'])->name('control-panel.os-adapters.packages.store');
Route::post('services', [OsAdapterController::class, 'service'])->name('control-panel.os-adapters.services.store');
Route::patch('services/{service}', [OsAdapterController::class, 'updateService'])->name('control-panel.os-adapters.services.update');
Route::post('firewall-rules', [OsAdapterController::class, 'firewall'])->name('control-panel.os-adapters.firewall.store');
Route::patch('firewall-rules/{rule}', [OsAdapterController::class, 'updateFirewall'])->name('control-panel.os-adapters.firewall.update');
Route::delete('firewall-rules/{rule}', [OsAdapterController::class, 'deleteFirewall'])->name('control-panel.os-adapters.firewall.delete');
Route::post('users', [OsAdapterController::class, 'user'])->name('control-panel.os-adapters.users.store');
Route::post('filesystems', [OsAdapterController::class, 'filesystem'])->name('control-panel.os-adapters.filesystems.store');
Route::post('repositories', [OsAdapterController::class, 'repository'])->name('control-panel.os-adapters.repositories.store');
Route::post('support-matrix', [OsAdapterController::class, 'supportMatrix'])->name('control-panel.os-adapters.support-matrix.store');
Route::get('{adapter}', [OsAdapterController::class, 'show'])->name('control-panel.os-adapters.show');
```

### Observed controller entry points

The signatures identify request handlers to review; their argument names are not complete JSON schemas. Read their request validation, actor/tenant resolution, policy, serialization and error paths before writing a client.

| Controller source | Public handler signatures |
| --- | --- |
| [OsAdapterController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-api/src/Http/Controllers/OsAdapterController.php) | `public function index(Request $request, ListOsAdapters $list): JsonResponse`<br>`public function show(Request $request, string $id): JsonResponse`<br>`public function serviceStatuses(Request $request, ServiceStatusReport $report): JsonResponse`<br>`public function missingServices(Request $request, ServiceStatusReport $report): JsonResponse`<br>`public function stoppedServices(Request $request, ServiceStatusReport $report): JsonResponse`<br>`public function installationCommands(Request $request, InstallationCommandReport $report): JsonResponse`<br>`public function checkService(Request $request, string $service, ServiceStatusReport $report): JsonResponse`<br>`public function store(Request $request, RegisterOsAdapter $register): JsonResponse`<br>`public function package(Request $request, RecordOsResource $record): JsonResponse`<br>`public function service(Request $request, RecordOsResource $record): JsonResponse`<br>`public function updateService(Request $request, string $service, UpdateOsService $update): JsonResponse`<br>`public function firewall(Request $request, CreateFirewallRule $create): JsonResponse`<br>`public function updateFirewall(Request $request, string $rule, UpdateFirewallRule $update): JsonResponse`<br>`public function deleteFirewall(Request $request, string $rule, DeleteFirewallRule $delete): JsonResponse`<br>`public function user(Request $request, RecordOsResource $record): JsonResponse`<br>`public function filesystem(Request $request, RecordOsResource $record): JsonResponse`<br>`public function repository(Request $request, RecordOsResource $record): JsonResponse`<br>`public function supportMatrix(Request $request, RecordSupportMatrix $record): JsonResponse` |

A client example is valid only after its exact request/response contract is established. Record required/nullable fields, business units, allowed values, operation identity/concurrency support, result/pagination envelope and recovery. An `Idempotency-Key` or `If-Match` example does not establish server support by itself.

## 4. OpenAPI schema

The matched source contains these machine-readable contract/schema files. Verify their version and parity with handlers; file presence does not prove deployed compatibility or a passing validation run.

- [modules/control-panel-os-adapters-api/openapi/v1/control-panel-os-adapters.yaml](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-os-adapters-api/openapi/v1/control-panel-os-adapters.yaml)

For the target contract, define stable operation IDs, explicit request/resource/collection/error schemas, allowed audiences/scopes, actor/tenant resolution, field sensitivity, pagination/filter limits, concurrency and retry semantics. Use the real manifest identity and actual route namespace, not a guessed repository-derived package or path.

Validate/bundle the fragment, check supported-version compatibility and generate clients only from the reviewed contract. Retain the source/schema commit or release in client compatibility notes. See the [API architecture](../../../architecture/API.md), [source mapping](../SOURCE-MAPPING.md#os-adapters), and [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) guides.

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
- Add one-to-one architecture tests proving this package depends on and presents only `control-panel-os-adapters`.
- Run independent installation, minimum/current compatibility, security, performance, generated-client smoke, and representative host-composition tests.
- Run Pest 5 with meaningful owned PHP targeting 100% line coverage; coverage complements contract, mutation, security, and failure assertions.

## 9. Definition of done

- The package name, manifest, Composer dependency, namespace, route prefix, and OpenAPI ownership all match `control-panel-os-adapters`.
- The audience/operation matrix is complete, least-privilege, documented, and enforced in CI.
- Schemas, implementation, examples, errors, SDK/client evidence, and documentation agree.
- Authorization, tenant/field isolation, idempotency/concurrency, limits, audit, observability, compatibility, and recovery tests pass.
- The API fragment aggregates without collisions and the independent package can be installed, tested, versioned, upgraded, and removed safely.
