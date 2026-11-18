# Property Management Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#property-management). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-real-estate-property-management-flutter
**Matching core package:** module-real-estate-property-management ([implementation](../core/property-management.md))
**Matching API package:** module-real-estate-property-management-api ([contract](../api/property-management.md))

## Implementation plan

This adapter presents Property Management for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Property Management API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/property-management.md), and [API module](../api/property-management.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `property-management`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-real-estate-mobile-flutter`](https://github.com/liberusoftware/project-real-estate-mobile-flutter) | [`module-real-estate-property-management-flutter`](https://github.com/liberusoftware/module-real-estate-property-management-flutter) (`module_real_estate_property_management_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-real-estate-dart-mobile`](https://github.com/liberusoftware/project-real-estate-dart-mobile) | [`module-real-estate-property-management-dart-mobile`](https://github.com/liberusoftware/module-real-estate-property-management-dart-mobile) (`module_real_estate_property_management_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-real-estate-dart-desktop`](https://github.com/liberusoftware/project-real-estate-dart-desktop) | [`module-real-estate-property-management-dart-desktop`](https://github.com/liberusoftware/module-real-estate-property-management-dart-desktop) (`module_real_estate_property_management_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api) | [API plan](../api/property-management.md) · [Core plan](../core/property-management.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Rent schedule** | Adaptive mobile cards/sheets for `rent schedule` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `rent schedule` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Statements** | Adaptive mobile cards/sheets for `statements` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `statements` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Inspections** | Adaptive mobile cards/sheets for `inspections` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `inspections` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Compliance** | Adaptive mobile cards/sheets for `compliance` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `compliance` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Maintenance** | Adaptive mobile cards/sheets for `maintenance` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `maintenance` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Contractors** | Adaptive mobile cards/sheets for `contractors` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `contractors` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Owner approvals** | Adaptive mobile cards/sheets for `owner approvals` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `owner approvals` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListManagementRecords.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Queries/ListManagementRecords.php) | `public function handle(int\|string $teamId, ?string $capability = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ManagementRecordPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Policies/ManagementRecordPolicy.php) | `public function view($user, ManagementRecord $record): bool`<br>`public function update($user, ManagementRecord $record): bool`<br>`public function delete($user, ManagementRecord $record): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Inspection.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Models/Inspection.php) | No literal fillable array detected; inspect the model and API schema. |
| [MaintenanceRequest.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Models/MaintenanceRequest.php) | No literal fillable array detected; inspect the model and API schema. |
| [ManagementRecord.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Models/ManagementRecord.php) | No literal fillable array detected; inspect the model and API schema. |
| [VendorQuote.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Models/VendorQuote.php) | No literal fillable array detected; inspect the model and API schema. |
| [WorkOrder.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Models/WorkOrder.php) | No literal fillable array detected; inspect the model and API schema. |
| [WorkOrderUpdate.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management/src/Models/WorkOrderUpdate.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [InspectionController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-api/src/Http/Controllers/InspectionController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateInspection $create): JsonResponse`<br>`public function show(Request $request, Inspection $inspection): JsonResponse`<br>`public function update(Request $request, Inspection $inspection, UpdateInspection $update): JsonResponse` |
| [MaintenanceRequestController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-api/src/Http/Controllers/MaintenanceRequestController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateMaintenanceRequest $create): JsonResponse`<br>`public function show(Request $request, MaintenanceRequest $maintenance): JsonResponse`<br>`public function update(Request $request, MaintenanceRequest $maintenance, UpdateMaintenanceRequest $update): JsonResponse` |
| [ManagementRecordController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-api/src/Http/Controllers/ManagementRecordController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateManagementRecord $create): JsonResponse`<br>`public function show(Request $request, ManagementRecord $record): JsonResponse`<br>`public function update(Request $request, ManagementRecord $record, TransitionManagementRecord $transition): JsonResponse`<br>`public function updateDetails(Request $request, ManagementRecord $record, UpdateManagementDetails $update): JsonResponse`<br>`public function recordFailure(Request $request, ManagementRecord $record, RecordManagementFailure $failure): JsonResponse` |
| [VendorQuoteController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-api/src/Http/Controllers/VendorQuoteController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateVendorQuote $create): JsonResponse`<br>`public function show(Request $request, VendorQuote $contractorQuote): JsonResponse`<br>`public function update(Request $request, VendorQuote $contractorQuote): JsonResponse`<br>`public function decide(Request $request, VendorQuote $contractorQuote, DecideVendorQuote $decide): JsonResponse` |
| [WorkOrderController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-api/src/Http/Controllers/WorkOrderController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateWorkOrder $create): JsonResponse`<br>`public function show(Request $request, WorkOrder $workOrder): JsonResponse`<br>`public function update(Request $request, WorkOrder $workOrder): JsonResponse`<br>`public function updates(Request $request, WorkOrder $workOrder): JsonResponse`<br>`public function storeUpdate(Request $request, WorkOrder $workOrder, RecordWorkOrderUpdate $record): JsonResponse` |

**Observed route declarations:**

[modules/real-estate-property-management-api/routes/api.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-property-management-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->prefix('api/v1/real-estate/property-management')->group(function (): void {
Route::get('/', [ManagementRecordController::class, 'index']);
Route::post('/', [ManagementRecordController::class, 'store']);
Route::get('/{record}', [ManagementRecordController::class, 'show']);
Route::patch('/{record}', [ManagementRecordController::class, 'update']);
Route::patch('/{record}/details', [ManagementRecordController::class, 'updateDetails']);
Route::post('/{record}/failure', [ManagementRecordController::class, 'recordFailure']);
Route::middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->prefix('api/v1/real-estate/work-orders')->group(function (): void {
Route::get('/', [WorkOrderController::class, 'index']);
Route::post('/', [WorkOrderController::class, 'store']);
Route::get('/{workOrder}', [WorkOrderController::class, 'show']);
Route::patch('/{workOrder}', [WorkOrderController::class, 'update']);
Route::get('/{workOrder}/updates', [WorkOrderController::class, 'updates']);
Route::post('/{workOrder}/updates', [WorkOrderController::class, 'storeUpdate']);
Route::middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->prefix('api/v1/real-estate/contractor-quotes')->group(function (): void {
Route::get('/', [VendorQuoteController::class, 'index']);
Route::post('/', [VendorQuoteController::class, 'store']);
Route::get('/{contractorQuote}', [VendorQuoteController::class, 'show']);
Route::patch('/{contractorQuote}', [VendorQuoteController::class, 'update']);
Route::post('/{contractorQuote}/decision', [VendorQuoteController::class, 'decide']);
Route::middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->prefix('api/v1/real-estate/maintenance')->group(function (): void {
Route::get('/', [MaintenanceRequestController::class, 'index']);
Route::post('/', [MaintenanceRequestController::class, 'store']);
Route::get('/{maintenance}', [MaintenanceRequestController::class, 'show']);
Route::patch('/{maintenance}', [MaintenanceRequestController::class, 'update']);
Route::middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->prefix('api/v1/real-estate/inspections')->group(function (): void {
Route::get('/', [InspectionController::class, 'index']);
Route::post('/', [InspectionController::class, 'store']);
Route::get('/{inspection}', [InspectionController::class, 'show']);
Route::patch('/{inspection}', [InspectionController::class, 'update']);
```
<!-- layer-implementation-plan:end -->
