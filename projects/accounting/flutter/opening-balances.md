# Opening Balances Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#opening-balances). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-opening-balances-flutter
**Matching core package:** module-accounting-opening-balances ([implementation](../core/opening-balances.md))
**Matching API package:** module-accounting-opening-balances-api ([contract](../api/opening-balances.md))

## Implementation plan

This adapter presents Opening Balances for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Opening Balances API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/opening-balances.md), and [API module](../api/opening-balances.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `opening-balances`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-accounting-erp-mobile-flutter`](https://github.com/liberusoftware/project-accounting-erp-mobile-flutter) | [`module-accounting-opening-balances-flutter`](https://github.com/liberusoftware/module-accounting-opening-balances-flutter) (`module_accounting_opening_balances_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-accounting-erp-dart-mobile`](https://github.com/liberusoftware/project-accounting-erp-dart-mobile) | [`module-accounting-opening-balances-dart-mobile`](https://github.com/liberusoftware/module-accounting-opening-balances-dart-mobile) (`module_accounting_opening_balances_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-accounting-erp-dart-desktop`](https://github.com/liberusoftware/project-accounting-erp-dart-desktop) | [`module-accounting-opening-balances-dart-desktop`](https://github.com/liberusoftware/module-accounting-opening-balances-dart-desktop) (`module_accounting_opening_balances_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | [API plan](../api/opening-balances.md) · [Core plan](../core/opening-balances.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Migration date** | Adaptive mobile cards/sheets for `migration date` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `migration date` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Account/customer/supplier/bank/item balances** | Adaptive mobile cards/sheets for `account/customer/supplier/bank/item balances` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `account/customer/supplier/bank/item balances` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Outstanding documents** | Adaptive mobile cards/sheets for `outstanding documents` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `outstanding documents` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Validation** | Adaptive mobile cards/sheets for `validation` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `validation` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Approval** | Adaptive mobile cards/sheets for `approval` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `approval` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Reconciliation** | Adaptive mobile cards/sheets for `reconciliation` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `reconciliation` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [OpeningBalanceQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-opening-balances/src/Queries/OpeningBalanceQuery.php) | `public function paginate(?int $teamId = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApproveOpeningBalances.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-opening-balances/src/Actions/ApproveOpeningBalances.php) | `public function handle(OpeningBalanceBatch $batch, int $actorId): OpeningBalanceBatch` |
| [CreateOpeningBalanceBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-opening-balances/src/Actions/CreateOpeningBalanceBatch.php) | `public function handle(array $attributes, array $entries): OpeningBalanceBatch` |
| [ReconcileOpeningBalances.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-opening-balances/src/Actions/ReconcileOpeningBalances.php) | `public function handle(OpeningBalanceBatch $batch, array $actuals): OpeningBalanceBatch` |
| [ValidateOpeningBalances.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-opening-balances/src/Actions/ValidateOpeningBalances.php) | `public function handle(OpeningBalanceBatch $batch): OpeningBalanceBatch` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [OpeningBalanceAudit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-opening-balances/src/Models/OpeningBalanceAudit.php) | `batch_id`, `event_type`, `actor_id`, `payload`, `payload_hash`, `created_at` |
| [OpeningBalanceBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-opening-balances/src/Models/OpeningBalanceBatch.php) | `team_id`, `batch_ref`, `migration_date`, `currency`, `status`, `source_hash`, `idempotency_key`, `summary`, `failure_message`, `requested_by`, `approved_by`, `approved_at`, `metadata` |
| [OpeningBalanceEntry.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-opening-balances/src/Models/OpeningBalanceEntry.php) | `batch_id`, `balance_type`, `reference_type`, `reference_id`, `document_ref`, `document_date`, `due_date`, `currency`, `debit_amount`, `credit_amount`, `status`, `description`, `metadata` |
| [OpeningBalanceReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-opening-balances/src/Models/OpeningBalanceReconciliation.php) | `batch_id`, `entry_id`, `expected_amount`, `actual_amount`, `variance`, `status`, `external_ref`, `notes`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [OpeningBalancesController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-opening-balances-api/src/Http/Controllers/OpeningBalancesController.php) | `public function index(Request $request, OpeningBalanceQuery $query): mixed`<br>`public function store(Request $request, CreateOpeningBalanceBatch $action): JsonResponse`<br>`public function show(OpeningBalanceBatch $openingBalance): OpeningBalanceResource`<br>`public function validateBatch(OpeningBalanceBatch $openingBalance, ValidateOpeningBalances $action): OpeningBalanceResource`<br>`public function approve(Request $request, OpeningBalanceBatch $openingBalance, ApproveOpeningBalances $action): OpeningBalanceResource`<br>`public function reconcile(Request $request, OpeningBalanceBatch $openingBalance, ReconcileOpeningBalances $action): OpeningBalanceResource` |

**Observed route declarations:**

[modules/accounting-opening-balances-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-opening-balances-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/opening-balances')->group(function (): void {
Route::get('/', [OpeningBalancesController::class, 'index'])->name('accounting.opening-balances.list');
Route::post('/', [OpeningBalancesController::class, 'store'])->name('accounting.opening-balances.create');
Route::get('/{openingBalance}', [OpeningBalancesController::class, 'show'])->name('accounting.opening-balances.show');
Route::post('/{openingBalance}/validate', [OpeningBalancesController::class, 'validateBatch'])->name('accounting.opening-balances.validate');
Route::post('/{openingBalance}/approve', [OpeningBalancesController::class, 'approve'])->name('accounting.opening-balances.approve');
Route::post('/{openingBalance}/reconcile', [OpeningBalancesController::class, 'reconcile'])->name('accounting.opening-balances.reconcile');
```
<!-- layer-implementation-plan:end -->
