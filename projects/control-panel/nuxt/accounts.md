# Control Panel: Accounts Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounts). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-control-panel-accounts-nuxt`
**Matching domain module:** `control-panel-accounts`
**Application:** Control Panel
**Source feature:** [Accounts](../features/accounts.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounts.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `control-panel-accounts` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Admin/reseller/customer hierarchy:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Packages:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Quotas:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Delegation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Branding:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Suspension:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-control-panel-accounts-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `admin-reseller-customer-hierarchy`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `packages`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `quotas`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `delegation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `branding`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `suspension`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

## 4. API contract and Nuxt consumption

- Consume only the matching API module linked above; use its documented OpenAPI schemas, routes, authentication, permissions, team context, pagination, errors, and operation semantics.
- Keep a typed API client and module-local composables under the package boundary; use `useFetch` or `useAsyncData` for SSR-safe reads and `$fetch` for event-driven mutations.
- Forward Sanctum cookies or approved authorization headers through a controlled client boundary; never persist long-lived tokens in browser storage or expose secrets in SSR payloads.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, and minimal-host installation tests.
- Test observable browser and SSR behavior with Vitest, Vue Test Utils, Playwright, TypeScript, and the supported Nuxt 4/Vue 3 stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `control-panel-accounts` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-control-panel-nuxt-vue`](https://github.com/liberusoftware/project-control-panel-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-control-panel-laravel-api`](https://github.com/liberusoftware/project-control-panel-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounts.md)) |
| Capability Nuxt module skeleton | [`module-control-panel-accounts-nuxt`](https://github.com/liberusoftware/module-control-panel-accounts-nuxt) (`@liberusoftware/module-control-panel-accounts-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Admin/reseller/customer hierarchy** | Expose composable and Vue 3 component for `admin/reseller/customer hierarchy` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounts.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Packages** | Expose composable and Vue 3 component for `packages` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounts.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Quotas** | Expose composable and Vue 3 component for `quotas` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounts.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Delegation** | Expose composable and Vue 3 component for `delegation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounts.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Branding** | Expose composable and Vue 3 component for `branding` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounts.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |
| **Suspension** | Expose composable and Vue 3 component for `suspension` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounts.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-control-panel-laravel-api`. |

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
