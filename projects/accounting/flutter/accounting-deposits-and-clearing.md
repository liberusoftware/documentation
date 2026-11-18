# Accounting Deposits And Clearing Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-deposits-and-clearing). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-deposits-and-clearing-flutter
**Matching core package:** module-accounting-accounting-deposits-and-clearing ([implementation](../core/accounting-deposits-and-clearing.md))
**Matching API package:** module-accounting-accounting-deposits-and-clearing-api ([contract](../api/accounting-deposits-and-clearing.md))

## Implementation plan

This adapter presents Accounting Deposits And Clearing for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Deposits And Clearing API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/accounting-deposits-and-clearing.md), and [API module](../api/accounting-deposits-and-clearing.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `accounting-deposits-and-clearing`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-accounting-erp-mobile-flutter`](https://github.com/liberusoftware/project-accounting-erp-mobile-flutter) | [`module-accounting-deposits-and-clearing-flutter`](https://github.com/liberusoftware/module-accounting-deposits-and-clearing-flutter) (`module_accounting_deposits_and_clearing_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-accounting-erp-dart-mobile`](https://github.com/liberusoftware/project-accounting-erp-dart-mobile) | [`module-accounting-deposits-and-clearing-dart-mobile`](https://github.com/liberusoftware/module-accounting-deposits-and-clearing-dart-mobile) (`module_accounting_deposits_and_clearing_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-accounting-erp-dart-desktop`](https://github.com/liberusoftware/project-accounting-erp-dart-desktop) | [`module-accounting-deposits-and-clearing-dart-desktop`](https://github.com/liberusoftware/module-accounting-deposits-and-clearing-dart-desktop) (`module_accounting_deposits_and_clearing_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | [API plan](../api/accounting-deposits-and-clearing.md) · [Core plan](../core/accounting-deposits-and-clearing.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Undeposited funds** | Adaptive mobile cards/sheets for `undeposited funds` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `undeposited funds` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Grouped deposits** | Adaptive mobile cards/sheets for `grouped deposits` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `grouped deposits` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Payment-provider clearing** | Adaptive mobile cards/sheets for `payment-provider clearing` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `payment-provider clearing` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Fees** | Adaptive mobile cards/sheets for `fees` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `fees` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Payouts** | Adaptive mobile cards/sheets for `payouts` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `payouts` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Timing differences** | Adaptive mobile cards/sheets for `timing differences` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `timing differences` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Reconciliation** | Adaptive mobile cards/sheets for `reconciliation` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `reconciliation` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ClearingQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Queries/ClearingQuery.php) | `public function undeposited(int $teamId): Collection`<br>`public function deposits(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateGroupedDeposit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Actions/CreateGroupedDeposit.php) | `public function handle(array $attributes, array $fundIds): ClearingDeposit` |
| [ReconcileDeposit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Actions/ReconcileDeposit.php) | `public function handle(ClearingDeposit $deposit, float $payoutAmount, float $feeAmount = 0): ClearingDeposit` |
| [RecordUndepositedFund.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Actions/RecordUndepositedFund.php) | `public function handle(array $attributes): ClearingFund` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ClearingDeposit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Models/ClearingDeposit.php) | `team_id`, `deposit_ref`, `provider`, `account_ref`, `currency`, `gross_amount`, `fee_amount`, `payout_amount`, `deposit_date`, `status`, `metadata` |
| [ClearingFund.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Models/ClearingFund.php) | `team_id`, `deposit_id`, `source_type`, `source_id`, `amount`, `currency`, `received_on`, `status`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ClearingController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing-api/src/Http/Controllers/ClearingController.php) | `public function funds(ClearingQuery $query): JsonResponse`<br>`public function deposits(ClearingQuery $query): JsonResponse`<br>`public function recordFund(Request $request, RecordUndepositedFund $action): JsonResponse`<br>`public function createDeposit(Request $request, CreateGroupedDeposit $action): JsonResponse`<br>`public function reconcile(Request $request, string $deposit, ReconcileDeposit $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-deposits-and-clearing-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/deposits-and-clearing')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.deposits-and-clearing.read')->group(function (): void {
Route::get('/funds', [ClearingController::class, 'funds']);
Route::get('/deposits', [ClearingController::class, 'deposits']);
Route::middleware('ability:accounting.deposits-and-clearing.write')->group(function (): void {
Route::post('/funds', [ClearingController::class, 'recordFund']);
Route::post('/deposits', [ClearingController::class, 'createDeposit']);
Route::post('/deposits/{deposit}/reconcile', [ClearingController::class, 'reconcile']);
```
<!-- layer-implementation-plan:end -->
