# Payroll Integration React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#payroll-integration). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-payroll-integration-react-native
**Matching core package:** module-accounting-payroll-integration ([implementation](../core/payroll-integration.md))
**Matching API package:** module-accounting-payroll-integration-api ([contract](../api/payroll-integration.md))

## Implementation plan

This adapter presents Payroll Integration for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Payroll Integration API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/payroll-integration.md), and [API module](../api/payroll-integration.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `payroll-integration`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/payroll-integration.md)) |
| Capability React Native module skeleton | [`module-accounting-payroll-integration-react-native`](https://github.com/liberusoftware/module-accounting-payroll-integration-react-native) (`@liberusoftware/module-accounting-payroll-integration-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Provider/period/run identity** | Progressive mobile list/detail/sheet flow for `provider/period/run identity` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Employee/contractor references** | Progressive mobile list/detail/sheet flow for `employee/contractor references` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Import validation** | Progressive mobile list/detail/sheet flow for `import validation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Dimensions/projects** | Progressive mobile list/detail/sheet flow for `dimensions/projects` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Provider adapters** | Progressive mobile list/detail/sheet flow for `provider adapters` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

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
