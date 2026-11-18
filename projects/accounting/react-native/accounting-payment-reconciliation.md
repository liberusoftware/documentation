# Accounting Payment Reconciliation React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-payment-reconciliation). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-payment-reconciliation-react-native
**Matching core package:** module-accounting-accounting-payment-reconciliation ([implementation](../core/accounting-payment-reconciliation.md))
**Matching API package:** module-accounting-accounting-payment-reconciliation-api ([contract](../api/accounting-payment-reconciliation.md))

## Implementation plan

This adapter presents Accounting Payment Reconciliation for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Payment Reconciliation API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/accounting-payment-reconciliation.md), and [API module](../api/accounting-payment-reconciliation.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `accounting-payment-reconciliation`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-payment-reconciliation.md)) |
| Capability React Native module skeleton | [`module-accounting-payment-reconciliation-react-native`](https://github.com/liberusoftware/module-accounting-payment-reconciliation-react-native) (`@liberusoftware/module-accounting-payment-reconciliation-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Gateway/merchant settlement imports** | Progressive mobile list/detail/sheet flow for `gateway/merchant settlement imports` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Gross-to-net fees/refunds/disputes** | Progressive mobile list/detail/sheet flow for `gross-to-net fees/refunds/disputes` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Matching** | Progressive mobile list/detail/sheet flow for `matching` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Missing items** | Progressive mobile list/detail/sheet flow for `missing items` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Provider drift** | Progressive mobile list/detail/sheet flow for `provider drift` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [SettlementQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Queries/SettlementQuery.php) | `public function paginate(?int $teamId = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function summary(?int $teamId = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [IdentifyMissingItems.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Actions/IdentifyMissingItems.php) | `public function handle(SettlementRun $run, array $expected): array` |
| [ImportSettlement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Actions/ImportSettlement.php) | `public function handle(array $attributes, array $items): SettlementRun` |
| [MatchSettlementItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Actions/MatchSettlementItem.php) | `public function handle(SettlementItem $item, string $referenceType, string $referenceId, float $amount, ?int $actorId = null, ?string $idempotencyKey = null): SettlementMatch` |
| [RecordProviderDrift.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Actions/RecordProviderDrift.php) | `public function handle(SettlementRun $run, string $field, mixed $expected, mixed $actual, string $severity = 'warning'): ProviderDrift` |
| [ResolveReconciliationException.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Actions/ResolveReconciliationException.php) | `public function handle(ReconciliationException $exception, int $actorId, string $resolution, bool $waive = false): ReconciliationException` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AuditEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Models/AuditEvidence.php) | `run_id`, `event_type`, `actor_id`, `payload`, `payload_hash`, `created_at` |
| [ProviderDrift.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Models/ProviderDrift.php) | `run_id`, `field`, `expected_value`, `actual_value`, `severity`, `status`, `resolution`, `resolved_by`, `resolved_at`, `metadata` |
| [ReconciliationException.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Models/ReconciliationException.php) | `run_id`, `kind`, `external_ref`, `expected_amount`, `actual_amount`, `currency`, `status`, `severity`, `resolution`, `resolved_by`, `resolved_at`, `metadata` |
| [SettlementItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Models/SettlementItem.php) | `run_id`, `external_ref`, `type`, `currency`, `gross_amount`, `fee_amount`, `refund_amount`, `dispute_amount`, `net_amount`, `status`, `reference_type`, `reference_id`, `source_payload`, `source_hash`, `metadata` |
| [SettlementMatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Models/SettlementMatch.php) | `run_id`, `item_id`, `reference_type`, `reference_id`, `matched_amount`, `confidence`, `status`, `matched_by`, `matched_at`, `idempotency_key`, `metadata` |
| [SettlementRun.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation/src/Models/SettlementRun.php) | `team_id`, `provider`, `merchant_ref`, `settlement_ref`, `period_start`, `period_end`, `currency`, `gross_amount`, `fee_amount`, `refund_amount`, `dispute_amount`, `net_amount`, `status`, `idempotency_key`, `source_hash`, `failure_message`, `metadata` |
| [Payment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation-api/src/Models/Payment.php) | `invoice_id`, `payment_date`, `payment_amount`, `qbo_id`, `qbo_sync_token`, `xero_id`, `sage_id`, `journal_entry_id`, `team_id` |

| Observed API controller | Handler signatures |
| --- | --- |
| [PaymentReconciliationController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation-api/src/Http/Controllers/PaymentReconciliationController.php) | `public function index(Request $request, SettlementQuery $query): mixed`<br>`public function store(Request $request, ImportSettlement $action): JsonResponse`<br>`public function show(SettlementRun $settlementRun): SettlementResource`<br>`public function match(Request $request, SettlementItem $settlementItem, MatchSettlementItem $action): JsonResponse`<br>`public function missing(Request $request, SettlementRun $settlementRun, IdentifyMissingItems $action): JsonResponse`<br>`public function drift(Request $request, SettlementRun $settlementRun, RecordProviderDrift $action): JsonResponse`<br>`public function summary(Request $request, SettlementQuery $query): array` |

**Observed route declarations:**

[modules/accounting-payment-reconciliation-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payment-reconciliation-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/payment-reconciliation')->group(function (): void {
Route::get('/', [PaymentReconciliationController::class, 'index'])->name('accounting.payment-reconciliation.list');
Route::post('/', [PaymentReconciliationController::class, 'store'])->name('accounting.payment-reconciliation.create');
Route::get('/summary', [PaymentReconciliationController::class, 'summary'])->name('accounting.payment-reconciliation.summary');
Route::get('/{settlementRun}', [PaymentReconciliationController::class, 'show'])->name('accounting.payment-reconciliation.show');
Route::post('/{settlementRun}/missing-items', [PaymentReconciliationController::class, 'missing'])->name('accounting.payment-reconciliation.missing');
Route::post('/{settlementRun}/provider-drift', [PaymentReconciliationController::class, 'drift'])->name('accounting.payment-reconciliation.drift');
Route::post('/items/{settlementItem}/match', [PaymentReconciliationController::class, 'match'])->name('accounting.payment-reconciliation.match');
```
<!-- layer-implementation-plan:end -->
