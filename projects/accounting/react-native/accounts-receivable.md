# Accounts Receivable React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounts-receivable). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounts-receivable-react-native
**Matching core package:** module-accounting-accounts-receivable ([implementation](../core/accounts-receivable.md))
**Matching API package:** module-accounting-accounts-receivable-api ([contract](../api/accounts-receivable.md))

## Implementation plan

This adapter presents Accounts Receivable for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounts Receivable API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/accounts-receivable.md), and [API module](../api/accounts-receivable.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `accounts-receivable`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounts-receivable.md)) |
| Capability React Native module skeleton | [`module-accounting-accounts-receivable-react-native`](https://github.com/liberusoftware/module-accounting-accounts-receivable-react-native) (`@liberusoftware/module-accounting-accounts-receivable-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Customer subledger** | Progressive mobile list/detail/sheet flow for `customer subledger` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Open items** | Progressive mobile list/detail/sheet flow for `open items` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Statements** | Progressive mobile list/detail/sheet flow for `statements` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Aging** | Progressive mobile list/detail/sheet flow for `aging` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Balances** | Progressive mobile list/detail/sheet flow for `balances` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Unapplied cash** | Progressive mobile list/detail/sheet flow for `unapplied cash` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Disputes** | Progressive mobile list/detail/sheet flow for `disputes` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Credit limits/holds** | Progressive mobile list/detail/sheet flow for `credit limits/holds` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Control-account reconciliation** | Progressive mobile list/detail/sheet flow for `control-account reconciliation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [AgingQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Queries/AgingQuery.php) | `public function handle(?int $partyId = null, ?\DateTimeInterface $asOf = null): array` |
| [ControlAccountReconciliationQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Queries/ControlAccountReconciliationQuery.php) | `public function handle(?float $controlBalance = null): array` |
| [CustomerSubledgerQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Queries/CustomerSubledgerQuery.php) | `public function handle(int $partyId): array` |
| [StatementQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Queries/StatementQuery.php) | `public function handle(int $partyId, ?\DateTimeInterface $from = null, ?\DateTimeInterface $to = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApplyReceipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Actions/ApplyReceipt.php) | `public function handle(ReceivableReceipt $receipt, ReceivableOpenItem $item, float $amount): ReceivableReceipt` |
| [CreateOpenItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Actions/CreateOpenItem.php) | `public function handle(array $attributes): ReceivableOpenItem` |
| [EnsureAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Actions/EnsureAccount.php) | `public function handle(int $partyId): ReceivableAccount` |
| [OpenDispute.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Actions/OpenDispute.php) | `public function handle(ReceivableOpenItem $item, string $reason, ?float $amount = null): ReceivableDispute` |
| [RecalculateAccountBalance.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Actions/RecalculateAccountBalance.php) | `public function handle(int $partyId): ReceivableAccount` |
| [RecordReceipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Actions/RecordReceipt.php) | `public function handle(array $attributes): ReceivableReceipt` |
| [ResolveDispute.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Actions/ResolveDispute.php) | `public function handle(ReceivableDispute $dispute, string $resolution, bool $accepted = false): ReceivableDispute` |
| [SetCreditControl.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Actions/SetCreditControl.php) | `public function handle(int $partyId, ?float $creditLimit = null, ?bool $hold = null, ?string $reason = null): ReceivableAccount` |
| [SyncFinalizedInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Actions/SyncFinalizedInvoice.php) | `public function handle(SalesInvoice $invoice): ReceivableOpenItem` |
| [AccountsReceivablePolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable-api/src/Policies/AccountsReceivablePolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function view(?Authenticatable $user, object $model): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function update(?Authenticatable $user, object $model): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ReceiptApplication.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Models/ReceiptApplication.php) | `receipt_id`, `open_item_id`, `amount` |
| [ReceivableAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Models/ReceivableAccount.php) | `party_id`, `credit_limit`, `current_balance`, `credit_hold`, `hold_reason`, `control_account_code`, `status`, `metadata` |
| [ReceivableDispute.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Models/ReceivableDispute.php) | `open_item_id`, `amount`, `reason`, `status`, `opened_at`, `resolved_at`, `resolution`, `metadata` |
| [ReceivableOpenItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Models/ReceivableOpenItem.php) | `party_id`, `source_type`, `source_id`, `reference`, `issued_on`, `due_on`, `original_amount`, `applied_amount`, `currency`, `status`, `metadata` |
| [ReceivableReceipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable/src/Models/ReceivableReceipt.php) | `party_id`, `received_on`, `amount`, `applied_amount`, `currency`, `reference`, `status`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [AccountsReceivableController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable-api/src/Http/Controllers/AccountsReceivableController.php) | `public function index(Request $request): JsonResponse`<br>`public function receipts(Request $request): JsonResponse`<br>`public function disputes(Request $request): JsonResponse`<br>`public function show(ReceivableOpenItem $openItem): ReceivableOpenItemResource`<br>`public function store(Request $request): ReceivableOpenItemResource`<br>`public function statement(Request $request, int $party): JsonResponse`<br>`public function aging(Request $request): JsonResponse`<br>`public function balances(Request $request, int $party): JsonResponse`<br>`public function receipt(Request $request): JsonResponse`<br>`public function apply(Request $request, ReceivableReceipt $receipt): JsonResponse`<br>`public function dispute(Request $request): JsonResponse`<br>`public function resolve(Request $request, ReceivableDispute $dispute): JsonResponse`<br>`public function credit(Request $request, int $party): JsonResponse`<br>`public function reconcile(Request $request): JsonResponse` |

**Observed route declarations:**

[modules/accounting-accounts-receivable-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-accounts-receivable-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/accounts-receivable')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [AccountsReceivableController::class, 'index'])->middleware('ability:accounting.receivables.read');
Route::get('/receipts', [AccountsReceivableController::class, 'receipts'])->middleware('ability:accounting.receivables.read');
Route::get('/disputes', [AccountsReceivableController::class, 'disputes'])->middleware('ability:accounting.receivables.read');
Route::get('/aging', [AccountsReceivableController::class, 'aging'])->middleware('ability:accounting.receivables.read');
Route::get('/reconciliation', [AccountsReceivableController::class, 'reconcile'])->middleware('ability:accounting.receivables.read');
Route::get('/statement/{party}', [AccountsReceivableController::class, 'statement'])->middleware('ability:accounting.receivables.read');
Route::get('/balances/{party}', [AccountsReceivableController::class, 'balances'])->middleware('ability:accounting.receivables.read');
Route::post('/', [AccountsReceivableController::class, 'store'])->middleware('ability:accounting.receivables.write');
Route::post('/receipts', [AccountsReceivableController::class, 'receipt'])->middleware('ability:accounting.receivables.write');
Route::post('/receipts/{receipt}/apply', [AccountsReceivableController::class, 'apply'])->middleware('ability:accounting.receivables.write');
Route::post('/disputes', [AccountsReceivableController::class, 'dispute'])->middleware('ability:accounting.receivables.write');
Route::post('/disputes/{dispute}/resolve', [AccountsReceivableController::class, 'resolve'])->middleware('ability:accounting.receivables.write');
Route::post('/customers/{party}/credit-control', [AccountsReceivableController::class, 'credit'])->middleware('ability:accounting.receivables.write');
Route::get('/{openItem}', [AccountsReceivableController::class, 'show'])->middleware('ability:accounting.receivables.read');
```
<!-- layer-implementation-plan:end -->
