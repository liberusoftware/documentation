# Crm Chat And Bots React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-chat-and-bots). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-chat-and-bots-react-native
**Matching core package:** module-crm-crm-chat-and-bots ([implementation](../core/crm-chat-and-bots.md))
**Matching API package:** module-crm-crm-chat-and-bots-api ([contract](../api/crm-chat-and-bots.md))

## Implementation plan

This adapter presents Crm Chat And Bots for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Chat And Bots API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/crm-chat-and-bots.md), and [API module](../api/crm-chat-and-bots.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `crm-chat-and-bots`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-chat-and-bots.md)) |
| Capability React Native module skeleton | [`module-crm-chat-and-bots-react-native`](https://github.com/liberusoftware/module-crm-chat-and-bots-react-native) (`@liberusoftware/module-crm-chat-and-bots-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Web chat** | Progressive mobile list/detail/sheet flow for `web chat` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Bot/playbook builder** | Progressive mobile list/detail/sheet flow for `bot/playbook builder` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Qualification** | Progressive mobile list/detail/sheet flow for `qualification` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Knowledge answers** | Progressive mobile list/detail/sheet flow for `knowledge answers` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Meeting booking** | Progressive mobile list/detail/sheet flow for `meeting booking` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Live-agent handoff** | Progressive mobile list/detail/sheet flow for `live-agent handoff` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Office hours** | Progressive mobile list/detail/sheet flow for `office hours` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Transcripts** | Progressive mobile list/detail/sheet flow for `transcripts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Channel identity** | Progressive mobile list/detail/sheet flow for `channel identity` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ChatBotQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-chat-and-bots/src/Queries/ChatBotQuery.php) | `public function bots(int $teamId): Builder`<br>`public function sessions(int $teamId): Builder` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [CreateChatBot.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-chat-and-bots/src/Actions/CreateChatBot.php) | `public function execute(int $teamId, int $ownerId, string $name, array $playbook, array $channels = []): ChatBot` |
| [HandoffChatSession.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-chat-and-bots/src/Actions/HandoffChatSession.php) | `public function execute(int $teamId, ChatSession $session, string $assignee): ChatSession` |
| [StartChatSession.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-chat-and-bots/src/Actions/StartChatSession.php) | `public function execute(int $teamId, ChatBot $bot, string $visitorKey, string $channel = 'web'): ChatSession` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [ChatBot.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-chat-and-bots/src/Models/ChatBot.php) | No literal fillable array detected; inspect the model and API schema. |
| [ChatSession.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-chat-and-bots/src/Models/ChatSession.php) | No literal fillable array detected; inspect the model and API schema. |

| Observed API controller | Handler signatures |
| --- | --- |
| [ChatAndBotsController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-chat-and-bots-api/src/Http/Controllers/ChatAndBotsController.php) | `public function __construct(private readonly ChatBotQuery $query)`<br>`public function bots(Request $request): JsonResponse`<br>`public function store(Request $request, CreateChatBot $a): JsonResponse`<br>`public function session(Request $request, ChatBot $bot, StartChatSession $a): JsonResponse`<br>`public function handoff(Request $request, ChatSession $session, HandoffChatSession $a): JsonResponse` |

**Observed route declarations:**

[modules/crm-chat-and-bots-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-chat-and-bots-api/routes/api.php)

```php
Route::middleware('auth:sanctum')->prefix('api/v1/crm/chat-and-bots')->group(function (): void {
Route::get('bots', [ChatAndBotsController::class, 'bots']);
Route::post('bots', [ChatAndBotsController::class, 'store']);
Route::post('bots/{bot}/sessions', [ChatAndBotsController::class, 'session']);
Route::post('sessions/{session}/handoff', [ChatAndBotsController::class, 'handoff']);
```
<!-- layer-implementation-plan:end -->
