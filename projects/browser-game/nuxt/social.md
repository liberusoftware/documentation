# Browser Game: Social Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#social). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-browser-game-social-nuxt`
**Matching domain module:** `browser-game-social`
**Application:** Browser Game
**Source feature:** [Social](../features/social.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/social.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `browser-game-social` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Friends:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Parties:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Chat:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Mail:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Guilds:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Alliances:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Permissions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Activity:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reporting:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-browser-game-social-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `friends`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `parties`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `chat`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `mail`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `guilds`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `alliances`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `permissions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `activity`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `reporting`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `browser-game-social` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-browser-game-nuxt-vue`](https://github.com/liberusoftware/project-browser-game-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-browser-game-laravel-api`](https://github.com/liberusoftware/project-browser-game-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/social.md)) |
| Capability Nuxt module skeleton | [`module-browser-game-social-nuxt`](https://github.com/liberusoftware/module-browser-game-social-nuxt) (`@liberusoftware/module-browser-game-social-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Friends** | Expose composable and Vue 3 component for `friends` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Parties** | Expose composable and Vue 3 component for `parties` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Chat** | Expose composable and Vue 3 component for `chat` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Mail** | Expose composable and Vue 3 component for `mail` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Guilds** | Expose composable and Vue 3 component for `guilds` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Alliances** | Expose composable and Vue 3 component for `alliances` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Permissions** | Expose composable and Vue 3 component for `permissions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Activity** | Expose composable and Vue 3 component for `activity` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Reporting** | Expose composable and Vue 3 component for `reporting` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [SocialQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social/src/Queries/SocialQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SocialActivity.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social/src/Models/SocialActivity.php) | No literal fillable array detected; inspect the model and API schema. |
| [SocialMembership.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social/src/Models/SocialMembership.php) | No literal fillable array detected; inspect the model and API schema. |
| [SocialRecord.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social/src/Models/SocialRecord.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [SocialController.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social-api/src/Http/Controllers/SocialController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request): JsonResponse`<br>`public function friendRequest(Request $request): JsonResponse`<br>`public function respondToFriendRequest(Request $request, SocialRecord $social): JsonResponse`<br>`public function createGroup(Request $request, string $kind): JsonResponse`<br>`public function mail(Request $request): JsonResponse`<br>`public function member(Request $request, SocialRecord $social): JsonResponse`<br>`public function message(Request $request, SocialRecord $social): JsonResponse`<br>`public function report(Request $request): JsonResponse`<br>`public function permissions(Request $request, SocialRecord $social): JsonResponse`<br>`public function activity(Request $request): JsonResponse`<br>`public function show(Request $request, SocialRecord $social): JsonResponse` |

**Observed route declarations:**

[modules/browser-game-social-api/routes/api.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-social-api/routes/api.php)

```php
Route::prefix('api/v1/browser-game/social')->middleware(['api', 'auth:sanctum', 'throttle:api'])->group(function (): void {
Route::get('/', [SocialController::class, 'index'])->name('browser-game.social.index');
Route::post('/', [SocialController::class, 'store'])->name('browser-game.social.store');
Route::post('/friends', [SocialController::class, 'friendRequest'])->name('browser-game.social.friends.create');
Route::post('/groups/{kind}', [SocialController::class, 'createGroup'])->whereIn('kind', ['party', 'chat', 'guild', 'alliance'])->name('browser-game.social.groups.create');
Route::post('/mail', [SocialController::class, 'mail'])->name('browser-game.social.mail.create');
Route::get('/activity', [SocialController::class, 'activity'])->name('browser-game.social.activity');
Route::post('/{social}/members', [SocialController::class, 'member'])->name('browser-game.social.member');
Route::patch('/{social}/permissions', [SocialController::class, 'permissions'])->name('browser-game.social.permissions');
Route::patch('/{social}/friend-response', [SocialController::class, 'respondToFriendRequest'])->name('browser-game.social.friends.respond');
Route::post('/{social}/messages', [SocialController::class, 'message'])->name('browser-game.social.message');
Route::post('/reports', [SocialController::class, 'report'])->name('browser-game.social.report');
Route::get('/{social}', [SocialController::class, 'show'])->name('browser-game.social.show');
```
<!-- layer-implementation-plan:end -->
