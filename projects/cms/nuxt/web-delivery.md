# CMS: Web Delivery Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#web-delivery). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-cms-web-delivery-nuxt`
**Matching domain module:** `cms-web-delivery`
**Application:** CMS
**Source feature:** [Web Delivery](../features/web-delivery.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/web-delivery.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `cms-web-delivery` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Canonical route rendering:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Response metadata:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Cache tags:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Preview mode:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Redirects:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Errors:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Maintenance:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Edge invalidation:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-cms-web-delivery-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `canonical-route-rendering`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `response-metadata`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `cache-tags`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `preview-mode`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `redirects`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `errors`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `maintenance`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `edge-invalidation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `cms-web-delivery` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-cms-nuxt-vue`](https://github.com/liberusoftware/project-cms-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-cms-laravel-api`](https://github.com/liberusoftware/project-cms-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/web-delivery.md)) |
| Capability Nuxt module skeleton | [`module-cms-web-delivery-nuxt`](https://github.com/liberusoftware/module-cms-web-delivery-nuxt) (`@liberusoftware/module-cms-web-delivery-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Canonical route rendering** | Expose composable and Vue 3 component for `canonical route rendering` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/web-delivery.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Response metadata** | Expose composable and Vue 3 component for `response metadata` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/web-delivery.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Cache tags** | Expose composable and Vue 3 component for `cache tags` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/web-delivery.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Preview mode** | Expose composable and Vue 3 component for `preview mode` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/web-delivery.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Redirects** | Expose composable and Vue 3 component for `redirects` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/web-delivery.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Errors** | Expose composable and Vue 3 component for `errors` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/web-delivery.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Maintenance** | Expose composable and Vue 3 component for `maintenance` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/web-delivery.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |
| **Edge invalidation** | Expose composable and Vue 3 component for `edge invalidation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/web-delivery.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-cms-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [DeliveryRouteQuery.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-web-delivery/src/Queries/DeliveryRouteQuery.php) | `public function paginate(int $perPage = 15, string $search = '', ?string $status = null): LengthAwarePaginator`<br>`public function find(string $path): ?DeliveryRoute` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [WebDeliveryService.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-web-delivery/src/Actions/WebDeliveryService.php) | `public function __construct(private EdgeInvalidationRegistry $edge)`<br>`public function registerRoute(array $attributes): DeliveryRoute`<br>`public function updateRoute(DeliveryRoute $route, array $attributes): DeliveryRoute`<br>`public function deleteRoute(DeliveryRoute $route): void`<br>`public function render(string $path, ?string $previewToken = null): DeliveryResult`<br>`public function issuePreviewToken(DeliveryRoute $route): string`<br>`public function setMaintenance(DeliveryRoute $route, bool $enabled): DeliveryRoute`<br>`public function invalidate(array $cacheTags, string $idempotencyKey, ?string $provider = null, int\|string\|null $teamId = null): DeliveryInvalidation` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [DeliveryInvalidation.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-web-delivery/src/Models/DeliveryInvalidation.php) | `idempotency_key`, `cache_tags`, `status`, `provider`, `failure_reason`, `completed_at`, `team_id` |
| [DeliveryRoute.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/cms-web-delivery/src/Models/DeliveryRoute.php) | `path`, `route_type`, `content_type`, `content_id`, `body`, `canonical_url`, `redirect_url`, `redirect_status`, `metadata`, `cache_tags`, `cache_ttl`, `preview_enabled`, `preview_token_hash`, `preview_expires_at`, `maintenance`, `status`, `error_status`, `error_message`, `team_id` |

| Observed API controller | Handler signatures |
| --- | --- |
| [WebDeliveryController.php](https://github.com/liberusoftware/project-cms-laravel-filament/blob/5d91aa9c0a3d4ae6b1cf238b324e9d0a05ba68e7/modules/module-cms-web-delivery-api/src/Http/Controllers/WebDeliveryController.php) | `public function __construct(private DeliveryRouteQuery $routes, private WebDeliveryService $delivery)`<br>`public function index(Request $request): AnonymousResourceCollection`<br>`public function show(string $path): DeliveryRouteResource`<br>`public function create(Request $request): DeliveryRouteResource`<br>`public function update(Request $request, int $route): DeliveryRouteResource`<br>`public function destroy(int $route): JsonResponse`<br>`public function resolve(Request $request): JsonResponse`<br>`public function previewToken(int $route): JsonResponse`<br>`public function invalidate(Request $request): JsonResponse`<br>`public function maintenance(Request $request, int $route): DeliveryRouteResource` |
<!-- layer-implementation-plan:end -->
