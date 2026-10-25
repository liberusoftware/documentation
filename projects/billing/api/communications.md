# Billing: Communications API

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#communications). Observed identity: [`liberusoftware/module-billing-communications-api`](../../../modules/source/liberusoftware--module-billing-communications-api.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one API module specification

**Proposed API design identifier:** `module-billing-communications-api`
**Matching domain module:** `billing-communications`
**Application:** Billing
**Source feature:** [Communications](../features/communications.md)
**Architecture:** [API.md](../../../architecture/API.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional API presentation package exposes approved HTTP operations for the Communications domain module. It presents exactly one independent module, delegates all authoritative behavior to that module's public actions/queries/policies, and contains no other module's API logic.

The domain capability includes:

- VoIP/SMS service inventory
- number lifecycle
- usage/rating imports
- provider adapters

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
| Source package | [liberusoftware/module-billing-communications-api](../../../modules/source/liberusoftware--module-billing-communications-api.md) |
| Source package | [liberusoftware/module-billing-communications](../../../modules/source/liberusoftware--module-billing-communications.md) |

### Observed route declarations

These are literal excerpts, not runnable standalone route files or expanded final URLs. Read group middleware/prefixes, provider loading and the host route configuration together. Authentication middleware alone does not establish the controller/domain permission policy.

[modules/module-billing-communications-api/routes/api.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications-api/routes/api.php)

```php
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.communications.read'])->prefix('api/v1/billing/communications')->group(function (): void {
Route::get('/voice/accounts', [CommunicationsController::class, 'voiceAccounts'])->name('billing.communications.voice.accounts.index');
Route::get('/voice/accounts/{account}/cdrs', [CommunicationsController::class, 'callRecords'])->whereNumber('account')->name('billing.communications.voice.cdrs.index');
Route::get('/voice/rates', [CommunicationsController::class, 'rates'])->name('billing.communications.voice.rates.index');
Route::get('/', [CommunicationsController::class, 'index'])->name('billing.communications.index');
Route::get('/numbers', [CommunicationsController::class, 'numbers'])->name('numbers');
Route::get('/providers', [CommunicationsController::class, 'providers'])->name('providers');
Route::get('/usage-imports', [CommunicationsController::class, 'usageImports'])->name('usage-imports');
Route::get('/{record}', [CommunicationsController::class, 'show'])->whereNumber('record')->name('billing.communications.show');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.communications.write', 'idempotency'])->prefix('api/v1/billing/communications')->group(function (): void {
Route::post('/voice/accounts', [CommunicationsController::class, 'createVoiceAccount'])->name('billing.communications.voice.accounts.store');
Route::post('/voice/accounts/{account}/provision', [CommunicationsController::class, 'provisionVoiceAccount'])->whereNumber('account')->name('billing.communications.voice.accounts.provision');
Route::post('/voice/accounts/{account}/cdrs', [CommunicationsController::class, 'ingestCallRecord'])->whereNumber('account')->name('billing.communications.voice.cdrs.store');
Route::post('/voice/rates', [CommunicationsController::class, 'createRate'])->name('billing.communications.voice.rates.store');
Route::post('/', [CommunicationsController::class, 'createService'])->name('billing.communications.store');
Route::patch('/{service}/lifecycle', [CommunicationsController::class, 'transitionService'])->whereNumber('service')->name('billing.communications.services.lifecycle');
Route::post('/numbers', [CommunicationsController::class, 'provisionNumber'])->name('billing.communications.numbers.store');
Route::patch('/numbers/{number}/status', [CommunicationsController::class, 'transitionNumber'])->whereNumber('number')->name('billing.communications.numbers.status');
Route::post('/providers', [CommunicationsController::class, 'createProvider'])->name('billing.communications.providers.store');
Route::post('/usage-imports', [CommunicationsController::class, 'importUsage'])->name('billing.communications.usage-imports.store');
```

### Observed controller entry points

The signatures identify request handlers to review; their argument names are not complete JSON schemas. Read their request validation, actor/tenant resolution, policy, serialization and error paths before writing a client.

| Controller source | Public handler signatures |
| --- | --- |
| [CommunicationsController.php](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications-api/src/Http/Controllers/CommunicationsController.php) | `public function index(Request $request): JsonResponse`<br>`public function show(Request $request, int $record): JsonResponse`<br>`public function createService(Request $request, CreateCommunicationService $create): JsonResponse`<br>`public function numbers(Request $request): JsonResponse`<br>`public function providers(Request $request): JsonResponse`<br>`public function usageImports(Request $request): JsonResponse`<br>`public function provisionNumber(Request $request, ProvisionCommunicationNumber $provision): JsonResponse`<br>`public function importUsage(Request $request, ImportCommunicationUsage $import): JsonResponse`<br>`public function transitionNumber(Request $request, int $number, TransitionCommunicationNumber $transition): JsonResponse`<br>`public function transitionService(Request $request, int $service, TransitionCommunicationService $transition): JsonResponse`<br>`public function createProvider(Request $request, CreateCommunicationProvider $create): JsonResponse`<br>`public function voiceAccounts(Request $request): JsonResponse`<br>`public function createVoiceAccount(Request $request, CreateVoipAccount $create): JsonResponse`<br>`public function provisionVoiceAccount(Request $request, int $account, ProvisionVoipAccount $provision): JsonResponse`<br>`public function rates(Request $request): JsonResponse`<br>`public function createRate(Request $request, CreateCallRateRule $create): JsonResponse`<br>`public function callRecords(Request $request, int $account): JsonResponse`<br>`public function ingestCallRecord(Request $request, int $account, IngestCallDetailRecord $ingest): JsonResponse` |

A client example is valid only after its exact request/response contract is established. Record required/nullable fields, business units, allowed values, operation identity/concurrency support, result/pagination envelope and recovery. An `Idempotency-Key` or `If-Match` example does not establish server support by itself.

## 4. OpenAPI schema

The matched source contains these machine-readable contract/schema files. Verify their version and parity with handlers; file presence does not prove deployed compatibility or a passing validation run.

- [modules/module-billing-communications-api/openapi/v1/billing-communications.yaml](https://github.com/liberusoftware/billing-laravel/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-communications-api/openapi/v1/billing-communications.yaml)

For the target contract, define stable operation IDs, explicit request/resource/collection/error schemas, allowed audiences/scopes, actor/tenant resolution, field sensitivity, pagination/filter limits, concurrency and retry semantics. Use the real manifest identity and actual route namespace, not a guessed repository-derived package or path.

Validate/bundle the fragment, check supported-version compatibility and generate clients only from the reviewed contract. Retain the source/schema commit or release in client compatibility notes. See the [API architecture](../../../architecture/API.md), [source mapping](../SOURCE-MAPPING.md#communications), and [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) guides.

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
- Add one-to-one architecture tests proving this package depends on and presents only `billing-communications`.
- Run independent installation, minimum/current compatibility, security, performance, generated-client smoke, and representative host-composition tests.
- Run Pest 5 with meaningful owned PHP targeting 100% line coverage; coverage complements contract, mutation, security, and failure assertions.

## 9. Definition of done

- The package name, manifest, Composer dependency, namespace, route prefix, and OpenAPI ownership all match `billing-communications`.
- The audience/operation matrix is complete, least-privilege, documented, and enforced in CI.
- Schemas, implementation, examples, errors, SDK/client evidence, and documentation agree.
- Authorization, tenant/field isolation, idempotency/concurrency, limits, audit, observability, compatibility, and recovery tests pass.
- The API fragment aggregates without collisions and the independent package can be installed, tested, versioned, upgraded, and removed safely.
