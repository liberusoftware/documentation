# Accounting: Sales Orders Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#sales-orders). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-accounting-sales-orders-nuxt`
**Matching domain module:** `accounting-sales-orders`
**Application:** Accounting
**Source feature:** [Sales Orders](../features/sales-orders.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/sales-orders.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `accounting-sales-orders` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Accepted demand:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Allocation/fulfillment references:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Deposits:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Partial invoicing:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Status:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Cancellation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Billing/Ecommerce integration:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-accounting-sales-orders-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `accepted-demand`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `allocation-fulfillment-references`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `deposits`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `partial-invoicing`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `status`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `cancellation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `billing-ecommerce-integration`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `accounting-sales-orders` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-accounting-erp-nuxt-vue`](https://github.com/liberusoftware/project-accounting-erp-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/sales-orders.md)) |
| Capability Nuxt module skeleton | [`module-accounting-sales-orders-nuxt`](https://github.com/liberusoftware/module-accounting-sales-orders-nuxt) (`@liberusoftware/module-accounting-sales-orders-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Accepted demand** | Expose composable and Vue 3 component for `accepted demand` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/sales-orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Allocation/fulfillment references** | Expose composable and Vue 3 component for `allocation/fulfillment references` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/sales-orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Deposits** | Expose composable and Vue 3 component for `deposits` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/sales-orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Partial invoicing** | Expose composable and Vue 3 component for `partial invoicing` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/sales-orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Status** | Expose composable and Vue 3 component for `status` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/sales-orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Cancellation** | Expose composable and Vue 3 component for `cancellation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/sales-orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |
| **Billing/Ecommerce integration** | Expose composable and Vue 3 component for `billing/ecommerce integration` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/sales-orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-accounting-erp-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [SalesOrderQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/src/Queries/SalesOrderQuery.php) | `public function paginate(?string $customer = null, ?string $status = null, int $perPage = 25, ?int $teamId = null): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddFulfillmentReference.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/src/Actions/AddFulfillmentReference.php) | `public function handle(SalesOrder $order, array $attributes): SalesOrderAllocation` |
| [AddSalesOrderDeposit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/src/Actions/AddSalesOrderDeposit.php) | `public function handle(SalesOrder $order, array $attributes): SalesOrderDeposit` |
| [CreateSalesOrder.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/src/Actions/CreateSalesOrder.php) | `public function handle(array $attributes, array $lines): SalesOrder` |
| [RecordPartialInvoice.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/src/Actions/RecordPartialInvoice.php) | `public function handle(SalesOrder $order, float $amount, string $invoiceReference): SalesOrder` |
| [TransitionSalesOrder.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/src/Actions/TransitionSalesOrder.php) | `public function handle(SalesOrder $order, OrderStatus\|string $status): SalesOrder` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SalesOrder.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/src/Models/SalesOrder.php) | `team_id`, `customer_id`, `estimate_id`, `order_number`, `order_date`, `status`, `currency`, `subtotal`, `tax_total`, `total`, `invoiced_total`, `notes`, `metadata` |
| [SalesOrderAllocation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/src/Models/SalesOrderAllocation.php) | `sales_order_id`, `item_id`, `fulfillment_type`, `fulfillment_id`, `quantity`, `status`, `metadata` |
| [SalesOrderDeposit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/src/Models/SalesOrderDeposit.php) | `sales_order_id`, `reference`, `amount`, `currency`, `status`, `metadata` |
| [SalesOrderItem.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders/src/Models/SalesOrderItem.php) | `sales_order_id`, `sku`, `description`, `quantity`, `unit_price`, `amount`, `tax_rate`, `tax_amount`, `invoiced_quantity`, `metadata` |
| [SalesOrder.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders-api/src/Models/SalesOrder.php) | `customer_id`, `estimate_id`, `sales_order_number`, `order_date`, `subtotal_amount`, `tax_amount`, `total_amount`, `status`, `notes`, `team_id` |

| Observed API controller | Handler signatures |
| --- | --- |
| [SalesOrderController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders-api/src/Http/Controllers/SalesOrderController.php) | `public function index(Request $request, SalesOrderQuery $query): mixed`<br>`public function show(Request $request, SalesOrder $salesOrder): SalesOrderResource`<br>`public function store(Request $request, CreateSalesOrder $action): JsonResponse`<br>`public function transition(Request $request, SalesOrder $salesOrder, TransitionSalesOrder $action): SalesOrderResource`<br>`public function deposit(Request $request, SalesOrder $salesOrder, AddSalesOrderDeposit $action): SalesOrderResource`<br>`public function invoice(Request $request, SalesOrder $salesOrder, RecordPartialInvoice $action): SalesOrderResource` |

**Observed route declarations:**

[modules/accounting-sales-orders-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-sales-orders-api/routes/api.php)

```php
Route::middleware(['api', 'auth:sanctum', 'throttle:api'])->prefix('api/v1/accounting/sales-orders')->group(function (): void {
Route::middleware('ability:accounting.sales-orders.read')->group(function (): void {
Route::get('/', [SalesOrderController::class, 'index']);
Route::get('/{salesOrder}', [SalesOrderController::class, 'show']);
Route::middleware('ability:accounting.sales-orders.write')->group(function (): void {
Route::post('/', [SalesOrderController::class, 'store']);
Route::post('/{salesOrder}/transition', [SalesOrderController::class, 'transition']);
Route::post('/{salesOrder}/deposits', [SalesOrderController::class, 'deposit']);
Route::post('/{salesOrder}/invoice', [SalesOrderController::class, 'invoice']);
```
<!-- layer-implementation-plan:end -->
