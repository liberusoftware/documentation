# Revenue Intelligence React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#revenue-intelligence). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-revenue-intelligence-react-native
**Matching core package:** module-crm-revenue-intelligence ([implementation](../core/revenue-intelligence.md))
**Matching API package:** module-crm-revenue-intelligence-api ([contract](../api/revenue-intelligence.md))

## Implementation plan

This adapter presents Revenue Intelligence for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Revenue Intelligence API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/revenue-intelligence.md), and [API module](../api/revenue-intelligence.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `revenue-intelligence`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/revenue-intelligence.md)) |
| Capability React Native module skeleton | [`module-crm-revenue-intelligence-react-native`](https://github.com/liberusoftware/module-crm-revenue-intelligence-react-native) (`@liberusoftware/module-crm-revenue-intelligence-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Pipeline inspection** | Progressive mobile list/detail/sheet flow for `pipeline inspection` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Health/risk** | Progressive mobile list/detail/sheet flow for `health/risk` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Engagement gaps** | Progressive mobile list/detail/sheet flow for `engagement gaps` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Opportunity scoring** | Progressive mobile list/detail/sheet flow for `opportunity scoring` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Relationship maps** | Progressive mobile list/detail/sheet flow for `relationship maps` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **White-space/next-product suggestions** | Progressive mobile list/detail/sheet flow for `white-space/next-product suggestions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Anomaly detection** | Progressive mobile list/detail/sheet flow for `anomaly detection` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Alerts** | Progressive mobile list/detail/sheet flow for `alerts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [RevenueIntelligenceQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Queries/RevenueIntelligenceQuery.php) | `public function insights(int $teamId)`<br>`public function alerts(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Actions/CreateAlert.php) | `public function __construct(private readonly RevenueIntelligencePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): RevenueIntelligenceAlert` |
| [RecordInsight.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Actions/RecordInsight.php) | `public function __construct(private readonly RevenueIntelligencePolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): RevenueInsight` |
| [ResolveAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Actions/ResolveAlert.php) | `public function __construct(private readonly RevenueIntelligencePolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $alertId): RevenueIntelligenceAlert` |
| [UpdateInsight.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Actions/UpdateInsight.php) | `public function __construct(private readonly RevenueIntelligencePolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $insightId, array $input): RevenueInsight` |
| [RevenueIntelligencePolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Services/RevenueIntelligencePolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [RevenueInsight.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Models/RevenueInsight.php) | No literal fillable array detected; inspect the model and API schema. |
| [RevenueIntelligenceAlert.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence/src/Models/RevenueIntelligenceAlert.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [RevenueIntelligenceController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence-api/src/Http/Controllers/RevenueIntelligenceController.php) | `public function insights(Request $r, RevenueIntelligenceQuery $q)`<br>`public function insight(Request $r, RecordInsight $a)`<br>`public function alerts(Request $r, RevenueIntelligenceQuery $q)`<br>`public function alert(Request $r, CreateAlert $a)`<br>`public function resolve(Request $r, int $alert, ResolveAlert $a)` |

**Observed route declarations:**

[modules/crm-revenue-intelligence-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-revenue-intelligence-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/revenue-intelligence')->group(function (): void {
Route::get('/insights', [RevenueIntelligenceController::class, 'insights']);
Route::post('/insights', [RevenueIntelligenceController::class, 'insight']);
Route::get('/alerts', [RevenueIntelligenceController::class, 'alerts']);
Route::post('/alerts', [RevenueIntelligenceController::class, 'alert']);
Route::post('/alerts/{alert}/resolve', [RevenueIntelligenceController::class, 'resolve']);
```
<!-- layer-implementation-plan:end -->
