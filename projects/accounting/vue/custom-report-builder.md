# Accounting: Custom Report Builder Vue + Inertia

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-accounting-custom-report-builder-vue-inertia`
**Matching domain module:** `accounting-custom-report-builder`
**Application:** Accounting
**Source feature:** [Custom Report Builder](../features/custom-report-builder.md)
**Architecture:** [VUE-INERTIA.md](../../../architecture/VUE-INERTIA.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/custom-report-builder.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../architecture/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package presents exactly one matching API module. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Governed measures/dimensions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Filters:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Grouping:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Formulas:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Comparisons:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Layouts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Permissions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Saved variants:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Exports:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-accounting-custom-report-builder-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `governed-measures-dimensions`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `filters`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `grouping`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `formulas`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `comparisons`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `layouts`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `permissions`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `saved-variants`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `exports`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

## 4. API contract and Inertia consumption

- Consume only the matching API module linked above; use its documented OpenAPI schemas, routes, authentication, permissions, team context, pagination, errors, and operation semantics.
- Keep a typed module-local API client and hooks boundary; use Inertia visits for page transitions and `useForm`/`router` for mutations, preserving server validation and redirect semantics.
- Forward Sanctum cookies or approved authorization headers through a controlled first-party boundary; never persist long-lived tokens in browser storage or expose secrets in page props.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, SSR hydration where enabled, and minimal-host installation tests.
- Test observable behavior with TypeScript, ESLint, Vitest, Vue Test Utils, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `accounting-custom-report-builder` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.
