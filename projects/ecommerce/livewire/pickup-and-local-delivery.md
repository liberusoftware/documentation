# Ecommerce: Pickup and Local Delivery Livewire

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-ecommerce-pickup-and-local-delivery-livewire`  
**Matching domain module:** `ecommerce-pickup-and-local-delivery`  
**Application:** Ecommerce  
**Source feature:** [Pickup and Local Delivery](../features/pickup-and-local-delivery.md)  
**Architecture:** [LIVEWIRE.md](../ECOMMERCE.md) · [MODULES.md](../ECOMMERCE.md) · [TESTING.md](../ECOMMERCE.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Locations:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Availability:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Slots:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Preparation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Ready-for-pickup:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Verification:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Curbside:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Routes:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Proof:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **No-collection policy:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-ecommerce-pickup-and-local-delivery-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-ecommerce-pickup-and-local-delivery::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `locations`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `availability`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `slots`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `preparation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `ready-for-pickup`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `verification`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `curbside`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `routes`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `proof`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `no-collection-policy`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `ecommerce-pickup-and-local-delivery` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
