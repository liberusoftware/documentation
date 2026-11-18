# CMS: Cms Views And Query Builder Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#cms-views-and-query-builder). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-cms-cms-views-and-query-builder-nuxt`
**Matching domain module:** `cms-views-and-query-builder`
**Application:** CMS
**Source feature:** [Cms Views And Query Builder](../features/cms-views-and-query-builder.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/cms-views-and-query-builder.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `cms-views-and-query-builder` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Permission-safe listings from content/fields/relationships with filters:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Sorting:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Grouping:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Exposed filters:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Pagination:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Feeds:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Displays:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-cms-cms-views-and-query-builder-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `permission-safe-listings-from-content-fields-relationships-with-filters`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `sorting`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `grouping`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `exposed-filters`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `pagination`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `feeds`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `displays`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `cms-views-and-query-builder` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-cms-nuxt-vue`](https://github.com/liberusoftware/project-cms-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/cms-views-and-query-builder.md)) |
| Capability Nuxt module skeleton | [`module-cms-views-and-query-builder-nuxt`](https://github.com/liberusoftware/module-cms-views-and-query-builder-nuxt) (`@liberusoftware/module-cms-views-and-query-builder-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Permission-safe listings from content/fields/relationships with filters** | Expose composable and Vue 3 component for `permission-safe listings from content/fields/relationships with filters` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-views-and-query-builder.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Sorting** | Expose composable and Vue 3 component for `sorting` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-views-and-query-builder.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Grouping** | Expose composable and Vue 3 component for `grouping` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-views-and-query-builder.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Exposed filters** | Expose composable and Vue 3 component for `exposed filters` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-views-and-query-builder.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Pagination** | Expose composable and Vue 3 component for `pagination` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-views-and-query-builder.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Feeds** | Expose composable and Vue 3 component for `feeds` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-views-and-query-builder.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Displays** | Expose composable and Vue 3 component for `displays` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/cms-views-and-query-builder.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListingQueryService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-views-and-query-builder/src/Queries/ListingQueryService.php) | `public function execute(ViewDefinition $view, int $perPage = 15, array $input = []): LengthAwarePaginator` |
| [ViewDefinitionQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-views-and-query-builder/src/Queries/ViewDefinitionQuery.php) | `public function list(int $perPage = 15, string $search = ''): LengthAwarePaginator`<br>`public function find(string $slug): ?ViewDefinition`<br>`public function publishedList(int $perPage = 15, string $search = ''): LengthAwarePaginator`<br>`public function findPublished(string $slug): ?ViewDefinition` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ViewDefinitionMutationService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-views-and-query-builder/src/Actions/ViewDefinitionMutationService.php) | `public function create(array $attributes): ViewDefinition`<br>`public function update(ViewDefinition $view, array $attributes): ViewDefinition` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ViewDefinition.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-views-and-query-builder/src/Models/ViewDefinition.php) | `name`, `slug`, `source`, `description`, `definition`, `visibility`, `status`, `published_at`, `user_id`, `team_id` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ViewsAndQueryBuilderController.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-views-and-query-builder-api/src/Http/Controllers/ViewsAndQueryBuilderController.php) | `public function __construct(private ViewDefinitionQuery $views, private ListingQueryService $listings)`<br>`public function index(Request $request): AnonymousResourceCollection`<br>`public function show(string $slug): ViewDefinitionResource`<br>`public function execute(Request $request, string $slug): AnonymousResourceCollection` |
<!-- layer-implementation-plan:end -->
