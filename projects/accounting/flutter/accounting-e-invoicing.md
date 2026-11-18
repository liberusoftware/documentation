# Accounting E Invoicing Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-e-invoicing). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-e-invoicing-flutter
**Matching core package:** module-accounting-accounting-e-invoicing ([implementation](../core/accounting-e-invoicing.md))
**Matching API package:** module-accounting-accounting-e-invoicing-api ([contract](../api/accounting-e-invoicing.md))

## Implementation plan

This adapter presents Accounting E Invoicing for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting E Invoicing API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/accounting-e-invoicing.md), and [API module](../api/accounting-e-invoicing.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `accounting-e-invoicing`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-accounting-erp-mobile-flutter`](https://github.com/liberusoftware/project-accounting-erp-mobile-flutter) | [`module-accounting-e-invoicing-flutter`](https://github.com/liberusoftware/module-accounting-e-invoicing-flutter) (`module_accounting_e_invoicing_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-accounting-erp-dart-mobile`](https://github.com/liberusoftware/project-accounting-erp-dart-mobile) | [`module-accounting-e-invoicing-dart-mobile`](https://github.com/liberusoftware/module-accounting-e-invoicing-dart-mobile) (`module_accounting_e_invoicing_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-accounting-erp-dart-desktop`](https://github.com/liberusoftware/project-accounting-erp-dart-desktop) | [`module-accounting-e-invoicing-dart-desktop`](https://github.com/liberusoftware/module-accounting-e-invoicing-dart-desktop) (`module_accounting_e_invoicing_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | [API plan](../api/accounting-e-invoicing.md) · [Core plan](../core/accounting-e-invoicing.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Structured invoice/credit formats** | Adaptive mobile cards/sheets for `structured invoice/credit formats` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `structured invoice/credit formats` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Tax-ID validation** | Adaptive mobile cards/sheets for `tax-id validation` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `tax-id validation` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Network/provider routing** | Adaptive mobile cards/sheets for `network/provider routing` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `network/provider routing` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Signatures** | Adaptive mobile cards/sheets for `signatures` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `signatures` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Delivery/receipt status** | Adaptive mobile cards/sheets for `delivery/receipt status` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `delivery/receipt status` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Archival** | Adaptive mobile cards/sheets for `archival` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `archival` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Reconciliation** | Adaptive mobile cards/sheets for `reconciliation` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `reconciliation` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [EInvoiceQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Queries/EInvoiceQuery.php) | `public function paginate(?int $legalEntityId = null, ?DocumentStatus $status = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ArchiveEInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Actions/ArchiveEInvoice.php) | `public function handle(EInvoiceDocument $d, ?string $actor = null): EInvoiceDocument` |
| [CreateEInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Actions/CreateEInvoice.php) | `public function handle(array $a): EInvoiceDocument` |
| [ReconcileEInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Actions/ReconcileEInvoice.php) | `public function handle(EInvoiceDocument $d, ?string $actor = null): EInvoiceDocument` |
| [RecordEInvoiceReceipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Actions/RecordEInvoiceReceipt.php) | `public function handle(EInvoiceDocument $d, bool $accepted, ?string $message = null, ?string $actor = null): EInvoiceDocument` |
| [SignEInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Actions/SignEInvoice.php) | `public function handle(EInvoiceDocument $d, string $signature, ?string $actor = null): EInvoiceDocument` |
| [SubmitEInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Actions/SubmitEInvoice.php) | `public function handle(EInvoiceDocument $d, string $provider, ?string $actor = null): EInvoiceDocument` |
| [ValidateEInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Actions/ValidateEInvoice.php) | `public function handle(EInvoiceDocument $d, ?string $actor = null): EInvoiceDocument` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [EInvoiceDocument.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Models/EInvoiceDocument.php) | `legal_entity_id`, `document_ref`, `document_type`, `format`, `status`, `tax_id`, `counterparty_ref`, `currency`, `provider_ref`, `payload`, `signature`, `submitted_at`, `received_at`, `archived_at`, `metadata` |
| [EInvoiceEvent.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing/src/Models/EInvoiceEvent.php) | `document_id`, `event`, `provider_ref`, `actor_ref`, `message`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [EInvoicingController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing-api/src/Http/Controllers/EInvoicingController.php) | `public function __construct(private readonly EInvoiceQuery $query)`<br>`public function index(Request $r): mixed`<br>`public function store(Request $r, CreateEInvoice $a): EInvoiceResource`<br>`public function show(EInvoiceDocument $d): EInvoiceResource`<br>`public function validateDocument(Request $r, EInvoiceDocument $d, ValidateEInvoice $a): EInvoiceResource`<br>`public function sign(Request $r, EInvoiceDocument $d, SignEInvoice $a): EInvoiceResource`<br>`public function submit(Request $r, EInvoiceDocument $d, SubmitEInvoice $a): EInvoiceResource`<br>`public function receipt(Request $r, EInvoiceDocument $d, RecordEInvoiceReceipt $a): EInvoiceResource`<br>`public function reconcile(Request $r, EInvoiceDocument $d, ReconcileEInvoice $a): EInvoiceResource`<br>`public function archive(Request $r, EInvoiceDocument $d, ArchiveEInvoice $a): EInvoiceResource` |

**Observed route declarations:**

[modules/accounting-e-invoicing-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-e-invoicing-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/e-invoicing')->group(function (): void {
Route::middleware('ability:accounting.e-invoicing.read')->group(function (): void {
Route::get('/', [EInvoicingController::class, 'index']);
Route::get('/{d}', [EInvoicingController::class, 'show']);
Route::middleware('ability:accounting.e-invoicing.write')->group(function (): void {
Route::post('/', [EInvoicingController::class, 'store']);
Route::post('/{d}/validate', [EInvoicingController::class, 'validateDocument']);
Route::post('/{d}/sign', [EInvoicingController::class, 'sign']);
Route::post('/{d}/submit', [EInvoicingController::class, 'submit']);
Route::post('/{d}/receipt', [EInvoicingController::class, 'receipt']);
Route::post('/{d}/reconcile', [EInvoicingController::class, 'reconcile']);
Route::post('/{d}/archive', [EInvoicingController::class, 'archive']);
```
<!-- layer-implementation-plan:end -->
