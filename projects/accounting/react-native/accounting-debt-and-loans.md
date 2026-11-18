# Accounting Debt And Loans React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-debt-and-loans). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-debt-and-loans-react-native
**Matching core package:** module-accounting-accounting-debt-and-loans ([implementation](../core/accounting-debt-and-loans.md))
**Matching API package:** module-accounting-accounting-debt-and-loans-api ([contract](../api/accounting-debt-and-loans.md))

## Implementation plan

This adapter presents Accounting Debt And Loans for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Debt And Loans API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/accounting-debt-and-loans.md), and [API module](../api/accounting-debt-and-loans.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `accounting-debt-and-loans`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-debt-and-loans.md)) |
| Capability React Native module skeleton | [`module-accounting-debt-and-loans-react-native`](https://github.com/liberusoftware/module-accounting-debt-and-loans-react-native) (`@liberusoftware/module-accounting-debt-and-loans-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Facilities** | Progressive mobile list/detail/sheet flow for `facilities` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Drawdowns** | Progressive mobile list/detail/sheet flow for `drawdowns` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Repayments** | Progressive mobile list/detail/sheet flow for `repayments` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Interest/fees** | Progressive mobile list/detail/sheet flow for `interest/fees` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Schedules** | Progressive mobile list/detail/sheet flow for `schedules` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Covenants** | Progressive mobile list/detail/sheet flow for `covenants` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Current/non-current split** | Progressive mobile list/detail/sheet flow for `current/non-current split` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Reconciliation** | Progressive mobile list/detail/sheet flow for `reconciliation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [DebtQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Queries/DebtQuery.php) | `public function facilities(int $teamId): Collection`<br>`public function position(int $teamId): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateDebtFacility.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Actions/CreateDebtFacility.php) | `public function handle(array $attributes): DebtFacility` |
| [ReconcileDebtMovement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Actions/ReconcileDebtMovement.php) | `public function handle(DebtMovement $movement, string $journalReference): DebtMovement` |
| [RecordDebtMovement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Actions/RecordDebtMovement.php) | `public function handle(DebtFacility $facility, string\|DebtMovementKind $kind, array $attributes): DebtMovement` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DebtCovenant.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Models/DebtCovenant.php) | `facility_id`, `team_id`, `covenant_ref`, `metric`, `threshold`, `operator`, `last_value`, `status`, `metadata` |
| [DebtFacility.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Models/DebtFacility.php) | `team_id`, `facility_ref`, `lender_ref`, `currency`, `limit_amount`, `drawn_amount`, `interest_rate`, `start_date`, `maturity_date`, `status`, `metadata` |
| [DebtMovement.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans/src/Models/DebtMovement.php) | `facility_id`, `team_id`, `kind`, `principal_amount`, `interest_amount`, `fee_amount`, `movement_date`, `due_date`, `status`, `journal_ref`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [DebtAndLoansController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans-api/src/Http/Controllers/DebtAndLoansController.php) | `public function index(Request $request): JsonResponse`<br>`public function position(DebtQuery $query): JsonResponse`<br>`public function store(Request $request, CreateDebtFacility $action): JsonResponse`<br>`public function movement(Request $request, string $facility, RecordDebtMovement $action): JsonResponse`<br>`public function reconcile(Request $request, string $movement, ReconcileDebtMovement $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-debt-and-loans-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-debt-and-loans-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/debt-and-loans')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.debt-and-loans.read')->group(function (): void {
Route::get('/facilities', [DebtAndLoansController::class, 'index']);
Route::get('/position', [DebtAndLoansController::class, 'position']);
Route::middleware('ability:accounting.debt-and-loans.write')->group(function (): void {
Route::post('/facilities', [DebtAndLoansController::class, 'store']);
Route::post('/facilities/{facility}/movements', [DebtAndLoansController::class, 'movement']);
Route::post('/movements/{movement}/reconcile', [DebtAndLoansController::class, 'reconcile']);
```
<!-- layer-implementation-plan:end -->
