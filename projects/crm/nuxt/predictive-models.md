# CRM: Predictive Models Nuxt

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#predictive-models). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one Nuxt 4 implementation

**Nuxt package:** `module-crm-predictive-models-nuxt`
**Matching domain module:** `crm-predictive-models`
**Application:** CRM
**Source feature:** [Predictive Models](../features/predictive-models.md)
**Architecture:** [NUXT.md](../../../standards/NUXT.md) · [API.md](../../../architecture/API.md) · [Matching API module](../api/predictive-models.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional Nuxt 4 presentation package presents exactly one matching API module. It contributes reusable pages, layouts, components, composables, typed API clients, and actions to application-owned Nuxt applications while delegating authorization, validation, team context, persistence, and business rules to the `crm-predictive-models` public API boundary. It must not contain another module's UI or depend on application `App\` classes.

## 2. Module-specific surfaces

- **Lead/opportunity scoring:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Churn/renewal risk:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Next action/product:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Forecast:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Routing:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Model registry:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Evaluation:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Drift:** page/component/composable/API-action behavior for this module's authorized workflow.
- **Explanations:** page/component/composable/API-action behavior for this module's authorized workflow.

## 3. Nuxt 4 implementation

- Register a stable `module-crm-predictive-models-nuxt` Nuxt module or layer and expose only prefixed exports from this package; applications compose it explicitly.
- Keep pages under `app/pages`, shared UI under `app/components`, data access under `app/composables`, and typed contracts under `shared/`.
- Use typed API clients, `useFetch`/`useAsyncData`, composables, route metadata, loading/error states, and accessible components over the matching API contract; never duplicate server-side invariants in client validation.
- Resolve actor, team, locale, and sensitive-field visibility through trusted API context and fail closed when required context is missing.

### Capability mapping

- `lead-opportunity-scoring`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `churn-renewal-risk`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `next-action-product`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `forecast`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `routing`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `model-registry`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `evaluation`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `drift`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.
- `explanations`: map the API query/action to the appropriate Nuxt page, component, composable, or typed API action.

## 4. API contract and Nuxt consumption

- Consume only the matching API module linked above; use its documented OpenAPI schemas, routes, authentication, permissions, team context, pagination, errors, and operation semantics.
- Keep a typed API client and module-local composables under the package boundary; use `useFetch` or `useAsyncData` for SSR-safe reads and `$fetch` for event-driven mutations.
- Forward Sanctum cookies or approved authorization headers through a controlled client boundary; never persist long-lived tokens in browser storage or expose secrets in SSR payloads.
- Validate client input for user experience, but rely on the API for authoritative authorization, validation, concurrency, idempotency, and business invariants.
- Map loading, empty, stale, unauthorized, forbidden, validation, rate-limit, and server-error responses to accessible UI states.

## 5. Security and verification

- Prove allowed, denied, wrong-team, invalid, stale/concurrent, duplicate, partial-failure, and recovery paths for every exposed surface.
- Add package discovery/collision, architecture-boundary, authorization, team-context, accessibility, localization, and minimal-host installation tests.
- Test observable browser and SSR behavior with Vitest, Vue Test Utils, Playwright, TypeScript, and the supported Nuxt 4/Vue 3 stack; domain behavior remains covered by the owning module.

## 6. Definition of done

- Package identity, public exports, API dependency, and module dependency match `crm-predictive-models` one-to-one.
- Every required route or application surface has an explicit page/component/composable/API-action mapping and no undeclared surface is discovered.
- Production build, route generation, API contract compatibility, authorization, team isolation, accessibility, compatibility, and meaningful TypeScript coverage gates pass.

<!-- layer-implementation-plan:start -->
## Structured feature plan, skeleton repository, and source evidence

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product Nuxt 4 host skeleton | [`project-crm-nuxt-vue`](https://github.com/liberusoftware/project-crm-nuxt-vue) | Standalone Nuxt 4 + Vue 3 application shell, Nitro server handlers, and SSR runtime config ([template](https://github.com/liberusoftware/project-boilerplate-nuxt-vue) · [wayfinder](../../wayfinders/nuxt-vue.md) · [runbook](../../../guides/presentation/NUXT.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root publishing versioned `/api/v1` endpoints ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/predictive-models.md)) |
| Capability Nuxt module skeleton | [`module-crm-predictive-models-nuxt`](https://github.com/liberusoftware/module-crm-predictive-models-nuxt) (`@liberusoftware/module-crm-predictive-models-nuxt`) | Reusable Nuxt 4 components, composables, and typed DTO parsers ([foundation](https://github.com/liberusoftware/module-boilerplate-nuxt) · [catalog](../../../modules/skeletons/nuxt-vue.md)) |

### Nuxt 4 feature, SSR, and API integration matrix

| Feature / aspect | Nuxt 4 page, Vue component & composable contract | SSR cache isolation, `$fetch` command & recovery contract |
| --- | --- | --- |
| **Lead/opportunity scoring** | Expose composable and Vue 3 component for `lead/opportunity scoring` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/predictive-models.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Churn/renewal risk** | Expose composable and Vue 3 component for `churn/renewal risk` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/predictive-models.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Next action/product** | Expose composable and Vue 3 component for `next action/product` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/predictive-models.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Forecast** | Expose composable and Vue 3 component for `forecast` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/predictive-models.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Routing** | Expose composable and Vue 3 component for `routing` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/predictive-models.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Model registry** | Expose composable and Vue 3 component for `model registry` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/predictive-models.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Evaluation** | Expose composable and Vue 3 component for `evaluation` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/predictive-models.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Drift** | Expose composable and Vue 3 component for `drift` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/predictive-models.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |
| **Explanations** | Expose composable and Vue 3 component for `explanations` using validated DTOs from `shared/`; share framework-neutral Vue UI with [Vue Inertia](../vue/predictive-models.md). | Use actor/tenant-scoped `useFetch`/`useAsyncData` keys (`private, no-store` default for authenticated reads) and `$fetch` mutations against `project-crm-laravel-api`. |

### Observed domain and transport source evidence

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

| Observed API controller | Handler signatures |
| --- | --- |
| [PredictiveModelsController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-predictive-models-api/src/Http/Controllers/PredictiveModelsController.php) | `public function models(Request $r, PredictiveModelQuery $q)`<br>`public function model(Request $r, RegisterPredictiveModel $a)`<br>`public function prediction(Request $r, RecordPrediction $a)`<br>`public function evaluation(Request $r, RecordEvaluation $a)`<br>`public function drift(Request $r, DetectDrift $a)` |

**Observed route declarations:**

[modules/crm-predictive-models-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-predictive-models-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/predictive-models')->group(function (): void {
Route::get('/models', [PredictiveModelsController::class, 'models']);
Route::post('/models', [PredictiveModelsController::class, 'model']);
Route::post('/predictions', [PredictiveModelsController::class, 'prediction']);
Route::post('/evaluations', [PredictiveModelsController::class, 'evaluation']);
Route::post('/drift', [PredictiveModelsController::class, 'drift']);
```
<!-- layer-implementation-plan:end -->
