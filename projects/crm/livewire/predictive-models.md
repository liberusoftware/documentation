# CRM: Predictive Models Livewire

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#predictive-models). Observed identity: [`liberusoftware/module-crm-predictive-models-livewire`](../../../modules/source/liberusoftware--module-crm-predictive-models-livewire.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Livewire 4 implementation

**Livewire package:** `module-crm-predictive-models-livewire`  
**Matching domain module:** `crm-predictive-models`  
**Application:** CRM  
**Source feature:** [Predictive Models](../features/predictive-models.md)  
**Architecture:** [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Livewire 4 presentation package provides interactive server-driven components for exactly one independent domain module. Components coordinate public queries/actions and presentation state; they do not own persistence, authorization decisions, tenancy, business rules, or theme identity. The package has no dependency on application `App\` classes or another module's internals.

## 2. Module-specific interactions

- **Lead/opportunity scoring:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Churn/renewal risk:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Next action/product:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Forecast:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Routing:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Model registry:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Evaluation:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Drift:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.
- **Explanations:** interactive component state, validation feedback, loading, and failure recovery for this domain capability.

## 3. Livewire 4 implementation

- Register a stable `module-crm-predictive-models-livewire` component namespace and service provider; use explicit aliases such as `<livewire:module-crm-predictive-models::component-name />` according to LIVEWIRE.md.
- Keep reusable components under `src/Components`, full-page components under `src/Pages`, and package views under `resources/views`.
- Treat public properties, URL state, events, uploads, and action parameters as untrusted input; validate and authorize at the Livewire boundary, then invoke the authoritative domain action/query.
- Keep public state minimal and non-sensitive, use locked/typed state where supported, and provide loading, validation, authorization, empty, and failure states.

### Capability mapping

- `lead-opportunity-scoring`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `churn-renewal-risk`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `next-action-product`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `forecast`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `routing`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `model-registry`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `evaluation`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `drift`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.
- `explanations`: expose a focused Livewire 4 component or full-page component backed by the corresponding domain query/action.

## 4. Security and verification

- Prove allowed, denied, wrong-tenant, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every component.
- Test hydration/dehydration, authorization, validation, events, loading, pagination/filter state, accessibility, and component alias collisions.
- Run Pest 5 Livewire tests against the supported Livewire 4/Laravel stack; domain behavior remains covered by the owning module.

## 5. Definition of done

- Package identity, namespace, aliases, and dependency match `crm-predictive-models` one-to-one.
- Every required interaction has a named component and view-model/state contract without leaking secrets or domain internals.
- Installation, registration, authorization, tenant isolation, accessibility, compatibility, and meaningful-PHP coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, view resolution contract, and source evidence

| Delivery boundary | Repository / specification | Responsibility |
| --- | --- | --- |
| Product Laravel host | [`project-crm-laravel-filament`](https://github.com/liberusoftware/project-crm-laravel-filament) | Route composition, session/CSRF middleware, and tracked `/modules` + `/themes` |
| Livewire & default views contract | [LIVEWIRE.md](../../../standards/LIVEWIRE.md) · [THEMES.md](../../../standards/THEMES.md) | Namespaced `resources/views` defaults resolved after active/parent theme overrides |
| Authoritative domain owner | [Core plan](../core/predictive-models.md) · [API plan](../api/predictive-models.md) | Domain actions, queries, policies, and persistence |

### Livewire 4 feature and component matrix

| Feature / aspect | Livewire 4 component & locked/typed state contract | Validation, domain delegation & recovery UX |
| --- | --- | --- |
| **Lead/opportunity scoring** | Expose a focused Livewire 4 component and namespaced Blade default view for `lead/opportunity scoring` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Churn/renewal risk** | Expose a focused Livewire 4 component and namespaced Blade default view for `churn/renewal risk` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Next action/product** | Expose a focused Livewire 4 component and namespaced Blade default view for `next action/product` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Forecast** | Expose a focused Livewire 4 component and namespaced Blade default view for `forecast` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Routing** | Expose a focused Livewire 4 component and namespaced Blade default view for `routing` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Model registry** | Expose a focused Livewire 4 component and namespaced Blade default view for `model registry` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Evaluation** | Expose a focused Livewire 4 component and namespaced Blade default view for `evaluation` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Drift** | Expose a focused Livewire 4 component and namespaced Blade default view for `drift` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |
| **Explanations** | Expose a focused Livewire 4 component and namespaced Blade default view for `explanations` with minimal non-sensitive public properties and `#[Locked]` identifiers. | Re-authorize actor/tenant context on every call, validate form inputs, invoke the core action/query, and render accessible loading, conflict, and error states. |

### Observed domain and transport source evidence

**Observed Livewire / view files:** [PredictiveModelsDashboard.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-predictive-models-livewire/src/Components/PredictiveModelsDashboard.php) · [PredictiveModelsLivewireServiceProvider.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-predictive-models-livewire/src/PredictiveModelsLivewireServiceProvider.php).

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
