# Accounting Contractor Reporting React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-contractor-reporting). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-contractor-reporting-react-native
**Matching core package:** module-accounting-accounting-contractor-reporting ([implementation](../core/accounting-contractor-reporting.md))
**Matching API package:** module-accounting-accounting-contractor-reporting-api ([contract](../api/accounting-contractor-reporting.md))

## Implementation plan

This adapter presents Accounting Contractor Reporting for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Contractor Reporting API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/accounting-contractor-reporting.md), and [API module](../api/accounting-contractor-reporting.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `accounting-contractor-reporting`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-contractor-reporting.md)) |
| Capability React Native module skeleton | [`module-accounting-contractor-reporting-react-native`](https://github.com/liberusoftware/module-accounting-contractor-reporting-react-native) (`@liberusoftware/module-accounting-contractor-reporting-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **1099-style thresholds** | Progressive mobile list/detail/sheet flow for `1099-style thresholds` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Classifications** | Progressive mobile list/detail/sheet flow for `classifications` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Payee validation** | Progressive mobile list/detail/sheet flow for `payee validation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Forms** | Progressive mobile list/detail/sheet flow for `forms` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Electronic filing adapters** | Progressive mobile list/detail/sheet flow for `electronic filing adapters` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Corrections** | Progressive mobile list/detail/sheet flow for `corrections` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Evidence** | Progressive mobile list/detail/sheet flow for `evidence` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ContractorReportQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-reporting/src/Queries/ContractorReportQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CorrectContractorReport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-reporting/src/Actions/CorrectContractorReport.php) | `public function handle(ContractorReport $report, array $correction): ContractorReport` |
| [CreateContractorReport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-reporting/src/Actions/CreateContractorReport.php) | `public function handle(array $attributes): ContractorReport` |
| [FileContractorReport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-reporting/src/Actions/FileContractorReport.php) | `public function handle(ContractorReport $report, string $adapter): ContractorReport` |
| [ValidateContractorReport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-reporting/src/Actions/ValidateContractorReport.php) | `public function handle(ContractorReport $report, array $validation): ContractorReport` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ContractorReport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-reporting/src/Models/ContractorReport.php) | `team_id`, `payee_ref`, `tax_year`, `classification`, `threshold`, `reportable_amount`, `form_type`, `status`, `filing_adapter`, `payee_validation`, `correction`, `evidence` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ContractorReportsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-reporting-api/src/Http/Controllers/ContractorReportsController.php) | `public function index(ContractorReportQuery $query): JsonResponse`<br>`public function store(Request $request, CreateContractorReport $action): JsonResponse`<br>`public function validateReport(Request $request, string $report, ValidateContractorReport $action): JsonResponse`<br>`public function file(Request $request, string $report, FileContractorReport $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-contractor-reporting-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-reporting-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/contractor-reporting')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.contractor-reporting.read')->get('/', [ContractorReportsController::class, 'index']);
Route::middleware('ability:accounting.contractor-reporting.write')->group(function (): void {
Route::post('/', [ContractorReportsController::class, 'store']);
Route::post('/{report}/validate', [ContractorReportsController::class, 'validateReport']);
Route::post('/{report}/file', [ContractorReportsController::class, 'file']);
```
<!-- layer-implementation-plan:end -->
