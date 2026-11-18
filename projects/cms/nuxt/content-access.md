# CMS: Content Access Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#content-access). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-cms-content-access-nuxt`
**Matching domain module:** `cms-content-access`
**Application:** CMS
**Source feature:** [Content Access](../features/content-access.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/content-access.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `cms-content-access` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Per-site/type/record/field visibility:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Audience rules:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Scheduled access:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Private links:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Content partitioning:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Preview authorization:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-cms-content-access-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `per-site-type-record-field-visibility`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `audience-rules`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `scheduled-access`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `private-links`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `content-partitioning`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `preview-authorization`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `cms-content-access` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-cms-nuxt-vue`](https://github.com/liberusoftware/project-cms-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/content-access.md)) |
| Capability Nuxt module skeleton | [`module-cms-content-access-nuxt`](https://github.com/liberusoftware/module-cms-content-access-nuxt) (`@liberusoftware/module-cms-content-access-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Per-site/type/record/field visibility** | Expose composable and Vue 3 component for `per-site/type/record/field visibility` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/content-access.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Audience rules** | Expose composable and Vue 3 component for `audience rules` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/content-access.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Scheduled access** | Expose composable and Vue 3 component for `scheduled access` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/content-access.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Private links** | Expose composable and Vue 3 component for `private links` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/content-access.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Content partitioning** | Expose composable and Vue 3 component for `content partitioning` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/content-access.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Preview authorization** | Expose composable and Vue 3 component for `preview authorization` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/content-access.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ContentAccessService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-access/src/Services/ContentAccessService.php) | `public function rule(string $subjectType, string $subjectKey, array $data = [], ?int $teamId = null): AccessRule`<br>`public function canAccess(string $subjectType, string $subjectKey, ?int $teamId, array $audiences = [], bool $preview = false, ?string $privateToken = null): bool`<br>`public function createPrivateLink(string $subjectType, string $subjectKey, ?int $teamId, ?int $maxUses = null): string`<br>`public function consumePrivateLink(string $token, string $subjectType, string $subjectKey, ?int $teamId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AccessRule.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-access/src/Models/AccessRule.php) | `team_id`, `subject_type`, `subject_key`, `visibility`, `audiences`, `fields`, `available_from`, `available_until`, `preview_allowed` |
| [PrivateLink.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-content-access/src/Models/PrivateLink.php) | `team_id`, `token_hash`, `subject_type`, `subject_key`, `expires_at`, `uses`, `max_uses`, `revoked_at` |
<!-- layer-implementation-plan:end -->
