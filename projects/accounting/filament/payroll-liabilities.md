# Accounting: Payroll Liabilities Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#payroll-liabilities). Observed identity: [`liberusoftware/module-accounting-payroll-liabilities-filament`](../../../modules/source/liberusoftware--module-accounting-payroll-liabilities-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-payroll-liabilities-filament`  
**Matching domain module:** `accounting-payroll-liabilities`  
**Application:** Accounting  
**Source feature:** [Payroll Liabilities](../features/payroll-liabilities.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-payroll-liabilities` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Agency/payee balances:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Due dates:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Payments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Allocations:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Exceptions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reconciliation:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-payroll-liabilities-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `agency-payee-balances`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `due-dates`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `payments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `allocations`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `exceptions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reconciliation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-payroll-liabilities` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-payroll-liabilities-filament`](https://github.com/liberusoftware/module-accounting-payroll-liabilities-filament) (`liberusoftware/accounting-payroll-liabilities-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/payroll-liabilities.md) · [API plan](../api/payroll-liabilities.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Agency/payee balances** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `agency/payee balances`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Due dates** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `due dates`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Payments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `payments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Allocations** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `allocations`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Exceptions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `exceptions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reconciliation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reconciliation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [PayrollLiabilitiesFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-liabilities-filament/src/PayrollLiabilitiesFilamentPlugin.php) · [PayrollLiabilitiesFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-liabilities-filament/src/PayrollLiabilitiesFilamentServiceProvider.php) · [PayrollLiabilityResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-liabilities-filament/src/Resources/PayrollLiabilityResource.php) · [ListPayrollLiabilities.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-liabilities-filament/src/Resources/PayrollLiabilityResource/Pages/ListPayrollLiabilities.php).

| Observed core query | Public method signatures |
| --- | --- |
| [PayrollLiabilitySummary.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-liabilities/src/Queries/PayrollLiabilitySummary.php) | `public function forTeam(?int $teamId = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AllocatePayrollLiability.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-liabilities/src/Actions/AllocatePayrollLiability.php) | `public function handle(PayrollLiability $liability, float $amount, string $allocationRef): PayrollLiability` |
| [RecordPayrollLiability.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-liabilities/src/Actions/RecordPayrollLiability.php) | `public function handle(array $attributes): PayrollLiability` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PayrollLiability.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-liabilities/src/Models/PayrollLiability.php) | `team_id`, `agency_ref`, `payee_ref`, `liability_ref`, `currency`, `amount`, `paid_amount`, `due_on`, `status`, `payment_ref`, `allocation_ref`, `exception_code`, `exception_message`, `reconciliation_ref`, `reconciled_at`, `metadata` |
<!-- layer-implementation-plan:end -->
