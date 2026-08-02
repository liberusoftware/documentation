# Ecommerce: Cart Livewire

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-ecommerce-cart-livewire`  
**Matching domain module:** `ecommerce-cart`  
**Application:** Ecommerce  
**Source feature:** [Cart](../features/cart.md)  
**Architecture:** [LIVEWIRE.md](../ECOMMERCE.md) · [MODULES.md](../ECOMMERCE.md) · [TESTING.md](../ECOMMERCE.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Guest/customer/company carts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Lines:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Configuration:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Quantity:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Validation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Persistence:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Merge:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Sharing:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Estimates:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Recalculation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-ecommerce-cart-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-ecommerce-cart::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `guest/customer/company-carts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `lines`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `configuration`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `quantity`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `validation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `persistence`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `merge`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `sharing`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `estimates`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `recalculation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `ecommerce-cart` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
