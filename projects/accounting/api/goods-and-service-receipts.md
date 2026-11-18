# Accounting: Goods and Service Receipts API

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#goods-and-service-receipts). Observed identity: [`liberusoftware/module-accounting-goods-and-service-receipts-api`](../../../modules/source/liberusoftware--module-accounting-goods-and-service-receipts-api.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one API module specification

**Proposed API design identifier:** `module-accounting-goods-and-service-receipts-api`<br>
**Matching domain module:** `accounting-goods-and-service-receipts`  
**Application:** Accounting  
**Source feature:** [Goods and Service Receipts](../features/goods-and-service-receipts.md)  
**Architecture:** [API.md](../../../architecture/API.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional API presentation package exposes approved HTTP operations for the Goods and Service Receipts domain module. It presents exactly one independent module, delegates all authoritative behavior to that module's public actions/queries/policies, and contains no other module's API logic.

The domain capability includes:

- Receipts
- Service confirmation
- Quantities
- Variance
- Returns
- Attachments
- Inventory/project references
- Accrual events

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
| Next.js React | [`project-accounting-erp-next-react`](https://github.com/liberusoftware/project-accounting-erp-next-react) | [Next.js plan](../nextjs/goods-and-service-receipts.md) | Server Component / Route Handler / BFF or Sanctum SPA with `no-store` private reads |
| Nuxt 4 Vue | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | [Nuxt plan](../nuxt/goods-and-service-receipts.md) | Nitro SSR / BFF or Sanctum SPA with actor/tenant-scoped `useFetch` keys |
| React Native Expo | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | [React Native plan](../react-native/goods-and-service-receipts.md) | Typed client with Keychain/Keystore token storage, PKCE/Sanctum, and idempotent retries |
| Flutter mobile | [`project-accounting-erp-mobile-flutter`](https://github.com/liberusoftware/project-accounting-erp-mobile-flutter) | [Flutter plan](../flutter/goods-and-service-receipts.md) | Typed Dart DTOs and platform-secure credentials on iOS and Android |
| Dart mobile & desktop | [`project-accounting-erp-dart-mobile`](https://github.com/liberusoftware/project-accounting-erp-dart-mobile) · [`project-accounting-erp-dart-desktop`](https://github.com/liberusoftware/project-accounting-erp-dart-desktop) | [Flutter & Dart plan](../flutter/goods-and-service-receipts.md) | Separate mobile and desktop native hosts consuming the same versioned `/api/v1` contract |

### Feature-to-API capability and operation matrix

| Feature / aspect | HTTP query and command intent | DTO allowlist, concurrency, and error contract |
| --- | --- | --- |
| **Receipts** | Expose authorized query/read projection and explicit domain transition command for `receipts` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Service confirmation** | Expose authorized query/read projection and explicit domain transition command for `service confirmation` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Quantities** | Expose authorized query/read projection and explicit domain transition command for `quantities` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Variance** | Expose authorized query/read projection and explicit domain transition command for `variance` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Returns** | Expose authorized query/read projection and explicit domain transition command for `returns` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Attachments** | Expose authorized query/read projection and explicit domain transition command for `attachments` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Inventory/project references** | Expose authorized query/read projection and explicit domain transition command for `inventory/project references` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Accrual events** | Expose authorized query/read projection and explicit domain transition command for `accrual events` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |

| Boundary | Observed identity and implementation reference |
| --- | --- |
| Source package | [liberusoftware/module-accounting-goods-and-service-receipts-api](../../../modules/source/liberusoftware--module-accounting-goods-and-service-receipts-api.md) |
| Source package | [liberusoftware/module-accounting-goods-and-service-receipts](../../../modules/source/liberusoftware--module-accounting-goods-and-service-receipts.md) |

### Observed route declarations

These are literal excerpts, not runnable standalone route files or expanded final URLs. Read group middleware/prefixes, provider loading and the host route configuration together. Authentication middleware alone does not establish the controller/domain permission policy.

[modules/accounting-goods-and-service-receipts-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/goods-and-service-receipts')->group(function (): void {
Route::get('/', [ReceiptsController::class, 'index'])->name('accounting.receipts.list');
Route::post('/', [ReceiptsController::class, 'store'])->name('accounting.receipts.create');
Route::get('/{receipt}', [ReceiptsController::class, 'show'])->name('accounting.receipts.show');
Route::post('/{receipt}/lines', [ReceiptsController::class, 'line'])->name('accounting.receipts.line');
Route::post('/{receipt}/service-confirmation', [ReceiptsController::class, 'confirmService'])->name('accounting.receipts.confirm-service');
Route::post('/{receipt}/returns', [ReceiptsController::class, 'return'])->name('accounting.receipts.return');
Route::post('/{receipt}/attachments', [ReceiptsController::class, 'attachment'])->name('accounting.receipts.attachment');
Route::post('/{receipt}/accruals', [ReceiptsController::class, 'accrual'])->name('accounting.receipts.accrual');
Route::get('/{receipt}/variance', [ReceiptsController::class, 'variance'])->name('accounting.receipts.variance');
```

### Observed controller entry points

The signatures identify request handlers to review; their argument names are not complete JSON schemas. Read their request validation, actor/tenant resolution, policy, serialization and error paths before writing a client.

| Controller source | Public handler signatures |
| --- | --- |
| [ReceiptsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts-api/src/Http/Controllers/ReceiptsController.php) | `public function __construct(private readonly ReceiptQuery $query)`<br>`public function index(Request $r): ReceiptResource`<br>`public function store(Request $r, CreateReceipt $a): ReceiptResource`<br>`public function show(Receipt $receipt): ReceiptResource`<br>`public function line(Request $r, Receipt $receipt, AddReceiptLine $a): ReceiptResource`<br>`public function confirmService(Request $r, Receipt $receipt, ConfirmService $a): ReceiptResource`<br>`public function return(Request $r, Receipt $receipt, ReturnReceipt $a): ReceiptResource`<br>`public function attachment(Request $r, Receipt $receipt, AddReceiptAttachment $a): ReceiptResource`<br>`public function accrual(Request $r, Receipt $receipt, PostAccrual $a): ReceiptResource`<br>`public function variance(Receipt $receipt, ReceiptQuery $q): JsonResponse` |

### Observed domain queries, actions, and storage models

API controllers delegate to these observed core domain entry points and serialize only allowlisted DTO fields rather than raw storage models.

| Core query source | Observed signatures |
| --- | --- |
| [ReceiptQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Queries/ReceiptQuery.php) | `public function paginate(?int $teamId = null, ?ReceiptStatus $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function variance(Receipt $receipt): array` |

| Core action / service source | Observed signatures |
| --- | --- |
| [AddReceiptAttachment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Actions/AddReceiptAttachment.php) | `public function handle(Receipt $receipt, array $a): ReceiptAttachment` |
| [AddReceiptLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Actions/AddReceiptLine.php) | `public function handle(Receipt $receipt, array $a): ReceiptLine` |
| [ConfirmService.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Actions/ConfirmService.php) | `public function handle(Receipt $receipt, array $a): ServiceConfirmation` |
| [CreateReceipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Actions/CreateReceipt.php) | `public function handle(array $a): Receipt` |
| [PostAccrual.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Actions/PostAccrual.php) | `public function handle(Receipt $receipt, array $a): ReceiptAccrual` |
| [ReturnReceipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Actions/ReturnReceipt.php) | `public function handle(Receipt $receipt, array $a): ReceiptReturn` |

| Core storage model | Observed fillable fields (review for DTO allowlist) |
| --- | --- |
| [Receipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Models/Receipt.php) | `team_id`, `receipt_ref`, `receipt_type`, `supplier_ref`, `purchase_order_ref`, `currency`, `status`, `received_at`, `inventory_ref`, `project_ref`, `total_value`, `metadata` |
| [ReceiptAccrual.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Models/ReceiptAccrual.php) | `receipt_id`, `accrual_ref`, `amount`, `currency`, `period_ref`, `status`, `posted_at`, `source_ref`, `metadata` |
| [ReceiptAttachment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Models/ReceiptAttachment.php) | `receipt_id`, `attachment_ref`, `kind`, `file_ref`, `description`, `checksum`, `attached_by`, `attached_at`, `metadata` |
| [ReceiptLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Models/ReceiptLine.php) | `receipt_id`, `line_ref`, `item_ref`, `description`, `ordered_quantity`, `received_quantity`, `returned_quantity`, `unit_price`, `line_value`, `variance_quantity`, `variance_value`, `inventory_ref`, `project_ref`, `metadata` |
| [ReceiptReturn.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Models/ReceiptReturn.php) | `receipt_id`, `return_ref`, `line_ref`, `quantity`, `value`, `reason`, `source_ref`, `returned_at`, `metadata` |
| [ServiceConfirmation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Models/ServiceConfirmation.php) | `receipt_id`, `confirmation_ref`, `service_period`, `quantity`, `value`, `confirmed_by`, `confirmed_at`, `comment`, `metadata` |

A client example is valid only after its exact request/response contract is established. Record required/nullable fields, business units, allowed values, operation identity/concurrency support, result/pagination envelope and recovery. An `Idempotency-Key` or `If-Match` example does not establish server support by itself.

## 4. OpenAPI schema

The matched source contains these machine-readable contract/schema files. Verify their version and parity with handlers; file presence does not prove deployed compatibility or a passing validation run.

- [openapi/v1/accounting-goods-and-service-receipts.yaml](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts-api/openapi/v1/accounting-goods-and-service-receipts.yaml)

For the target contract, define stable operation IDs, explicit request/resource/collection/error schemas, allowed audiences/scopes, actor/tenant resolution, field sensitivity, pagination/filter limits, concurrency and retry semantics. Use the real manifest identity and actual route namespace, not a guessed repository-derived package or path.

Validate/bundle the fragment, check supported-version compatibility and generate clients only from the reviewed contract. Retain the source/schema commit or release in client compatibility notes. See the [API architecture](../../../architecture/API.md), [source mapping](../SOURCE-MAPPING.md#goods-and-service-receipts), and [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) guides.

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
- Add one-to-one architecture tests proving this package depends on and presents only `accounting-goods-and-service-receipts`.
- Run independent installation, minimum/current compatibility, security, performance, generated-client smoke, and representative host-composition tests.
- Run Pest 5 with meaningful owned PHP targeting 100% line coverage; coverage complements contract, mutation, security, and failure assertions.

## 9. Definition of done

- The package name, manifest, Composer dependency, namespace, route prefix, and OpenAPI ownership all match `accounting-goods-and-service-receipts`.
- The audience/operation matrix is complete, least-privilege, documented, and enforced in CI.
- Schemas, implementation, examples, errors, SDK/client evidence, and documentation agree.
- Authorization, tenant/field isolation, idempotency/concurrency, limits, audit, observability, compatibility, and recovery tests pass.
- The API fragment aggregates without collisions and the independent package can be installed, tested, versioned, upgraded, and removed safely.
