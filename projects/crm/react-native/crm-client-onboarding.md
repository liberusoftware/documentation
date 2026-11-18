# Crm Client Onboarding React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-client-onboarding). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-client-onboarding-react-native
**Matching core package:** module-crm-crm-client-onboarding ([implementation](../core/crm-client-onboarding.md))
**Matching API package:** module-crm-crm-client-onboarding-api ([contract](../api/crm-client-onboarding.md))

## Implementation plan

This adapter presents Crm Client Onboarding for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Client Onboarding API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/crm-client-onboarding.md), and [API module](../api/crm-client-onboarding.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `crm-client-onboarding`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-client-onboarding.md)) |
| Capability React Native module skeleton | [`module-crm-client-onboarding-react-native`](https://github.com/liberusoftware/module-crm-client-onboarding-react-native) (`@liberusoftware/module-crm-client-onboarding-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Intake** | Progressive mobile list/detail/sheet flow for `intake` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Domain/provider connections** | Progressive mobile list/detail/sheet flow for `domain/provider connections` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Data import** | Progressive mobile list/detail/sheet flow for `data import` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Snapshot application** | Progressive mobile list/detail/sheet flow for `snapshot application` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Verification** | Progressive mobile list/detail/sheet flow for `verification` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Launch checklist** | Progressive mobile list/detail/sheet flow for `launch checklist` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Training** | Progressive mobile list/detail/sheet flow for `training` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Handoff** | Progressive mobile list/detail/sheet flow for `handoff` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Health** | Progressive mobile list/detail/sheet flow for `health` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ClientOnboardingQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-client-onboarding/src/Queries/ClientOnboardingQuery.php) | `public function onboardings(int $teamId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CompleteOnboardingStep.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-client-onboarding/src/Actions/CompleteOnboardingStep.php) | `public function execute(int $teamId, int $actorId, ClientOnboarding $onboarding, string $kind, string $label, array $evidence = []): ClientOnboardingStep` |
| [StartClientOnboarding.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-client-onboarding/src/Actions/StartClientOnboarding.php) | `public function execute(int $teamId, int $ownerId, string $clientKey, array $intake = []): ClientOnboarding` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ClientOnboarding.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-client-onboarding/src/Models/ClientOnboarding.php) | No literal fillable array detected; inspect the model and API schema. |
| [ClientOnboardingStep.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-client-onboarding/src/Models/ClientOnboardingStep.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ClientOnboardingController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-client-onboarding-api/src/Http/Controllers/ClientOnboardingController.php) | `public function __construct(private readonly ClientOnboardingQuery $query)`<br>`public function index(): JsonResponse`<br>`public function store(StartClientOnboarding $a): JsonResponse`<br>`public function step(ClientOnboarding $onboarding, CompleteOnboardingStep $a): JsonResponse` |

**Observed route declarations:**

[modules/crm-client-onboarding-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-client-onboarding-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/client-onboarding')->group(function (): void {
Route::get('/', [ClientOnboardingController::class, 'index']);
Route::post('/', [ClientOnboardingController::class, 'store']);
Route::post('{onboarding}/steps', [ClientOnboardingController::class, 'step']);
```
<!-- layer-implementation-plan:end -->
