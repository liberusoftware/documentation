# Control Panel Monitoring Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#control-panel-monitoring). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-control-panel-control-panel-monitoring-flutter
**Matching core package:** module-control-panel-control-panel-monitoring ([implementation](../core/control-panel-monitoring.md))
**Matching API package:** module-control-panel-control-panel-monitoring-api ([contract](../api/control-panel-monitoring.md))

## Implementation plan

This adapter presents Control Panel Monitoring for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Control Panel Monitoring API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/control-panel-monitoring.md), and [API module](../api/control-panel-monitoring.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `control-panel-monitoring`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-control-panel-mobile-flutter`](https://github.com/liberusoftware/project-control-panel-mobile-flutter) | [`module-control-panel-monitoring-flutter`](https://github.com/liberusoftware/module-control-panel-monitoring-flutter) (`module_control_panel_monitoring_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-control-panel-dart-mobile`](https://github.com/liberusoftware/project-control-panel-dart-mobile) | [`module-control-panel-monitoring-dart-mobile`](https://github.com/liberusoftware/module-control-panel-monitoring-dart-mobile) (`module_control_panel_monitoring_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-control-panel-dart-desktop`](https://github.com/liberusoftware/project-control-panel-dart-desktop) | [`module-control-panel-monitoring-dart-desktop`](https://github.com/liberusoftware/module-control-panel-monitoring-dart-desktop) (`module_control_panel_monitoring_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api) | [API plan](../api/control-panel-monitoring.md) · [Core plan](../core/control-panel-monitoring.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Metrics** | Adaptive mobile cards/sheets for `metrics` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `metrics` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Logs** | Adaptive mobile cards/sheets for `logs` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `logs` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Uptime** | Adaptive mobile cards/sheets for `uptime` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `uptime` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Capacity** | Adaptive mobile cards/sheets for `capacity` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `capacity` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Alerts** | Adaptive mobile cards/sheets for `alerts` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `alerts` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Incidents** | Adaptive mobile cards/sheets for `incidents` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `incidents` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Maintenance windows** | Adaptive mobile cards/sheets for `maintenance windows` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `maintenance windows` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Status** | Adaptive mobile cards/sheets for `status` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `status` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListMonitors.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring/src/Queries/ListMonitors.php) | `public function execute(?string $teamId, int $perPage = 25, string $search = ''): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CancelMaintenanceWindow.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring/src/Actions/CancelMaintenanceWindow.php) | `public function execute(MaintenanceWindow $window): MaintenanceWindow` |
| [DeleteMaintenanceWindow.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring/src/Actions/DeleteMaintenanceWindow.php) | `public function execute(MaintenanceWindow $window): void` |
| [RecordMonitoringEvent.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring/src/Actions/RecordMonitoringEvent.php) | `public function execute(array $a): MonitoringEvent` |
| [RecordMonitoringResource.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring/src/Actions/RecordMonitoringResource.php) | `public function execute(array $a): Model` |
| [RegisterMonitor.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring/src/Actions/RegisterMonitor.php) | `public function execute(array $attributes): Monitor` |
| [ResolveMonitoringEvent.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring/src/Actions/ResolveMonitoringEvent.php) | `public function execute(MonitoringEvent $event): MonitoringEvent` |
| [UpdateMaintenanceWindow.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring/src/Actions/UpdateMaintenanceWindow.php) | `public function execute(MaintenanceWindow $window, array $attributes): MaintenanceWindow` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AlertRule.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring/src/Models/AlertRule.php) | `id`, `team_id`, `name`, `condition`, `threshold`, `channels`, `active` |
| [CapacitySnapshot.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring/src/Models/CapacitySnapshot.php) | `id`, `team_id`, `resource`, `used`, `available`, `unit`, `captured_at`, `details` |
| [Incident.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring/src/Models/Incident.php) | `id`, `team_id`, `title`, `severity`, `status`, `summary`, `started_at`, `resolved_at`, `metadata` |
| [LogEntry.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring/src/Models/LogEntry.php) | `id`, `team_id`, `source`, `level`, `message`, `context`, `logged_at` |
| [MaintenanceWindow.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring/src/Models/MaintenanceWindow.php) | `id`, `team_id`, `name`, `starts_at`, `ends_at`, `scope`, `status`, `details` |
| [MetricSample.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring/src/Models/MetricSample.php) | `id`, `team_id`, `monitor_id`, `name`, `value`, `unit`, `dimensions`, `sampled_at` |
| [Monitor.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring/src/Models/Monitor.php) | `team_id`, `subject_type`, `subject_id`, `name`, `status`, `last_checked_at`, `metrics` |
| [MonitoringEvent.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring/src/Models/MonitoringEvent.php) | `id`, `team_id`, `monitor_id`, `kind`, `status`, `payload`, `starts_at`, `ends_at` |

| Observed API controller | Handler signatures |
| --- | --- |
| [MonitorController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring-api/src/Http/Controllers/MonitorController.php) | `public function index(Request $request, ListMonitors $list): JsonResponse`<br>`public function show(Request $request, string $id): JsonResponse`<br>`public function store(Request $request, RegisterMonitor $register): JsonResponse`<br>`public function event(Request $request, RecordMonitoringEvent $record): JsonResponse`<br>`public function record(Request $request, RecordMonitoringResource $record): JsonResponse`<br>`public function resolveEvent(Request $request, string $id, ResolveMonitoringEvent $resolve): JsonResponse`<br>`public function cancelMaintenance(Request $request, MaintenanceWindow $window, CancelMaintenanceWindow $cancel): JsonResponse`<br>`public function deleteMaintenance(Request $request, string $id, DeleteMaintenanceWindow $delete): JsonResponse`<br>`public function updateMaintenance(Request $request, string $id, UpdateMaintenanceWindow $update): JsonResponse` |

**Observed route declarations:**

[modules/control-panel-monitoring-api/routes/api.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-monitoring-api/routes/api.php)

```php
Route::prefix('api/v1/control-panel/monitoring')->middleware(['api', 'auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [MonitorController::class, 'index'])->name('control-panel.monitoring.index');
Route::post('/', [MonitorController::class, 'store'])->name('control-panel.monitoring.store');
Route::post('/events', [MonitorController::class, 'event'])->name('control-panel.monitoring.events.store');
Route::post('/events/{event}/resolve', [MonitorController::class, 'resolveEvent'])->name('control-panel.monitoring.events.resolve');
Route::post('/resources', [MonitorController::class, 'record'])->name('control-panel.monitoring.resources.store');
Route::post('/maintenance/{window}/cancel', [MonitorController::class, 'cancelMaintenance'])->name('control-panel.monitoring.maintenance.cancel');
Route::delete('/maintenance/{window}', [MonitorController::class, 'deleteMaintenance'])->name('control-panel.monitoring.maintenance.delete');
Route::patch('/maintenance/{window}', [MonitorController::class, 'updateMaintenance'])->name('control-panel.monitoring.maintenance.update');
Route::get('{monitor}', [MonitorController::class, 'show'])->name('control-panel.monitoring.show');
```
<!-- layer-implementation-plan:end -->
