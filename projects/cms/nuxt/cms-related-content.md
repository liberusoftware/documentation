# CMS: Cms Related Content Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-related-content). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-cms-cms-related-content-nuxt`
**Matching domain module:** `cms-related-content`
**Application:** CMS
**Source feature:** [Cms Related Content](../features/cms-related-content.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/cms-related-content.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `cms-related-content` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Manual/rule/search-driven relationships:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Similarity:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Recency:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Taxonomy:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Exclusions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Explainability:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Fallback:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-cms-cms-related-content-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `manual-rule-search-driven-relationships`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `similarity`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `recency`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `taxonomy`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `exclusions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `explainability`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `fallback`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `cms-related-content` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-cms-nuxt-vue`](https://github.com/liberusoftware/project-cms-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/cms-related-content.md)) |
| Capability Nuxt module skeleton | [`module-cms-related-content-nuxt`](https://github.com/liberusoftware/module-cms-related-content-nuxt) (`@liberusoftware/module-cms-related-content-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Manual/rule/search-driven relationships** | Expose composable and Vue 3 component for `manual/rule/search-driven relationships` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-related-content.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Similarity** | Expose composable and Vue 3 component for `similarity` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-related-content.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Recency** | Expose composable and Vue 3 component for `recency` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-related-content.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Taxonomy** | Expose composable and Vue 3 component for `taxonomy` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-related-content.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Exclusions** | Expose composable and Vue 3 component for `exclusions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-related-content.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Explainability** | Expose composable and Vue 3 component for `explainability` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-related-content.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Fallback** | Expose composable and Vue 3 component for `fallback` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-related-content.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [RelatedContentService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-related-content/src/Services/RelatedContentService.php) | `public function relate(string $sourceType, int $sourceId, string $targetType, int $targetId, string $mode = 'manual', float $score = 1, array $taxonomy = [], ?int $teamId = null): RelatedContent`<br>`public function exclude(string $sourceType, int $sourceId, string $targetType, int $targetId, ?int $teamId = null): RelatedContent`<br>`public function remove(string $sourceType, int $sourceId, string $targetType, int $targetId, ?int $teamId = null): int`<br>`public function related(string $sourceType, int $sourceId, int $limit = 10, array $taxonomy = [], ?int $teamId = null): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [RelatedContent.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-related-content/src/Models/RelatedContent.php) | `source_type`, `source_id`, `target_type`, `target_id`, `mode`, `score`, `explanation`, `taxonomy`, `excluded`, `team_id` |
<!-- layer-implementation-plan:end -->
