# CRM: Templates and Snapshots Livewire

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-templates-and-snapshots-livewire`  
**Matching domain module:** `crm-templates-and-snapshots`  
**Application:** CRM  
**Source feature:** [Templates and Snapshots](../features/templates-and-snapshots.md)  
**Architecture:** [LIVEWIRE.md](../CRM.md) · [MODULES.md](../CRM.md) · [TESTING.md](../CRM.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Versioned bundles of fields:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Pipelines:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Workflows:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Forms:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Funnels:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Calendars:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Templates:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Dashboards:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Settings with preview:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Protected sharing:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Install:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Update:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Rollback:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-templates-and-snapshots-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-crm-templates-and-snapshots::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `versioned-bundles-of-fields`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `pipelines`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `workflows`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `forms`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `funnels`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `calendars`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `templates`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `dashboards`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `settings-with-preview`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `protected-sharing`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `install`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `update`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `rollback`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-templates-and-snapshots` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
