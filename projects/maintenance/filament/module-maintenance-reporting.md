# Maintenance: Module Maintenance Reporting Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#module-maintenance-reporting). Observed identity: [`liberusoftware/module-maintenance-reporting-filament`](../../../modules/source/liberusoftware--module-maintenance-reporting-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-maintenance-module-maintenance-reporting-filament`  
**Matching domain module:** `module-maintenance-reporting`  
**Application:** Maintenance  
**Source feature:** [Module Maintenance Reporting](../features/module-maintenance-reporting.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `module-maintenance-reporting` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Backlog:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Response:** resource/table/form/action or page behavior for this module's authorized workflow.
- **First-time fix:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Downtime:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Cost:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Utilization:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Stock:** resource/table/form/action or page behavior for this module's authorized workflow.
- **SLA:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Compliance metrics:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-maintenance-module-maintenance-reporting-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `backlog`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `response`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `first-time-fix`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `downtime`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `cost`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `utilization`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `stock`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `sla`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `compliance-metrics`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `module-maintenance-reporting` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-maintenance-laravel-filament`](https://github.com/liberusoftware/project-maintenance-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-maintenance-reporting-filament`](https://github.com/liberusoftware/module-maintenance-reporting-filament) (`liberusoftware/maintenance-reporting-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/module-maintenance-reporting.md) · [API plan](../api/module-maintenance-reporting.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Backlog** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `backlog`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Response** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `response`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **First-time fix** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `first-time fix`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Downtime** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `downtime`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Cost** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `cost`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Utilization** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `utilization`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Stock** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `stock`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **SLA** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `sla`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Compliance metrics** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `compliance metrics`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ReportingFilamentPlugin.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting-filament/src/ReportingFilamentPlugin.php) · [ReportingFilamentServiceProvider.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting-filament/src/ReportingFilamentServiceProvider.php) · [ReportingResource.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting-filament/src/Resources/ReportingResource.php) · [CreateReport.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting-filament/src/Resources/ReportingResource/Pages/CreateReport.php) · [EditReport.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting-filament/src/Resources/ReportingResource/Pages/EditReport.php) · [ListReports.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting-filament/src/Resources/ReportingResource/Pages/ListReports.php).

| Observed core query | Public method signatures |
| --- | --- |
| [BuildReportSummary.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting/src/Queries/BuildReportSummary.php) | `public function handle(int $teamId, ?CarbonInterface $start = null, ?CarbonInterface $end = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateReportRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting/src/Actions/CreateReportRecord.php) | `public function handle(int $teamId, array $attributes): ReportRecord` |
| [DeleteReportRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting/src/Actions/DeleteReportRecord.php) | `public function handle(int $teamId, ReportRecord $record): void` |
| [PublishReport.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting/src/Actions/PublishReport.php) | `public function execute(int $teamId, ReportRecord $record): ReportRecord` |
| [UpdateReportRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting/src/Actions/UpdateReportRecord.php) | `public function handle(int $teamId, ReportRecord $record, array $attributes): ReportRecord` |
| [ReportRecordPolicy.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting/src/Policies/ReportRecordPolicy.php) | `public function viewAny(object $user): bool`<br>`public function view(object $user, ReportRecord $record): bool`<br>`public function create(object $user): bool`<br>`public function update(object $user, ReportRecord $record): bool`<br>`public function delete(object $user, ReportRecord $record): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ReportKind.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting/src/Models/ReportKind.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReportRecord.php](https://github.com/liberusoftware/project-maintenance-laravel-filament/blob/c267d625e264e86ad223be8a3a08a3728afc7344/modules/module-maintenance-reporting/src/Models/ReportRecord.php) | `kind`, `title`, `description`, `metric_value`, `period_start`, `period_end`, `status`, `metadata`, `team_id` |
<!-- layer-implementation-plan:end -->
