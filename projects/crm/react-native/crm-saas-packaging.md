# Crm Saas Packaging React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-saas-packaging). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-saas-packaging-react-native
**Matching core package:** module-crm-crm-saas-packaging ([implementation](../core/crm-saas-packaging.md))
**Matching API package:** module-crm-crm-saas-packaging-api ([contract](../api/crm-saas-packaging.md))

## Implementation plan

This adapter presents Crm Saas Packaging for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Saas Packaging API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/crm-saas-packaging.md), and [API module](../api/crm-saas-packaging.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `crm-saas-packaging`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-saas-packaging.md)) |
| Capability React Native module skeleton | [`module-crm-saas-packaging-react-native`](https://github.com/liberusoftware/module-crm-saas-packaging-react-native) (`@liberusoftware/module-crm-saas-packaging-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Plans** | Progressive mobile list/detail/sheet flow for `plans` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Feature/module entitlements** | Progressive mobile list/detail/sheet flow for `feature/module entitlements` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Limits** | Progressive mobile list/detail/sheet flow for `limits` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Trials** | Progressive mobile list/detail/sheet flow for `trials` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Signup provisioning** | Progressive mobile list/detail/sheet flow for `signup provisioning` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Upgrade/downgrade** | Progressive mobile list/detail/sheet flow for `upgrade/downgrade` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Suspension** | Progressive mobile list/detail/sheet flow for `suspension` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Cancellation** | Progressive mobile list/detail/sheet flow for `cancellation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Billing integration** | Progressive mobile list/detail/sheet flow for `billing integration` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [SaasQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/src/Queries/SaasQuery.php) | `public function plans()`<br>`public function subscription(int $teamId): ?SaasSubscription`<br>`public function usage(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ChangeSubscriptionStatus.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/src/Actions/ChangeSubscriptionStatus.php) | `public function execute(int $teamId, int $actorId, string $status): SaasSubscription` |
| [ProvisionSubscription.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/src/Actions/ProvisionSubscription.php) | `public function execute(int $teamId, int $actorId, array $data): SaasSubscription` |
| [RecordUsage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/src/Actions/RecordUsage.php) | `public function execute(int $teamId, int $actorId, array $data): SaasUsage` |
| [UpdateSubscription.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/src/Actions/UpdateSubscription.php) | `public function execute(int $teamId, int $actorId, array $data): SaasSubscription` |
| [SaasPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/src/Services/SaasPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [SaasPlan.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/src/Models/SaasPlan.php) | No literal fillable array detected; inspect the model and API schema. |
| [SaasSubscription.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/src/Models/SaasSubscription.php) | No literal fillable array detected; inspect the model and API schema. |
| [SaasUsage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging/src/Models/SaasUsage.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [SaasController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging-api/src/Http/Controllers/SaasController.php) | `public function plans(SaasQuery $q)`<br>`public function subscription(Request $r, SaasQuery $q)`<br>`public function provision(Request $r, ProvisionSubscription $a)`<br>`public function status(Request $r, string $status, ChangeSubscriptionStatus $a)`<br>`public function usage(Request $r, SaasQuery $q)`<br>`public function recordUsage(Request $r, RecordUsage $a)` |

**Observed route declarations:**

[modules/crm-saas-packaging-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-saas-packaging-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/saas-packaging')->group(function (): void {
Route::get('/plans', [SaasController::class, 'plans']);
Route::get('/subscription', [SaasController::class, 'subscription']);
Route::post('/subscription', [SaasController::class, 'provision']);
Route::post('/subscription/{status}', [SaasController::class, 'status'])->whereIn('status', ['active', 'suspended', 'cancelled']);
Route::get('/usage', [SaasController::class, 'usage']);
Route::post('/usage', [SaasController::class, 'recordUsage']);
```
<!-- layer-implementation-plan:end -->
