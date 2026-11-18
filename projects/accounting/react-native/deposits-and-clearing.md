# Deposits And Clearing React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#deposits-and-clearing). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-deposits-and-clearing-react-native
**Matching core package:** module-accounting-deposits-and-clearing ([implementation](../core/deposits-and-clearing.md))
**Matching API package:** module-accounting-deposits-and-clearing-api ([contract](../api/deposits-and-clearing.md))

## Implementation plan

This adapter presents Deposits And Clearing for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Deposits And Clearing API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/deposits-and-clearing.md), and [API module](../api/deposits-and-clearing.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `deposits-and-clearing`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/deposits-and-clearing.md)) |
| Capability React Native module skeleton | [`module-accounting-deposits-and-clearing-react-native`](https://github.com/liberusoftware/module-accounting-deposits-and-clearing-react-native) (`@liberusoftware/module-accounting-deposits-and-clearing-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Undeposited funds** | Progressive mobile list/detail/sheet flow for `undeposited funds` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Grouped deposits** | Progressive mobile list/detail/sheet flow for `grouped deposits` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Payment-provider clearing** | Progressive mobile list/detail/sheet flow for `payment-provider clearing` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Fees** | Progressive mobile list/detail/sheet flow for `fees` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Payouts** | Progressive mobile list/detail/sheet flow for `payouts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Timing differences** | Progressive mobile list/detail/sheet flow for `timing differences` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Reconciliation** | Progressive mobile list/detail/sheet flow for `reconciliation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ClearingQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Queries/ClearingQuery.php) | `public function undeposited(int $teamId): Collection`<br>`public function deposits(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateGroupedDeposit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Actions/CreateGroupedDeposit.php) | `public function handle(array $attributes, array $fundIds): ClearingDeposit` |
| [ReconcileDeposit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Actions/ReconcileDeposit.php) | `public function handle(ClearingDeposit $deposit, float $payoutAmount, float $feeAmount = 0): ClearingDeposit` |
| [RecordUndepositedFund.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Actions/RecordUndepositedFund.php) | `public function handle(array $attributes): ClearingFund` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ClearingDeposit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Models/ClearingDeposit.php) | `team_id`, `deposit_ref`, `provider`, `account_ref`, `currency`, `gross_amount`, `fee_amount`, `payout_amount`, `deposit_date`, `status`, `metadata` |
| [ClearingFund.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing/src/Models/ClearingFund.php) | `team_id`, `deposit_id`, `source_type`, `source_id`, `amount`, `currency`, `received_on`, `status`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ClearingController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing-api/src/Http/Controllers/ClearingController.php) | `public function funds(ClearingQuery $query): JsonResponse`<br>`public function deposits(ClearingQuery $query): JsonResponse`<br>`public function recordFund(Request $request, RecordUndepositedFund $action): JsonResponse`<br>`public function createDeposit(Request $request, CreateGroupedDeposit $action): JsonResponse`<br>`public function reconcile(Request $request, string $deposit, ReconcileDeposit $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-deposits-and-clearing-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-deposits-and-clearing-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/deposits-and-clearing')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.deposits-and-clearing.read')->group(function (): void {
Route::get('/funds', [ClearingController::class, 'funds']);
Route::get('/deposits', [ClearingController::class, 'deposits']);
Route::middleware('ability:accounting.deposits-and-clearing.write')->group(function (): void {
Route::post('/funds', [ClearingController::class, 'recordFund']);
Route::post('/deposits', [ClearingController::class, 'createDeposit']);
Route::post('/deposits/{deposit}/reconcile', [ClearingController::class, 'reconcile']);
```
<!-- layer-implementation-plan:end -->
