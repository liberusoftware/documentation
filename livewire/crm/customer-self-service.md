# CRM: Customer Self-Service Livewire

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-customer-self-service-livewire`  
**Matching domain module:** `crm-customer-self-service`  
**Application:** CRM  
**Source feature:** [Customer Self-Service](../../features/crm/customer-self-service.md)  
**Architecture:** [LIVEWIRE.md](../../LIVEWIRE.md) · [MODULES.md](../../MODULES.md) · [TESTING.md](../../TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Customer portal:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Case submission/status:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Knowledge search:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Community links:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Appointments:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Documents:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Invoices/orders references:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Profile:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Preferences:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-customer-self-service-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-crm-customer-self-service::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `customer-portal`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `case-submission/status`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `knowledge-search`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `community-links`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `appointments`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `documents`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `invoices/orders-references`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `profile`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `preferences`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-customer-self-service` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
