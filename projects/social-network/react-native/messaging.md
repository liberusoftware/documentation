# Messaging React Native + Expo

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#messaging). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-social-network-messaging-react-native
**Matching core package:** module-social-network-messaging ([implementation](../core/messaging.md))
**Matching API package:** module-social-network-messaging-api ([contract](../api/messaging.md))

## Implementation plan

This adapter presents Messaging for the React Native + Expo surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use strict TypeScript, typed navigation, schema-validated API responses, secure Keychain/Keystore storage, and platform permission boundaries.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Messaging API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [React Native + Expo standard](../../../standards/REACT-NATIVE.md), [mobile architecture](../../../architecture/MOBILE.md), [React Native + Expo technology](../../../technologies/REACT-NATIVE.md), [core module](../core/messaging.md), and [API module](../api/messaging.md).

<!-- layer-implementation-plan:start -->
## Structured mobile feature plan, skeleton repository, and source evidence

**Matching domain module:** `messaging`

| Delivery boundary | Repository / specification | Role in implementation |
| --- | --- | --- |
| Product React Native Expo host skeleton | [`project-social-network-mobile-react`](https://github.com/liberusoftware/project-social-network-mobile-react) | Native iOS/Android Expo Router application shell, SecureStore session provider, and EAS build config ([template](https://github.com/liberusoftware/project-boilerplate-mobile-react) · [wayfinder](../../wayfinders/mobile-react.md) · [runbook](../../../guides/presentation/REACT-NATIVE.md)) |
| Shared product API backend | [`project-social-network-laravel-api`](https://github.com/liberusoftware/project-social-network-laravel-api) | Authoritative Laravel HTTP composition root ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [API plan](../api/messaging.md)) |
| Capability React Native module skeleton | [`module-social-network-messaging-react-native`](https://github.com/liberusoftware/module-social-network-messaging-react-native) (`@liberusoftware/module-social-network-messaging-react-native`) | Metro-compatible TypeScript mobile screens, hooks, and DTO validators ([foundation](https://github.com/liberusoftware/module-boilerplate-react-native) · [catalog](../../../modules/skeletons/mobile-react.md)) |

### React Native + Expo feature and mobile screen matrix

| Feature / aspect | Native iOS / Android screen, navigation & accessibility | Typed API client, SecureStore & offline/retry recovery |
| --- | --- | --- |
| **Conversations** | Progressive mobile list/detail/sheet flow for `conversations` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Membership** | Progressive mobile list/detail/sheet flow for `membership` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Delivery/read state** | Progressive mobile list/detail/sheet flow for `delivery/read state` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Attachments** | Progressive mobile list/detail/sheet flow for `attachments` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Requests** | Progressive mobile list/detail/sheet flow for `requests` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Safety** | Progressive mobile list/detail/sheet flow for `safety` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |
| **Retention** | Progressive mobile list/detail/sheet flow for `retention` with safe areas, touch-target sizing, screen-reader labels, and validated deep links. | Call `project-social-network-laravel-api` via injected session-scoped client; isolate local drafts by account/workspace, and reconcile timeouts with `Idempotency-Key` before retry. |

### Observed domain and transport source evidence

| Observed core action / service / policy | Public method signatures |
| --- | --- |
| [AddParticipant.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Actions/AddParticipant.php) | `public function __construct(private MessagingAuthorizer $authorizer)`<br>`public function handle(Profile $actor, string $conversationId, Profile $participant): void` |
| [AddReaction.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Actions/AddReaction.php) | `public function __construct( private MessagingAuthorizer $authorizer, private Dispatcher $events, )`<br>`public function handle(Profile $profile, Message $message, string $emoji): MessageReaction` |
| [CreateConversation.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Actions/CreateConversation.php) | `public function __construct(private MessagingAuthorizer $authorizer)`<br>`public function handle(Profile $creator, ?string $title = null, array $participantIds = []): Conversation` |
| [DeleteMessage.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Actions/DeleteMessage.php) | `public function __construct(private MessagingAuthorizer $authorizer)`<br>`public function handle(Profile $actor, string $conversationId, Message $message): void` |
| [GetConversation.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Actions/GetConversation.php) | `public function handle(Profile $viewer, string $conversationId): Conversation` |
| [ListConversations.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Actions/ListConversations.php) | `public function handle(Profile $profile, int $limit = 25): Collection` |
| [MarkConversationRead.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Actions/MarkConversationRead.php) | `public function handle(Profile $profile, string $conversationId): void` |
| [RemoveParticipant.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Actions/RemoveParticipant.php) | `public function __construct(private MessagingAuthorizer $authorizer)`<br>`public function handle(Profile $actor, string $conversationId, Profile $participant): void` |
| [RemoveReaction.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Actions/RemoveReaction.php) | `public function __construct(private MessagingAuthorizer $authorizer)`<br>`public function handle(Profile $profile, Message $message, string $emoji): void` |
| [SendMessage.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Actions/SendMessage.php) | `public function __construct(private MessagingAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $sender, string $conversationId, string $body, array $attachments = [], bool $encrypted = false): Message` |

| Observed storage model | Fillable attributes (review sensitivity for DTO projection) |
| --- | --- |
| [Conversation.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Models/Conversation.php) | `id`, `created_by_profile_id`, `state`, `title` |
| [Message.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Models/Message.php) | `id`, `conversation_id`, `sender_profile_id`, `body`, `encrypted_body`, `encryption_key_id`, `state`, `attachments` |
| [MessageReaction.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Models/MessageReaction.php) | `id`, `message_id`, `conversation_id`, `profile_id`, `emoji` |

| Observed API controller | Handler signatures |
| --- | --- |
| [MessagingController.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging-api/src/Http/Controllers/MessagingController.php) | `public function conversation(Request $request, GetProfile $get, CreateConversation $create): JsonResponse`<br>`public function index(Request $request, GetProfile $get, ListConversations $list): JsonResponse`<br>`public function unreadCount(Request $request, GetProfile $get, UnreadMessageCount $count): JsonResponse`<br>`public function show(string $conversation, Request $request, GetProfile $get, GetConversation $view): JsonResponse`<br>`public function messages(string $conversation, Request $request, GetProfile $get, GetConversation $view): JsonResponse`<br>`public function message(string $conversation, Request $request, GetProfile $get, SendMessage $send): JsonResponse`<br>`public function reaction(string $conversation, Message $message, Request $request, GetProfile $get, AddReaction $add): JsonResponse`<br>`public function removeReaction(string $conversation, Message $message, string $emoji, Request $request, GetProfile $get, RemoveReaction $remove): JsonResponse`<br>`public function typing(string $conversation, Request $request, GetProfile $get): JsonResponse`<br>`public function read(string $conversation, Request $request, GetProfile $get, MarkConversationRead $read): JsonResponse`<br>`public function destroyMessage(string $conversation, string $message, Request $request, GetProfile $get, DeleteMessage $delete): JsonResponse`<br>`public function addParticipant(string $conversation, Request $request, GetProfile $get, AddParticipant $add): JsonResponse`<br>`public function removeParticipant(string $conversation, string $profile, Request $request, GetProfile $get, RemoveParticipant $remove): JsonResponse` |

**Observed route declarations:**

[modules/social-network-messaging-api/routes/api.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging-api/routes/api.php)

```php
Route::prefix('api/v1/social-network/messaging')
Route::get('/conversations', [MessagingController::class, 'index'])->name('index');
Route::post('/conversations', [MessagingController::class, 'conversation'])->name('conversation');
Route::get('/unread-count', [MessagingController::class, 'unreadCount'])->name('unread-count');
Route::get('/conversations/{conversation}', [MessagingController::class, 'show'])->name('show');
Route::get('/conversations/{conversation}/messages', [MessagingController::class, 'messages'])->name('messages');
Route::post('/conversations/{conversation}/participants', [MessagingController::class, 'addParticipant'])->name('participants.add');
Route::delete('/conversations/{conversation}/participants/{profile}', [MessagingController::class, 'removeParticipant'])->name('participants.remove');
Route::post('/conversations/{conversation}/messages', [MessagingController::class, 'message'])->name('message');
Route::delete('/conversations/{conversation}/messages/{message}', [MessagingController::class, 'destroyMessage'])->name('message.destroy');
Route::post('/conversations/{conversation}/messages/{message}/reactions', [MessagingController::class, 'reaction'])->name('reaction');
Route::delete('/conversations/{conversation}/messages/{message}/reactions/{emoji}', [MessagingController::class, 'removeReaction'])->name('reaction.remove');
Route::post('/conversations/{conversation}/typing', [MessagingController::class, 'typing'])->name('typing');
Route::post('/conversations/{conversation}/read', [MessagingController::class, 'read'])->name('read');
```
<!-- layer-implementation-plan:end -->
