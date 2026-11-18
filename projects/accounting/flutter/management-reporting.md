# Management Reporting Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#management-reporting). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-management-reporting-flutter
**Matching core package:** module-accounting-management-reporting ([implementation](../core/management-reporting.md))
**Matching API package:** module-accounting-management-reporting-api ([contract](../api/management-reporting.md))

## Implementation plan

This adapter presents Management Reporting for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Management Reporting API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/management-reporting.md), and [API module](../api/management-reporting.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `management-reporting`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-accounting-erp-mobile-flutter`](https://github.com/liberusoftware/project-accounting-erp-mobile-flutter) | [`module-accounting-management-reporting-flutter`](https://github.com/liberusoftware/module-accounting-management-reporting-flutter) (`module_accounting_management_reporting_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-accounting-erp-dart-mobile`](https://github.com/liberusoftware/project-accounting-erp-dart-mobile) | [`module-accounting-management-reporting-dart-mobile`](https://github.com/liberusoftware/module-accounting-management-reporting-dart-mobile) (`module_accounting_management_reporting_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-accounting-erp-dart-desktop`](https://github.com/liberusoftware/project-accounting-erp-dart-desktop) | [`module-accounting-management-reporting-dart-desktop`](https://github.com/liberusoftware/module-accounting-management-reporting-dart-desktop) (`module_accounting_management_reporting_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | [API plan](../api/management-reporting.md) · [Core plan](../core/management-reporting.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Report packs** | Adaptive mobile cards/sheets for `report packs` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `report packs` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Narratives** | Adaptive mobile cards/sheets for `narratives` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `narratives` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Charts** | Adaptive mobile cards/sheets for `charts` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `charts` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Schedules** | Adaptive mobile cards/sheets for `schedules` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `schedules` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Review** | Adaptive mobile cards/sheets for `review` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `review` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Approval** | Adaptive mobile cards/sheets for `approval` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `approval` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **PDF/spreadsheet delivery** | Adaptive mobile cards/sheets for `pdf/spreadsheet delivery` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `pdf/spreadsheet delivery` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Archive** | Adaptive mobile cards/sheets for `archive` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `archive` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ReportQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Queries/ReportQuery.php) | `public function packs(?int $teamId = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function summary(ReportPack $report): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddReportContent.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Actions/AddReportContent.php) | `public function narrative(ReportPack $report, array $attributes): ReportNarrative`<br>`public function chart(ReportPack $report, array $attributes): ReportChart` |
| [ArchiveReport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Actions/ArchiveReport.php) | `public function handle(ReportPack $report): ReportPack` |
| [CreateReportPack.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Actions/CreateReportPack.php) | `public function handle(array $attributes): ReportPack` |
| [DeliverReport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Actions/DeliverReport.php) | `public function handle(ReportPack $report, string $format, array $attributes = []): ReportDelivery` |
| [ReviewReport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Actions/ReviewReport.php) | `public function handle(ReportPack $report, string $actor, string $decision, ?string $comment = null): ReportPack` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ReportChart.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Models/ReportChart.php) | `report_pack_id`, `chart_ref`, `title`, `chart_type`, `data_source`, `series`, `options`, `metadata` |
| [ReportDelivery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Models/ReportDelivery.php) | `report_pack_id`, `format`, `file_ref`, `status`, `recipients`, `checksum`, `delivered_at`, `failure_message`, `metadata` |
| [ReportNarrative.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Models/ReportNarrative.php) | `report_pack_id`, `section_ref`, `title`, `body`, `author_ref`, `version`, `metadata` |
| [ReportPack.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Models/ReportPack.php) | `team_id`, `report_ref`, `name`, `period_start`, `period_end`, `currency`, `status`, `version`, `owner_ref`, `approved_by`, `approved_at`, `delivered_at`, `archived_at`, `metadata` |
| [ReportReview.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Models/ReportReview.php) | `report_pack_id`, `actor_ref`, `decision`, `comment`, `reviewed_at`, `metadata` |
| [ReportSchedule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting/src/Models/ReportSchedule.php) | `report_pack_id`, `frequency`, `timezone`, `recipients`, `next_run_at`, `active`, `last_run_at`, `failure_message`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ManagementReportingController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting-api/src/Http/Controllers/ManagementReportingController.php) | `public function index(Request $request, ReportQuery $query): mixed`<br>`public function store(Request $request, CreateReportPack $action): ReportPackResource`<br>`public function show(ReportPack $reportPack): ReportPackResource`<br>`public function review(Request $request, ReportPack $reportPack, ReviewReport $action): ReportPackResource`<br>`public function deliver(Request $request, ReportPack $reportPack, DeliverReport $action): JsonResponse`<br>`public function archive(ReportPack $reportPack, ArchiveReport $action): ReportPackResource` |

**Observed route declarations:**

[modules/accounting-management-reporting-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-management-reporting-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/management-reporting')->group(function (): void {
Route::get('/packs', [ManagementReportingController::class, 'index'])->name('accounting.management-reporting.list');
Route::post('/packs', [ManagementReportingController::class, 'store'])->name('accounting.management-reporting.create');
Route::get('/packs/{reportPack}', [ManagementReportingController::class, 'show'])->name('accounting.management-reporting.show');
Route::post('/packs/{reportPack}/review', [ManagementReportingController::class, 'review'])->name('accounting.management-reporting.review');
Route::post('/packs/{reportPack}/deliver', [ManagementReportingController::class, 'deliver'])->name('accounting.management-reporting.deliver');
Route::post('/packs/{reportPack}/archive', [ManagementReportingController::class, 'archive'])->name('accounting.management-reporting.archive');
```
<!-- layer-implementation-plan:end -->
