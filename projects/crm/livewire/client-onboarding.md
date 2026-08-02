# CRM: Client Onboarding Livewire

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-client-onboarding-livewire`  
**Matching domain module:** `crm-client-onboarding`  
**Application:** CRM  
**Source feature:** [Client Onboarding](../features/client-onboarding.md)  
**Architecture:** [LIVEWIRE.md](../CRM.md) · [MODULES.md](../CRM.md) · [TESTING.md](../CRM.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Intake:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Domain/provider connections:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Data import:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Snapshot application:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Verification:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Launch checklist:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Training:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Handoff:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Health:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-client-onboarding-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-crm-client-onboarding::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `intake`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `domain/provider-connections`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `data-import`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `snapshot-application`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `verification`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `launch-checklist`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `training`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `handoff`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `health`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-client-onboarding` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
