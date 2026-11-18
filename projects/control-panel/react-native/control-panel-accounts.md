# Control Panel Accounts React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#control-panel-accounts). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-control-panel-control-panel-accounts-react-native
**Matching core package:** module-control-panel-control-panel-accounts ([implementation](../core/control-panel-accounts.md))
**Matching API package:** module-control-panel-control-panel-accounts-api ([contract](../api/control-panel-accounts.md))

## Implementation plan

This adapter presents Control Panel Accounts for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Control Panel Accounts API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/control-panel-accounts.md), and [API module](../api/control-panel-accounts.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `control-panel-accounts`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-control-panel-mobile-react`](https://github.com/liberusoftware/project-control-panel-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/control-panel-accounts.md)) |
| Capability React Native module skeleton | [`module-control-panel-accounts-react-native`](https://github.com/liberusoftware/module-control-panel-accounts-react-native) (`@liberusoftware/module-control-panel-accounts-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Admin/reseller/customer hierarchy** | Progressive mobile list/detail/sheet flow for `admin/reseller/customer hierarchy` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Packages** | Progressive mobile list/detail/sheet flow for `packages` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Quotas** | Progressive mobile list/detail/sheet flow for `quotas` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Delegation** | Progressive mobile list/detail/sheet flow for `delegation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Branding** | Progressive mobile list/detail/sheet flow for `branding` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Suspension** | Progressive mobile list/detail/sheet flow for `suspension` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-control-panel-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListAccounts.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts/src/Queries/ListAccounts.php) | `public function execute(?string $teamId, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ActivateAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts/src/Actions/ActivateAccount.php) | `public function execute(Account $account): Account` |
| [ArchiveAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts/src/Actions/ArchiveAccount.php) | `public function execute(Account $account): Account` |
| [AssignHostingPackage.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts/src/Actions/AssignHostingPackage.php) | `public function execute(Account $account, HostingPackage $package, array $attributes = []): HostingPackageAssignment` |
| [CreateAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts/src/Actions/CreateAccount.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(array $attributes): Account` |
| [CreateHostingPackage.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts/src/Actions/CreateHostingPackage.php) | `public function execute(array $attributes): HostingPackage` |
| [DelegateAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts/src/Actions/DelegateAccount.php) | `public function execute(Account $account, array $attributes): AccountDelegation` |
| [RemoveHostingPackageAssignment.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts/src/Actions/RemoveHostingPackageAssignment.php) | `public function execute(HostingPackageAssignment $assignment): void` |
| [RevokeDelegation.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts/src/Actions/RevokeDelegation.php) | `public function execute(AccountDelegation $delegation): AccountDelegation` |
| [SuspendAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts/src/Actions/SuspendAccount.php) | `public function __construct(private Dispatcher $events)`<br>`public function execute(Account $account, string $reason): Account` |
| [UpdateAccount.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts/src/Actions/UpdateAccount.php) | `public function execute(Account $account, array $attributes): Account` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Account.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts/src/Models/Account.php) | `team_id`, `parent_id`, `owner_id`, `type`, `status`, `name`, `brand`, `quota_overrides`, `suspended_reason`, `suspended_at` |
| [AccountDelegation.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts/src/Models/AccountDelegation.php) | `team_id`, `account_id`, `delegate_id`, `permissions`, `expires_at`, `active` |
| [HostingPackage.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts/src/Models/HostingPackage.php) | `team_id`, `name`, `limits`, `features`, `active` |
| [HostingPackageAssignment.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts/src/Models/HostingPackageAssignment.php) | `team_id`, `account_id`, `hosting_package_id`, `start_date`, `end_date`, `active` |

| Observed API controller | Handler signatures |
| --- | --- |
| [AccountController.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts-api/src/Http/Controllers/AccountController.php) | `public function index(Request $request, ListAccounts $list): JsonResponse`<br>`public function suspend(Request $request, Account $account, SuspendAccount $suspend): JsonResponse`<br>`public function activate(Request $request, Account $account, ActivateAccount $activate): JsonResponse`<br>`public function archive(Request $request, Account $account, ArchiveAccount $archive): JsonResponse`<br>`public function package(Request $request, CreateHostingPackage $create): JsonResponse`<br>`public function packages(Request $request): JsonResponse`<br>`public function assignments(Request $request, Account $account): JsonResponse`<br>`public function assignPackage(Request $request, Account $account, AssignHostingPackage $assign): JsonResponse`<br>`public function updateAssignment(Request $request, string $assignment, UpdateHostingPackageAssignment $update): JsonResponse`<br>`public function removeAssignment(Request $request, string $assignment, RemoveHostingPackageAssignment $remove): JsonResponse`<br>`public function updatePackage(Request $request, string $package, UpdateHostingPackage $update): JsonResponse`<br>`public function delegate(Request $request, Account $account, DelegateAccount $delegate): JsonResponse`<br>`public function delegations(Request $request, Account $account): JsonResponse`<br>`public function revokeDelegation(Request $request, string $delegation, RevokeDelegation $revoke): JsonResponse`<br>`public function updateDelegation(Request $request, string $delegation, UpdateDelegation $update): JsonResponse`<br>`public function branding(Request $request, Account $account, UpdateBranding $update): JsonResponse`<br>`public function quotaCheck(Request $request, Account $account, QuotaGuard $quotas): JsonResponse`<br>`public function show(Request $request, string $id): JsonResponse`<br>`public function update(Request $request, Account $account, UpdateAccount $update): JsonResponse`<br>`public function store(Request $request, CreateAccount $create): JsonResponse` |

**Observed route declarations:**

[modules/control-panel-accounts-api/routes/api.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts-api/routes/api.php)

```php
Route::prefix('api/v1/control-panel/accounts')
Route::get('/', [AccountController::class, 'index'])->name('control-panel.accounts.index');
Route::post('/', [AccountController::class, 'store'])->name('control-panel.accounts.store');
Route::post('{account}/suspend', [AccountController::class, 'suspend'])->name('control-panel.accounts.suspend');
Route::post('{account}/activate', [AccountController::class, 'activate'])->name('control-panel.accounts.activate');
Route::post('{account}/archive', [AccountController::class, 'archive'])->name('control-panel.accounts.archive');
Route::post('{account}/delegations', [AccountController::class, 'delegate'])->name('control-panel.accounts.delegate');
Route::patch('{account}/branding', [AccountController::class, 'branding'])->name('control-panel.accounts.branding');
Route::post('{account}/quota-check', [AccountController::class, 'quotaCheck'])->name('control-panel.accounts.quota-check');
Route::post('packages', [AccountController::class, 'package'])->name('control-panel.accounts.packages.store');
Route::get('packages', [AccountController::class, 'packages'])->name('control-panel.accounts.packages.index');
Route::patch('packages/{package}', [AccountController::class, 'updatePackage'])->name('control-panel.accounts.packages.update');
Route::get('{account}/hosting-packages', [AccountController::class, 'assignments'])->name('control-panel.accounts.hosting-packages.index');
Route::post('{account}/hosting-packages', [AccountController::class, 'assignPackage'])->name('control-panel.accounts.hosting-packages.store');
Route::patch('hosting-package-assignments/{assignment}', [AccountController::class, 'updateAssignment'])->name('control-panel.accounts.hosting-packages.update');
Route::delete('hosting-package-assignments/{assignment}', [AccountController::class, 'removeAssignment'])->name('control-panel.accounts.hosting-packages.destroy');
Route::get('{account}/delegations', [AccountController::class, 'delegations'])->name('control-panel.accounts.delegations.index');
Route::post('delegations/{delegation}/revoke', [AccountController::class, 'revokeDelegation'])->name('control-panel.accounts.delegations.revoke');
Route::patch('delegations/{delegation}', [AccountController::class, 'updateDelegation'])->name('control-panel.accounts.delegations.update');
Route::patch('{account}', [AccountController::class, 'update'])->name('control-panel.accounts.update');
Route::get('{account}', [AccountController::class, 'show'])->name('control-panel.accounts.show');
```
<!-- layer-implementation-plan:end -->
