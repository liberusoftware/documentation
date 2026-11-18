# Accounting: Accounting Purchase Orders Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-purchase-orders). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-accounting-purchase-orders-nuxt`
**Matching domain module:** `accounting-purchase-orders`
**Application:** Accounting
**Source feature:** [Accounting Purchase Orders](../features/accounting-purchase-orders.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/accounting-purchase-orders.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-purchase-orders` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Supplier items:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Prices:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Quantities:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Delivery:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Approval:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Issue:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Receipts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Partials:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Changes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Closure:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Commitments:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-accounting-purchase-orders-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `supplier-items`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `prices`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `quantities`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `delivery`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `approval`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `issue`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `receipts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `partials`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `changes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `closure`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `commitments`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-purchase-orders` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-purchase-orders.md)) |
| Capability Nuxt module skeleton | [`module-accounting-purchase-orders-nuxt`](https://github.com/liberusoftware/module-accounting-purchase-orders-nuxt) (`@liberusoftware/module-accounting-purchase-orders-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Supplier items** | Expose composable and Vue 3 component for `supplier items` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-purchase-orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Prices** | Expose composable and Vue 3 component for `prices` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-purchase-orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Quantities** | Expose composable and Vue 3 component for `quantities` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-purchase-orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Delivery** | Expose composable and Vue 3 component for `delivery` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-purchase-orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Approval** | Expose composable and Vue 3 component for `approval` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-purchase-orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Issue** | Expose composable and Vue 3 component for `issue` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-purchase-orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Receipts** | Expose composable and Vue 3 component for `receipts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-purchase-orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Partials** | Expose composable and Vue 3 component for `partials` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-purchase-orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Changes** | Expose composable and Vue 3 component for `changes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-purchase-orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Closure** | Expose composable and Vue 3 component for `closure` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-purchase-orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Commitments** | Expose composable and Vue 3 component for `commitments` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/accounting-purchase-orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreatePurchaseOrder.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-orders/src/Actions/CreatePurchaseOrder.php) | `public function handle(array $attributes, array $lines): PurchaseOrder` |
| [RecordPurchaseOrderChange.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-orders/src/Actions/RecordPurchaseOrderChange.php) | `public function handle(PurchaseOrder $order, array $attributes): PurchaseOrderChange` |
| [RecordPurchaseReceipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-orders/src/Actions/RecordPurchaseReceipt.php) | `public function handle(PurchaseOrder $order, array $attributes): PurchaseReceipt` |
| [TransitionPurchaseOrder.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-orders/src/Actions/TransitionPurchaseOrder.php) | `public function handle(PurchaseOrder $order, PurchaseOrderStatus $status, array $attributes = []): PurchaseOrder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PurchaseOrder.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-orders/src/Models/PurchaseOrder.php) | `team_id`, `supplier_ref`, `order_number`, `currency`, `order_date`, `expected_delivery_on`, `total_amount`, `status`, `commitment_ref`, `source_requisition_ref`, `notes`, `metadata` |
| [PurchaseOrderChange.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-orders/src/Models/PurchaseOrderChange.php) | `order_id`, `version`, `changes`, `reason`, `actor_ref`, `approved_at`, `metadata` |
| [PurchaseOrderLine.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-orders/src/Models/PurchaseOrderLine.php) | `order_id`, `item_ref`, `description`, `quantity`, `unit_price`, `received_quantity`, `delivery_metadata`, `metadata` |
| [PurchaseReceipt.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-orders/src/Models/PurchaseReceipt.php) | `order_id`, `receipt_ref`, `received_on`, `lines`, `status`, `document_ref`, `metadata` |
| [PurchaseOrder.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-orders-api/src/Models/PurchaseOrder.php) | `supplier_id`, `po_number`, `order_date`, `expected_delivery_date`, `total_amount`, `status`, `notes`, `purchase_request_id`, `team_id` |

| Observed API controller | Handler signatures |
| --- | --- |
| [PurchaseOrdersController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-orders-api/src/Http/Controllers/PurchaseOrdersController.php) | `public function index(Request $request): AnonymousResourceCollection`<br>`public function store(Request $request, CreatePurchaseOrder $action): JsonResponse`<br>`public function show(Request $request, PurchaseOrder $order): PurchaseOrderResource`<br>`public function transition(Request $request, PurchaseOrder $order, TransitionPurchaseOrder $action): PurchaseOrderResource`<br>`public function receipt(Request $request, PurchaseOrder $order, RecordPurchaseReceipt $action): JsonResponse`<br>`public function change(Request $request, PurchaseOrder $order, RecordPurchaseOrderChange $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-purchase-orders-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-purchase-orders-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/purchase-orders')->group(function (): void {
Route::middleware('ability:accounting.purchase-orders.read')->group(function (): void {
Route::get('/', [PurchaseOrdersController::class, 'index']);
Route::get('/{order}', [PurchaseOrdersController::class, 'show']);
Route::middleware('ability:accounting.purchase-orders.write')->group(function (): void {
Route::post('/', [PurchaseOrdersController::class, 'store']);
Route::post('/{order}/transition', [PurchaseOrdersController::class, 'transition']);
Route::post('/{order}/receipts', [PurchaseOrdersController::class, 'receipt']);
Route::post('/{order}/changes', [PurchaseOrdersController::class, 'change']);
```
<!-- layer-implementation-plan:end -->
