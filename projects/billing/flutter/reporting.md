# Reporting Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#reporting). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-billing-reporting-flutter
**Matching core package:** module-billing-reporting ([implementation](../core/reporting.md))
**Matching API package:** module-billing-reporting-api ([contract](../api/reporting.md))

## Implementation plan

This adapter presents Reporting for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Reporting API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/reporting.md), and [API module](../api/reporting.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `reporting`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-billing-mobile-flutter`](https://github.com/liberusoftware/project-billing-mobile-flutter) | [`module-billing-reporting-flutter`](https://github.com/liberusoftware/module-billing-reporting-flutter) (`module_billing_reporting_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-billing-dart-mobile`](https://github.com/liberusoftware/project-billing-dart-mobile) | [`module-billing-reporting-dart-mobile`](https://github.com/liberusoftware/module-billing-reporting-dart-mobile) (`module_billing_reporting_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-billing-dart-desktop`](https://github.com/liberusoftware/project-billing-dart-desktop) | [`module-billing-reporting-dart-desktop`](https://github.com/liberusoftware/module-billing-reporting-dart-desktop) (`module_billing_reporting_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api) | [API plan](../api/reporting.md) · [Core plan](../core/reporting.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **MRR/ARR** | Adaptive mobile cards/sheets for `mrr/arr` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `mrr/arr` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-billing-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Churn** | Adaptive mobile cards/sheets for `churn` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `churn` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-billing-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Aging** | Adaptive mobile cards/sheets for `aging` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `aging` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-billing-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Revenue** | Adaptive mobile cards/sheets for `revenue` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `revenue` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-billing-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Tax** | Adaptive mobile cards/sheets for `tax` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `tax` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-billing-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Usage** | Adaptive mobile cards/sheets for `usage` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `usage` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-billing-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Provisioning** | Adaptive mobile cards/sheets for `provisioning` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `provisioning` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-billing-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Collection** | Adaptive mobile cards/sheets for `collection` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `collection` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-billing-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Provider metrics** | Adaptive mobile cards/sheets for `provider metrics` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `provider metrics` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-billing-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

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
