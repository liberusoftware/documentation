# Transfers React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#transfers). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-transfers-react-native
**Matching core package:** module-accounting-transfers ([implementation](../core/transfers.md))
**Matching API package:** module-accounting-transfers-api ([contract](../api/transfers.md))

## Implementation plan

This adapter presents Transfers for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Transfers API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/transfers.md), and [API module](../api/transfers.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `transfers`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/transfers.md)) |
| Capability React Native module skeleton | [`module-accounting-transfers-react-native`](https://github.com/liberusoftware/module-accounting-transfers-react-native) (`@liberusoftware/module-accounting-transfers-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Inter-account/entity transfers** | Progressive mobile list/detail/sheet flow for `inter-account/entity transfers` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Currency conversion** | Progressive mobile list/detail/sheet flow for `currency conversion` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Fees** | Progressive mobile list/detail/sheet flow for `fees` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **In-transit state** | Progressive mobile list/detail/sheet flow for `in-transit state` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Paired posting** | Progressive mobile list/detail/sheet flow for `paired posting` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Reconciliation** | Progressive mobile list/detail/sheet flow for `reconciliation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CompleteTransfer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-transfers/src/Actions/CompleteTransfer.php) | `public function handle(Transfer $transfer): Transfer` |
| [CreateTransfer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-transfers/src/Actions/CreateTransfer.php) | `public function handle(array $attributes): Transfer` |
| [ReconcileTransfer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-transfers/src/Actions/ReconcileTransfer.php) | `public function handle(Transfer $transfer, array $attributes): TransferReconciliation` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Transfer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-transfers/src/Models/Transfer.php) | `team_id`, `source_account_ref`, `destination_account_ref`, `source_currency`, `destination_currency`, `source_amount`, `destination_amount`, `exchange_rate`, `fee_amount`, `status`, `reference`, `metadata` |
| [TransferReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-transfers/src/Models/TransferReconciliation.php) | `team_id`, `transfer_id`, `external_ref`, `amount`, `reconciled_on`, `status`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [TransfersController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-transfers-api/src/Http/Controllers/TransfersController.php) | `public function index(Request $request): mixed`<br>`public function store(Request $request, CreateTransfer $action): mixed`<br>`public function complete(Request $request, string $transfer, CompleteTransfer $action): mixed`<br>`public function reconcile(Request $request, string $transfer, ReconcileTransfer $action): mixed` |

**Observed route declarations:**

[modules/accounting-transfers-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-transfers-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/transfers')->middleware(['auth:sanctum'])->group(function (): void {
Route::get('/', [TransfersController::class, 'index'])->middleware('ability:accounting.transfers.read');
Route::post('/', [TransfersController::class, 'store'])->middleware('ability:accounting.transfers.write');
Route::post('/{transfer}/complete', [TransfersController::class, 'complete'])->middleware('ability:accounting.transfers.write');
Route::post('/{transfer}/reconcile', [TransfersController::class, 'reconcile'])->middleware('ability:accounting.transfers.write');
```
<!-- layer-implementation-plan:end -->
