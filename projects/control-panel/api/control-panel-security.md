# Control Panel: Control Panel Security API

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#control-panel-security). Observed identity: [`liberusoftware/module-control-panel-security-api`](../../../modules/source/liberusoftware--module-control-panel-security-api.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one API module specification

**Proposed API design identifier:** `module-control-panel-control-panel-security-api`<br>
**Matching domain module:** `control-panel-security`  
**Application:** Control Panel  
**Source feature:** [Control Panel Security](../features/control-panel-security.md)  
**Architecture:** [API.md](../../../architecture/API.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional API presentation package exposes approved HTTP operations for the Control Panel Security domain module. It presents exactly one independent module, delegates all authoritative behavior to that module's public actions/queries/policies, and contains no other module's API logic.

The domain capability includes:

- Control Panel Security domain entities, lifecycle, validation, permissions, and audit
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
| Source package | [liberusoftware/module-control-panel-security-api](../../../modules/source/liberusoftware--module-control-panel-security-api.md) |
| Source package | [liberusoftware/module-control-panel-security](../../../modules/source/liberusoftware--module-control-panel-security.md) |

### Observed route declarations

These are literal excerpts, not runnable standalone route files or expanded final URLs. Read group middleware/prefixes, provider loading and the host route configuration together. Authentication middleware alone does not establish the controller/domain permission policy.

[modules/control-panel-security-api/routes/api.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-api/routes/api.php)

```php
Route::prefix('api/v1/control-panel/security')->middleware(['api', 'auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [SecurityFindingController::class, 'index'])->name('control-panel.security.index');
Route::post('/', [SecurityFindingController::class, 'store'])->name('control-panel.security.store');
Route::post('{finding}/resolve', [SecurityFindingController::class, 'resolve'])->name('control-panel.security.resolve');
Route::patch('{finding}', [SecurityFindingController::class, 'update'])->name('control-panel.security.update');
Route::post('hardening', [SecurityFindingController::class, 'hardening'])->name('control-panel.security.hardening.store');
Route::post('patches', [SecurityFindingController::class, 'patch'])->name('control-panel.security.patches.store');
Route::post('mfa-rbac', [SecurityFindingController::class, 'policy'])->name('control-panel.security.mfa-rbac.store');
Route::get('mfa-rbac', [SecurityFindingController::class, 'policies'])->name('control-panel.security.mfa-rbac.index');
Route::post('secrets', [SecurityFindingController::class, 'secret'])->name('control-panel.security.secrets.store');
Route::get('secrets', [SecurityFindingController::class, 'secrets'])->name('control-panel.security.secrets.index');
Route::post('malware-scans', [SecurityFindingController::class, 'malware'])->name('control-panel.security.malware.store');
Route::get('malware-scans', [SecurityFindingController::class, 'malwareScans'])->name('control-panel.security.malware.index');
Route::post('intrusion-controls', [SecurityFindingController::class, 'intrusion'])->name('control-panel.security.intrusion.store');
Route::get('intrusion-controls', [SecurityFindingController::class, 'intrusionControls'])->name('control-panel.security.intrusion.index');
Route::get('patches', [SecurityFindingController::class, 'patches'])->name('control-panel.security.patches.index');
Route::post('fail2ban', [SecurityFindingController::class, 'fail2ban'])->name('control-panel.security.fail2ban.store');
Route::get('fail2ban/{jail}/bans', [SecurityFindingController::class, 'listFail2banBans'])->name('control-panel.security.fail2ban.bans.index');
Route::post('fail2ban/{jail}/bans', [SecurityFindingController::class, 'fail2banBans'])->name('control-panel.security.fail2ban.bans.store');
Route::post('fail2ban/bans/{ban}/unban', [SecurityFindingController::class, 'unbanFail2ban'])->name('control-panel.security.fail2ban.bans.unban');
Route::post('compliance', [SecurityFindingController::class, 'compliance'])->name('control-panel.security.compliance.store');
Route::get('{finding}', [SecurityFindingController::class, 'show'])->name('control-panel.security.show');
```

### Observed controller entry points

The signatures identify request handlers to review; their argument names are not complete JSON schemas. Read their request validation, actor/tenant resolution, policy, serialization and error paths before writing a client.

| Controller source | Public handler signatures |
| --- | --- |
| [SecurityFindingController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-api/src/Http/Controllers/SecurityFindingController.php) | `public function index(Request $request, ListFindings $list): JsonResponse`<br>`public function show(Request $request, string $id): JsonResponse`<br>`public function store(Request $request, RecordFinding $record): JsonResponse`<br>`public function resolve(Request $request, string $id, ResolveSecurityFinding $resolve): JsonResponse`<br>`public function update(Request $request, string $id, UpdateSecurityFinding $update): JsonResponse`<br>`public function hardening(Request $request, RecordSecurityResource $record): JsonResponse`<br>`public function patch(Request $request, RecordSecurityResource $record): JsonResponse`<br>`public function patches(Request $request): JsonResponse`<br>`public function policy(Request $request, RecordSecurityResource $record): JsonResponse`<br>`public function policies(Request $request): JsonResponse`<br>`public function secret(Request $request, StoreSecret $store): JsonResponse`<br>`public function secrets(Request $request): JsonResponse`<br>`public function malware(Request $request, RecordSecurityResource $record): JsonResponse`<br>`public function malwareScans(Request $request): JsonResponse`<br>`public function intrusion(Request $request, RecordSecurityResource $record): JsonResponse`<br>`public function intrusionControls(Request $request): JsonResponse`<br>`public function fail2ban(Request $request, ConfigureFail2ban $configure): JsonResponse`<br>`public function fail2banBans(Request $request, string $jail, RecordFail2banBan $record): JsonResponse`<br>`public function listFail2banBans(Request $request, string $jail): JsonResponse`<br>`public function unbanFail2ban(Request $request, string $ban, UnbanFail2banBan $unban): JsonResponse`<br>`public function compliance(Request $request, RecordSecurityResource $record): JsonResponse` |

A client example is valid only after its exact request/response contract is established. Record required/nullable fields, business units, allowed values, operation identity/concurrency support, result/pagination envelope and recovery. An `Idempotency-Key` or `If-Match` example does not establish server support by itself.

## 4. OpenAPI schema

The matched source contains these machine-readable contract/schema files. Verify their version and parity with handlers; file presence does not prove deployed compatibility or a passing validation run.

- [modules/control-panel-security-api/openapi/v1/control-panel-security.yaml](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-security-api/openapi/v1/control-panel-security.yaml)

For the target contract, define stable operation IDs, explicit request/resource/collection/error schemas, allowed audiences/scopes, actor/tenant resolution, field sensitivity, pagination/filter limits, concurrency and retry semantics. Use the real manifest identity and actual route namespace, not a guessed repository-derived package or path.

Validate/bundle the fragment, check supported-version compatibility and generate clients only from the reviewed contract. Retain the source/schema commit or release in client compatibility notes. See the [API architecture](../../../architecture/API.md), [source mapping](../SOURCE-MAPPING.md#control-panel-security), and [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) guides.

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
- Add one-to-one architecture tests proving this package depends on and presents only `control-panel-security`.
- Run independent installation, minimum/current compatibility, security, performance, generated-client smoke, and representative host-composition tests.
- Run Pest 5 with meaningful owned PHP targeting 100% line coverage; coverage complements contract, mutation, security, and failure assertions.

## 9. Definition of done

- The package name, manifest, Composer dependency, namespace, route prefix, and OpenAPI ownership all match `control-panel-security`.
- The audience/operation matrix is complete, least-privilege, documented, and enforced in CI.
- Schemas, implementation, examples, errors, SDK/client evidence, and documentation agree.
- Authorization, tenant/field isolation, idempotency/concurrency, limits, audit, observability, compatibility, and recovery tests pass.
- The API fragment aggregates without collisions and the independent package can be installed, tested, versioned, upgraded, and removed safely.
