# Accounts Payable Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounts-payable). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounts-payable-flutter
**Matching core package:** module-accounting-accounts-payable ([implementation](../core/accounts-payable.md))
**Matching API package:** module-accounting-accounts-payable-api ([contract](../api/accounts-payable.md))

## Implementation plan

This adapter presents Accounts Payable for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounts Payable API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/accounts-payable.md), and [API module](../api/accounts-payable.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `accounts-payable`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-accounting-erp-mobile-flutter`](https://github.com/liberusoftware/project-accounting-erp-mobile-flutter) | [`module-accounting-accounts-payable-flutter`](https://github.com/liberusoftware/module-accounting-accounts-payable-flutter) (`module_accounting_accounts_payable_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-accounting-erp-dart-mobile`](https://github.com/liberusoftware/project-accounting-erp-dart-mobile) | [`module-accounting-accounts-payable-dart-mobile`](https://github.com/liberusoftware/module-accounting-accounts-payable-dart-mobile) (`module_accounting_accounts_payable_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-accounting-erp-dart-desktop`](https://github.com/liberusoftware/project-accounting-erp-dart-desktop) | [`module-accounting-accounts-payable-dart-desktop`](https://github.com/liberusoftware/module-accounting-accounts-payable-dart-desktop) (`module_accounting_accounts_payable_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | [API plan](../api/accounts-payable.md) · [Core plan](../core/accounts-payable.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Supplier subledger** | Adaptive mobile cards/sheets for `supplier subledger` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `supplier subledger` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Open items** | Adaptive mobile cards/sheets for `open items` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `open items` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Aging** | Adaptive mobile cards/sheets for `aging` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `aging` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Balances** | Adaptive mobile cards/sheets for `balances` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `balances` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Credits** | Adaptive mobile cards/sheets for `credits` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `credits` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Disputes** | Adaptive mobile cards/sheets for `disputes` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `disputes` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Holds** | Adaptive mobile cards/sheets for `holds` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `holds` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Payment terms** | Adaptive mobile cards/sheets for `payment terms` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `payment terms` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Control-account reconciliation** | Adaptive mobile cards/sheets for `control-account reconciliation` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `control-account reconciliation` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [AgingQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Queries/AgingQuery.php) | `public function handle(?int $partyId = null, ?\DateTimeInterface $asOf = null): array` |
| [ControlAccountReconciliationQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Queries/ControlAccountReconciliationQuery.php) | `public function handle(): array` |
| [SupplierSubledgerQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Queries/SupplierSubledgerQuery.php) | `public function handle(int $partyId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApplyPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Actions/ApplyPayment.php) | `public function handle(PayablePayment $payment, PayableOpenItem $item, float $amount): PayablePayment` |
| [CreateOpenItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Actions/CreateOpenItem.php) | `public function handle(array $attributes): PayableOpenItem` |
| [EnsureAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Actions/EnsureAccount.php) | `public function handle(int $partyId): PayableAccount` |
| [OpenDispute.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Actions/OpenDispute.php) | `public function handle(PayableOpenItem $item, string $reason, ?float $amount = null): PayableDispute` |
| [RecalculateAccountBalance.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Actions/RecalculateAccountBalance.php) | `public function handle(int $partyId): PayableAccount` |
| [RecordPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Actions/RecordPayment.php) | `public function handle(array $attributes): PayablePayment` |
| [ResolveDispute.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Actions/ResolveDispute.php) | `public function handle(PayableDispute $dispute, string $resolution, bool $accepted = false): PayableDispute` |
| [SetPaymentControl.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Actions/SetPaymentControl.php) | `public function handle(int $partyId, ?bool $paymentHold = null, ?string $holdReason = null): PayableAccount` |
| [AccountingAccountsPayablePolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable-api/src/Policies/AccountingAccountsPayablePolicy.php) | `public function viewAny(?object $user = null): bool`<br>`public function view(?object $user, object $item): bool`<br>`public function create(?object $user = null): bool`<br>`public function update(?object $user, object $item): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PayableAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Models/PayableAccount.php) | `party_id`, `current_balance`, `payment_hold`, `hold_reason`, `control_account_code`, `status`, `metadata` |
| [PayableDispute.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Models/PayableDispute.php) | `open_item_id`, `amount`, `reason`, `status`, `opened_at`, `resolved_at`, `resolution`, `metadata` |
| [PayableOpenItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Models/PayableOpenItem.php) | `party_id`, `source_type`, `source_id`, `reference`, `issued_on`, `due_on`, `original_amount`, `paid_amount`, `currency`, `payment_terms`, `status`, `metadata` |
| [PayablePayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Models/PayablePayment.php) | `party_id`, `paid_on`, `amount`, `applied_amount`, `currency`, `reference`, `status`, `metadata` |
| [PaymentApplication.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable/src/Models/PaymentApplication.php) | `payment_id`, `open_item_id`, `amount` |

| Observed API controller | Handler signatures |
| --- | --- |
| [PayableOpenItemController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable-api/src/Http/Controllers/PayableOpenItemController.php) | `public function index(Request $request): mixed`<br>`public function store(Request $request, CreateOpenItem $action): PayableOpenItemResource`<br>`public function show(string $payableOpenItem): PayableOpenItemResource`<br>`public function aging(Request $request, AgingQuery $query): JsonResponse`<br>`public function balances(string $party, SupplierSubledgerQuery $query): JsonResponse`<br>`public function payment(Request $request, RecordPayment $action): JsonResponse`<br>`public function apply(Request $request, string $payment, ApplyPayment $action): JsonResponse`<br>`public function dispute(Request $request, OpenDispute $action): JsonResponse`<br>`public function resolve(Request $request, string $dispute, ResolveDispute $action): JsonResponse`<br>`public function paymentControl(Request $request, string $party, SetPaymentControl $action): JsonResponse`<br>`public function reconcile(ControlAccountReconciliationQuery $query): JsonResponse` |

**Observed route declarations:**

[modules/accounting-accounts-payable-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-payable-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/accounts-payable')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.payables.read')->group(function (): void {
Route::get('/', [PayableOpenItemController::class, 'index']);
Route::get('/aging', [PayableOpenItemController::class, 'aging']);
Route::get('/balances/{party}', [PayableOpenItemController::class, 'balances']);
Route::get('/reconciliation', [PayableOpenItemController::class, 'reconcile']);
Route::get('/open-items/{payableOpenItem}', [PayableOpenItemController::class, 'show']);
Route::middleware('ability:accounting.payables.write')->group(function (): void {
Route::post('/open-items', [PayableOpenItemController::class, 'store']);
Route::post('/payments', [PayableOpenItemController::class, 'payment']);
Route::post('/payments/{payment}/apply', [PayableOpenItemController::class, 'apply']);
Route::post('/disputes', [PayableOpenItemController::class, 'dispute']);
Route::post('/disputes/{dispute}/resolve', [PayableOpenItemController::class, 'resolve']);
Route::post('/suppliers/{party}/payment-control', [PayableOpenItemController::class, 'paymentControl']);
```
<!-- layer-implementation-plan:end -->
