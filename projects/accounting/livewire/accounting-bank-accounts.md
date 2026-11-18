# Accounting: Accounting Bank Accounts Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-bank-accounts). Observed identity: [`liberusoftware/module-accounting-bank-accounts-livewire`](../../../modules/source/liberusoftware--module-accounting-bank-accounts-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-accounting-bank-accounts-livewire`  
**Matching domain module:** `accounting-bank-accounts`  
**Application:** Accounting  
**Source feature:** [Accounting Bank Accounts](../features/accounting-bank-accounts.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Bank/current/savings/credit/loan/cash accounts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Ownership:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Currency:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Opening data:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Feeds:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Lifecycle:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Restricted details:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-accounting-bank-accounts-livewire` component namespace and service provider; use explicit aliases such as `<livewire:accountingAccountingBankAccounts::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `bank-current-savings-credit-loan-cash-accounts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `ownership`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `currency`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `opening-data`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `feeds`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `lifecycle`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `restricted-details`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-bank-accounts` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/accounting-bank-accounts.md) · [API plan](../api/accounting-bank-accounts.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Bank/current/savings/credit/loan/cash accounts** | Expose a focused Livewire 4 component and namespaced Blade default view for `bank/current/savings/credit/loan/cash accounts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Ownership** | Expose a focused Livewire 4 component and namespaced Blade default view for `ownership` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Currency** | Expose a focused Livewire 4 component and namespaced Blade default view for `currency` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Opening data** | Expose a focused Livewire 4 component and namespaced Blade default view for `opening data` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Feeds** | Expose a focused Livewire 4 component and namespaced Blade default view for `feeds` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Lifecycle** | Expose a focused Livewire 4 component and namespaced Blade default view for `lifecycle` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Restricted details** | Expose a focused Livewire 4 component and namespaced Blade default view for `restricted details` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [Accounts.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-accounts-livewire/src/Livewire/Accounts.php) · [BankAccountsLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-accounts-livewire/src/BankAccountsLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [BankAccountBalanceQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-accounts/src/Queries/BankAccountBalanceQuery.php) | `public function handle(?int $legalEntityId = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateBankAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-accounts/src/Actions/CreateBankAccount.php) | `public function handle(array $attributes): BankAccount` |
| [SetBankAccountStatus.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-accounts/src/Actions/SetBankAccountStatus.php) | `public function handle(BankAccount $account, BankAccountStatus $status): BankAccount` |
| [UpdateBankAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-accounts/src/Actions/UpdateBankAccount.php) | `public function handle(BankAccount $account, array $attributes): BankAccount` |
| [BankAccountsPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-accounts-api/src/Policies/BankAccountsPolicy.php) | `public function viewAny(?object $user = null): bool`<br>`public function view(?object $user, object $account): bool`<br>`public function create(?object $user = null): bool`<br>`public function update(?object $user, object $account): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [BankAccount.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-accounts/src/Models/BankAccount.php) | `legal_entity_id`, `owner_type`, `owner_id`, `name`, `institution_name`, `account_type`, `currency`, `opening_balance`, `opening_date`, `current_balance`, `account_number`, `routing_number`, `feed_reference`, `status`, `closed_at`, `metadata` |
<!-- layer-implementation-plan:end -->
