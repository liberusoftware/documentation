# Crm Activities React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-activities). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-activities-react-native
**Matching core package:** module-crm-crm-activities ([implementation](../core/crm-activities.md))
**Matching API package:** module-crm-crm-activities-api ([contract](../api/crm-activities.md))

## Implementation plan

This adapter presents Crm Activities for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Activities API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/crm-activities.md), and [API module](../api/crm-activities.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `crm-activities`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-activities.md)) |
| Capability React Native module skeleton | [`module-crm-activities-react-native`](https://github.com/liberusoftware/module-crm-activities-react-native) (`@liberusoftware/module-crm-activities-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Tasks** | Progressive mobile list/detail/sheet flow for `tasks` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Calls** | Progressive mobile list/detail/sheet flow for `calls` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Meetings** | Progressive mobile list/detail/sheet flow for `meetings` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Emails** | Progressive mobile list/detail/sheet flow for `emails` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Deadlines** | Progressive mobile list/detail/sheet flow for `deadlines` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Recurrence** | Progressive mobile list/detail/sheet flow for `recurrence` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Queues** | Progressive mobile list/detail/sheet flow for `queues` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Bulk completion** | Progressive mobile list/detail/sheet flow for `bulk completion` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Reminders** | Progressive mobile list/detail/sheet flow for `reminders` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Outcomes** | Progressive mobile list/detail/sheet flow for `outcomes` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Goals** | Progressive mobile list/detail/sheet flow for `goals` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Activity reporting** | Progressive mobile list/detail/sheet flow for `activity reporting` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CancelActivity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities/src/Actions/CancelActivity.php) | `public function execute(Activity $activity): Activity` |
| [CompleteActivities.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities/src/Actions/CompleteActivities.php) | `public function execute(int $teamId, array $activityIds, ?string $outcome = null, ?string $notes = null): int` |
| [CreateActivity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities/src/Actions/CreateActivity.php) | `public function execute(int $teamId, ?int $actorId, array $attributes): Activity` |
| [CreateActivityGoal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities/src/Actions/CreateActivityGoal.php) | `public function execute(int $teamId, array $attributes): ActivityGoal` |
| [ActivityReport.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities/src/Services/ActivityReport.php) | `public function summarize(int $teamId, Carbon $from, Carbon $until): array` |
| [ActivityScheduler.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities/src/Services/ActivityScheduler.php) | `public function nextOccurrence(Activity $activity): ?Activity`<br>`public function dueReminders(int $teamId, ?Carbon $at = null): Collection` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Activity.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities/src/Models/Activity.php) | `team_id`, `actor_id`, `assigned_to`, `kind`, `status`, `title`, `description`, `subject_type`, `subject_id`, `starts_at`, `due_at`, `ends_at`, `recurrence`, `recurrence_until`, `reminder_at`, `queue`, `outcome`, `outcome_notes`, `metadata`, `completed_at` |
| [ActivityEvent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities/src/Models/ActivityEvent.php) | `team_id`, `activity_id`, `actor_id`, `event`, `details` |
| [ActivityGoal.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities/src/Models/ActivityGoal.php) | `team_id`, `owner_id`, `name`, `kind`, `target`, `progress`, `starts_at`, `ends_at`, `status`, `criteria` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ActivityController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities-api/src/Http/Controllers/ActivityController.php) | `public function index(Request $request): JsonResponse`<br>`public function store(Request $request, CreateActivity $create): JsonResponse`<br>`public function show(Request $request, int $activity): JsonResponse`<br>`public function update(Request $request, int $activity): JsonResponse`<br>`public function complete(Request $request, CompleteActivities $complete): JsonResponse`<br>`public function cancel(Request $request, int $activity, CancelActivity $cancel): JsonResponse`<br>`public function report(Request $request, ActivityReport $report): JsonResponse` |

**Observed route declarations:**

[modules/crm-activities-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-activities-api/routes/api.php)

```php
Route::middleware(['auth:sanctum', 'throttle:api'])->prefix('api/v1/crm/activities')->group(function (): void {
Route::get('/', [ActivityController::class, 'index']);
Route::post('/', [ActivityController::class, 'store']);
Route::get('/report', [ActivityController::class, 'report']);
Route::post('/complete', [ActivityController::class, 'complete']);
Route::get('/{activity}', [ActivityController::class, 'show']);
Route::patch('/{activity}', [ActivityController::class, 'update']);
Route::post('/{activity}/cancel', [ActivityController::class, 'cancel']);
```
<!-- layer-implementation-plan:end -->
