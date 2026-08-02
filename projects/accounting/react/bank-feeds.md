# Accounting: Bank Feeds React + Inertia

## Canonical one-to-one React/Inertia implementation

**Package:** `module-accounting-bank-feeds-react-inertia`
**Matching domain module:** `accounting-bank-feeds`
**Application:** Accounting
**Source feature:** [Bank Feeds](../features/bank-feeds.md)
**Architecture:** [REACT.md](../ACCOUNTING.md) · [API.md](../ACCOUNTING.md) · [Matching API module](../api/bank-feeds.md) · [MODULES.md](../ACCOUNTING.md) · [TESTING.md](../ACCOUNTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package presents exactly one matching API module. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Consent/connections:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Institutions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Account mapping:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Cursors:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Imports:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Duplicates:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Pending/posted state:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Health:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Provider adapters:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-accounting-bank-feeds-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `consent-connections`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `institutions`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `account-mapping`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `cursors`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `imports`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `duplicates`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `pending-posted-state`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `health`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `provider-adapters`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-bank-feeds` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.
