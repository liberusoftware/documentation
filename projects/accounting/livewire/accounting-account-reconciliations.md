# Accounting: Accounting Account Reconciliations Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-account-reconciliations). Observed identity: [`liberusoftware/module-accounting-account-reconciliations-livewire`](../../../modules/source/liberusoftware--module-accounting-account-reconciliations-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-accounting-account-reconciliations-livewire`  
**Matching domain module:** `accounting-account-reconciliations`  
**Application:** Accounting  
**Source feature:** [Accounting Account Reconciliations](../features/accounting-account-reconciliations.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **GL account templates:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Source balances:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Supporting items:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Preparer/reviewer:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Aging:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Certification:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Carry-forward:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-accounting-account-reconciliations-livewire` component namespace and service provider; use explicit aliases such as `<livewire:accountingAccountingAccountReconciliations::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `gl-account-templates`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `source-balances`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `supporting-items`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `preparer-reviewer`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `aging`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `certification`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `carry-forward`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-account-reconciliations` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/accounting-account-reconciliations.md) · [API plan](../api/accounting-account-reconciliations.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **GL account templates** | Expose a focused Livewire 4 component and namespaced Blade default view for `gl account templates` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Source balances** | Expose a focused Livewire 4 component and namespaced Blade default view for `source balances` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Supporting items** | Expose a focused Livewire 4 component and namespaced Blade default view for `supporting items` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Preparer/reviewer** | Expose a focused Livewire 4 component and namespaced Blade default view for `preparer/reviewer` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Aging** | Expose a focused Livewire 4 component and namespaced Blade default view for `aging` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Certification** | Expose a focused Livewire 4 component and namespaced Blade default view for `certification` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Carry-forward** | Expose a focused Livewire 4 component and namespaced Blade default view for `carry-forward` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [Reconciliations.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations-livewire/src/Livewire/Reconciliations.php) · [AccountReconciliationsLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-account-reconciliations-livewire/src/AccountReconciliationsLivewireServiceProvider.php).

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
<!-- layer-implementation-plan:end -->
