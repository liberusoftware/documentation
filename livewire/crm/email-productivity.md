# CRM: Email Productivity Livewire

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-email-productivity-livewire`  
**Matching domain module:** `crm-email-productivity`  
**Application:** CRM  
**Source feature:** [Email Productivity](../../features/crm/email-productivity.md)  
**Architecture:** [LIVEWIRE.md](../../LIVEWIRE.md) · [MODULES.md](../../MODULES.md) · [TESTING.md](../../TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Mailbox sync:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Send/log:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Templates:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Snippets:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Scheduling:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Open/click/reply tracking policy:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Shared/team inbox:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Signatures:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Sidebars:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Gmail/Outlook adapters:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-email-productivity-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-crm-email-productivity::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `mailbox-sync`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `send/log`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `templates`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `snippets`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `scheduling`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `open/click/reply-tracking-policy`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `shared/team-inbox`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `signatures`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `sidebars`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `gmail/outlook-adapters`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-email-productivity` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
