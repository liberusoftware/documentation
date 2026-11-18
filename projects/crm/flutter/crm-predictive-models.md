# Crm Predictive Models Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-predictive-models). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-predictive-models-flutter
**Matching core package:** module-crm-crm-predictive-models ([implementation](../core/crm-predictive-models.md))
**Matching API package:** module-crm-crm-predictive-models-api ([contract](../api/crm-predictive-models.md))

## Implementation plan

This adapter presents Crm Predictive Models for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Predictive Models API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/crm-predictive-models.md), and [API module](../api/crm-predictive-models.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `crm-predictive-models`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-crm-mobile-flutter`](https://github.com/liberusoftware/project-crm-mobile-flutter) | [`module-crm-predictive-models-flutter`](https://github.com/liberusoftware/module-crm-predictive-models-flutter) (`module_crm_predictive_models_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-crm-dart-mobile`](https://github.com/liberusoftware/project-crm-dart-mobile) | [`module-crm-predictive-models-dart-mobile`](https://github.com/liberusoftware/module-crm-predictive-models-dart-mobile) (`module_crm_predictive_models_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-crm-dart-desktop`](https://github.com/liberusoftware/project-crm-dart-desktop) | [`module-crm-predictive-models-dart-desktop`](https://github.com/liberusoftware/module-crm-predictive-models-dart-desktop) (`module_crm_predictive_models_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | [API plan](../api/crm-predictive-models.md) · [Core plan](../core/crm-predictive-models.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Lead/opportunity scoring** | Adaptive mobile cards/sheets for `lead/opportunity scoring` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `lead/opportunity scoring` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Churn/renewal risk** | Adaptive mobile cards/sheets for `churn/renewal risk` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `churn/renewal risk` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Next action/product** | Adaptive mobile cards/sheets for `next action/product` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `next action/product` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Forecast** | Adaptive mobile cards/sheets for `forecast` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `forecast` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Routing** | Adaptive mobile cards/sheets for `routing` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `routing` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Model registry** | Adaptive mobile cards/sheets for `model registry` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `model registry` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Evaluation** | Adaptive mobile cards/sheets for `evaluation` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `evaluation` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Drift** | Adaptive mobile cards/sheets for `drift` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `drift` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Explanations** | Adaptive mobile cards/sheets for `explanations` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `explanations` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

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
