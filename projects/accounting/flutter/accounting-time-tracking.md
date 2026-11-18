# Accounting Time Tracking Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-time-tracking). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-time-tracking-flutter
**Matching core package:** module-accounting-accounting-time-tracking ([implementation](../core/accounting-time-tracking.md))
**Matching API package:** module-accounting-accounting-time-tracking-api ([contract](../api/accounting-time-tracking.md))

## Implementation plan

This adapter presents Accounting Time Tracking for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Time Tracking API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/accounting-time-tracking.md), and [API module](../api/accounting-time-tracking.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `accounting-time-tracking`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-accounting-erp-mobile-flutter`](https://github.com/liberusoftware/project-accounting-erp-mobile-flutter) | [`module-accounting-time-tracking-flutter`](https://github.com/liberusoftware/module-accounting-time-tracking-flutter) (`module_accounting_time_tracking_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-accounting-erp-dart-mobile`](https://github.com/liberusoftware/project-accounting-erp-dart-mobile) | [`module-accounting-time-tracking-dart-mobile`](https://github.com/liberusoftware/module-accounting-time-tracking-dart-mobile) (`module_accounting_time_tracking_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-accounting-erp-dart-desktop`](https://github.com/liberusoftware/project-accounting-erp-dart-desktop) | [`module-accounting-time-tracking-dart-desktop`](https://github.com/liberusoftware/module-accounting-time-tracking-dart-desktop) (`module_accounting_time_tracking_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | [API plan](../api/accounting-time-tracking.md) · [Core plan](../core/accounting-time-tracking.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Timesheets** | Adaptive mobile cards/sheets for `timesheets` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `timesheets` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Timers** | Adaptive mobile cards/sheets for `timers` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `timers` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Employees/contractors** | Adaptive mobile cards/sheets for `employees/contractors` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `employees/contractors` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Customers/projects/tasks** | Adaptive mobile cards/sheets for `customers/projects/tasks` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `customers/projects/tasks` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Billable/cost rates** | Adaptive mobile cards/sheets for `billable/cost rates` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `billable/cost rates` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Approval** | Adaptive mobile cards/sheets for `approval` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `approval` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Payroll/invoice export** | Adaptive mobile cards/sheets for `payroll/invoice export` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `payroll/invoice export` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Corrections** | Adaptive mobile cards/sheets for `corrections` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `corrections` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApproveTimeEntry.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-time-tracking/src/Actions/ApproveTimeEntry.php) | `public function handle(TimeEntry $entry): TimeEntry` |
| [CreateTimeEntry.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-time-tracking/src/Actions/CreateTimeEntry.php) | `public function handle(array $attributes): TimeEntry` |
| [StartTimer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-time-tracking/src/Actions/StartTimer.php) | `public function handle(array $attributes): TimeTimer` |
| [StopTimer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-time-tracking/src/Actions/StopTimer.php) | `public function handle(TimeTimer $timer): TimeTimer` |
| [SubmitTimeEntry.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-time-tracking/src/Actions/SubmitTimeEntry.php) | `public function handle(TimeEntry $entry): TimeEntry` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [TimeEntry.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-time-tracking/src/Models/TimeEntry.php) | `team_id`, `worker_ref`, `customer_ref`, `project_ref`, `task_ref`, `worked_on`, `hours`, `billable_rate`, `cost_rate`, `currency`, `billable`, `status`, `description`, `metadata` |
| [TimeExport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-time-tracking/src/Models/TimeExport.php) | `team_id`, `destination`, `period_start`, `period_end`, `entry_count`, `status`, `exported_at`, `metadata` |
| [TimeTimer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-time-tracking/src/Models/TimeTimer.php) | `team_id`, `worker_ref`, `project_ref`, `started_at`, `stopped_at`, `status` |

| Observed API controller | Handler signatures |
| --- | --- |
| [TimeTrackingController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-time-tracking-api/src/Http/Controllers/TimeTrackingController.php) | `public function entries(Request $request): mixed`<br>`public function createEntry(Request $request, CreateTimeEntry $action): mixed`<br>`public function submit(Request $request, string $entry, SubmitTimeEntry $action): mixed`<br>`public function approve(Request $request, string $entry, ApproveTimeEntry $action): mixed`<br>`public function startTimer(Request $request, StartTimer $action): mixed`<br>`public function stopTimer(Request $request, string $timer, StopTimer $action): mixed` |

**Observed route declarations:**

[modules/accounting-time-tracking-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-time-tracking-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/time-tracking')->middleware(['auth:sanctum'])->group(function (): void {
Route::get('/entries', [TimeTrackingController::class, 'entries'])->middleware('ability:accounting.time-tracking.read');
Route::post('/entries', [TimeTrackingController::class, 'createEntry'])->middleware('ability:accounting.time-tracking.write');
Route::post('/entries/{entry}/submit', [TimeTrackingController::class, 'submit'])->middleware('ability:accounting.time-tracking.write');
Route::post('/entries/{entry}/approve', [TimeTrackingController::class, 'approve'])->middleware('ability:accounting.time-tracking.approve');
Route::post('/timers/start', [TimeTrackingController::class, 'startTimer'])->middleware('ability:accounting.time-tracking.write');
Route::post('/timers/{timer}/stop', [TimeTrackingController::class, 'stopTimer'])->middleware('ability:accounting.time-tracking.write');
```
<!-- layer-implementation-plan:end -->
