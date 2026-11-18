# Scheduling Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#scheduling). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-maintenance-scheduling-flutter
**Matching core package:** module-maintenance-scheduling ([implementation](../core/scheduling.md))
**Matching API package:** module-maintenance-scheduling-api ([contract](../api/scheduling.md))

## Implementation plan

This adapter presents Scheduling for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Scheduling API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/scheduling.md), and [API module](../api/scheduling.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `scheduling`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-maintenance-mobile-flutter`](https://github.com/liberusoftware/project-maintenance-mobile-flutter) | [`module-maintenance-scheduling-flutter`](https://github.com/liberusoftware/module-maintenance-scheduling-flutter) (`module_maintenance_scheduling_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-maintenance-dart-mobile`](https://github.com/liberusoftware/project-maintenance-dart-mobile) | [`module-maintenance-scheduling-dart-mobile`](https://github.com/liberusoftware/module-maintenance-scheduling-dart-mobile) (`module_maintenance_scheduling_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-maintenance-dart-desktop`](https://github.com/liberusoftware/project-maintenance-dart-desktop) | [`module-maintenance-scheduling-dart-desktop`](https://github.com/liberusoftware/module-maintenance-scheduling-dart-desktop) (`module_maintenance_scheduling_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api) | [API plan](../api/scheduling.md) · [Core plan](../core/scheduling.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Calendars** | Adaptive mobile cards/sheets for `calendars` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `calendars` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Skills** | Adaptive mobile cards/sheets for `skills` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `skills` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Territories** | Adaptive mobile cards/sheets for `territories` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `territories` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Shifts** | Adaptive mobile cards/sheets for `shifts` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `shifts` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Availability** | Adaptive mobile cards/sheets for `availability` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `availability` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Travel** | Adaptive mobile cards/sheets for `travel` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `travel` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Dispatch** | Adaptive mobile cards/sheets for `dispatch` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `dispatch` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Conflict handling** | Adaptive mobile cards/sheets for `conflict handling` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `conflict handling` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateScheduleEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-scheduling/src/Actions/CreateScheduleEntry.php) | `public function handle(int $teamId, array $attributes): ScheduleEntry` |
| [DeleteScheduleEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-scheduling/src/Actions/DeleteScheduleEntry.php) | `public function handle(int $teamId, ScheduleEntry $entry): void` |
| [TransitionScheduleEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-scheduling/src/Actions/TransitionScheduleEntry.php) | `public function handle(int $teamId, ScheduleEntry $entry, string $status): ScheduleEntry` |
| [UpdateScheduleEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-scheduling/src/Actions/UpdateScheduleEntry.php) | `public function handle(int $teamId, ScheduleEntry $entry, array $attributes): ScheduleEntry` |
| [ScheduleEntryPolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-scheduling/src/Policies/ScheduleEntryPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, ScheduleEntry $entry): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, ScheduleEntry $entry): bool`<br>`public function delete(object $user, ScheduleEntry $entry): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ScheduleEntry.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-scheduling/src/Models/ScheduleEntry.php) | `team_id`, `title`, `description`, `resource_key`, `equipment_id`, `assigned_to`, `checklist_id`, `instructions`, `estimated_duration`, `starts_at`, `ends_at`, `status`, `territory`, `metadata`, `recurrence_type`, `recurrence_value`, `next_due_at`, `last_completed_at`, `priority` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ScheduleEntryController.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-scheduling-api/src/Http/Controllers/ScheduleEntryController.php) | `public function index(Request $r): JsonResponse`<br>`public function store(Request $r, CreateScheduleEntry $create): JsonResponse`<br>`public function transition(Request $r, ScheduleEntry $scheduleEntry, TransitionScheduleEntry $transition): JsonResponse`<br>`public function show(Request $r, ScheduleEntry $scheduleEntry): JsonResponse`<br>`public function update(Request $r, ScheduleEntry $scheduleEntry, UpdateScheduleEntry $update): JsonResponse`<br>`public function destroy(Request $r, ScheduleEntry $scheduleEntry, DeleteScheduleEntry $delete): JsonResponse` |

**Observed route declarations:**

[modules/module-maintenance-scheduling-api/routes/api.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-scheduling-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/maintenance/scheduling')->group(function (): void {
Route::get('/', [ScheduleEntryController::class, 'index']);
Route::post('/', [ScheduleEntryController::class, 'store']);
Route::get('/{scheduleEntry}', [ScheduleEntryController::class, 'show']);
Route::patch('/{scheduleEntry}', [ScheduleEntryController::class, 'update']);
Route::post('/{scheduleEntry}/transitions', [ScheduleEntryController::class, 'transition']);
Route::delete('/{scheduleEntry}', [ScheduleEntryController::class, 'destroy']);
```
<!-- layer-implementation-plan:end -->
