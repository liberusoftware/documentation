# Accounting: Bill Payments API

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#bill-payments). Observed identity: [`liberusoftware/module-accounting-bill-payments-api`](../../../modules/source/liberusoftware--module-accounting-bill-payments-api.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one API module specification

**Proposed API design identifier:** `module-accounting-bill-payments-api`<br>
**Matching domain module:** `accounting-bill-payments`  
**Application:** Accounting  
**Source feature:** [Bill Payments](../features/bill-payments.md)  
**Architecture:** [API.md](../../../architecture/API.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional API presentation package exposes approved HTTP operations for the Bill Payments domain module. It presents exactly one independent module, delegates all authoritative behavior to that module's public actions/queries/policies, and contains no other module's API logic.

The domain capability includes:

- Payment proposals
- Due-date/discount optimization
- Bank details validation
- Maker-checker approval
- Files/APIs
- Remittances
- Status

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
| Next.js React | [`project-accounting-erp-next-react`](https://github.com/liberusoftware/project-accounting-erp-next-react) | [Next.js plan](../nextjs/bill-payments.md) | Server Component / Route Handler / BFF or Sanctum SPA with `no-store` private reads |
| Nuxt 4 Vue | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | [Nuxt plan](../nuxt/bill-payments.md) | Nitro SSR / BFF or Sanctum SPA with actor/tenant-scoped `useFetch` keys |
| React Native Expo | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | [React Native plan](../react-native/bill-payments.md) | Typed client with Keychain/Keystore token storage, PKCE/Sanctum, and idempotent retries |
| Flutter mobile | [`project-accounting-erp-mobile-flutter`](https://github.com/liberusoftware/project-accounting-erp-mobile-flutter) | [Flutter plan](../flutter/bill-payments.md) | Typed Dart DTOs and platform-secure credentials on iOS and Android |
| Dart mobile & desktop | [`project-accounting-erp-dart-mobile`](https://github.com/liberusoftware/project-accounting-erp-dart-mobile) · [`project-accounting-erp-dart-desktop`](https://github.com/liberusoftware/project-accounting-erp-dart-desktop) | [Flutter & Dart plan](../flutter/bill-payments.md) | Separate mobile and desktop native hosts consuming the same versioned `/api/v1` contract |

### Feature-to-API capability and operation matrix

| Feature / aspect | HTTP query and command intent | DTO allowlist, concurrency, and error contract |
| --- | --- | --- |
| **Payment proposals** | Expose authorized query/read projection and explicit domain transition command for `payment proposals` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Due-date/discount optimization** | Expose authorized query/read projection and explicit domain transition command for `due-date/discount optimization` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Bank details validation** | Expose authorized query/read projection and explicit domain transition command for `bank details validation` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Maker-checker approval** | Expose authorized query/read projection and explicit domain transition command for `maker-checker approval` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Files/APIs** | Expose authorized query/read projection and explicit domain transition command for `files/apis` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Remittances** | Expose authorized query/read projection and explicit domain transition command for `remittances` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Status** | Expose authorized query/read projection and explicit domain transition command for `status` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |

| Boundary | Observed identity and implementation reference |
| --- | --- |
| Source package | [liberusoftware/module-accounting-bill-payments-api](../../../modules/source/liberusoftware--module-accounting-bill-payments-api.md) |
| Source package | [liberusoftware/module-accounting-bill-payments](../../../modules/source/liberusoftware--module-accounting-bill-payments.md) |

### Observed route declarations

These are literal excerpts, not runnable standalone route files or expanded final URLs. Read group middleware/prefixes, provider loading and the host route configuration together. Authentication middleware alone does not establish the controller/domain permission policy.

[modules/accounting-bill-payments-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/bill-payments')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [BillPaymentController::class, 'index'])->middleware('ability:accounting.bill-payments.read');
Route::post('/', [BillPaymentController::class, 'store'])->middleware('ability:accounting.bill-payments.write');
Route::get('/{payment}', [BillPaymentController::class, 'show'])->middleware('ability:accounting.bill-payments.read');
Route::get('/{payment}/optimization', [BillPaymentController::class, 'optimization'])->middleware('ability:accounting.bill-payments.read');
Route::post('/{payment}/request-approval', [BillPaymentController::class, 'requestApproval'])->middleware('ability:accounting.bill-payments.write');
Route::post('/{payment}/approve', [BillPaymentController::class, 'approve'])->middleware('ability:accounting.bill-payments.write');
Route::post('/{payment}/reject', [BillPaymentController::class, 'reject'])->middleware('ability:accounting.bill-payments.write');
```

### Observed controller entry points

The signatures identify request handlers to review; their argument names are not complete JSON schemas. Read their request validation, actor/tenant resolution, policy, serialization and error paths before writing a client.

| Controller source | Public handler signatures |
| --- | --- |
| [BillPaymentController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments-api/src/Http/Controllers/BillPaymentController.php) | `public function index(Request $request): mixed`<br>`public function store(Request $request, CreateBillPaymentProposal $action): BillPaymentResource`<br>`public function show(string $payment): BillPaymentResource`<br>`public function requestApproval(string $payment, RequestBillPaymentApproval $action): BillPaymentResource`<br>`public function approve(string $payment, ApproveBillPayment $action): BillPaymentResource`<br>`public function reject(Request $request, string $payment, RejectBillPayment $action): BillPaymentResource`<br>`public function optimization(string $payment, BillPaymentOptimizationQuery $query): mixed` |

### Observed domain queries, actions, and storage models

API controllers delegate to these observed core domain entry points and serialize only allowlisted DTO fields rather than raw storage models.

| Core query source | Observed signatures |
| --- | --- |
| [BillPaymentOptimizationQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Queries/BillPaymentOptimizationQuery.php) | `public function handle(BillPaymentProposal $payment): array` |

| Core action / service source | Observed signatures |
| --- | --- |
| [ApproveBillPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Actions/ApproveBillPayment.php) | `public function handle(BillPaymentProposal $payment): BillPaymentProposal` |
| [CreateBillPaymentProposal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Actions/CreateBillPaymentProposal.php) | `public function handle(array $attributes): BillPaymentProposal` |
| [MarkBillPaymentPaid.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Actions/MarkBillPaymentPaid.php) | `public function handle(BillPaymentProposal $payment): BillPaymentProposal` |
| [RejectBillPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Actions/RejectBillPayment.php) | `public function handle(BillPaymentProposal $payment, string $reason): BillPaymentProposal` |
| [RequestBillPaymentApproval.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Actions/RequestBillPaymentApproval.php) | `public function handle(BillPaymentProposal $payment): BillPaymentProposal` |
| [SubmitBillPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Actions/SubmitBillPayment.php) | `public function handle(BillPaymentProposal $payment, PaymentProviderAdapter $adapter): BillPaymentProposal` |
| [BillPaymentsPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments-api/src/Policies/BillPaymentsPolicy.php) | `public function viewAny(?object $user = null): bool`<br>`public function view(?object $user, object $payment): bool`<br>`public function create(?object $user = null): bool`<br>`public function update(?object $user, object $payment): bool` |

| Core storage model | Observed fillable fields (review for DTO allowlist) |
| --- | --- |
| [BillPaymentProposal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Models/BillPaymentProposal.php) | `team_id`, `supplier_id`, `bill_reference`, `amount`, `currency`, `due_date`, `discount_date`, `discount_rate`, `payment_date`, `bank_details`, `provider`, `provider_connection_id`, `payment_payload`, `idempotency_key`, `status`, `requested_by`, `approved_by`, `approved_at`, `submitted_at`, `paid_at`, `rejected_at`, `failure_code`, `failure_message`, `provider_reference`, `provider_result`, `remittance_reference`, `remittance_sent_at`, `metadata` |
| [Bill.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments-api/src/Models/Bill.php) | `vendor_id`, `bill_number`, `bill_date`, `due_date`, `subtotal_amount`, `tax_amount`, `total_amount`, `amount_paid`, `tax_rate_id`, `status`, `payment_status`, `purchase_order_id`, `reference_number`, `notes`, `document_path`, `approved_by`, `approved_at`, `approval_status`, `rejection_reason`, `team_id`, `is_recurring`, `recurrence_frequency`, `recurrence_start`, `recurrence_end`, `last_generated`, `qbo_id`, `qbo_sync_token`, `xero_id`, `sage_id` |
| [BillPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments-api/src/Models/BillPayment.php) | `bill_id`, `payment_date`, `amount`, `payment_method`, `reference_number`, `bank_account_id`, `notes` |

A client example is valid only after its exact request/response contract is established. Record required/nullable fields, business units, allowed values, operation identity/concurrency support, result/pagination envelope and recovery. An `Idempotency-Key` or `If-Match` example does not establish server support by itself.

## 4. OpenAPI schema

The matched source contains these machine-readable contract/schema files. Verify their version and parity with handlers; file presence does not prove deployed compatibility or a passing validation run.

- [openapi/v1/accounting-bill-payments.yaml](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments-api/openapi/v1/accounting-bill-payments.yaml)

For the target contract, define stable operation IDs, explicit request/resource/collection/error schemas, allowed audiences/scopes, actor/tenant resolution, field sensitivity, pagination/filter limits, concurrency and retry semantics. Use the real manifest identity and actual route namespace, not a guessed repository-derived package or path.

Validate/bundle the fragment, check supported-version compatibility and generate clients only from the reviewed contract. Retain the source/schema commit or release in client compatibility notes. See the [API architecture](../../../architecture/API.md), [source mapping](../SOURCE-MAPPING.md#bill-payments), and [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) guides.

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
- Add one-to-one architecture tests proving this package depends on and presents only `accounting-bill-payments`.
- Run independent installation, minimum/current compatibility, security, performance, generated-client smoke, and representative host-composition tests.
- Run Pest 5 with meaningful owned PHP targeting 100% line coverage; coverage complements contract, mutation, security, and failure assertions.

## 9. Definition of done

- The package name, manifest, Composer dependency, namespace, route prefix, and OpenAPI ownership all match `accounting-bill-payments`.
- The audience/operation matrix is complete, least-privilege, documented, and enforced in CI.
- Schemas, implementation, examples, errors, SDK/client evidence, and documentation agree.
- Authorization, tenant/field isolation, idempotency/concurrency, limits, audit, observability, compatibility, and recovery tests pass.
- The API fragment aggregates without collisions and the independent package can be installed, tested, versioned, upgraded, and removed safely.
