# CRM: Consent and Preferences Livewire

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-consent-and-preferences-livewire`  
**Matching domain module:** `crm-consent-and-preferences`  
**Application:** CRM  
**Source feature:** [Consent and Preferences](../features/consent-and-preferences.md)  
**Architecture:** [LIVEWIRE.md](../CRM.md) · [MODULES.md](../CRM.md) · [TESTING.md](../CRM.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Lawful basis:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Subscriptions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Channel/topic preferences:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Suppression:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Quiet hours:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Recording consent:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Proof:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Expiry:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Withdrawal:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Policy evaluation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-consent-and-preferences-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-crm-consent-and-preferences::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `lawful-basis`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `subscriptions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `channel/topic-preferences`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `suppression`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `quiet-hours`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `recording-consent`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `proof`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `expiry`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `withdrawal`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `policy-evaluation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-consent-and-preferences` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
