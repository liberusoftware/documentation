# Social Network: Media Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#media). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-social-network-media-nuxt`
**Matching domain module:** `social-network-media`
**Application:** Social Network
**Source feature:** [Media](../features/media.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/media.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `social-network-media` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Images:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Video:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Audio:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Files:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Processing:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Alt text:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Captions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Rights:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Delivery:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-social-network-media-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `images`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `video`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `audio`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `files`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `processing`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `alt-text`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `captions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `rights`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `delivery`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `social-network-media` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-social-network-nuxt-vue`](https://github.com/liberusoftware/project-social-network-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-social-network-laravel-api`](https://github.com/liberusoftware/project-social-network-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/media.md)) |
| Capability Nuxt module skeleton | [`module-social-network-media-nuxt`](https://github.com/liberusoftware/module-social-network-media-nuxt) (`@liberusoftware/module-social-network-media-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Images** | Expose composable and Vue 3 component for `images` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/media.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Video** | Expose composable and Vue 3 component for `video` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/media.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Audio** | Expose composable and Vue 3 component for `audio` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/media.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Files** | Expose composable and Vue 3 component for `files` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/media.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Processing** | Expose composable and Vue 3 component for `processing` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/media.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Alt text** | Expose composable and Vue 3 component for `alt text` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/media.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Captions** | Expose composable and Vue 3 component for `captions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/media.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Rights** | Expose composable and Vue 3 component for `rights` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/media.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |
| **Delivery** | Expose composable and Vue 3 component for `delivery` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/media.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-social-network-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateAlbum.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Actions/CreateAlbum.php) | `public function handle(Profile $owner, array $attributes): Album` |
| [DeleteAlbum.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Actions/DeleteAlbum.php) | `public function handle(Profile $owner, Album $album): void` |
| [DeleteMediaAsset.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Actions/DeleteMediaAsset.php) | `public function handle(Profile $owner, MediaAsset $asset): void` |
| [MarkMediaReady.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Actions/MarkMediaReady.php) | `public function handle(Profile $owner, MediaAsset $asset): MediaAsset` |
| [RegisterMediaAsset.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Actions/RegisterMediaAsset.php) | `public function __construct(private MediaAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $owner, array $attributes): MediaAsset` |
| [UpdateAlbum.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Actions/UpdateAlbum.php) | `public function handle(Profile $owner, Album $album, array $attributes): Album` |
| [UpdateMediaAsset.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Actions/UpdateMediaAsset.php) | `public function __construct(private MediaAuthorizer $authorizer)`<br>`public function handle(Profile $owner, MediaAsset $asset, array $attributes): MediaAsset` |
| [MediaAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Contracts/MediaAuthorizer.php) | `public function upload(Profile $owner): void`<br>`public function update(Profile $owner): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Album.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Models/Album.php) | `id`, `owner_profile_id`, `name`, `description`, `privacy`, `cover_path` |
| [MediaAsset.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media/src/Models/MediaAsset.php) | `id`, `owner_profile_id`, `album_id`, `type`, `state`, `disk`, `path`, `mime_type`, `size`, `checksum`, `alt_text`, `captions`, `rights`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [MediaController.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media-api/src/Http/Controllers/MediaController.php) | `public function store(Request $request, GetProfile $get, RegisterMediaAsset $register): JsonResponse`<br>`public function index(Request $request, GetProfile $get): JsonResponse`<br>`public function show(string $asset, Request $request, GetProfile $get): JsonResponse`<br>`public function update(string $asset, Request $request, GetProfile $get, UpdateMediaAsset $update): JsonResponse`<br>`public function ready(string $asset, Request $request, GetProfile $get, MarkMediaReady $ready): JsonResponse`<br>`public function destroy(string $asset, Request $request, GetProfile $get, DeleteMediaAsset $delete): JsonResponse`<br>`public function albums(Request $request, GetProfile $get): JsonResponse`<br>`public function storeAlbum(Request $request, GetProfile $get, CreateAlbum $create): JsonResponse`<br>`public function showAlbum(string $album, Request $request, GetProfile $get): JsonResponse`<br>`public function updateAlbum(string $album, Request $request, GetProfile $get, UpdateAlbum $update): JsonResponse`<br>`public function destroyAlbum(string $album, Request $request, GetProfile $get, DeleteAlbum $delete): JsonResponse` |

**Observed route declarations:**

[modules/social-network-media-api/routes/api.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-media-api/routes/api.php)

```php
Route::prefix('api/v1/social-network/media')->middleware(['auth:sanctum', 'throttle:30,1'])->name('social-network.media.api.')->group(function (): void {
Route::get('/', [MediaController::class, 'index'])->name('index');
Route::get('/albums', [MediaController::class, 'albums'])->name('albums.index');
Route::post('/albums', [MediaController::class, 'storeAlbum'])->name('albums.store');
Route::get('/albums/{album}', [MediaController::class, 'showAlbum'])->name('albums.show');
Route::patch('/albums/{album}', [MediaController::class, 'updateAlbum'])->name('albums.update');
Route::delete('/albums/{album}', [MediaController::class, 'destroyAlbum'])->name('albums.destroy');
Route::post('/', [MediaController::class, 'store'])->name('store');
Route::post('/{asset}/ready', [MediaController::class, 'ready'])->name('ready');
Route::get('/{asset}', [MediaController::class, 'show'])->name('show');
Route::patch('/{asset}', [MediaController::class, 'update'])->name('update');
Route::delete('/{asset}', [MediaController::class, 'destroy'])->name('destroy');
```
<!-- layer-implementation-plan:end -->
