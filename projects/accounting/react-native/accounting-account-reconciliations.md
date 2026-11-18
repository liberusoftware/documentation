# Accounting Account Reconciliations React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-account-reconciliations). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-account-reconciliations-react-native
**Matching core package:** module-accounting-accounting-account-reconciliations ([implementation](../core/accounting-account-reconciliations.md))
**Matching API package:** module-accounting-accounting-account-reconciliations-api ([contract](../api/accounting-account-reconciliations.md))

## Implementation plan

This adapter presents Accounting Account Reconciliations for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Account Reconciliations API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/accounting-account-reconciliations.md), and [API module](../api/accounting-account-reconciliations.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `accounting-account-reconciliations`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-account-reconciliations.md)) |
| Capability React Native module skeleton | [`module-accounting-account-reconciliations-react-native`](https://github.com/liberusoftware/module-accounting-account-reconciliations-react-native) (`@liberusoftware/module-accounting-account-reconciliations-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **GL account templates** | Progressive mobile list/detail/sheet flow for `gl account templates` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Source balances** | Progressive mobile list/detail/sheet flow for `source balances` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Supporting items** | Progressive mobile list/detail/sheet flow for `supporting items` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Preparer/reviewer** | Progressive mobile list/detail/sheet flow for `preparer/reviewer` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Aging** | Progressive mobile list/detail/sheet flow for `aging` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Certification** | Progressive mobile list/detail/sheet flow for `certification` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Carry-forward** | Progressive mobile list/detail/sheet flow for `carry-forward` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [AccountReconciliationQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/src/Queries/AccountReconciliationQuery.php) | `public function paginate(?int $teamId, ?string $status = null, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CarryForwardAccountReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/src/Actions/CarryForwardAccountReconciliation.php) | `public function handle(AccountReconciliation $reconciliation, array $carryForward): AccountReconciliation` |
| [CertifyAccountReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/src/Actions/CertifyAccountReconciliation.php) | `public function handle(AccountReconciliation $reconciliation, array $certification): AccountReconciliation` |
| [CreateAccountReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/src/Actions/CreateAccountReconciliation.php) | `public function handle(array $attributes): AccountReconciliation` |
| [PrepareAccountReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/src/Actions/PrepareAccountReconciliation.php) | `public function handle(AccountReconciliation $reconciliation, array $preparer, array $sourceBalance, array $supportingItems = []): AccountReconciliation` |
| [ReviewAccountReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/src/Actions/ReviewAccountReconciliation.php) | `public function handle(AccountReconciliation $reconciliation, array $reviewer): AccountReconciliation` |
| [AccountReconciliationsPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations-api/src/Policies/AccountReconciliationsPolicy.php) | `public function viewAny(?object $user): bool`<br>`public function view(?object $user, object $record): bool`<br>`public function create(?object $user): bool`<br>`public function update(?object $user, object $record): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AccountReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations/src/Models/AccountReconciliation.php) | `team_id`, `book_id`, `account_id`, `period_start`, `period_end`, `status`, `template`, `source_balance`, `supporting_items`, `preparer`, `reviewer`, `aging`, `certification`, `carry_forward` |
| [Account.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations-api/src/Models/Account.php) | `account_number`, `account_name`, `account_type`, `normal_balance`, `balance`, `opening_balance`, `description`, `currency_id`, `parent_id`, `industry_type`, `is_active`, `allow_manual_entry`, `user_id`, `team_id`, `qbo_id`, `qbo_sync_token`, `xero_id`, `sage_id` |

| Observed API controller | Handler signatures |
| --- | --- |
| [AccountReconciliationController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations-api/src/Http/Controllers/AccountReconciliationController.php) | `public function index(Request $request, AccountReconciliationQuery $query): mixed`<br>`public function show(AccountReconciliation $reconciliation): AccountReconciliationResource`<br>`public function store(Request $request, CreateAccountReconciliation $action): AccountReconciliationResource`<br>`public function prepare(Request $request, AccountReconciliation $reconciliation, PrepareAccountReconciliation $action): AccountReconciliationResource`<br>`public function review(Request $request, AccountReconciliation $reconciliation, ReviewAccountReconciliation $action): AccountReconciliationResource`<br>`public function certify(Request $request, AccountReconciliation $reconciliation, CertifyAccountReconciliation $action): AccountReconciliationResource`<br>`public function carryForward(Request $request, AccountReconciliation $reconciliation, CarryForwardAccountReconciliation $action): AccountReconciliationResource` |

**Observed route declarations:**

[modules/accounting-account-reconciliations-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/account-reconciliations')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('/', [AccountReconciliationController::class, 'index'])->middleware('ability:accounting.account-reconciliations.read');
Route::post('/', [AccountReconciliationController::class, 'store'])->middleware('ability:accounting.account-reconciliations.write');
Route::post('/{reconciliation}/prepare', [AccountReconciliationController::class, 'prepare'])->middleware('ability:accounting.account-reconciliations.write');
Route::post('/{reconciliation}/review', [AccountReconciliationController::class, 'review'])->middleware('ability:accounting.account-reconciliations.write');
Route::post('/{reconciliation}/certify', [AccountReconciliationController::class, 'certify'])->middleware('ability:accounting.account-reconciliations.write');
Route::post('/{reconciliation}/carry-forward', [AccountReconciliationController::class, 'carryForward'])->middleware('ability:accounting.account-reconciliations.write');
Route::get('/{reconciliation}', [AccountReconciliationController::class, 'show'])->middleware('ability:accounting.account-reconciliations.read');
```
<!-- layer-implementation-plan:end -->
