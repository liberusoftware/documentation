# Accounting Chart Of Accounts React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-chart-of-accounts). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-chart-of-accounts-react-native
**Matching core package:** module-accounting-accounting-chart-of-accounts ([implementation](../core/accounting-chart-of-accounts.md))
**Matching API package:** module-accounting-accounting-chart-of-accounts-api ([contract](../api/accounting-chart-of-accounts.md))

## Implementation plan

This adapter presents Accounting Chart Of Accounts for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Chart Of Accounts API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/accounting-chart-of-accounts.md), and [API module](../api/accounting-chart-of-accounts.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `accounting-chart-of-accounts`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-chart-of-accounts.md)) |
| Capability React Native module skeleton | [`module-accounting-chart-of-accounts-react-native`](https://github.com/liberusoftware/module-accounting-chart-of-accounts-react-native) (`@liberusoftware/module-accounting-chart-of-accounts-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Account types** | Progressive mobile list/detail/sheet flow for `account types` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Codes** | Progressive mobile list/detail/sheet flow for `codes` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Hierarchies** | Progressive mobile list/detail/sheet flow for `hierarchies` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Control accounts** | Progressive mobile list/detail/sheet flow for `control accounts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Normal balances** | Progressive mobile list/detail/sheet flow for `normal balances` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Templates** | Progressive mobile list/detail/sheet flow for `templates` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Restrictions** | Progressive mobile list/detail/sheet flow for `restrictions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Localization** | Progressive mobile list/detail/sheet flow for `localization` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Lifecycle** | Progressive mobile list/detail/sheet flow for `lifecycle` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ArchiveAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-chart-of-accounts/src/Actions/ArchiveAccount.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(Account $account): Account` |
| [SaveAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-chart-of-accounts/src/Actions/SaveAccount.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(array $attributes, ?Account $account = null): Account` |
| [AccountPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-chart-of-accounts-api/src/Policies/AccountPolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function view(?Authenticatable $user, Account $account): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function update(?Authenticatable $user, Account $account): bool`<br>`public function delete(?Authenticatable $user, Account $account): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Account.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-chart-of-accounts/src/Models/Account.php) | `legal_entity_id`, `code`, `name`, `description`, `type`, `normal_balance`, `parent_id`, `is_control_account`, `allow_manual_entry`, `is_active`, `locale`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [AccountController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-chart-of-accounts-api/src/Http/Controllers/AccountController.php) | `public function index(Request $request): JsonResponse`<br>`public function tree(Request $request): JsonResponse`<br>`public function show(string $account): AccountResource`<br>`public function store(StoreAccountRequest $request, SaveAccount $save): JsonResponse`<br>`public function update(UpdateAccountRequest $request, string $account, SaveAccount $save): AccountResource`<br>`public function destroy(string $account, ArchiveAccount $archive): Response` |

**Observed route declarations:**

[modules/accounting-chart-of-accounts-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-chart-of-accounts-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/chart-of-accounts')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::get('accounts', [AccountController::class, 'index'])->middleware('ability:accounting.chart.read');
Route::get('accounts/tree', [AccountController::class, 'tree'])->middleware('ability:accounting.chart.read');
Route::get('accounts/{account}', [AccountController::class, 'show'])->middleware('ability:accounting.chart.read');
Route::post('accounts', [AccountController::class, 'store'])->middleware('ability:accounting.chart.write');
Route::delete('accounts/{account}', [AccountController::class, 'destroy'])->middleware('ability:accounting.chart.write');
```
<!-- layer-implementation-plan:end -->
