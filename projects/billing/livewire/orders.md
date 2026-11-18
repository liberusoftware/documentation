# Billing: Orders Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#orders). Observed identity: [`liberusoftware/module-billing-orders-livewire`](../../../modules/source/liberusoftware--module-billing-orders-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-billing-orders-livewire`  
**Matching domain module:** `billing-orders`  
**Application:** Billing  
**Source feature:** [Orders](../features/orders.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Quotes:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Carts:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Checkout:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Fraud review:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Agreements:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Order state:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Change orders:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-billing-orders-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-billing-orders::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `quotes`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `carts`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `checkout`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `fraud-review`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `agreements`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `order-state`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `change-orders`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `billing-orders` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-billing-laravel-filament`](https://github.com/liberusoftware/project-billing-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/orders.md) · [API plan](../api/orders.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Quotes** | Expose a focused Livewire 4 component and namespaced Blade default view for `quotes` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Carts** | Expose a focused Livewire 4 component and namespaced Blade default view for `carts` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Checkout** | Expose a focused Livewire 4 component and namespaced Blade default view for `checkout` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Fraud review** | Expose a focused Livewire 4 component and namespaced Blade default view for `fraud review` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Agreements** | Expose a focused Livewire 4 component and namespaced Blade default view for `agreements` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Order state** | Expose a focused Livewire 4 component and namespaced Blade default view for `order state` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Change orders** | Expose a focused Livewire 4 component and namespaced Blade default view for `change orders` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [OrderList.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-orders-livewire/src/Components/OrderList.php) · [OrderSupport.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-orders-livewire/src/Components/OrderSupport.php) · [QuoteList.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-orders-livewire/src/Components/QuoteList.php) · [OrdersLivewireServiceProvider.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-orders-livewire/src/OrdersLivewireServiceProvider.php).

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
<!-- layer-implementation-plan:end -->
