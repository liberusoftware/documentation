# Billing: Reporting Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#reporting). Observed identity: [`liberusoftware/module-billing-reporting-filament`](../../../modules/source/liberusoftware--module-billing-reporting-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-billing-reporting-filament`  
**Matching domain module:** `billing-reporting`  
**Application:** Billing  
**Source feature:** [Reporting](../features/reporting.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `billing-reporting` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **MRR/ARR:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Churn:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Aging:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Revenue:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Tax:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Usage:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Provisioning:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Collection:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Provider metrics:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-billing-reporting-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `mrr-arr`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `churn`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `aging`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `revenue`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `tax`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `usage`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `provisioning`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `collection`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `provider-metrics`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `billing-reporting` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-billing-laravel-filament`](https://github.com/liberusoftware/project-billing-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-billing-reporting-filament`](https://github.com/liberusoftware/module-billing-reporting-filament) (`liberusoftware/billing-reporting-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/reporting.md) · [API plan](../api/reporting.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **MRR/ARR** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `mrr/arr`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Churn** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `churn`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Aging** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `aging`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Revenue** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `revenue`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Tax** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `tax`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Usage** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `usage`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Provisioning** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `provisioning`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Collection** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `collection`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Provider metrics** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `provider metrics`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ReportingFilamentPlugin.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting-filament/src/ReportingFilamentPlugin.php) · [ReportingFilamentServiceProvider.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting-filament/src/ReportingFilamentServiceProvider.php) · [MetricSnapshotResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting-filament/src/Resources/MetricSnapshotResource.php) · [CreateMetricSnapshot.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting-filament/src/Resources/MetricSnapshotResource/Pages/CreateMetricSnapshot.php) · [ListMetricSnapshots.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting-filament/src/Resources/MetricSnapshotResource/Pages/ListMetricSnapshots.php) · [ReportingMetricResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting-filament/src/Resources/ReportingMetricResource.php) · [CreateReportingMetric.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting-filament/src/Resources/ReportingMetricResource/Pages/CreateReportingMetric.php) · [ListReportingMetrics.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting-filament/src/Resources/ReportingMetricResource/Pages/ListReportingMetrics.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ListMetricSnapshots.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Queries/ListMetricSnapshots.php) | `public function execute(int $teamId, int $perPage = 25): LengthAwarePaginator` |
| [ListReportingMetrics.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Queries/ListReportingMetrics.php) | `public function execute(int $teamId, ?string $metric = null, int $perPage = 25): LengthAwarePaginator` |
| [ListReportingRecords.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Queries/ListReportingRecords.php) | `public function handle(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CalculateReportingMetric.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Actions/CalculateReportingMetric.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(int $teamId, string $metric, CarbonImmutable $periodStart, CarbonImmutable $periodEnd, ?string $currency = null): array` |
| [CreateMetricSnapshot.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Actions/CreateMetricSnapshot.php) | `public function handle(int $teamId, array $attributes): MetricSnapshot` |
| [ExportReportingMetrics.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Actions/ExportReportingMetrics.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(int $teamId, ?string $metric = null): string` |
| [GenerateCustomerBillingSummary.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Actions/GenerateCustomerBillingSummary.php) | `public function __construct(private DatabaseManager $database)`<br>`public function execute(int $teamId, int $customerId, ?string $currency = null): array` |
| [RecordReportingMetric.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Actions/RecordReportingMetric.php) | `public function execute(int $teamId, array $attributes): ReportingMetric` |
| [MetricSnapshotPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Policies/MetricSnapshotPolicy.php) | `public function viewAny(?Authenticatable $user): bool`<br>`public function create(?Authenticatable $user): bool`<br>`public function view(?Authenticatable $user, MetricSnapshot $record): bool`<br>`public function update(?Authenticatable $user, MetricSnapshot $record): bool` |
| [ReportingMetricPolicy.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Policies/ReportingMetricPolicy.php) | `public function viewAny(?object $user): bool`<br>`public function create(?object $user): bool`<br>`public function view(?object $user, object $record): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MetricSnapshot.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Models/MetricSnapshot.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReportingMetric.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/module-billing-reporting/src/Models/ReportingMetric.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
