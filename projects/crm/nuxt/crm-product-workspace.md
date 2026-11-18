# CRM: CRM Product Workspace Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-product-workspace). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-product-workspace-nuxt`
**Matching domain module:** `crm-product-workspace`
**Application:** CRM
**Source feature:** [CRM Product Workspace](../features/crm-product-workspace.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/crm-product-workspace.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-product-workspace` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Sales-facing catalog projections:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Bundles:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Entitlements:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Price-book references:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Product eligibility:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Governed Billing/Ecommerce synchronization:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-product-workspace-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `sales-facing-catalog-projections`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `bundles`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `entitlements`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `price-book-references`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `product-eligibility`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `governed-billing-ecommerce-synchronization`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `crm-product-workspace` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-product-workspace.md)) |
| Capability Nuxt module skeleton | [`module-crm-product-workspace-nuxt`](https://github.com/liberusoftware/module-crm-product-workspace-nuxt) (`@liberusoftware/module-crm-product-workspace-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Sales-facing catalog projections** | Expose composable and Vue 3 component for `sales-facing catalog projections` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-product-workspace.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Bundles** | Expose composable and Vue 3 component for `bundles` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-product-workspace.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Entitlements** | Expose composable and Vue 3 component for `entitlements` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-product-workspace.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Price-book references** | Expose composable and Vue 3 component for `price-book references` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-product-workspace.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Product eligibility** | Expose composable and Vue 3 component for `product eligibility` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-product-workspace.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Governed Billing/Ecommerce synchronization** | Expose composable and Vue 3 component for `governed billing/ecommerce synchronization` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/crm-product-workspace.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ProductWorkspaceQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace/src/Queries/ProductWorkspaceQuery.php) | `public function products(int $teamId)`<br>`public function entitlements(int $teamId, int $customerId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [GrantEntitlement.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace/src/Actions/GrantEntitlement.php) | `public function __construct(private readonly ProductWorkspacePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProductEntitlement` |
| [RecordProductSync.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace/src/Actions/RecordProductSync.php) | `public function __construct(private readonly ProductWorkspacePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ProductSync` |
| [UpsertWorkspaceProduct.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace/src/Actions/UpsertWorkspaceProduct.php) | `public function __construct(private readonly ProductWorkspacePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): WorkspaceProduct` |
| [ProductWorkspacePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace/src/Services/ProductWorkspacePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ProductBundle.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace/src/Models/ProductBundle.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProductEntitlement.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace/src/Models/ProductEntitlement.php) | No literal fillable array detected; inspect the model and API schema. |
| [ProductSync.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace/src/Models/ProductSync.php) | No literal fillable array detected; inspect the model and API schema. |
| [WorkspaceProduct.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace/src/Models/WorkspaceProduct.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ProductWorkspaceController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace-api/src/Http/Controllers/ProductWorkspaceController.php) | `public function __construct(private readonly ProductWorkspaceQuery $query)`<br>`public function products(): JsonResponse`<br>`public function store(UpsertWorkspaceProduct $action): JsonResponse`<br>`public function entitlement(GrantEntitlement $action): JsonResponse`<br>`public function sync(RecordProductSync $action): JsonResponse` |

**Observed route declarations:**

[modules/crm-product-workspace-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-product-workspace-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/crm-product-workspace')->group(function (): void {
Route::get('products', [ProductWorkspaceController::class, 'products']);
Route::post('products', [ProductWorkspaceController::class, 'store']);
Route::post('entitlements', [ProductWorkspaceController::class, 'entitlement']);
Route::post('syncs', [ProductWorkspaceController::class, 'sync']);
```
<!-- layer-implementation-plan:end -->
