# Billing: Module Billing Orders Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-billing-orders). Observed identity: [`liberusoftware/module-billing-orders-filament`](../../../modules/source/liberusoftware--module-billing-orders-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-billing-module-billing-orders-filament`  
**Matching domain module:** `module-billing-orders`  
**Application:** Billing  
**Source feature:** [Module Billing Orders](../features/module-billing-orders.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `module-billing-orders` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Quotes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Carts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Checkout:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Fraud review:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Agreements:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Order state:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Change orders:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-billing-module-billing-orders-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `quotes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `carts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `checkout`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `fraud-review`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `agreements`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `order-state`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `change-orders`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `module-billing-orders` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-billing-laravel-filament`](https://github.com/liberusoftware/project-billing-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-billing-orders-filament`](https://github.com/liberusoftware/module-billing-orders-filament) (`liberusoftware/billing-orders-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/module-billing-orders.md) · [API plan](../api/module-billing-orders.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Quotes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `quotes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Carts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `carts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Checkout** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `checkout`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Fraud review** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `fraud review`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Agreements** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `agreements`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Order state** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `order state`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Change orders** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `change orders`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [OrdersFilamentPlugin.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-orders-filament/src/OrdersFilamentPlugin.php) · [OrdersFilamentServiceProvider.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-orders-filament/src/OrdersFilamentServiceProvider.php) · [CartResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-orders-filament/src/Resources/CartResource.php) · [CreateCart.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-orders-filament/src/Resources/CartResource/Pages/CreateCart.php) · [ListCarts.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-orders-filament/src/Resources/CartResource/Pages/ListCarts.php) · [OrderResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-orders-filament/src/Resources/OrderResource.php) · [CreateOrder.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-orders-filament/src/Resources/OrderResource/Pages/CreateOrder.php) · [ListOrders.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-orders-filament/src/Resources/OrderResource/Pages/ListOrders.php) · [QuoteResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-orders-filament/src/Resources/QuoteResource.php) · [CreateQuote.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-orders-filament/src/Resources/QuoteResource/Pages/CreateQuote.php) · [ListQuotes.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-orders-filament/src/Resources/QuoteResource/Pages/ListQuotes.php).

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
