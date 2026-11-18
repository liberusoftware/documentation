# Social Network: Social Network Messaging API

<!-- source-reconciliation:start -->
**Source reconciliation:** [design-to-source map](../SOURCE-MAPPING.md#social-network-messaging). Observed identity: [`liberusoftware/module-social-network-messaging-api`](../../../modules/source/liberusoftware--module-social-network-messaging-api.md). Requirements and examples below describe the target design; the linked source reference records observed metadata and code, and does not certify release availability or implemented parity.
<!-- source-reconciliation:end -->

## Canonical one-to-one API module specification

**Proposed API design identifier:** `module-social-network-social-network-messaging-api`<br>
**Matching domain module:** `social-network-messaging`  
**Application:** Social Network  
**Source feature:** [Social Network Messaging](../features/social-network-messaging.md)  
**Architecture:** [API.md](../../../architecture/API.md) · [MODULES.md](../../../architecture/MODULES.md) · [TESTING.md](../../../standards/TESTING.md)

## 1. Purpose and ownership

This optional API presentation package exposes approved HTTP operations for the Social Network Messaging domain module. It presents exactly one independent module, delegates all authoritative behavior to that module's public actions/queries/policies, and contains no other module's API logic.

The domain capability includes:

- Conversations
- Membership
- Delivery/read state
- Attachments
- Requests
- Safety
- Retention

Installation does not expose every capability automatically. The host application selects this package, API version, audiences, route groups, and operations in its API manifest.

## 2. Contract design

- Publish an OpenAPI 3.1 fragment with stable operation IDs, schemas, examples, scopes, errors, pagination, rate limits, idempotency, and deprecation metadata.
- Choose the route namespace through the host's reviewed API contract; observed source prefixes below take precedence over repository/design-name guesses.
- Represent resources through explicit API DTOs/resources rather than automatic Eloquent serialization.
- Use lowercase kebab-case paths, snake_case JSON fields, opaque identifiers, ISO 8601 timestamps, explicit money objects, and RFC 9457 Problem Details errors.
- Compatible additions remain within the major version; removals or semantic breaks require a new major version or approved migration path.

## 3. Endpoint examples

**Contract status:** use the observed source below for current route/handler/schema evidence. The surrounding module scope is a target design; its feature labels are not request field names. Do not generate a create/update/delete payload or final URL by mechanically copying the design identifier.

### Product API backend and client integration

This module API adapter is composed into [`project-social-network-laravel-api`](https://github.com/liberusoftware/project-social-network-laravel-api), the shared Laravel HTTP backend for independent web, mobile, and desktop clients ([backend guide](../../../guides/LARAVEL-API-BACKENDS.md) · [repository map](../../REPOSITORIES.md#laravel-applications)).

| Consuming client surface | Host repository | Module adapter plan | Transport and auth contract |
| --- | --- | --- | --- |
| Next.js React | [`project-social-network-next-react`](https://github.com/liberusoftware/project-social-network-next-react) | [Next.js plan](../nextjs/social-network-messaging.md) | Server Component / Route Handler / BFF or Sanctum SPA with `no-store` private reads |
| Nuxt 4 Vue | [`project-social-network-nuxt-vue`](https://github.com/liberusoftware/project-social-network-nuxt-vue) | [Nuxt plan](../nuxt/social-network-messaging.md) | Nitro SSR / BFF or Sanctum SPA with actor/tenant-scoped `useFetch` keys |
| React Native Expo | [`project-social-network-mobile-react`](https://github.com/liberusoftware/project-social-network-mobile-react) | [React Native plan](../react-native/social-network-messaging.md) | Typed client with Keychain/Keystore token storage, PKCE/Sanctum, and idempotent retries |
| Flutter mobile | [`project-social-network-mobile-flutter`](https://github.com/liberusoftware/project-social-network-mobile-flutter) | [Flutter plan](../flutter/social-network-messaging.md) | Typed Dart DTOs and platform-secure credentials on iOS and Android |
| Dart mobile & desktop | [`project-social-network-dart-mobile`](https://github.com/liberusoftware/project-social-network-dart-mobile) · [`project-social-network-dart-desktop`](https://github.com/liberusoftware/project-social-network-dart-desktop) | [Flutter & Dart plan](../flutter/social-network-messaging.md) | Separate mobile and desktop native hosts consuming the same versioned `/api/v1` contract |

### Feature-to-API capability and operation matrix

| Feature / aspect | HTTP query and command intent | DTO allowlist, concurrency, and error contract |
| --- | --- | --- |
| **Conversations** | Expose authorized query/read projection and explicit domain transition command for `conversations` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Membership** | Expose authorized query/read projection and explicit domain transition command for `membership` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Delivery/read state** | Expose authorized query/read projection and explicit domain transition command for `delivery/read state` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Attachments** | Expose authorized query/read projection and explicit domain transition command for `attachments` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Requests** | Expose authorized query/read projection and explicit domain transition command for `requests` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Safety** | Expose authorized query/read projection and explicit domain transition command for `safety` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |
| **Retention** | Expose authorized query/read projection and explicit domain transition command for `retention` delegating to the core module boundary. | Explicit `snake_case` resource/request DTOs; `Idempotency-Key` for retryable writes, `If-Match` for mutable state, and RFC 9457 Problem Details (`401`/`403`/`409`/`412`/`422`/`429`). |

| Boundary | Observed identity and implementation reference |
| --- | --- |
| Source package | [liberusoftware/module-social-network-messaging-api](../../../modules/source/liberusoftware--module-social-network-messaging-api.md) |
| Source package | [liberusoftware/module-social-network-messaging](../../../modules/source/liberusoftware--module-social-network-messaging.md) |

### Observed route declarations

These are literal excerpts, not runnable standalone route files or expanded final URLs. Read group middleware/prefixes, provider loading and the host route configuration together. Authentication middleware alone does not establish the controller/domain permission policy.

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

### Observed controller entry points

The signatures identify request handlers to review; their argument names are not complete JSON schemas. Read their request validation, actor/tenant resolution, policy, serialization and error paths before writing a client.

| Controller source | Public handler signatures |
| --- | --- |
| [MessagingController.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging-api/src/Http/Controllers/MessagingController.php) | `public function conversation(Request $request, GetProfile $get, CreateConversation $create): JsonResponse`<br>`public function index(Request $request, GetProfile $get, ListConversations $list): JsonResponse`<br>`public function unreadCount(Request $request, GetProfile $get, UnreadMessageCount $count): JsonResponse`<br>`public function show(string $conversation, Request $request, GetProfile $get, GetConversation $view): JsonResponse`<br>`public function messages(string $conversation, Request $request, GetProfile $get, GetConversation $view): JsonResponse`<br>`public function message(string $conversation, Request $request, GetProfile $get, SendMessage $send): JsonResponse`<br>`public function reaction(string $conversation, Message $message, Request $request, GetProfile $get, AddReaction $add): JsonResponse`<br>`public function removeReaction(string $conversation, Message $message, string $emoji, Request $request, GetProfile $get, RemoveReaction $remove): JsonResponse`<br>`public function typing(string $conversation, Request $request, GetProfile $get): JsonResponse`<br>`public function read(string $conversation, Request $request, GetProfile $get, MarkConversationRead $read): JsonResponse`<br>`public function destroyMessage(string $conversation, string $message, Request $request, GetProfile $get, DeleteMessage $delete): JsonResponse`<br>`public function addParticipant(string $conversation, Request $request, GetProfile $get, AddParticipant $add): JsonResponse`<br>`public function removeParticipant(string $conversation, string $profile, Request $request, GetProfile $get, RemoveParticipant $remove): JsonResponse` |

### Observed domain queries, actions, and storage models

API controllers delegate to these observed core domain entry points and serialize only allowlisted DTO fields rather than raw storage models.

| Core action / service source | Observed signatures |
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
| [UnreadMessageCount.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Actions/UnreadMessageCount.php) | `public function handle(Profile $profile): int` |
| [MessagingAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Contracts/MessagingAuthorizer.php) | `public function create(Profile $actor): void`<br>`public function send(Profile $actor): void` |

| Core storage model | Observed fillable fields (review for DTO allowlist) |
| --- | --- |
| [Conversation.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Models/Conversation.php) | `id`, `created_by_profile_id`, `state`, `title` |
| [Message.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Models/Message.php) | `id`, `conversation_id`, `sender_profile_id`, `body`, `encrypted_body`, `encryption_key_id`, `state`, `attachments` |
| [MessageReaction.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Models/MessageReaction.php) | `id`, `message_id`, `conversation_id`, `profile_id`, `emoji` |

A client example is valid only after its exact request/response contract is established. Record required/nullable fields, business units, allowed values, operation identity/concurrency support, result/pagination envelope and recovery. An `Idempotency-Key` or `If-Match` example does not establish server support by itself.

## 4. OpenAPI schema

The matched source contains these machine-readable contract/schema files. Verify their version and parity with handlers; file presence does not prove deployed compatibility or a passing validation run.

- [openapi/v1/social-network-messaging.yaml](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging-api/openapi/v1/social-network-messaging.yaml)

For the target contract, define stable operation IDs, explicit request/resource/collection/error schemas, allowed audiences/scopes, actor/tenant resolution, field sensitivity, pagination/filter limits, concurrency and retry semantics. Use the real manifest identity and actual route namespace, not a guessed repository-derived package or path.

Validate/bundle the fragment, check supported-version compatibility and generate clients only from the reviewed contract. Retain the source/schema commit or release in client compatibility notes. See the [API architecture](../../../architecture/API.md), [source mapping](../SOURCE-MAPPING.md#social-network-messaging), and [Composer](../../../guides/COMPOSER.md)/[npm](../../../guides/NPM.md) guides.

## 5. Audience and operation matrix

| Audience                       | Default exposure                    | Required controls                                                                      |
| ------------------------------ | ----------------------------------- | -------------------------------------------------------------------------------------- |
| Public/anonymous               | Disabled unless explicitly required | Enumeration resistance, strict rate limits, field minimization, abuse controls         |
| Authenticated customer/partner | Explicit allowlist                  | Tenant/resource ownership, purpose-specific scopes, field policy                       |
| Staff/administrator            | Explicit allowlist                  | Role/permission policy, tenant context, recent authentication for risky actions, audit |
| Service/integration client     | Explicit allowlist                  | Service identity, least-privilege scopes, expiry/rotation, idempotency, quotas         |

Every exposed operation must map to one audience, domain query/action, permission/scope, request/response schema, rate limit, idempotency/concurrency policy, audit event, and test set. Unmapped operations fail CI.

## 6. Implementation strategy

- Keep routes, controllers/handlers, requests, API resources, OpenAPI fragments, and transport tests in this API package.
- Validate shape at the request boundary and enforce authoritative invariants again in the domain action.
- Resolve tenant and actor context from trusted authentication/application routing; never grant context from a caller-supplied tenant identifier alone.
- Authorize field visibility as well as record/action access, and return concealment-safe errors where enumeration is a risk.
- Use idempotency keys for retryable writes, ETags/`If-Match` for relevant concurrent updates, and asynchronous operation resources for slow/bulk/provider-dependent work.
- Compose cross-module workflows in the application layer; do not query or mutate another module's private storage from this API package.

## 7. Security, resilience, and observability

- Threat-model authentication, authorization, tenant isolation, mass assignment, object references, abusive queries, uploads/downloads, webhooks, and sensitive data.
- Bound pagination, filters, includes, payloads, batch sizes, timeouts, and retry budgets.
- Redact credentials and protected data from logs and errors while recording request, correlation, API/module/version, tenant, principal, operation, status, latency, rate-limit, and idempotency outcomes.
- Define availability, latency, error-rate and queued-operation objectives plus alerts and recovery/reconciliation runbooks.

## 8. Verification strategy

- Lint OpenAPI, validate examples, detect implementation drift and breaking changes, and reject path/schema/operation-ID collisions during application aggregation.
- Test every operation for allowed, unauthenticated, wrong-tenant, insufficient-scope, insufficient-permission, hidden-field, invalid, missing, duplicate, stale, concurrent, throttled, and failure/recovery paths as applicable.
- Test pagination, filtering, sorting, includes, dates, money, identifiers, enums, idempotency, ETags, async operations, bulk partial failure, and stable Problem Details.
- Add one-to-one architecture tests proving this package depends on and presents only `social-network-messaging`.
- Run independent installation, minimum/current compatibility, security, performance, generated-client smoke, and representative host-composition tests.
- Run Pest 5 with meaningful owned PHP targeting 100% line coverage; coverage complements contract, mutation, security, and failure assertions.

## 9. Definition of done

- The package name, manifest, Composer dependency, namespace, route prefix, and OpenAPI ownership all match `social-network-messaging`.
- The audience/operation matrix is complete, least-privilege, documented, and enforced in CI.
- Schemas, implementation, examples, errors, SDK/client evidence, and documentation agree.
- Authorization, tenant/field isolation, idempotency/concurrency, limits, audit, observability, compatibility, and recovery tests pass.
- The API fragment aggregates without collisions and the independent package can be installed, tested, versioned, upgraded, and removed safely.
