# Control Panel: Accounts Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounts). Observed identity: [`liberusoftware/module-control-panel-accounts-livewire`](../../../modules/source/liberusoftware--module-control-panel-accounts-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-control-panel-accounts-livewire`  
**Matching domain module:** `control-panel-accounts`  
**Application:** Control Panel  
**Source feature:** [Accounts](../features/accounts.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Admin/reseller/customer hierarchy:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Packages:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Quotas:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Delegation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Branding:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Suspension:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-control-panel-accounts-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-control-panel-accounts::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `admin-reseller-customer-hierarchy`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `packages`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `quotas`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `delegation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `branding`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `suspension`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `control-panel-accounts` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-control-panel-laravel-filament`](https://github.com/liberusoftware/project-control-panel-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/accounts.md) · [API plan](../api/accounts.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Admin/reseller/customer hierarchy** | Expose a focused Livewire 4 component and namespaced Blade default view for `admin/reseller/customer hierarchy` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Packages** | Expose a focused Livewire 4 component and namespaced Blade default view for `packages` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Quotas** | Expose a focused Livewire 4 component and namespaced Blade default view for `quotas` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Delegation** | Expose a focused Livewire 4 component and namespaced Blade default view for `delegation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Branding** | Expose a focused Livewire 4 component and namespaced Blade default view for `branding` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Suspension** | Expose a focused Livewire 4 component and namespaced Blade default view for `suspension` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [AccountsLivewireServiceProvider.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts-livewire/src/AccountsLivewireServiceProvider.php) · [AccountFeatureInventory.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts-livewire/src/Components/AccountFeatureInventory.php) · [AccountInventory.php](https://github.com/liberusoftware/project-control-panel-laravel-filament/blob/1797f25d705f780bacddcdf228c9a1dc995c3580/modules/control-panel-accounts-livewire/src/Components/AccountInventory.php).

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
<!-- layer-implementation-plan:end -->
