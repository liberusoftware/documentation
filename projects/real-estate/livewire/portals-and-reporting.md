# Real Estate: Portals and Reporting Livewire

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-real-estate-portals-and-reporting-livewire`  
**Matching domain module:** `real-estate-portals-and-reporting`  
**Application:** Real Estate  
**Source feature:** [Portals and Reporting](../features/portals-and-reporting.md)  
**Architecture:** [LIVEWIRE.md](../REAL-ESTATE.md) · [MODULES.md](../REAL-ESTATE.md) · [TESTING.md](../REAL-ESTATE.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Party self-service plus pipeline:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Conversion:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Source:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Fee:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Time-to-complete:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Occupancy:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Compliance metrics:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-real-estate-portals-and-reporting-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-real-estate-portals-and-reporting::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `party-self-service-plus-pipeline`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `conversion`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `source`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `fee`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `time-to-complete`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `occupancy`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `compliance-metrics`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `real-estate-portals-and-reporting` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
