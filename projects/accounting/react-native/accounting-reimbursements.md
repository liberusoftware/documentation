# Accounting Reimbursements React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-reimbursements). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-reimbursements-react-native
**Matching core package:** module-accounting-accounting-reimbursements ([implementation](../core/accounting-reimbursements.md))
**Matching API package:** module-accounting-accounting-reimbursements-api ([contract](../api/accounting-reimbursements.md))

## Implementation plan

This adapter presents Accounting Reimbursements for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Reimbursements API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/accounting-reimbursements.md), and [API module](../api/accounting-reimbursements.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `accounting-reimbursements`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-reimbursements.md)) |
| Capability React Native module skeleton | [`module-accounting-reimbursements-react-native`](https://github.com/liberusoftware/module-accounting-reimbursements-react-native) (`@liberusoftware/module-accounting-reimbursements-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Approved expense/mileage liabilities** | Progressive mobile list/detail/sheet flow for `approved expense/mileage liabilities` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Payment batches** | Progressive mobile list/detail/sheet flow for `payment batches` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Bank export/provider status** | Progressive mobile list/detail/sheet flow for `bank export/provider status` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Remittance** | Progressive mobile list/detail/sheet flow for `remittance` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Failure** | Progressive mobile list/detail/sheet flow for `failure` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Reconciliation** | Progressive mobile list/detail/sheet flow for `reconciliation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreatePaymentBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-reimbursements/src/Actions/CreatePaymentBatch.php) | `public function handle(array $liabilityIds, ?int $teamId = null): ReimbursementBatch` |
| [CreateReimbursementLiability.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-reimbursements/src/Actions/CreateReimbursementLiability.php) | `public function handle(array $attributes): ReimbursementLiability` |
| [ReconcilePaymentBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-reimbursements/src/Actions/ReconcilePaymentBatch.php) | `public function handle(ReimbursementBatch $batch, float $settledAmount, ?string $externalRef = null): ReimbursementReconciliation` |
| [UpdatePaymentProviderStatus.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-reimbursements/src/Actions/UpdatePaymentProviderStatus.php) | `public function handle(ReimbursementBatch $batch, array $attributes): ReimbursementBatch` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ReimbursementBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-reimbursements/src/Models/ReimbursementBatch.php) | `team_id`, `currency`, `total_amount`, `status`, `provider`, `provider_ref`, `exported_at`, `submitted_at`, `paid_at`, `failure_message`, `metadata` |
| [ReimbursementLiability.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-reimbursements/src/Models/ReimbursementLiability.php) | `team_id`, `payee_ref`, `source_type`, `source_id`, `kind`, `currency`, `amount`, `approved_at`, `status`, `batch_id`, `metadata` |
| [ReimbursementReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-reimbursements/src/Models/ReimbursementReconciliation.php) | `batch_id`, `expected_amount`, `settled_amount`, `variance`, `status`, `external_ref`, `notes`, `metadata` |
| [ReimbursementRemittance.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-reimbursements/src/Models/ReimbursementRemittance.php) | `batch_id`, `payee_ref`, `amount`, `currency`, `status`, `document_ref`, `sent_at`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ReimbursementsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-reimbursements-api/src/Http/Controllers/ReimbursementsController.php) | `public function index(Request $request): mixed`<br>`public function store(Request $request, CreateReimbursementLiability $action): mixed`<br>`public function batch(Request $request, CreatePaymentBatch $action): ReimbursementBatch`<br>`public function status(Request $request, ReimbursementBatch $batch, UpdatePaymentProviderStatus $action): ReimbursementBatch`<br>`public function reconcile(Request $request, ReimbursementBatch $batch, ReconcilePaymentBatch $action): mixed` |

**Observed route declarations:**

[modules/accounting-reimbursements-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-reimbursements-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/reimbursements')->group(function (): void {
Route::middleware('ability:accounting.reimbursements.read')->group(function (): void {
Route::get('/', [ReimbursementsController::class, 'index']);
Route::middleware('ability:accounting.reimbursements.write')->group(function (): void {
Route::post('/', [ReimbursementsController::class, 'store']);
Route::post('/batches', [ReimbursementsController::class, 'batch']);
Route::post('/batches/{batch}/status', [ReimbursementsController::class, 'status']);
Route::post('/batches/{batch}/reconcile', [ReimbursementsController::class, 'reconcile']);
```
<!-- layer-implementation-plan:end -->
