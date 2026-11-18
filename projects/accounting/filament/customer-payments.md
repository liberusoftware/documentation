# Accounting: Customer Payments Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#customer-payments). Observed identity: [`liberusoftware/module-accounting-customer-payments-filament`](../../../modules/source/liberusoftware--module-accounting-customer-payments-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-customer-payments-filament`  
**Matching domain module:** `accounting-customer-payments`  
**Application:** Accounting  
**Source feature:** [Customer Payments](../features/customer-payments.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-customer-payments` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Receipts and online payment links via payment-contracts:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Gateway/bank references and provider provenance:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Deposits and undeposited funds clearing:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Allocations and partial/overpayments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Refunds and chargeback adjustments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reconciliation with merchant settlements:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-customer-payments-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `receipts-and-online-payment-links-via-payment-contracts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `gateway-bank-references-and-provider-provenance`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `deposits-and-undeposited-funds-clearing`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `allocations-and-partial-overpayments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `refunds-and-chargeback-adjustments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reconciliation-with-merchant-settlements`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-customer-payments` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-customer-payments-filament`](https://github.com/liberusoftware/module-accounting-customer-payments-filament) (`liberusoftware/accounting-customer-payments-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/customer-payments.md) · [API plan](../api/customer-payments.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Receipts and online payment links via payment-contracts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `receipts and online payment links via payment-contracts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Gateway/bank references and provider provenance** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `gateway/bank references and provider provenance`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Deposits and undeposited funds clearing** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `deposits and undeposited funds clearing`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Allocations and partial/overpayments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `allocations and partial/overpayments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Refunds and chargeback adjustments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `refunds and chargeback adjustments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reconciliation with merchant settlements** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reconciliation with merchant settlements`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [CustomerPaymentsFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-payments-filament/src/CustomerPaymentsFilamentPlugin.php) · [CustomerPaymentsFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-payments-filament/src/CustomerPaymentsFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [CustomerPaymentQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-payments/src/Queries/CustomerPaymentQuery.php) | `public function forTeam(int $teamId): Collection`<br>`public function forCustomer(int $teamId, string $customerId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AllocateCustomerPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-payments/src/Actions/AllocateCustomerPayment.php) | `public function handle(CustomerPayment $payment, string $documentRef, float $amount): CustomerPaymentAllocation` |
| [ReconcileCustomerPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-payments/src/Actions/ReconcileCustomerPayment.php) | `public function handle(CustomerPayment $payment, string $depositReference): CustomerPayment` |
| [RecordCustomerPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-payments/src/Actions/RecordCustomerPayment.php) | `public function handle(array $attributes): CustomerPayment` |
| [RefundCustomerPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-payments/src/Actions/RefundCustomerPayment.php) | `public function handle(CustomerPayment $payment, float $amount): CustomerPayment` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CustomerPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-payments/src/Models/CustomerPayment.php) | `team_id`, `customer_id`, `kind`, `reference`, `status`, `currency`, `amount`, `allocated_amount`, `refunded_amount`, `gateway_reference`, `deposit_reference`, `metadata` |
| [CustomerPaymentAllocation.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-payments/src/Models/CustomerPaymentAllocation.php) | `payment_id`, `team_id`, `document_ref`, `amount` |
| [Customer.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-customer-payments-api/src/Models/Customer.php) | `customer_name`, `customer_last_name`, `customer_address`, `customer_email`, `customer_phone`, `customer_city`, `credit_hold`, `qbo_id`, `sage_id`, `xero_id`, `team_id` |
<!-- layer-implementation-plan:end -->
