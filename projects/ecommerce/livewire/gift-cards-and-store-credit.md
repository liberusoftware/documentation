# Ecommerce: Gift Cards and Store Credit Livewire

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-ecommerce-gift-cards-and-store-credit-livewire`  
**Matching domain module:** `ecommerce-gift-cards-and-store-credit`  
**Application:** Ecommerce  
**Source feature:** [Gift Cards and Store Credit](../features/gift-cards-and-store-credit.md)  
**Architecture:** [LIVEWIRE.md](../ECOMMERCE.md) · [MODULES.md](../ECOMMERCE.md) · [TESTING.md](../ECOMMERCE.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Issue:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Activate:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Send:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Redeem:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Partial use:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Balances:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Expiry:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Refund:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Transfer policy:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Liabilities:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Immutable ledger:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-ecommerce-gift-cards-and-store-credit-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-ecommerce-gift-cards-and-store-credit::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `issue`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `activate`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `send`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `redeem`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `partial-use`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `balances`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `expiry`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `refund`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `transfer-policy`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `liabilities`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `immutable-ledger`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `ecommerce-gift-cards-and-store-credit` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
