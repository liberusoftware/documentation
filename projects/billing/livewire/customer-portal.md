# Billing: Customer Portal Livewire

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-billing-customer-portal-livewire`  
**Matching domain module:** `billing-customer-portal`  
**Application:** Billing  
**Source feature:** [Customer Portal](../features/customer-portal.md)  
**Architecture:** [LIVEWIRE.md](../BILLING.md) · [MODULES.md](../BILLING.md) · [TESTING.md](../BILLING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Profile:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Orders:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Services:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Usage:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Invoices:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Payments:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Tickets:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Changes:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Cancellation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-billing-customer-portal-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-billing-customer-portal::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `profile`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `orders`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `services`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `usage`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `invoices`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `payments`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `tickets`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `changes`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `cancellation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `billing-customer-portal` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
