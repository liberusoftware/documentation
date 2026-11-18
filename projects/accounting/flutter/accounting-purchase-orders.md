# Accounting Purchase Orders Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-purchase-orders). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-purchase-orders-flutter
**Matching core package:** module-accounting-accounting-purchase-orders ([implementation](../core/accounting-purchase-orders.md))
**Matching API package:** module-accounting-accounting-purchase-orders-api ([contract](../api/accounting-purchase-orders.md))

## Implementation plan

This adapter presents Accounting Purchase Orders for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Purchase Orders API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/accounting-purchase-orders.md), and [API module](../api/accounting-purchase-orders.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `accounting-purchase-orders`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-accounting-erp-mobile-flutter`](https://github.com/liberusoftware/project-accounting-erp-mobile-flutter) | [`module-accounting-purchase-orders-flutter`](https://github.com/liberusoftware/module-accounting-purchase-orders-flutter) (`module_accounting_purchase_orders_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-accounting-erp-dart-mobile`](https://github.com/liberusoftware/project-accounting-erp-dart-mobile) | [`module-accounting-purchase-orders-dart-mobile`](https://github.com/liberusoftware/module-accounting-purchase-orders-dart-mobile) (`module_accounting_purchase_orders_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-accounting-erp-dart-desktop`](https://github.com/liberusoftware/project-accounting-erp-dart-desktop) | [`module-accounting-purchase-orders-dart-desktop`](https://github.com/liberusoftware/module-accounting-purchase-orders-dart-desktop) (`module_accounting_purchase_orders_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | [API plan](../api/accounting-purchase-orders.md) · [Core plan](../core/accounting-purchase-orders.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Supplier items** | Adaptive mobile cards/sheets for `supplier items` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `supplier items` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Prices** | Adaptive mobile cards/sheets for `prices` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `prices` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Quantities** | Adaptive mobile cards/sheets for `quantities` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `quantities` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Delivery** | Adaptive mobile cards/sheets for `delivery` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `delivery` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Approval** | Adaptive mobile cards/sheets for `approval` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `approval` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Issue** | Adaptive mobile cards/sheets for `issue` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `issue` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Receipts** | Adaptive mobile cards/sheets for `receipts` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `receipts` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Partials** | Adaptive mobile cards/sheets for `partials` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `partials` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Changes** | Adaptive mobile cards/sheets for `changes` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `changes` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Closure** | Adaptive mobile cards/sheets for `closure` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `closure` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Commitments** | Adaptive mobile cards/sheets for `commitments` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `commitments` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

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
