# Genealogy: Media React + Inertia

## Canonical one-to-one React/Inertia implementation

**Package:** `module-genealogy-media-react-inertia`
**Matching domain module:** `genealogy-media`
**Application:** Genealogy
**Source feature:** [Media](../../features/genealogy/media.md)
**Architecture:** [REACT.md](../../REACT.md) · [API.md](../../API.md) · [Matching API module](../../api/genealogy/media.md) · [MODULES.md](../../MODULES.md) · [TESTING.md](../../TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package presents exactly one matching API module. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Documents:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Photographs:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Audio/video:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Transcription:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Rights:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Links:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Preservation metadata:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-genealogy-media-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `documents`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `photographs`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `audio-video`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `transcription`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `rights`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `links`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `preservation-metadata`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

## 4. API contract and Inertia consumption

- Consume only the matching API module linked above; use its documented OpenAPI schemas, routes, authentication, permissions, team context, pagination, errors, and operation semantics.
- Keep a typed module-local API client and hooks boundary; use Inertia visits for page transitions and `useForm`/`router` for mutations, preserving server validation and redirect semantics.
- Forward Sanctum cookies or approved authorization headers through a controlled first-party boundary; never persist long-lived tokens in browser storage or expose secrets in page props.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, SSR hydration where enabled, and minimal-host installation tests.
- Test observable behavior with TypeScript, ESLint, Vitest, React Testing Library, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `genealogy-media` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.
