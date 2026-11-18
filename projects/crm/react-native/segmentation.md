# Segmentation React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#segmentation). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-segmentation-react-native
**Matching core package:** module-crm-segmentation ([implementation](../core/segmentation.md))
**Matching API package:** module-crm-segmentation-api ([contract](../api/segmentation.md))

## Implementation plan

This adapter presents Segmentation for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Segmentation API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/segmentation.md), and [API module](../api/segmentation.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `segmentation`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/segmentation.md)) |
| Capability React Native module skeleton | [`module-crm-segmentation-react-native`](https://github.com/liberusoftware/module-crm-segmentation-react-native) (`@liberusoftware/module-crm-segmentation-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Static/dynamic audiences** | Progressive mobile list/detail/sheet flow for `static/dynamic audiences` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Nested conditions** | Progressive mobile list/detail/sheet flow for `nested conditions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Behavioral events** | Progressive mobile list/detail/sheet flow for `behavioral events` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Calculated attributes** | Progressive mobile list/detail/sheet flow for `calculated attributes` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Exclusions** | Progressive mobile list/detail/sheet flow for `exclusions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Estimated counts** | Progressive mobile list/detail/sheet flow for `estimated counts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Refresh** | Progressive mobile list/detail/sheet flow for `refresh` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Lineage** | Progressive mobile list/detail/sheet flow for `lineage` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [SegmentationQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Queries/SegmentationQuery.php) | `public function audiences(int $teamId)`<br>`public function members(int $teamId, int $audienceId)`<br>`public function events(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateAudience.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Actions/CreateAudience.php) | `public function execute(int $teamId, int $actorId, array $data): Audience` |
| [RecordBehaviorEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Actions/RecordBehaviorEvent.php) | `public function execute(int $teamId, int $actorId, array $data): BehaviorEvent` |
| [RefreshAudience.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Actions/RefreshAudience.php) | `public function execute(int $teamId, int $actorId, int $audienceId, array $data = []): Audience` |
| [UpdateAudience.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Actions/UpdateAudience.php) | `public function execute(int $teamId, int $actorId, int $audienceId, array $data): Audience` |
| [SegmentationAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Services/SegmentationAudit.php) | `public function record(int $teamId, ?int $actorId, int $audienceId, string $operation, array $details = []): SegmentationLineage` |
| [SegmentationPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Services/SegmentationPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Audience.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Models/Audience.php) | No literal fillable array detected; inspect the model and API schema. |
| [AudienceMember.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Models/AudienceMember.php) | No literal fillable array detected; inspect the model and API schema. |
| [BehaviorEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Models/BehaviorEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [SegmentationLineage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation/src/Models/SegmentationLineage.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [SegmentationController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation-api/src/Http/Controllers/SegmentationController.php) | `public function index(Request $r, SegmentationQuery $q)`<br>`public function store(Request $r, CreateAudience $a)`<br>`public function update(Request $r, int $audience, UpdateAudience $a)`<br>`public function members(Request $r, int $audience, SegmentationQuery $q)`<br>`public function refresh(Request $r, int $audience, RefreshAudience $a)`<br>`public function event(Request $r, RecordBehaviorEvent $a)` |

**Observed route declarations:**

[modules/crm-segmentation-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-segmentation-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/segmentation')->group(function (): void {
Route::get('/audiences', [SegmentationController::class, 'index']);
Route::post('/audiences', [SegmentationController::class, 'store']);
Route::patch('/audiences/{audience}', [SegmentationController::class, 'update']);
Route::get('/audiences/{audience}/members', [SegmentationController::class, 'members']);
Route::post('/audiences/{audience}/refresh', [SegmentationController::class, 'refresh']);
Route::post('/events', [SegmentationController::class, 'event']);
```
<!-- layer-implementation-plan:end -->
