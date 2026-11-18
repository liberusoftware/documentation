# CRM: Advertising Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#advertising). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-advertising-nuxt`
**Matching domain module:** `crm-advertising`
**Application:** CRM
**Source feature:** [Advertising](../features/advertising.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/advertising.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-advertising` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Ad-account connections:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Campaign visibility:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Lead-ad ingestion:** page/component/composable/API-action behavior for this module's authorized workflow.
- **CRM audiences:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Offline/server conversions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Spend/performance sync:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Attribution:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-advertising-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `ad-account-connections`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `campaign-visibility`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `lead-ad-ingestion`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `crm-audiences`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `offline-server-conversions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `spend-performance-sync`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `attribution`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-advertising` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/advertising.md)) |
| Capability Nuxt module skeleton | [`module-crm-advertising-nuxt`](https://github.com/liberusoftware/module-crm-advertising-nuxt) (`@liberusoftware/module-crm-advertising-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Ad-account connections** | Expose composable and Vue 3 component for `ad-account connections` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/advertising.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Campaign visibility** | Expose composable and Vue 3 component for `campaign visibility` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/advertising.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Lead-ad ingestion** | Expose composable and Vue 3 component for `lead-ad ingestion` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/advertising.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **CRM audiences** | Expose composable and Vue 3 component for `crm audiences` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/advertising.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Offline/server conversions** | Expose composable and Vue 3 component for `offline/server conversions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/advertising.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Spend/performance sync** | Expose composable and Vue 3 component for `spend/performance sync` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/advertising.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Attribution** | Expose composable and Vue 3 component for `attribution` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/advertising.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [AdvertisingQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising/src/Queries/AdvertisingQuery.php) | `public function records(int $teamId, ?string $kind = null): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [TransitionRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising/src/Actions/TransitionRecord.php) | `public function execute(int $teamId, int $id, string $status): AdvertisingRecord` |
| [UpsertRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising/src/Actions/UpsertRecord.php) | `public function execute(int $teamId, array $attributes, ?int $id = null): AdvertisingRecord` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AdvertisingRecord.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising/src/Models/AdvertisingRecord.php) | `team_id`, `kind`, `name`, `status`, `external_id`, `platform`, `payload`, `starts_at`, `ends_at`, `completed_at` |

| Observed API controller | Handler signatures |
| --- | --- |
| [AdvertisingController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising-api/src/Http/Controllers/AdvertisingController.php) | `public function __construct(private readonly AdvertisingQuery $query)`<br>`public function index(Request $request): JsonResponse`<br>`public function store(Request $request, UpsertRecord $upsert): JsonResponse`<br>`public function show(int $record): AdvertisingResource`<br>`public function update(Request $request, int $record, UpsertRecord $upsert): JsonResponse`<br>`public function transition(Request $request, int $record, TransitionRecord $transition): JsonResponse`<br>`public function destroy(int $record, TransitionRecord $transition): JsonResponse` |

**Observed route declarations:**

[modules/crm-advertising-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-advertising-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/advertising')->group(function (): void {
Route::get('records', [AdvertisingController::class, 'index']);
Route::post('records', [AdvertisingController::class, 'store']);
Route::get('records/{record}', [AdvertisingController::class, 'show']);
Route::patch('records/{record}', [AdvertisingController::class, 'update']);
Route::post('records/{record}/transition', [AdvertisingController::class, 'transition']);
Route::delete('records/{record}', [AdvertisingController::class, 'destroy']);
```
<!-- layer-implementation-plan:end -->
