# CMS: Translation Management Vue + Inertia\n\n## Canonical one-to-one Vue/Inertia implementation\n\n**Package:** `module-cms-translation-management-vue-inertia`\n**Matching domain module:** `cms-translation-management`\n**Application:** CMS\n**Source feature:** [Translation Management](../features/translation-management.md)\n**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/translation-management.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)\n\n## 1. Purpose and ownership\n\nThis optional Vue 3 + Inertia 3 presentation package presents exactly one matching API module. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.\n\n## 2. Module-specific surfaces\n\n- **Jobs:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Source changes:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Assignments:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Vendor adapters:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Machine translation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Review:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Memory/glossaries:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Status:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Cost:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Reconciliation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n\n## 3. Vue 3 + Inertia 3 implementation\n\n- Register a stable `module-cms-translation-management-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.\n- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.\n- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.\n- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.\n\n### Capability mapping\n\n- `jobs`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.\n- `source-changes`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.\n- `assignments`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.\n- `vendor-adapters`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.\n- `machine-translation`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.\n- `review`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.\n- `memory-glossaries`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.\n- `status`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.\n- `cost`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.\n- `reconciliation`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.\n\n## 4. API contract and Inertia consumption\n\n- Consume only the matching API module linked above; use its documented OpenAPI schemas, routes, authentication, permissions, team context, pagination, errors, and operation semantics.\n- Keep a typed module-local API client and hooks boundary; use Inertia visits for page transitions and `useForm`/`router` for mutations, preserving server validation and redirect semantics.\n- Forward Sanctum cookies or approved authorization headers through a controlled first-party boundary; never persist long-lived tokens in browser storage or expose secrets in page props.\n- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.\n- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.\n\n## 5. Security and verification\n\n- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.\n- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, SSR hydration where enabled, and minimal-host installation tests.\n- Test observable behavior with TypeScript, ESLint, Vitest, Vue Test Utils, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.\n\n## 6. Definition of done\n\n- Package identity, public exports, API dependency, and module dependency match `cms-translation-management` one-to-one.\n- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.\n- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-cms-translation-management-vue-inertia`
**Matching domain module:** `cms-translation-management`
**Application:** CMS
**Source feature:** [Translation Management](../features/translation-management.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/translation-management.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package presents exactly one matching API module. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Jobs:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Source changes:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Assignments:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Vendor adapters:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Machine translation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Review:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Memory/glossaries:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Status:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Cost:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Reconciliation:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-cms-translation-management-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `jobs`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `source-changes`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `assignments`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `vendor-adapters`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `machine-translation`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `review`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `memory-glossaries`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `status`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `cost`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `reconciliation`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `cms-translation-management` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.
