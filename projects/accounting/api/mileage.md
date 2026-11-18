# Accounting: Mileage API

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#mileage). Observed identity: [`liberusoftware/module-accounting-mileage-api`](../../../modules/source/liberusoftware--module-accounting-mileage-api.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one API module specification

**Proposed API design identifier:** `module-accounting-mileage-api`<br>
**Matching domain module:** `accounting-mileage`  
**Application:** Accounting  
**Source feature:** [Mileage](../features/mileage.md)  
**Architecture:** [API.md](../../../architecture/API.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional API presentation package exposes approved HTTP operations for the Mileage domain module. It presents exactly one independent module, delegates all authoritative behavior to that module's public actions/queries/policies, and contains no other module's API logic.

The domain capability includes:

- Vehicles/rates
- Trip capture/import
- Distance
- Business purpose
- Projects
- Policy
- Approval
- Reimbursement
- Regional reporting

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

This module API adapter is composed into [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api), the shared Laravel HTTP backend for independent web, mobile, and desktop clients ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [repository map](../../REPOSITORIES.md#laravel-applications)).

| Consuming client surface | Host repository | Module adapter plan | Transport and auth contract |
| --- | --- | --- | --- |
| Next.js React | [`project-accounting-erp-next-react`](https://github.com/liberusoftware/project-accounting-erp-next-react) | [Next.js plan](../nextjs/mileage.md) | Server Component / Route Handler / BFF or Sanctum SPA with `no-store` private reads |
| Nuxt 4 Vue | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | [Nuxt plan](../nuxt/mileage.md) | Nitro SSR / BFF or Sanctum SPA with actor/tenant-scoped `useFetch` keys |
| React Native Expo | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | [React Native plan](../react-native/mileage.md) | Typed client with Keychain/Keystore token storage, PKCE/Sanctum, and idempotent retries |
| Flutter mobile | [`project-accounting-erp-mobile-flutter`](https://github.com/liberusoftware/project-accounting-erp-mobile-flutter) | [Flutter plan](../flutter/mileage.md) | Typed Dart DTOs and platform-secure credentials on iOS and Android |
| Dart mobile & desktop | [`project-accounting-erp-dart-mobile`](https://github.com/liberusoftware/project-accounting-erp-dart-mobile) · [`project-accounting-erp-dart-desktop`](https://github.com/liberusoftware/project-accounting-erp-dart-desktop) | [Flutter & Dart plan](../flutter/mileage.md) | Separate mobile and desktop native hosts consuming the same versioned `/api/v1` contract |

### Feature-to-API capability and operation matrix

| Feature / aspect | HTTP query and command intent | DTO allowlist, concurrency, and error contract |
| --- | --- | --- |
| **Vehicles/rates** | Expose authorized query/read projection and explicit domain transition command for `vehicles/rates` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Trip capture/import** | Expose authorized query/read projection and explicit domain transition command for `trip capture/import` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Distance** | Expose authorized query/read projection and explicit domain transition command for `distance` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Business purpose** | Expose authorized query/read projection and explicit domain transition command for `business purpose` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Projects** | Expose authorized query/read projection and explicit domain transition command for `projects` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Policy** | Expose authorized query/read projection and explicit domain transition command for `policy` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Approval** | Expose authorized query/read projection and explicit domain transition command for `approval` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Reimbursement** | Expose authorized query/read projection and explicit domain transition command for `reimbursement` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Regional reporting** | Expose authorized query/read projection and explicit domain transition command for `regional reporting` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |

| Boundary | Observed identity and implementation reference |
| --- | --- |
| Source package | [liberusoftware/module-accounting-mileage-api](../../../modules/source/liberusoftware--module-accounting-mileage-api.md) |
| Source package | [liberusoftware/module-accounting-mileage](../../../modules/source/liberusoftware--module-accounting-mileage.md) |

### Observed route declarations

These are literal excerpts, not runnable standalone route files or expanded final URLs. Read group middleware/prefixes, provider loading and the host route configuration together. Authentication middleware alone does not establish the controller/domain permission policy.

[modules/accounting-mileage-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/mileage')->group(function (): void {
Route::get('/', [MileageController::class, 'index'])->name('accounting.mileage.list');
Route::post('/', [MileageController::class, 'store'])->name('accounting.mileage.create');
Route::get('/vehicles', [MileageController::class, 'vehicles'])->name('accounting.mileage.vehicles');
Route::post('/vehicles', [MileageController::class, 'vehicle'])->name('accounting.mileage.vehicle');
Route::post('/rates', [MileageController::class, 'rate'])->name('accounting.mileage.rate');
Route::get('/report/regional', [MileageController::class, 'report'])->name('accounting.mileage.report');
Route::get('/{trip}', [MileageController::class, 'show'])->name('accounting.mileage.get');
Route::post('/{trip}/submit', [MileageController::class, 'submit'])->name('accounting.mileage.submit');
Route::post('/{trip}/approve', [MileageController::class, 'approve'])->name('accounting.mileage.approve');
Route::post('/{trip}/reimburse', [MileageController::class, 'reimburse'])->name('accounting.mileage.reimburse');
```

### Observed controller entry points

The signatures identify request handlers to review; their argument names are not complete JSON schemas. Read their request validation, actor/tenant resolution, policy, serialization and error paths before writing a client.

| Controller source | Public handler signatures |
| --- | --- |
| [MileageController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage-api/src/Http/Controllers/MileageController.php) | `public function index(Request $request, MileageQuery $query): mixed`<br>`public function store(Request $request, CaptureTrip $action): MileageResource`<br>`public function show(MileageTrip $trip): MileageResource`<br>`public function vehicles(Request $request): mixed`<br>`public function vehicle(Request $request, CreateVehicle $action): JsonResponse`<br>`public function rate(Request $request, RecordMileageRate $action): JsonResponse`<br>`public function submit(MileageTrip $trip, SubmitTrip $action): MileageResource`<br>`public function approve(Request $request, MileageTrip $trip, ApproveTrip $action): MileageResource`<br>`public function reimburse(Request $request, MileageTrip $trip, ReimburseTrip $action): JsonResponse`<br>`public function report(Request $request, MileageQuery $query): array` |

### Observed domain queries, actions, and storage models

API controllers delegate to these observed core domain entry points and serialize only allowlisted DTO fields rather than raw storage models.

| Core query source | Observed signatures |
| --- | --- |
| [MileageQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Queries/MileageQuery.php) | `public function trips(?int $teamId = null, int $perPage = 25): LengthAwarePaginator`<br>`public function rates(?int $teamId = null, int $perPage = 25): LengthAwarePaginator`<br>`public function regionalReport(?int $teamId = null, ?string $region = null): array` |

| Core action / service source | Observed signatures |
| --- | --- |
| [ApproveTrip.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Actions/ApproveTrip.php) | `public function handle(MileageTrip $trip, string $actor, bool $approved = true, ?string $reason = null): MileageTrip` |
| [CaptureTrip.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Actions/CaptureTrip.php) | `public function handle(array $attributes): MileageTrip` |
| [CreateVehicle.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Actions/CreateVehicle.php) | `public function handle(array $attributes): Vehicle` |
| [RecordMileageRate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Actions/RecordMileageRate.php) | `public function handle(array $attributes): MileageRate` |
| [ReimburseTrip.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Actions/ReimburseTrip.php) | `public function handle(MileageTrip $trip, string $payee, ?string $externalRef = null): MileageReimbursement` |
| [SubmitTrip.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Actions/SubmitTrip.php) | `public function handle(MileageTrip $trip): MileageTrip` |

| Core storage model | Observed fillable fields (review for DTO allowlist) |
| --- | --- |
| [MileageApproval.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Models/MileageApproval.php) | `trip_id`, `actor_ref`, `decision`, `reason`, `decided_at`, `metadata` |
| [MileagePolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Models/MileagePolicy.php) | `team_id`, `name`, `region`, `max_distance_per_trip`, `max_distance_per_day`, `requires_purpose`, `requires_project`, `approval_threshold`, `currency`, `active`, `metadata` |
| [MileageRate.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Models/MileageRate.php) | `team_id`, `region`, `vehicle_type`, `currency`, `rate_per_distance`, `effective_from`, `effective_until`, `active`, `metadata` |
| [MileageReimbursement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Models/MileageReimbursement.php) | `trip_id`, `payee_ref`, `currency`, `amount`, `status`, `external_ref`, `failure_message`, `paid_at`, `metadata` |
| [MileageTrip.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Models/MileageTrip.php) | `team_id`, `trip_ref`, `employee_ref`, `vehicle_id`, `rate_id`, `policy_id`, `project_ref`, `origin`, `destination`, `trip_date`, `distance`, `distance_unit`, `business_purpose`, `region`, `currency`, `reimbursement_amount`, `status`, `source`, `source_hash`, `submitted_at`, `approved_at`, `reimbursed_at`, `metadata` |
| [Vehicle.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage/src/Models/Vehicle.php) | `team_id`, `owner_ref`, `registration`, `make`, `model`, `fuel_type`, `co2_g_per_km`, `active`, `metadata` |

A client example is valid only after its exact request/response contract is established. Record required/nullable fields, business units, allowed values, operation identity/concurrency support, result/pagination envelope and recovery. An `Idempotency-Key` or `If-Match` example does not establish server support by itself.

## 4. OpenAPI schema

The matched source contains these machine-readable contract/schema files. Verify their version and parity with handlers; file presence does not prove deployed compatibility or a passing validation run.

- [openapi/v1/accounting-mileage.yaml](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-mileage-api/openapi/v1/accounting-mileage.yaml)

For the target contract, define stable operation IDs, explicit request/resource/collection/error schemas, allowed audiences/scopes, actor/tenant resolution, field sensitivity, pagination/filter limits, concurrency and retry semantics. Use the real manifest identity and actual route namespace, not a guessed repository-derived package or path.

Validate/bundle the fragment, check supported-version compatibility and generate clients only from the reviewed contract. Retain the source/schema commit or release in client compatibility notes. See the [API architecture](../../../architecture/API.md), [source mapping](../SOURCE-MAPPING.md#mileage), and [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) guides.

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
- Add one-to-one architecture tests proving this package depends on and presents only `accounting-mileage`.
- Run independent installation, minimum/current compatibility, security, performance, generated-client smoke, and representative host-composition tests.
- Run Pest 5 with meaningful owned PHP targeting 100% line coverage; coverage complements contract, mutation, security, and failure assertions.

## 9. Definition of done

- The package name, manifest, Composer dependency, namespace, route prefix, and OpenAPI ownership all match `accounting-mileage`.
- The audience/operation matrix is complete, least-privilege, documented, and enforced in CI.
- Schemas, implementation, examples, errors, SDK/client evidence, and documentation agree.
- Authorization, tenant/field isolation, idempotency/concurrency, limits, audit, observability, compatibility, and recovery tests pass.
- The API fragment aggregates without collisions and the independent package can be installed, tested, versioned, upgraded, and removed safely.
