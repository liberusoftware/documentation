# Real Estate: Core API

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#core). Observed identity: [`liberusoftware/real-estate-core-api`](../../../modules/source/liberusoftware--real-estate-core-api.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one API module specification

**Proposed API design identifier:** `module-real-estate-core-api`<br>
**Matching domain module:** `core`  
**Application:** Real Estate  
**Source feature:** [Core](../features/core.md)  
**Architecture:** [API.md](../../../architecture/API.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional API presentation package exposes approved HTTP operations for the Core domain module. It presents exactly one independent module, delegates all authoritative behavior to that module's public actions/queries/policies, and contains no other module's API logic.

The domain capability includes:

- Core domain entities, lifecycle, validation, permissions, and audit
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
| Source package | [liberusoftware/real-estate-core-api](../../../modules/source/liberusoftware--real-estate-core-api.md) |
| Source package | [liberusoftware/real-estate-core](../../../modules/source/liberusoftware--real-estate-core.md) |

### Observed route declarations

These are literal excerpts, not runnable standalone route files or expanded final URLs. Read group middleware/prefixes, provider loading and the host route configuration together. Authentication middleware alone does not establish the controller/domain permission policy.

[modules/real-estate-core-api/routes/api.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/routes/api.php)

```php
Route::get('api/v1/public/territories', [PublicTerritoryController::class, 'index'])
Route::prefix('api/v1/real-estate/calendar-entries')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::post('/', [CalendarEntryController::class, 'store']);
Route::delete('/{calendarEntry}', [CalendarEntryController::class, 'destroy']);
Route::prefix('api/v1/real-estate/communications')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::post('/', [CommunicationController::class, 'store']);
Route::delete('/{communication}', [CommunicationController::class, 'destroy']);
Route::middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('api/v1/real-estate/core/{kind}', [CoreConfigurationController::class, 'list'])->whereIn('kind', ['terminology', 'statuses', 'audit']);
Route::put('api/v1/real-estate/core/terminology/{key}', [CoreConfigurationController::class, 'terminology']);
Route::post('api/v1/real-estate/core/statuses', [CoreConfigurationController::class, 'status']);
Route::post('api/v1/real-estate/core/audit', [CoreConfigurationController::class, 'audit']);
Route::post('api/v1/real-estate/numbering/{key}/next', [NumberingController::class, 'next'])
Route::prefix('api/v1/real-estate/branches')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [BranchController::class, 'index'])->name('real-estate.branches.index');
Route::post('/', [BranchController::class, 'store'])->name('real-estate.branches.store');
Route::get('/{branch}', [BranchController::class, 'show'])->name('real-estate.branches.show');
Route::delete('/{branch}', [BranchController::class, 'destroy'])->name('real-estate.branches.destroy');
Route::prefix('api/v1/real-estate/agencies')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [AgencyController::class, 'index']);
Route::post('/', [AgencyController::class, 'store']);
Route::get('/{agency}', [AgencyController::class, 'show']);
Route::delete('/{agency}', [AgencyController::class, 'destroy']);
Route::prefix('api/v1/real-estate/territories')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [TerritoryController::class, 'index']);
Route::post('/', [TerritoryController::class, 'store']);
Route::get('/{territory}', [TerritoryController::class, 'show']);
Route::delete('/{territory}', [TerritoryController::class, 'destroy']);
```

### Observed controller entry points

The signatures identify request handlers to review; their argument names are not complete JSON schemas. Read their request validation, actor/tenant resolution, policy, serialization and error paths before writing a client.

| Controller source | Public handler signatures |
| --- | --- |
| [AgencyController.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/Http/Controllers/AgencyController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateAgency $create): JsonResponse`<br>`public function show(Request $request, Agency $agency): JsonResponse`<br>`public function update(Request $request, Agency $agency, UpdateAgency $update): JsonResponse`<br>`public function destroy(Request $request, Agency $agency, DeleteAgency $delete): Response` |
| [BranchController.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/Http/Controllers/BranchController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateBranch $create): JsonResponse`<br>`public function show(Request $request, Branch $branch): JsonResponse`<br>`public function update(Request $request, Branch $branch, UpdateBranch $update): JsonResponse`<br>`public function destroy(Request $request, Branch $branch, DeleteBranch $delete): Response` |
| [CalendarEntryController.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/Http/Controllers/CalendarEntryController.php) | `public function store(Request $request, CreateCalendarEntry $create): JsonResponse`<br>`public function update(Request $request, CalendarEntry $calendarEntry): JsonResponse`<br>`public function destroy(Request $request, CalendarEntry $calendarEntry): Response` |
| [CommunicationController.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/Http/Controllers/CommunicationController.php) | `public function store(Request $request, RecordCommunication $record): JsonResponse`<br>`public function update(Request $request, Communication $communication): JsonResponse`<br>`public function destroy(Request $request, Communication $communication): Response` |
| [CoreConfigurationController.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/Http/Controllers/CoreConfigurationController.php) | `public function terminology(Request $request, string $key, SetTerminology $set): JsonResponse`<br>`public function status(Request $request, DefineStatus $define): JsonResponse`<br>`public function audit(Request $request, RecordAuditEntry $record): JsonResponse`<br>`public function list(Request $request, string $kind): JsonResponse` |
| [NumberingController.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/Http/Controllers/NumberingController.php) | `public function next(Request $request, string $key, NextNumber $nextNumber): JsonResponse` |
| [PublicTerritoryController.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/Http/Controllers/PublicTerritoryController.php) | `public function index(): JsonResponse` |
| [TerritoryController.php](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/src/Http/Controllers/TerritoryController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateTerritory $create): JsonResponse`<br>`public function show(Request $request, Territory $territory): JsonResponse`<br>`public function update(Request $request, Territory $territory, UpdateTerritory $update): JsonResponse`<br>`public function destroy(Request $request, Territory $territory, DeleteTerritory $delete): Response` |

A client example is valid only after its exact request/response contract is established. Record required/nullable fields, business units, allowed values, operation identity/concurrency support, result/pagination envelope and recovery. An `Idempotency-Key` or `If-Match` example does not establish server support by itself.

## 4. OpenAPI schema

The matched source contains these machine-readable contract/schema files. Verify their version and parity with handlers; file presence does not prove deployed compatibility or a passing validation run.

- [modules/real-estate-core-api/openapi/v1/real-estate-core.yaml](https://github.com/liberusoftware/real-estate-laravel/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-core-api/openapi/v1/real-estate-core.yaml)

For the target contract, define stable operation IDs, explicit request/resource/collection/error schemas, allowed audiences/scopes, actor/tenant resolution, field sensitivity, pagination/filter limits, concurrency and retry semantics. Use the real manifest identity and actual route namespace, not a guessed repository-derived package or path.

Validate/bundle the fragment, check supported-version compatibility and generate clients only from the reviewed contract. Retain the source/schema commit or release in client compatibility notes. See the [API architecture](../../../architecture/API.md), [source mapping](../SOURCE-MAPPING.md#core), and [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) guides.

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
- Add one-to-one architecture tests proving this package depends on and presents only `core`.
- Run independent installation, minimum/current compatibility, security, performance, generated-client smoke, and representative host-composition tests.
- Run Pest 5 with meaningful owned PHP targeting 100% line coverage; coverage complements contract, mutation, security, and failure assertions.

## 9. Definition of done

- The package name, manifest, Composer dependency, namespace, route prefix, and OpenAPI ownership all match `core`.
- The audience/operation matrix is complete, least-privilege, documented, and enforced in CI.
- Schemas, implementation, examples, errors, SDK/client evidence, and documentation agree.
- Authorization, tenant/field isolation, idempotency/concurrency, limits, audit, observability, compatibility, and recovery tests pass.
- The API fragment aggregates without collisions and the independent package can be installed, tested, versioned, upgraded, and removed safely.
