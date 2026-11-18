# Crm Customer Data Platform React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-customer-data-platform). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-customer-data-platform-react-native
**Matching core package:** module-crm-crm-customer-data-platform ([implementation](../core/crm-customer-data-platform.md))
**Matching API package:** module-crm-crm-customer-data-platform-api ([contract](../api/crm-customer-data-platform.md))

## Implementation plan

This adapter presents Crm Customer Data Platform for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Customer Data Platform API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/crm-customer-data-platform.md), and [API module](../api/crm-customer-data-platform.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `crm-customer-data-platform`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-customer-data-platform.md)) |
| Capability React Native module skeleton | [`module-crm-customer-data-platform-react-native`](https://github.com/liberusoftware/module-crm-customer-data-platform-react-native) (`@liberusoftware/module-crm-customer-data-platform-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Source profiles** | Progressive mobile list/detail/sheet flow for `source profiles` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Identity resolution** | Progressive mobile list/detail/sheet flow for `identity resolution` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Unified profiles** | Progressive mobile list/detail/sheet flow for `unified profiles` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Audience activation** | Progressive mobile list/detail/sheet flow for `audience activation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Event ingestion** | Progressive mobile list/detail/sheet flow for `event ingestion` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Consent-aware calculated attributes** | Progressive mobile list/detail/sheet flow for `consent-aware calculated attributes` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Profile lineage** | Progressive mobile list/detail/sheet flow for `profile lineage` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CdpQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Queries/CdpQuery.php) | `public function profiles(int $teamId)`<br>`public function audiences(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ActivateCdpAudience.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Actions/ActivateCdpAudience.php) | `public function __construct(private readonly CdpPolicy $policy)`<br>`public function execute(int $teamId, int $userId, CdpAudience $audience, string $destination): CdpAudience` |
| [CreateCdpAudience.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Actions/CreateCdpAudience.php) | `public function __construct(private readonly CdpPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): CdpAudience` |
| [IngestCdpEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Actions/IngestCdpEvent.php) | `public function execute(int $teamId, CdpProfile $profile, array $input): CdpEvent` |
| [UpsertCdpProfile.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Actions/UpsertCdpProfile.php) | `public function __construct(private readonly CdpPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): CdpProfile` |
| [CdpPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Services/CdpPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CdpAudience.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Models/CdpAudience.php) | No literal fillable array detected; inspect the model and API schema. |
| [CdpEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Models/CdpEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [CdpIdentity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Models/CdpIdentity.php) | No literal fillable array detected; inspect the model and API schema. |
| [CdpProfile.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform/src/Models/CdpProfile.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [CdpController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform-api/src/Http/Controllers/CdpController.php) | `public function __construct(private readonly CdpQuery $query)`<br>`public function profiles(): JsonResponse`<br>`public function storeProfile(UpsertCdpProfile $action): JsonResponse`<br>`public function event(CdpProfile $profile, IngestCdpEvent $action): JsonResponse`<br>`public function audiences(): JsonResponse`<br>`public function storeAudience(CreateCdpAudience $action): JsonResponse`<br>`public function activate(CdpAudience $audience, ActivateCdpAudience $action): JsonResponse` |

**Observed route declarations:**

[modules/crm-customer-data-platform-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-customer-data-platform-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/customer-data-platform')->group(function (): void {
Route::get('profiles', [CdpController::class, 'profiles']);
Route::post('profiles', [CdpController::class, 'storeProfile']);
Route::post('profiles/{profile}/events', [CdpController::class, 'event']);
Route::get('audiences', [CdpController::class, 'audiences']);
Route::post('audiences', [CdpController::class, 'storeAudience']);
Route::post('audiences/{audience}/activate', [CdpController::class, 'activate']);
```
<!-- layer-implementation-plan:end -->
