# Social Network Messaging Flutter + Dart

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#social-network-messaging). No dedicated package name match was found for this layer in the scanned module manifests. Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

**Package:** module-social-network-social-network-messaging-flutter
**Matching core package:** module-social-network-social-network-messaging ([implementation](../core/social-network-messaging.md))
**Matching API package:** module-social-network-social-network-messaging-api ([contract](../api/social-network-messaging.md))

## Implementation plan

This adapter presents Social Network Messaging for the Flutter + Dart surface. It owns platform UI, navigation/state integration, device-facing behavior, and client error/recovery mapping; the matching core package remains authoritative for domain rules, persistence, authorization, tenancy, audit, and lifecycle transitions.

- Use sound Dart null safety, typed DTOs, stable Flutter plugins, secure platform storage, and explicit application state models.
- Preserve the API contract, tenant/team context, field visibility, localization, timezone/currency formatting, and server-side authorization.
- Model loading, empty, denied, offline, queued, conflict, retry, and recovery states; make writes idempotent and safe to resume after interruption.
- Support screen readers, dynamic text, keyboard/switch access, contrast, reduced motion, RTL, rotation, deep links, and platform back behavior.
- Document cache classification, expiry/invalidation, native permissions, push/deep-link handling, supported OS versions, and release configuration.

## Verification

Test Social Network Messaging API mapping, authorization outcomes, state transitions, lifecycle interruption, permission denial, offline/retry/conflict behavior, accessibility, localization, and signed release builds on supported platforms.

See [Flutter + Dart standard](../../../standards/FLUTTER.md), [mobile architecture](../../../architecture/MOBILE.md), [Flutter + Dart technology](../../../technologies/FLUTTER.md), [core module](../core/social-network-messaging.md), and [API module](../api/social-network-messaging.md).

<!-- layer-implementation-plan:start -->
## Structured Flutter mobile, Dart mobile, and Dart desktop implementation plan

**Matching domain module:** `social-network-messaging`

This specification governs the shared Flutter/Dart capability design and the three independent native presentation hosts and module skeletons that consume [`project-social-network-laravel-api`](https://github.com/liberusoftware/project-social-network-laravel-api).

| Target surface | Host application skeleton | Capability module skeleton | Wayfinder & implementation runbook |
| --- | --- | --- | --- |
| Flutter mobile (`iOS` / `Android`) | [`project-social-network-mobile-flutter`](https://github.com/liberusoftware/project-social-network-mobile-flutter) | [`module-social-network-messaging-flutter`](https://github.com/liberusoftware/module-social-network-messaging-flutter) (`module_social_network_messaging_flutter`) | [mobile-flutter.md](../../wayfinders/mobile-flutter.md) · [FLUTTER.md](../../../guides/presentation/FLUTTER.md) · [catalog](../../../modules/skeletons/mobile-flutter.md) |
| Dart mobile (`iOS` / `Android`) | [`project-social-network-dart-mobile`](https://github.com/liberusoftware/project-social-network-dart-mobile) | [`module-social-network-messaging-dart-mobile`](https://github.com/liberusoftware/module-social-network-messaging-dart-mobile) (`module_social_network_messaging_dart_mobile`) | [dart-mobile.md](../../wayfinders/dart-mobile.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-mobile.md) |
| Dart desktop (`Linux` / `macOS` / `Windows`) | [`project-social-network-dart-desktop`](https://github.com/liberusoftware/project-social-network-dart-desktop) | [`module-social-network-messaging-dart-desktop`](https://github.com/liberusoftware/module-social-network-messaging-dart-desktop) (`module_social_network_messaging_dart_desktop`) | [dart-desktop.md](../../wayfinders/dart-desktop.md) · [DART.md](../../../guides/presentation/DART.md) · [catalog](../../../modules/skeletons/dart-desktop.md) |
| Shared product API backend | [`project-social-network-laravel-api`](https://github.com/liberusoftware/project-social-network-laravel-api) | [API plan](../api/social-network-messaging.md) · [Core plan](../core/social-network-messaging.md) | [LARAVEL-API-BACKENDS.md](../../../guides/LARAVEL-API-BACKENDS.md) |

### Feature and aspect matrix across mobile and desktop hosts

| Feature / aspect | Mobile touch & adaptive widgets (`-mobile-flutter`, `-dart-mobile`) | Desktop windowed, keyboard & export workflows (`-dart-desktop`) | Typed Dart DTO, repository & offline/conflict recovery |
| --- | --- | --- | --- |
| **Conversations** | Adaptive mobile cards/sheets for `conversations` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `conversations` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Membership** | Adaptive mobile cards/sheets for `membership` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `membership` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Delivery/read state** | Adaptive mobile cards/sheets for `delivery/read state` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `delivery/read state` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Attachments** | Adaptive mobile cards/sheets for `attachments` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `attachments` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Requests** | Adaptive mobile cards/sheets for `requests` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `requests` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Safety** | Adaptive mobile cards/sheets for `safety` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `safety` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |
| **Retention** | Adaptive mobile cards/sheets for `retention` with safe areas, semantic labels, platform back navigation, and foreground state refresh. | Resizable desktop split-pane/table workspace for `retention` with keyboard focus traversal, shortcuts, multi-window draft safety, and authorized print/export. | Checked Dart `fromJson` DTOs over `project-social-network-laravel-api`; platform-secure token storage, account-isolated draft queues, and idempotent retry/conflict handling. |

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
