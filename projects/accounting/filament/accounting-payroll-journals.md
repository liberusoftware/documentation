# Accounting: Accounting Payroll Journals Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-payroll-journals). Observed identity: [`liberusoftware/module-accounting-payroll-journals-filament`](../../../modules/source/liberusoftware--module-accounting-payroll-journals-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accounting-payroll-journals-filament`  
**Matching domain module:** `accounting-payroll-journals`  
**Application:** Accounting  
**Source feature:** [Accounting Payroll Journals](../features/accounting-payroll-journals.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-payroll-journals` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Gross pay:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Taxes:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Deductions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Benefits:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Employer costs:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Net pay:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Liabilities:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Allocation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Posting:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reversal:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Corrections:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accounting-payroll-journals-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `gross-pay`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `taxes`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `deductions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `benefits`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `employer-costs`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `net-pay`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `liabilities`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `allocation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `posting`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reversal`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `corrections`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-payroll-journals` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-payroll-journals-filament`](https://github.com/liberusoftware/module-accounting-payroll-journals-filament) (`liberusoftware/accounting-payroll-journals-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-payroll-journals.md) · [API plan](../api/accounting-payroll-journals.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Gross pay** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `gross pay`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Taxes** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `taxes`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Deductions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `deductions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Benefits** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `benefits`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Employer costs** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `employer costs`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Net pay** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `net pay`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Liabilities** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `liabilities`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Allocation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `allocation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Posting** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `posting`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reversal** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reversal`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Corrections** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `corrections`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [PayrollJournalsFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-journals-filament/src/PayrollJournalsFilamentPlugin.php) · [PayrollJournalsFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-journals-filament/src/PayrollJournalsFilamentServiceProvider.php) · [PayrollJournalResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-journals-filament/src/Resources/PayrollJournalResource.php) · [ListPayrollJournals.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-journals-filament/src/Resources/PayrollJournalResource/Pages/ListPayrollJournals.php).

| Observed core query | Public method signatures |
| --- | --- |
| [PayrollJournalSummary.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-journals/src/Queries/PayrollJournalSummary.php) | `public function forTeam(?int $teamId = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreatePayrollJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-journals/src/Actions/CreatePayrollJournal.php) | `public function handle(array $attributes): PayrollJournal` |
| [PostPayrollJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-journals/src/Actions/PostPayrollJournal.php) | `public function handle(PayrollJournal $journal): PayrollJournal` |
| [ReversePayrollJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-journals/src/Actions/ReversePayrollJournal.php) | `public function handle(PayrollJournal $journal, string $reversalRef): PayrollJournal` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [PayrollJournal.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-payroll-journals/src/Models/PayrollJournal.php) | `team_id`, `journal_ref`, `payroll_period_start`, `payroll_period_end`, `currency`, `gross_pay`, `taxes`, `deductions`, `benefits`, `employer_costs`, `net_pay`, `liabilities`, `allocation`, `status`, `posted_at`, `reversed_at`, `reversal_ref`, `correction_ref`, `metadata` |
<!-- layer-implementation-plan:end -->
