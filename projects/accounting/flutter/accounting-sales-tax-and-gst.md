# Accounting Sales Tax And Gst Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-sales-tax-and-gst). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-sales-tax-and-gst-flutter
**Matching core package:** module-accounting-accounting-sales-tax-and-gst ([implementation](../core/accounting-sales-tax-and-gst.md))
**Matching API package:** module-accounting-accounting-sales-tax-and-gst-api ([contract](../api/accounting-sales-tax-and-gst.md))

## Implementation plan

This adapter presents Accounting Sales Tax And Gst for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Sales Tax And Gst API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/accounting-sales-tax-and-gst.md), and [API module](../api/accounting-sales-tax-and-gst.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `accounting-sales-tax-and-gst`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-accounting-erp-mobile-flutter`](https://github.com/liberusoftware/project-accounting-erp-mobile-flutter) | [`module-accounting-sales-tax-and-gst-flutter`](https://github.com/liberusoftware/module-accounting-sales-tax-and-gst-flutter) (`module_accounting_sales_tax_and_gst_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-accounting-erp-dart-mobile`](https://github.com/liberusoftware/project-accounting-erp-dart-mobile) | [`module-accounting-sales-tax-and-gst-dart-mobile`](https://github.com/liberusoftware/module-accounting-sales-tax-and-gst-dart-mobile) (`module_accounting_sales_tax_and_gst_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-accounting-erp-dart-desktop`](https://github.com/liberusoftware/project-accounting-erp-dart-desktop) | [`module-accounting-sales-tax-and-gst-dart-desktop`](https://github.com/liberusoftware/module-accounting-sales-tax-and-gst-dart-desktop) (`module_accounting_sales_tax_and_gst_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | [API plan](../api/accounting-sales-tax-and-gst.md) · [Core plan](../core/accounting-sales-tax-and-gst.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Registrations/nexus** | Adaptive mobile cards/sheets for `registrations/nexus` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `registrations/nexus` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Destination/origin rules** | Adaptive mobile cards/sheets for `destination/origin rules` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `destination/origin rules` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Taxable bases** | Adaptive mobile cards/sheets for `taxable bases` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `taxable bases` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Liabilities** | Adaptive mobile cards/sheets for `liabilities` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `liabilities` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Adjustments** | Adaptive mobile cards/sheets for `adjustments` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `adjustments` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Return periods** | Adaptive mobile cards/sheets for `return periods` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `return periods` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Calculation adapters** | Adaptive mobile cards/sheets for `calculation adapters` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `calculation adapters` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [SalesTaxRecordQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-tax-and-gst/src/Queries/SalesTaxRecordQuery.php) | `public function paginate(?string $context = null, ?string $type = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ActivateSalesTaxRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-tax-and-gst/src/Actions/ActivateSalesTaxRecord.php) | `public function handle(SalesTaxRecord $record): SalesTaxRecord` |
| [CloseSalesTaxRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-tax-and-gst/src/Actions/CloseSalesTaxRecord.php) | `public function handle(SalesTaxRecord $record): SalesTaxRecord` |
| [CreateSalesTaxRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-tax-and-gst/src/Actions/CreateSalesTaxRecord.php) | `public function handle(array $attributes): SalesTaxRecord` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SalesTaxRecord.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-tax-and-gst/src/Models/SalesTaxRecord.php) | `context_id`, `type`, `jurisdiction`, `origin`, `destination`, `rate`, `taxable_base`, `liability`, `status`, `period_start`, `period_end`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [SalesTaxController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-tax-and-gst-api/src/Http/Controllers/SalesTaxController.php) | `public function index(Request $request, SalesTaxRecordQuery $query): mixed`<br>`public function show(SalesTaxRecord $record): SalesTaxResource`<br>`public function store(Request $request, CreateSalesTaxRecord $action): SalesTaxResource`<br>`public function activate(SalesTaxRecord $record, ActivateSalesTaxRecord $action): SalesTaxResource`<br>`public function close(SalesTaxRecord $record, CloseSalesTaxRecord $action): SalesTaxResource` |

**Observed route declarations:**

[modules/accounting-sales-tax-and-gst-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-tax-and-gst-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/sales-tax-and-gst')->group(function (): void {
Route::middleware('ability:accounting.sales-tax-and-gst.read')->group(function (): void {
Route::get('/', [SalesTaxController::class, 'index']);
Route::get('/{record}', [SalesTaxController::class, 'show']);
Route::middleware('ability:accounting.sales-tax-and-gst.write')->group(function (): void {
Route::post('/', [SalesTaxController::class, 'store']);
Route::post('/{record}/activate', [SalesTaxController::class, 'activate']);
Route::post('/{record}/close', [SalesTaxController::class, 'close']);
```
<!-- layer-implementation-plan:end -->
