# Social Network: Social Network Engagement Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#social-network-engagement). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-social-network-social-network-engagement-nuxt`
**Matching domain module:** `social-network-engagement`
**Application:** Social Network
**Source feature:** [Social Network Engagement](../features/social-network-engagement.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/social-network-engagement.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `social-network-engagement` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Reactions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Comments:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Replies:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Sharing:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Bookmarks:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Counters:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Abuse limits:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-social-network-social-network-engagement-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `reactions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `comments`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `replies`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `sharing`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `bookmarks`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `counters`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `abuse-limits`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `social-network-engagement` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-social-network-nuxt-vue`](https://github.com/liberusoftware/project-social-network-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-social-network-laravel-api`](https://github.com/liberusoftware/project-social-network-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/social-network-engagement.md)) |
| Capability Nuxt module skeleton | [`module-social-network-engagement-nuxt`](https://github.com/liberusoftware/module-social-network-engagement-nuxt) (`@liberusoftware/module-social-network-engagement-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Reactions** | Expose composable and Vue 3 component for `reactions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social-network-engagement.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Comments** | Expose composable and Vue 3 component for `comments` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social-network-engagement.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Replies** | Expose composable and Vue 3 component for `replies` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social-network-engagement.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Sharing** | Expose composable and Vue 3 component for `sharing` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social-network-engagement.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Bookmarks** | Expose composable and Vue 3 component for `bookmarks` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social-network-engagement.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Counters** | Expose composable and Vue 3 component for `counters` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social-network-engagement.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Abuse limits** | Expose composable and Vue 3 component for `abuse limits` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social-network-engagement.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateEngagement.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-engagement/src/Actions/CreateEngagement.php) | `public function __construct(private EngagementAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $actor, array $attributes): Engagement` |
| [DeleteEngagement.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-engagement/src/Actions/DeleteEngagement.php) | `public function __construct(private EngagementAuthorizer $authorizer)`<br>`public function handle(Profile $actor, Engagement $engagement): void` |
| [ListEngagements.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-engagement/src/Actions/ListEngagements.php) | `public function handle(string $targetType, string $targetId, ?string $kind = null, int $limit = 50): Collection`<br>`public function count(string $targetType, string $targetId, ?string $kind = null): int` |
| [UpdateEngagement.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-engagement/src/Actions/UpdateEngagement.php) | `public function handle(Profile $actor, Engagement $engagement, string $body): Engagement` |
| [EngagementAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-engagement/src/Contracts/EngagementAuthorizer.php) | `public function create(Profile $actor): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Engagement.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-engagement/src/Models/Engagement.php) | `id`, `actor_profile_id`, `target_type`, `target_id`, `kind`, `reaction_type`, `body` |

| Observed API controller | Handler signatures |
| --- | --- |
| [EngagementController.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-engagement-api/src/Http/Controllers/EngagementController.php) | `public function store(Request $request, GetProfile $get, CreateEngagement $create): JsonResponse`<br>`public function destroy(string $engagement, Request $request, GetProfile $get, DeleteEngagement $delete): JsonResponse`<br>`public function index(string $targetType, string $targetId, Request $request, ListEngagements $list): JsonResponse`<br>`public function update(string $engagement, Request $request, GetProfile $get, UpdateEngagement $update): JsonResponse` |

**Observed route declarations:**

[modules/social-network-engagement-api/routes/api.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-engagement-api/routes/api.php)

```php
Route::prefix('api/v1/social-network/engagement')->middleware(['auth:sanctum', 'throttle:60,1'])->name('social-network.engagement.api.')->group(function (): void {
Route::post('/', [EngagementController::class, 'store'])->name('store');
Route::get('/target/{targetType}/{targetId}', [EngagementController::class, 'index'])->name('index');
Route::patch('/{engagement}', [EngagementController::class, 'update'])->name('update');
Route::delete('/{engagement}', [EngagementController::class, 'destroy'])->name('destroy');
```
<!-- layer-implementation-plan:end -->
