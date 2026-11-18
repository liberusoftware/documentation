# Accounts Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounts). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-control-panel-accounts-flutter
**Matching core package:** module-control-panel-accounts ([implementation](../core/accounts.md))
**Matching API package:** module-control-panel-accounts-api ([contract](../api/accounts.md))

## Implementation plan

This adapter presents Accounts for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounts API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/accounts.md), and [API module](../api/accounts.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `accounts`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-control-panel-mobile-flutter`](https://github.com/liberusoftware/project-control-panel-mobile-flutter) | [`module-control-panel-accounts-flutter`](https://github.com/liberusoftware/module-control-panel-accounts-flutter) (`module_control_panel_accounts_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-control-panel-dart-mobile`](https://github.com/liberusoftware/project-control-panel-dart-mobile) | [`module-control-panel-accounts-dart-mobile`](https://github.com/liberusoftware/module-control-panel-accounts-dart-mobile) (`module_control_panel_accounts_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-control-panel-dart-desktop`](https://github.com/liberusoftware/project-control-panel-dart-desktop) | [`module-control-panel-accounts-dart-desktop`](https://github.com/liberusoftware/module-control-panel-accounts-dart-desktop) (`module_control_panel_accounts_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api) | [API plan](../api/accounts.md) · [Core plan](../core/accounts.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Admin/reseller/customer hierarchy** | Adaptive mobile cards/sheets for `admin/reseller/customer hierarchy` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `admin/reseller/customer hierarchy` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Packages** | Adaptive mobile cards/sheets for `packages` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `packages` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Quotas** | Adaptive mobile cards/sheets for `quotas` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `quotas` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Delegation** | Adaptive mobile cards/sheets for `delegation` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `delegation` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Branding** | Adaptive mobile cards/sheets for `branding` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `branding` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Suspension** | Adaptive mobile cards/sheets for `suspension` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `suspension` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-control-panel-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

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
