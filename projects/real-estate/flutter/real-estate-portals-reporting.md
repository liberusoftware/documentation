# Real Estate Portals Reporting Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#real-estate-portals-reporting). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-real-estate-real-estate-portals-reporting-flutter
**Matching core package:** module-real-estate-real-estate-portals-reporting ([implementation](../core/real-estate-portals-reporting.md))
**Matching API package:** module-real-estate-real-estate-portals-reporting-api ([contract](../api/real-estate-portals-reporting.md))

## Implementation plan

This adapter presents Real Estate Portals Reporting for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Real Estate Portals Reporting API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/real-estate-portals-reporting.md), and [API module](../api/real-estate-portals-reporting.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `real-estate-portals-reporting`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-real-estate-mobile-flutter`](https://github.com/liberusoftware/project-real-estate-mobile-flutter) | [`module-real-estate-portals-reporting-flutter`](https://github.com/liberusoftware/module-real-estate-portals-reporting-flutter) (`module_real_estate_portals_reporting_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-real-estate-dart-mobile`](https://github.com/liberusoftware/project-real-estate-dart-mobile) | [`module-real-estate-portals-reporting-dart-mobile`](https://github.com/liberusoftware/module-real-estate-portals-reporting-dart-mobile) (`module_real_estate_portals_reporting_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-real-estate-dart-desktop`](https://github.com/liberusoftware/project-real-estate-dart-desktop) | [`module-real-estate-portals-reporting-dart-desktop`](https://github.com/liberusoftware/module-real-estate-portals-reporting-dart-desktop) (`module_real_estate_portals_reporting_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api) | [API plan](../api/real-estate-portals-reporting.md) · [Core plan](../core/real-estate-portals-reporting.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Party self-service plus pipeline** | Adaptive mobile cards/sheets for `party self-service plus pipeline` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `party self-service plus pipeline` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Conversion** | Adaptive mobile cards/sheets for `conversion` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `conversion` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Source** | Adaptive mobile cards/sheets for `source` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `source` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Fee** | Adaptive mobile cards/sheets for `fee` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `fee` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Time-to-complete** | Adaptive mobile cards/sheets for `time-to-complete` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `time-to-complete` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Occupancy** | Adaptive mobile cards/sheets for `occupancy` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `occupancy` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Compliance metrics** | Adaptive mobile cards/sheets for `compliance metrics` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `compliance metrics` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-real-estate-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [PortalReportPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-portals-reporting/src/Policies/PortalReportPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, PortalReport $portalReport): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, PortalReport $portalReport): bool`<br>`public function delete(AuthUser $authUser, PortalReport $portalReport): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, PortalReport $portalReport): bool`<br>`public function forceDelete(AuthUser $authUser, PortalReport $portalReport): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, PortalReport $portalReport): bool`<br>`public function reorder(AuthUser $authUser): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DashboardLayout.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-portals-reporting/src/Models/DashboardLayout.php) | No literal fillable array detected; inspect the model and API schema. |
| [PortalReport.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-portals-reporting/src/Models/PortalReport.php) | No literal fillable array detected; inspect the model and API schema. |
| [SavedReport.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-portals-reporting/src/Models/SavedReport.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [DashboardLayoutController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-portals-reporting-api/src/Http/Controllers/DashboardLayoutController.php) | `public function store(Request $r): JsonResponse` |
| [PortalReportController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-portals-reporting-api/src/Http/Controllers/PortalReportController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreatePortalReport $create): JsonResponse`<br>`public function show(Request $request, PortalReport $portalReport): JsonResponse`<br>`public function update(Request $request, PortalReport $portalReport, UpdatePortalReport $update): JsonResponse`<br>`public function transition(Request $request, PortalReport $portalReport, string $status, TransitionPortalReport $transition): JsonResponse`<br>`public function metric(Request $request, PortalReport $portalReport, string $metric, RecordPortalMetric $record): JsonResponse`<br>`public function destroy(Request $request, PortalReport $portalReport, DeletePortalReport $delete): Response` |
| [SavedReportController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-portals-reporting-api/src/Http/Controllers/SavedReportController.php) | `public function store(Request $r): JsonResponse`<br>`public function show(Request $r, SavedReport $savedReport): JsonResponse`<br>`public function run(Request $r, SavedReport $savedReport): JsonResponse`<br>`public function export(Request $r, SavedReport $savedReport): StreamedResponse` |

**Observed route declarations:**

[modules/real-estate-portals-reporting-api/routes/api.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-portals-reporting-api/routes/api.php)

```php
Route::prefix('api/v1/real-estate/saved-reports')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::post('/', [SavedReportController::class, 'store']);
Route::get('/{savedReport}', [SavedReportController::class, 'show']);
Route::get('/{savedReport}/run', [SavedReportController::class, 'run']);
Route::get('/{savedReport}/export', [SavedReportController::class, 'export']);
Route::post('api/v1/real-estate/dashboard-layouts', [DashboardLayoutController::class, 'store'])->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency']);
Route::prefix('api/v1/real-estate/portals-and-reporting')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [PortalReportController::class, 'index']);
Route::post('/', [PortalReportController::class, 'store']);
Route::get('/{portalReport}', [PortalReportController::class, 'show']);
Route::post('/{portalReport}/transition/{status}', [PortalReportController::class, 'transition']);
Route::patch('/{portalReport}/metrics/{metric}', [PortalReportController::class, 'metric'])->whereIn('metric', ['conversion', 'source', 'fee', 'time_to_complete', 'occupancy', 'compliance']);
Route::delete('/{portalReport}', [PortalReportController::class, 'destroy']);
```
<!-- layer-implementation-plan:end -->
