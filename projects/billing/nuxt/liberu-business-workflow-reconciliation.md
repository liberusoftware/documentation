# Billing: Liberu Business Workflow Reconciliation Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#liberu-business-workflow-reconciliation). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-billing-liberu-business-workflow-reconciliation-nuxt`
**Matching domain module:** `liberu-business-workflow-reconciliation`
**Application:** Billing
**Source feature:** [Liberu Business Workflow Reconciliation](../features/liberu-business-workflow-reconciliation.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/liberu-business-workflow-reconciliation.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `liberu-business-workflow-reconciliation` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Workflow run registry:** page/component/composable/API-action behavior for this module's authorized workflow.
- **State mapping:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reconciliation rules:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Recovery coordination:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Audit timeline:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-billing-liberu-business-workflow-reconciliation-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `workflow-run-registry`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `state-mapping`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `reconciliation-rules`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `recovery-coordination`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `audit-timeline`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

## 4. API contract and Nuxt consumption

- Consume only the matching API module linked above; use its documented OpenAPI schemas, routes, authentication, permissions, team context, pagination, errors, and operation semantics.
- Keep a typed API client and module-local composables under the package boundary; use `useFetch` or `useAsyncData` for SSR-safe reads and `$fetch` for event-driven mutations.
- Forward Sanctum cookies or approved authorization headers through a controlled client boundary; never persist long-lived tokens in browser storage or expose secrets in SSR payloads.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, and minimal-host installation tests.
- Test observable browser and SSR behavior with Vitest, Vue Test Utils, Playwright, TypeScript, and the supported Nuxt 4/Vue 3 stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `liberu-business-workflow-reconciliation` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-billing-nuxt-vue`](https://github.com/liberusoftware/project-billing-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/liberu-business-workflow-reconciliation.md)) |
| Capability Nuxt module skeleton | [`module-module-liberu-business-workflow-reconciliation-3b42eab6-nuxt`](https://github.com/liberusoftware/module-module-liberu-business-workflow-reconciliation-3b42eab6-nuxt) (`@liberusoftware/module-module-liberu-business-workflow-reconciliation-3b42eab6-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Workflow run registry** | Expose composable and Vue 3 component for `workflow run registry` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/liberu-business-workflow-reconciliation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **State mapping** | Expose composable and Vue 3 component for `state mapping` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/liberu-business-workflow-reconciliation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Reconciliation rules** | Expose composable and Vue 3 component for `reconciliation rules` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/liberu-business-workflow-reconciliation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Recovery coordination** | Expose composable and Vue 3 component for `recovery coordination` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/liberu-business-workflow-reconciliation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Audit timeline** | Expose composable and Vue 3 component for `audit timeline` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/liberu-business-workflow-reconciliation.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateReconciliationCase.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-business-workflow-reconciliation/src/Actions/CreateReconciliationCase.php) | `public function execute(array $attributes): ReconciliationCase` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [WorkflowRun.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/liberu-business-workflow-reconciliation/src/Models/WorkflowRun.php) | `team_id`, `correlation_id`, `workflow_key`, `contract_version`, `state`, `steps`, `last_error` |
<!-- layer-implementation-plan:end -->
