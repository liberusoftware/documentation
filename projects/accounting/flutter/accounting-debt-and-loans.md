# Accounting Debt And Loans Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-debt-and-loans). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-debt-and-loans-flutter
**Matching core package:** module-accounting-accounting-debt-and-loans ([implementation](../core/accounting-debt-and-loans.md))
**Matching API package:** module-accounting-accounting-debt-and-loans-api ([contract](../api/accounting-debt-and-loans.md))

## Implementation plan

This adapter presents Accounting Debt And Loans for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Debt And Loans API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/accounting-debt-and-loans.md), and [API module](../api/accounting-debt-and-loans.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `accounting-debt-and-loans`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-accounting-erp-mobile-flutter`](https://github.com/liberusoftware/project-accounting-erp-mobile-flutter) | [`module-accounting-debt-and-loans-flutter`](https://github.com/liberusoftware/module-accounting-debt-and-loans-flutter) (`module_accounting_debt_and_loans_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-accounting-erp-dart-mobile`](https://github.com/liberusoftware/project-accounting-erp-dart-mobile) | [`module-accounting-debt-and-loans-dart-mobile`](https://github.com/liberusoftware/module-accounting-debt-and-loans-dart-mobile) (`module_accounting_debt_and_loans_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-accounting-erp-dart-desktop`](https://github.com/liberusoftware/project-accounting-erp-dart-desktop) | [`module-accounting-debt-and-loans-dart-desktop`](https://github.com/liberusoftware/module-accounting-debt-and-loans-dart-desktop) (`module_accounting_debt_and_loans_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | [API plan](../api/accounting-debt-and-loans.md) · [Core plan](../core/accounting-debt-and-loans.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Facilities** | Adaptive mobile cards/sheets for `facilities` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `facilities` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Drawdowns** | Adaptive mobile cards/sheets for `drawdowns` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `drawdowns` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Repayments** | Adaptive mobile cards/sheets for `repayments` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `repayments` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Interest/fees** | Adaptive mobile cards/sheets for `interest/fees` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `interest/fees` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Schedules** | Adaptive mobile cards/sheets for `schedules` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `schedules` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Covenants** | Adaptive mobile cards/sheets for `covenants` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `covenants` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Current/non-current split** | Adaptive mobile cards/sheets for `current/non-current split` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `current/non-current split` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Reconciliation** | Adaptive mobile cards/sheets for `reconciliation` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `reconciliation` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [DebtQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Queries/DebtQuery.php) | `public function facilities(int $teamId): Collection`<br>`public function position(int $teamId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateDebtFacility.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Actions/CreateDebtFacility.php) | `public function handle(array $attributes): DebtFacility` |
| [ReconcileDebtMovement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Actions/ReconcileDebtMovement.php) | `public function handle(DebtMovement $movement, string $journalReference): DebtMovement` |
| [RecordDebtMovement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Actions/RecordDebtMovement.php) | `public function handle(DebtFacility $facility, string\|DebtMovementKind $kind, array $attributes): DebtMovement` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DebtCovenant.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Models/DebtCovenant.php) | `facility_id`, `team_id`, `covenant_ref`, `metric`, `threshold`, `operator`, `last_value`, `status`, `metadata` |
| [DebtFacility.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Models/DebtFacility.php) | `team_id`, `facility_ref`, `lender_ref`, `currency`, `limit_amount`, `drawn_amount`, `interest_rate`, `start_date`, `maturity_date`, `status`, `metadata` |
| [DebtMovement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Models/DebtMovement.php) | `facility_id`, `team_id`, `kind`, `principal_amount`, `interest_amount`, `fee_amount`, `movement_date`, `due_date`, `status`, `journal_ref`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [DebtAndLoansController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans-api/src/Http/Controllers/DebtAndLoansController.php) | `public function index(Request $request): JsonResponse`<br>`public function position(DebtQuery $query): JsonResponse`<br>`public function store(Request $request, CreateDebtFacility $action): JsonResponse`<br>`public function movement(Request $request, string $facility, RecordDebtMovement $action): JsonResponse`<br>`public function reconcile(Request $request, string $movement, ReconcileDebtMovement $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-debt-and-loans-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/debt-and-loans')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.debt-and-loans.read')->group(function (): void {
Route::get('/facilities', [DebtAndLoansController::class, 'index']);
Route::get('/position', [DebtAndLoansController::class, 'position']);
Route::middleware('ability:accounting.debt-and-loans.write')->group(function (): void {
Route::post('/facilities', [DebtAndLoansController::class, 'store']);
Route::post('/facilities/{facility}/movements', [DebtAndLoansController::class, 'movement']);
Route::post('/movements/{movement}/reconcile', [DebtAndLoansController::class, 'reconcile']);
```
<!-- layer-implementation-plan:end -->
