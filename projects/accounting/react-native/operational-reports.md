# Operational Reports React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#operational-reports). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-operational-reports-react-native
**Matching core package:** module-accounting-operational-reports ([implementation](../core/operational-reports.md))
**Matching API package:** module-accounting-operational-reports-api ([contract](../api/operational-reports.md))

## Implementation plan

This adapter presents Operational Reports for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Operational Reports API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/operational-reports.md), and [API module](../api/operational-reports.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `operational-reports`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/operational-reports.md)) |
| Capability React Native module skeleton | [`module-accounting-operational-reports-react-native`](https://github.com/liberusoftware/module-accounting-operational-reports-react-native) (`@liberusoftware/module-accounting-operational-reports-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Receivables/payables** | Progressive mobile list/detail/sheet flow for `receivables/payables` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Sales/purchases** | Progressive mobile list/detail/sheet flow for `sales/purchases` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Tax** | Progressive mobile list/detail/sheet flow for `tax` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Bank** | Progressive mobile list/detail/sheet flow for `bank` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Inventory** | Progressive mobile list/detail/sheet flow for `inventory` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Assets** | Progressive mobile list/detail/sheet flow for `assets` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Expenses** | Progressive mobile list/detail/sheet flow for `expenses` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Projects** | Progressive mobile list/detail/sheet flow for `projects` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Payroll** | Progressive mobile list/detail/sheet flow for `payroll` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Exception reports** | Progressive mobile list/detail/sheet flow for `exception reports` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ReportQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-operational-reports/src/Queries/ReportQuery.php) | `public function paginate(?int $teamId = null, ?string $category = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function exceptions(?int $teamId = null): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [GenerateReport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-operational-reports/src/Actions/GenerateReport.php) | `public function handle(array $attributes, array $rows = [], array $exceptions = []): ReportRun` |
| [PublishReport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-operational-reports/src/Actions/PublishReport.php) | `public function handle(ReportRun $run, int $actorId): ReportRun` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ReportAudit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-operational-reports/src/Models/ReportAudit.php) | `run_id`, `event_type`, `actor_id`, `payload`, `payload_hash`, `created_at` |
| [ReportException.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-operational-reports/src/Models/ReportException.php) | `run_id`, `exception_key`, `severity`, `message`, `source_type`, `source_id`, `status`, `resolution`, `resolved_by`, `resolved_at`, `metadata` |
| [ReportRow.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-operational-reports/src/Models/ReportRow.php) | `run_id`, `row_key`, `label`, `source_type`, `source_id`, `amount`, `currency`, `state`, `dimensions`, `payload` |
| [ReportRun.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-operational-reports/src/Models/ReportRun.php) | `team_id`, `report_key`, `name`, `category`, `period_start`, `period_end`, `currency`, `status`, `filters`, `summary`, `source_hash`, `requested_by`, `published_by`, `published_at`, `failure_message`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [OperationalReportsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-operational-reports-api/src/Http/Controllers/OperationalReportsController.php) | `public function index(Request $request, ReportQuery $query): mixed`<br>`public function store(Request $request, GenerateReport $action): JsonResponse`<br>`public function show(ReportRun $reportRun): ReportResource`<br>`public function publish(Request $request, ReportRun $reportRun, PublishReport $action): ReportResource`<br>`public function exceptions(Request $request, ReportQuery $query): mixed` |

**Observed route declarations:**

[modules/accounting-operational-reports-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-operational-reports-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/operational-reports')->group(function (): void {
Route::get('/', [OperationalReportsController::class, 'index'])->name('accounting.operational-reports.list');
Route::post('/', [OperationalReportsController::class, 'store'])->name('accounting.operational-reports.create');
Route::get('/exceptions', [OperationalReportsController::class, 'exceptions'])->name('accounting.operational-reports.exceptions');
Route::get('/{reportRun}', [OperationalReportsController::class, 'show'])->name('accounting.operational-reports.show');
Route::post('/{reportRun}/publish', [OperationalReportsController::class, 'publish'])->name('accounting.operational-reports.publish');
```
<!-- layer-implementation-plan:end -->
