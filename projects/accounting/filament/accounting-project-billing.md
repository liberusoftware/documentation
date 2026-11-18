# Accounting: Accounting Project Billing Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-project-billing). Observed identity: [`liberusoftware/module-accounting-project-billing-filament`](../../../modules/source/liberusoftware--module-accounting-project-billing-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accounting-project-billing-filament`  
**Matching domain module:** `accounting-project-billing`  
**Application:** Accounting  
**Source feature:** [Accounting Project Billing](../features/accounting-project-billing.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-project-billing` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Fixed fee:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Time/material:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Milestone:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Progress:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Retainer:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Billable time/expense:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Write-up/down:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Invoice handoff:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accounting-project-billing-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `fixed-fee`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `time-material`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `milestone`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `progress`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `retainer`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `billable-time-expense`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `write-up-down`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `invoice-handoff`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-project-billing` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-project-billing-filament`](https://github.com/liberusoftware/module-accounting-project-billing-filament) (`liberusoftware/accounting-project-billing-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-project-billing.md) · [API plan](../api/accounting-project-billing.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Fixed fee** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `fixed fee`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Time/material** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `time/material`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Milestone** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `milestone`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Progress** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `progress`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Retainer** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `retainer`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Billable time/expense** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `billable time/expense`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Write-up/down** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `write-up/down`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Invoice handoff** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `invoice handoff`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ProjectBillingFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-billing-filament/src/ProjectBillingFilamentPlugin.php) · [ProjectBillingFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-billing-filament/src/ProjectBillingFilamentServiceProvider.php) · [ListProjectBilling.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-billing-filament/src/Resources/Pages/ListProjectBilling.php) · [ProjectBillingResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-billing-filament/src/Resources/ProjectBillingResource.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ProjectBillingSummary.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-billing/src/Queries/ProjectBillingSummary.php) | `public function forProject(int $projectJobId, ?int $teamId = null): array`<br>`public function summarize(Collection $rows): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [HandoffProjectBilling.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-billing/src/Actions/HandoffProjectBilling.php) | `public function handle(ProjectBilling $billing, ?string $invoiceRef = null): ProjectBilling` |
| [RecordProjectBilling.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-billing/src/Actions/RecordProjectBilling.php) | `public function handle(array $attributes): ProjectBilling` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ProjectBilling.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-billing/src/Models/ProjectBilling.php) | `team_id`, `project_job_id`, `method`, `status`, `period_start`, `period_end`, `currency`, `quantity`, `rate`, `amount`, `progress_percent`, `billable_time_amount`, `billable_expense_amount`, `retainer_amount`, `write_up_down_amount`, `source_ref`, `invoice_ref`, `metadata` |
| [Project.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-project-billing-api/src/Models/Project.php) | `name`, `code`, `description`, `start_date`, `end_date`, `status`, `allocation_percentage` |
<!-- layer-implementation-plan:end -->
