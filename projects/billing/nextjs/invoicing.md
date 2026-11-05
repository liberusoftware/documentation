# Invoicing: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-billing-invoicing`.

**Proposed design identifier:** `module-billing-invoicing-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/invoicing.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-billing-invoicing](../../../modules/source/liberusoftware--module-billing-invoicing.md) |
| API | [liberusoftware/module-billing-invoicing-api](../../../modules/source/liberusoftware--module-billing-invoicing-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Schedules | A focused authorized view or workflow section for schedules; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Line generation | A focused authorized view or workflow section for line generation; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Tax | A focused authorized view or workflow section for tax; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Credits | A focused authorized view or workflow section for credits; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Adjustments | A focused authorized view or workflow section for adjustments; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| PDFs | A focused authorized view or workflow section for pdfs; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Delivery | A focused authorized view or workflow section for delivery; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Finalization | A focused authorized view or workflow section for finalization; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

These are observed PHP query entry points, not assumed HTTP endpoints. Use an owning API adapter to authorize and serialize their results.

| Source query | Signatures |
| --- | --- |
| [ListInvoices.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Queries/ListInvoices.php) | `public function execute(?int $teamId, int $perPage = 25): LengthAwarePaginator` |

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [AddInvoiceLine.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/AddInvoiceLine.php) | `public function execute(Invoice $invoice, string $description, int $quantity, int $unitAmountMinor, float $taxRate = 0): InvoiceLine` |
| [ApplyInvoiceAdjustment.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/ApplyInvoiceAdjustment.php) | `public function execute(Invoice $invoice, int $amountMinor, string $reason, string $type = 'adjustment'): Invoice` |
| [ApplyInvoiceLateFee.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/ApplyInvoiceLateFee.php) | `public function execute(Invoice $invoice, int $amountMinor, ?CarbonInterface $at = null): Invoice` |
| [CreateInvoice.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/CreateInvoice.php) | `public function execute(array $attributes): Invoice` |
| [CreateInvoiceSchedule.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/CreateInvoiceSchedule.php) | `public function execute(array $attributes): InvoiceSchedule` |
| [CreateInvoiceSupport.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/CreateInvoiceSupport.php) | `public function execute(int $teamId, array $attributes): InvoiceSupport` |
| [CreatePaymentPlan.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/CreatePaymentPlan.php) | `public function execute(Invoice $invoice, int $totalInstallments, string $frequency = 'monthly', ?CarbonInterface $startAt = null): PaymentPlan` |
| [DeliverInvoice.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/DeliverInvoice.php) | `public function execute(Invoice $invoice, string $destination, ?int $documentId = null): InvoiceSupport` |
| [FinalizeInvoice.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/FinalizeInvoice.php) | `public function execute(Invoice $invoice): Invoice` |
| [GenerateInvoiceDocument.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/GenerateInvoiceDocument.php) | `public function execute(Invoice $invoice, string $format = 'pdf'): InvoiceSupport` |
| [RunInvoiceSchedule.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/RunInvoiceSchedule.php) | `public function execute(InvoiceSchedule $schedule, ?CarbonInterface $at = null): Invoice` |
| [RunPaymentPlan.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Actions/RunPaymentPlan.php) | `public function execute(PaymentPlan $paymentPlan, ?CarbonInterface $at = null): Invoice` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [Invoice.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Models/Invoice.php) | No literal fillable array detected; inspect the model and API schema. |
| [InvoiceLine.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Models/InvoiceLine.php) | No literal fillable array detected; inspect the model and API schema. |
| [InvoiceSchedule.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Models/InvoiceSchedule.php) | No literal fillable array detected; inspect the model and API schema. |
| [InvoiceSupport.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Models/InvoiceSupport.php) | No literal fillable array detected; inspect the model and API schema. |
| [PaymentPlan.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-invoicing/src/Models/PaymentPlan.php) | No literal fillable array detected; inspect the model and API schema. |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

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

## Server/client and React reuse

Keep API credentials and session forwarding in server-only exports. A Server Component may load authorized serializable data and compose a Client Component for interaction. Put ordinary event callbacks inside the client boundary; server-to-client props must follow the framework serialization/action rules.

Share framework-independent React cards, tables, labels, formatting and field primitives with Inertia. Keep `next/link`, Next.js navigation, server actions and cache invalidation in this adapter, and Inertia visits, page props and redirects in its wrapper. Reuse domain/API DTOs without importing PHP models or another application's private frontend state.

## State, failures and verification

| Situation | User-facing behavior and integration requirement |
| --- | --- |
| Loading or empty authorized query | Accessible progress/empty copy; preserve filters and avoid displaying stale records from another scope |
| Expired session or denied permission | Reauthenticate or show a scoped denial; discard protected cached data and do not retry as a broader service identity |
| Invalid command input | Preserve safe draft values, announce field errors and use the authoritative API validation outcome |
| Stale record / concurrent change | Reload/review the current version; do not overwrite silently or invent an ETag contract the API does not support |
| Timeout after a write | Query the operation/current record when supported before retrying; an idempotency key works only if the owning API actually stores/enforces it |
| Long-running or partly failed operation | Show a durable operation reference, progress, last error and a permitted retry/recovery action |

Start authenticated reads with explicit no-store behavior until a reviewed tenant/permission-aware caching policy exists. Refresh affected read models after confirmed mutations; pending transport acceptance is not a completed business transition. Recheck access for evidence/export downloads.

Verify the actual supported query/command journeys, invalid and denied paths, tenant switching, stale state, retry recovery, keyboard/focus behavior and secret exclusion from browser bundles. Build/test the packed adapter in a clean consuming Next.js application using its declared versions and API contract. No npm package or application suite was executed by this plan generator.

See the [Next.js standard](../../../standards/NEXTJS.md), [npm lifecycle guide](../../../guides/NPM.md), [API architecture](../../../architecture/API.md), and [shared ownership guide](../../../architecture/SHARED-MODULES.md).
