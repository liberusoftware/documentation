# CRM: Crm Forecasting Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-forecasting). Observed identity: [`liberusoftware/module-crm-forecasting-filament`](../../../modules/source/liberusoftware--module-crm-forecasting-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-crm-forecasting-filament`  
**Matching domain module:** `crm-forecasting`  
**Application:** CRM  
**Source feature:** [Crm Forecasting](../features/crm-forecasting.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-forecasting` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Forecast categories:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Rollups:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Manager adjustments:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Commit/best-case/pipeline views:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Coverage:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Trend:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Scenario:** resource/table/form/action or page behavior for this module's authorized workflow.
- **History:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Accuracy:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Submission workflow:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-crm-forecasting-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `forecast-categories`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `rollups`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `manager-adjustments`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `commit-best-case-pipeline-views`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `coverage`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `trend`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `scenario`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `history`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `accuracy`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `submission-workflow`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-forecasting` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-forecasting-filament`](https://github.com/liberusoftware/module-crm-forecasting-filament) (`liberusoftware/crm-forecasting-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-forecasting.md) · [API plan](../api/crm-forecasting.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Forecast categories** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `forecast categories`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Rollups** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `rollups`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Manager adjustments** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `manager adjustments`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Commit/best-case/pipeline views** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `commit/best-case/pipeline views`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Coverage** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `coverage`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Trend** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `trend`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Scenario** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `scenario`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **History** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `history`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Accuracy** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `accuracy`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Submission workflow** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `submission workflow`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [ForecastingFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forecasting-filament/src/ForecastingFilamentServiceProvider.php) · [ForecastResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forecasting-filament/src/Resources/ForecastResource.php) · [CreateForecast.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forecasting-filament/src/Resources/Pages/CreateForecast.php) · [EditForecast.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forecasting-filament/src/Resources/Pages/EditForecast.php) · [ListForecasts.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forecasting-filament/src/Resources/Pages/ListForecasts.php).

| Observed core query | Public method signatures |
| --- | --- |
| [ForecastingQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forecasting/src/Queries/ForecastingQuery.php) | `public function categories(int $teamId)`<br>`public function forecasts(int $teamId, string $period)`<br>`public function summary(int $teamId, string $period): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCategory.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forecasting/src/Actions/CreateCategory.php) | `public function __construct(private readonly ForecastingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ForecastCategory` |
| [RecordForecast.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forecasting/src/Actions/RecordForecast.php) | `public function __construct(private readonly ForecastingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): Forecast` |
| [SubmitForecast.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forecasting/src/Actions/SubmitForecast.php) | `public function __construct(private readonly ForecastingPolicy $policy)`<br>`public function execute(int $teamId, int $userId, Forecast $forecast): ForecastSubmission` |
| [ForecastingPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forecasting/src/Services/ForecastingPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Forecast.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forecasting/src/Models/Forecast.php) | No literal fillable array detected; inspect the model and API schema. |
| [ForecastAdjustment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forecasting/src/Models/ForecastAdjustment.php) | No literal fillable array detected; inspect the model and API schema. |
| [ForecastCategory.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forecasting/src/Models/ForecastCategory.php) | No literal fillable array detected; inspect the model and API schema. |
| [ForecastSubmission.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forecasting/src/Models/ForecastSubmission.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
