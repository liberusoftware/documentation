# Billing: Orders React + Inertia

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#orders). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one React/Inertia implementation

**Package:** `module-billing-orders-react-inertia`
**Matching domain module:** `billing-orders`
**Application:** Billing
**Source feature:** [Orders](../features/orders.md)
**Architecture:** [REACT.md](../../../standards/REACT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/orders.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional React 19.2 + Inertia 3 presentation package adapts the matching domain contract through Laravel-owned Inertia routes. It contributes reusable Inertia pages, React components, hooks, typed API adapters, forms, and actions to application-owned Laravel applications while delegating authentication, authorization, validation, team context, persistence, and business rules to the matching public application/API boundary. It must not contain another module's UI, private Laravel model access, or application-specific `App\` coupling.

## 2. Module-specific surfaces

- **Quotes:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Carts:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Checkout:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Fraud review:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Agreements:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Order state:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.
- **Change orders:** page, component, hook, form, and failure-state behavior for this module's authorized workflow.

## 3. React 19.2 + Inertia 3 implementation

- Register a stable `module-billing-orders-react-inertia` package and expose only explicitly prefixed public exports; applications compose it explicitly.
- Keep Inertia pages under `resources/js/Pages`, shared UI under `resources/js/Components`, hooks under `resources/js/hooks`, typed contracts under `resources/js/types`, and transport/error adapters under `resources/js/lib`.
- Use `createInertiaApp`, `Link`, `router`, `useForm`, typed page props, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted Laravel/API context and fail closed when required context is missing.

### Capability mapping

- `quotes`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `carts`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `checkout`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `fraud-review`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `agreements`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `order-state`: map the matching API query/action to a focused React page, component, hook, or Inertia form.
- `change-orders`: map the matching API query/action to a focused React page, component, hook, or Inertia form.

## 4. API contract and Inertia consumption

<!-- inertia-transport:start -->
### Inertia transport boundary

Use Laravel-owned Inertia page/command routes for visits and forms. The controller can invoke the module's public application actions in the same host or use a deliberate API adapter, then return an Inertia page/redirect response. A bare REST JSON resource response is not an Inertia page. Keep authoritative domain authorization and validation in the owning boundary for either path.

Independent API consumers and Next.js use their reviewed HTTP/session integration. Share DTOs and framework-independent UI primitives; keep Inertia page props, visits, form errors and redirects in the Inertia wrapper. Do not introduce loopback HTTP solely to reuse a public action inside the same Laravel host.

See the [Inertia standard](../../../standards/INERTIA.md), [request lifecycle](https://inertiajs.com/docs/v3/core-concepts/how-it-works) and [redirect behavior](https://inertiajs.com/docs/v3/the-basics/redirects).
<!-- inertia-transport:end -->

- Reuse the matching public application/API contracts. For HTTP consumption, use its documented schemas, routes, authentication, permissions, tenant context, errors and operation semantics; Inertia visits still require an Inertia response.
- Keep a typed module-local API client and hooks boundary; use Inertia visits for page transitions and `useForm`/`router` for mutations, preserving server validation and redirect semantics.
- Forward Sanctum cookies or approved authorization headers through a controlled first-party boundary; never persist long-lived tokens in browser storage or expose secrets in page props.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, SSR hydration where enabled, and minimal-host installation tests.
- Test observable behavior with TypeScript, ESLint, Vitest, React Testing Library, Playwright, and the supported Laravel/Inertia stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `billing-orders` one-to-one.
- Every required route or application surface has an explicit page/component/hook/form/API-action mapping and no undeclared surface is discovered.
- Production asset/SSR build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Inertia React host skeleton | [`project-billing-laravel-inertia-react`](https://github.com/liberusoftware/project-billing-laravel-inertia-react) | Laravel 13 + Inertia 3 + React 19.2 host shell, web/session/CSRF routes, and Vite build ([template](https://github.com/liberusoftware/project-boilerplate-laravel-inertia-react) · [wayfinder](../../wayfinders/laravel-inertia-react.md) · [runbook](../../../guides/presentation/INERTIA.md)) |
| Capability React Inertia module skeleton | [`module-billing-orders-react-inertia`](https://github.com/liberusoftware/module-billing-orders-react-inertia) (`@liberusoftware/module-billing-orders-react-inertia`) | Reusable Inertia React pages, hooks, forms, and framework-independent React UI ([foundation](https://github.com/liberusoftware/module-boilerplate-react-inertia) · [catalog](../../../modules/skeletons/laravel-inertia-react.md)) |
| Shared React reuse | [Next.js plan](../nextjs/orders.md) · [Core plan](../core/orders.md) · [API plan](../api/orders.md) | Share presentational React components and DTO types with Next.js while keeping Inertia navigation/forms in this adapter |

### React 19.2 + Inertia 3 feature and component matrix

| Feature / aspect | Inertia React page, shared component & hook contract | Laravel controller, `useForm` mutation & recovery contract |
| --- | --- | --- |
| **Quotes** | Render `quotes` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Carts** | Render `carts` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Checkout** | Render `checkout` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Fraud review** | Render `fraud review` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Agreements** | Render `agreements` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Order state** | Render `order state` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |
| **Change orders** | Render `change orders` with typed Inertia page props (`resources/js/Pages`) and framework-neutral React components (`resources/js/Components`). | Submit commands via Inertia `useForm`/`router` to Laravel session/CSRF routes; map validation (422), conflict (409/412), and pending operations without losing draft state. |

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
