# Social Network: Social Graph Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#social-graph). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-social-network-social-graph-nuxt`
**Matching domain module:** `social-network-social-graph`
**Application:** Social Network
**Source feature:** [Social Graph](../features/social-graph.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/social-graph.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `social-network-social-graph` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Follow/friend models:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Requests:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Lists:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Suggestions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Blocks:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Relationship visibility:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-social-network-social-graph-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `follow-friend-models`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `requests`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `lists`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `suggestions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `blocks`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `relationship-visibility`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `social-network-social-graph` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-social-network-nuxt-vue`](https://github.com/liberusoftware/project-social-network-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-social-network-laravel-api`](https://github.com/liberusoftware/project-social-network-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/social-graph.md)) |
| Capability Nuxt module skeleton | [`module-social-network-social-graph-nuxt`](https://github.com/liberusoftware/module-social-network-social-graph-nuxt) (`@liberusoftware/module-social-network-social-graph-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Follow/friend models** | Expose composable and Vue 3 component for `follow/friend models` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social-graph.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Requests** | Expose composable and Vue 3 component for `requests` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social-graph.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Lists** | Expose composable and Vue 3 component for `lists` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social-graph.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Suggestions** | Expose composable and Vue 3 component for `suggestions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social-graph.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Blocks** | Expose composable and Vue 3 component for `blocks` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social-graph.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Relationship visibility** | Expose composable and Vue 3 component for `relationship visibility` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social-graph.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AcceptFriendship.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Actions/AcceptFriendship.php) | `public function handle(Profile $actor, Relationship $relationship): Relationship` |
| [AddProfileToList.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Actions/AddProfileToList.php) | `public function __construct(private GraphAuthorizer $authorizer)`<br>`public function handle(Profile $owner, GraphList $list, Profile $profile): GraphList` |
| [BlockProfile.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Actions/BlockProfile.php) | `public function __construct(private GraphAuthorizer $authorizer)`<br>`public function handle(Profile $source, Profile $target): Block` |
| [CancelFriendship.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Actions/CancelFriendship.php) | `public function handle(Profile $actor, Relationship $relationship): Relationship` |
| [CreateList.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Actions/CreateList.php) | `public function __construct(private GraphAuthorizer $authorizer)`<br>`public function handle(Profile $owner, array $attributes): GraphList` |
| [CreateRelationship.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Actions/CreateRelationship.php) | `public function __construct(private GraphAuthorizer $authorizer, private Dispatcher $events)`<br>`public function follow(Profile $source, Profile $target): Relationship`<br>`public function friend(Profile $source, Profile $target): Relationship` |
| [ListOwnedBlocks.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Actions/ListOwnedBlocks.php) | `public function __construct(private GraphAuthorizer $authorizer)`<br>`public function handle(Profile $owner): Collection` |
| [ListOwnedLists.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Actions/ListOwnedLists.php) | `public function __construct(private GraphAuthorizer $authorizer)`<br>`public function handle(Profile $owner): Collection` |
| [ListRelationships.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Actions/ListRelationships.php) | `public function __construct(private GraphAuthorizer $authorizer)`<br>`public function handle(Profile $viewer, ?string $type = null, ?string $status = null, int $limit = 100): Collection` |
| [RejectFriendship.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Actions/RejectFriendship.php) | `public function handle(Profile $actor, Relationship $relationship): Relationship` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Block.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Models/Block.php) | `id`, `source_profile_id`, `target_profile_id` |
| [GraphList.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Models/GraphList.php) | `id`, `owner_profile_id`, `name`, `visibility` |
| [Relationship.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph/src/Models/Relationship.php) | `id`, `source_profile_id`, `target_profile_id`, `relationship_type`, `status`, `visibility` |

| Observed API controller | Handler signatures |
| --- | --- |
| [SocialGraphController.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph-api/src/Http/Controllers/SocialGraphController.php) | `public function follow(string $profile, Request $request, GetProfile $get, CreateRelationship $create): JsonResponse`<br>`public function friend(string $profile, Request $request, GetProfile $get, CreateRelationship $create): JsonResponse`<br>`public function index(Request $request, GetProfile $get, ListRelationships $list): JsonResponse`<br>`public function suggestions(Request $request, GetProfile $get, SuggestProfiles $suggest): JsonResponse`<br>`public function block(string $profile, Request $request, GetProfile $get, BlockProfile $block): JsonResponse`<br>`public function unblock(string $profile, Request $request, GetProfile $get, UnblockProfile $unblock): JsonResponse`<br>`public function accept(Relationship $relationship, Request $request, GetProfile $get, AcceptFriendship $accept): JsonResponse`<br>`public function reject(Relationship $relationship, Request $request, GetProfile $get, RejectFriendship $reject): JsonResponse`<br>`public function cancel(Relationship $relationship, Request $request, GetProfile $get, CancelFriendship $cancel): JsonResponse`<br>`public function visibility(Relationship $relationship, Request $request, GetProfile $get, UpdateRelationshipVisibility $update): JsonResponse`<br>`public function lists(Request $request, GetProfile $get, ListOwnedLists $lists): JsonResponse`<br>`public function createList(Request $request, GetProfile $get, CreateList $create): JsonResponse`<br>`public function addListMember(GraphList $list, string $profile, Request $request, GetProfile $get, AddProfileToList $add): JsonResponse`<br>`public function removeListMember(GraphList $list, string $profile, Request $request, GetProfile $get, RemoveProfileFromList $remove): JsonResponse` |

**Observed route declarations:**

[modules/social-network-social-graph-api/routes/api.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-social-graph-api/routes/api.php)

```php
Route::prefix('api/v1/social-network/social-graph')->middleware(['auth:sanctum', 'throttle:60,1'])->name('social-network.social-graph.api.')->group(function (): void {
Route::post('/me/following/{profile}', [SocialGraphController::class, 'follow'])->name('follow');
Route::post('/me/friend-requests/{profile}', [SocialGraphController::class, 'friend'])->name('friend');
Route::get('/me/relationships', [SocialGraphController::class, 'index'])->name('index');
Route::get('/me/suggestions', [SocialGraphController::class, 'suggestions'])->name('suggestions');
Route::put('/me/blocks/{profile}', [SocialGraphController::class, 'block'])->name('block');
Route::delete('/me/blocks/{profile}', [SocialGraphController::class, 'unblock'])->name('unblock');
Route::post('/me/relationships/{relationship}/accept', [SocialGraphController::class, 'accept'])->name('accept');
Route::post('/me/relationships/{relationship}/reject', [SocialGraphController::class, 'reject'])->name('reject');
Route::post('/me/relationships/{relationship}/cancel', [SocialGraphController::class, 'cancel'])->name('cancel');
Route::patch('/me/relationships/{relationship}/visibility', [SocialGraphController::class, 'visibility'])->name('visibility');
Route::get('/me/lists', [SocialGraphController::class, 'lists'])->name('lists');
Route::post('/me/lists', [SocialGraphController::class, 'createList'])->name('lists.create');
Route::put('/me/lists/{list}/profiles/{profile}', [SocialGraphController::class, 'addListMember'])->name('lists.profiles.add');
Route::delete('/me/lists/{list}/profiles/{profile}', [SocialGraphController::class, 'removeListMember'])->name('lists.profiles.remove');
```
<!-- layer-implementation-plan:end -->
