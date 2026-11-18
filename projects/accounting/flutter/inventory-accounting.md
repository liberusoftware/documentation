# Inventory Accounting Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#inventory-accounting). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-inventory-accounting-flutter
**Matching core package:** module-accounting-inventory-accounting ([implementation](../core/inventory-accounting.md))
**Matching API package:** module-accounting-inventory-accounting-api ([contract](../api/inventory-accounting.md))

## Implementation plan

This adapter presents Inventory Accounting for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Inventory Accounting API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/inventory-accounting.md), and [API module](../api/inventory-accounting.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `inventory-accounting`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-accounting-erp-mobile-flutter`](https://github.com/liberusoftware/project-accounting-erp-mobile-flutter) | [`module-accounting-inventory-accounting-flutter`](https://github.com/liberusoftware/module-accounting-inventory-accounting-flutter) (`module_accounting_inventory_accounting_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-accounting-erp-dart-mobile`](https://github.com/liberusoftware/project-accounting-erp-dart-mobile) | [`module-accounting-inventory-accounting-dart-mobile`](https://github.com/liberusoftware/module-accounting-inventory-accounting-dart-mobile) (`module_accounting_inventory_accounting_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-accounting-erp-dart-desktop`](https://github.com/liberusoftware/project-accounting-erp-dart-desktop) | [`module-accounting-inventory-accounting-dart-desktop`](https://github.com/liberusoftware/module-accounting-inventory-accounting-dart-desktop) (`module_accounting_inventory_accounting_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | [API plan](../api/inventory-accounting.md) · [Core plan](../core/inventory-accounting.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Perpetual/periodic methods** | Adaptive mobile cards/sheets for `perpetual/periodic methods` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `perpetual/periodic methods` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Valuation** | Adaptive mobile cards/sheets for `valuation` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `valuation` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Cost layers** | Adaptive mobile cards/sheets for `cost layers` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `cost layers` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Cost of sales** | Adaptive mobile cards/sheets for `cost of sales` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `cost of sales` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Landed cost** | Adaptive mobile cards/sheets for `landed cost` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `landed cost` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Adjustments** | Adaptive mobile cards/sheets for `adjustments` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `adjustments` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Write-downs** | Adaptive mobile cards/sheets for `write-downs` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `write-downs` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Subledger reconciliation** | Adaptive mobile cards/sheets for `subledger reconciliation` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `subledger reconciliation` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [InventoryQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Queries/InventoryQuery.php) | `public function paginate(?int $teamId = null, ?InventoryStatus $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function valuation(InventoryItem $item): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AdjustInventory.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Actions/AdjustInventory.php) | `public function handle(InventoryItem $item, array $attributes): InventoryAdjustment` |
| [ApplyLandedCost.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Actions/ApplyLandedCost.php) | `public function handle(InventoryItem $item, array $attributes): LandedCost` |
| [CreateInventoryItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Actions/CreateInventoryItem.php) | `public function handle(array $attributes): InventoryItem` |
| [IssueInventory.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Actions/IssueInventory.php) | `public function handle(InventoryItem $item, array $attributes): float` |
| [ReceiveInventory.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Actions/ReceiveInventory.php) | `public function handle(InventoryItem $item, array $attributes): CostLayer` |
| [ReconcileInventory.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Actions/ReconcileInventory.php) | `public function handle(array $attributes, ?InventoryItem $item = null): InventoryReconciliation` |
| [WriteDownInventory.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Actions/WriteDownInventory.php) | `public function handle(InventoryItem $item, array $attributes): InventoryWriteDown` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CostLayer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Models/CostLayer.php) | `item_id`, `layer_ref`, `received_at`, `quantity_received`, `quantity_remaining`, `unit_cost`, `total_cost`, `source_ref`, `metadata` |
| [InventoryAdjustment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Models/InventoryAdjustment.php) | `item_id`, `adjustment_ref`, `quantity_delta`, `value_delta`, `reason`, `actor_ref`, `adjusted_at`, `metadata` |
| [InventoryItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Models/InventoryItem.php) | `team_id`, `item_ref`, `description`, `warehouse_ref`, `currency`, `valuation_method`, `status`, `quantity_on_hand`, `inventory_value`, `metadata` |
| [InventoryMovement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Models/InventoryMovement.php) | `item_id`, `movement_ref`, `movement_type`, `quantity`, `unit_cost`, `total_cost`, `source_ref`, `occurred_at`, `metadata` |
| [InventoryReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Models/InventoryReconciliation.php) | `team_id`, `reconciliation_ref`, `period_ref`, `subledger_value`, `general_ledger_value`, `variance`, `status`, `actor_ref`, `reconciled_at`, `metadata` |
| [InventoryWriteDown.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Models/InventoryWriteDown.php) | `item_id`, `write_down_ref`, `amount`, `reason`, `actor_ref`, `written_down_at`, `metadata` |
| [LandedCost.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting/src/Models/LandedCost.php) | `item_id`, `cost_ref`, `amount`, `allocation_basis`, `source_ref`, `allocated_at`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [InventoryAccountingController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting-api/src/Http/Controllers/InventoryAccountingController.php) | `public function __construct(private readonly InventoryQuery $query)`<br>`public function index(Request $request): InventoryItemResource`<br>`public function store(Request $request, CreateInventoryItem $action): InventoryItemResource`<br>`public function show(InventoryItem $item): InventoryItemResource`<br>`public function receive(Request $request, InventoryItem $item, ReceiveInventory $action): InventoryItemResource`<br>`public function issue(Request $request, InventoryItem $item, IssueInventory $action): JsonResponse`<br>`public function adjust(Request $request, InventoryItem $item, AdjustInventory $action): InventoryItemResource`<br>`public function landed(Request $request, InventoryItem $item, ApplyLandedCost $action): InventoryItemResource`<br>`public function writeDown(Request $request, InventoryItem $item, WriteDownInventory $action): InventoryItemResource`<br>`public function valuation(InventoryItem $item, InventoryQuery $query): JsonResponse`<br>`public function reconcile(Request $request, ReconcileInventory $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-inventory-accounting-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-inventory-accounting-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/inventory-accounting')->group(function (): void {
Route::get('/', [InventoryAccountingController::class, 'index'])->name('accounting.inventory-accounting.list');
Route::post('/', [InventoryAccountingController::class, 'store'])->name('accounting.inventory-accounting.create');
Route::get('/{item}', [InventoryAccountingController::class, 'show'])->name('accounting.inventory-accounting.show');
Route::post('/{item}/receipts', [InventoryAccountingController::class, 'receive'])->name('accounting.inventory-accounting.receive');
Route::post('/{item}/issues', [InventoryAccountingController::class, 'issue'])->name('accounting.inventory-accounting.issue');
Route::post('/{item}/adjustments', [InventoryAccountingController::class, 'adjust'])->name('accounting.inventory-accounting.adjust');
Route::post('/{item}/landed-costs', [InventoryAccountingController::class, 'landed'])->name('accounting.inventory-accounting.landed');
Route::post('/{item}/write-downs', [InventoryAccountingController::class, 'writeDown'])->name('accounting.inventory-accounting.write-down');
Route::get('/{item}/valuation', [InventoryAccountingController::class, 'valuation'])->name('accounting.inventory-accounting.valuation');
Route::post('/reconciliations', [InventoryAccountingController::class, 'reconcile'])->name('accounting.inventory-accounting.reconcile');
```
<!-- layer-implementation-plan:end -->
