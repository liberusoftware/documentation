# Accounting: Bank Reconciliation Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#bank-reconciliation). Observed identity: [`liberusoftware/module-accounting-bank-reconciliation-livewire`](../../../modules/source/liberusoftware--module-accounting-bank-reconciliation-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-bank-reconciliation-livewire`  
**Matching domain module:** `accounting-bank-reconciliation`  
**Application:** Accounting  
**Source feature:** [Bank Reconciliation](../features/bank-reconciliation.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Suggested/exact matches:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Transfers:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Grouped receipts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Fees/interest:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Adjustments:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Statement balance:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Exceptions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Sign-off:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-bank-reconciliation-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-accounting-bank-reconciliation::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `suggested-exact-matches`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `transfers`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `grouped-receipts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `fees-interest`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `adjustments`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `statement-balance`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `exceptions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `sign-off`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-bank-reconciliation` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/bank-reconciliation.md) · [API plan](../api/bank-reconciliation.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Suggested/exact matches** | Expose a focused Livewire 4 component and namespaced Blade default view for `suggested/exact matches` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Transfers** | Expose a focused Livewire 4 component and namespaced Blade default view for `transfers` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Grouped receipts** | Expose a focused Livewire 4 component and namespaced Blade default view for `grouped receipts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Fees/interest** | Expose a focused Livewire 4 component and namespaced Blade default view for `fees/interest` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Adjustments** | Expose a focused Livewire 4 component and namespaced Blade default view for `adjustments` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Statement balance** | Expose a focused Livewire 4 component and namespaced Blade default view for `statement balance` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Exceptions** | Expose a focused Livewire 4 component and namespaced Blade default view for `exceptions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Sign-off** | Expose a focused Livewire 4 component and namespaced Blade default view for `sign-off` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [Sessions.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation-livewire/src/Livewire/Sessions.php) · [BankReconciliationLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation-livewire/src/BankReconciliationLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ReconciliationSummaryQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/src/Queries/ReconciliationSummaryQuery.php) | `public function handle(ReconciliationSession $session): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddReconciliationEntry.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/src/Actions/AddReconciliationEntry.php) | `public function handle(ReconciliationSession $session, array $attributes): ReconciliationEntry` |
| [ConfirmReconciliationEntry.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/src/Actions/ConfirmReconciliationEntry.php) | `public function handle(ReconciliationEntry $entry): ReconciliationEntry` |
| [CreateReconciliationSession.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/src/Actions/CreateReconciliationSession.php) | `public function handle(array $attributes): ReconciliationSession` |
| [SignOffReconciliation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/src/Actions/SignOffReconciliation.php) | `public function handle(ReconciliationSession $session): ReconciliationSession` |
| [BankReconciliationPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation-api/src/Policies/BankReconciliationPolicy.php) | `public function viewAny(?object $user = null): bool`<br>`public function view(?object $user, object $session): bool`<br>`public function create(?object $user = null): bool`<br>`public function update(?object $user, object $session): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ReconciliationEntry.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/src/Models/ReconciliationEntry.php) | `team_id`, `session_id`, `source_type`, `source_id`, `kind`, `status`, `amount`, `currency`, `confidence`, `description`, `metadata`, `exception_reason`, `confirmed_at`, `confirmed_by` |
| [ReconciliationSession.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bank-reconciliation/src/Models/ReconciliationSession.php) | `team_id`, `user_id`, `bank_account_id`, `period_start`, `period_end`, `opening_balance`, `statement_balance`, `status`, `signed_off_at`, `signed_off_by`, `metadata` |
<!-- layer-implementation-plan:end -->
