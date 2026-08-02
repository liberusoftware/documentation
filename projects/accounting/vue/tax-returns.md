# Accounting: Tax Returns Vue + Inertia\n\n## Canonical one-to-one Vue/Inertia implementation\n\n**Package:** `module-accounting-tax-returns-vue-inertia`\n**Matching domain module:** `accounting-tax-returns`\n**Application:** Accounting\n**Source feature:** [Tax Returns](../features/tax-returns.md)\n**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/tax-returns.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)\n\n## 1. Purpose and ownership\n\nThis optional Vue 3 + Inertia 3 presentation package presents exactly one matching API module. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.\n\n## 2. Module-specific surfaces\n\n- **Return preparation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Source reconciliation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Diagnostics:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Review:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Approval:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Submission adapter:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Receipt/status:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Payment:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Amendments:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n\n## 3. Vue 3 + Inertia 3 implementation\n\n- Register a stable `module-accounting-tax-returns-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.\n- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.\n- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.\n- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.\n\n### Capability mapping\n\n- `return-preparation`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.\n- `source-reconciliation`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.\n- `diagnostics`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.\n- `review`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.\n- `approval`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.\n- `submission-adapter`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.\n- `receipt-status`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.\n- `payment`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.\n- `amendments`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.\n\n## 4. API contract and Inertia consumption\n\n- Consume only the matching API module linked above; use its documented OpenAPI schemas, routes, authentication, permissions, team context, pagination, errors, and operation semantics.\n- Keep a typed module-local API client and hooks boundary; use Inertia visits for page transitions and `useForm`/`router` for mutations, preserving server validation and redirect semantics.\n- Forward Sanctum cookies or approved authorization headers through a controlled first-party boundary; never persist long-lived tokens in browser storage or expose secrets in page props.\n- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.\n- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.\n\n## 5. Security and verification\n\n- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.\n- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, SSR hydration where enabled, and minimal-host installation tests.\n- Test observable behavior with TypeScript, ESLint, Vitest, Vue Test Utils, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.\n\n## 6. Definition of done\n\n- Package identity, public exports, API dependency, and module dependency match `accounting-tax-returns` one-to-one.\n- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.\n- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-accounting-tax-returns-vue-inertia`
**Matching domain module:** `accounting-tax-returns`
**Application:** Accounting
**Source feature:** [Tax Returns](../features/tax-returns.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/tax-returns.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package presents exactly one matching API module. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Return preparation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Source reconciliation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Diagnostics:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Review:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Approval:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Submission adapter:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Receipt/status:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Payment:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Amendments:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-accounting-tax-returns-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `return-preparation`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `source-reconciliation`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `diagnostics`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `review`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `approval`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `submission-adapter`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `receipt-status`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `payment`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `amendments`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-tax-returns` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.
