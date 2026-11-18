# Control Panel: Control Panel Accounts React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#control-panel-accounts). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-control-panel-control-panel-accounts-react-inertia`
**Matching domain module:** `control-panel-accounts`
**Application:** Control Panel
**Source feature:** [Control Panel Accounts](../features/control-panel-accounts.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/control-panel-accounts.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Admin/reseller/customer hierarchy:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Packages:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Quotas:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Delegation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Branding:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Suspension:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-control-panel-control-panel-accounts-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `admin-reseller-customer-hierarchy`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `packages`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `quotas`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `delegation`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `branding`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `suspension`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

## 4. API contract and Inertia consumption

<!-- inertia-transport:start -->
### Inertia transport boundary

Use Laravel-owned Inertia page/command routes for visits and forms. The controller can invoke the module's public application actions in the same host or use a deliberate API adapter, then return an Inertia page/redirect response. A bare REST JSON resource response is not an Inertia page. Keep authoritative domain authorization and validation in the owning boundary for either path.

Independent API consumers and Next.js use their reviewed HTTP/session integration. Share DTOs and framework-independent UI primitives; keep Inertia page props, visits, form errors and redirects in the Inertia wrapper. Do not introduce loopback HTTP solely to reuse a public action inside the same Laravel host.

See the [Inertia standard](../../../standards/INERTIA.md), [request lifecycle](https://inertiajs.com/docs/v3/core-concepts/how-it-works) and [redirect behavior](https://inertiajs.com/docs/v3/the-basics/redirects).
<!-- inertia-transport:end -->

- Reuse the matching public application/API contracts. For HTTP consumption, use its documented schemas, routes, authentication, permissions, tenant context, errors and operation semantics; Inertia visits still require an Inertia response.
- Keep a typed module-local API client and hooks boundary; use Inertia visits for page transitions and `useForm`/`router` for mutations, preserving server validation and redirect semantics.
- Forward Sanctum cookies or approved authorization headers through a controlled first-party boundary; never persist long-lived tokens in browser storage or expose secrets in page props.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, SSR hydration where enabled, and minimal-host installation tests.
- Test observable behavior with TypeScript, ESLint, Vitest, React Testing Library, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `control-panel-accounts` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-control-panel-laravel-inertia-react`](https://github.com/liberusoftware/project-control-panel-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-control-panel-accounts-react-inertia`](https://github.com/liberusoftware/module-control-panel-accounts-react-inertia) (`@liberusoftware/module-control-panel-accounts-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/control-panel-accounts.md) · [Core plan](../core/control-panel-accounts.md) · [API plan](../api/control-panel-accounts.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Admin/reseller/customer hierarchy** | Render `admin/reseller/customer hierarchy` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Packages** | Render `packages` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Quotas** | Render `quotas` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Delegation** | Render `delegation` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Branding** | Render `branding` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Suspension** | Render `suspension` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

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
