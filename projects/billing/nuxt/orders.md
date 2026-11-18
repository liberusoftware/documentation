# Billing: Orders Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#orders). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-billing-orders-nuxt`
**Matching domain module:** `billing-orders`
**Application:** Billing
**Source feature:** [Orders](../features/orders.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/orders.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `billing-orders` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Quotes:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Carts:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Checkout:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Fraud review:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Agreements:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Order state:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Change orders:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-billing-orders-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `quotes`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `carts`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `checkout`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `fraud-review`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `agreements`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `order-state`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `change-orders`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

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

- Package identity, public exports, API dependency, and module dependency match `billing-orders` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-billing-nuxt-vue`](https://github.com/liberusoftware/project-billing-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-billing-laravel-api`](https://github.com/liberusoftware/project-billing-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/orders.md)) |
| Capability Nuxt module skeleton | [`module-billing-orders-nuxt`](https://github.com/liberusoftware/module-billing-orders-nuxt) (`@liberusoftware/module-billing-orders-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Quotes** | Expose composable and Vue 3 component for `quotes` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Carts** | Expose composable and Vue 3 component for `carts` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Checkout** | Expose composable and Vue 3 component for `checkout` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Fraud review** | Expose composable and Vue 3 component for `fraud review` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Agreements** | Expose composable and Vue 3 component for `agreements` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Order state** | Expose composable and Vue 3 component for `order state` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |
| **Change orders** | Expose composable and Vue 3 component for `change orders` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/orders.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-billing-laravel-api`. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ListOrders.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-orders/src/Queries/ListOrders.php) | `public function execute(?int $teamId, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddChangeOrder.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-orders/src/Actions/AddChangeOrder.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Order $order, array $change): Order` |
| [CheckoutCart.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-orders/src/Actions/CheckoutCart.php) | `public function __construct(private DatabaseManager $database, private CreateOrder $createOrder)`<br>`public function execute(Cart $cart, array $attributes): Order` |
| [ConvertQuoteToOrder.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-orders/src/Actions/ConvertQuoteToOrder.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Quote $quote): Order` |
| [CreateCart.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-orders/src/Actions/CreateCart.php) | `public function execute(array $attributes): Cart` |
| [CreateOrder.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-orders/src/Actions/CreateOrder.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): Order` |
| [CreateQuote.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-orders/src/Actions/CreateQuote.php) | `public function execute(array $attributes): Quote` |
| [ExpireQuotes.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-orders/src/Actions/ExpireQuotes.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(?int $teamId = null): int` |
| [ReviewFraud.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-orders/src/Actions/ReviewFraud.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Order $order, FraudReviewStatus $status): Order` |
| [TransitionOrder.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-orders/src/Actions/TransitionOrder.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Order $order, OrderStatus $status, ?FraudReviewStatus $fraudStatus = null): Order` |
| [TransitionQuote.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-orders/src/Actions/TransitionQuote.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Quote $quote, string $status): Quote` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Cart.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-orders/src/Models/Cart.php) | No literal fillable array detected; inspect the model and API schema. |
| [Order.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-orders/src/Models/Order.php) | No literal fillable array detected; inspect the model and API schema. |
| [Quote.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-orders/src/Models/Quote.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [OrderController.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-orders-api/src/Http/Controllers/OrderController.php) | `public function index(Request $request, ListOrders $query): JsonResponse`<br>`public function store(Request $request, CreateOrder $create): JsonResponse`<br>`public function quote(Request $request, CreateQuote $create): JsonResponse`<br>`public function cart(Request $request, CreateCart $create): JsonResponse`<br>`public function quoteTransition(Request $request, int $quote, TransitionQuote $transition): JsonResponse`<br>`public function convertQuote(Request $request, int $quote, ConvertQuoteToOrder $convert): JsonResponse`<br>`public function expireQuotes(Request $request, ExpireQuotes $expire): JsonResponse`<br>`public function checkout(Request $request, Cart $cart, CheckoutCart $checkout): JsonResponse`<br>`public function fraud(Request $request, Order $order, ReviewFraud $review): JsonResponse`<br>`public function change(Request $request, Order $order, AddChangeOrder $add): JsonResponse` |

**Observed route declarations:**

[modules/module-billing-orders-api/routes/api.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-orders-api/routes/api.php)

```php
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.orders.read'])->prefix('api/v1/billing/orders')->name('billing.orders.')->group(fn () => Route::get('/', [OrderController::class, 'index'])->name('orders.index'));
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.orders.write', 'idempotency'])->prefix('api/v1/billing/orders')->name('billing.orders.')->group(fn () => Route::post('/', [OrderController::class, 'store'])->name('orders.store'));
Route::middleware(['api', 'throttle:api', 'auth:sanctum', 'ability:billing.orders.write', 'idempotency'])->prefix('api/v1/billing/orders')->name('billing.orders.')->group(function (): void {
Route::post('/quotes', [OrderController::class, 'quote'])->name('quotes.store');
Route::patch('/quotes/{quote}/lifecycle', [OrderController::class, 'quoteTransition'])->whereNumber('quote')->name('quotes.lifecycle');
Route::post('/quotes/{quote}/convert', [OrderController::class, 'convertQuote'])->whereNumber('quote')->name('quotes.convert');
Route::post('/quotes/expire', [OrderController::class, 'expireQuotes'])->name('quotes.expire');
Route::post('/carts', [OrderController::class, 'cart'])->name('carts.store');
Route::post('/carts/{cart}/checkout', [OrderController::class, 'checkout'])->name('carts.checkout');
Route::post('/{order}/fraud-review', [OrderController::class, 'fraud'])->name('fraud-review');
Route::post('/{order}/change-orders', [OrderController::class, 'change'])->name('change-orders.store');
```
<!-- layer-implementation-plan:end -->
