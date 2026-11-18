# Accounting Client Collaboration React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#accounting-client-collaboration). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-accounting-accounting-client-collaboration-react-native
**Matching core package:** module-accounting-accounting-client-collaboration ([implementation](../core/accounting-client-collaboration.md))
**Matching API package:** module-accounting-accounting-client-collaboration-api ([contract](../api/accounting-client-collaboration.md))

## Implementation plan

This adapter presents Accounting Client Collaboration for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Accounting Client Collaboration API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/accounting-client-collaboration.md), and [API module](../api/accounting-client-collaboration.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `accounting-client-collaboration`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-accounting-erp-mobile-react`](https://github.com/liberusoftware/project-accounting-erp-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-accounting-erp-laravel-api`](https://github.com/liberusoftware/project-accounting-erp-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/accounting-client-collaboration.md)) |
| Capability React Native module skeleton | [`module-accounting-client-collaboration-react-native`](https://github.com/liberusoftware/module-accounting-client-collaboration-react-native) (`@liberusoftware/module-accounting-client-collaboration-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Secure document requests** | Progressive mobile list/detail/sheet flow for `secure document requests` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Questions** | Progressive mobile list/detail/sheet flow for `questions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Tasks** | Progressive mobile list/detail/sheet flow for `tasks` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Discussions** | Progressive mobile list/detail/sheet flow for `discussions` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Approvals** | Progressive mobile list/detail/sheet flow for `approvals` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Status** | Progressive mobile list/detail/sheet flow for `status` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Reminders** | Progressive mobile list/detail/sheet flow for `reminders` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Evidence** | Progressive mobile list/detail/sheet flow for `evidence` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-accounting-erp-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [CollaborationQuery.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-client-collaboration/src/Queries/CollaborationQuery.php) | `public function forTeam(int $teamId): Collection` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateCollaborationThread.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-client-collaboration/src/Actions/CreateCollaborationThread.php) | `public function handle(array $attributes): CollaborationThread` |
| [RecordCollaborationActivity.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-client-collaboration/src/Actions/RecordCollaborationActivity.php) | `public function message(CollaborationThread $thread, array $message): CollaborationThread`<br>`public function approval(CollaborationThread $thread, array $approval): CollaborationThread`<br>`public function reminder(CollaborationThread $thread, array $reminder): CollaborationThread`<br>`public function evidence(CollaborationThread $thread, array $evidence): CollaborationThread` |
| [ResolveCollaboration.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-client-collaboration/src/Actions/ResolveCollaboration.php) | `public function approve(CollaborationThread $thread, string $approver): CollaborationThread`<br>`public function close(CollaborationThread $thread): CollaborationThread` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [CollaborationThread.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-client-collaboration/src/Models/CollaborationThread.php) | `team_id`, `thread_ref`, `kind`, `subject`, `status`, `participants`, `messages`, `approvals`, `reminders`, `evidence` |

| Observed API controller | Handler signatures |
| --- | --- |
| [CollaborationController.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-client-collaboration-api/src/Http/Controllers/CollaborationController.php) | `public function index(CollaborationQuery $query): JsonResponse`<br>`public function store(Request $request, CreateCollaborationThread $action): JsonResponse`<br>`public function message(Request $request, string $thread, RecordCollaborationActivity $action): JsonResponse`<br>`public function approval(Request $request, string $thread, RecordCollaborationActivity $action): JsonResponse`<br>`public function evidence(Request $request, string $thread, RecordCollaborationActivity $action): JsonResponse` |

**Observed route declarations:**

[modules/accounting-client-collaboration-api/routes/api.php](https://github.com/liberusoftware/project-accounting-erp-laravel-filament/blob/39a49babafc0b8caf12c018abdd765f215ecf207/modules/accounting-client-collaboration-api/routes/api.php)

```php
Route::prefix('api/v1/accounting/client-collaboration')->middleware(['auth:sanctum', 'throttle:60,1'])->group(function (): void {
Route::middleware('ability:accounting.client-collaboration.read')->get('/', [CollaborationController::class, 'index']);
Route::middleware('ability:accounting.client-collaboration.write')->group(function (): void {
Route::post('/', [CollaborationController::class, 'store']);
Route::post('/{thread}/messages', [CollaborationController::class, 'message']);
Route::post('/{thread}/approvals', [CollaborationController::class, 'approval']);
Route::post('/{thread}/evidence', [CollaborationController::class, 'evidence']);
```
<!-- layer-implementation-plan:end -->
