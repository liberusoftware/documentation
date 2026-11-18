# Preventative Maintenance Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#preventative-maintenance). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-maintenance-preventative-maintenance-flutter
**Matching core package:** module-maintenance-preventative-maintenance ([implementation](../core/preventative-maintenance.md))
**Matching API package:** module-maintenance-preventative-maintenance-api ([contract](../api/preventative-maintenance.md))

## Implementation plan

This adapter presents Preventative Maintenance for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Preventative Maintenance API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/preventative-maintenance.md), and [API module](../api/preventative-maintenance.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `preventative-maintenance`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-maintenance-mobile-flutter`](https://github.com/liberusoftware/project-maintenance-mobile-flutter) | [`module-maintenance-preventative-maintenance-flutter`](https://github.com/liberusoftware/module-maintenance-preventative-maintenance-flutter) (`module_maintenance_preventative_maintenance_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-maintenance-dart-mobile`](https://github.com/liberusoftware/project-maintenance-dart-mobile) | [`module-maintenance-preventative-maintenance-dart-mobile`](https://github.com/liberusoftware/module-maintenance-preventative-maintenance-dart-mobile) (`module_maintenance_preventative_maintenance_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-maintenance-dart-desktop`](https://github.com/liberusoftware/project-maintenance-dart-desktop) | [`module-maintenance-preventative-maintenance-dart-desktop`](https://github.com/liberusoftware/module-maintenance-preventative-maintenance-dart-desktop) (`module_maintenance_preventative_maintenance_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api) | [API plan](../api/preventative-maintenance.md) · [Core plan](../core/preventative-maintenance.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Plans** | Adaptive mobile cards/sheets for `plans` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `plans` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Triggers** | Adaptive mobile cards/sheets for `triggers` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `triggers` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Frequencies** | Adaptive mobile cards/sheets for `frequencies` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `frequencies` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Meter rules** | Adaptive mobile cards/sheets for `meter rules` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `meter rules` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Forecasts** | Adaptive mobile cards/sheets for `forecasts` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `forecasts` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Generation** | Adaptive mobile cards/sheets for `generation` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `generation` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Optimization** | Adaptive mobile cards/sheets for `optimization` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `optimization` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CompleteMaintenancePlan.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-preventative-maintenance/src/Actions/CompleteMaintenancePlan.php) | `public function handle(int $teamId, MaintenancePlan $plan, ?CarbonInterface $completedAt = null): MaintenancePlan` |
| [CreateMaintenancePlan.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-preventative-maintenance/src/Actions/CreateMaintenancePlan.php) | `public function handle(int $teamId, array $attributes): MaintenancePlan` |
| [DeleteMaintenancePlan.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-preventative-maintenance/src/Actions/DeleteMaintenancePlan.php) | `public function handle(int $teamId, MaintenancePlan $plan): void` |
| [UpdateMaintenancePlan.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-preventative-maintenance/src/Actions/UpdateMaintenancePlan.php) | `public function handle(int $teamId, MaintenancePlan $plan, array $attributes): MaintenancePlan` |
| [MaintenancePlanPolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-preventative-maintenance/src/Policies/MaintenancePlanPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, MaintenancePlan $plan): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, MaintenancePlan $plan): bool`<br>`public function delete(object $user, MaintenancePlan $plan): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MaintenancePlan.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-preventative-maintenance/src/Models/MaintenancePlan.php) | `team_id`, `name`, `code`, `description`, `equipment_id`, `assigned_to`, `checklist_id`, `instructions`, `estimated_duration`, `frequency_unit`, `frequency_value`, `next_due_at`, `last_completed_at`, `is_active`, `rules` |

| Observed API controller | Handler signatures |
| --- | --- |
| [MaintenancePlanController.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-preventative-maintenance-api/src/Http/Controllers/MaintenancePlanController.php) | `public function index(Request $r): JsonResponse`<br>`public function complete(Request $r, MaintenancePlan $maintenancePlan, CompleteMaintenancePlan $complete): JsonResponse`<br>`public function store(Request $r, CreateMaintenancePlan $create): JsonResponse`<br>`public function show(Request $r, MaintenancePlan $maintenancePlan): JsonResponse`<br>`public function update(Request $r, MaintenancePlan $maintenancePlan, UpdateMaintenancePlan $update): JsonResponse`<br>`public function destroy(Request $r, MaintenancePlan $maintenancePlan, DeleteMaintenancePlan $delete): JsonResponse` |

**Observed route declarations:**

[modules/module-maintenance-preventative-maintenance-api/routes/api.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-preventative-maintenance-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/maintenance/preventative-maintenance')->group(function (): void {
Route::get('/', [MaintenancePlanController::class, 'index']);
Route::post('/', [MaintenancePlanController::class, 'store']);
Route::get('/{maintenancePlan}', [MaintenancePlanController::class, 'show']);
Route::patch('/{maintenancePlan}', [MaintenancePlanController::class, 'update']);
Route::post('/{maintenancePlan}/complete', [MaintenancePlanController::class, 'complete']);
Route::delete('/{maintenancePlan}', [MaintenancePlanController::class, 'destroy']);
```
<!-- layer-implementation-plan:end -->
