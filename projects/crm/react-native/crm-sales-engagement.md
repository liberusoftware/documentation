# Crm Sales Engagement React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-sales-engagement). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-sales-engagement-react-native
**Matching core package:** module-crm-crm-sales-engagement ([implementation](../core/crm-sales-engagement.md))
**Matching API package:** module-crm-crm-sales-engagement-api ([contract](../api/crm-sales-engagement.md))

## Implementation plan

This adapter presents Crm Sales Engagement for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Sales Engagement API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/crm-sales-engagement.md), and [API module](../api/crm-sales-engagement.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `crm-sales-engagement`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-sales-engagement.md)) |
| Capability React Native module skeleton | [`module-crm-sales-engagement-react-native`](https://github.com/liberusoftware/module-crm-sales-engagement-react-native) (`@liberusoftware/module-crm-sales-engagement-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Sequences/cadences** | Progressive mobile list/detail/sheet flow for `sequences/cadences` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Multi-channel steps** | Progressive mobile list/detail/sheet flow for `multi-channel steps` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Templates/snippets** | Progressive mobile list/detail/sheet flow for `templates/snippets` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Task queues** | Progressive mobile list/detail/sheet flow for `task queues` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Enrollment/re-entry** | Progressive mobile list/detail/sheet flow for `enrollment/re-entry` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Throttles** | Progressive mobile list/detail/sheet flow for `throttles` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Timezone windows** | Progressive mobile list/detail/sheet flow for `timezone windows` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Reply/meeting stop rules** | Progressive mobile list/detail/sheet flow for `reply/meeting stop rules` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Experiments** | Progressive mobile list/detail/sheet flow for `experiments` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [EngagementQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Queries/EngagementQuery.php) | `public function sequences(int $teamId)`<br>`public function enrollments(int $teamId)`<br>`public function tasks(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddStep.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Actions/AddStep.php) | `public function execute(int $teamId, int $actorId, array $data): EngagementStep` |
| [CreateSequence.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Actions/CreateSequence.php) | `public function execute(int $teamId, int $actorId, array $data): EngagementSequence` |
| [EnrollContact.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Actions/EnrollContact.php) | `public function execute(int $teamId, int $actorId, array $data): Enrollment` |
| [RecordEngagementEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Actions/RecordEngagementEvent.php) | `public function execute(int $teamId, int $actorId, array $data): EngagementEvent` |
| [StopEnrollment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Actions/StopEnrollment.php) | `public function execute(int $teamId, int $actorId, int $id, string $reason): Enrollment` |
| [UpdateSequence.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Actions/UpdateSequence.php) | `public function execute(int $teamId, int $actorId, int $sequenceId, array $data): EngagementSequence` |
| [EngagementPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Services/EngagementPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [EngagementEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Models/EngagementEvent.php) | No literal fillable array detected; inspect the model and API schema. |
| [EngagementSequence.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Models/EngagementSequence.php) | No literal fillable array detected; inspect the model and API schema. |
| [EngagementStep.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Models/EngagementStep.php) | No literal fillable array detected; inspect the model and API schema. |
| [EngagementTask.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Models/EngagementTask.php) | No literal fillable array detected; inspect the model and API schema. |
| [Enrollment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement/src/Models/Enrollment.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [EngagementController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement-api/src/Http/Controllers/EngagementController.php) | `public function sequences(Request $r, EngagementQuery $q)`<br>`public function sequence(Request $r, CreateSequence $a)`<br>`public function step(Request $r, AddStep $a)`<br>`public function enrollments(Request $r, EngagementQuery $q)`<br>`public function enroll(Request $r, EnrollContact $a)`<br>`public function stop(Request $r, int $enrollment, string $reason, StopEnrollment $a)`<br>`public function tasks(Request $request, EngagementQuery $query)`<br>`public function complete(Request $request, int $task, CompleteEngagementTask $action)`<br>`public function event(Request $r, RecordEngagementEvent $a)` |

**Observed route declarations:**

[modules/crm-sales-engagement-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-sales-engagement-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/sales-engagement')->group(function (): void {
Route::get('/sequences', [EngagementController::class, 'sequences']);
Route::post('/sequences', [EngagementController::class, 'sequence']);
Route::post('/steps', [EngagementController::class, 'step']);
Route::get('/enrollments', [EngagementController::class, 'enrollments']);
Route::post('/enrollments', [EngagementController::class, 'enroll']);
Route::post('/enrollments/{enrollment}/stop/{reason}', [EngagementController::class, 'stop']);
Route::get('/tasks', [EngagementController::class, 'tasks']);
Route::post('/tasks/{task}/complete', [EngagementController::class, 'complete']);
Route::post('/events', [EngagementController::class, 'event']);
```
<!-- layer-implementation-plan:end -->
