# Crm Unified Conversations React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#crm-unified-conversations). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-crm-crm-unified-conversations-react-native
**Matching core package:** module-crm-crm-unified-conversations ([implementation](../core/crm-unified-conversations.md))
**Matching API package:** module-crm-crm-unified-conversations-api ([contract](../api/crm-unified-conversations.md))

## Implementation plan

This adapter presents Crm Unified Conversations for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Crm Unified Conversations API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/crm-unified-conversations.md), and [API module](../api/crm-unified-conversations.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `crm-unified-conversations`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-crm-mobile-react`](https://github.com/liberusoftware/project-crm-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-crm-laravel-api`](https://github.com/liberusoftware/project-crm-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/crm-unified-conversations.md)) |
| Capability React Native module skeleton | [`module-crm-unified-conversations-react-native`](https://github.com/liberusoftware/module-crm-unified-conversations-react-native) (`@liberusoftware/module-crm-unified-conversations-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Omnichannel threads** | Progressive mobile list/detail/sheet flow for `omnichannel threads` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Participants** | Progressive mobile list/detail/sheet flow for `participants` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Identity matching** | Progressive mobile list/detail/sheet flow for `identity matching` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Assignments** | Progressive mobile list/detail/sheet flow for `assignments` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Collision detection** | Progressive mobile list/detail/sheet flow for `collision detection` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Drafts** | Progressive mobile list/detail/sheet flow for `drafts` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Internal notes** | Progressive mobile list/detail/sheet flow for `internal notes` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Attachments** | Progressive mobile list/detail/sheet flow for `attachments` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Delivery/read state** | Progressive mobile list/detail/sheet flow for `delivery/read state` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Timeline** | Progressive mobile list/detail/sheet flow for `timeline` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-crm-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core query | Public method signatures |
| --- | --- |
| [ConversationQuery.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Queries/ConversationQuery.php) | `public function list(int $teamId)`<br>`public function find(int $teamId, int $id): Conversation` |

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AssignConversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Actions/AssignConversation.php) | `public function execute(int $teamId, int $actorId, int $conversationId, ?int $assignee): Conversation` |
| [OpenConversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Actions/OpenConversation.php) | `public function execute(int $teamId, int $actorId, array $data): Conversation` |
| [SendMessage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Actions/SendMessage.php) | `public function execute(int $teamId, int $actorId, int $conversationId, array $data): ConversationMessage` |
| [SyncExternalConversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Actions/SyncExternalConversation.php) | `public function execute(int $teamId, array $data): Conversation` |
| [ConversationAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Services/ConversationAudit.php) | `public function record(int $teamId, ?int $actorId, string $event, array $details = []): void` |
| [ConversationPolicy.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Services/ConversationPolicy.php) | `public function canManage(int $teamId, int $userId): bool` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Conversation.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Models/Conversation.php) | `team_id`, `channel`, `external_id`, `subject`, `status`, `priority`, `assigned_to`, `last_message_at`, `metadata` |
| [ConversationAudit.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Models/ConversationAudit.php) | `team_id`, `actor_id`, `event`, `details` |
| [ConversationMessage.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Models/ConversationMessage.php) | `team_id`, `conversation_id`, `external_id`, `sender_id`, `body`, `direction`, `metadata`, `internal`, `delivery_status`, `read_at`, `idempotency_key` |
| [ConversationParticipant.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations/src/Models/ConversationParticipant.php) | `team_id`, `conversation_id`, `identity`, `name`, `role` |

| Observed API controller | Handler signatures |
| --- | --- |
| [ConversationController.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations-api/src/Http/Controllers/ConversationController.php) | `public function index(Request $r, ConversationQuery $q): JsonResponse`<br>`public function store(Request $r, OpenConversation $a): JsonResponse`<br>`public function message(Request $r, int $conversation, SendMessage $a): JsonResponse` |

**Observed route declarations:**

[modules/crm-unified-conversations-api/routes/api.php](https://github.com/liberusoftware/project-crm-laravel-filament/blob/63aad94e94c0f9a18038e301eb979138c657be64/modules/crm-unified-conversations-api/routes/api.php)

```php
Route::middleware(['auth:sanctum', 'throttle:api'])->prefix('api/v1/crm/unified-conversations')->group(function () {
Route::get('/', [ConversationController::class, 'index']);
Route::post('/', [ConversationController::class, 'store']);
Route::post('/{conversation}/messages', [ConversationController::class, 'message']);
```
<!-- layer-implementation-plan:end -->
