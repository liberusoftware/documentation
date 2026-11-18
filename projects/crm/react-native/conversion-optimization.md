# Conversion Optimization React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#conversion-optimization). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-conversion-optimization-react-native
**Matching core package:** module-crm-conversion-optimization ([implementation](../core/conversion-optimization.md))
**Matching API package:** module-crm-conversion-optimization-api ([contract](../api/conversion-optimization.md))

## Implementation plan

This adapter presents Conversion Optimization for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Conversion Optimization API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/conversion-optimization.md), and [API module](../api/conversion-optimization.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `conversion-optimization`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/conversion-optimization.md)) |
| Capability React Native module skeleton | [`module-crm-conversion-optimization-react-native`](https://github.com/liberusoftware/module-crm-conversion-optimization-react-native) (`@liberusoftware/module-crm-conversion-optimization-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **A/B and multivariate tests** | Progressive mobile list/detail/sheet flow for `a/b and multivariate tests` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Traffic allocation** | Progressive mobile list/detail/sheet flow for `traffic allocation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Goals** | Progressive mobile list/detail/sheet flow for `goals` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Statistical policy** | Progressive mobile list/detail/sheet flow for `statistical policy` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Popups** | Progressive mobile list/detail/sheet flow for `popups` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Banners** | Progressive mobile list/detail/sheet flow for `banners` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **CTAs** | Progressive mobile list/detail/sheet flow for `ctas` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Personalization rules** | Progressive mobile list/detail/sheet flow for `personalization rules` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Experiment reporting** | Progressive mobile list/detail/sheet flow for `experiment reporting` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

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
