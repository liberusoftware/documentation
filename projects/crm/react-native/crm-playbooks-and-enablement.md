# Crm Playbooks And Enablement React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-playbooks-and-enablement). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-playbooks-and-enablement-react-native
**Matching core package:** module-crm-crm-playbooks-and-enablement ([implementation](../core/crm-playbooks-and-enablement.md))
**Matching API package:** module-crm-crm-playbooks-and-enablement-api ([contract](../api/crm-playbooks-and-enablement.md))

## Implementation plan

This adapter presents Crm Playbooks And Enablement for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Playbooks And Enablement API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/crm-playbooks-and-enablement.md), and [API module](../api/crm-playbooks-and-enablement.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `crm-playbooks-and-enablement`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-playbooks-and-enablement.md)) |
| Capability React Native module skeleton | [`module-crm-playbooks-and-enablement-react-native`](https://github.com/liberusoftware/module-crm-playbooks-and-enablement-react-native) (`@liberusoftware/module-crm-playbooks-and-enablement-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Guided scripts** | Progressive mobile list/detail/sheet flow for `guided scripts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Qualification cards** | Progressive mobile list/detail/sheet flow for `qualification cards` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Battlecards** | Progressive mobile list/detail/sheet flow for `battlecards` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Onboarding content** | Progressive mobile list/detail/sheet flow for `onboarding content` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Required evidence** | Progressive mobile list/detail/sheet flow for `required evidence` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Coaching checklists** | Progressive mobile list/detail/sheet flow for `coaching checklists` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Document/content recommendations** | Progressive mobile list/detail/sheet flow for `document/content recommendations` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Usage analytics** | Progressive mobile list/detail/sheet flow for `usage analytics` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [PlaybookQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Queries/PlaybookQuery.php) | `public function playbooks(int $teamId)`<br>`public function assignments(int $teamId)`<br>`public function recommendations(int $teamId)`<br>`public function usage(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AssignPlaybook.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Actions/AssignPlaybook.php) | `public function __construct(private readonly PlaybookPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PlaybookAssignment` |
| [CompletePlaybook.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Actions/CompletePlaybook.php) | `public function __construct(private readonly PlaybookPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $assignmentId, array $input): PlaybookAssignment` |
| [CreatePlaybook.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Actions/CreatePlaybook.php) | `public function __construct(private readonly PlaybookPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): Playbook` |
| [RecommendPlaybook.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Actions/RecommendPlaybook.php) | `public function __construct(private readonly PlaybookPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PlaybookRecommendation` |
| [RecordPlaybookUsage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Actions/RecordPlaybookUsage.php) | `public function __construct(private readonly PlaybookPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): PlaybookUsage` |
| [UpdatePlaybook.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Actions/UpdatePlaybook.php) | `public function __construct(private readonly PlaybookPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $playbookId, array $input): Playbook` |
| [PlaybookPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Services/PlaybookPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Playbook.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Models/Playbook.php) | No literal fillable array detected; inspect the model and API schema. |
| [PlaybookAssignment.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Models/PlaybookAssignment.php) | No literal fillable array detected; inspect the model and API schema. |
| [PlaybookRecommendation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Models/PlaybookRecommendation.php) | No literal fillable array detected; inspect the model and API schema. |
| [PlaybookUsage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement/src/Models/PlaybookUsage.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [PlaybooksAndEnablementController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement-api/src/Http/Controllers/PlaybooksAndEnablementController.php) | `public function playbooks(Request $r, PlaybookQuery $q)`<br>`public function playbook(Request $r, CreatePlaybook $a)`<br>`public function assignment(Request $r, AssignPlaybook $a)`<br>`public function complete(Request $r, int $assignment, CompletePlaybook $a)`<br>`public function recommendation(Request $r, RecommendPlaybook $a)`<br>`public function usage(Request $r, RecordPlaybookUsage $a)` |

**Observed route declarations:**

[modules/crm-playbooks-and-enablement-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-playbooks-and-enablement-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/playbooks-and-enablement')->group(function (): void {
Route::get('/playbooks', [PlaybooksAndEnablementController::class, 'playbooks']);
Route::post('/playbooks', [PlaybooksAndEnablementController::class, 'playbook']);
Route::post('/assignments', [PlaybooksAndEnablementController::class, 'assignment']);
Route::post('/assignments/{assignment}/complete', [PlaybooksAndEnablementController::class, 'complete']);
Route::post('/recommendations', [PlaybooksAndEnablementController::class, 'recommendation']);
Route::post('/usage', [PlaybooksAndEnablementController::class, 'usage']);
```
<!-- layer-implementation-plan:end -->
