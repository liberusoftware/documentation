# Genealogy: Genealogy Tree Viewer Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#genealogy-tree-viewer). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-genealogy-genealogy-tree-viewer-nuxt`
**Matching domain module:** `genealogy-tree-viewer`
**Application:** Genealogy
**Source feature:** [Genealogy Tree Viewer](../features/genealogy-tree-viewer.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/genealogy-tree-viewer.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `genealogy-tree-viewer` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Pedigree:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Descendants:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Fan/chart views:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Navigation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Filters:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Large-tree rendering:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-genealogy-genealogy-tree-viewer-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `pedigree`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `descendants`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `fan-chart-views`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `navigation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `filters`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `large-tree-rendering`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `genealogy-tree-viewer` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-genealogy-nuxt-vue`](https://github.com/liberusoftware/project-genealogy-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-genealogy-laravel-api`](https://github.com/liberusoftware/project-genealogy-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/genealogy-tree-viewer.md)) |
| Capability Nuxt module skeleton | [`module-genealogy-tree-viewer-nuxt`](https://github.com/liberusoftware/module-genealogy-tree-viewer-nuxt) (`@liberusoftware/module-genealogy-tree-viewer-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Pedigree** | Expose composable and Vue 3 component for `pedigree` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/genealogy-tree-viewer.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-genealogy-laravel-api`. |
| **Descendants** | Expose composable and Vue 3 component for `descendants` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/genealogy-tree-viewer.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-genealogy-laravel-api`. |
| **Fan/chart views** | Expose composable and Vue 3 component for `fan/chart views` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/genealogy-tree-viewer.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-genealogy-laravel-api`. |
| **Navigation** | Expose composable and Vue 3 component for `navigation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/genealogy-tree-viewer.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-genealogy-laravel-api`. |
| **Filters** | Expose composable and Vue 3 component for `filters` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/genealogy-tree-viewer.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-genealogy-laravel-api`. |
| **Large-tree rendering** | Expose composable and Vue 3 component for `large-tree rendering` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/genealogy-tree-viewer.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-genealogy-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [TreeGraph.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-tree-viewer/src/Queries/TreeGraph.php) | `public function for( Person $root, int $generations = 3, bool $includeLiving = true, string $view = 'chart', bool $includeSiblings = false, int $maxNodes = 2000, ): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateTreeView.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-tree-viewer/src/Actions/CreateTreeView.php) | `public function execute(array $attributes): TreeView` |
| [DeleteTreeView.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-tree-viewer/src/Actions/DeleteTreeView.php) | `public function execute(TreeView $tree): void` |
| [UpdateTreeView.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-tree-viewer/src/Actions/UpdateTreeView.php) | `public function execute(TreeView $tree, array $attributes): TreeView` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [TreeView.php](https://github.com/liberusoftware/project-genealogy-laravel-filament/blob/577e93db23cc969fd532086c06524f9f2bb2b5ea/modules/genealogy-tree-viewer/src/Models/TreeView.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
