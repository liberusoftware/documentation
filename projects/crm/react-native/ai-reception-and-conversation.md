# Ai Reception And Conversation React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#ai-reception-and-conversation). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-ai-reception-and-conversation-react-native
**Matching core package:** module-crm-ai-reception-and-conversation ([implementation](../core/ai-reception-and-conversation.md))
**Matching API package:** module-crm-ai-reception-and-conversation-api ([contract](../api/ai-reception-and-conversation.md))

## Implementation plan

This adapter presents Ai Reception And Conversation for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Ai Reception And Conversation API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/ai-reception-and-conversation.md), and [API module](../api/ai-reception-and-conversation.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `ai-reception-and-conversation`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/ai-reception-and-conversation.md)) |
| Capability React Native module skeleton | [`module-crm-ai-reception-and-conversation-react-native`](https://github.com/liberusoftware/module-crm-ai-reception-and-conversation-react-native) (`@liberusoftware/module-crm-ai-reception-and-conversation-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Governed chat/voice agents** | Progressive mobile list/detail/sheet flow for `governed chat/voice agents` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Approved knowledge/tools** | Progressive mobile list/detail/sheet flow for `approved knowledge/tools` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Qualification** | Progressive mobile list/detail/sheet flow for `qualification` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Booking** | Progressive mobile list/detail/sheet flow for `booking` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Summaries** | Progressive mobile list/detail/sheet flow for `summaries` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Confidence** | Progressive mobile list/detail/sheet flow for `confidence` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Live handoff** | Progressive mobile list/detail/sheet flow for `live handoff` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Testing** | Progressive mobile list/detail/sheet flow for `testing` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Human-approval policy** | Progressive mobile list/detail/sheet flow for `human-approval policy` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [ActivateReceptionAgent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation/src/Actions/ActivateReceptionAgent.php) | `public function execute(int $teamId, ReceptionAgent $agent): ReceptionAgent` |
| [CreateReceptionAgent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation/src/Actions/CreateReceptionAgent.php) | `public function execute(int $teamId, int $ownerId, array $input): ReceptionAgent` |
| [RecordReceptionTurn.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation/src/Actions/RecordReceptionTurn.php) | `public function execute(int $teamId, int $actorId, ReceptionConversation $conversation, array $input): ReceptionConversation` |
| [RequestReceptionHandoff.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation/src/Actions/RequestReceptionHandoff.php) | `public function execute(int $teamId, int $actorId, ReceptionConversation $conversation, string $reason): ReceptionConversation` |
| [StartReceptionConversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation/src/Actions/StartReceptionConversation.php) | `public function execute(int $teamId, ReceptionAgent $agent, array $input = []): ReceptionConversation` |
| [ReceptionResponder.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation/src/Services/ReceptionResponder.php) | `public function respond(ReceptionAgent $agent, ReceptionConversation $conversation, string $input): string` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ReceptionAgent.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation/src/Models/ReceptionAgent.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReceptionAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation/src/Models/ReceptionAudit.php) | No literal fillable array detected; inspect the model and API schema. |
| [ReceptionConversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation/src/Models/ReceptionConversation.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ReceptionController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation-api/src/Http/Controllers/ReceptionController.php) | `public function agents(Request $request): JsonResponse`<br>`public function createAgent(Request $request, CreateReceptionAgent $action): JsonResponse`<br>`public function activate(Request $request, ReceptionAgent $agent, ActivateReceptionAgent $action): JsonResponse`<br>`public function start(Request $request, ReceptionAgent $agent, StartReceptionConversation $action): JsonResponse`<br>`public function turn(Request $request, ReceptionConversation $conversation, RecordReceptionTurn $action): JsonResponse`<br>`public function handoff(Request $request, ReceptionConversation $conversation, RequestReceptionHandoff $action): JsonResponse` |

**Observed route declarations:**

[modules/crm-ai-reception-and-conversation-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-ai-reception-and-conversation-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/ai-reception-and-conversation')->group(function (): void {
Route::get('agents', [ReceptionController::class, 'agents']);
Route::post('agents', [ReceptionController::class, 'createAgent']);
Route::post('agents/{agent}/activate', [ReceptionController::class, 'activate']);
Route::post('agents/{agent}/conversations', [ReceptionController::class, 'start']);
Route::post('conversations/{conversation}/turns', [ReceptionController::class, 'turn']);
Route::post('conversations/{conversation}/handoff', [ReceptionController::class, 'handoff']);
```
<!-- layer-implementation-plan:end -->
