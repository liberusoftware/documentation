# Attribution React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#attribution). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-attribution-react-native
**Matching core package:** module-crm-attribution ([implementation](../core/attribution.md))
**Matching API package:** module-crm-attribution-api ([contract](../api/attribution.md))

## Implementation plan

This adapter presents Attribution for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Attribution API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/attribution.md), and [API module](../api/attribution.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `attribution`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/attribution.md)) |
| Capability React Native module skeleton | [`module-crm-attribution-react-native`](https://github.com/liberusoftware/module-crm-attribution-react-native) (`@liberusoftware/module-crm-attribution-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **First/last/multi-touch models** | Progressive mobile list/detail/sheet flow for `first/last/multi-touch models` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Campaign members** | Progressive mobile list/detail/sheet flow for `campaign members` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Source normalization** | Progressive mobile list/detail/sheet flow for `source normalization` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **UTM/click IDs** | Progressive mobile list/detail/sheet flow for `utm/click ids` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Offline conversions** | Progressive mobile list/detail/sheet flow for `offline conversions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Influence** | Progressive mobile list/detail/sheet flow for `influence` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Cost allocation** | Progressive mobile list/detail/sheet flow for `cost allocation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Model comparison** | Progressive mobile list/detail/sheet flow for `model comparison` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [AttributionQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-attribution/src/Queries/AttributionQuery.php) | `public function touchpoints(int $teamId): Builder`<br>`public function conversions(int $teamId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [RecordConversion.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-attribution/src/Actions/RecordConversion.php) | `public function execute(int $teamId, array $input): Conversion` |
| [RecordTouchpoint.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-attribution/src/Actions/RecordTouchpoint.php) | `public function execute(int $teamId, array $input): Touchpoint` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Conversion.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-attribution/src/Models/Conversion.php) | No literal fillable array detected; inspect the model and API schema. |
| [Touchpoint.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-attribution/src/Models/Touchpoint.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [AttributionController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-attribution-api/src/Http/Controllers/AttributionController.php) | `public function __construct(private readonly AttributionQuery $query)`<br>`public function touchpoints(Request $request): JsonResponse`<br>`public function recordTouchpoint(Request $request, RecordTouchpoint $action): JsonResponse`<br>`public function conversions(Request $request): JsonResponse`<br>`public function recordConversion(Request $request, RecordConversion $action): JsonResponse` |

**Observed route declarations:**

[modules/crm-attribution-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-attribution-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/attribution')->group(function (): void {
Route::get('touchpoints', [AttributionController::class, 'touchpoints']);
Route::post('touchpoints', [AttributionController::class, 'recordTouchpoint']);
Route::get('conversions', [AttributionController::class, 'conversions']);
Route::post('conversions', [AttributionController::class, 'recordConversion']);
```
<!-- layer-implementation-plan:end -->
