# CRM: Email Productivity React + Inertia

## Canonical one-to-one React/Inertia implementation

**Package:** `module-crm-email-productivity-react-inertia`
**Matching domain module:** `crm-email-productivity`
**Application:** CRM
**Source feature:** [Email Productivity](../features/email-productivity.md)
**Architecture:** [REACT.md](../CRM.md) · [API.md](../CRM.md) · [Matching API module](../api/email-productivity.md) · [MODULES.md](../CRM.md) · [TESTING.md](../CRM.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package presents exactly one matching API module. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Mailbox sync:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Send/log:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Templates:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Snippets:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Scheduling:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Open/click/reply tracking policy:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Shared/team inbox:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Signatures:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Sidebars:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Gmail/Outlook adapters:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-crm-email-productivity-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `mailbox-sync`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `send-log`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `templates`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `snippets`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `scheduling`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `open-click-reply-tracking-policy`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `shared-team-inbox`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `signatures`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `sidebars`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `gmail-outlook-adapters`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `crm-email-productivity` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.
