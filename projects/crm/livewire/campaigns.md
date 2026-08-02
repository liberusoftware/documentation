# CRM: Campaigns Livewire

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-campaigns-livewire`  
**Matching domain module:** `crm-campaigns`  
**Application:** CRM  
**Source feature:** [Campaigns](../features/campaigns.md)  
**Architecture:** [LIVEWIRE.md](../CRM.md) · [MODULES.md](../CRM.md) · [TESTING.md](../CRM.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Campaign hierarchy:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Briefs:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Objectives:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Budget:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Assets:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Channels:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Audience:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Owners:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Calendar:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Tasks:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Costs:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Responses:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Influence:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **ROI:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-campaigns-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-crm-campaigns::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `campaign-hierarchy`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `briefs`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `objectives`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `budget`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `assets`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `channels`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `audience`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `owners`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `calendar`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `tasks`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `costs`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `responses`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `influence`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `roi`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-campaigns` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
