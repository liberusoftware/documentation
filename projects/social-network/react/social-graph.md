# Social Network: Social Graph React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#social-graph). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-social-network-social-graph-react-inertia`
**Matching domain module:** `social-network-social-graph`
**Application:** Social Network
**Source feature:** [Social Graph](../features/social-graph.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/social-graph.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Follow/friend models:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Requests:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Lists:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Suggestions:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Blocks:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Relationship visibility:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-social-network-social-graph-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `follow-friend-models`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `requests`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `lists`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `suggestions`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `blocks`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `relationship-visibility`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

## 4. API contract and Inertia consumption

<!-- inertia-transport:start -->
### Inertia transport boundary

Use Laravel-owned Inertia page/command routes for visits and forms. The controller can invoke the module's public application actions in the same host or use a deliberate API adapter, then return an Inertia page/redirect response. A bare REST JSON resource response is not an Inertia page. Keep authoritative domain authorization and validation in the owning boundary for either path.

Independent API consumers and Next.js use their reviewed HTTP/session integration. Share DTOs and framework-independent UI primitives; keep Inertia page props, visits, form errors and redirects in the Inertia wrapper. Do not introduce loopback HTTP solely to reuse a public action inside the same Laravel host.

See the [Inertia standard](../../../standards/INERTIA.md), [request lifecycle](https://inertiajs.com/docs/v3/core-concepts/how-it-works) and [redirect behavior](https://inertiajs.com/docs/v3/the-basics/redirects).
<!-- inertia-transport:end -->

- Reuse the matching public application/API contracts. For HTTP consumption, use its documented schemas, routes, authentication, permissions, tenant context, errors and operation semantics; Inertia visits still require an Inertia response.
- Keep a typed module-local API client and hooks boundary; use Inertia visits for page transitions and `useForm`/`router` for mutations, preserving server validation and redirect semantics.
- Forward Sanctum cookies or approved authorization headers through a controlled first-party boundary; never persist long-lived tokens in browser storage or expose secrets in page props.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, SSR hydration where enabled, and minimal-host installation tests.
- Test observable behavior with TypeScript, ESLint, Vitest, React Testing Library, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `social-network-social-graph` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-social-network-laravel-inertia-react`](https://github.com/liberusoftware/project-social-network-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-social-network-social-graph-react-inertia`](https://github.com/liberusoftware/module-social-network-social-graph-react-inertia) (`@liberusoftware/module-social-network-social-graph-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/social-graph.md) · [Core plan](../core/social-graph.md) · [API plan](../api/social-graph.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Follow/friend models** | Render `follow/friend models` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Requests** | Render `requests` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Lists** | Render `lists` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Suggestions** | Render `suggestions` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Blocks** | Render `blocks` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Relationship visibility** | Render `relationship visibility` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

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
