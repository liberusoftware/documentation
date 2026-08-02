# CRM: SLA and Entitlements Vue + Inertia\n\n## Canonical one-to-one Vue/Inertia implementation\n\n**Package:** `module-crm-sla-and-entitlements-vue-inertia`\n**Matching domain module:** `crm-sla-and-entitlements`\n**Application:** CRM\n**Source feature:** [SLA and Entitlements](../features/sla-and-entitlements.md)\n**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/sla-and-entitlements.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)\n\n## 1. Purpose and ownership\n\nThis optional Vue 3 + Inertia 3 presentation package presents exactly one matching API module. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.\n\n## 2. Module-specific surfaces\n\n- **Service contracts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Coverage:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Business calendars:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Response/resolution targets:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Milestones:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Pauses:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Warnings:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Breaches:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Escalations:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n- **Exceptions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.\n\n## 3. Vue 3 + Inertia 3 implementation\n\n- Register a stable `module-crm-sla-and-entitlements-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.\n- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.\n- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.\n- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.\n\n### Capability mapping\n\n- `service-contracts`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.\n- `coverage`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.\n- `business-calendars`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.\n- `response-resolution-targets`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.\n- `milestones`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.\n- `pauses`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.\n- `warnings`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.\n- `breaches`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.\n- `escalations`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.\n- `exceptions`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.\n\n## 4. API contract and Inertia consumption\n\n- Consume only the matching API module linked above; use its documented OpenAPI schemas, routes, authentication, permissions, team context, pagination, errors, and operation semantics.\n- Keep a typed module-local API client and hooks boundary; use Inertia visits for page transitions and `useForm`/`router` for mutations, preserving server validation and redirect semantics.\n- Forward Sanctum cookies or approved authorization headers through a controlled first-party boundary; never persist long-lived tokens in browser storage or expose secrets in page props.\n- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.\n- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.\n\n## 5. Security and verification\n\n- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.\n- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, SSR hydration where enabled, and minimal-host installation tests.\n- Test observable behavior with TypeScript, ESLint, Vitest, Vue Test Utils, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.\n\n## 6. Definition of done\n\n- Package identity, public exports, API dependency, and module dependency match `crm-sla-and-entitlements` one-to-one.\n- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.\n- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

## Canonical one-to-one Vue/Inertia implementation

**Package:** `module-crm-sla-and-entitlements-vue-inertia`
**Matching domain module:** `crm-sla-and-entitlements`
**Application:** CRM
**Source feature:** [SLA and Entitlements](../features/sla-and-entitlements.md)
**Architecture:** [VUE-INERTIA.md](../../../standards/VUE.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/sla-and-entitlements.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Vue 3 + Inertia 3 presentation package presents exactly one matching API module. It contributes reusable Inertia pages, Vue components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Service contracts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Coverage:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Business calendars:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Response/resolution targets:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Milestones:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Pauses:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Warnings:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Breaches:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Escalations:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Exceptions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. Vue 3 + Inertia 3 implementation

- Register a stable `module-crm-sla-and-entitlements-vue-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, composables under `resources/js/composables`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `service-contracts`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `coverage`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `business-calendars`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `response-resolution-targets`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `milestones`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `pauses`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `warnings`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `breaches`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `escalations`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.
- `exceptions`: map the matching API query/action to a focused Vue page, component, hook, or Inertia form.

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

- Package identity, public exports, API dependency, and module dependency match `crm-sla-and-entitlements` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.
