# Accounting: QuickBooks Online Migration React + Inertia

## Canonical one-to-one React/Inertia implementation

**Package:** `module-accounting-quickbooks-online-migration-react-inertia`
**Matching domain module:** `accounting-quickbooks-online-migration`
**Application:** Accounting
**Source feature:** [QuickBooks Online Migration](../features/quickbooks-online-migration.md)
**Architecture:** [REACT.md](../ACCOUNTING.md) · [API.md](../ACCOUNTING.md) · [Matching API module](../api/quickbooks-online-migration.md) · [MODULES.md](../ACCOUNTING.md) · [TESTING.md](../ACCOUNTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package presents exactly one matching API module. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Chart:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Classes/locations:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Contacts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Items:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Invoices/bills/credits/payments:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Journals:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Bank data:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Projects:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Tax:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Attachments:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Source IDs:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-accounting-quickbooks-online-migration-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `chart`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `classes-locations`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `contacts`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `items`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `invoices-bills-credits-payments`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `journals`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `bank-data`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `projects`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `tax`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `attachments`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `source-ids`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-quickbooks-online-migration` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.
