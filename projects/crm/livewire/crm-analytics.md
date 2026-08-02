# CRM: CRM Analytics Livewire

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-analytics-livewire`  
**Matching domain module:** `crm-analytics`  
**Application:** CRM  
**Source feature:** [CRM Analytics](../features/crm-analytics.md)  
**Architecture:** [LIVEWIRE.md](../CRM.md) · [MODULES.md](../CRM.md) · [TESTING.md](../CRM.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Governed datasets:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Dashboards:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Reports:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Pivots:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Funnels:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Cohorts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Goals:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Schedules:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Exports:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Row-level access:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Metric lineage:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-analytics-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-crm-analytics::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `governed-datasets`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `dashboards`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `reports`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `pivots`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `funnels`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `cohorts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `goals`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `schedules`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `exports`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `row-level-access`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `metric-lineage`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-analytics` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
