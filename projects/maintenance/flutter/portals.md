# Portals Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#portals). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-maintenance-portals-flutter
**Matching core package:** module-maintenance-portals ([implementation](../core/portals.md))
**Matching API package:** module-maintenance-portals-api ([contract](../api/portals.md))

## Implementation plan

This adapter presents Portals for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Portals API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/portals.md), and [API module](../api/portals.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `portals`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-maintenance-mobile-flutter`](https://github.com/liberusoftware/project-maintenance-mobile-flutter) | [`module-maintenance-portals-flutter`](https://github.com/liberusoftware/module-maintenance-portals-flutter) (`module_maintenance_portals_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-maintenance-dart-mobile`](https://github.com/liberusoftware/project-maintenance-dart-mobile) | [`module-maintenance-portals-dart-mobile`](https://github.com/liberusoftware/module-maintenance-portals-dart-mobile) (`module_maintenance_portals_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-maintenance-dart-desktop`](https://github.com/liberusoftware/project-maintenance-dart-desktop) | [`module-maintenance-portals-dart-desktop`](https://github.com/liberusoftware/module-maintenance-portals-dart-desktop) (`module_maintenance_portals_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api) | [API plan](../api/portals.md) · [Core plan](../core/portals.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Customer requests** | Adaptive mobile cards/sheets for `customer requests` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `customer requests` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Approvals** | Adaptive mobile cards/sheets for `approvals` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `approvals` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Status** | Adaptive mobile cards/sheets for `status` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `status` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Engineer schedule/work/offline capture** | Adaptive mobile cards/sheets for `engineer schedule/work/offline capture` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `engineer schedule/work/offline capture` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreatePortalRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-portals/src/Actions/CreatePortalRecord.php) | `public function handle(int $teamId, array $attributes): PortalRecord` |
| [DeletePortalRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-portals/src/Actions/DeletePortalRecord.php) | `public function handle(int $teamId, PortalRecord $record): void` |
| [TransitionPortalRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-portals/src/Actions/TransitionPortalRecord.php) | `public function handle(int $teamId, PortalRecord $record, string $status): PortalRecord` |
| [UpdatePortalRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-portals/src/Actions/UpdatePortalRecord.php) | `public function handle(int $teamId, PortalRecord $record, array $attributes): PortalRecord` |
| [PortalRecordPolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-portals/src/Policies/PortalRecordPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, PortalRecord $record): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, PortalRecord $record): bool`<br>`public function delete(object $user, PortalRecord $record): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PortalRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-portals/src/Models/PortalRecord.php) | `kind`, `title`, `description`, `status`, `requested_by`, `metadata`, `team_id` |

| Observed API controller | Handler signatures |
| --- | --- |
| [PortalsRecordController.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-portals-api/src/Http/Controllers/PortalsRecordController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreatePortalRecord $create): JsonResponse`<br>`public function show(Request $request, PortalRecord $record): JsonResponse`<br>`public function update(Request $request, PortalRecord $record, UpdatePortalRecord $update): JsonResponse`<br>`public function destroy(Request $request, PortalRecord $record, DeletePortalRecord $delete): JsonResponse`<br>`public function transition(Request $request, PortalRecord $record, TransitionPortalRecord $transition): JsonResponse` |

**Observed route declarations:**

[modules/module-maintenance-portals-api/routes/api.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-portals-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/maintenance/portals')->group(function (): void {
Route::get('/', [PortalsRecordController::class, 'index']);
Route::post('/', [PortalsRecordController::class, 'store']);
Route::post('/{record}/transition', [PortalsRecordController::class, 'transition']);
Route::get('/{record}', [PortalsRecordController::class, 'show']);
Route::patch('/{record}', [PortalsRecordController::class, 'update']);
Route::delete('/{record}', [PortalsRecordController::class, 'destroy']);
```
<!-- layer-implementation-plan:end -->
