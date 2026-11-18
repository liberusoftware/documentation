# Reporting React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#reporting). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-billing-reporting-react-native
**Matching core package:** module-billing-reporting ([implementation](../core/reporting.md))
**Matching API package:** module-billing-reporting-api ([contract](../api/reporting.md))

## Implementation plan

This adapter presents Reporting for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Reporting API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/reporting.md), and [API module](../api/reporting.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `reporting`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-billing-mobile-react`](https://github.com/liberusoftware/project-billing-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/reporting.md)) |
| Capability React Native module skeleton | [`module-billing-reporting-react-native`](https://github.com/liberusoftware/module-billing-reporting-react-native) (`@liberusoftware/module-billing-reporting-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **MRR/ARR** | Progressive mobile list/detail/sheet flow for `mrr/arr` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Churn** | Progressive mobile list/detail/sheet flow for `churn` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Aging** | Progressive mobile list/detail/sheet flow for `aging` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Revenue** | Progressive mobile list/detail/sheet flow for `revenue` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Tax** | Progressive mobile list/detail/sheet flow for `tax` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Usage** | Progressive mobile list/detail/sheet flow for `usage` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Provisioning** | Progressive mobile list/detail/sheet flow for `provisioning` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Collection** | Progressive mobile list/detail/sheet flow for `collection` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Provider metrics** | Progressive mobile list/detail/sheet flow for `provider metrics` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListMetricSnapshots.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Queries/ListMetricSnapshots.php) | `public function execute(int $teamId, int $perPage = 25): LengthAwarePaginator` |
| [ListReportingMetrics.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Queries/ListReportingMetrics.php) | `public function execute(int $teamId, ?string $metric = null, int $perPage = 25): LengthAwarePaginator` |
| [ListReportingRecords.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Queries/ListReportingRecords.php) | `public function handle(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CalculateReportingMetric.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Actions/CalculateReportingMetric.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(int $teamId, string $metric, CarbonImmutable $periodStart, CarbonImmutable $periodEnd, ?string $currency = null): array` |
| [CreateMetricSnapshot.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Actions/CreateMetricSnapshot.php) | `public function handle(int $teamId, array $attributes): MetricSnapshot` |
| [ExportReportingMetrics.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Actions/ExportReportingMetrics.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(int $teamId, ?string $metric = null): string` |
| [GenerateCustomerBillingSummary.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Actions/GenerateCustomerBillingSummary.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(int $teamId, int $customerId, ?string $currency = null): array` |
| [RecordReportingMetric.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Actions/RecordReportingMetric.php) | `public function execute(int $teamId, array $attributes): ReportingMetric` |
| [MetricSnapshotPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Policies/MetricSnapshotPolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function view(?Authenticatable $user, MetricSnapshot $record): bool`<br>`public function update(?Authenticatable $user, MetricSnapshot $record): bool` |
| [ReportingMetricPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Policies/ReportingMetricPolicy.php) | `public function viewAny(?object $user): bool`<br>`public function create(?object $user): bool`<br>`public function view(?object $user, object $record): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MetricSnapshot.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Models/MetricSnapshot.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReportingMetric.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Models/ReportingMetric.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ReportingController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting-api/src/Http/Controllers/ReportingController.php) | `public function metrics(Request $request, ListReportingMetrics $metrics): JsonResponse`<br>`public function exportMetrics(Request $request, ExportReportingMetrics $export): Response`<br>`public function recordMetric(Request $request, RecordReportingMetric $record): JsonResponse`<br>`public function calculateMetric(Request $request, CalculateReportingMetric $calculate, RecordReportingMetric $record): JsonResponse`<br>`public function snapshots(Request $request, ListMetricSnapshots $snapshots): JsonResponse`<br>`public function customerSummary(Request $request, GenerateCustomerBillingSummary $summary, int $customer): JsonResponse`<br>`public function createSnapshot(Request $request, CreateMetricSnapshot $create): JsonResponse`<br>`public function snapshot(Request $request, int $record): JsonResponse` |
| [ReportingMetricController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting-api/src/Http/Controllers/ReportingMetricController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, RecordReportingMetric $record): JsonResponse` |

**Observed route declarations:**

[modules/module-billing-reporting-api/routes/api.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting-api/routes/api.php)

```php
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.reporting.read'])->prefix('api/v1/billing/reporting/metrics')->group(function (): void {
Route::get('/', [ReportingController::class, 'metrics'])->name('billing.reporting.metrics.index');
Route::get('/export', [ReportingController::class, 'exportMetrics'])->name('billing.reporting.metrics.export');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.reporting.write', 'idempotency'])->prefix('api/v1/billing/reporting/metrics')->group(function (): void {
Route::post('/', [ReportingController::class, 'recordMetric'])->name('billing.reporting.metrics.store');
Route::post('/calculate', [ReportingController::class, 'calculateMetric'])->name('billing.reporting.metrics.calculate');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.reporting.read'])->prefix('api/v1/billing/reporting')->group(function (): void {
Route::get('/customers/{customer}/summary', [ReportingController::class, 'customerSummary'])->whereNumber('customer')->name('billing.reporting.customers.summary');
Route::get('/', [ReportingController::class, 'snapshots'])->name('billing.reporting.snapshots.index');
Route::get('/{record}', [ReportingController::class, 'snapshot'])->whereNumber('record')->name('billing.reporting.snapshots.show');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.reporting.write', 'idempotency'])->prefix('api/v1/billing/reporting')->group(function (): void {
Route::post('/snapshots', [ReportingController::class, 'createSnapshot'])->name('billing.reporting.snapshots.store');
```
<!-- layer-implementation-plan:end -->
