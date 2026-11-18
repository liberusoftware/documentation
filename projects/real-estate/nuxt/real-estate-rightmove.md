# Real Estate: Real Estate Rightmove Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#real-estate-rightmove). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-real-estate-real-estate-rightmove-nuxt`
**Matching domain module:** `real-estate-rightmove`
**Application:** Real Estate
**Source feature:** [Real Estate Rightmove](../features/real-estate-rightmove.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/real-estate-rightmove.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `real-estate-rightmove` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Rightmove sync state:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Provider payload boundary:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Retry and error state:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-real-estate-real-estate-rightmove-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `rightmove-sync-state`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `provider-payload-boundary`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `retry-and-error-state`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `real-estate-rightmove` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-real-estate-nuxt-vue`](https://github.com/liberusoftware/project-real-estate-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/real-estate-rightmove.md)) |
| Capability Nuxt module skeleton | [`module-real-estate-rightmove-nuxt`](https://github.com/liberusoftware/module-real-estate-rightmove-nuxt) (`@liberusoftware/module-real-estate-rightmove-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Rightmove sync state** | Expose composable and Vue 3 component for `rightmove sync state` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-rightmove.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Provider payload boundary** | Expose composable and Vue 3 component for `provider payload boundary` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-rightmove.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Retry and error state** | Expose composable and Vue 3 component for `retry and error state` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/real-estate-rightmove.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [RightmoveTransport.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-rightmove/src/Contracts/RightmoveTransport.php) | `public function sendProperty(string $reference, array $payload, array $credentials): array`<br>`public function removeProperty(string $reference, array $credentials): array`<br>`public function branchPropertyList(array $credentials): array` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [RightmoveSync.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-rightmove/src/Models/RightmoveSync.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [RightmoveSyncController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-rightmove-api/src/Http/Controllers/RightmoveSyncController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateRightmoveSync $create): JsonResponse`<br>`public function show(Request $request, RightmoveSync $rightmoveSync): JsonResponse`<br>`public function sync(Request $request, RightmoveSync $rightmoveSync, SyncRightmoveListing $sync): JsonResponse`<br>`public function update(Request $request, RightmoveSync $rightmoveSync, UpdateRightmoveSync $update): JsonResponse`<br>`public function destroy(Request $request, RightmoveSync $rightmoveSync, DeleteRightmoveSync $delete): Response` |

**Observed route declarations:**

[modules/real-estate-rightmove-api/routes/api.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-rightmove-api/routes/api.php)

```php
Route::prefix('api/v1/real-estate/integrations/rightmove/syncs')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [RightmoveSyncController::class, 'index']);
Route::post('/', [RightmoveSyncController::class, 'store']);
Route::post('/{rightmoveSync}/sync', [RightmoveSyncController::class, 'sync']);
Route::get('/{rightmoveSync}', [RightmoveSyncController::class, 'show']);
Route::delete('/{rightmoveSync}', [RightmoveSyncController::class, 'destroy']);
```
<!-- layer-implementation-plan:end -->
