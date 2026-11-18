# Forecasting Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#forecasting). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-forecasting-flutter
**Matching core package:** module-crm-forecasting ([implementation](../core/forecasting.md))
**Matching API package:** module-crm-forecasting-api ([contract](../api/forecasting.md))

## Implementation plan

This adapter presents Forecasting for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Forecasting API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/forecasting.md), and [API module](../api/forecasting.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `forecasting`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-crm-mobile-flutter`](https://github.com/liberusoftware/project-crm-mobile-flutter) | [`module-crm-forecasting-flutter`](https://github.com/liberusoftware/module-crm-forecasting-flutter) (`module_crm_forecasting_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-crm-dart-mobile`](https://github.com/liberusoftware/project-crm-dart-mobile) | [`module-crm-forecasting-dart-mobile`](https://github.com/liberusoftware/module-crm-forecasting-dart-mobile) (`module_crm_forecasting_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-crm-dart-desktop`](https://github.com/liberusoftware/project-crm-dart-desktop) | [`module-crm-forecasting-dart-desktop`](https://github.com/liberusoftware/module-crm-forecasting-dart-desktop) (`module_crm_forecasting_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | [API plan](../api/forecasting.md) · [Core plan](../core/forecasting.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Forecast categories** | Adaptive mobile cards/sheets for `forecast categories` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `forecast categories` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Rollups** | Adaptive mobile cards/sheets for `rollups` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `rollups` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Manager adjustments** | Adaptive mobile cards/sheets for `manager adjustments` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `manager adjustments` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Commit/best-case/pipeline views** | Adaptive mobile cards/sheets for `commit/best-case/pipeline views` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `commit/best-case/pipeline views` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Coverage** | Adaptive mobile cards/sheets for `coverage` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `coverage` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Trend** | Adaptive mobile cards/sheets for `trend` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `trend` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Scenario** | Adaptive mobile cards/sheets for `scenario` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `scenario` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **History** | Adaptive mobile cards/sheets for `history` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `history` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Accuracy** | Adaptive mobile cards/sheets for `accuracy` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `accuracy` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Submission workflow** | Adaptive mobile cards/sheets for `submission workflow` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `submission workflow` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

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

| Observed API controller | Handler signatures |
| --- | --- |
| [ForecastingController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forecasting-api/src/Http/Controllers/ForecastingController.php) | `public function __construct(private readonly ForecastingQuery $query)`<br>`public function categories(): JsonResponse`<br>`public function index(string $period): JsonResponse`<br>`public function storeCategory(CreateCategory $action): JsonResponse`<br>`public function store(RecordForecast $action): JsonResponse`<br>`public function submit(int $forecast, SubmitForecast $action): JsonResponse`<br>`public function adjust(int $forecast, AdjustForecast $action): JsonResponse` |

**Observed route declarations:**

[modules/crm-forecasting-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-forecasting-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/forecasting')->group(function (): void {
Route::get('categories', [ForecastingController::class, 'categories']);
Route::get('forecasts/{period}', [ForecastingController::class, 'index']);
Route::post('categories', [ForecastingController::class, 'storeCategory']);
Route::post('forecasts', [ForecastingController::class, 'store']);
Route::post('forecasts/{forecast}/submit', [ForecastingController::class, 'submit']);
Route::post('forecasts/{forecast}/adjustments', [ForecastingController::class, 'adjust']);
```
<!-- layer-implementation-plan:end -->
