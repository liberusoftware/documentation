# Accounting Year End Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-year-end). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-year-end-flutter
**Matching core package:** module-accounting-accounting-year-end ([implementation](../core/accounting-year-end.md))
**Matching API package:** module-accounting-accounting-year-end-api ([contract](../api/accounting-year-end.md))

## Implementation plan

This adapter presents Accounting Year End for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Year End API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/accounting-year-end.md), and [API module](../api/accounting-year-end.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `accounting-year-end`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-accounting-erp-mobile-flutter`](https://github.com/liberusoftware/project-accounting-erp-mobile-flutter) | [`module-accounting-year-end-flutter`](https://github.com/liberusoftware/module-accounting-year-end-flutter) (`module_accounting_year_end_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-accounting-erp-dart-mobile`](https://github.com/liberusoftware/project-accounting-erp-dart-mobile) | [`module-accounting-year-end-dart-mobile`](https://github.com/liberusoftware/module-accounting-year-end-dart-mobile) (`module_accounting_year_end_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-accounting-erp-dart-desktop`](https://github.com/liberusoftware/project-accounting-erp-dart-desktop) | [`module-accounting-year-end-dart-desktop`](https://github.com/liberusoftware/module-accounting-year-end-dart-desktop) (`module_accounting_year_end_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | [API plan](../api/accounting-year-end.md) · [Core plan](../core/accounting-year-end.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Final adjustments** | Adaptive mobile cards/sheets for `final adjustments` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `final adjustments` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Retained earnings/roll-forward** | Adaptive mobile cards/sheets for `retained earnings/roll-forward` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `retained earnings/roll-forward` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Opening balances** | Adaptive mobile cards/sheets for `opening balances` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `opening balances` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Statutory/tax handoff** | Adaptive mobile cards/sheets for `statutory/tax handoff` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `statutory/tax handoff` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Lock** | Adaptive mobile cards/sheets for `lock` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `lock` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Archive** | Adaptive mobile cards/sheets for `archive` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `archive` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Evidence** | Adaptive mobile cards/sheets for `evidence` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `evidence` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [YearEndQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Queries/YearEndQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddYearEndAdjustment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Actions/AddYearEndAdjustment.php) | `public function handle(YearEndPeriod $period, array $attributes): YearEndAdjustment` |
| [ArchiveYearEnd.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Actions/ArchiveYearEnd.php) | `public function handle(YearEndPeriod $period): YearEndPeriod` |
| [CloseYearEnd.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Actions/CloseYearEnd.php) | `public function handle(YearEndClose $close, string $closingEntryRef): YearEndClose` |
| [CreateYearEndClose.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Actions/CreateYearEndClose.php) | `public function handle(array $attributes): YearEndClose` |
| [CreateYearEndPeriod.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Actions/CreateYearEndPeriod.php) | `public function handle(array $attributes): YearEndPeriod` |
| [LockYearEnd.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Actions/LockYearEnd.php) | `public function handle(YearEndPeriod $period, int $actor): YearEndPeriod` |
| [ReopenYearEnd.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Actions/ReopenYearEnd.php) | `public function handle(YearEndClose $close): YearEndClose` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [YearEndAdjustment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Models/YearEndAdjustment.php) | `period_id`, `team_id`, `adjustment_ref`, `amount`, `description`, `journal_ref`, `status`, `evidence` |
| [YearEndClose.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Models/YearEndClose.php) | `team_id`, `fiscal_year`, `period_end`, `retained_earnings_account_ref`, `net_income`, `status`, `closed_at`, `locked_at`, `closing_entry_ref`, `metadata` |
| [YearEndPeriod.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end/src/Models/YearEndPeriod.php) | `team_id`, `period_ref`, `period_end`, `status`, `retained_earnings`, `opening_balances`, `statutory_handoff`, `evidence`, `locked_by`, `locked_at`, `archived_at` |

| Observed API controller | Handler signatures |
| --- | --- |
| [YearEndController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end-api/src/Http/Controllers/YearEndController.php) | `public function index(YearEndQuery $query): JsonResponse`<br>`public function store(Request $request, CreateYearEndPeriod $action): JsonResponse`<br>`public function adjustment(Request $request, string $period, AddYearEndAdjustment $action): JsonResponse`<br>`public function lock(Request $request, string $period, LockYearEnd $action): JsonResponse`<br>`public function archive(Request $request, string $period, ArchiveYearEnd $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-year-end-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-year-end-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/year-end')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.year-end.read')->get('/', [YearEndController::class, 'index']);
Route::middleware('ability:accounting.year-end.write')->group(function (): void {
Route::post('/', [YearEndController::class, 'store']);
Route::post('/{period}/adjustments', [YearEndController::class, 'adjustment']);
Route::post('/{period}/lock', [YearEndController::class, 'lock']);
Route::post('/{period}/archive', [YearEndController::class, 'archive']);
```
<!-- layer-implementation-plan:end -->
