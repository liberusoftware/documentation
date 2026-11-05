# liberusoftware/module-social-network-messaging: observed package reference

**Evidence status:** extracted from tracked source at the commits below. This reference indexes declared metadata, source callables and persistence files. It does not establish a stable public API, implemented acceptance criteria, successful tests, registry availability or runtime safety.

Conversations, membership, message delivery, read state, requests, safety, attachments, and retention.

## Source locations

| Application | Actual directory | Commit | Reference variant | Test files |
| --- | --- | --- | --- | ---: |
| [social-network](../../projects/social-network/SOURCE-MODULES.md) | [social-network-messaging](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/composer.json) | `08bbc484b50f` | [Variant 1](#variant-1) | 2 |

Physical source locations: **1**. Reference variants: **1**. Compatibility symlinks are excluded as separate implementations. Reference variants also include tests, scripts and OpenAPI files, so they can be more granular than the runtime-only [shared comparison](../../architecture/SHARED-MODULE-COMPARISON.md).

Use the manifest identity above for resolution. A `module-...` repository or design identifier may differ. See the [Composer lifecycle guide](../../guides/COMPOSER.md), [npm lifecycle guide](../../guides/NPM.md) and [shared ownership guide](../../architecture/SHARED-MODULES.md).

## Variant 1

Representative: project-social-network-laravel-filament, `social-network-messaging`. Matching reference files in this variant are indexed once; the location table preserves every consuming application.

### Manifest and registration

| Property | Observed value |
| --- | --- |
| Composer name | `liberusoftware/module-social-network-messaging` |
| Composer version field | `0.1.2` |
| Package type | `liberu-module` |
| Module manifest name | `social-network-messaging` |
| Module version field | `0.1.2` |
| Category / layers | `"product"` |
| Manifest provider(s) | `"Liberu\\SocialNetwork\\Messaging\\MessagingServiceProvider"` |
| Composer Laravel provider registration | `[]` |
| default_enabled field | `true` |

The manifest default is not proof of deployment enablement. Providers, manifest schemas and registration mechanisms differ across packages; inspect the actual host resolver before adoption. Both Composer auto-discovery and module-manager registration may need review when both are declared.

Source metadata: [composer.json](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/composer.json) · [module.json](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/module.json).

**Declared capabilities:** social-network.messaging

**Declared features:** Conversations, Membership, Delivery and read state, Attachments, Unread counts, Requests, Safety, Retention

### Dependencies and namespace mapping

| Dependency | Constraint |
| --- | --- |
| `illuminate/database` | `^13.0` |
| `illuminate/events` | `^13.0` |
| `illuminate/support` | `^13.0` |
| `liberusoftware/module-social-network-profiles` | `^0.1` |
| `php` | `^8.5` |

PSR-4 mappings: `{"Liberu\\SocialNetwork\\Messaging\\": "src/"}`.

Module resolver requirements: `{"laravel": "^13.0", "packages": {"liberusoftware/module-social-network-profiles": "^0.1"}, "php": "^8.5"}`.

### Source entry points

The following paths identify contracts, actions, queries, policies, services and presentation code for review. Listed public methods are signature excerpts, not API schema or authorization guarantees. Resolve argument types/imports in the linked file and check the provider/call sites before invoking a class.

| Source file | Public method signatures observed |
| --- | --- |
| [src/Actions/AddParticipant.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Actions/AddParticipant.php) | `public function __construct(private MessagingAuthorizer $authorizer)`<br>`public function handle(Profile $actor, string $conversationId, Profile $participant): void` |
| [src/Actions/AddReaction.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Actions/AddReaction.php) | `public function __construct( private MessagingAuthorizer $authorizer, private Dispatcher $events, )`<br>`public function handle(Profile $profile, Message $message, string $emoji): MessageReaction` |
| [src/Actions/CreateConversation.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Actions/CreateConversation.php) | `public function __construct(private MessagingAuthorizer $authorizer)`<br>`public function handle(Profile $creator, ?string $title = null, array $participantIds = []): Conversation` |
| [src/Actions/DeleteMessage.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Actions/DeleteMessage.php) | `public function __construct(private MessagingAuthorizer $authorizer)`<br>`public function handle(Profile $actor, string $conversationId, Message $message): void` |
| [src/Actions/GetConversation.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Actions/GetConversation.php) | `public function handle(Profile $viewer, string $conversationId): Conversation` |
| [src/Actions/ListConversations.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Actions/ListConversations.php) | `public function handle(Profile $profile, int $limit = 25): Collection` |
| [src/Actions/MarkConversationRead.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Actions/MarkConversationRead.php) | `public function handle(Profile $profile, string $conversationId): void` |
| [src/Actions/RemoveParticipant.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Actions/RemoveParticipant.php) | `public function __construct(private MessagingAuthorizer $authorizer)`<br>`public function handle(Profile $actor, string $conversationId, Profile $participant): void` |
| [src/Actions/RemoveReaction.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Actions/RemoveReaction.php) | `public function __construct(private MessagingAuthorizer $authorizer)`<br>`public function handle(Profile $profile, Message $message, string $emoji): void` |
| [src/Actions/SendMessage.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Actions/SendMessage.php) | `public function __construct(private MessagingAuthorizer $authorizer, private Dispatcher $events)`<br>`public function handle(Profile $sender, string $conversationId, string $body, array $attachments = [], bool $encrypted = false): Message` |
| [src/Actions/UnreadMessageCount.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Actions/UnreadMessageCount.php) | `public function handle(Profile $profile): int` |
| [src/Contracts/MessagingAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Contracts/MessagingAuthorizer.php) | `public function create(Profile $actor): void`<br>`public function send(Profile $actor): void` |

Other non-legacy PHP sources: [src/Authorization/GateMessagingAuthorizer.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Authorization/GateMessagingAuthorizer.php) · [src/Events/MessageReactionAdded.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Events/MessageReactionAdded.php) · [src/Events/MessageSent.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Events/MessageSent.php) · [src/Events/UserTyping.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Events/UserTyping.php) · [src/MessagingServiceProvider.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/MessagingServiceProvider.php) · [src/Models/Conversation.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Models/Conversation.php) · [src/Models/Message.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Models/Message.php) · [src/Models/MessageReaction.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/src/Models/MessageReaction.php).

### Persistence and lifecycle evidence

Migrations/settings files are source history, not proof they were applied. Check existing tables, migration records, locks, backfills and recovery before adoption.

- [database/migrations/2026_08_24_080000_create_social_messaging_tables.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/database/migrations/2026_08_24_080000_create_social_messaging_tables.php)
- [database/migrations/2026_08_24_160000_create_social_message_reactions_table.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/database/migrations/2026_08_24_160000_create_social_message_reactions_table.php)
- [database/migrations/2026_08_25_000000_add_encryption_to_social_messages_table.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/database/migrations/2026_08_25_000000_add_encryption_to_social_messages_table.php)

### Verification and consumer use

Declared Composer scripts: `{"test": "pest", "test:coverage": "pest --coverage --min=100 --coverage-clover=coverage.xml", "test:feature": "pest tests/Feature", "test:parallel": "pest --parallel", "test:unit": "pest tests/Unit"}`.

Tracked files under `tests/`: **2**. Presence and counts do not establish assertions, coverage or a passing run.

- [tests/Pest.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/tests/Pest.php)
- [tests/Unit/PackageStructureTest.php](https://github.com/liberusoftware/project-social-network-laravel-filament/blob/08bbc484b50fc7e841a499375329c6de32614145/modules/social-network-messaging/tests/Unit/PackageStructureTest.php)

Before adoption, verify module enablement, clean consumer resolution, actor/tenant authorization, invalid input, duplicates/concurrency, migration compatibility and failure recovery for the actual call path. Use the owning application/package scripts and supported PHP/framework versions. This documentation extraction did not install, boot, test or release the package.
