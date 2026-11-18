# Module Billing Payments React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-billing-payments). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-billing-module-billing-payments-react-native
**Matching core package:** module-billing-module-billing-payments ([implementation](../core/module-billing-payments.md))
**Matching API package:** module-billing-module-billing-payments-api ([contract](../api/module-billing-payments.md))

## Implementation plan

This adapter presents Module Billing Payments for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Module Billing Payments API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/module-billing-payments.md), and [API module](../api/module-billing-payments.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `module-billing-payments`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-billing-mobile-react`](https://github.com/liberusoftware/project-billing-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/module-billing-payments.md)) |
| Capability React Native module skeleton | [`module-billing-payments-react-native`](https://github.com/liberusoftware/module-billing-payments-react-native) (`@liberusoftware/module-billing-payments-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Unified payment-contracts and payment-core integration** | Progressive mobile list/detail/sheet flow for `unified payment-contracts and payment-core integration` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Methods and vaulted payment instruments** | Progressive mobile list/detail/sheet flow for `methods and vaulted payment instruments` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Mandates and Direct Debit lifecycles** | Progressive mobile list/detail/sheet flow for `mandates and direct debit lifecycles` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Gateway drivers and capability discovery** | Progressive mobile list/detail/sheet flow for `gateway drivers and capability discovery` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Capture and allocation** | Progressive mobile list/detail/sheet flow for `capture and allocation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Refunds and disputes** | Progressive mobile list/detail/sheet flow for `refunds and disputes` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Reconciliation** | Progressive mobile list/detail/sheet flow for `reconciliation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListPayments.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Queries/ListPayments.php) | `public function execute(?int $teamId, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AllocatePayment.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/AllocatePayment.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Payment $payment, int $amountMinor, ?int $invoiceId = null): PaymentAllocation` |
| [CapturePayment.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/CapturePayment.php) | `public function __construct(private DatabaseManager $database, private GatewayManager $gateways)`<br>`public function execute(Payment $payment): Payment` |
| [CreatePayment.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/CreatePayment.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): Payment` |
| [CreatePaymentMandate.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/CreatePaymentMandate.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): PaymentMandate` |
| [CreatePaymentMethod.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/CreatePaymentMethod.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): PaymentMethod` |
| [OpenDispute.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/OpenDispute.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Payment $payment, int $amountMinor, string $reason): PaymentDispute` |
| [ReconcilePayment.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/ReconcilePayment.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Payment $payment, string $providerReference, bool $matched = true, ?string $notes = null): PaymentReconciliation` |
| [RefundPayment.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/RefundPayment.php) | `public function __construct(private DatabaseManager $database, private GatewayManager $gateways)`<br>`public function execute(Payment $payment, int $amountMinor, string $reason = 'requested'): PaymentRefund` |
| [TransitionPaymentMandate.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/TransitionPaymentMandate.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(PaymentMandate $mandate, string $status): PaymentMandate` |
| [TransitionPaymentMethod.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/TransitionPaymentMethod.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(PaymentMethod $method, PaymentMethodStatus $status): PaymentMethod` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Payment.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Models/Payment.php) | No literal fillable array detected; inspect the model and API schema. |
| [PaymentAllocation.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Models/PaymentAllocation.php) | No literal fillable array detected; inspect the model and API schema. |
| [PaymentDispute.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Models/PaymentDispute.php) | No literal fillable array detected; inspect the model and API schema. |
| [PaymentMandate.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Models/PaymentMandate.php) | No literal fillable array detected; inspect the model and API schema. |
| [PaymentMethod.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Models/PaymentMethod.php) | No literal fillable array detected; inspect the model and API schema. |
| [PaymentReconciliation.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Models/PaymentReconciliation.php) | No literal fillable array detected; inspect the model and API schema. |
| [PaymentRefund.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Models/PaymentRefund.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [PaymentController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments-api/src/Http/Controllers/PaymentController.php) | `public function index(Request $request, ListPayments $query): JsonResponse`<br>`public function show(Request $request, Payment $payment): JsonResponse`<br>`public function store(Request $request, CreatePayment $create): JsonResponse`<br>`public function capture(Request $request, Payment $payment, CapturePayment $capture): JsonResponse`<br>`public function refund(Request $request, Payment $payment, RefundPayment $refund): JsonResponse`<br>`public function dispute(Request $request, Payment $payment, OpenDispute $dispute): JsonResponse`<br>`public function allocate(Request $request, Payment $payment, AllocatePayment $allocate): JsonResponse`<br>`public function reconcile(Request $request, Payment $payment, ReconcilePayment $reconcile): JsonResponse` |
| [PaymentMethodController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments-api/src/Http/Controllers/PaymentMethodController.php) | `public function methods(Request $request): JsonResponse`<br>`public function storeMethod(Request $request, CreatePaymentMethod $create): JsonResponse`<br>`public function mandates(Request $request): JsonResponse`<br>`public function storeMandate(Request $request, CreatePaymentMandate $create): JsonResponse`<br>`public function transitionMethod(Request $request, PaymentMethod $method, TransitionPaymentMethod $transition): JsonResponse`<br>`public function transitionMandate(Request $request, PaymentMandate $mandate, TransitionPaymentMandate $transition): JsonResponse` |

**Observed route declarations:**

[modules/module-billing-payments-api/routes/api.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments-api/routes/api.php)

```php
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.payments.read'])
Route::get('/', [PaymentController::class, 'index'])->name('index');
Route::get('/{payment}', [PaymentController::class, 'show'])->whereNumber('payment')->name('show');
Route::get('/methods', [PaymentMethodController::class, 'methods'])->name('methods.index');
Route::get('/mandates', [PaymentMethodController::class, 'mandates'])->name('mandates.index');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.payments.write', 'idempotency'])
Route::post('/', [PaymentController::class, 'store'])->name('store');
Route::post('/methods', [PaymentMethodController::class, 'storeMethod'])->name('methods.store');
Route::post('/mandates', [PaymentMethodController::class, 'storeMandate'])->name('mandates.store');
Route::patch('/methods/{method}/status', [PaymentMethodController::class, 'transitionMethod'])->whereNumber('method')->name('methods.status');
Route::patch('/mandates/{mandate}/status', [PaymentMethodController::class, 'transitionMandate'])->whereNumber('mandate')->name('mandates.status');
Route::post('/{payment}/capture', [PaymentController::class, 'capture'])->name('capture');
Route::post('/{payment}/refund', [PaymentController::class, 'refund'])->name('refund');
Route::post('/{payment}/dispute', [PaymentController::class, 'dispute'])->name('dispute');
Route::post('/{payment}/allocate', [PaymentController::class, 'allocate'])->name('allocate');
Route::post('/{payment}/reconcile', [PaymentController::class, 'reconcile'])->name('reconcile');
```
<!-- layer-implementation-plan:end -->
