# CRM: Crm Predictive Models Filament

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-predictive-models). Observed identity: [`liberusoftware/module-crm-predictive-models-filament`](../../../modules/source/liberusoftware--module-crm-predictive-models-filament.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Filament 5 implementation

**Filament package:** `module-crm-crm-predictive-models-filament`  
**Matching domain module:** `crm-predictive-models`  
**Application:** CRM  
**Source feature:** [Crm Predictive Models](../features/crm-predictive-models.md)  
**Architecture:** [FILAMENT.md](../../../standards/FILAMENT.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Filament 5 presentation package presents exactly one independent domain module. It contributes reusable resources, pages, widgets, schemas, tables, infolists, and actions to application-owned panels while delegating authorization, validation, tenancy, persistence, and business rules to the `crm-predictive-models` public boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Lead/opportunity scoring:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Churn/renewal risk:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Next action/product:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Forecast:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Routing:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Model registry:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Evaluation:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Drift:** resource/table/form/action or page behavior for this module's authorized workflow.
- **Explanations:** resource/table/form/action or page behavior for this module's authorized workflow.

## 3. Filament 5 implementation

- Register a stable `module-crm-crm-predictive-models-filament` plugin and discover only classes in this package's namespace; applications attach it explicitly to each eligible panel.
- Keep resources under `src/Resources`, resource pages and relation managers beneath their resource, and shared module-local widgets/pages under `src/Widgets` and `src/Pages`.
- Use Filament 5 schemas, tables, infolists, actions, notifications, authorization hooks, and panel configuration as adapters over domain queries/actions; never duplicate domain invariants in form validation.
- Resolve actor, tenant, locale, and sensitive-field visibility through trusted application context and fail closed when required context is missing.

### Capability mapping

- `lead-opportunity-scoring`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `churn-renewal-risk`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `next-action-product`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `forecast`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `routing`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `model-registry`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `evaluation`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `drift`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.
- `explanations`: map the domain query/action to the appropriate Filament 5 resource, page, widget, or action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add plugin discovery/collision, architecture-boundary, authorization, tenancy, accessibility, localization, and minimal-host installation tests.
- Test observable Filament behavior with Pest 5 and the supported Filament 5/Livewire 4 stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, plugin ID, and dependency match `crm-predictive-models` one-to-one.
- Every required panel surface has an explicit resource/page/widget/action mapping and no undeclared surface is discovered.
- Production discovery/cache build, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, repository skeleton, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Filament host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Panel registration, tenant/workspace context, navigation, and tracked `/modules` + `/themes` |
| Capability Filament package | [`module-crm-predictive-models-filament`](https://github.com/liberusoftware/module-crm-predictive-models-filament) (`liberusoftware/crm-predictive-models-filament`) | One-to-one Filament 5 resources, schemas, tables, infolists, widgets, and actions ([foundation](https://github.com/liberusoftware/module-boilerplate-filament) · [catalog](../../../modules/skeletons/laravel-filament.md)) |
| Authoritative domain owner | [Core plan](../core/crm-predictive-models.md) · [API plan](../api/crm-predictive-models.md) | Domain actions, queries, policies, and persistence |

### Filament 5 feature and surface matrix

| Feature / aspect | Filament 5 resource, schema, table, infolist & widget contract | Policy, tenant scope & action delegation |
| --- | --- | --- |
| **Lead/opportunity scoring** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `lead/opportunity scoring`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Churn/renewal risk** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `churn/renewal risk`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Next action/product** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `next action/product`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Forecast** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `forecast`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Routing** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `routing`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Model registry** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `model registry`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Evaluation** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `evaluation`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Drift** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `drift`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |
| **Explanations** | Provide a dedicated Filament 5 table column/filter, form schema section, infolist entry, or header/table action for `explanations`. | Authorize via the core policy and current workspace/tenant before rendering or executing the domain action; never bypass domain actions with raw model saves. |

### Observed domain and transport source evidence

**Observed Filament class files:** [PredictiveModelsFilamentPlugin.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-predictive-models-filament/src/PredictiveModelsFilamentPlugin.php) · [PredictiveModelsFilamentServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-predictive-models-filament/src/PredictiveModelsFilamentServiceProvider.php) · [PredictionResource.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-predictive-models-filament/src/Resources/PredictionResource.php) · [CreatePrediction.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-predictive-models-filament/src/Resources/PredictionResource/Pages/CreatePrediction.php) · [EditPrediction.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-predictive-models-filament/src/Resources/PredictionResource/Pages/EditPrediction.php) · [ListPredictions.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-predictive-models-filament/src/Resources/PredictionResource/Pages/ListPredictions.php).

| Observed core query | Public method signatures |
| --- | --- |
| [PredictiveModelQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-predictive-models/src/Queries/PredictiveModelQuery.php) | `public function models(int $teamId)`<br>`public function predictions(int $teamId)`<br>`public function evaluations(int $teamId)`<br>`public function drift(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [DetectDrift.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-predictive-models/src/Actions/DetectDrift.php) | `public function __construct(private readonly PredictiveModelPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ModelDrift` |
| [RecordEvaluation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-predictive-models/src/Actions/RecordEvaluation.php) | `public function __construct(private readonly PredictiveModelPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ModelEvaluation` |
| [RecordPrediction.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-predictive-models/src/Actions/RecordPrediction.php) | `public function __construct(private readonly PredictiveModelPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): Prediction` |
| [RegisterPredictiveModel.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-predictive-models/src/Actions/RegisterPredictiveModel.php) | `public function __construct(private readonly PredictiveModelPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PredictiveModel` |
| [UpdatePrediction.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-predictive-models/src/Actions/UpdatePrediction.php) | `public function __construct(private readonly PredictiveModelPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $predictionId, array $input): Prediction` |
| [PredictiveModelPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-predictive-models/src/Services/PredictiveModelPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ModelDrift.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-predictive-models/src/Models/ModelDrift.php) | No literal fillable array detected; inspect the model and API schema. |
| [ModelEvaluation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-predictive-models/src/Models/ModelEvaluation.php) | No literal fillable array detected; inspect the model and API schema. |
| [Prediction.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-predictive-models/src/Models/Prediction.php) | No literal fillable array detected; inspect the model and API schema. |
| [PredictiveModel.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-predictive-models/src/Models/PredictiveModel.php) | No literal fillable array detected; inspect the model and API schema. |
<!-- layer-implementation-plan:end -->
