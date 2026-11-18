# Accounting Kpi And Goals Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-kpi-and-goals). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-kpi-and-goals-flutter
**Matching core package:** module-accounting-accounting-kpi-and-goals ([implementation](../core/accounting-kpi-and-goals.md))
**Matching API package:** module-accounting-accounting-kpi-and-goals-api ([contract](../api/accounting-kpi-and-goals.md))

## Implementation plan

This adapter presents Accounting Kpi And Goals for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Kpi And Goals API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/accounting-kpi-and-goals.md), and [API module](../api/accounting-kpi-and-goals.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `accounting-kpi-and-goals`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-accounting-erp-mobile-flutter`](https://github.com/liberusoftware/project-accounting-erp-mobile-flutter) | [`module-accounting-kpi-and-goals-flutter`](https://github.com/liberusoftware/module-accounting-kpi-and-goals-flutter) (`module_accounting_kpi_and_goals_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-accounting-erp-dart-mobile`](https://github.com/liberusoftware/project-accounting-erp-dart-mobile) | [`module-accounting-kpi-and-goals-dart-mobile`](https://github.com/liberusoftware/module-accounting-kpi-and-goals-dart-mobile) (`module_accounting_kpi_and_goals_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-accounting-erp-dart-desktop`](https://github.com/liberusoftware/project-accounting-erp-dart-desktop) | [`module-accounting-kpi-and-goals-dart-desktop`](https://github.com/liberusoftware/module-accounting-kpi-and-goals-dart-desktop) (`module_accounting_kpi_and_goals_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | [API plan](../api/accounting-kpi-and-goals.md) · [Core plan](../core/accounting-kpi-and-goals.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Governed metrics** | Adaptive mobile cards/sheets for `governed metrics` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `governed metrics` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Targets** | Adaptive mobile cards/sheets for `targets` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `targets` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Owners** | Adaptive mobile cards/sheets for `owners` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `owners` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Thresholds** | Adaptive mobile cards/sheets for `thresholds` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `thresholds` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Periods** | Adaptive mobile cards/sheets for `periods` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `periods` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Alerts** | Adaptive mobile cards/sheets for `alerts` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `alerts` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Commentary** | Adaptive mobile cards/sheets for `commentary` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `commentary` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **History** | Adaptive mobile cards/sheets for `history` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `history` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [KpiQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Queries/KpiQuery.php) | `public function goals(?int $teamId = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function progress(KpiGoal $goal): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddCommentary.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Actions/AddCommentary.php) | `public function handle(KpiGoal $goal, string $actor, string $body, ?string $period = null): KpiCommentary` |
| [CreateGoal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Actions/CreateGoal.php) | `public function handle(KpiMetric $metric, array $attributes): KpiGoal` |
| [CreateMetric.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Actions/CreateMetric.php) | `public function handle(array $attributes): KpiMetric` |
| [RecordMeasurement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Actions/RecordMeasurement.php) | `public function handle(KpiGoal $goal, array $attributes): KpiMeasurement` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [KpiAlert.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Models/KpiAlert.php) | `team_id`, `goal_id`, `measurement_id`, `severity`, `status`, `message`, `triggered_at`, `acknowledged_by`, `resolved_at`, `metadata` |
| [KpiCommentary.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Models/KpiCommentary.php) | `goal_id`, `actor_ref`, `body`, `period_ref`, `metadata` |
| [KpiGoal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Models/KpiGoal.php) | `team_id`, `metric_id`, `goal_ref`, `name`, `owner_ref`, `period_start`, `period_end`, `baseline`, `target`, `warning_threshold`, `critical_threshold`, `status`, `metadata` |
| [KpiMeasurement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Models/KpiMeasurement.php) | `team_id`, `metric_id`, `goal_id`, `period_ref`, `measured_on`, `value`, `progress`, `source_ref`, `metadata` |
| [KpiMetric.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals/src/Models/KpiMetric.php) | `team_id`, `metric_ref`, `name`, `description`, `unit`, `direction`, `source_contract`, `formula`, `owner_ref`, `active`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [KpiController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals-api/src/Http/Controllers/KpiController.php) | `public function index(Request $request, KpiQuery $query): mixed`<br>`public function metric(Request $request, CreateMetric $action): JsonResponse`<br>`public function goal(Request $request, KpiMetric $metric, CreateGoal $action): KpiGoalResource`<br>`public function show(KpiGoal $goal, KpiQuery $query): array`<br>`public function measurement(Request $request, KpiGoal $goal, RecordMeasurement $action): JsonResponse`<br>`public function commentary(Request $request, KpiGoal $goal, AddCommentary $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-kpi-and-goals-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-kpi-and-goals-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/kpi-and-goals')->group(function (): void {
Route::get('/goals', [KpiController::class, 'index'])->name('accounting.kpi-and-goals.list');
Route::post('/metrics', [KpiController::class, 'metric'])->name('accounting.kpi-and-goals.metric');
Route::post('/metrics/{metric}/goals', [KpiController::class, 'goal'])->name('accounting.kpi-and-goals.goal');
Route::get('/goals/{goal}', [KpiController::class, 'show'])->name('accounting.kpi-and-goals.show');
Route::post('/goals/{goal}/measurements', [KpiController::class, 'measurement'])->name('accounting.kpi-and-goals.measurement');
Route::post('/goals/{goal}/commentary', [KpiController::class, 'commentary'])->name('accounting.kpi-and-goals.commentary');
```
<!-- layer-implementation-plan:end -->
