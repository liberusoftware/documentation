# Accounting Time Tracking React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-time-tracking). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-time-tracking-react-native
**Matching core package:** module-accounting-accounting-time-tracking ([implementation](../core/accounting-time-tracking.md))
**Matching API package:** module-accounting-accounting-time-tracking-api ([contract](../api/accounting-time-tracking.md))

## Implementation plan

This adapter presents Accounting Time Tracking for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Time Tracking API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/accounting-time-tracking.md), and [API module](../api/accounting-time-tracking.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `accounting-time-tracking`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-time-tracking.md)) |
| Capability React Native module skeleton | [`module-accounting-time-tracking-react-native`](https://github.com/liberusoftware/module-accounting-time-tracking-react-native) (`@liberusoftware/module-accounting-time-tracking-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Timesheets** | Progressive mobile list/detail/sheet flow for `timesheets` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Timers** | Progressive mobile list/detail/sheet flow for `timers` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Employees/contractors** | Progressive mobile list/detail/sheet flow for `employees/contractors` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Customers/projects/tasks** | Progressive mobile list/detail/sheet flow for `customers/projects/tasks` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Billable/cost rates** | Progressive mobile list/detail/sheet flow for `billable/cost rates` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Approval** | Progressive mobile list/detail/sheet flow for `approval` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Payroll/invoice export** | Progressive mobile list/detail/sheet flow for `payroll/invoice export` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Corrections** | Progressive mobile list/detail/sheet flow for `corrections` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

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
