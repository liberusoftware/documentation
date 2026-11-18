# Real Estate Portals Reporting React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#real-estate-portals-reporting). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-real-estate-real-estate-portals-reporting-react-native
**Matching core package:** module-real-estate-real-estate-portals-reporting ([implementation](../core/real-estate-portals-reporting.md))
**Matching API package:** module-real-estate-real-estate-portals-reporting-api ([contract](../api/real-estate-portals-reporting.md))

## Implementation plan

This adapter presents Real Estate Portals Reporting for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Real Estate Portals Reporting API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/real-estate-portals-reporting.md), and [API module](../api/real-estate-portals-reporting.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `real-estate-portals-reporting`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-real-estate-mobile-react`](https://github.com/liberusoftware/project-real-estate-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/real-estate-portals-reporting.md)) |
| Capability React Native module skeleton | [`module-real-estate-portals-reporting-react-native`](https://github.com/liberusoftware/module-real-estate-portals-reporting-react-native) (`@liberusoftware/module-real-estate-portals-reporting-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Party self-service plus pipeline** | Progressive mobile list/detail/sheet flow for `party self-service plus pipeline` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Conversion** | Progressive mobile list/detail/sheet flow for `conversion` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Source** | Progressive mobile list/detail/sheet flow for `source` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Fee** | Progressive mobile list/detail/sheet flow for `fee` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Time-to-complete** | Progressive mobile list/detail/sheet flow for `time-to-complete` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Occupancy** | Progressive mobile list/detail/sheet flow for `occupancy` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Compliance metrics** | Progressive mobile list/detail/sheet flow for `compliance metrics` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-real-estate-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

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
