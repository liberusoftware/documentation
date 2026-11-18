# Accounting Payroll Payments Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-payroll-payments). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-payroll-payments-flutter
**Matching core package:** module-accounting-accounting-payroll-payments ([implementation](../core/accounting-payroll-payments.md))
**Matching API package:** module-accounting-accounting-payroll-payments-api ([contract](../api/accounting-payroll-payments.md))

## Implementation plan

This adapter presents Accounting Payroll Payments for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Payroll Payments API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/accounting-payroll-payments.md), and [API module](../api/accounting-payroll-payments.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `accounting-payroll-payments`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-accounting-erp-mobile-flutter`](https://github.com/liberusoftware/project-accounting-erp-mobile-flutter) | [`module-accounting-payroll-payments-flutter`](https://github.com/liberusoftware/module-accounting-payroll-payments-flutter) (`module_accounting_payroll_payments_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-accounting-erp-dart-mobile`](https://github.com/liberusoftware/project-accounting-erp-dart-mobile) | [`module-accounting-payroll-payments-dart-mobile`](https://github.com/liberusoftware/module-accounting-payroll-payments-dart-mobile) (`module_accounting_payroll_payments_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-accounting-erp-dart-desktop`](https://github.com/liberusoftware/project-accounting-erp-dart-desktop) | [`module-accounting-payroll-payments-dart-desktop`](https://github.com/liberusoftware/module-accounting-payroll-payments-dart-desktop) (`module_accounting_payroll_payments_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | [API plan](../api/accounting-payroll-payments.md) · [Core plan](../core/accounting-payroll-payments.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Net-pay and liability batch references** | Adaptive mobile cards/sheets for `net-pay and liability batch references` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `net-pay and liability batch references` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Approvals** | Adaptive mobile cards/sheets for `approvals` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `approvals` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Bank/provider status** | Adaptive mobile cards/sheets for `bank/provider status` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `bank/provider status` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Failures** | Adaptive mobile cards/sheets for `failures` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `failures` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Bank reconciliation** | Adaptive mobile cards/sheets for `bank reconciliation` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `bank reconciliation` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

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
