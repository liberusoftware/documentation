# Accounting: Accounting Operational Reports Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-operational-reports). Observed identity: [`liberusoftware/module-accounting-operational-reports-filament`](../../../modules/source/liberusoftware--module-accounting-operational-reports-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-accounting-accounting-operational-reports-filament`  
**Matching domain module:** `accounting-operational-reports`  
**Application:** Accounting  
**Source feature:** [Accounting Operational Reports](../features/accounting-operational-reports.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `accounting-operational-reports` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Receivables/payables:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Sales/purchases:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Tax:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Bank:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Inventory:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Assets:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Expenses:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Projects:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Payroll:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Exception reports:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-accounting-accounting-operational-reports-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `receivables-payables`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `sales-purchases`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `tax`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `bank`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `inventory`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `assets`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `expenses`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `projects`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `payroll`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `exception-reports`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `accounting-operational-reports` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-accounting-erp-laravel-filament`](https://github.com/liberusoftware/project-accounting-erp-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-accounting-operational-reports-filament`](https://github.com/liberusoftware/module-accounting-operational-reports-filament) (`liberusoftware/accounting-operational-reports-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/accounting-operational-reports.md) · [API plan](../api/accounting-operational-reports.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Receivables/payables** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `receivables/payables`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Sales/purchases** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `sales/purchases`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Tax** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `tax`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Bank** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `bank`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Inventory** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `inventory`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Assets** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `assets`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Expenses** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `expenses`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Projects** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `projects`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Payroll** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `payroll`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Exception reports** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `exception reports`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [OperationalReportsFilamentPlugin.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-operational-reports-filament/src/OperationalReportsFilamentPlugin.php) · [OperationalReportsFilamentServiceProvider.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-operational-reports-filament/src/OperationalReportsFilamentServiceProvider.php) · [ListReportRuns.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-operational-reports-filament/src/Resources/Pages/ListReportRuns.php) · [ReportRunResource.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-operational-reports-filament/src/Resources/ReportRunResource.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ReportQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-operational-reports/src/Queries/ReportQuery.php) | `public function paginate(?int $teamId = null, ?string $category = null, ?string $status = null, int $perPage = 25): LengthAwarePaginator`<br>`public function exceptions(?int $teamId = null): LengthAwarePaginator` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [GenerateReport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-operational-reports/src/Actions/GenerateReport.php) | `public function handle(array $attributes, array $rows = [], array $exceptions = []): ReportRun` |
| [PublishReport.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-operational-reports/src/Actions/PublishReport.php) | `public function handle(ReportRun $run, int $actorId): ReportRun` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ReportAudit.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-operational-reports/src/Models/ReportAudit.php) | `run_id`, `event_type`, `actor_id`, `payload`, `payload_hash`, `created_at` |
| [ReportException.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-operational-reports/src/Models/ReportException.php) | `run_id`, `exception_key`, `severity`, `message`, `source_type`, `source_id`, `status`, `resolution`, `resolved_by`, `resolved_at`, `metadata` |
| [ReportRow.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-operational-reports/src/Models/ReportRow.php) | `run_id`, `row_key`, `label`, `source_type`, `source_id`, `amount`, `currency`, `state`, `dimensions`, `payload` |
| [ReportRun.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-operational-reports/src/Models/ReportRun.php) | `team_id`, `report_key`, `name`, `category`, `period_start`, `period_end`, `currency`, `status`, `filters`, `summary`, `source_hash`, `requested_by`, `published_by`, `published_at`, `failure_message`, `metadata` |
<!-- layer-implementation-plan:end -->
