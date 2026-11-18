# Accounting: Accounting Bill Payments Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-bill-payments). Observed identity: [`liberusoftware/module-accounting-bill-payments-filament`](../../../modules/source/liberusoftware--module-accounting-bill-payments-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accounting-bill-payments-filament`  
**Matching domain module:** `accounting-bill-payments`  
**Application:** Accounting  
**Source feature:** [Accounting Bill Payments](../features/accounting-bill-payments.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-bill-payments` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Payment proposals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Due-date/discount optimization:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Bank details validation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Maker-checker approval:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Files/APIs:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Remittances:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Status:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accounting-bill-payments-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `payment-proposals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `due-date-discount-optimization`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `bank-details-validation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `maker-checker-approval`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `files-apis`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `remittances`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `status`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-bill-payments` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-bill-payments-filament`](https://github.com/liberusoftware/module-accounting-bill-payments-filament) (`liberusoftware/accounting-bill-payments-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-bill-payments.md) · [API plan](../api/accounting-bill-payments.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Payment proposals** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `payment proposals`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Due-date/discount optimization** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `due-date/discount optimization`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Bank details validation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `bank details validation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Maker-checker approval** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `maker-checker approval`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Files/APIs** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `files/apis`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Remittances** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `remittances`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Status** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `status`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [BillPaymentsFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments-filament/src/BillPaymentsFilamentPlugin.php) · [BillPaymentsFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments-filament/src/BillPaymentsFilamentServiceProvider.php) · [BillPaymentResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments-filament/src/Resources/BillPaymentResource.php).

| Observed core query | Public method signatures |
| --- | --- |
| [BillPaymentOptimizationQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Queries/BillPaymentOptimizationQuery.php) | `public function handle(BillPaymentProposal $payment): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApproveBillPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Actions/ApproveBillPayment.php) | `public function handle(BillPaymentProposal $payment): BillPaymentProposal` |
| [CreateBillPaymentProposal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Actions/CreateBillPaymentProposal.php) | `public function handle(array $attributes): BillPaymentProposal` |
| [MarkBillPaymentPaid.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Actions/MarkBillPaymentPaid.php) | `public function handle(BillPaymentProposal $payment): BillPaymentProposal` |
| [RejectBillPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Actions/RejectBillPayment.php) | `public function handle(BillPaymentProposal $payment, string $reason): BillPaymentProposal` |
| [RequestBillPaymentApproval.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Actions/RequestBillPaymentApproval.php) | `public function handle(BillPaymentProposal $payment): BillPaymentProposal` |
| [SubmitBillPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Actions/SubmitBillPayment.php) | `public function handle(BillPaymentProposal $payment, PaymentProviderAdapter $adapter): BillPaymentProposal` |
| [BillPaymentsPolicy.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments-api/src/Policies/BillPaymentsPolicy.php) | `public function viewAny(?object $user = null): bool`<br>`public function view(?object $user, object $payment): bool`<br>`public function create(?object $user = null): bool`<br>`public function update(?object $user, object $payment): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [BillPaymentProposal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments/src/Models/BillPaymentProposal.php) | `team_id`, `supplier_id`, `bill_reference`, `amount`, `currency`, `due_date`, `discount_date`, `discount_rate`, `payment_date`, `bank_details`, `provider`, `provider_connection_id`, `payment_payload`, `idempotency_key`, `status`, `requested_by`, `approved_by`, `approved_at`, `submitted_at`, `paid_at`, `rejected_at`, `failure_code`, `failure_message`, `provider_reference`, `provider_result`, `remittance_reference`, `remittance_sent_at`, `metadata` |
| [Bill.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments-api/src/Models/Bill.php) | `vendor_id`, `bill_number`, `bill_date`, `due_date`, `subtotal_amount`, `tax_amount`, `total_amount`, `amount_paid`, `tax_rate_id`, `status`, `payment_status`, `purchase_order_id`, `reference_number`, `notes`, `document_path`, `approved_by`, `approved_at`, `approval_status`, `rejection_reason`, `team_id`, `is_recurring`, `recurrence_frequency`, `recurrence_start`, `recurrence_end`, `last_generated`, `qbo_id`, `qbo_sync_token`, `xero_id`, `sage_id` |
| [BillPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-bill-payments-api/src/Models/BillPayment.php) | `bill_id`, `payment_date`, `amount`, `payment_method`, `reference_number`, `bank_account_id`, `notes` |
<!-- layer-implementation-plan:end -->
