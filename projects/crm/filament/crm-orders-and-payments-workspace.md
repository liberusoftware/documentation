# CRM: Crm Orders And Payments Workspace Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-orders-and-payments-workspace). Observed identity: [`liberusoftware/module-crm-orders-and-payments-workspace-filament`](../../../modules/source/liberusoftware--module-crm-orders-and-payments-workspace-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-crm-orders-and-payments-workspace-filament`  
**Matching domain module:** `crm-orders-and-payments-workspace`  
**Application:** CRM  
**Source feature:** [Crm Orders And Payments Workspace](../features/crm-orders-and-payments-workspace.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-orders-and-payments-workspace` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Payment links:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Deposits:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Order/subscription references:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Invoice/payment status:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Refunds/disputes visibility:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Billing/Ecommerce handoff:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-crm-orders-and-payments-workspace-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `payment-links`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `deposits`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `order-subscription-references`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `invoice-payment-status`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `refunds-disputes-visibility`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `billing-ecommerce-handoff`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-orders-and-payments-workspace` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-orders-and-payments-workspace-filament`](https://github.com/liberusoftware/module-crm-orders-and-payments-workspace-filament) (`liberusoftware/crm-orders-and-payments-workspace-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-orders-and-payments-workspace.md) · [API plan](../api/crm-orders-and-payments-workspace.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Payment links** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `payment links`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Deposits** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `deposits`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Order/subscription references** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `order/subscription references`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Invoice/payment status** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `invoice/payment status`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Refunds/disputes visibility** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `refunds/disputes visibility`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Billing/Ecommerce handoff** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `billing/ecommerce handoff`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [OrdersAndPaymentsWorkspaceFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-orders-and-payments-workspace-filament/src/OrdersAndPaymentsWorkspaceFilamentServiceProvider.php) · [CreatePaymentTransaction.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-orders-and-payments-workspace-filament/src/Resources/Pages/CreatePaymentTransaction.php) · [EditPaymentTransaction.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-orders-and-payments-workspace-filament/src/Resources/Pages/EditPaymentTransaction.php) · [ListPaymentTransactions.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-orders-and-payments-workspace-filament/src/Resources/Pages/ListPaymentTransactions.php) · [PaymentTransactionResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-orders-and-payments-workspace-filament/src/Resources/PaymentTransactionResource.php).

| Observed core query | Public method signatures |
| --- | --- |
| [TransactionQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-orders-and-payments-workspace/src/Queries/TransactionQuery.php) | `public function forTeam(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateTransaction.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-orders-and-payments-workspace/src/Actions/CreateTransaction.php) | `public function __construct(private readonly OrdersPaymentsPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PaymentTransaction` |
| [RecordPaymentEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-orders-and-payments-workspace/src/Actions/RecordPaymentEvent.php) | `public function __construct(private readonly OrdersPaymentsPolicy $policy)`<br>`public function execute(int $teamId, int $userId, PaymentTransaction $transaction, array $input): PaymentEvent` |
| [OrdersPaymentsPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-orders-and-payments-workspace/src/Services/OrdersPaymentsPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PaymentEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-orders-and-payments-workspace/src/Models/PaymentEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [PaymentTransaction.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-orders-and-payments-workspace/src/Models/PaymentTransaction.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
