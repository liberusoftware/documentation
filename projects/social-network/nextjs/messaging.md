# Messaging: Next.js presentation plan

<!-- nextjs-plan:generated -->

**Status:** proposed adapter, not an observed npm release. The source entry points below describe reviewed locations/signatures; screen, route and component decisions are implementation targets until the API and UI contracts are verified.

**Adapter group:** `liberusoftware/module-social-network-messaging`.

**Proposed design identifier:** `module-social-network-messaging-nextjs`. Confirm the actual npm scope/name, exports and peer versions before publishing.

## Scope and ownership

The [domain specification](../features/messaging.md) owns the intended capability scope. Laravel and the owning modules remain authoritative for permissions, validation, state changes and persistence. The Next.js application owns public routes, session integration and deployment; the adapter contributes components and transport helpers.

This plan is the shared documentation home for **2 existing design spellings/consumer scopes** that map to the same core identity. They reference one adapter plan rather than create competing implementations. Source variants still need compatibility review before a common release.

| Boundary | Observed package reference |
| --- | --- |
| Core | [liberusoftware/module-social-network-messaging](../../../modules/source/liberusoftware--module-social-network-messaging.md) |
| API | [liberusoftware/module-social-network-messaging-api](../../../modules/source/liberusoftware--module-social-network-messaging-api.md) |

## Module surfaces and component contracts

| Capability in the domain scope | Next.js composition target |
| --- | --- |
| Conversations | A focused authorized view or workflow section for conversations; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Membership | A focused authorized view or workflow section for membership; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Delivery/read state | A focused authorized view or workflow section for delivery/read state; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Attachments | A focused authorized view or workflow section for attachments; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Requests | A focused authorized view or workflow section for requests; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Safety | A focused authorized view or workflow section for safety; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |
| Retention | A focused authorized view or workflow section for retention; define the exact read DTO, permitted command, validation and recovery state from the owning API before implementation. |

Use a list/workspace view only where a domain query exists, a detail/evidence view for an authorized record, and one command form per supported transition. Prefer API-returned permitted actions and explicit field allowlists. Contract/configuration modules can be composed into another workspace instead of receiving artificial resource routes.

## Query and command integration

Observed action/service candidates for the transport review are below. A service method is not automatically a command, an authorized public API or a safe server action; inspect its implementation and calling policies.

| Source action/service | Signatures |
| --- | --- |
| [AddParticipant.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Actions/AddParticipant.php) | `public function handle(Profile $actor, string $conversationId, Profile $participant): void` |
| [AddReaction.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Actions/AddReaction.php) | `public function handle(Profile $profile, Message $message, string $emoji): MessageReaction` |
| [CreateConversation.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Actions/CreateConversation.php) | `public function handle(Profile $creator, ?string $title = null, array $participantIds = []): Conversation` |
| [DeleteMessage.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Actions/DeleteMessage.php) | `public function handle(Profile $actor, string $conversationId, Message $message): void` |
| [GetConversation.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Actions/GetConversation.php) | `public function handle(Profile $viewer, string $conversationId): Conversation` |
| [ListConversations.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Actions/ListConversations.php) | `public function handle(Profile $profile, int $limit = 25): Collection` |
| [MarkConversationRead.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Actions/MarkConversationRead.php) | `public function handle(Profile $profile, string $conversationId): void` |
| [RemoveParticipant.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Actions/RemoveParticipant.php) | `public function handle(Profile $actor, string $conversationId, Profile $participant): void` |
| [RemoveReaction.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Actions/RemoveReaction.php) | `public function handle(Profile $profile, Message $message, string $emoji): void` |
| [SendMessage.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Actions/SendMessage.php) | `public function handle(Profile $sender, string $conversationId, string $body, array $attachments = [], bool $encrypted = false): Message` |
| [UnreadMessageCount.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Actions/UnreadMessageCount.php) | `public function handle(Profile $profile): int` |

The server transport resolves the authenticated actor and tenant/entity membership, calls a fixed configured Laravel origin and validates the response DTO. Every server action/route handler authorizes its invocation; Laravel independently authorizes its operation. Browser input can select a scope but cannot establish membership or change the trusted API origin.

### Record-field review

These are observed storage models and fillable field names, not a browser DTO schema. Review sensitivity, computed values and owner policy; use an explicit API allowlist rather than exposing every model field.

| Source model | Observed fillable fields |
| --- | --- |
| [Conversation.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Models/Conversation.php) | `id`, `created_by_profile_id`, `state`, `title` |
| [Message.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Models/Message.php) | `id`, `conversation_id`, `sender_profile_id`, `body`, `encrypted_body`, `encryption_key_id`, `state`, `attachments` |
| [MessageReaction.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Models/MessageReaction.php) | `id`, `message_id`, `conversation_id`, `profile_id`, `emoji` |

### Route source evidence

The following are literal declaration excerpts. They are not expanded final URLs: group prefixes, middleware, provider registration and host routing must be read together. Target API examples elsewhere do not override these source contracts.

[modules/social-network-messaging-api/routes/api.php](https://github.com/liberusoftware/social-network-laravel/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging-api/routes/api.php)

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

## Server/client and React reuse

Keep API credentials and session forwarding in server-only exports. A Server Component may load authorized serializable data and compose a Client Component for interaction. Put ordinary event callbacks inside the client boundary; server-to-client props must follow the framework serialization/action rules.

Share framework-independent React cards, tables, labels, formatting and field primitives with Inertia. Keep `next/link`, Next.js navigation, server actions and cache invalidation in this adapter, and Inertia visits, page props and redirects in its wrapper. Reuse domain/API DTOs without importing PHP models or another application's private frontend state.

## State, failures and verification

| Situation | User-facing behavior and integration requirement |
| --- | --- |
| Loading or empty authorized query | Accessible progress/empty copy; preserve filters and avoid displaying stale records from another scope |
| Expired session or denied permission | Reauthenticate or show a scoped denial; discard protected cached data and do not retry as a broader service identity |
| Invalid command input | Preserve safe draft values, announce field errors and use the authoritative API validation outcome |
| Stale record / concurrent change | Reload/review the current version; do not overwrite silently or invent an ETag contract the API does not support |
| Timeout after a write | Query the operation/current record when supported before retrying; an idempotency key works only if the owning API actually stores/enforces it |
| Long-running or partly failed operation | Show a durable operation reference, progress, last error and a permitted retry/recovery action |

Start authenticated reads with explicit no-store behavior until a reviewed tenant/permission-aware caching policy exists. Refresh affected read models after confirmed mutations; pending transport acceptance is not a completed business transition. Recheck access for evidence/export downloads.

Verify the actual supported query/command journeys, invalid and denied paths, tenant switching, stale state, retry recovery, keyboard/focus behavior and secret exclusion from browser bundles. Build/test the packed adapter in a clean consuming Next.js application using its declared versions and API contract. No npm package or application suite was executed by this plan generator.

See the [Next.js standard](../../../standards/NEXTJS.md), [npm lifecycle guide](../../../guides/NPM.md), [API architecture](../../../architecture/API.md), and [shared ownership guide](../../../architecture/SHARED-MODULES.md).
