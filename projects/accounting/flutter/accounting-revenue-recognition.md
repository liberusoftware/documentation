# Accounting Revenue Recognition Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-revenue-recognition). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-revenue-recognition-flutter
**Matching core package:** module-accounting-accounting-revenue-recognition ([implementation](../core/accounting-revenue-recognition.md))
**Matching API package:** module-accounting-accounting-revenue-recognition-api ([contract](../api/accounting-revenue-recognition.md))

## Implementation plan

This adapter presents Accounting Revenue Recognition for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Revenue Recognition API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/accounting-revenue-recognition.md), and [API module](../api/accounting-revenue-recognition.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `accounting-revenue-recognition`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-accounting-erp-mobile-flutter`](https://github.com/liberusoftware/project-accounting-erp-mobile-flutter) | [`module-accounting-revenue-recognition-flutter`](https://github.com/liberusoftware/module-accounting-revenue-recognition-flutter) (`module_accounting_revenue_recognition_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-accounting-erp-dart-mobile`](https://github.com/liberusoftware/project-accounting-erp-dart-mobile) | [`module-accounting-revenue-recognition-dart-mobile`](https://github.com/liberusoftware/module-accounting-revenue-recognition-dart-mobile) (`module_accounting_revenue_recognition_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-accounting-erp-dart-desktop`](https://github.com/liberusoftware/project-accounting-erp-dart-desktop) | [`module-accounting-revenue-recognition-dart-desktop`](https://github.com/liberusoftware/module-accounting-revenue-recognition-dart-desktop) (`module_accounting_revenue_recognition_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | [API plan](../api/accounting-revenue-recognition.md) · [Core plan](../core/accounting-revenue-recognition.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Obligations/schedules** | Adaptive mobile cards/sheets for `obligations/schedules` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `obligations/schedules` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Allocation references** | Adaptive mobile cards/sheets for `allocation references` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `allocation references` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Deferred/accrued revenue** | Adaptive mobile cards/sheets for `deferred/accrued revenue` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `deferred/accrued revenue` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Recognition runs** | Adaptive mobile cards/sheets for `recognition runs` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `recognition runs` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Modifications** | Adaptive mobile cards/sheets for `modifications` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `modifications` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Reconciliation (optional)** | Adaptive mobile cards/sheets for `reconciliation (optional)` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `reconciliation (optional)` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateRevenueSchedule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Actions/CreateRevenueSchedule.php) | `public function handle(array $attributes): RevenueSchedule` |
| [ModifyRevenueSchedule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Actions/ModifyRevenueSchedule.php) | `public function handle(RevenueSchedule $schedule, array $attributes): RevenueModification` |
| [RecognizeDueRevenue.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Actions/RecognizeDueRevenue.php) | `public function handle(RevenueSchedule $schedule, string $asOfDate, ?int $teamId = null): RevenueRecognitionRun` |
| [ReconcileRevenueRun.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Actions/ReconcileRevenueRun.php) | `public function handle(RevenueRecognitionRun $run, array $references = []): RevenueRecognitionRun` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [RevenueAllocationReference.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Models/RevenueAllocationReference.php) | `team_id`, `reference_type`, `reference_id`, `allocation`, `status`, `metadata` |
| [RevenueModification.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Models/RevenueModification.php) | `schedule_id`, `effective_date`, `amount_delta`, `reason`, `status`, `metadata` |
| [RevenueObligation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Models/RevenueObligation.php) | `team_id`, `source_type`, `source_id`, `description`, `currency`, `total_amount`, `start_date`, `periods`, `status`, `metadata` |
| [RevenueRecognitionRun.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Models/RevenueRecognitionRun.php) | `team_id`, `as_of_date`, `status`, `processed_entries`, `failed_entries`, `errors`, `metadata`, `started_at`, `finished_at` |
| [RevenueReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Models/RevenueReconciliation.php) | `run_id`, `reference_type`, `reference_id`, `expected_amount`, `recognized_amount`, `variance`, `status`, `notes`, `metadata` |
| [RevenueSchedule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Models/RevenueSchedule.php) | `obligation_id`, `allocation_reference_id`, `total_amount`, `start_date`, `periods`, `deferred_account_ref`, `revenue_account_ref`, `status`, `funded`, `metadata` |
| [RevenueScheduleEntry.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition/src/Models/RevenueScheduleEntry.php) | `schedule_id`, `period_number`, `recognition_date`, `amount`, `status`, `recognized_at`, `ledger_reference`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [RevenueRecognitionController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition-api/src/Http/Controllers/RevenueRecognitionController.php) | `public function index(Request $request): mixed`<br>`public function store(Request $request, CreateRevenueSchedule $action): mixed`<br>`public function show(Request $request, RevenueSchedule $schedule): RevenueScheduleResource`<br>`public function recognize(Request $request, RevenueSchedule $schedule, RecognizeDueRevenue $action): mixed`<br>`public function modify(Request $request, RevenueSchedule $schedule, ModifyRevenueSchedule $action): mixed`<br>`public function reconcile(Request $request, RevenueRecognitionRun $run, ReconcileRevenueRun $action): mixed` |

**Observed route declarations:**

[modules/accounting-revenue-recognition-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-revenue-recognition-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/revenue-recognition')->group(function (): void {
Route::middleware('ability:accounting.revenue-recognition.read')->group(function (): void {
Route::get('/', [RevenueRecognitionController::class, 'index']);
Route::get('/{schedule}', [RevenueRecognitionController::class, 'show']);
Route::middleware('ability:accounting.revenue-recognition.write')->group(function (): void {
Route::post('/', [RevenueRecognitionController::class, 'store']);
Route::post('/{schedule}/recognize', [RevenueRecognitionController::class, 'recognize']);
Route::post('/{schedule}/modify', [RevenueRecognitionController::class, 'modify']);
Route::post('/runs/{run}/reconcile', [RevenueRecognitionController::class, 'reconcile']);
```
<!-- layer-implementation-plan:end -->
