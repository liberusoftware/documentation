# Browser Game: Social Livewire

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-browser-game-social-livewire`  
**Matching domain module:** `browser-game-social`  
**Application:** Browser Game  
**Source feature:** [Social](../features/social.md)  
**Architecture:** [LIVEWIRE.md](../BROWSER-GAME.md) · [MODULES.md](../BROWSER-GAME.md) · [TESTING.md](../BROWSER-GAME.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Friends:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Parties:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Chat:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Mail:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Guilds:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Alliances:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Permissions:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Activity:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Reporting:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-browser-game-social-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-browser-game-social::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `friends`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `parties`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `chat`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `mail`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `guilds`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `alliances`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `permissions`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `activity`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `reporting`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `browser-game-social` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
