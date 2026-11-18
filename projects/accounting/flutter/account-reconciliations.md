# Account Reconciliations Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#account-reconciliations). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-account-reconciliations-flutter
**Matching core package:** module-accounting-account-reconciliations ([implementation](../core/account-reconciliations.md))
**Matching API package:** module-accounting-account-reconciliations-api ([contract](../api/account-reconciliations.md))

## Implementation plan

This adapter presents Account Reconciliations for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Account Reconciliations API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/account-reconciliations.md), and [API module](../api/account-reconciliations.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `account-reconciliations`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-accounting-erp-mobile-flutter`](https://github.com/liberusoftware/project-accounting-erp-mobile-flutter) | [`module-accounting-account-reconciliations-flutter`](https://github.com/liberusoftware/module-accounting-account-reconciliations-flutter) (`module_accounting_account_reconciliations_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-accounting-erp-dart-mobile`](https://github.com/liberusoftware/project-accounting-erp-dart-mobile) | [`module-accounting-account-reconciliations-dart-mobile`](https://github.com/liberusoftware/module-accounting-account-reconciliations-dart-mobile) (`module_accounting_account_reconciliations_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-accounting-erp-dart-desktop`](https://github.com/liberusoftware/project-accounting-erp-dart-desktop) | [`module-accounting-account-reconciliations-dart-desktop`](https://github.com/liberusoftware/module-accounting-account-reconciliations-dart-desktop) (`module_accounting_account_reconciliations_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | [API plan](../api/account-reconciliations.md) · [Core plan](../core/account-reconciliations.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **GL account templates** | Adaptive mobile cards/sheets for `gl account templates` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `gl account templates` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Source balances** | Adaptive mobile cards/sheets for `source balances` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `source balances` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Supporting items** | Adaptive mobile cards/sheets for `supporting items` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `supporting items` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Preparer/reviewer** | Adaptive mobile cards/sheets for `preparer/reviewer` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `preparer/reviewer` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Aging** | Adaptive mobile cards/sheets for `aging` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `aging` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Certification** | Adaptive mobile cards/sheets for `certification` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `certification` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Carry-forward** | Adaptive mobile cards/sheets for `carry-forward` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `carry-forward` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [AccountReconciliationQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/src/Queries/AccountReconciliationQuery.php) | `public function paginate(?int $teamId, ?string $status = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CarryForwardAccountReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/src/Actions/CarryForwardAccountReconciliation.php) | `public function handle(AccountReconciliation $reconciliation, array $carryForward): AccountReconciliation` |
| [CertifyAccountReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/src/Actions/CertifyAccountReconciliation.php) | `public function handle(AccountReconciliation $reconciliation, array $certification): AccountReconciliation` |
| [CreateAccountReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/src/Actions/CreateAccountReconciliation.php) | `public function handle(array $attributes): AccountReconciliation` |
| [PrepareAccountReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/src/Actions/PrepareAccountReconciliation.php) | `public function handle(AccountReconciliation $reconciliation, array $preparer, array $sourceBalance, array $supportingItems = []): AccountReconciliation` |
| [ReviewAccountReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/src/Actions/ReviewAccountReconciliation.php) | `public function handle(AccountReconciliation $reconciliation, array $reviewer): AccountReconciliation` |
| [AccountReconciliationsPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations-api/src/Policies/AccountReconciliationsPolicy.php) | `public function viewAny(?object $user): bool`<br>`public function view(?object $user, object $record): bool`<br>`public function create(?object $user): bool`<br>`public function update(?object $user, object $record): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AccountReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/src/Models/AccountReconciliation.php) | `team_id`, `book_id`, `account_id`, `period_start`, `period_end`, `status`, `template`, `source_balance`, `supporting_items`, `preparer`, `reviewer`, `aging`, `certification`, `carry_forward` |
| [Account.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations-api/src/Models/Account.php) | `account_number`, `account_name`, `account_type`, `normal_balance`, `balance`, `opening_balance`, `description`, `currency_id`, `parent_id`, `industry_type`, `is_active`, `allow_manual_entry`, `user_id`, `team_id`, `qbo_id`, `qbo_sync_token`, `xero_id`, `sage_id` |

| Observed API controller | Handler signatures |
| --- | --- |
| [AccountReconciliationController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations-api/src/Http/Controllers/AccountReconciliationController.php) | `public function index(Request $request, AccountReconciliationQuery $query): mixed`<br>`public function show(AccountReconciliation $reconciliation): AccountReconciliationResource`<br>`public function store(Request $request, CreateAccountReconciliation $action): AccountReconciliationResource`<br>`public function prepare(Request $request, AccountReconciliation $reconciliation, PrepareAccountReconciliation $action): AccountReconciliationResource`<br>`public function review(Request $request, AccountReconciliation $reconciliation, ReviewAccountReconciliation $action): AccountReconciliationResource`<br>`public function certify(Request $request, AccountReconciliation $reconciliation, CertifyAccountReconciliation $action): AccountReconciliationResource`<br>`public function carryForward(Request $request, AccountReconciliation $reconciliation, CarryForwardAccountReconciliation $action): AccountReconciliationResource` |

**Observed route declarations:**

[modules/accounting-account-reconciliations-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/account-reconciliations')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [AccountReconciliationController::class, 'index'])->middleware('ability:accounting.account-reconciliations.read');
Route::post('/', [AccountReconciliationController::class, 'store'])->middleware('ability:accounting.account-reconciliations.write');
Route::post('/{reconciliation}/prepare', [AccountReconciliationController::class, 'prepare'])->middleware('ability:accounting.account-reconciliations.write');
Route::post('/{reconciliation}/review', [AccountReconciliationController::class, 'review'])->middleware('ability:accounting.account-reconciliations.write');
Route::post('/{reconciliation}/certify', [AccountReconciliationController::class, 'certify'])->middleware('ability:accounting.account-reconciliations.write');
Route::post('/{reconciliation}/carry-forward', [AccountReconciliationController::class, 'carryForward'])->middleware('ability:accounting.account-reconciliations.write');
Route::get('/{reconciliation}', [AccountReconciliationController::class, 'show'])->middleware('ability:accounting.account-reconciliations.read');
```
<!-- layer-implementation-plan:end -->
