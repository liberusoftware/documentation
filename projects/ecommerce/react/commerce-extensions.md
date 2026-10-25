# Ecommerce: Commerce Extensions React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#commerce-extensions). Implementation also lives in the [application tree](../SOURCE-APPLICATION.md); preserve this documented module. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-ecommerce-commerce-extensions-react-inertia`
**Matching domain module:** `ecommerce-commerce-extensions`
**Application:** Ecommerce
**Source feature:** [Commerce Extensions](../features/commerce-extensions.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/commerce-extensions.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Extension manifests:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Install/update/uninstall:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Scopes:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Webhooks:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Functions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **UI extensions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Compatibility:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Health:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Rollback:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-ecommerce-commerce-extensions-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `extension-manifests`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `install-update-uninstall`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `scopes`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `webhooks`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `functions`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `ui-extensions`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `compatibility`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `health`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `rollback`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

## 4. API contract and Inertia consumption

<!-- inertia-transport:start -->
### Inertia transport boundary

Use Laravel-owned Inertia page/command routes for visits and forms. The controller can invoke the module's public application actions in the same host or use a deliberate API adapter, then return an Inertia page/redirect response. A bare REST JSON resource response is not an Inertia page. Keep authoritative domain authorization and validation in the owning boundary for either path.

Independent API consumers and Next.js use their reviewed HTTP/session integration. Share DTOs and framework-independent UI primitives; keep Inertia page props, visits, form errors and redirects in the Inertia wrapper. Do not introduce loopback HTTP solely to reuse a public action inside the same Laravel host.

See the [Inertia standard](../../../standards/INERTIA.md), [request lifecycle](https://inertiajs.com/docs/v3/core-concepts/how-it-works) and [redirect behavior](https://inertiajs.com/docs/v3/the-basics/redirects).
<!-- inertia-transport:end -->

- Reuse the matching public application/API contracts. For HTTP consumption, use its documented schemas, routes, authentication, permissions, tenant context, errors and operation semantics; Inertia visits still require an Inertia response.
- Keep a typed module-local API client and hooks boundary; use Inertia visits for page transitions and `useForm`/`router` for mutations, preserving server validation and redirect semantics.
- Forward Sanctum cookies or approved authorization headers through a controlled first-party boundary; never persist long-lived tokens in browser storage or expose secrets in page props.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, SSR hydration where enabled, and minimal-host installation tests.
- Test observable behavior with TypeScript, ESLint, Vitest, React Testing Library, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `ecommerce-commerce-extensions` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.
