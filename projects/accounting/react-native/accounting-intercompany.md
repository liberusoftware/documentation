# Accounting Intercompany React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-intercompany). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-intercompany-react-native
**Matching core package:** module-accounting-accounting-intercompany ([implementation](../core/accounting-intercompany.md))
**Matching API package:** module-accounting-accounting-intercompany-api ([contract](../api/accounting-intercompany.md))

## Implementation plan

This adapter presents Accounting Intercompany for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Intercompany API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/accounting-intercompany.md), and [API module](../api/accounting-intercompany.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `accounting-intercompany`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-intercompany.md)) |
| Capability React Native module skeleton | [`module-accounting-intercompany-react-native`](https://github.com/liberusoftware/module-accounting-intercompany-react-native) (`@liberusoftware/module-accounting-intercompany-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Counterparties** | Progressive mobile list/detail/sheet flow for `counterparties` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Trading rules** | Progressive mobile list/detail/sheet flow for `trading rules` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Paired transactions** | Progressive mobile list/detail/sheet flow for `paired transactions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Confirmations** | Progressive mobile list/detail/sheet flow for `confirmations` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Settlement** | Progressive mobile list/detail/sheet flow for `settlement` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Differences** | Progressive mobile list/detail/sheet flow for `differences` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Transfer-pricing evidence** | Progressive mobile list/detail/sheet flow for `transfer-pricing evidence` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Reconciliation** | Progressive mobile list/detail/sheet flow for `reconciliation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [IntercompanyQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Queries/IntercompanyQuery.php) | `public function paginate(?int $teamId = null, ?TransactionStatus $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function reconciliationSummary(IntercompanyTransaction $transaction): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddTransferPricingEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Actions/AddTransferPricingEvidence.php) | `public function handle(IntercompanyTransaction $transaction, array $a): TransferPricingEvidence` |
| [ConfigureTradingRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Actions/ConfigureTradingRule.php) | `public function handle(IntercompanyCounterparty $counterparty, array $a): TradingRule` |
| [ConfirmTransaction.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Actions/ConfirmTransaction.php) | `public function handle(IntercompanyTransaction $transaction, string $entity, bool $confirmed, ?string $comment = null): IntercompanyTransaction` |
| [CreateCounterparty.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Actions/CreateCounterparty.php) | `public function handle(array $a): IntercompanyCounterparty` |
| [CreateTransaction.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Actions/CreateTransaction.php) | `public function handle(IntercompanyCounterparty $counterparty, array $a): IntercompanyTransaction` |
| [ReconcileIntercompany.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Actions/ReconcileIntercompany.php) | `public function handle(array $a): IntercompanyReconciliation` |
| [RecordDifference.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Actions/RecordDifference.php) | `public function handle(IntercompanyTransaction $transaction, array $a): IntercompanyDifference` |
| [SettleTransaction.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Actions/SettleTransaction.php) | `public function handle(IntercompanyTransaction $transaction, array $a): IntercompanyTransaction` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [IntercompanyConfirmation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Models/IntercompanyConfirmation.php) | `transaction_id`, `entity_ref`, `status`, `confirmed_amount`, `comment`, `actor_ref`, `confirmed_at`, `metadata` |
| [IntercompanyCounterparty.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Models/IntercompanyCounterparty.php) | `team_id`, `entity_ref`, `counterparty_ref`, `name`, `default_currency`, `active`, `metadata` |
| [IntercompanyDifference.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Models/IntercompanyDifference.php) | `transaction_id`, `difference_ref`, `amount`, `reason`, `status`, `actor_ref`, `resolved_at`, `metadata` |
| [IntercompanyReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Models/IntercompanyReconciliation.php) | `team_id`, `reconciliation_ref`, `period_ref`, `entity_ref`, `counterparty_ref`, `transaction_count`, `source_total`, `counterparty_total`, `difference_total`, `status`, `actor_ref`, `reconciled_at`, `metadata` |
| [IntercompanySettlement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Models/IntercompanySettlement.php) | `transaction_id`, `settlement_ref`, `amount`, `currency`, `settled_at`, `source_ref`, `metadata` |
| [IntercompanyTransaction.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Models/IntercompanyTransaction.php) | `team_id`, `transaction_ref`, `counterparty_id`, `source_entity_ref`, `target_entity_ref`, `transaction_type`, `description`, `amount`, `currency`, `status`, `transaction_date`, `metadata` |
| [TradingRule.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Models/TradingRule.php) | `counterparty_id`, `rule_ref`, `description`, `pricing_method`, `markup_percent`, `currency`, `active`, `metadata` |
| [TransferPricingEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany/src/Models/TransferPricingEvidence.php) | `transaction_id`, `evidence_ref`, `kind`, `file_ref`, `description`, `arm_length_value`, `currency`, `captured_at`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [IntercompanyController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany-api/src/Http/Controllers/IntercompanyController.php) | `public function __construct(private readonly IntercompanyQuery $query)`<br>`public function index(Request $r): IntercompanyTransactionResource`<br>`public function counterparty(Request $r, CreateCounterparty $a): JsonResponse`<br>`public function rule(Request $r, IntercompanyCounterparty $counterparty, ConfigureTradingRule $a): JsonResponse`<br>`public function store(Request $r, IntercompanyCounterparty $counterparty, CreateTransaction $a): IntercompanyTransactionResource`<br>`public function show(IntercompanyTransaction $transaction): IntercompanyTransactionResource`<br>`public function confirm(Request $r, IntercompanyTransaction $transaction, ConfirmTransaction $a): IntercompanyTransactionResource`<br>`public function settle(Request $r, IntercompanyTransaction $transaction, SettleTransaction $a): IntercompanyTransactionResource`<br>`public function difference(Request $r, IntercompanyTransaction $transaction, RecordDifference $a): JsonResponse`<br>`public function evidence(Request $r, IntercompanyTransaction $transaction, AddTransferPricingEvidence $a): JsonResponse`<br>`public function summary(IntercompanyTransaction $transaction): JsonResponse`<br>`public function reconcile(Request $r, ReconcileIntercompany $a): JsonResponse` |

**Observed route declarations:**

[modules/accounting-intercompany-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-intercompany-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/intercompany')->group(function (): void {
Route::get('/', [IntercompanyController::class, 'index'])->name('accounting.intercompany.list');
Route::post('/counterparties', [IntercompanyController::class, 'counterparty'])->name('accounting.intercompany.counterparty');
Route::post('/counterparties/{counterparty}/rules', [IntercompanyController::class, 'rule'])->name('accounting.intercompany.rule');
Route::post('/counterparties/{counterparty}/transactions', [IntercompanyController::class, 'store'])->name('accounting.intercompany.create');
Route::get('/transactions/{transaction}', [IntercompanyController::class, 'show'])->name('accounting.intercompany.show');
Route::post('/transactions/{transaction}/confirm', [IntercompanyController::class, 'confirm'])->name('accounting.intercompany.confirm');
Route::post('/transactions/{transaction}/settle', [IntercompanyController::class, 'settle'])->name('accounting.intercompany.settle');
Route::post('/transactions/{transaction}/differences', [IntercompanyController::class, 'difference'])->name('accounting.intercompany.difference');
Route::post('/transactions/{transaction}/evidence', [IntercompanyController::class, 'evidence'])->name('accounting.intercompany.evidence');
Route::get('/transactions/{transaction}/summary', [IntercompanyController::class, 'summary'])->name('accounting.intercompany.summary');
Route::post('/reconciliations', [IntercompanyController::class, 'reconcile'])->name('accounting.intercompany.reconcile');
```
<!-- layer-implementation-plan:end -->
