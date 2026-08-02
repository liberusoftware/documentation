# CRM: Case Management React + Inertia

## Canonical one-to-one React/Inertia implementation

**Package:** `module-crm-case-management-react-inertia`
**Matching domain module:** `crm-case-management`
**Application:** CRM
**Source feature:** [Case Management](../features/case-management.md)
**Architecture:** [REACT.md](../CRM.md) · [API.md](../CRM.md) · [Matching API module](../api/case-management.md) · [MODULES.md](../CRM.md) · [TESTING.md](../CRM.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package presents exactly one matching API module. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Tickets/cases:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Types:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Pipelines:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Statuses:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Priorities:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Ownership:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Parent/child cases:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Related assets/orders:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Entitlements:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Escalation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Audit:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-crm-case-management-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `tickets-cases`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `types`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `pipelines`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `statuses`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `priorities`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `ownership`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `parent-child-cases`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `related-assets-orders`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `entitlements`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `escalation`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `audit`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `crm-case-management` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.
