# Prospecting Agent React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#prospecting-agent). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-prospecting-agent-react-native
**Matching core package:** module-crm-prospecting-agent ([implementation](../core/prospecting-agent.md))
**Matching API package:** module-crm-prospecting-agent-api ([contract](../api/prospecting-agent.md))

## Implementation plan

This adapter presents Prospecting Agent for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Prospecting Agent API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/prospecting-agent.md), and [API module](../api/prospecting-agent.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `prospecting-agent`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/prospecting-agent.md)) |
| Capability React Native module skeleton | [`module-crm-prospecting-agent-react-native`](https://github.com/liberusoftware/module-crm-prospecting-agent-react-native) (`@liberusoftware/module-crm-prospecting-agent-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Approved research** | Progressive mobile list/detail/sheet flow for `approved research` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Target selection** | Progressive mobile list/detail/sheet flow for `target selection` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Personalization** | Progressive mobile list/detail/sheet flow for `personalization` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Sequence preparation** | Progressive mobile list/detail/sheet flow for `sequence preparation` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Engagement monitoring** | Progressive mobile list/detail/sheet flow for `engagement monitoring` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Policy-based review/dispatch** | Progressive mobile list/detail/sheet flow for `policy-based review/dispatch` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ProspectingAgentQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent/src/Queries/ProspectingAgentQuery.php) | `public function runs(int $teamId)`<br>`public function targets(int $teamId)`<br>`public function sequences(int $teamId)`<br>`public function engagements(int $teamId)` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ApproveAgentRun.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent/src/Actions/ApproveAgentRun.php) | `public function __construct(private readonly ProspectingAgentPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $runId): AgentRun` |
| [CreateAgentRun.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent/src/Actions/CreateAgentRun.php) | `public function __construct(private readonly ProspectingAgentPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): AgentRun` |
| [DispatchSequence.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent/src/Actions/DispatchSequence.php) | `public function __construct(private readonly ProspectingAgentPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $sequenceId): AgentSequence` |
| [PrepareSequence.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent/src/Actions/PrepareSequence.php) | `public function __construct(private readonly ProspectingAgentPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): AgentSequence` |
| [RecordEngagement.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent/src/Actions/RecordEngagement.php) | `public function __construct(private readonly ProspectingAgentPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): AgentEngagement` |
| [SelectTarget.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent/src/Actions/SelectTarget.php) | `public function __construct(private readonly ProspectingAgentPolicy $policy)`<br>`public function execute(int $teamId, int $userId, array $input): AgentTarget` |
| [UpdateAgentRun.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent/src/Actions/UpdateAgentRun.php) | `public function __construct(private readonly ProspectingAgentPolicy $policy)`<br>`public function execute(int $teamId, int $userId, int $runId, array $input): AgentRun` |
| [ProspectingAgentPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent/src/Services/ProspectingAgentPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [AgentEngagement.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent/src/Models/AgentEngagement.php) | No literal fillable array detected; inspect the model and API schema. |
| [AgentRun.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent/src/Models/AgentRun.php) | No literal fillable array detected; inspect the model and API schema. |
| [AgentSequence.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent/src/Models/AgentSequence.php) | No literal fillable array detected; inspect the model and API schema. |
| [AgentTarget.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent/src/Models/AgentTarget.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ProspectingAgentController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent-api/src/Http/Controllers/ProspectingAgentController.php) | `public function runs(Request $r, ProspectingAgentQuery $q)`<br>`public function run(Request $r, CreateAgentRun $a)`<br>`public function approve(Request $r, int $run, ApproveAgentRun $a)`<br>`public function target(Request $r, SelectTarget $a)`<br>`public function sequence(Request $r, PrepareSequence $a)`<br>`public function dispatch(Request $r, int $sequence, DispatchSequence $a)`<br>`public function engagement(Request $r, RecordEngagement $a)` |

**Observed route declarations:**

[modules/crm-prospecting-agent-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-prospecting-agent-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/prospecting-agent')->group(function (): void {
Route::get('/runs', [ProspectingAgentController::class, 'runs']);
Route::post('/runs', [ProspectingAgentController::class, 'run']);
Route::post('/runs/{run}/approve', [ProspectingAgentController::class, 'approve']);
Route::post('/targets', [ProspectingAgentController::class, 'target']);
Route::post('/sequences', [ProspectingAgentController::class, 'sequence']);
Route::post('/sequences/{sequence}/dispatch', [ProspectingAgentController::class, 'dispatch']);
Route::post('/engagements', [ProspectingAgentController::class, 'engagement']);
```
<!-- layer-implementation-plan:end -->
