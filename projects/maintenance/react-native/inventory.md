# Inventory React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#inventory). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-maintenance-inventory-react-native
**Matching core package:** module-maintenance-inventory ([implementation](../core/inventory.md))
**Matching API package:** module-maintenance-inventory-api ([contract](../api/inventory.md))

## Implementation plan

This adapter presents Inventory for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Inventory API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/inventory.md), and [API module](../api/inventory.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `inventory`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-maintenance-mobile-react`](https://github.com/liberusoftware/project-maintenance-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/inventory.md)) |
| Capability React Native module skeleton | [`module-maintenance-inventory-react-native`](https://github.com/liberusoftware/module-maintenance-inventory-react-native) (`@liberusoftware/module-maintenance-inventory-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Parts** | Progressive mobile list/detail/sheet flow for `parts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-maintenance-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Warehouses/vans** | Progressive mobile list/detail/sheet flow for `warehouses/vans` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-maintenance-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Stock ledger** | Progressive mobile list/detail/sheet flow for `stock ledger` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-maintenance-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Reservations** | Progressive mobile list/detail/sheet flow for `reservations` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-maintenance-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Issues/returns** | Progressive mobile list/detail/sheet flow for `issues/returns` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-maintenance-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Transfers** | Progressive mobile list/detail/sheet flow for `transfers` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-maintenance-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Reorder** | Progressive mobile list/detail/sheet flow for `reorder` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-maintenance-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Counts** | Progressive mobile list/detail/sheet flow for `counts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-maintenance-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AdjustStock.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/AdjustStock.php) | `public function handle(int $teamId, StockItem $item, int $delta, string $reason = 'adjustment', ?int $userId = null, ?string $notes = null): StockItem` |
| [CreateStockItem.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/CreateStockItem.php) | `public function handle(int $teamId, array $attributes): StockItem` |
| [DeleteStockItem.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/DeleteStockItem.php) | `public function handle(int $teamId, StockItem $item): void` |
| [IssueStock.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/IssueStock.php) | `public function __construct(private readonly AdjustStock $adjustStock)`<br>`public function handle(int $teamId, StockItem $item, int $quantity, ?int $userId = null, ?string $notes = null): StockItem` |
| [ReleaseReservedStock.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/ReleaseReservedStock.php) | `public function handle(int $teamId, StockItem $item, int $quantity): StockItem` |
| [ReserveStock.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/ReserveStock.php) | `public function handle(int $teamId, StockItem $item, int $quantity): StockItem` |
| [ReturnStock.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/ReturnStock.php) | `public function __construct(private readonly AdjustStock $adjustStock)`<br>`public function handle(int $teamId, StockItem $item, int $quantity, ?int $userId = null, ?string $notes = null): StockItem` |
| [UpdateStockItem.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Actions/UpdateStockItem.php) | `public function handle(int $teamId, StockItem $item, array $attributes): StockItem` |
| [StockItemPolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Policies/StockItemPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, StockItem $item): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, StockItem $item): bool`<br>`public function delete(object $user, StockItem $item): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [StockItem.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Models/StockItem.php) | `team_id`, `part_number`, `name`, `description`, `category`, `location`, `supplier_name`, `lead_time_days`, `notes`, `quantity`, `reorder_level`, `reorder_quantity`, `unit`, `unit_cost` |
| [StockMovement.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory/src/Models/StockMovement.php) | `team_id`, `stock_item_id`, `user_id`, `delta`, `quantity_before`, `quantity_after`, `reason`, `notes` |

| Observed API controller | Handler signatures |
| --- | --- |
| [StockItemController.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory-api/src/Http/Controllers/StockItemController.php) | `public function index(Request $r): JsonResponse`<br>`public function store(Request $r, CreateStockItem $create): JsonResponse`<br>`public function show(Request $r, StockItem $stockItem): JsonResponse`<br>`public function adjust(Request $r, StockItem $stockItem, AdjustStock $adjust): JsonResponse`<br>`public function reserve(Request $r, StockItem $stockItem, ReserveStock $reserve): JsonResponse`<br>`public function release(Request $r, StockItem $stockItem, ReleaseReservedStock $release): JsonResponse`<br>`public function issue(Request $r, StockItem $stockItem, IssueStock $issue): JsonResponse`<br>`public function return(Request $r, StockItem $stockItem, ReturnStock $returnStock): JsonResponse`<br>`public function update(Request $r, StockItem $stockItem, UpdateStockItem $update): JsonResponse`<br>`public function destroy(Request $r, StockItem $stockItem, DeleteStockItem $delete): JsonResponse`<br>`public function movements(Request $r, StockItem $stockItem): JsonResponse` |

**Observed route declarations:**

[modules/module-maintenance-inventory-api/routes/api.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-inventory-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/maintenance/inventory')->group(function (): void {
Route::get('/', [StockItemController::class, 'index']);
Route::post('/', [StockItemController::class, 'store']);
Route::get('/{stockItem}', [StockItemController::class, 'show']);
Route::patch('/{stockItem}', [StockItemController::class, 'update']);
Route::delete('/{stockItem}', [StockItemController::class, 'destroy']);
Route::post('/{stockItem}/adjust', [StockItemController::class, 'adjust']);
Route::post('/{stockItem}/reserve', [StockItemController::class, 'reserve']);
Route::post('/{stockItem}/release', [StockItemController::class, 'release']);
Route::post('/{stockItem}/issue', [StockItemController::class, 'issue']);
Route::post('/{stockItem}/return', [StockItemController::class, 'return']);
Route::get('/{stockItem}/movements', [StockItemController::class, 'movements']);
```
<!-- layer-implementation-plan:end -->
