# Real Estate: Viewings Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#viewings). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-real-estate-viewings-nuxt`
**Matching domain module:** `real-estate-viewings`
**Application:** Real Estate
**Source feature:** [Viewings](../features/viewings.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/viewings.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `real-estate-viewings` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Availability:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Booking:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Confirmation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Access:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Accompaniment:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Reminders:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Feedback:** page/component/composable/API-action behavior for this module's authorized workflow.
- **No-shows:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-real-estate-viewings-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `availability`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `booking`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `confirmation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `access`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `accompaniment`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `reminders`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `feedback`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `no-shows`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `real-estate-viewings` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-real-estate-nuxt-vue`](https://github.com/liberusoftware/project-real-estate-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-real-estate-laravel-api`](https://github.com/liberusoftware/project-real-estate-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/viewings.md)) |
| Capability Nuxt module skeleton | [`module-real-estate-viewings-nuxt`](https://github.com/liberusoftware/module-real-estate-viewings-nuxt) (`@liberusoftware/module-real-estate-viewings-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Availability** | Expose composable and Vue 3 component for `availability` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/viewings.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Booking** | Expose composable and Vue 3 component for `booking` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/viewings.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Confirmation** | Expose composable and Vue 3 component for `confirmation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/viewings.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Access** | Expose composable and Vue 3 component for `access` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/viewings.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Accompaniment** | Expose composable and Vue 3 component for `accompaniment` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/viewings.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Reminders** | Expose composable and Vue 3 component for `reminders` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/viewings.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **Feedback** | Expose composable and Vue 3 component for `feedback` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/viewings.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |
| **No-shows** | Expose composable and Vue 3 component for `no-shows` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/viewings.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-real-estate-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [AvailableViewingSlots.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-viewings/src/Queries/AvailableViewingSlots.php) | `public function handle( int\|string $teamId, int\|string\|null $propertyId, CarbonImmutable $date, int $durationMinutes = 60, ): array` |
| [ViewingCalendarExport.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-viewings/src/Queries/ViewingCalendarExport.php) | `public function handle(Viewing\|int\|string $viewing): string` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ViewingPolicy.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-viewings/src/Policies/ViewingPolicy.php) | `public function viewAny(AuthUser $authUser): bool`<br>`public function view(AuthUser $authUser, Viewing $viewing): bool`<br>`public function create(AuthUser $authUser): bool`<br>`public function update(AuthUser $authUser, Viewing $viewing): bool`<br>`public function delete(AuthUser $authUser, Viewing $viewing): bool`<br>`public function deleteAny(AuthUser $authUser): bool`<br>`public function restore(AuthUser $authUser, Viewing $viewing): bool`<br>`public function forceDelete(AuthUser $authUser, Viewing $viewing): bool`<br>`public function forceDeleteAny(AuthUser $authUser): bool`<br>`public function restoreAny(AuthUser $authUser): bool`<br>`public function replicate(AuthUser $authUser, Viewing $viewing): bool`<br>`public function reorder(AuthUser $authUser): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Viewing.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-viewings/src/Models/Viewing.php) | No literal fillable array detected; inspect the model and API schema. |
| [ViewingFeedback.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-viewings/src/Models/ViewingFeedback.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ViewingController.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-viewings-api/src/Http/Controllers/ViewingController.php) | `public function index(Request $request): JsonResponse`<br>`public function availability(Request $request, AvailableViewingSlots $slots): JsonResponse`<br>`public function store(Request $request, CreateViewing $create): JsonResponse`<br>`public function show(Request $request, Viewing $viewing): JsonResponse`<br>`public function update(Request $request, Viewing $viewing, UpdateViewing $update): JsonResponse`<br>`public function destroy(Request $request, Viewing $viewing, DeleteViewing $delete): Response`<br>`public function confirm(Request $request, Viewing $viewing, ConfirmViewing $confirm): JsonResponse`<br>`public function complete(Request $request, Viewing $viewing, CompleteViewing $complete): JsonResponse`<br>`public function cancel(Request $request, Viewing $viewing, CancelViewing $cancel): JsonResponse`<br>`public function noShow(Request $request, Viewing $viewing, MarkViewingNoShow $noShow): JsonResponse` |

**Observed route declarations:**

[modules/real-estate-viewings-api/routes/api.php](https://github.com/liberusoftware/project-real-estate-laravel-filament/blob/178d8015b601c99dec43acfdc12724aae2b3731a/modules/real-estate-viewings-api/routes/api.php)

```php
Route::prefix('api/v1/real-estate/viewings')->middleware(['api', 'auth:sanctum', 'throttle:api', 'api.idempotency'])->group(function (): void {
Route::get('/', [ViewingController::class, 'index'])->name('real-estate.viewings.index');
Route::post('/', [ViewingController::class, 'store'])->name('real-estate.viewings.store');
Route::get('/availability', [ViewingController::class, 'availability'])->name('real-estate.viewings.availability');
Route::get('/{viewing}', [ViewingController::class, 'show'])->name('real-estate.viewings.show');
Route::delete('/{viewing}', [ViewingController::class, 'destroy'])->name('real-estate.viewings.destroy');
Route::post('/{viewing}/confirm', [ViewingController::class, 'confirm'])->name('real-estate.viewings.confirm');
Route::post('/{viewing}/complete', [ViewingController::class, 'complete'])->name('real-estate.viewings.complete');
Route::post('/{viewing}/cancel', [ViewingController::class, 'cancel'])->name('real-estate.viewings.cancel');
Route::post('/{viewing}/no-show', [ViewingController::class, 'noShow'])->name('real-estate.viewings.no-show');
```
<!-- layer-implementation-plan:end -->
