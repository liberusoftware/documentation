# Social Network: Social Network Profiles Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#social-network-profiles). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-social-network-social-network-profiles-nuxt`
**Matching domain module:** `social-network-profiles`
**Application:** Social Network
**Source feature:** [Social Network Profiles](../features/social-network-profiles.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/social-network-profiles.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `social-network-profiles` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Handles:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Bios:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Attributes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Avatars:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Verification:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Visibility:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Blocking:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Profile lifecycle:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-social-network-social-network-profiles-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `handles`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `bios`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `attributes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `avatars`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `verification`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `visibility`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `blocking`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `profile-lifecycle`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `social-network-profiles` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-social-network-nuxt-vue`](https://github.com/liberusoftware/project-social-network-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-social-network-laravel-api`](https://github.com/liberusoftware/project-social-network-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/social-network-profiles.md)) |
| Capability Nuxt module skeleton | [`module-social-network-profiles-nuxt`](https://github.com/liberusoftware/module-social-network-profiles-nuxt) (`@liberusoftware/module-social-network-profiles-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Handles** | Expose composable and Vue 3 component for `handles` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social-network-profiles.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Bios** | Expose composable and Vue 3 component for `bios` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social-network-profiles.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Attributes** | Expose composable and Vue 3 component for `attributes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social-network-profiles.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Avatars** | Expose composable and Vue 3 component for `avatars` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social-network-profiles.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Verification** | Expose composable and Vue 3 component for `verification` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social-network-profiles.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Visibility** | Expose composable and Vue 3 component for `visibility` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social-network-profiles.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Blocking** | Expose composable and Vue 3 component for `blocking` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social-network-profiles.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Profile lifecycle** | Expose composable and Vue 3 component for `profile lifecycle` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/social-network-profiles.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [BlockProfile.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/src/Actions/BlockProfile.php) | `public function __construct(private ProfileAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $blocker, Profile $blocked): void` |
| [GetProfile.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/src/Actions/GetProfile.php) | `public function __construct(private ProfileRepository $profiles, private ProfileAuthorizer $authorizer)`<br>`public function byId(string $id): Profile`<br>`public function forUser(int\|string $userId): Profile` |
| [UnblockProfile.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/src/Actions/UnblockProfile.php) | `public function __construct(private ProfileAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $blocker, Profile $blocked): void` |
| [UpdateLifecycleState.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/src/Actions/UpdateLifecycleState.php) | `public function __construct(private Dispatcher $events)`<br>`public function handle(Profile $profile, string $state): Profile` |
| [UpdateProfile.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/src/Actions/UpdateProfile.php) | `public function __construct(private ProfileRepository $profiles, private ProfileAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $profile, array $attributes): Profile` |
| [UpdateVerificationStatus.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/src/Actions/UpdateVerificationStatus.php) | `public function __construct(private Dispatcher $events)`<br>`public function handle(Profile $profile, string $status): Profile` |
| [ProfileAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/src/Contracts/ProfileAuthorizer.php) | `public function view(Profile $profile): void`<br>`public function update(Profile $profile): void`<br>`public function block(Profile $profile, Profile $target): void` |
| [ProfileRepository.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/src/Contracts/ProfileRepository.php) | `public function forUser(int\|string $userId): Profile`<br>`public function find(string $id): Profile` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Profile.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles/src/Models/Profile.php) | `id`, `user_id`, `handle`, `bio`, `attributes`, `avatar_path`, `verification_status`, `visibility`, `lifecycle_state` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ProfilesController.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles-api/src/Http/Controllers/ProfilesController.php) | `public function me(Request $request, GetProfile $get): JsonResponse`<br>`public function show(string $profile, GetProfile $get): JsonResponse`<br>`public function update(Request $request, GetProfile $get, UpdateProfile $update): JsonResponse`<br>`public function block(string $profile, Request $request, GetProfile $get, BlockProfile $block): JsonResponse`<br>`public function unblock(string $profile, Request $request, GetProfile $get, UnblockProfile $unblock): JsonResponse`<br>`public function lifecycle(Request $request, GetProfile $get, UpdateLifecycleState $update): JsonResponse`<br>`public function verification(string $profile, Request $request, GetProfile $get, UpdateVerificationStatus $update): JsonResponse` |

**Observed route declarations:**

[modules/social-network-profiles-api/routes/api.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-profiles-api/routes/api.php)

```php
Route::prefix('api/v1/social-network/profiles')->middleware(['auth:sanctum', 'throttle:60,1'])->name('social-network.profiles.api.')->group(function (): void {
Route::get('/me', [ProfilesController::class, 'me'])->name('me');
Route::patch('/me', [ProfilesController::class, 'update'])->name('update');
Route::post('/me/blocks/{profile}', [ProfilesController::class, 'block'])->name('block');
Route::delete('/me/blocks/{profile}', [ProfilesController::class, 'unblock'])->name('unblock');
Route::patch('/me/lifecycle', [ProfilesController::class, 'lifecycle'])->name('lifecycle');
Route::patch('/{profile}/verification', [ProfilesController::class, 'verification'])->name('verification');
Route::get('/{profile}', [ProfilesController::class, 'show'])->name('show');
```
<!-- layer-implementation-plan:end -->
