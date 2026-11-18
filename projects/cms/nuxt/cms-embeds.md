# CMS: Cms Embeds Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-embeds). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-cms-cms-embeds-nuxt`
**Matching domain module:** `cms-embeds`
**Application:** CMS
**Source feature:** [Cms Embeds](../features/cms-embeds.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/cms-embeds.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `cms-embeds` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Provider allowlists:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Normalized embed records:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Privacy modes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Consent:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Responsive rendering:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Fallback:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Provider adapters:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-cms-cms-embeds-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `provider-allowlists`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `normalized-embed-records`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `privacy-modes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `consent`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `responsive-rendering`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `fallback`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `provider-adapters`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `cms-embeds` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-cms-nuxt-vue`](https://github.com/liberusoftware/project-cms-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/cms-embeds.md)) |
| Capability Nuxt module skeleton | [`module-cms-embeds-nuxt`](https://github.com/liberusoftware/module-cms-embeds-nuxt) (`@liberusoftware/module-cms-embeds-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Provider allowlists** | Expose composable and Vue 3 component for `provider allowlists` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-embeds.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Normalized embed records** | Expose composable and Vue 3 component for `normalized embed records` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-embeds.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Privacy modes** | Expose composable and Vue 3 component for `privacy modes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-embeds.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Consent** | Expose composable and Vue 3 component for `consent` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-embeds.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Responsive rendering** | Expose composable and Vue 3 component for `responsive rendering` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-embeds.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Fallback** | Expose composable and Vue 3 component for `fallback` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-embeds.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Provider adapters** | Expose composable and Vue 3 component for `provider adapters` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-embeds.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [EmbedsQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-embeds/src/Queries/EmbedsQuery.php) | `public function list(int $perPage = 15, string $search = ''): mixed`<br>`public function find(int $id): ?Embed` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [EmbedsService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-embeds/src/Services/EmbedsService.php) | `public function provider(array $a, ?int $teamId = null): Provider`<br>`public function embed(array $a, ?int $teamId = null): Embed`<br>`public function publish(Embed $e): Embed`<br>`public function render(Embed $e, bool $consented = false): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Embed.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-embeds/src/Models/Embed.php) | No literal fillable array detected; inspect the model and API schema. |
| [Provider.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-embeds/src/Models/Provider.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
