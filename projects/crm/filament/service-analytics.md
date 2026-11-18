# CRM: Service Analytics Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#service-analytics). Observed identity: [`liberusoftware/module-crm-service-analytics-filament`](../../../modules/source/liberusoftware--module-crm-service-analytics-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-service-analytics-filament`  
**Matching domain module:** `crm-service-analytics`  
**Application:** CRM  
**Source feature:** [Service Analytics](../features/service-analytics.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-service-analytics` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Volume:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Backlog:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Deflection:** resource/table/form/action or page behavior for this module's authorized workflow.
- **First response:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Resolution:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Reopen:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Transfer:** resource/table/form/action or page behavior for this module's authorized workflow.
- **SLA:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Satisfaction:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Quality:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Staffing:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Cost-to-serve:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-service-analytics-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `volume`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `backlog`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `deflection`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `first-response`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `resolution`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `reopen`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `transfer`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `sla`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `satisfaction`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `quality`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `staffing`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `cost-to-serve`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-service-analytics` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-service-analytics-filament`](https://github.com/liberusoftware/module-crm-service-analytics-filament) (`liberusoftware/crm-service-analytics-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/service-analytics.md) · [API plan](../api/service-analytics.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Volume** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `volume`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Backlog** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `backlog`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Deflection** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `deflection`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **First response** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `first response`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Resolution** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `resolution`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Reopen** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `reopen`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Transfer** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `transfer`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **SLA** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `sla`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Satisfaction** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `satisfaction`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Quality** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `quality`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Staffing** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `staffing`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Cost-to-serve** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `cost-to-serve`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [AnalyticsSnapshotResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-analytics-filament/src/Resources/AnalyticsSnapshotResource.php) · [ListAnalyticsSnapshots.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-analytics-filament/src/Resources/AnalyticsSnapshotResource/Pages/ListAnalyticsSnapshots.php) · [ServiceAnalyticsFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-analytics-filament/src/ServiceAnalyticsFilamentPlugin.php) · [ServiceAnalyticsFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-analytics-filament/src/ServiceAnalyticsFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [AnalyticsQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-analytics/src/Queries/AnalyticsQuery.php) | `public function snapshots(int $teamId)`<br>`public function metric(int $teamId, string $metric, $from = null, $to = null)`<br>`public function summary(int $teamId, $from = null, $to = null): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [RecordMetric.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-analytics/src/Actions/RecordMetric.php) | `public function execute(int $teamId, int $actorId, array $data): AnalyticsSnapshot` |
| [RecordServiceMetrics.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-analytics/src/Actions/RecordServiceMetrics.php) | `public function execute(int $teamId, int $actorId, array $metrics): int` |
| [AnalyticsAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-analytics/src/Services/AnalyticsAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $details = []): Audit` |
| [AnalyticsPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-analytics/src/Services/AnalyticsPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AnalyticsAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-analytics/src/Models/AnalyticsAudit.php) | No literal fillable array detected; inspect the model and API schema. |
| [AnalyticsSnapshot.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-service-analytics/src/Models/AnalyticsSnapshot.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
