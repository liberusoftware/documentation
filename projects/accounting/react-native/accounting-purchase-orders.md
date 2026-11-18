# Accounting Purchase Orders React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-purchase-orders). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-purchase-orders-react-native
**Matching core package:** module-accounting-accounting-purchase-orders ([implementation](../core/accounting-purchase-orders.md))
**Matching API package:** module-accounting-accounting-purchase-orders-api ([contract](../api/accounting-purchase-orders.md))

## Implementation plan

This adapter presents Accounting Purchase Orders for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Purchase Orders API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/accounting-purchase-orders.md), and [API module](../api/accounting-purchase-orders.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `accounting-purchase-orders`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-purchase-orders.md)) |
| Capability React Native module skeleton | [`module-accounting-purchase-orders-react-native`](https://github.com/liberusoftware/module-accounting-purchase-orders-react-native) (`@liberusoftware/module-accounting-purchase-orders-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Supplier items** | Progressive mobile list/detail/sheet flow for `supplier items` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Prices** | Progressive mobile list/detail/sheet flow for `prices` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Quantities** | Progressive mobile list/detail/sheet flow for `quantities` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Delivery** | Progressive mobile list/detail/sheet flow for `delivery` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Approval** | Progressive mobile list/detail/sheet flow for `approval` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Issue** | Progressive mobile list/detail/sheet flow for `issue` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Receipts** | Progressive mobile list/detail/sheet flow for `receipts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Partials** | Progressive mobile list/detail/sheet flow for `partials` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Changes** | Progressive mobile list/detail/sheet flow for `changes` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Closure** | Progressive mobile list/detail/sheet flow for `closure` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Commitments** | Progressive mobile list/detail/sheet flow for `commitments` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreatePurchaseOrder.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-orders/src/Actions/CreatePurchaseOrder.php) | `public function handle(array $attributes, array $lines): PurchaseOrder` |
| [RecordPurchaseOrderChange.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-orders/src/Actions/RecordPurchaseOrderChange.php) | `public function handle(PurchaseOrder $order, array $attributes): PurchaseOrderChange` |
| [RecordPurchaseReceipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-orders/src/Actions/RecordPurchaseReceipt.php) | `public function handle(PurchaseOrder $order, array $attributes): PurchaseReceipt` |
| [TransitionPurchaseOrder.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-orders/src/Actions/TransitionPurchaseOrder.php) | `public function handle(PurchaseOrder $order, PurchaseOrderStatus $status, array $attributes = []): PurchaseOrder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PurchaseOrder.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-orders/src/Models/PurchaseOrder.php) | `team_id`, `supplier_ref`, `order_number`, `currency`, `order_date`, `expected_delivery_on`, `total_amount`, `status`, `commitment_ref`, `source_requisition_ref`, `notes`, `metadata` |
| [PurchaseOrderChange.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-orders/src/Models/PurchaseOrderChange.php) | `order_id`, `version`, `changes`, `reason`, `actor_ref`, `approved_at`, `metadata` |
| [PurchaseOrderLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-orders/src/Models/PurchaseOrderLine.php) | `order_id`, `item_ref`, `description`, `quantity`, `unit_price`, `received_quantity`, `delivery_metadata`, `metadata` |
| [PurchaseReceipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-orders/src/Models/PurchaseReceipt.php) | `order_id`, `receipt_ref`, `received_on`, `lines`, `status`, `document_ref`, `metadata` |
| [PurchaseOrder.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-orders-api/src/Models/PurchaseOrder.php) | `supplier_id`, `po_number`, `order_date`, `expected_delivery_date`, `total_amount`, `status`, `notes`, `purchase_request_id`, `team_id` |

| Observed API controller | Handler signatures |
| --- | --- |
| [PurchaseOrdersController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-orders-api/src/Http/Controllers/PurchaseOrdersController.php) | `public function index(Request $request): AnonymousResourceCollection`<br>`public function store(Request $request, CreatePurchaseOrder $action): JsonResponse`<br>`public function show(Request $request, PurchaseOrder $order): PurchaseOrderResource`<br>`public function transition(Request $request, PurchaseOrder $order, TransitionPurchaseOrder $action): PurchaseOrderResource`<br>`public function receipt(Request $request, PurchaseOrder $order, RecordPurchaseReceipt $action): JsonResponse`<br>`public function change(Request $request, PurchaseOrder $order, RecordPurchaseOrderChange $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-purchase-orders-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-orders-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/purchase-orders')->group(function (): void {
Route::middleware('ability:accounting.purchase-orders.read')->group(function (): void {
Route::get('/', [PurchaseOrdersController::class, 'index']);
Route::get('/{order}', [PurchaseOrdersController::class, 'show']);
Route::middleware('ability:accounting.purchase-orders.write')->group(function (): void {
Route::post('/', [PurchaseOrdersController::class, 'store']);
Route::post('/{order}/transition', [PurchaseOrdersController::class, 'transition']);
Route::post('/{order}/receipts', [PurchaseOrdersController::class, 'receipt']);
Route::post('/{order}/changes', [PurchaseOrdersController::class, 'change']);
```
<!-- layer-implementation-plan:end -->
