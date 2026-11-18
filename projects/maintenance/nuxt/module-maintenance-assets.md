# Maintenance: Module Maintenance Assets Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-maintenance-assets). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-maintenance-module-maintenance-assets-nuxt`
**Matching domain module:** `module-maintenance-assets`
**Application:** Maintenance
**Source feature:** [Module Maintenance Assets](../features/module-maintenance-assets.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/module-maintenance-assets.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `module-maintenance-assets` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Hierarchies:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Categories:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Specifications:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Meters:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Warranties:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Condition:** page/component/composable/API-action behavior for this module's authorized workflow.
- **QR/barcodes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **History:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-maintenance-module-maintenance-assets-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `hierarchies`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `categories`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `specifications`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `meters`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `warranties`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `condition`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `qr-barcodes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `history`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `module-maintenance-assets` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-maintenance-nuxt-vue`](https://github.com/liberusoftware/project-maintenance-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-maintenance-laravel-api`](https://github.com/liberusoftware/project-maintenance-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/module-maintenance-assets.md)) |
| Capability Nuxt module skeleton | [`module-maintenance-assets-nuxt`](https://github.com/liberusoftware/module-maintenance-assets-nuxt) (`@liberusoftware/module-maintenance-assets-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Hierarchies** | Expose composable and Vue 3 component for `hierarchies` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-maintenance-assets.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Categories** | Expose composable and Vue 3 component for `categories` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-maintenance-assets.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Specifications** | Expose composable and Vue 3 component for `specifications` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-maintenance-assets.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Meters** | Expose composable and Vue 3 component for `meters` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-maintenance-assets.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Warranties** | Expose composable and Vue 3 component for `warranties` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-maintenance-assets.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **Condition** | Expose composable and Vue 3 component for `condition` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-maintenance-assets.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **QR/barcodes** | Expose composable and Vue 3 component for `qr/barcodes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-maintenance-assets.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |
| **History** | Expose composable and Vue 3 component for `history` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/module-maintenance-assets.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-maintenance-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateAsset.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-assets/src/Actions/CreateAsset.php) | `public function handle(int $teamId, array $attributes): Asset` |
| [DeleteAsset.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-assets/src/Actions/DeleteAsset.php) | `public function handle(int $teamId, Asset $asset): void` |
| [RecordAssetHistory.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-assets/src/Actions/RecordAssetHistory.php) | `public function handle(int $teamId, Asset $asset, string $type, string $note, ?int $actorId = null): Asset` |
| [UpdateAsset.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-assets/src/Actions/UpdateAsset.php) | `public function handle(int $teamId, Asset $asset, array $attributes): Asset` |
| [AssetPolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-assets/src/Policies/AssetPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, Asset $asset): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, Asset $asset): bool`<br>`public function delete(object $user, Asset $asset): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Asset.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-assets/src/Models/Asset.php) | `team_id`, `name`, `description`, `code`, `category`, `serial_number`, `model`, `manufacturer`, `location`, `purchase_date`, `warranty_expiry`, `notes`, `condition`, `criticality`, `status`, `qr_code`, `barcode`, `sensor_enabled`, `sensor_type`, `sensor_id`, `sensor_config`, `last_sensor_reading_at`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [AssetController.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-assets-api/src/Http/Controllers/AssetController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateAsset $create): JsonResponse`<br>`public function show(Request $request, Asset $asset): JsonResponse`<br>`public function history(Request $request, Asset $asset, RecordAssetHistory $recordHistory): JsonResponse`<br>`public function update(Request $request, Asset $asset, UpdateAsset $update): JsonResponse`<br>`public function destroy(Request $request, Asset $asset, DeleteAsset $delete): JsonResponse` |

**Observed route declarations:**

[modules/module-maintenance-assets-api/routes/api.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-assets-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/maintenance/assets')->group(function (): void {
Route::get('/', [AssetController::class, 'index']);
Route::post('/', [AssetController::class, 'store']);
Route::post('/{asset}/history', [AssetController::class, 'history']);
Route::get('/{asset}', [AssetController::class, 'show']);
Route::patch('/{asset}', [AssetController::class, 'update']);
Route::delete('/{asset}', [AssetController::class, 'destroy']);
```
<!-- layer-implementation-plan:end -->
