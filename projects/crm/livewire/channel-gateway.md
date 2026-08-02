# CRM: Channel Gateway Livewire

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-channel-gateway-livewire`  
**Matching domain module:** `crm-channel-gateway`  
**Application:** CRM  
**Source feature:** [Channel Gateway](../features/channel-gateway.md)  
**Architecture:** [LIVEWIRE.md](../CRM.md) · [MODULES.md](../CRM.md) · [TESTING.md](../CRM.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Provider-neutral email:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **SMS/MMS:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **WhatsApp:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Web chat:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Social messaging:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Push contracts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Routing:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Templates:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Health:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Provider selection:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-channel-gateway-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-crm-channel-gateway::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `provider-neutral-email`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `sms/mms`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `whatsapp`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `web-chat`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `social-messaging`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `push-contracts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `routing`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `templates`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `health`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `provider-selection`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-channel-gateway` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
