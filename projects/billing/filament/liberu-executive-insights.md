# Billing: Liberu Executive Insights Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#liberu-executive-insights). Observed identity: [`liberusoftware/module-liberu-executive-insights-filament`](../../../modules/source/liberusoftware--module-liberu-executive-insights-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-billing-liberu-executive-insights-filament`  
**Matching domain module:** `liberu-executive-insights`  
**Application:** Billing  
**Source feature:** [Liberu Executive Insights](../features/liberu-executive-insights.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `liberu-executive-insights` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Metric registry:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Cross-product projections:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Evidence drill-through:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Decision snapshots:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Data-quality operations:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-billing-liberu-executive-insights-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `metric-registry`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `cross-product-projections`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `evidence-drill-through`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `decision-snapshots`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `data-quality-operations`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `liberu-executive-insights` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-billing-laravel-filament`](https://github.com/liberusoftware/project-billing-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-module-liberu-executive-insights-5279400e-filament`](https://github.com/liberusoftware/module-module-liberu-executive-insights-5279400e-filament) (`liberusoftware/module-liberu-executive-insights-5279400e-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/liberu-executive-insights.md) · [API plan](../api/liberu-executive-insights.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Metric registry** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `metric registry`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Cross-product projections** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `cross-product projections`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Evidence drill-through** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `evidence drill-through`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Decision snapshots** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `decision snapshots`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Data-quality operations** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `data-quality operations`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ExecutiveInsightsFilamentServiceProvider.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-executive-insights-filament/src/ExecutiveInsightsFilamentServiceProvider.php) · [InsightSnapshotResource.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-executive-insights-filament/src/Resources/InsightSnapshotResource.php) · [CreateInsightSnapshot.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-executive-insights-filament/src/Resources/InsightSnapshotResource/Pages/CreateInsightSnapshot.php) · [EditInsightSnapshot.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-executive-insights-filament/src/Resources/InsightSnapshotResource/Pages/EditInsightSnapshot.php) · [ListInsightSnapshots.php](https://github.com/liberusoftware/project-billing-laravel-filament/blob/4743bdfebd1c122e10bf80171d0210ab27e34a54/modules/liberu-executive-insights-filament/src/Resources/InsightSnapshotResource/Pages/ListInsightSnapshots.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [RegisterMetric.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/liberu-executive-insights/src/Actions/RegisterMetric.php) | `public function __construct(private readonly Dispatcher $events)`<br>`public function handle(array $attributes): MetricDefinition` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [MetricDefinition.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/liberu-executive-insights/src/Models/MetricDefinition.php) | `team_id`, `key`, `name`, `formula`, `version`, `dimensions`, `currency`, `timezone`, `freshness_seconds`, `is_active` |
<!-- layer-implementation-plan:end -->
