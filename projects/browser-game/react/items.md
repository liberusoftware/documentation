# Browser Game: Items React + Inertia\n\n## Canonical one-to-one React/Inertia implementation\n\n**Package:** `module-browser-game-items-react-inertia`\n**Matching domain module:** `browser-game-items`\n**Application:** Browser Game\n**Source feature:** [Items](../features/items.md)\n**Architecture:** [REACT.md](../BROWSER-GAME.md) · [API.md](../BROWSER-GAME.md) · [Matching API module](../api/items.md) · [MODULES.md](../BROWSER-GAME.md) · [TESTING.md](../BROWSER-GAME.md)\n\n## 1. Purpose and ownership\n\nThis optional React 19.2 + Inertia 3 presentation package presents exactly one matching API module. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.\n\n## 2. Module-specific surfaces\n\n- **Definitions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Inventory:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Equipment:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Durability:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Binding:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Containers:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Stack rules:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Provenance:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n\n## 3. React 19.2 + Inertia 3 implementation\n\n- Register a stable `module-browser-game-items-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.\n- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.\n- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.\n- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.\n\n### Capability mapping\n\n- `definitions`: map the matching API query/action to a focused React page, component, hook, or Inertia form.\n- `inventory`: map the matching API query/action to a focused React page, component, hook, or Inertia form.\n- `equipment`: map the matching API query/action to a focused React page, component, hook, or Inertia form.\n- `durability`: map the matching API query/action to a focused React page, component, hook, or Inertia form.\n- `binding`: map the matching API query/action to a focused React page, component, hook, or Inertia form.\n- `containers`: map the matching API query/action to a focused React page, component, hook, or Inertia form.\n- `stack-rules`: map the matching API query/action to a focused React page, component, hook, or Inertia form.\n- `provenance`: map the matching API query/action to a focused React page, component, hook, or Inertia form.\n\n## 4. API contract and Inertia consumption\n\n- Consume only the matching API module linked above; use its documented OpenAPI schemas, routes, authentication, permissions, team context, pagination, errors, and operation semantics.\n- Keep a typed module-local API client and hooks boundary; use Inertia visits for page transitions and `useForm`/`router` for mutations, preserving server validation and redirect semantics.\n- Forward Sanctum cookies or approved authorization headers through a controlled first-party boundary; never persist long-lived tokens in browser storage or expose secrets in page props.\n- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.\n- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.\n\n## 5. Security and verification\n\n- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.\n- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, SSR hydration where enabled, and minimal-host installation tests.\n- Test observable behavior with TypeScript, ESLint, Vitest, React Testing Library, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.\n\n## 6. Definition of done\n\n- Package identity, public exports, API dependency, and module dependency match `browser-game-items` one-to-one.\n- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.\n- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

## Canonical one-to-one React/Inertia implementation

**Package:** `module-browser-game-items-react-inertia`
**Matching domain module:** `browser-game-items`
**Application:** Browser Game
**Source feature:** [Items](../features/items.md)
**Architecture:** [REACT.md](../BROWSER-GAME.md) · [API.md](../BROWSER-GAME.md) · [Matching API module](../api/items.md) · [MODULES.md](../BROWSER-GAME.md) · [TESTING.md](../BROWSER-GAME.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package presents exactly one matching API module. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Definitions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Inventory:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Equipment:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Durability:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Binding:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Containers:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Stack rules:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Provenance:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-browser-game-items-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `definitions`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `inventory`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `equipment`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `durability`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `binding`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `containers`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `stack-rules`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `provenance`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `browser-game-items` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.
