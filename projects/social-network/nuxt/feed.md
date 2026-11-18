# Social Network: Feed Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#feed). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-social-network-feed-nuxt`
**Matching domain module:** `social-network-feed`
**Application:** Social Network
**Source feature:** [Feed](../features/feed.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/feed.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `social-network-feed` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Candidate generation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Ranking:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Chronological mode:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Filters:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Pagination:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Explanations:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Controls:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-social-network-feed-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `candidate-generation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `ranking`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `chronological-mode`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `filters`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `pagination`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `explanations`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `controls`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `social-network-feed` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-social-network-nuxt-vue`](https://github.com/liberusoftware/project-social-network-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-social-network-laravel-api`](https://github.com/liberusoftware/project-social-network-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/feed.md)) |
| Capability Nuxt module skeleton | [`module-social-network-feed-nuxt`](https://github.com/liberusoftware/module-social-network-feed-nuxt) (`@liberusoftware/module-social-network-feed-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Candidate generation** | Expose composable and Vue 3 component for `candidate generation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/feed.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Ranking** | Expose composable and Vue 3 component for `ranking` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/feed.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Chronological mode** | Expose composable and Vue 3 component for `chronological mode` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/feed.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Filters** | Expose composable and Vue 3 component for `filters` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/feed.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Pagination** | Expose composable and Vue 3 component for `pagination` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/feed.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Explanations** | Expose composable and Vue 3 component for `explanations` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/feed.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Controls** | Expose composable and Vue 3 component for `controls` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/feed.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddFeedEntry.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-feed/src/Actions/AddFeedEntry.php) | `public function __construct(private Dispatcher $events, private FeedAuthorizer $authorizer)`<br>`public function handle(Profile $viewer, string $itemType, string $itemId, float $rank = 0): FeedEntry` |
| [GetFeed.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-feed/src/Actions/GetFeed.php) | `public function __construct(private FeedAuthorizer $authorizer)`<br>`public function handle(Profile $viewer, int $limit = 20, ?string $after = null): Collection` |
| [UpdateFeedControls.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-feed/src/Actions/UpdateFeedControls.php) | `public function __construct(private FeedAuthorizer $authorizer)`<br>`public function handle(Profile $profile, array $data): array` |
| [FeedAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-feed/src/Contracts/FeedAuthorizer.php) | `public function view(Profile $viewer): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [FeedEntry.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-feed/src/Models/FeedEntry.php) | `id`, `viewer_profile_id`, `item_type`, `item_id`, `rank`, `visible_at` |

| Observed API controller | Handler signatures |
| --- | --- |
| [FeedController.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-feed-api/src/Http/Controllers/FeedController.php) | `public function index(Request $request, GetProfile $get, GetFeed $feed): JsonResponse`<br>`public function controls(Request $request, GetProfile $get, UpdateFeedControls $update): JsonResponse` |

**Observed route declarations:**

[modules/social-network-feed-api/routes/api.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-feed-api/routes/api.php)

```php
Route::prefix('api/v1/social-network/feed')->middleware(['auth:sanctum', 'throttle:60,1'])->name('social-network.feed.api.')->group(function (): void {
Route::get('/', [FeedController::class, 'index'])->name('index');
Route::patch('/controls', [FeedController::class, 'controls'])->name('controls');
```
<!-- layer-implementation-plan:end -->
