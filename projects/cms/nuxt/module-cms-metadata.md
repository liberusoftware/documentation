# CMS: Module Cms Metadata Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-cms-metadata). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-cms-module-cms-metadata-nuxt`
**Matching domain module:** `module-cms-metadata`
**Application:** CMS
**Source feature:** [Module Cms Metadata](../features/module-cms-metadata.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/module-cms-metadata.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `module-cms-metadata` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Arbitrary governed metadata:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Definitions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Inheritance:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Validation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Provenance:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Indexing:** page/component/composable/API-action behavior for this module's authorized workflow.
- **API exposure:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-cms-module-cms-metadata-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `arbitrary-governed-metadata`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `definitions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `inheritance`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `validation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `provenance`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `indexing`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `api-exposure`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `module-cms-metadata` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-cms-nuxt-vue`](https://github.com/liberusoftware/project-cms-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/module-cms-metadata.md)) |
| Capability Nuxt module skeleton | [`module-cms-metadata-nuxt`](https://github.com/liberusoftware/module-cms-metadata-nuxt) (`@liberusoftware/module-cms-metadata-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Arbitrary governed metadata** | Expose composable and Vue 3 component for `arbitrary governed metadata` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-metadata.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Definitions** | Expose composable and Vue 3 component for `definitions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-metadata.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Inheritance** | Expose composable and Vue 3 component for `inheritance` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-metadata.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Validation** | Expose composable and Vue 3 component for `validation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-metadata.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Provenance** | Expose composable and Vue 3 component for `provenance` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-metadata.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Indexing** | Expose composable and Vue 3 component for `indexing` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-metadata.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **API exposure** | Expose composable and Vue 3 component for `api exposure` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-cms-metadata.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [MetadataService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-metadata/src/Services/MetadataService.php) | `public function all(string $subjectType, int\|string $subjectId): array`<br>`public function get(string $subjectType, int\|string $subjectId, string $key, mixed $default = null): mixed`<br>`public function set(string $subjectType, int\|string $subjectId, string $key, mixed $value, ?int $teamId = null): MetadataEntry`<br>`public function remove(string $subjectType, int\|string $subjectId, string $key): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MetadataEntry.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-metadata/src/Models/MetadataEntry.php) | `subject_type`, `subject_id`, `key`, `value`, `value_type`, `team_id` |
<!-- layer-implementation-plan:end -->
