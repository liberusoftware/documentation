# Labor And Time Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#labor-and-time). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-maintenance-labor-and-time-flutter
**Matching core package:** module-maintenance-labor-and-time ([implementation](../core/labor-and-time.md))
**Matching API package:** module-maintenance-labor-and-time-api ([contract](../api/labor-and-time.md))

## Implementation plan

This adapter presents Labor And Time for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Labor And Time API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/labor-and-time.md), and [API module](../api/labor-and-time.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `labor-and-time`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-maintenance-mobile-flutter`](https://github.com/liberusoftware/project-maintenance-mobile-flutter) | [`module-maintenance-labor-and-time-flutter`](https://github.com/liberusoftware/module-maintenance-labor-and-time-flutter) (`module_maintenance_labor_and_time_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-maintenance-dart-mobile`](https://github.com/liberusoftware/project-maintenance-dart-mobile) | [`module-maintenance-labor-and-time-dart-mobile`](https://github.com/liberusoftware/module-maintenance-labor-and-time-dart-mobile) (`module_maintenance_labor_and_time_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-maintenance-dart-desktop`](https://github.com/liberusoftware/project-maintenance-dart-desktop) | [`module-maintenance-labor-and-time-dart-desktop`](https://github.com/liberusoftware/module-maintenance-labor-and-time-dart-desktop) (`module_maintenance_labor_and_time_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api) | [API plan](../api/labor-and-time.md) · [Core plan](../core/labor-and-time.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Engineer skills** | Adaptive mobile cards/sheets for `engineer skills` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `engineer skills` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Attendance** | Adaptive mobile cards/sheets for `attendance` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `attendance` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Time entries** | Adaptive mobile cards/sheets for `time entries` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `time entries` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Rates** | Adaptive mobile cards/sheets for `rates` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `rates` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Expenses** | Adaptive mobile cards/sheets for `expenses` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `expenses` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Approval** | Adaptive mobile cards/sheets for `approval` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `approval` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApproveTimeEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time/src/Actions/ApproveTimeEntry.php) | `public function handle(int $teamId, TimeEntry $entry, int $approverId): TimeEntry` |
| [CreateTimeEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time/src/Actions/CreateTimeEntry.php) | `public function handle(int $teamId, array $attributes): TimeEntry` |
| [DeleteTimeEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time/src/Actions/DeleteTimeEntry.php) | `public function handle(int $teamId, TimeEntry $entry): void` |
| [RejectTimeEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time/src/Actions/RejectTimeEntry.php) | `public function handle(int $teamId, TimeEntry $entry, int $approverId, ?string $reason = null): TimeEntry` |
| [UpdateTimeEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time/src/Actions/UpdateTimeEntry.php) | `public function handle(int $teamId, TimeEntry $entry, array $attributes): TimeEntry` |
| [TimeEntryPolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time/src/Policies/TimeEntryPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, TimeEntry $entry): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, TimeEntry $entry): bool`<br>`public function delete(object $user, TimeEntry $entry): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [TimeEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time/src/Models/TimeEntry.php) | `team_id`, `user_id`, `work_order_id`, `description`, `started_at`, `ended_at`, `minutes`, `rate`, `status`, `expense_amount`, `currency` |

| Observed API controller | Handler signatures |
| --- | --- |
| [TimeEntryController.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time-api/src/Http/Controllers/TimeEntryController.php) | `public function index(Request $r): JsonResponse`<br>`public function store(Request $r, CreateTimeEntry $create): JsonResponse`<br>`public function show(Request $r, TimeEntry $timeEntry): JsonResponse`<br>`public function approve(Request $r, TimeEntry $timeEntry, ApproveTimeEntry $approve): JsonResponse`<br>`public function reject(Request $r, TimeEntry $timeEntry, RejectTimeEntry $reject): JsonResponse`<br>`public function update(Request $r, TimeEntry $timeEntry, UpdateTimeEntry $update): JsonResponse`<br>`public function destroy(Request $r, TimeEntry $timeEntry, DeleteTimeEntry $delete): JsonResponse` |

**Observed route declarations:**

[modules/module-maintenance-labor-and-time-api/routes/api.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-labor-and-time-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/maintenance/labor-and-time')->group(function (): void {
Route::get('/', [TimeEntryController::class, 'index']);
Route::post('/', [TimeEntryController::class, 'store']);
Route::get('/{timeEntry}', [TimeEntryController::class, 'show']);
Route::patch('/{timeEntry}', [TimeEntryController::class, 'update']);
Route::delete('/{timeEntry}', [TimeEntryController::class, 'destroy']);
Route::post('/{timeEntry}/approve', [TimeEntryController::class, 'approve']);
Route::post('/{timeEntry}/reject', [TimeEntryController::class, 'reject']);
```
<!-- layer-implementation-plan:end -->
