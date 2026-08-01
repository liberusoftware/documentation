# Accounting: Mileage Livewire

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-accounting-mileage-livewire`  
**Matching domain module:** `accounting-mileage`  
**Application:** Accounting  
**Source feature:** [Mileage](../../features/accounting/mileage.md)  
**Architecture:** [LIVEWIRE.md](../../LIVEWIRE.md) · [MODULES.md](../../MODULES.md) · [TESTING.md](../../TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Vehicles/rates:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Trip capture/import:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Distance:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Business purpose:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Projects:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Policy:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Approval:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Reimbursement:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Regional reporting:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-accounting-mileage-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-accounting-mileage::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `vehicles/rates`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `trip-capture/import`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `distance`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `business-purpose`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `projects`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `policy`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `approval`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `reimbursement`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `regional-reporting`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `accounting-mileage` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
