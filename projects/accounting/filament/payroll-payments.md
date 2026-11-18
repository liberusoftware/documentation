# Accounting: Payroll Payments Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#payroll-payments). Observed identity: [`liberusoftware/module-accounting-payroll-payments-filament`](../../../modules/source/liberusoftware--module-accounting-payroll-payments-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-payroll-payments-filament`  
**Matching domain module:** `accounting-payroll-payments`  
**Application:** Accounting  
**Source feature:** [Payroll Payments](../features/payroll-payments.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-payroll-payments` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Net-pay and liability batch references:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Approvals:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Bank/provider status:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Failures:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Bank reconciliation:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-payroll-payments-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `net-pay-and-liability-batch-references`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `approvals`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `bank-provider-status`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `failures`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `bank-reconciliation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-payroll-payments` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-payroll-payments-filament`](https://github.com/liberusoftware/module-accounting-payroll-payments-filament) (`liberusoftware/accounting-payroll-payments-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/payroll-payments.md) · [API plan](../api/payroll-payments.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Net-pay and liability batch references** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `net-pay and liability batch references`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Approvals** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `approvals`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Bank/provider status** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `bank/provider status`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Failures** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `failures`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Bank reconciliation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `bank reconciliation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [PayrollPaymentsFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-payments-filament/src/PayrollPaymentsFilamentPlugin.php) · [PayrollPaymentsFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-payments-filament/src/PayrollPaymentsFilamentServiceProvider.php) · [PayrollPaymentBatchResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-payments-filament/src/Resources/PayrollPaymentBatchResource.php) · [ListPayrollPaymentBatches.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-payments-filament/src/Resources/PayrollPaymentBatchResource/Pages/ListPayrollPaymentBatches.php).

| Observed core query | Public method signatures |
| --- | --- |
| [PayrollPaymentSummary.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-payments/src/Queries/PayrollPaymentSummary.php) | `public function forTeam(?int $teamId = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreatePayrollPaymentBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-payments/src/Actions/CreatePayrollPaymentBatch.php) | `public function handle(array $attributes): PayrollPaymentBatch` |
| [TransitionPayrollPayment.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-payments/src/Actions/TransitionPayrollPayment.php) | `public function handle(PayrollPaymentBatch $batch, PaymentStatus $status, ?array $details = null): PayrollPaymentBatch` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PayrollPaymentBatch.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-payments/src/Models/PayrollPaymentBatch.php) | `team_id`, `batch_ref`, `net_pay_ref`, `liability_ref`, `currency`, `net_pay_amount`, `liability_amount`, `status`, `provider`, `provider_payment_ref`, `failure_code`, `failure_message`, `approved_by`, `approved_at`, `submitted_at`, `settled_at`, `reconciled_at`, `reconciliation_ref`, `metadata` |
<!-- layer-implementation-plan:end -->
