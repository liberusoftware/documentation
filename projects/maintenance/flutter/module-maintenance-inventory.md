# Module Maintenance Inventory Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-maintenance-inventory). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-maintenance-module-maintenance-inventory-flutter
**Matching core package:** module-maintenance-module-maintenance-inventory ([implementation](../core/module-maintenance-inventory.md))
**Matching API package:** module-maintenance-module-maintenance-inventory-api ([contract](../api/module-maintenance-inventory.md))

## Implementation plan

This adapter presents Module Maintenance Inventory for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Module Maintenance Inventory API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/module-maintenance-inventory.md), and [API module](../api/module-maintenance-inventory.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `module-maintenance-inventory`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-maintenance-mobile-flutter`](https://github.com/liberusoftware/project-maintenance-mobile-flutter) | [`module-maintenance-inventory-flutter`](https://github.com/liberusoftware/module-maintenance-inventory-flutter) (`module_maintenance_inventory_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-maintenance-dart-mobile`](https://github.com/liberusoftware/project-maintenance-dart-mobile) | [`module-maintenance-inventory-dart-mobile`](https://github.com/liberusoftware/module-maintenance-inventory-dart-mobile) (`module_maintenance_inventory_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-maintenance-dart-desktop`](https://github.com/liberusoftware/project-maintenance-dart-desktop) | [`module-maintenance-inventory-dart-desktop`](https://github.com/liberusoftware/module-maintenance-inventory-dart-desktop) (`module_maintenance_inventory_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api) | [API plan](../api/module-maintenance-inventory.md) · [Core plan](../core/module-maintenance-inventory.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Parts** | Adaptive mobile cards/sheets for `parts` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `parts` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Warehouses/vans** | Adaptive mobile cards/sheets for `warehouses/vans` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `warehouses/vans` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Stock ledger** | Adaptive mobile cards/sheets for `stock ledger` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `stock ledger` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Reservations** | Adaptive mobile cards/sheets for `reservations` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `reservations` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Issues/returns** | Adaptive mobile cards/sheets for `issues/returns` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `issues/returns` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Transfers** | Adaptive mobile cards/sheets for `transfers` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `transfers` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Reorder** | Adaptive mobile cards/sheets for `reorder` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `reorder` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Counts** | Adaptive mobile cards/sheets for `counts` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `counts` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

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
