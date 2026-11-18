# Payroll Integration Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#payroll-integration). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-payroll-integration-flutter
**Matching core package:** module-accounting-payroll-integration ([implementation](../core/payroll-integration.md))
**Matching API package:** module-accounting-payroll-integration-api ([contract](../api/payroll-integration.md))

## Implementation plan

This adapter presents Payroll Integration for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Payroll Integration API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/payroll-integration.md), and [API module](../api/payroll-integration.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `payroll-integration`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-accounting-erp-mobile-flutter`](https://github.com/liberusoftware/project-accounting-erp-mobile-flutter) | [`module-accounting-payroll-integration-flutter`](https://github.com/liberusoftware/module-accounting-payroll-integration-flutter) (`module_accounting_payroll_integration_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-accounting-erp-dart-mobile`](https://github.com/liberusoftware/project-accounting-erp-dart-mobile) | [`module-accounting-payroll-integration-dart-mobile`](https://github.com/liberusoftware/module-accounting-payroll-integration-dart-mobile) (`module_accounting_payroll_integration_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-accounting-erp-dart-desktop`](https://github.com/liberusoftware/project-accounting-erp-dart-desktop) | [`module-accounting-payroll-integration-dart-desktop`](https://github.com/liberusoftware/module-accounting-payroll-integration-dart-desktop) (`module_accounting_payroll_integration_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | [API plan](../api/payroll-integration.md) · [Core plan](../core/payroll-integration.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Provider/period/run identity** | Adaptive mobile cards/sheets for `provider/period/run identity` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `provider/period/run identity` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Employee/contractor references** | Adaptive mobile cards/sheets for `employee/contractor references` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `employee/contractor references` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Import validation** | Adaptive mobile cards/sheets for `import validation` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `import validation` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Dimensions/projects** | Adaptive mobile cards/sheets for `dimensions/projects` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `dimensions/projects` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Provider adapters** | Adaptive mobile cards/sheets for `provider adapters` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `provider adapters` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-accounting-erp-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [PayrollImportSummary.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-integration/src/Queries/PayrollImportSummary.php) | `public function forTeam(?int $teamId = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ImportPayrollRun.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-integration/src/Actions/ImportPayrollRun.php) | `public function handle(array $attributes): PayrollImport` |
| [MarkPayrollImport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-integration/src/Actions/MarkPayrollImport.php) | `public function handle(PayrollImport $import, ImportStatus $status): PayrollImport` |
| [PayrollProviderAdapter.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-integration/src/Contracts/PayrollProviderAdapter.php) | `public function validateImport(array $payload): array`<br>`public function import(array $payload): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PayrollImport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-integration/src/Models/PayrollImport.php) | `team_id`, `provider`, `period_start`, `period_end`, `run_ref`, `currency`, `employee_refs`, `contractor_refs`, `dimensions`, `project_refs`, `payload_hash`, `validation_errors`, `adapter_ref`, `status`, `imported_at`, `reconciled_at`, `metadata` |
| [Payroll.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-integration-api/src/Models/Payroll.php) | `employee_id`, `base_salary`, `overtime_hours`, `overtime_rate`, `tax_deductions`, `other_deductions`, `net_salary`, `pay_period_start`, `pay_period_end`, `payment_date`, `payment_status` |

| Observed API controller | Handler signatures |
| --- | --- |
| [PayrollIntegrationController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-integration-api/src/Http/Controllers/PayrollIntegrationController.php) | `public function index(Request $request): AnonymousResourceCollection`<br>`public function store(Request $request, ImportPayrollRun $action): JsonResponse`<br>`public function show(Request $request, PayrollImport $payrollImport): PayrollImportResource`<br>`public function status(Request $request, PayrollImport $payrollImport, MarkPayrollImport $action): PayrollImportResource`<br>`public function summary(Request $request, PayrollImportSummary $query): array` |

**Observed route declarations:**

[modules/accounting-payroll-integration-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-integration-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/payroll-integration')->group(function (): void {
Route::middleware('ability:accounting.payroll-integration.read')->group(function (): void {
Route::get('/', [PayrollIntegrationController::class, 'index']);
Route::get('/summary', [PayrollIntegrationController::class, 'summary']);
Route::get('/{payrollImport}', [PayrollIntegrationController::class, 'show']);
Route::middleware('ability:accounting.payroll-integration.write')->group(function (): void {
Route::post('/', [PayrollIntegrationController::class, 'store']);
Route::post('/{payrollImport}/status', [PayrollIntegrationController::class, 'status']);
```
<!-- layer-implementation-plan:end -->
