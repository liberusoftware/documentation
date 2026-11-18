# Module Billing Invoicing React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-billing-invoicing). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-billing-module-billing-invoicing-react-native
**Matching core package:** module-billing-module-billing-invoicing ([implementation](../core/module-billing-invoicing.md))
**Matching API package:** module-billing-module-billing-invoicing-api ([contract](../api/module-billing-invoicing.md))

## Implementation plan

This adapter presents Module Billing Invoicing for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Module Billing Invoicing API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/module-billing-invoicing.md), and [API module](../api/module-billing-invoicing.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `module-billing-invoicing`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-billing-mobile-react`](https://github.com/liberusoftware/project-billing-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/module-billing-invoicing.md)) |
| Capability React Native module skeleton | [`module-billing-invoicing-react-native`](https://github.com/liberusoftware/module-billing-invoicing-react-native) (`@liberusoftware/module-billing-invoicing-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Schedules** | Progressive mobile list/detail/sheet flow for `schedules` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Line generation** | Progressive mobile list/detail/sheet flow for `line generation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Tax** | Progressive mobile list/detail/sheet flow for `tax` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Credits** | Progressive mobile list/detail/sheet flow for `credits` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Adjustments** | Progressive mobile list/detail/sheet flow for `adjustments` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **PDFs** | Progressive mobile list/detail/sheet flow for `pdfs` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Delivery** | Progressive mobile list/detail/sheet flow for `delivery` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Finalization** | Progressive mobile list/detail/sheet flow for `finalization` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-billing-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListInvoices.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Queries/ListInvoices.php) | `public function execute(?int $teamId, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddInvoiceLine.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/AddInvoiceLine.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Invoice $invoice, string $description, int $quantity, int $unitAmountMinor, float $taxRate = 0): InvoiceLine` |
| [ApplyInvoiceAdjustment.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/ApplyInvoiceAdjustment.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Invoice $invoice, int $amountMinor, string $reason, string $type = 'adjustment'): Invoice` |
| [ApplyInvoiceLateFee.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/ApplyInvoiceLateFee.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Invoice $invoice, int $amountMinor, ?CarbonInterface $at = null): Invoice` |
| [CreateInvoice.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/CreateInvoice.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): Invoice` |
| [CreateInvoiceSchedule.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/CreateInvoiceSchedule.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): InvoiceSchedule` |
| [CreateInvoiceSupport.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/CreateInvoiceSupport.php) | `public function execute(int $teamId, array $attributes): InvoiceSupport` |
| [CreatePaymentPlan.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/CreatePaymentPlan.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Invoice $invoice, int $totalInstallments, string $frequency = 'monthly', ?CarbonInterface $startAt = null): PaymentPlan` |
| [DeliverInvoice.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/DeliverInvoice.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Invoice $invoice, string $destination, ?int $documentId = null): InvoiceSupport` |
| [FinalizeInvoice.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/FinalizeInvoice.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Invoice $invoice): Invoice` |
| [GenerateInvoiceDocument.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/GenerateInvoiceDocument.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Invoice $invoice, string $format = 'pdf'): InvoiceSupport` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Invoice.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Models/Invoice.php) | No literal fillable array detected; inspect the model and API schema. |
| [InvoiceLine.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Models/InvoiceLine.php) | No literal fillable array detected; inspect the model and API schema. |
| [InvoiceSchedule.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Models/InvoiceSchedule.php) | No literal fillable array detected; inspect the model and API schema. |
| [InvoiceSupport.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Models/InvoiceSupport.php) | No literal fillable array detected; inspect the model and API schema. |
| [PaymentPlan.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Models/PaymentPlan.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [InvoiceController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing-api/src/Http/Controllers/InvoiceController.php) | `public function index(Request $request, ListInvoices $query): JsonResponse`<br>`public function store(Request $request, CreateInvoice $create): JsonResponse`<br>`public function line(Request $request, Invoice $invoice, AddInvoiceLine $add): JsonResponse`<br>`public function finalize(Request $request, Invoice $invoice, FinalizeInvoice $finalize): JsonResponse`<br>`public function schedule(Request $request, CreateInvoiceSchedule $create): JsonResponse`<br>`public function runSchedule(Request $request, InvoiceSchedule $schedule, RunInvoiceSchedule $run): JsonResponse`<br>`public function paymentPlan(Request $request, CreatePaymentPlan $create): JsonResponse`<br>`public function runPaymentPlan(Request $request, PaymentPlan $paymentPlan, RunPaymentPlan $run): JsonResponse`<br>`public function adjust(Request $request, Invoice $invoice, ApplyInvoiceAdjustment $adjust): JsonResponse`<br>`public function lateFee(Request $request, Invoice $invoice, ApplyInvoiceLateFee $lateFee): JsonResponse`<br>`public function document(Request $request, Invoice $invoice, GenerateInvoiceDocument $document): JsonResponse`<br>`public function deliver(Request $request, Invoice $invoice, DeliverInvoice $deliver): JsonResponse` |
| [InvoiceSupportController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing-api/src/Http/Controllers/InvoiceSupportController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateInvoiceSupport $create): JsonResponse` |

**Observed route declarations:**

[modules/module-billing-invoicing-api/routes/api.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing-api/routes/api.php)

```php
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.invoicing.read'])->prefix('api/v1/billing/invoicing/support')->name('billing.invoicing.support.')->group(function (): void {
Route::get('/', [InvoiceSupportController::class, 'index'])->name('index');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.invoicing.write', 'idempotency'])->prefix('api/v1/billing/invoicing/support')->name('billing.invoicing.support.')->group(function (): void {
Route::post('/', [InvoiceSupportController::class, 'store'])->name('store');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.invoicing.read'])->prefix('api/v1/billing/invoicing')->name('billing.invoicing.')->group(function (): void {
Route::get('/', [InvoiceController::class, 'index'])->name('index');
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.invoicing.write', 'idempotency'])->prefix('api/v1/billing/invoicing')->name('billing.invoicing.')->group(function (): void {
Route::post('/', [InvoiceController::class, 'store'])->name('store');
Route::post('/schedules', [InvoiceController::class, 'schedule'])->name('schedule');
Route::post('/schedules/{schedule}/run', [InvoiceController::class, 'runSchedule'])->name('schedule.run');
Route::post('/payment-plans', [InvoiceController::class, 'paymentPlan'])->name('payment-plan.create');
Route::post('/payment-plans/{paymentPlan}/run', [InvoiceController::class, 'runPaymentPlan'])->name('payment-plan.run');
Route::post('/{invoice}/lines', [InvoiceController::class, 'line'])->name('line');
Route::post('/{invoice}/finalize', [InvoiceController::class, 'finalize'])->name('finalize');
Route::post('/{invoice}/adjustments', [InvoiceController::class, 'adjust'])->name('adjust');
Route::post('/{invoice}/late-fees', [InvoiceController::class, 'lateFee'])->name('late-fee');
Route::post('/{invoice}/document', [InvoiceController::class, 'document'])->name('document');
Route::post('/{invoice}/deliver', [InvoiceController::class, 'deliver'])->name('deliver');
```
<!-- layer-implementation-plan:end -->
