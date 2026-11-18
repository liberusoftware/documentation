# Reporting Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#reporting). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-maintenance-reporting-flutter
**Matching core package:** module-maintenance-reporting ([implementation](../core/reporting.md))
**Matching API package:** module-maintenance-reporting-api ([contract](../api/reporting.md))

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

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-maintenance-mobile-flutter`](https://github.com/liberusoftware/project-maintenance-mobile-flutter) | [`module-maintenance-reporting-flutter`](https://github.com/liberusoftware/module-maintenance-reporting-flutter) (`module_maintenance_reporting_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-maintenance-dart-mobile`](https://github.com/liberusoftware/project-maintenance-dart-mobile) | [`module-maintenance-reporting-dart-mobile`](https://github.com/liberusoftware/module-maintenance-reporting-dart-mobile) (`module_maintenance_reporting_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-maintenance-dart-desktop`](https://github.com/liberusoftware/project-maintenance-dart-desktop) | [`module-maintenance-reporting-dart-desktop`](https://github.com/liberusoftware/module-maintenance-reporting-dart-desktop) (`module_maintenance_reporting_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api) | [API plan](../api/reporting.md) · [Core plan](../core/reporting.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Backlog** | Adaptive mobile cards/sheets for `backlog` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `backlog` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Response** | Adaptive mobile cards/sheets for `response` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `response` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **First-time fix** | Adaptive mobile cards/sheets for `first-time fix` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `first-time fix` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Downtime** | Adaptive mobile cards/sheets for `downtime` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `downtime` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Cost** | Adaptive mobile cards/sheets for `cost` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `cost` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Utilization** | Adaptive mobile cards/sheets for `utilization` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `utilization` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Stock** | Adaptive mobile cards/sheets for `stock` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `stock` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **SLA** | Adaptive mobile cards/sheets for `sla` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `sla` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Compliance metrics** | Adaptive mobile cards/sheets for `compliance metrics` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `compliance metrics` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-maintenance-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [BuildReportSummary.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting/src/Queries/BuildReportSummary.php) | `public function handle(int $teamId, ?CarbonInterface $start = null, ?CarbonInterface $end = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateReportRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting/src/Actions/CreateReportRecord.php) | `public function handle(int $teamId, array $attributes): ReportRecord` |
| [DeleteReportRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting/src/Actions/DeleteReportRecord.php) | `public function handle(int $teamId, ReportRecord $record): void` |
| [PublishReport.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting/src/Actions/PublishReport.php) | `public function execute(int $teamId, ReportRecord $record): ReportRecord` |
| [UpdateReportRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting/src/Actions/UpdateReportRecord.php) | `public function handle(int $teamId, ReportRecord $record, array $attributes): ReportRecord` |
| [ReportRecordPolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting/src/Policies/ReportRecordPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, ReportRecord $record): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, ReportRecord $record): bool`<br>`public function delete(object $user, ReportRecord $record): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ReportKind.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting/src/Models/ReportKind.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReportRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting/src/Models/ReportRecord.php) | `kind`, `title`, `description`, `metric_value`, `period_start`, `period_end`, `status`, `metadata`, `team_id` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ReportingRecordController.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting-api/src/Http/Controllers/ReportingRecordController.php) | `public function index(Request $request): JsonResponse`<br>`public function summary(Request $request, BuildReportSummary $summary): JsonResponse`<br>`public function store(Request $request, CreateReportRecord $create): JsonResponse`<br>`public function publish(Request $request, ReportRecord $record, PublishReport $publish): JsonResponse`<br>`public function show(Request $request, ReportRecord $record): JsonResponse`<br>`public function update(Request $request, ReportRecord $record, UpdateReportRecord $update): JsonResponse`<br>`public function destroy(Request $request, ReportRecord $record, DeleteReportRecord $delete): JsonResponse` |

**Observed route declarations:**

[modules/module-maintenance-reporting-api/routes/api.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/maintenance/reporting')->group(function (): void {
Route::get('/', [ReportingRecordController::class, 'index']);
Route::get('/summary', [ReportingRecordController::class, 'summary']);
Route::post('/', [ReportingRecordController::class, 'store']);
Route::get('/{record}', [ReportingRecordController::class, 'show']);
Route::patch('/{record}', [ReportingRecordController::class, 'update']);
Route::post('/{record}/publish', [ReportingRecordController::class, 'publish']);
Route::delete('/{record}', [ReportingRecordController::class, 'destroy']);
```
<!-- layer-implementation-plan:end -->
