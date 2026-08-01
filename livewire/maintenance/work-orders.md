# Maintenance: Work Orders Livewire

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-maintenance-work-orders-livewire`  
**Matching domain module:** `maintenance-work-orders`  
**Application:** Maintenance  
**Source feature:** [Work Orders](../../features/maintenance/work-orders.md)  
**Architecture:** [LIVEWIRE.md](../../LIVEWIRE.md) · [MODULES.md](../../MODULES.md) · [TESTING.md](../../TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Requests:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Triage:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Jobs:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Tasks:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Status machine:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Dependencies:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Notes:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Evidence:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Completion:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-maintenance-work-orders-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-maintenance-work-orders::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `requests`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `triage`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `jobs`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `tasks`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `status-machine`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `dependencies`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `notes`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `evidence`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `completion`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `maintenance-work-orders` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
