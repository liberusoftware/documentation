# Accounting Accounts Payable React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-accounts-payable). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-accounts-payable-react-native
**Matching core package:** module-accounting-accounting-accounts-payable ([implementation](../core/accounting-accounts-payable.md))
**Matching API package:** module-accounting-accounting-accounts-payable-api ([contract](../api/accounting-accounts-payable.md))

## Implementation plan

This adapter presents Accounting Accounts Payable for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Accounts Payable API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/accounting-accounts-payable.md), and [API module](../api/accounting-accounts-payable.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `accounting-accounts-payable`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-accounts-payable.md)) |
| Capability React Native module skeleton | [`module-accounting-accounts-payable-react-native`](https://github.com/liberusoftware/module-accounting-accounts-payable-react-native) (`@liberusoftware/module-accounting-accounts-payable-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Supplier subledger** | Progressive mobile list/detail/sheet flow for `supplier subledger` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Open items** | Progressive mobile list/detail/sheet flow for `open items` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Aging** | Progressive mobile list/detail/sheet flow for `aging` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Balances** | Progressive mobile list/detail/sheet flow for `balances` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Credits** | Progressive mobile list/detail/sheet flow for `credits` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Disputes** | Progressive mobile list/detail/sheet flow for `disputes` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Holds** | Progressive mobile list/detail/sheet flow for `holds` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Payment terms** | Progressive mobile list/detail/sheet flow for `payment terms` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Control-account reconciliation** | Progressive mobile list/detail/sheet flow for `control-account reconciliation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

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
