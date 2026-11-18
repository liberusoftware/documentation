# Accounting: Payroll Journals Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#payroll-journals). Observed identity: [`liberusoftware/module-accounting-payroll-journals-livewire`](../../../modules/source/liberusoftware--module-accounting-payroll-journals-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-payroll-journals-livewire`  
**Matching domain module:** `accounting-payroll-journals`  
**Application:** Accounting  
**Source feature:** [Payroll Journals](../features/payroll-journals.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Gross pay:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Taxes:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Deductions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Benefits:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Employer costs:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Net pay:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Liabilities:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Allocation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Posting:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Reversal:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Corrections:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-payroll-journals-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-accounting-payroll-journals::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `gross-pay`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `taxes`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `deductions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `benefits`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `employer-costs`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `net-pay`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `liabilities`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `allocation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `posting`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `reversal`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `corrections`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-payroll-journals` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/payroll-journals.md) · [API plan](../api/payroll-journals.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Gross pay** | Expose a focused Livewire 4 component and namespaced Blade default view for `gross pay` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Taxes** | Expose a focused Livewire 4 component and namespaced Blade default view for `taxes` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Deductions** | Expose a focused Livewire 4 component and namespaced Blade default view for `deductions` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Benefits** | Expose a focused Livewire 4 component and namespaced Blade default view for `benefits` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Employer costs** | Expose a focused Livewire 4 component and namespaced Blade default view for `employer costs` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Net pay** | Expose a focused Livewire 4 component and namespaced Blade default view for `net pay` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Liabilities** | Expose a focused Livewire 4 component and namespaced Blade default view for `liabilities` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Allocation** | Expose a focused Livewire 4 component and namespaced Blade default view for `allocation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Posting** | Expose a focused Livewire 4 component and namespaced Blade default view for `posting` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Reversal** | Expose a focused Livewire 4 component and namespaced Blade default view for `reversal` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Corrections** | Expose a focused Livewire 4 component and namespaced Blade default view for `corrections` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [PayrollJournals.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-journals-livewire/src/Livewire/PayrollJournals.php) · [PayrollJournalsLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-journals-livewire/src/PayrollJournalsLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [PayrollJournalSummary.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-journals/src/Queries/PayrollJournalSummary.php) | `public function forTeam(?int $teamId = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreatePayrollJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-journals/src/Actions/CreatePayrollJournal.php) | `public function handle(array $attributes): PayrollJournal` |
| [PostPayrollJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-journals/src/Actions/PostPayrollJournal.php) | `public function handle(PayrollJournal $journal): PayrollJournal` |
| [ReversePayrollJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-journals/src/Actions/ReversePayrollJournal.php) | `public function handle(PayrollJournal $journal, string $reversalRef): PayrollJournal` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PayrollJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-journals/src/Models/PayrollJournal.php) | `team_id`, `journal_ref`, `payroll_period_start`, `payroll_period_end`, `currency`, `gross_pay`, `taxes`, `deductions`, `benefits`, `employer_costs`, `net_pay`, `liabilities`, `allocation`, `status`, `posted_at`, `reversed_at`, `reversal_ref`, `correction_ref`, `metadata` |
<!-- layer-implementation-plan:end -->
