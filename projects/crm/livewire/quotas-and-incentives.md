# CRM: Quotas and Incentives Livewire

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-quotas-and-incentives-livewire`  
**Matching domain module:** `crm-quotas-and-incentives`  
**Application:** CRM  
**Source feature:** [Quotas and Incentives](../features/quotas-and-incentives.md)  
**Architecture:** [LIVEWIRE.md](../CRM.md) · [MODULES.md](../CRM.md) · [TESTING.md](../CRM.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Quotas:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Ramps:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Crediting:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Splits:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Territories:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Attainment:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Commission plans:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Accelerators:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Adjustments:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Disputes:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Approvals:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Payroll/export adapters:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-quotas-and-incentives-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-crm-quotas-and-incentives::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `quotas`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `ramps`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `crediting`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `splits`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `territories`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `attainment`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `commission-plans`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `accelerators`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `adjustments`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `disputes`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `approvals`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `payroll/export-adapters`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-quotas-and-incentives` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
