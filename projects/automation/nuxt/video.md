# Automation: Video Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#video). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-automation-video-nuxt`
**Matching domain module:** `automation-video`
**Application:** Automation
**Source feature:** [Video](../features/video.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/video.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `automation-video` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Generation/editing jobs:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Scripts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Captions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Audio:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Moderation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Provenance:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Delivery:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-automation-video-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `generation-editing-jobs`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `scripts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `captions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `audio`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `moderation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `provenance`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
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

- Package identity, public exports, API dependency, and module dependency match `automation-video` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-automation-nuxt-vue`](https://github.com/liberusoftware/project-automation-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-automation-laravel-api`](https://github.com/liberusoftware/project-automation-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/video.md)) |
| Capability Nuxt module skeleton | [`module-automation-video-nuxt`](https://github.com/liberusoftware/module-automation-video-nuxt) (`@liberusoftware/module-automation-video-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Generation/editing jobs** | Expose composable and Vue 3 component for `generation/editing jobs` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/video.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-automation-laravel-api`. |
| **Scripts** | Expose composable and Vue 3 component for `scripts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/video.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-automation-laravel-api`. |
| **Captions** | Expose composable and Vue 3 component for `captions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/video.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-automation-laravel-api`. |
| **Audio** | Expose composable and Vue 3 component for `audio` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/video.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-automation-laravel-api`. |
| **Moderation** | Expose composable and Vue 3 component for `moderation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/video.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-automation-laravel-api`. |
| **Provenance** | Expose composable and Vue 3 component for `provenance` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/video.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-automation-laravel-api`. |
| **Delivery** | Expose composable and Vue 3 component for `delivery` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/video.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-automation-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateVideoResource.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-video/src/Actions/CreateVideoResource.php) | `public function execute(string $teamId, string $name, array $payload = [], ?string $idempotencyKey = null, ?string $actorId = null, ?string $correlationId = null): VideoResource` |
| [TransitionVideoResource.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-video/src/Actions/TransitionVideoResource.php) | `public function execute(VideoResource $resource, string $teamId, string $status, array $allowedStatuses = ['draft', 'active', 'paused', 'completed', 'failed', 'cancelled'], ?string $actorId = null, ?string $correlationId = null): VideoResource` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [VideoResource.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-video/src/Models/VideoResource.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [VideoResourceController.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-video-api/src/Http/Controllers/VideoResourceController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateVideoResource $create): JsonResponse`<br>`public function show(Request $request, string $id): JsonResponse`<br>`public function update(Request $request, string $id): JsonResponse`<br>`public function destroy(Request $request, string $id): JsonResponse`<br>`public function transition(Request $request, string $id, TransitionVideoResource $transition): JsonResponse` |

**Observed route declarations:**

[modules/module-automation-video-api/routes/api.php](https://github.com/liberusoftware/project-automation-laravel-filament/blob/68e5f07a67041f8438530c71bc86515cbd11da70/modules/module-automation-video-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:60,1'])->prefix('api/v1/automation/video')->group(function (): void {
Route::get('/', [VideoResourceController::class, 'index']);
Route::post('/', [VideoResourceController::class, 'store']);
Route::get('/{id}', [VideoResourceController::class, 'show']);
Route::patch('/{id}', [VideoResourceController::class, 'update']);
Route::delete('/{id}', [VideoResourceController::class, 'destroy']);
Route::post('/{id}/transition', [VideoResourceController::class, 'transition']);
```
<!-- layer-implementation-plan:end -->
