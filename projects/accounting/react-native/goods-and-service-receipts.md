# Goods And Service Receipts React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#goods-and-service-receipts). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-goods-and-service-receipts-react-native
**Matching core package:** module-accounting-goods-and-service-receipts ([implementation](../core/goods-and-service-receipts.md))
**Matching API package:** module-accounting-goods-and-service-receipts-api ([contract](../api/goods-and-service-receipts.md))

## Implementation plan

This adapter presents Goods And Service Receipts for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Goods And Service Receipts API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/goods-and-service-receipts.md), and [API module](../api/goods-and-service-receipts.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `goods-and-service-receipts`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/goods-and-service-receipts.md)) |
| Capability React Native module skeleton | [`module-accounting-goods-and-service-receipts-react-native`](https://github.com/liberusoftware/module-accounting-goods-and-service-receipts-react-native) (`@liberusoftware/module-accounting-goods-and-service-receipts-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Receipts** | Progressive mobile list/detail/sheet flow for `receipts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Service confirmation** | Progressive mobile list/detail/sheet flow for `service confirmation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Quantities** | Progressive mobile list/detail/sheet flow for `quantities` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Variance** | Progressive mobile list/detail/sheet flow for `variance` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Returns** | Progressive mobile list/detail/sheet flow for `returns` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Attachments** | Progressive mobile list/detail/sheet flow for `attachments` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Inventory/project references** | Progressive mobile list/detail/sheet flow for `inventory/project references` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Accrual events** | Progressive mobile list/detail/sheet flow for `accrual events` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ReceiptQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Queries/ReceiptQuery.php) | `public function paginate(?int $teamId = null, ?ReceiptStatus $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function variance(Receipt $receipt): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddReceiptAttachment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Actions/AddReceiptAttachment.php) | `public function handle(Receipt $receipt, array $a): ReceiptAttachment` |
| [AddReceiptLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Actions/AddReceiptLine.php) | `public function handle(Receipt $receipt, array $a): ReceiptLine` |
| [ConfirmService.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Actions/ConfirmService.php) | `public function handle(Receipt $receipt, array $a): ServiceConfirmation` |
| [CreateReceipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Actions/CreateReceipt.php) | `public function handle(array $a): Receipt` |
| [PostAccrual.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Actions/PostAccrual.php) | `public function handle(Receipt $receipt, array $a): ReceiptAccrual` |
| [ReturnReceipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Actions/ReturnReceipt.php) | `public function handle(Receipt $receipt, array $a): ReceiptReturn` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Receipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Models/Receipt.php) | `team_id`, `receipt_ref`, `receipt_type`, `supplier_ref`, `purchase_order_ref`, `currency`, `status`, `received_at`, `inventory_ref`, `project_ref`, `total_value`, `metadata` |
| [ReceiptAccrual.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Models/ReceiptAccrual.php) | `receipt_id`, `accrual_ref`, `amount`, `currency`, `period_ref`, `status`, `posted_at`, `source_ref`, `metadata` |
| [ReceiptAttachment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Models/ReceiptAttachment.php) | `receipt_id`, `attachment_ref`, `kind`, `file_ref`, `description`, `checksum`, `attached_by`, `attached_at`, `metadata` |
| [ReceiptLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Models/ReceiptLine.php) | `receipt_id`, `line_ref`, `item_ref`, `description`, `ordered_quantity`, `received_quantity`, `returned_quantity`, `unit_price`, `line_value`, `variance_quantity`, `variance_value`, `inventory_ref`, `project_ref`, `metadata` |
| [ReceiptReturn.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Models/ReceiptReturn.php) | `receipt_id`, `return_ref`, `line_ref`, `quantity`, `value`, `reason`, `source_ref`, `returned_at`, `metadata` |
| [ServiceConfirmation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts/src/Models/ServiceConfirmation.php) | `receipt_id`, `confirmation_ref`, `service_period`, `quantity`, `value`, `confirmed_by`, `confirmed_at`, `comment`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ReceiptsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-goods-and-service-receipts-api/src/Http/Controllers/ReceiptsController.php) | `public function __construct(private readonly ReceiptQuery $query)`<br>`public function index(Request $r): ReceiptResource`<br>`public function store(Request $r, CreateReceipt $a): ReceiptResource`<br>`public function show(Receipt $receipt): ReceiptResource`<br>`public function line(Request $r, Receipt $receipt, AddReceiptLine $a): ReceiptResource`<br>`public function confirmService(Request $r, Receipt $receipt, ConfirmService $a): ReceiptResource`<br>`public function return(Request $r, Receipt $receipt, ReturnReceipt $a): ReceiptResource`<br>`public function attachment(Request $r, Receipt $receipt, AddReceiptAttachment $a): ReceiptResource`<br>`public function accrual(Request $r, Receipt $receipt, PostAccrual $a): ReceiptResource`<br>`public function variance(Receipt $receipt, ReceiptQuery $q): JsonResponse` |

**Observed route declarations:**

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
<!-- layer-implementation-plan:end -->
