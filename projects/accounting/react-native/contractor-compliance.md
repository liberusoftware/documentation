# Contractor Compliance React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#contractor-compliance). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-contractor-compliance-react-native
**Matching core package:** module-accounting-contractor-compliance ([implementation](../core/contractor-compliance.md))
**Matching API package:** module-accounting-contractor-compliance-api ([contract](../api/contractor-compliance.md))

## Implementation plan

This adapter presents Contractor Compliance for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Contractor Compliance API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/contractor-compliance.md), and [API module](../api/contractor-compliance.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `contractor-compliance`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/contractor-compliance.md)) |
| Capability React Native module skeleton | [`module-accounting-contractor-compliance-react-native`](https://github.com/liberusoftware/module-accounting-contractor-compliance-react-native) (`@liberusoftware/module-accounting-contractor-compliance-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Contractor records** | Progressive mobile list/detail/sheet flow for `contractor records` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Status/evidence** | Progressive mobile list/detail/sheet flow for `status/evidence` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Withholding schemes** | Progressive mobile list/detail/sheet flow for `withholding schemes` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **CIS/1099-style classifications** | Progressive mobile list/detail/sheet flow for `cis/1099-style classifications` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Deductions** | Progressive mobile list/detail/sheet flow for `deductions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Statements** | Progressive mobile list/detail/sheet flow for `statements` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Regional exports** | Progressive mobile list/detail/sheet flow for `regional exports` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ContractorQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-compliance/src/Queries/ContractorQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ExportContractorCompliance.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-compliance/src/Actions/ExportContractorCompliance.php) | `public function handle(Contractor $contractor, string $region): Contractor` |
| [IssueContractorStatement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-compliance/src/Actions/IssueContractorStatement.php) | `public function handle(Contractor $contractor, array $statement): Contractor` |
| [RecordContractorEvidence.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-compliance/src/Actions/RecordContractorEvidence.php) | `public function handle(Contractor $contractor, array $evidence): Contractor` |
| [RegisterContractor.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-compliance/src/Actions/RegisterContractor.php) | `public function handle(array $attributes): Contractor` |
| [UpdateContractorCompliance.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-compliance/src/Actions/UpdateContractorCompliance.php) | `public function handle(Contractor $contractor, array $attributes): Contractor` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Contractor.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-compliance/src/Models/Contractor.php) | `team_id`, `contractor_ref`, `legal_name`, `classification`, `status`, `withholding_scheme`, `deductions`, `evidence`, `statement`, `regional_export` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ContractorsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-compliance-api/src/Http/Controllers/ContractorsController.php) | `public function index(ContractorQuery $query): JsonResponse`<br>`public function store(Request $request, RegisterContractor $action): JsonResponse`<br>`public function evidence(Request $request, string $contractor, RecordContractorEvidence $action): JsonResponse`<br>`public function statement(Request $request, string $contractor, IssueContractorStatement $action): JsonResponse`<br>`public function export(Request $request, string $contractor, ExportContractorCompliance $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-contractor-compliance-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-contractor-compliance-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/contractor-compliance')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.contractor-compliance.read')->get('/', [ContractorsController::class, 'index']);
Route::middleware('ability:accounting.contractor-compliance.write')->group(function (): void {
Route::post('/', [ContractorsController::class, 'store']);
Route::post('/{contractor}/evidence', [ContractorsController::class, 'evidence']);
Route::post('/{contractor}/statement', [ContractorsController::class, 'statement']);
Route::post('/{contractor}/export', [ContractorsController::class, 'export']);
```
<!-- layer-implementation-plan:end -->
