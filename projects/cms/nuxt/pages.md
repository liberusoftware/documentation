# CMS: Pages Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#pages). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-cms-pages-nuxt`
**Matching domain module:** `cms-pages`
**Application:** CMS
**Source feature:** [Pages](../features/pages.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/pages.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `cms-pages` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Hierarchy:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Slugs:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Routing:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Home/error pages:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Aliases:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Redirects:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Breadcrumbs:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Templates:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Previews:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-cms-pages-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `hierarchy`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `slugs`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `routing`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `home-error-pages`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `aliases`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `redirects`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `breadcrumbs`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `templates`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `previews`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `cms-pages` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-cms-nuxt-vue`](https://github.com/liberusoftware/project-cms-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/pages.md)) |
| Capability Nuxt module skeleton | [`module-cms-pages-nuxt`](https://github.com/liberusoftware/module-cms-pages-nuxt) (`@liberusoftware/module-cms-pages-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Hierarchy** | Expose composable and Vue 3 component for `hierarchy` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/pages.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Slugs** | Expose composable and Vue 3 component for `slugs` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/pages.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Routing** | Expose composable and Vue 3 component for `routing` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/pages.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Home/error pages** | Expose composable and Vue 3 component for `home/error pages` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/pages.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Aliases** | Expose composable and Vue 3 component for `aliases` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/pages.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Redirects** | Expose composable and Vue 3 component for `redirects` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/pages.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Breadcrumbs** | Expose composable and Vue 3 component for `breadcrumbs` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/pages.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Templates** | Expose composable and Vue 3 component for `templates` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/pages.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Previews** | Expose composable and Vue 3 component for `previews` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/pages.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [PageTreeQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/src/Queries/PageTreeQuery.php) | `public function roots(string $search = ''): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [PageRepositoryInterface.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/src/Contracts/PageRepositoryInterface.php) | `public function find(int $id): ?Page`<br>`public function findBySlug(string $slug): ?Page`<br>`public function findByPath(string $path): ?Page`<br>`public function redirectForPath(string $path): ?PageRedirect`<br>`public function published(): array`<br>`public function roots(): array`<br>`public function search(string $query, int $limit): array` |
| [PageRoutingService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/src/Services/PageRoutingService.php) | `public function addAlias(Page $page, string $path): PageAlias`<br>`public function createRedirect(array $attributes): PageRedirect`<br>`public function updateRedirect(PageRedirect $redirect, array $attributes): PageRedirect`<br>`public function deleteRedirect(PageRedirect $redirect): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Page.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/src/Models/Page.php) | `title`, `slug`, `content`, `excerpt`, `template`, `status`, `published_at`, `parent_id`, `featured_media_id`, `team_id`, `user_id`, `is_home`, `is_error` |
| [PageAlias.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/src/Models/PageAlias.php) | `page_id`, `path`, `team_id` |
| [PageRedirect.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/src/Models/PageRedirect.php) | `from_path`, `to_path`, `status_code`, `active`, `team_id` |

| Observed API controller | Handler signatures |
| --- | --- |
| [PageApiController.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/src/Http/Controllers/PageApiController.php) | `public function __construct(private PageRepositoryInterface $pages)`<br>`public function index(): AnonymousResourceCollection`<br>`public function show(string $slug): PageResource` |
| [PageWriteController.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-pages/src/Http/Controllers/PageWriteController.php) | `public function __construct(private PageRepositoryInterface $pages)`<br>`public function store(StorePageRequest $request): JsonResponse`<br>`public function update(UpdatePageRequest $request, int $id): PageResource`<br>`public function destroy(int $id): Response` |
| [PageRoutingController.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-pages-api/src/Http/Controllers/PageRoutingController.php) | `public function __construct(private PageRoutingService $routing)`<br>`public function alias(Request $request, int $id): JsonResponse`<br>`public function redirect(Request $request): JsonResponse`<br>`public function deleteRedirect(int $id): JsonResponse` |
<!-- layer-implementation-plan:end -->
