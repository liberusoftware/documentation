# Social Network: Social Network Communities Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#social-network-communities). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-social-network-social-network-communities-nuxt`
**Matching domain module:** `social-network-communities`
**Application:** Social Network
**Source feature:** [Social Network Communities](../features/social-network-communities.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/social-network-communities.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `social-network-communities` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Groups/pages:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Memberships:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Roles:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Rules:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Feeds:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Files:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Questions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Moderation:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-social-network-social-network-communities-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `groups-pages`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `memberships`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `roles`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `rules`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `feeds`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `files`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `questions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `moderation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `social-network-communities` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-social-network-nuxt-vue`](https://github.com/liberusoftware/project-social-network-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-social-network-laravel-api`](https://github.com/liberusoftware/project-social-network-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/social-network-communities.md)) |
| Capability Nuxt module skeleton | [`module-social-network-communities-nuxt`](https://github.com/liberusoftware/module-social-network-communities-nuxt) (`@liberusoftware/module-social-network-communities-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Groups/pages** | Expose composable and Vue 3 component for `groups/pages` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social-network-communities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Memberships** | Expose composable and Vue 3 component for `memberships` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social-network-communities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Roles** | Expose composable and Vue 3 component for `roles` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social-network-communities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Rules** | Expose composable and Vue 3 component for `rules` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social-network-communities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Feeds** | Expose composable and Vue 3 component for `feeds` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social-network-communities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Files** | Expose composable and Vue 3 component for `files` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social-network-communities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Questions** | Expose composable and Vue 3 component for `questions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social-network-communities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Moderation** | Expose composable and Vue 3 component for `moderation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social-network-communities.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCommunity.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-communities/src/Actions/CreateCommunity.php) | `public function __construct(private CommunityAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $owner, array $attributes): Community` |
| [JoinCommunity.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-communities/src/Actions/JoinCommunity.php) | `public function __construct(private CommunityAuthorizer $authorizer)`<br>`public function handle(Profile $member, Community $community): Membership` |
| [LeaveCommunity.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-communities/src/Actions/LeaveCommunity.php) | `public function handle(Profile $member, Community $community): void` |
| [ListCommunities.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-communities/src/Actions/ListCommunities.php) | `public function handle(Profile $viewer, int $limit = 25): Collection` |
| [CommunityAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-communities/src/Contracts/CommunityAuthorizer.php) | `public function create(Profile $owner): void`<br>`public function join(Profile $member): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Community.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-communities/src/Models/Community.php) | `id`, `owner_profile_id`, `name`, `slug`, `description`, `visibility`, `rules` |
| [Membership.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-communities/src/Models/Membership.php) | `community_id`, `profile_id`, `role`, `status` |

| Observed API controller | Handler signatures |
| --- | --- |
| [CommunitiesController.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-communities-api/src/Http/Controllers/CommunitiesController.php) | `public function store(Request $request, GetProfile $get, CreateCommunity $create): JsonResponse`<br>`public function index(Request $request, GetProfile $get, ListCommunities $list): JsonResponse`<br>`public function join(string $community, Request $request, GetProfile $get, JoinCommunity $join): JsonResponse`<br>`public function leave(string $community, Request $request, GetProfile $get, LeaveCommunity $leave): JsonResponse` |

**Observed route declarations:**

[modules/social-network-communities-api/routes/api.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-communities-api/routes/api.php)

```php
Route::prefix('api/v1/social-network/communities')->middleware(['auth:sanctum', 'throttle:60,1'])->name('social-network.communities.api.')->group(function (): void {
Route::get('/', [CommunitiesController::class, 'index'])->name('index');
Route::post('/', [CommunitiesController::class, 'store'])->name('store');
Route::post('/{community}/join', [CommunitiesController::class, 'join'])->name('join');
Route::delete('/{community}/leave', [CommunitiesController::class, 'leave'])->name('leave');
```
<!-- layer-implementation-plan:end -->
