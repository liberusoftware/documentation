# Ecommerce: Point of Sale Livewire

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-ecommerce-point-of-sale-livewire`  
**Matching domain module:** `ecommerce-point-of-sale`  
**Application:** Ecommerce  
**Source feature:** [Point of Sale](../features/point-of-sale.md)  
**Architecture:** [LIVEWIRE.md](../ECOMMERCE.md) · [MODULES.md](../ECOMMERCE.md) · [TESTING.md](../ECOMMERCE.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Registers:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Carts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Customers:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Products:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Taxes:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Discounts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Tenders:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Receipts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Returns/exchanges:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Holds:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Staff actions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-ecommerce-point-of-sale-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-ecommerce-point-of-sale::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `registers`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `carts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `customers`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `products`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `taxes`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `discounts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `tenders`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `receipts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `returns/exchanges`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `holds`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `staff-actions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `ecommerce-point-of-sale` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
