# Inventory Accounting React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#inventory-accounting). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-inventory-accounting-react-native
**Matching core package:** module-accounting-inventory-accounting ([implementation](../core/inventory-accounting.md))
**Matching API package:** module-accounting-inventory-accounting-api ([contract](../api/inventory-accounting.md))

## Implementation plan

This adapter presents Inventory Accounting for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Inventory Accounting API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/inventory-accounting.md), and [API module](../api/inventory-accounting.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `inventory-accounting`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/inventory-accounting.md)) |
| Capability React Native module skeleton | [`module-accounting-inventory-accounting-react-native`](https://github.com/liberusoftware/module-accounting-inventory-accounting-react-native) (`@liberusoftware/module-accounting-inventory-accounting-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Perpetual/periodic methods** | Progressive mobile list/detail/sheet flow for `perpetual/periodic methods` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Valuation** | Progressive mobile list/detail/sheet flow for `valuation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Cost layers** | Progressive mobile list/detail/sheet flow for `cost layers` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Cost of sales** | Progressive mobile list/detail/sheet flow for `cost of sales` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Landed cost** | Progressive mobile list/detail/sheet flow for `landed cost` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Adjustments** | Progressive mobile list/detail/sheet flow for `adjustments` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Write-downs** | Progressive mobile list/detail/sheet flow for `write-downs` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Subledger reconciliation** | Progressive mobile list/detail/sheet flow for `subledger reconciliation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

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
