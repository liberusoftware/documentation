# CMS: Content Entities Livewire

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-cms-content-entities-livewire`  
**Matching domain module:** `cms-content-entities`  
**Application:** CMS  
**Source feature:** [Content Entities](../../features/cms/content-entities.md)  
**Architecture:** [LIVEWIRE.md](../../LIVEWIRE.md) · [MODULES.md](../../MODULES.md) · [TESTING.md](../../TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Typed entities:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Bundles/content types:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Lifecycle:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Authorship:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Status:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Cloning:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Relationships:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Canonical identifiers:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-cms-content-entities-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-cms-content-entities::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `typed-entities`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `bundles/content-types`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `lifecycle`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `authorship`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `status`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `cloning`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `relationships`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `canonical-identifiers`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `cms-content-entities` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.
