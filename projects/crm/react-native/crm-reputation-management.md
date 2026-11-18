# Crm Reputation Management React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-reputation-management). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-reputation-management-react-native
**Matching core package:** module-crm-crm-reputation-management ([implementation](../core/crm-reputation-management.md))
**Matching API package:** module-crm-crm-reputation-management-api ([contract](../api/crm-reputation-management.md))

## Implementation plan

This adapter presents Crm Reputation Management for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Reputation Management API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/crm-reputation-management.md), and [API module](../api/crm-reputation-management.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `crm-reputation-management`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-reputation-management.md)) |
| Capability React Native module skeleton | [`module-crm-reputation-management-react-native`](https://github.com/liberusoftware/module-crm-reputation-management-react-native) (`@liberusoftware/module-crm-reputation-management-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Review requests** | Progressive mobile list/detail/sheet flow for `review requests` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Review-site connections** | Progressive mobile list/detail/sheet flow for `review-site connections` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Monitoring** | Progressive mobile list/detail/sheet flow for `monitoring` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Response workflow** | Progressive mobile list/detail/sheet flow for `response workflow` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Templates** | Progressive mobile list/detail/sheet flow for `templates` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Escalation** | Progressive mobile list/detail/sheet flow for `escalation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Sentiment** | Progressive mobile list/detail/sheet flow for `sentiment` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Location rollups** | Progressive mobile list/detail/sheet flow for `location rollups` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Reputation reporting** | Progressive mobile list/detail/sheet flow for `reputation reporting` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ReputationQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Queries/ReputationQuery.php) | `public function connections(int $teamId)`<br>`public function requests(int $teamId)`<br>`public function reviews(int $teamId)`<br>`public function templates(int $teamId)`<br>`public function rollups(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ConnectReviewSite.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Actions/ConnectReviewSite.php) | `public function __construct(private readonly ReputationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ReputationConnection` |
| [CreateReviewRequest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Actions/CreateReviewRequest.php) | `public function __construct(private readonly ReputationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ReputationRequest` |
| [EscalateReview.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Actions/EscalateReview.php) | `public function __construct(private readonly ReputationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $reviewId): ReputationReview` |
| [RecordReview.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Actions/RecordReview.php) | `public function __construct(private readonly ReputationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ReputationReview` |
| [RespondToReview.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Actions/RespondToReview.php) | `public function __construct(private readonly ReputationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $reviewId, array $input): ReputationReview` |
| [SaveTemplate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Actions/SaveTemplate.php) | `public function __construct(private readonly ReputationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): ReputationTemplate` |
| [UpdateReview.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Actions/UpdateReview.php) | `public function __construct(private readonly ReputationPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $reviewId, array $input): ReputationReview` |
| [ReputationPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Services/ReputationPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ReputationConnection.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Models/ReputationConnection.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReputationRequest.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Models/ReputationRequest.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReputationReview.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Models/ReputationReview.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReputationRollup.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Models/ReputationRollup.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReputationTemplate.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management/src/Models/ReputationTemplate.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ReputationManagementController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management-api/src/Http/Controllers/ReputationManagementController.php) | `public function connections(Request $r, ReputationQuery $q)`<br>`public function connection(Request $r, ConnectReviewSite $a)`<br>`public function requests(Request $r, ReputationQuery $q)`<br>`public function request(Request $r, CreateReviewRequest $a)`<br>`public function reviews(Request $r, ReputationQuery $q)`<br>`public function review(Request $r, RecordReview $a)`<br>`public function respond(Request $r, int $review, RespondToReview $a)`<br>`public function template(Request $r, SaveTemplate $a)` |

**Observed route declarations:**

[modules/crm-reputation-management-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-reputation-management-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/reputation-management')->group(function (): void {
Route::get('/connections', [ReputationManagementController::class, 'connections']);
Route::post('/connections', [ReputationManagementController::class, 'connection']);
Route::get('/requests', [ReputationManagementController::class, 'requests']);
Route::post('/requests', [ReputationManagementController::class, 'request']);
Route::get('/reviews', [ReputationManagementController::class, 'reviews']);
Route::post('/reviews', [ReputationManagementController::class, 'review']);
Route::post('/reviews/{review}/respond', [ReputationManagementController::class, 'respond']);
Route::post('/templates', [ReputationManagementController::class, 'template']);
```
<!-- layer-implementation-plan:end -->
