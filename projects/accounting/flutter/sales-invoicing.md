# Sales Invoicing Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#sales-invoicing). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-sales-invoicing-flutter
**Matching core package:** module-accounting-sales-invoicing ([implementation](../core/sales-invoicing.md))
**Matching API package:** module-accounting-sales-invoicing-api ([contract](../api/sales-invoicing.md))

## Implementation plan

This adapter presents Sales Invoicing for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Sales Invoicing API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/sales-invoicing.md), and [API module](../api/sales-invoicing.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `sales-invoicing`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-accounting-erp-mobile-flutter`](https://github.com/liberusoftware/project-accounting-erp-mobile-flutter) | [`module-accounting-sales-invoicing-flutter`](https://github.com/liberusoftware/module-accounting-sales-invoicing-flutter) (`module_accounting_sales_invoicing_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-accounting-erp-dart-mobile`](https://github.com/liberusoftware/project-accounting-erp-dart-mobile) | [`module-accounting-sales-invoicing-dart-mobile`](https://github.com/liberusoftware/module-accounting-sales-invoicing-dart-mobile) (`module_accounting_sales_invoicing_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-accounting-erp-dart-desktop`](https://github.com/liberusoftware/project-accounting-erp-dart-desktop) | [`module-accounting-sales-invoicing-dart-desktop`](https://github.com/liberusoftware/module-accounting-sales-invoicing-dart-desktop) (`module_accounting_sales_invoicing_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | [API plan](../api/sales-invoicing.md) · [Core plan](../core/sales-invoicing.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Draft/approved/final invoices** | Adaptive mobile cards/sheets for `draft/approved/final invoices` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `draft/approved/final invoices` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Line items** | Adaptive mobile cards/sheets for `line items` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `line items` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Tax** | Adaptive mobile cards/sheets for `tax` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `tax` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Discounts** | Adaptive mobile cards/sheets for `discounts` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `discounts` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Deposits** | Adaptive mobile cards/sheets for `deposits` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `deposits` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Recurring sources** | Adaptive mobile cards/sheets for `recurring sources` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `recurring sources` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Branding** | Adaptive mobile cards/sheets for `branding` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `branding` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **PDFs** | Adaptive mobile cards/sheets for `pdfs` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `pdfs` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Delivery** | Adaptive mobile cards/sheets for `delivery` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `delivery` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Immutability** | Adaptive mobile cards/sheets for `immutability` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `immutability` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApproveInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing/src/Actions/ApproveInvoice.php) | `public function handle(SalesInvoice $invoice): SalesInvoice` |
| [CreateInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing/src/Actions/CreateInvoice.php) | `public function handle(array $attributes, array $lines): SalesInvoice` |
| [FinalizeInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing/src/Actions/FinalizeInvoice.php) | `public function handle(SalesInvoice $invoice, ?string $actor = null): SalesInvoice` |
| [GenerateInvoicePdf.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing/src/Actions/GenerateInvoicePdf.php) | `public function handle(SalesInvoice $invoice, string $format = 'pdf'): array` |
| [MarkInvoiceDelivered.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing/src/Actions/MarkInvoiceDelivered.php) | `public function handle(SalesInvoice $invoice): SalesInvoice` |
| [RecordDeposit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing/src/Actions/RecordDeposit.php) | `public function handle(SalesInvoice $invoice, array $attributes): SalesInvoice` |
| [SetInvoiceBranding.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing/src/Actions/SetInvoiceBranding.php) | `public function handle(SalesInvoice $invoice, array $branding): SalesInvoice` |
| [SetRecurringSource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing/src/Actions/SetRecurringSource.php) | `public function handle(SalesInvoice $invoice, array $source): SalesInvoice` |
| [SalesInvoicingPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing-api/src/Policies/SalesInvoicingPolicy.php) | `public function viewAny(?Authenticatable $u): bool`<br>`public function view(?Authenticatable $u, SalesInvoice $i): bool`<br>`public function create(?Authenticatable $u): bool`<br>`public function update(?Authenticatable $u, SalesInvoice $i): bool`<br>`public function delete(?Authenticatable $u, SalesInvoice $i): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SalesInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing/src/Models/SalesInvoice.php) | `invoice_number`, `party_id`, `invoice_date`, `due_on`, `status`, `subtotal`, `discount_total`, `tax_total`, `total`, `currency`, `notes`, `branding`, `recurring_source`, `delivery_status`, `delivered_at`, `metadata` |
| [SalesInvoiceDeposit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing/src/Models/SalesInvoiceDeposit.php) | `invoice_id`, `amount`, `currency`, `reference`, `received_by` |
| [SalesInvoiceLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing/src/Models/SalesInvoiceLine.php) | `invoice_id`, `description`, `quantity`, `unit_price`, `discount_rate`, `tax_rate`, `net_amount`, `tax_amount`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [SalesInvoicingController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing-api/src/Http/Controllers/SalesInvoicingController.php) | `public function index(Request $request)`<br>`public function show(string $invoice): SalesInvoiceResource`<br>`public function store(Request $request, CreateInvoice $create)`<br>`public function approve(string $invoice, ApproveInvoice $approve): SalesInvoiceResource`<br>`public function finalize(Request $request, string $invoice, FinalizeInvoice $finalize): SalesInvoiceResource`<br>`public function deposit(Request $request, string $invoice, RecordDeposit $deposit): SalesInvoiceResource`<br>`public function deliver(string $invoice, MarkInvoiceDelivered $deliver): SalesInvoiceResource`<br>`public function destroy(string $invoice): Response` |

**Observed route declarations:**

[modules/accounting-sales-invoicing-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-invoicing-api/routes/api.php)

```php
Route::middleware(['auth:sanctum', 'throttle:60,1'])->prefix('api/v1/accounting/sales-invoicing')->group(function (): void {
Route::get('/', [SalesInvoicingController::class, 'index'])->middleware('ability:accounting.invoices.read');
Route::post('/', [SalesInvoicingController::class, 'store'])->middleware('ability:accounting.invoices.write');
Route::get('/{invoice}', [SalesInvoicingController::class, 'show'])->middleware('ability:accounting.invoices.read');
Route::post('/{invoice}/approve', [SalesInvoicingController::class, 'approve'])->middleware('ability:accounting.invoices.write');
Route::post('/{invoice}/finalize', [SalesInvoicingController::class, 'finalize'])->middleware('ability:accounting.invoices.write');
Route::post('/{invoice}/deposit', [SalesInvoicingController::class, 'deposit'])->middleware('ability:accounting.invoices.write');
Route::post('/{invoice}/deliver', [SalesInvoicingController::class, 'deliver'])->middleware('ability:accounting.invoices.write');
Route::delete('/{invoice}', [SalesInvoicingController::class, 'destroy'])->middleware('ability:accounting.invoices.write');
```
<!-- layer-implementation-plan:end -->
