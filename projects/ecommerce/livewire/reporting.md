# Ecommerce: Reporting Livewire

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-ecommerce-reporting-livewire`  
**Matching domain module:** `ecommerce-reporting`  
**Application:** Ecommerce  
**Source feature:** [Reporting](../features/reporting.md)  
**Architecture:** [LIVEWIRE.md](../ECOMMERCE.md) · [MODULES.md](../ECOMMERCE.md) · [TESTING.md](../ECOMMERCE.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Sales:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Margin:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Tax:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Discount:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Inventory:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Fulfillment:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Returns:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Customer:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Channel:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Market:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **B2B:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **POS:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Seller metrics:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-ecommerce-reporting-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-ecommerce-reporting::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `sales`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `margin`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `tax`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `discount`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `inventory`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `fulfillment`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `returns`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `customer`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `channel`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `market`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `b2b`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `pos`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `seller-metrics`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `ecommerce-reporting` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
