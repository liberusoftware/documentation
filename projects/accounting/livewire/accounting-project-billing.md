# Accounting: Accounting Project Billing Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-project-billing). Observed identity: [`liberusoftware/module-accounting-project-billing-livewire`](../../../modules/source/liberusoftware--module-accounting-project-billing-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-accounting-project-billing-livewire`  
**Matching domain module:** `accounting-project-billing`  
**Application:** Accounting  
**Source feature:** [Accounting Project Billing](../features/accounting-project-billing.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Fixed fee:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Time/material:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Milestone:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Progress:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Retainer:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Billable time/expense:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Write-up/down:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Invoice handoff:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-accounting-project-billing-livewire` component namespace and service provider; use explicit aliases such as `<livewire:accountingAccountingProjectBilling::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `fixed-fee`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `time-material`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `milestone`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `progress`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `retainer`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `billable-time-expense`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `write-up-down`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `invoice-handoff`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-project-billing` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/accounting-project-billing.md) · [API plan](../api/accounting-project-billing.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Fixed fee** | Expose a focused Livewire 4 component and namespaced Blade default view for `fixed fee` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Time/material** | Expose a focused Livewire 4 component and namespaced Blade default view for `time/material` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Milestone** | Expose a focused Livewire 4 component and namespaced Blade default view for `milestone` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Progress** | Expose a focused Livewire 4 component and namespaced Blade default view for `progress` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Retainer** | Expose a focused Livewire 4 component and namespaced Blade default view for `retainer` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Billable time/expense** | Expose a focused Livewire 4 component and namespaced Blade default view for `billable time/expense` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Write-up/down** | Expose a focused Livewire 4 component and namespaced Blade default view for `write-up/down` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Invoice handoff** | Expose a focused Livewire 4 component and namespaced Blade default view for `invoice handoff` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [ProjectBillings.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-billing-livewire/src/Livewire/ProjectBillings.php) · [ProjectBillingLivewireServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-billing-livewire/src/ProjectBillingLivewireServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ProjectBillingSummary.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-billing/src/Queries/ProjectBillingSummary.php) | `public function forProject(int $projectJobId, ?int $teamId = null): array`<br>`public function summarize(Collection $rows): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [HandoffProjectBilling.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-billing/src/Actions/HandoffProjectBilling.php) | `public function handle(ProjectBilling $billing, ?string $invoiceRef = null): ProjectBilling` |
| [RecordProjectBilling.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-billing/src/Actions/RecordProjectBilling.php) | `public function handle(array $attributes): ProjectBilling` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ProjectBilling.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-billing/src/Models/ProjectBilling.php) | `team_id`, `project_job_id`, `method`, `status`, `period_start`, `period_end`, `currency`, `quantity`, `rate`, `amount`, `progress_percent`, `billable_time_amount`, `billable_expense_amount`, `retainer_amount`, `write_up_down_amount`, `source_ref`, `invoice_ref`, `metadata` |
| [Project.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-billing-api/src/Models/Project.php) | `name`, `code`, `description`, `start_date`, `end_date`, `status`, `allocation_percentage` |
<!-- layer-implementation-plan:end -->
