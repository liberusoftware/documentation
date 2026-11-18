# Accounting: Product and Service Items Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#product-and-service-items). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-product-and-service-items-nuxt`
**Matching domain module:** `accounting-product-and-service-items`
**Application:** Accounting
**Source feature:** [Product and Service Items](../features/product-and-service-items.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/product-and-service-items.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-product-and-service-items` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Items/services:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Codes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Purchase/sales descriptions:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Accounts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Tax defaults:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Units:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Costs/prices:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Ecommerce references:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-product-and-service-items-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `items-services`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `codes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `purchase-sales-descriptions`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `accounts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `tax-defaults`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `units`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `costs-prices`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `ecommerce-references`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-product-and-service-items` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/product-and-service-items.md)) |
| Capability Nuxt module skeleton | [`module-accounting-product-and-service-items-nuxt`](https://github.com/liberusoftware/module-accounting-product-and-service-items-nuxt) (`@liberusoftware/module-accounting-product-and-service-items-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Items/services** | Expose composable and Vue 3 component for `items/services` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/product-and-service-items.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Codes** | Expose composable and Vue 3 component for `codes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/product-and-service-items.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Purchase/sales descriptions** | Expose composable and Vue 3 component for `purchase/sales descriptions` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/product-and-service-items.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Accounts** | Expose composable and Vue 3 component for `accounts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/product-and-service-items.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Tax defaults** | Expose composable and Vue 3 component for `tax defaults` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/product-and-service-items.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Units** | Expose composable and Vue 3 component for `units` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/product-and-service-items.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Costs/prices** | Expose composable and Vue 3 component for `costs/prices` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/product-and-service-items.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Ecommerce references** | Expose composable and Vue 3 component for `ecommerce references` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/product-and-service-items.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [FindAccountingItems.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-product-and-service-items/src/Queries/FindAccountingItems.php) | `public function search(?string $term = null): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [SaveAccountingItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-product-and-service-items/src/Actions/SaveAccountingItem.php) | `public function handle(array $attributes): AccountingItem` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AccountingItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-product-and-service-items/src/Models/AccountingItem.php) | `team_id`, `code`, `name`, `kind`, `purchase_description`, `sales_description`, `sales_account_ref`, `purchase_account_ref`, `tax_default_ref`, `unit`, `purchase_price`, `sales_price`, `currency`, `status`, `ecommerce_refs`, `metadata` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ProductAndServiceItemsController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-product-and-service-items-api/src/Http/Controllers/ProductAndServiceItemsController.php) | `public function index(Request $request, FindAccountingItems $query): AnonymousResourceCollection`<br>`public function store(Request $request, SaveAccountingItem $action): JsonResponse`<br>`public function show(Request $request, AccountingItem $accountingItem): AccountingItemResource` |

**Observed route declarations:**

[modules/accounting-product-and-service-items-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-product-and-service-items-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/product-and-service-items')->group(function (): void {
Route::middleware('ability:accounting.product-and-service-items.read')->group(function (): void {
Route::get('/', [ProductAndServiceItemsController::class, 'index']);
Route::get('/{accountingItem}', [ProductAndServiceItemsController::class, 'show']);
Route::post('/', [ProductAndServiceItemsController::class, 'store'])->middleware('ability:accounting.product-and-service-items.write');
```
<!-- layer-implementation-plan:end -->
