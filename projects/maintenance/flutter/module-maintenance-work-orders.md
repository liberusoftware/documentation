# Module Maintenance Work Orders Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-maintenance-work-orders). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-maintenance-module-maintenance-work-orders-flutter
**Matching core package:** module-maintenance-module-maintenance-work-orders ([implementation](../core/module-maintenance-work-orders.md))
**Matching API package:** module-maintenance-module-maintenance-work-orders-api ([contract](../api/module-maintenance-work-orders.md))

## Implementation plan

This adapter presents Module Maintenance Work Orders for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Module Maintenance Work Orders API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/module-maintenance-work-orders.md), and [API module](../api/module-maintenance-work-orders.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `module-maintenance-work-orders`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-maintenance-mobile-flutter`](https://github.com/liberusoftware/project-maintenance-mobile-flutter) | [`module-maintenance-work-orders-flutter`](https://github.com/liberusoftware/module-maintenance-work-orders-flutter) (`module_maintenance_work_orders_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-maintenance-dart-mobile`](https://github.com/liberusoftware/project-maintenance-dart-mobile) | [`module-maintenance-work-orders-dart-mobile`](https://github.com/liberusoftware/module-maintenance-work-orders-dart-mobile) (`module_maintenance_work_orders_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-maintenance-dart-desktop`](https://github.com/liberusoftware/project-maintenance-dart-desktop) | [`module-maintenance-work-orders-dart-desktop`](https://github.com/liberusoftware/module-maintenance-work-orders-dart-desktop) (`module_maintenance_work_orders_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api) | [API plan](../api/module-maintenance-work-orders.md) · [Core plan](../core/module-maintenance-work-orders.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Requests** | Adaptive mobile cards/sheets for `requests` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `requests` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Triage** | Adaptive mobile cards/sheets for `triage` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `triage` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Jobs** | Adaptive mobile cards/sheets for `jobs` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `jobs` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Tasks** | Adaptive mobile cards/sheets for `tasks` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `tasks` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Status machine** | Adaptive mobile cards/sheets for `status machine` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `status machine` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Dependencies** | Adaptive mobile cards/sheets for `dependencies` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `dependencies` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Notes** | Adaptive mobile cards/sheets for `notes` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `notes` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Evidence** | Adaptive mobile cards/sheets for `evidence` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `evidence` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Completion** | Adaptive mobile cards/sheets for `completion` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `completion` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddWorkOrderComment.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Actions/AddWorkOrderComment.php) | `public function handle(int $teamId, WorkOrder $workOrder, int $userId, string $comment, bool $internal = false): WorkOrderComment` |
| [AddWorkOrderDependency.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Actions/AddWorkOrderDependency.php) | `public function handle(int $teamId, WorkOrder $workOrder, WorkOrder $dependsOn): WorkOrderDependency` |
| [AddWorkOrderEvidence.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Actions/AddWorkOrderEvidence.php) | `public function handle(int $teamId, WorkOrder $workOrder, array $attributes): WorkOrderEvidence` |
| [CreateWorkOrder.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Actions/CreateWorkOrder.php) | `public function handle(int $teamId, array $attributes): WorkOrder` |
| [DeleteWorkOrder.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Actions/DeleteWorkOrder.php) | `public function handle(int $teamId, WorkOrder $workOrder): void` |
| [RemoveWorkOrderDependency.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Actions/RemoveWorkOrderDependency.php) | `public function handle(int $teamId, WorkOrderDependency $dependency): void` |
| [RemoveWorkOrderEvidence.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Actions/RemoveWorkOrderEvidence.php) | `public function handle(int $teamId, WorkOrderEvidence $evidence): void` |
| [TransitionWorkOrder.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Actions/TransitionWorkOrder.php) | `public function handle(int $teamId, WorkOrder $workOrder, string $status, ?int $actorId = null): WorkOrder` |
| [UpdateWorkOrder.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Actions/UpdateWorkOrder.php) | `public function handle(int $teamId, WorkOrder $workOrder, array $attributes): WorkOrder` |
| [WorkOrderPolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Policies/WorkOrderPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, WorkOrder $order): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, WorkOrder $order): bool`<br>`public function delete(object $user, WorkOrder $order): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [WorkOrder.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Models/WorkOrder.php) | `team_id`, `number`, `title`, `description`, `location`, `equipment_id`, `customer_id`, `vendor_id`, `assigned_to`, `due_date`, `started_at`, `estimated_minutes`, `actual_minutes`, `maintenance_plan_id`, `checklist_id`, `priority`, `status`, `requested_by`, `guest_name`, `guest_email`, `guest_phone`, `submitted_at`, `reviewed_by`, `reviewed_at`, `completed_at`, `notes`, `metadata` |
| [WorkOrderComment.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Models/WorkOrderComment.php) | `team_id`, `work_order_id`, `user_id`, `comment`, `is_internal` |
| [WorkOrderDependency.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Models/WorkOrderDependency.php) | `team_id`, `work_order_id`, `depends_on_work_order_id` |
| [WorkOrderEvidence.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders/src/Models/WorkOrderEvidence.php) | `team_id`, `work_order_id`, `added_by`, `kind`, `label`, `reference`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [WorkOrderController.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders-api/src/Http/Controllers/WorkOrderController.php) | `public function index(Request $r): JsonResponse`<br>`public function store(Request $r, CreateWorkOrder $create): JsonResponse`<br>`public function show(Request $r, WorkOrder $workOrder): JsonResponse`<br>`public function update(Request $r, WorkOrder $workOrder, UpdateWorkOrder $update): JsonResponse`<br>`public function destroy(Request $r, WorkOrder $workOrder, DeleteWorkOrder $delete): JsonResponse`<br>`public function transition(Request $r, WorkOrder $workOrder, TransitionWorkOrder $transition): JsonResponse`<br>`public function comments(Request $r, WorkOrder $workOrder): JsonResponse`<br>`public function comment(Request $r, WorkOrder $workOrder, AddWorkOrderComment $add): JsonResponse`<br>`public function dependencies(Request $r, WorkOrder $workOrder): JsonResponse`<br>`public function addDependency(Request $r, WorkOrder $workOrder, AddWorkOrderDependency $add): JsonResponse`<br>`public function removeDependency(Request $r, WorkOrder $workOrder, WorkOrderDependency $dependency, RemoveWorkOrderDependency $remove): JsonResponse`<br>`public function evidence(Request $r, WorkOrder $workOrder): JsonResponse`<br>`public function addEvidence(Request $r, WorkOrder $workOrder, AddWorkOrderEvidence $add): JsonResponse`<br>`public function removeEvidence(Request $r, WorkOrder $workOrder, WorkOrderEvidence $evidence, RemoveWorkOrderEvidence $remove): JsonResponse` |

**Observed route declarations:**

[modules/module-maintenance-work-orders-api/routes/api.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-work-orders-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/maintenance/work-orders')->group(function (): void {
Route::get('/', [WorkOrderController::class, 'index']);
Route::post('/', [WorkOrderController::class, 'store']);
Route::get('/{workOrder}', [WorkOrderController::class, 'show']);
Route::patch('/{workOrder}', [WorkOrderController::class, 'update']);
Route::delete('/{workOrder}', [WorkOrderController::class, 'destroy']);
Route::post('/{workOrder}/transitions', [WorkOrderController::class, 'transition']);
Route::get('/{workOrder}/comments', [WorkOrderController::class, 'comments']);
Route::post('/{workOrder}/comments', [WorkOrderController::class, 'comment']);
Route::get('/{workOrder}/dependencies', [WorkOrderController::class, 'dependencies']);
Route::post('/{workOrder}/dependencies', [WorkOrderController::class, 'addDependency']);
Route::delete('/{workOrder}/dependencies/{dependency}', [WorkOrderController::class, 'removeDependency']);
Route::get('/{workOrder}/evidence', [WorkOrderController::class, 'evidence']);
Route::post('/{workOrder}/evidence', [WorkOrderController::class, 'addEvidence']);
Route::delete('/{workOrder}/evidence/{evidence}', [WorkOrderController::class, 'removeEvidence']);
```
<!-- layer-implementation-plan:end -->
