# CRM: Crm Revenue Intelligence Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-revenue-intelligence). Observed identity: [`liberusoftware/module-crm-revenue-intelligence-filament`](../../../modules/source/liberusoftware--module-crm-revenue-intelligence-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-crm-revenue-intelligence-filament`  
**Matching domain module:** `crm-revenue-intelligence`  
**Application:** CRM  
**Source feature:** [Crm Revenue Intelligence](../features/crm-revenue-intelligence.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-revenue-intelligence` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Pipeline inspection:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Health/risk:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Engagement gaps:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Opportunity scoring:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Relationship maps:** resource/table/form/action or page behavior for this module's authorized workflow.
- **White-space/next-product suggestions:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Anomaly detection:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Alerts:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-crm-revenue-intelligence-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `pipeline-inspection`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `health-risk`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `engagement-gaps`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `opportunity-scoring`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `relationship-maps`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `white-space-next-product-suggestions`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `anomaly-detection`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `alerts`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-revenue-intelligence` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-revenue-intelligence-filament`](https://github.com/liberusoftware/module-crm-revenue-intelligence-filament) (`liberusoftware/crm-revenue-intelligence-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-revenue-intelligence.md) · [API plan](../api/crm-revenue-intelligence.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Pipeline inspection** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `pipeline inspection`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Health/risk** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `health/risk`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Engagement gaps** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `engagement gaps`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Opportunity scoring** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `opportunity scoring`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Relationship maps** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `relationship maps`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **White-space/next-product suggestions** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `white-space/next-product suggestions`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Anomaly detection** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `anomaly detection`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Alerts** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `alerts`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [InsightResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence-filament/src/Resources/InsightResource.php) · [CreateInsight.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence-filament/src/Resources/InsightResource/Pages/CreateInsight.php) · [EditInsight.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence-filament/src/Resources/InsightResource/Pages/EditInsight.php) · [ListInsights.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence-filament/src/Resources/InsightResource/Pages/ListInsights.php) · [RevenueIntelligenceFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence-filament/src/RevenueIntelligenceFilamentPlugin.php) · [RevenueIntelligenceFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence-filament/src/RevenueIntelligenceFilamentServiceProvider.php).

| Observed core query | Public method signatures |
| --- | --- |
| [RevenueIntelligenceQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Queries/RevenueIntelligenceQuery.php) | `public function insights(int $teamId)`<br>`public function alerts(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Actions/CreateAlert.php) | `public function __construct(private readonly RevenueIntelligencePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): RevenueIntelligenceAlert` |
| [RecordInsight.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Actions/RecordInsight.php) | `public function __construct(private readonly RevenueIntelligencePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): RevenueInsight` |
| [ResolveAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Actions/ResolveAlert.php) | `public function __construct(private readonly RevenueIntelligencePolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $alertId): RevenueIntelligenceAlert` |
| [UpdateInsight.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Actions/UpdateInsight.php) | `public function __construct(private readonly RevenueIntelligencePolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $insightId, array $input): RevenueInsight` |
| [RevenueIntelligencePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Services/RevenueIntelligencePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [RevenueInsight.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Models/RevenueInsight.php) | No literal fillable array detected; inspect the model and API schema. |
| [RevenueIntelligenceAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Models/RevenueIntelligenceAlert.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
