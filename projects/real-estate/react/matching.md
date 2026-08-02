# Real Estate: Matching React + Inertia\n\n## Canonical one-to-one React/Inertia implementation\n\n**Package:** `module-real-estate-matching-react-inertia`\n**Matching domain module:** `real-estate-matching`\n**Application:** Real Estate\n**Source feature:** [Matching](../features/matching.md)\n**Architecture:** [REACT.md](../REAL-ESTATE.md) · [API.md](../REAL-ESTATE.md) · [Matching API module](../api/matching.md) · [MODULES.md](../REAL-ESTATE.md) · [TESTING.md](../REAL-ESTATE.md)\n\n## 1. Purpose and ownership\n\nThis optional React 19.2 + Inertia 3 presentation package presents exactly one matching API module. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.\n\n## 2. Module-specific surfaces\n\n- **Applicant requirements:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Affordability:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Preferences:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Scoring:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Alerts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Feedback:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Exclusions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n\n## 3. React 19.2 + Inertia 3 implementation\n\n- Register a stable `module-real-estate-matching-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.\n- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.\n- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.\n- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.\n\n### Capability mapping\n\n- `applicant-requirements`: map the matching API query/action to a focused React page, component, hook, or Inertia form.\n- `affordability`: map the matching API query/action to a focused React page, component, hook, or Inertia form.\n- `preferences`: map the matching API query/action to a focused React page, component, hook, or Inertia form.\n- `scoring`: map the matching API query/action to a focused React page, component, hook, or Inertia form.\n- `alerts`: map the matching API query/action to a focused React page, component, hook, or Inertia form.\n- `feedback`: map the matching API query/action to a focused React page, component, hook, or Inertia form.\n- `exclusions`: map the matching API query/action to a focused React page, component, hook, or Inertia form.\n\n## 4. API contract and Inertia consumption\n\n- Consume only the matching API module linked above; use its documented OpenAPI schemas, routes, authentication, permissions, team context, pagination, errors, and operation semantics.\n- Keep a typed module-local API client and hooks boundary; use Inertia visits for page transitions and `useForm`/`router` for mutations, preserving server validation and redirect semantics.\n- Forward Sanctum cookies or approved authorization headers through a controlled first-party boundary; never persist long-lived tokens in browser storage or expose secrets in page props.\n- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.\n- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.\n\n## 5. Security and verification\n\n- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.\n- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, SSR hydration where enabled, and minimal-host installation tests.\n- Test observable behavior with TypeScript, ESLint, Vitest, React Testing Library, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.\n\n## 6. Definition of done\n\n- Package identity, public exports, API dependency, and module dependency match `real-estate-matching` one-to-one.\n- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.\n- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

## Canonical one-to-one React/Inertia implementation

**Package:** `module-real-estate-matching-react-inertia`
**Matching domain module:** `real-estate-matching`
**Application:** Real Estate
**Source feature:** [Matching](../features/matching.md)
**Architecture:** [REACT.md](../REAL-ESTATE.md) · [API.md](../REAL-ESTATE.md) · [Matching API module](../api/matching.md) · [MODULES.md](../REAL-ESTATE.md) · [TESTING.md](../REAL-ESTATE.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package presents exactly one matching API module. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Applicant requirements:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Affordability:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Preferences:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Scoring:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Alerts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Feedback:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Exclusions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-real-estate-matching-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `applicant-requirements`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `affordability`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `preferences`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `scoring`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `alerts`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `feedback`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `exclusions`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `real-estate-matching` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.
