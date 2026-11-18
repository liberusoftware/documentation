# Billing: Module Billing Payments Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-billing-payments). Observed identity: [`liberusoftware/module-billing-payments-filament`](../../../modules/source/liberusoftware--module-billing-payments-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-billing-module-billing-payments-filament`  
**Matching domain module:** `module-billing-payments`  
**Application:** Billing  
**Source feature:** [Module Billing Payments](../features/module-billing-payments.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `module-billing-payments` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Unified payment-contracts and payment-core integration:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Methods and vaulted payment instruments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Mandates and Direct Debit lifecycles:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Gateway drivers and capability discovery:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Capture and allocation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Refunds and disputes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reconciliation:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-billing-module-billing-payments-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `unified-payment-contracts-and-payment-core-integration`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `methods-and-vaulted-payment-instruments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `mandates-and-direct-debit-lifecycles`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `gateway-drivers-and-capability-discovery`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `capture-and-allocation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `refunds-and-disputes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reconciliation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `module-billing-payments` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-billing-laravel-filament`](https://github.com/liberusoftware/project-billing-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-billing-payments-filament`](https://github.com/liberusoftware/module-billing-payments-filament) (`liberusoftware/billing-payments-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/module-billing-payments.md) · [API plan](../api/module-billing-payments.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Unified payment-contracts and payment-core integration** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `unified payment-contracts and payment-core integration`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Methods and vaulted payment instruments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `methods and vaulted payment instruments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Mandates and Direct Debit lifecycles** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `mandates and direct debit lifecycles`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Gateway drivers and capability discovery** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `gateway drivers and capability discovery`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Capture and allocation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `capture and allocation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Refunds and disputes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `refunds and disputes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reconciliation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reconciliation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [PaymentsFilamentPlugin.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments-filament/src/PaymentsFilamentPlugin.php) · [PaymentsFilamentServiceProvider.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments-filament/src/PaymentsFilamentServiceProvider.php) · [PaymentAllocationResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments-filament/src/Resources/PaymentAllocationResource.php) · [ListPaymentAllocations.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments-filament/src/Resources/PaymentAllocationResource/Pages/ListPaymentAllocations.php) · [PaymentDisputeResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments-filament/src/Resources/PaymentDisputeResource.php) · [ListPaymentDisputes.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments-filament/src/Resources/PaymentDisputeResource/Pages/ListPaymentDisputes.php) · [PaymentMandateResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments-filament/src/Resources/PaymentMandateResource.php) · [CreatePaymentMandate.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments-filament/src/Resources/PaymentMandateResource/Pages/CreatePaymentMandate.php) · [ListPaymentMandates.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments-filament/src/Resources/PaymentMandateResource/Pages/ListPaymentMandates.php) · [PaymentMethodResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments-filament/src/Resources/PaymentMethodResource.php) · [CreatePaymentMethod.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments-filament/src/Resources/PaymentMethodResource/Pages/CreatePaymentMethod.php) · [ListPaymentMethods.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments-filament/src/Resources/PaymentMethodResource/Pages/ListPaymentMethods.php) · [PaymentReconciliationResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments-filament/src/Resources/PaymentReconciliationResource.php) · [ListPaymentReconciliations.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments-filament/src/Resources/PaymentReconciliationResource/Pages/ListPaymentReconciliations.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ListPayments.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Queries/ListPayments.php) | `public function execute(?int $teamId, int $perPage = 25): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AllocatePayment.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/AllocatePayment.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Payment $payment, int $amountMinor, ?int $invoiceId = null): PaymentAllocation` |
| [CapturePayment.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/CapturePayment.php) | `public function __construct(private DatabaseManager $database, private GatewayManager $gateways)`<br>`public function execute(Payment $payment): Payment` |
| [CreatePayment.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/CreatePayment.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): Payment` |
| [CreatePaymentMandate.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/CreatePaymentMandate.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): PaymentMandate` |
| [CreatePaymentMethod.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/CreatePaymentMethod.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(array $attributes): PaymentMethod` |
| [OpenDispute.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/OpenDispute.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Payment $payment, int $amountMinor, string $reason): PaymentDispute` |
| [ReconcilePayment.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/ReconcilePayment.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(Payment $payment, string $providerReference, bool $matched = true, ?string $notes = null): PaymentReconciliation` |
| [RefundPayment.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/RefundPayment.php) | `public function __construct(private DatabaseManager $database, private GatewayManager $gateways)`<br>`public function execute(Payment $payment, int $amountMinor, string $reason = 'requested'): PaymentRefund` |
| [TransitionPaymentMandate.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/TransitionPaymentMandate.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(PaymentMandate $mandate, string $status): PaymentMandate` |
| [TransitionPaymentMethod.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Actions/TransitionPaymentMethod.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(PaymentMethod $method, PaymentMethodStatus $status): PaymentMethod` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Payment.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Models/Payment.php) | No literal fillable array detected; inspect the model and API schema. |
| [PaymentAllocation.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Models/PaymentAllocation.php) | No literal fillable array detected; inspect the model and API schema. |
| [PaymentDispute.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Models/PaymentDispute.php) | No literal fillable array detected; inspect the model and API schema. |
| [PaymentMandate.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Models/PaymentMandate.php) | No literal fillable array detected; inspect the model and API schema. |
| [PaymentMethod.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Models/PaymentMethod.php) | No literal fillable array detected; inspect the model and API schema. |
| [PaymentReconciliation.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Models/PaymentReconciliation.php) | No literal fillable array detected; inspect the model and API schema. |
| [PaymentRefund.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-payments/src/Models/PaymentRefund.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
