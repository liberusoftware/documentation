# Conversion Optimization Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#conversion-optimization). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-conversion-optimization-flutter
**Matching core package:** module-crm-conversion-optimization ([implementation](../core/conversion-optimization.md))
**Matching API package:** module-crm-conversion-optimization-api ([contract](../api/conversion-optimization.md))

## Implementation plan

This adapter presents Conversion Optimization for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Conversion Optimization API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/conversion-optimization.md), and [API module](../api/conversion-optimization.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `conversion-optimization`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-crm-mobile-flutter`](https://github.com/liberusoftware/project-crm-mobile-flutter) | [`module-crm-conversion-optimization-flutter`](https://github.com/liberusoftware/module-crm-conversion-optimization-flutter) (`module_crm_conversion_optimization_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-crm-dart-mobile`](https://github.com/liberusoftware/project-crm-dart-mobile) | [`module-crm-conversion-optimization-dart-mobile`](https://github.com/liberusoftware/module-crm-conversion-optimization-dart-mobile) (`module_crm_conversion_optimization_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-crm-dart-desktop`](https://github.com/liberusoftware/project-crm-dart-desktop) | [`module-crm-conversion-optimization-dart-desktop`](https://github.com/liberusoftware/module-crm-conversion-optimization-dart-desktop) (`module_crm_conversion_optimization_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | [API plan](../api/conversion-optimization.md) · [Core plan](../core/conversion-optimization.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **A/B and multivariate tests** | Adaptive mobile cards/sheets for `a/b and multivariate tests` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `a/b and multivariate tests` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Traffic allocation** | Adaptive mobile cards/sheets for `traffic allocation` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `traffic allocation` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Goals** | Adaptive mobile cards/sheets for `goals` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `goals` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Statistical policy** | Adaptive mobile cards/sheets for `statistical policy` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `statistical policy` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Popups** | Adaptive mobile cards/sheets for `popups` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `popups` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Banners** | Adaptive mobile cards/sheets for `banners` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `banners` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **CTAs** | Adaptive mobile cards/sheets for `ctas` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `ctas` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Personalization rules** | Adaptive mobile cards/sheets for `personalization rules` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `personalization rules` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Experiment reporting** | Adaptive mobile cards/sheets for `experiment reporting` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `experiment reporting` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-crm-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ConversionReportQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversion-optimization/src/Queries/ConversionReportQuery.php) | `public function experiments(int $teamId): Builder`<br>`public function report(int $teamId, ConversionExperiment $experiment): array` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ActivateExperiment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversion-optimization/src/Actions/ActivateExperiment.php) | `public function execute(int $teamId, int $userId, ConversionExperiment $experiment): ConversionExperiment` |
| [CreateConversionExperiment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversion-optimization/src/Actions/CreateConversionExperiment.php) | `public function execute(int $teamId, int $userId, array $input): ConversionExperiment` |
| [RecordConversion.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversion-optimization/src/Actions/RecordConversion.php) | `public function execute(int $teamId, ConversionExperiment $experiment, string $subjectKey, string $variant, string $event, float $value = 1): ConversionObservation` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ConversionExperiment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversion-optimization/src/Models/ConversionExperiment.php) | No literal fillable array detected; inspect the model and API schema. |
| [ConversionObservation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversion-optimization/src/Models/ConversionObservation.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ConversionOptimizationController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversion-optimization-api/src/Http/Controllers/ConversionOptimizationController.php) | `public function __construct(private readonly ConversionReportQuery $query)`<br>`public function index(): JsonResponse`<br>`public function store(CreateConversionExperiment $a): JsonResponse`<br>`public function activate(ConversionExperiment $e, ActivateExperiment $a): JsonResponse`<br>`public function convert(ConversionExperiment $e, RecordConversion $a): JsonResponse`<br>`public function report(ConversionExperiment $e): JsonResponse` |

**Observed route declarations:**

[modules/crm-conversion-optimization-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-conversion-optimization-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/conversion-optimization')->group(function (): void {
Route::get('experiments', [ConversionOptimizationController::class, 'index']);
Route::post('experiments', [ConversionOptimizationController::class, 'store']);
Route::post('experiments/{experiment}/activate', [ConversionOptimizationController::class, 'activate']);
Route::post('experiments/{experiment}/conversions', [ConversionOptimizationController::class, 'convert']);
Route::get('experiments/{experiment}/report', [ConversionOptimizationController::class, 'report']);
```
<!-- layer-implementation-plan:end -->
