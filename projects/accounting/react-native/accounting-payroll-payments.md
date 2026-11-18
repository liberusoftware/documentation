# Accounting Payroll Payments React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-payroll-payments). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-payroll-payments-react-native
**Matching core package:** module-accounting-accounting-payroll-payments ([implementation](../core/accounting-payroll-payments.md))
**Matching API package:** module-accounting-accounting-payroll-payments-api ([contract](../api/accounting-payroll-payments.md))

## Implementation plan

This adapter presents Accounting Payroll Payments for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Payroll Payments API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/accounting-payroll-payments.md), and [API module](../api/accounting-payroll-payments.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `accounting-payroll-payments`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-payroll-payments.md)) |
| Capability React Native module skeleton | [`module-accounting-payroll-payments-react-native`](https://github.com/liberusoftware/module-accounting-payroll-payments-react-native) (`@liberusoftware/module-accounting-payroll-payments-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Net-pay and liability batch references** | Progressive mobile list/detail/sheet flow for `net-pay and liability batch references` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Approvals** | Progressive mobile list/detail/sheet flow for `approvals` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Bank/provider status** | Progressive mobile list/detail/sheet flow for `bank/provider status` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Failures** | Progressive mobile list/detail/sheet flow for `failures` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Bank reconciliation** | Progressive mobile list/detail/sheet flow for `bank reconciliation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [PayrollPaymentSummary.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-payments/src/Queries/PayrollPaymentSummary.php) | `public function forTeam(?int $teamId = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreatePayrollPaymentBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-payments/src/Actions/CreatePayrollPaymentBatch.php) | `public function handle(array $attributes): PayrollPaymentBatch` |
| [TransitionPayrollPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-payments/src/Actions/TransitionPayrollPayment.php) | `public function handle(PayrollPaymentBatch $batch, PaymentStatus $status, ?array $details = null): PayrollPaymentBatch` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PayrollPaymentBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-payments/src/Models/PayrollPaymentBatch.php) | `team_id`, `batch_ref`, `net_pay_ref`, `liability_ref`, `currency`, `net_pay_amount`, `liability_amount`, `status`, `provider`, `provider_payment_ref`, `failure_code`, `failure_message`, `approved_by`, `approved_at`, `submitted_at`, `settled_at`, `reconciled_at`, `reconciliation_ref`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [PayrollPaymentsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-payments-api/src/Http/Controllers/PayrollPaymentsController.php) | `public function index(Request $request): AnonymousResourceCollection`<br>`public function store(Request $request, CreatePayrollPaymentBatch $action): JsonResponse`<br>`public function show(Request $request, PayrollPaymentBatch $payrollPaymentBatch): PayrollPaymentBatchResource`<br>`public function transition(Request $request, PayrollPaymentBatch $payrollPaymentBatch, TransitionPayrollPayment $action): PayrollPaymentBatchResource`<br>`public function summary(Request $request, PayrollPaymentSummary $query): array` |

**Observed route declarations:**

[modules/accounting-payroll-payments-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-payments-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/payroll-payments')->group(function (): void {
Route::middleware('ability:accounting.payroll-payments.read')->group(function (): void {
Route::get('/', [PayrollPaymentsController::class, 'index']);
Route::get('/summary', [PayrollPaymentsController::class, 'summary']);
Route::get('/{payrollPaymentBatch}', [PayrollPaymentsController::class, 'show']);
Route::middleware('ability:accounting.payroll-payments.write')->group(function (): void {
Route::post('/', [PayrollPaymentsController::class, 'store']);
Route::post('/{payrollPaymentBatch}/transition', [PayrollPaymentsController::class, 'transition']);
```
<!-- layer-implementation-plan:end -->
