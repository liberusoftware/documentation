# Browser Game: Commerce Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#commerce). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-browser-game-commerce-nuxt`
**Matching domain module:** `browser-game-commerce`
**Application:** Browser Game
**Source feature:** [Commerce](../features/commerce.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/commerce.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `browser-game-commerce` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Premium membership:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Entitlements:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Store:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Regional pricing:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Receipts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Refunds:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Parental controls:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-browser-game-commerce-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `premium-membership`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `entitlements`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `store`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `regional-pricing`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `receipts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `refunds`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `parental-controls`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `browser-game-commerce` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-browser-game-nuxt-vue`](https://github.com/liberusoftware/project-browser-game-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-browser-game-laravel-api`](https://github.com/liberusoftware/project-browser-game-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/commerce.md)) |
| Capability Nuxt module skeleton | [`module-browser-game-commerce-nuxt`](https://github.com/liberusoftware/module-browser-game-commerce-nuxt) (`@liberusoftware/module-browser-game-commerce-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Premium membership** | Expose composable and Vue 3 component for `premium membership` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/commerce.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Entitlements** | Expose composable and Vue 3 component for `entitlements` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/commerce.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Store** | Expose composable and Vue 3 component for `store` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/commerce.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Regional pricing** | Expose composable and Vue 3 component for `regional pricing` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/commerce.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Receipts** | Expose composable and Vue 3 component for `receipts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/commerce.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Refunds** | Expose composable and Vue 3 component for `refunds` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/commerce.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |
| **Parental controls** | Expose composable and Vue 3 component for `parental controls` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/commerce.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-browser-game-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CommerceQuery.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/src/Queries/CommerceQuery.php) | `public function visible(?string $tenantId, ?string $teamId): Builder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CommerceEntitlement.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/src/Models/CommerceEntitlement.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommerceOrder.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/src/Models/CommerceOrder.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommerceOrderLine.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/src/Models/CommerceOrderLine.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommerceProduct.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/src/Models/CommerceProduct.php) | No literal fillable array detected; inspect the model and API schema. |
| [CommerceRecord.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce/src/Models/CommerceRecord.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [CommerceController.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce-api/src/Http/Controllers/CommerceController.php) | `public function index(Request $request): JsonResponse`<br>`public function products(Request $request): JsonResponse`<br>`public function checkout(Request $request): JsonResponse`<br>`public function complete(Request $request, CommerceOrder $order): JsonResponse`<br>`public function refund(Request $request, CommerceOrder $order): JsonResponse`<br>`public function show(Request $request, CommerceRecord $commerce): JsonResponse` |

**Observed route declarations:**

[modules/browser-game-commerce-api/routes/api.php](https://github.com/liberusoftware/project-browser-game-laravel-filament/blob/790fdffebd3a19bf914aea8a4ef049f87f52c62d/modules/browser-game-commerce-api/routes/api.php)

```php
Route::prefix('api/v1/browser-game/commerce')->middleware(['api', 'auth:sanctum', 'throttle:api'])->group(function (): void {
Route::get('/', [CommerceController::class, 'index'])->name('browser-game.commerce.index');
Route::get('/products', [CommerceController::class, 'products'])->name('browser-game.commerce.products');
Route::post('/checkout', [CommerceController::class, 'checkout'])->name('browser-game.commerce.checkout');
Route::post('/orders/{order}/complete', [CommerceController::class, 'complete'])->name('browser-game.commerce.orders.complete');
Route::post('/orders/{order}/refund', [CommerceController::class, 'refund'])->name('browser-game.commerce.orders.refund');
Route::get('/{commerce}', [CommerceController::class, 'show'])->name('browser-game.commerce.show');
```
<!-- layer-implementation-plan:end -->
