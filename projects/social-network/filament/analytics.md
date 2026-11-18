# Social Network: Analytics Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#analytics). Observed identity: [`liberusoftware/module-social-network-analytics-filament`](../../../modules/source/liberusoftware--module-social-network-analytics-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-social-network-analytics-filament`  
**Matching domain module:** `social-network-analytics`  
**Application:** Social Network  
**Source feature:** [Analytics](../features/analytics.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `social-network-analytics` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Growth:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Engagement:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Retention:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Health:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Moderation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Delivery:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Privacy-governed insights:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-social-network-analytics-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `growth`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `engagement`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `retention`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `health`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `moderation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `delivery`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `privacy-governed-insights`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `social-network-analytics` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-social-network-laravel-filament`](https://github.com/liberusoftware/project-social-network-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-social-network-analytics-filament`](https://github.com/liberusoftware/module-social-network-analytics-filament) (`liberusoftware/social-network-analytics-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/analytics.md) · [API plan](../api/analytics.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Growth** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `growth`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Engagement** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `engagement`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Retention** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `retention`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Health** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `health`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Moderation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `moderation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Delivery** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `delivery`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Privacy-governed insights** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `privacy-governed insights`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [AnalyticsFilamentPlugin.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics-filament/src/AnalyticsFilamentPlugin.php) · [AnalyticsFilamentServiceProvider.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics-filament/src/AnalyticsFilamentServiceProvider.php) · [Dashboard.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics-filament/src/Pages/Dashboard.php).

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [BuildSnapshot.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics/src/Actions/BuildSnapshot.php) | `public function __construct( private AnalyticsAuthorizer $authorizer, private Dispatcher $events, )`<br>`public function handle(object $actor, string $metric, string $periodStart, string $periodEnd, int $cohortSize, float $value, array $dimensions = []): MetricSnapshot` |
| [GetMetrics.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics/src/Actions/GetMetrics.php) | `public function __construct(private AnalyticsAuthorizer $authorizer)`<br>`public function handle(object $actor, string $metric, int $limit = 30): Collection` |
| [RecordMetric.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics/src/Actions/RecordMetric.php) | `public function __construct( private AnalyticsAuthorizer $authorizer, private Dispatcher $events, )`<br>`public function handle(object $actor, string $name, array $dimensions = [], int $value = 1): AnalyticsEvent` |
| [AnalyticsAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics/src/Contracts/AnalyticsAuthorizer.php) | `public function view(object $actor, string $metric): void`<br>`public function record(object $actor, string $metric): void` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AnalyticsEvent.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics/src/Models/AnalyticsEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [MetricSnapshot.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-analytics/src/Models/MetricSnapshot.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
